# 06 — Evidence Model, Chain of Custody & Disposition

> "Evidence over assumption. Every finding is supported by evidence." — sleuthforensics.in/about
>
> The platform's job is to make that statement *structurally true* rather than aspirational.

---

## 1. The evidence ladder

The brief asks for a clear distinction between raw evidence, working copies, processed evidence, analytical artefacts, screenshots/logs, findings and reports. Model this as a **provenance ladder**: every item declares its parent, so any statement in a report can be walked back to the thing it came from.

```
  L0  SOURCE              The original. A device, an account, a system, a person's
                          handover. Never analysed directly. Often never in Sleuth's
                          possession at all — only referenced.
       │  acquire  (hash, verify, custody record opened)  ⟨ CUSTODY GATE ⟩
       ▼
  L1  RAW EVIDENCE        Forensic image, memory dump, log export, collected file set.
                          Immutable. Read-only. Hashed at acquisition and verified.
       │  derive  (verify parent hash first)
       ▼
  L2  WORKING COPY        The copy that is actually worked on. Its own hash. Provably
                          derived from a specific L1 item. Disposable and re-derivable.
       │  process  (tool + version + parameters recorded)
       ▼
  L3  PROCESSED EVIDENCE  Parsed, normalised, carved, indexed, decoded output.
                          Records the tool and version that produced it — so it can
                          be reproduced or re-run when a tool is later found faulty.
       │  analyse
       ▼
  L4  ANALYTICAL ARTEFACT Timelines, IOC sets, attack-path graphs, correlation matrices,
                          diff sets. Sleuth's analytical work product.
       │
  L5  CONTEMPORANEOUS     Screenshots, tool logs, session recordings, examiner notes.
      RECORD              Captured *while* working. Attaches at any level. This is what
                          shows the work was done as described.
       │  assert
       ▼
  L6  FINDING             A claim. MUST link to ≥1 item at L1–L5. A finding whose
                          evidence links are all removed becomes invalid, not merely
                          flagged — it cannot be included in a report.
       │  communicate
       ▼
  L7  REPORT              The client-facing statement. Cites findings, which cite
                          evidence, which traces to source.
```

Reading the ladder upward from any sentence in a delivered report to the physical device it came from is the single capability that distinguishes a forensic platform from a project tracker. Every link in that chain is a stored relationship, not a convention.

### 1.1 An important scoping consequence

Only L1 and L2 are large binary objects. L3–L5 are mostly structured data and modest files. **The platform does not need to store forensic images to deliver most of this value** — it needs to *register* them, hash them, and track their custody and location. See Decision D1 in `15-assumptions-and-open-questions.md`; the recommendation is register-first, managed-storage later.

---

## 2. The evidence record

| Field | Notes |
|---|---|
| `evidence_id` | Human-usable, engagement-scoped, monospace-rendered: `ENG-2026-0141-E007` |
| `level` | L0–L5 |
| `parent_evidence_id` | Required for L2–L4. This is the provenance chain. |
| `source_description` | "Dell Latitude 5420, S/N ABC123, recovered from Finance, 3rd floor" |
| `source_type` | Host · Mobile device · Removable media · Cloud account · Log source · Network capture · Document · Interview record · Physical item |
| `client_asset_ref` | Links to the client's own asset identifier where one exists |
| `description` | What it is, in plain language |
| `acquisition_datetime` + `timezone` | Timezone is mandatory. Timeline work across sources fails silently without it. |
| `acquisition_method` | Physical · Logical · File-system · Targeted collection · Memory capture · Cloud API export · Live response · Manual export |
| `acquisition_tool` + `tool_version` | References the tool catalogue. Version matters when a tool is later found defective. |
| `examiner` | The person, not the team |
| `write_blocker_used` | Boolean + method. Required for physical acquisitions. |
| `hash_algorithm` | SHA-256 default; SHA-1/MD5 permitted only as *additional* values for legacy tool compatibility, never alone |
| `acquisition_hash` | Computed at acquisition |
| `verification_hash` + `verified_at` + `verified_by` | Computed independently after acquisition |
| `integrity_status` | `Verified` · `Verification pending` · **`FAILED`** · `Not applicable` |
| `size_bytes`, `file_count` | Sanity-check values |
| `storage_location` | Where it physically/logically is — evidence safe, lab NAS, encrypted volume, platform store |
| `storage_medium_id` | Which drive/safe/container, for physical retrieval |
| `classification` | Client Confidential · Restricted · Privileged · Personal Data |
| `contains_personal_data` | Drives retention and disposition rules |
| `legal_hold` | Blocks disposition entirely while set |
| `retention_until` | Calculated at close from policy + hold |
| `disposition_status` | Retained · Return scheduled · Returned · Destruction scheduled · Destroyed · **Overdue** |

### 2.1 Integrity failure is a system event, not a field update

If `verification_hash ≠ acquisition_hash`:

1. `integrity_status = FAILED`, immediately and irreversibly for that record.
2. Every derived item (L2–L4) is marked **provenance-suspect**.
3. Every finding referencing any affected item is flagged and **removed from the report draft**.
4. The Evidence Integrity Gate blocks.
5. The Reviewer and Engagement Manager are notified. Work does not continue quietly.
6. The event is permanently part of the engagement record and appears in the report's limitations.

No role can clear a failed integrity status. A new acquisition can be taken; the failure itself remains on the record. This is deliberate: the value of an integrity check is entirely in the fact that it cannot be talked out of.

---

## 3. Chain of custody

Custody is an **append-only event stream** per evidence item. Events are never edited or deleted.

| Event | Captured |
|---|---|
| `ACQUIRED` | who, when, where, method, tool+version, hash, write-blocker |
| `VERIFIED` | who, when, hash compared, result |
| `TRANSFERRED` | from → to, when, method (hand carry / courier / encrypted transfer), container/seal number, both parties acknowledged |
| `RECEIVED` | receiver, when, seal intact yes/no, condition notes |
| `ACCESSED` | who, when, purpose, duration, read or copy |
| `COPY_DERIVED` | parent, child, method, hash of child |
| `PROCESSED` | tool, version, parameters, output reference |
| `STORED` | location, medium, container, access controls |
| `SEALED` / `UNSEALED` | seal number, witness where applicable |
| `HOLD_APPLIED` / `HOLD_RELEASED` | authority, reason, reference |
| `RETURNED` | recipient, their identity verification, acknowledgement reference |
| `DESTROYED` | method, who performed it, **who witnessed it**, certificate reference |

### 3.1 Gap detection

A custody chain is valid when every interval between acquisition and the present is attributable to a named, recorded holder. The system computes this continuously rather than trusting the record to look complete:

```
GAP DETECTED — ENG-2026-0141-E007
  TRANSFERRED  2026-09-14 16:40  P. Nair → courier (AWB 88213)
  RECEIVED     2026-09-16 09:05  S. Kulkarni, seal intact
  ⚠ 40h 25m unattributed while in transit.
    Courier tracking reference required, or the gap must be
    documented as a limitation before this item supports a finding.
```

A detected gap does not delete evidence. It becomes a known, documented limitation that flows into the report. Pretending gaps do not happen is what makes a record indefensible; recording them honestly is what makes it survivable.

### 3.2 The custody strip

Every place an evidence item appears in the UI carries a compact, always-visible integrity strip. It is not behind a tab, because the one thing a consultant must never have to go looking for is whether the thing they are about to rely on is sound.

```
ENG-2026-0141-E007   L1 RAW   ● VERIFIED   SHA-256 4f2a…c81d
custody: 6 events · complete · holder: S. Kulkarni · evidence safe A-3
```

---

## 4. Access history

Custody answers *who held it*. Access answers *who looked inside it*. Both are required, and they are different questions.

Every read, preview, download or export of evidence content records: user, role, timestamp, engagement, purpose (selected, not free text), item, action, IP and device, and whether it was part of a bulk operation. Bulk export requires Engagement Manager approval and is always notified.

This log is a deliverable in its own right. When a client or counsel asks "who at Sleuth has seen this?", the answer should take seconds and be complete.

---

## 5. Disposition

The brief calls for evidence return/destruction at closure. In practice this is the obligation most likely to be quietly skipped, because by then everyone has moved on — and it is also the one that creates a growing liability.

```
CLOSURE
   │
   ├─ legal_hold set? ──yes──► RETAIN. Disposition blocked. Review date set.
   │                            Hold authority and reference recorded.
   │
   ├─ client instruction?
   │     ├─ RETURN     → schedule · verify recipient identity · transfer with seal
   │     │                · obtain signed acknowledgement · record RETURNED
   │     ├─ DESTROY    → schedule · method per policy · performed by + WITNESSED by
   │     │                · certificate generated · record DESTROYED
   │     └─ RETAIN     → retention period + justification + review date
   │                      · re-consent requirement if it holds personal data
   │
   └─ no instruction  → BLOCKS THE CLOSURE GATE. The engagement cannot close.
```

**Standing rules**

- Disposition is authorised by the Engagement Manager only, and is always a logged privileged action.
- Destruction requires a **witness** who is not the person performing it.
- Destruction of an item **does not delete its record**. The evidence record, its hashes, its full custody chain and its destruction certificate remain permanently. What is destroyed is the content, never the provenance.
- Derived items follow their parent unless separately held — and the system enumerates them so nothing is missed.
- Overdue disposition is a standing item on the Oversight dashboard, because an unreturned client hard drive sitting in a safe eighteen months after closure is a real liability, not a housekeeping detail.

---

## 6. Evidence for non-forensic archetypes

Custody applies fully to A3. The other archetypes still need evidence, with proportionate handling:

| Archetype | What counts as evidence | Custody |
|---|---|---|
| **A1** | Documents received, interview records, configuration exports, screenshots, observation notes | Not required. But **every maturity rating must cite its source** — the A1 equivalent of the evidence link, checked at the Evidence Sufficiency gate. An unsourced maturity score is an assumption wearing a number. |
| **A2** | Tool output, request/response captures, PoC artefacts, screenshots, command logs | Light: retained, hashed at collection, held for the retention period so a disputed finding can be reproduced. No transfer chain. |
| **A3** | Full ladder | **Mandatory, gating** |
| **A4** | Monitoring output, screenshots of exposures, cycle snapshots | Light; snapshot retention so a "this was exposed on this date" claim is supportable |

A2's retention requirement deserves a note. When a client disputes a finding three months after delivery — "that was never exploitable" — the captured request/response pair settles it in a minute. Without it, Sleuth's credibility rests on a consultant's recollection.

---

## 7. What this model is not

It is deliberately **not** a forensic analysis tool. It does not parse images, run carving, or replace the examiner's toolkit. It is the record of *what was acquired, by whom, how, where it is, who touched it, what was derived from it, and what was concluded* — the layer that makes the analysis defensible and that no forensic suite provides across engagements.
