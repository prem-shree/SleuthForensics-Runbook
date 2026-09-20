# 22 — Core Spine Specification

> **Status — Draft / Needs SME Validation.** Provenance: `PROPOSED` (structure) and
> `INDUSTRY-PRACTICE` (method), never `SLEUTH-SUPPLIED`. Nothing here is confirmed Sleuth practice.

The ten shared modules every one of the 20 engagement types inherits. **Written once, referenced
everywhere.** This is the payload of the "change once" guarantee in `20-shared-module-inheritance.md`.

**59 procedures.** Higher than the ~35 I estimated earlier — specifying it properly surfaced work
that a summary hid, particularly in authorisation, evidence and closure.

---

## In plain terms

Whatever the job — a penetration test, a forensic examination, a compliance review — about 60% of
the work is the same: qualify the client, get the paperwork signed, confirm you're allowed to start,
ask the right questions, record what you did, get it reviewed, send it out, and close properly.

That common 60% lives here, in one place. When Sleuth improves how it handles evidence, it is edited
once and every engagement type gets the improvement.

---

## Reading the specification

| Column | Meaning |
|---|---|
| **ID** | Stable reference. Runbooks and extension points cite these |
| **Procedure** | What it is called |
| **Objective / key steps** | What it achieves and how |
| **Records** | What must exist afterwards. *This is the audit trail* |
| ⟨ ⟩ | A gate evaluation |
| ⊗ | A stop condition |
| ▲ | An escalation |
| ✋ | An approval requirement |
| ⟪slot⟫ | A declared extension point — where archetype/service modules inject |

---

## `core.intake` — Phase 0, Enquiry & Triage

| ID | Procedure | Objective / key steps | Records |
|---|---|---|---|
| `IN-01` | Record enquiry | Capture the enquiry against the contact-form schema: name, company, work email, phone, area of interest, urgency, message *(`SITE-DERIVED` field set)* | Enquiry record, source, received timestamp |
| `IN-02` | Conflict of interest check | Check the prospective client, and any named adverse party, against existing and past engagements. ⊗ if Sleuth acts for an opposing party | Check performed, by whom, outcome, basis |
| `IN-03` | Client identity verification | Confirm the enquirer is who they claim and is connected to the organisation they name. For individuals, confirm identity proportionately | Method used, evidence seen, verified by |
| `IN-04` | Urgency triage | Route by the four urgency values. "Urgent — Active Incident" branches immediately to the emergency path *(`core.authorisation` AU-07)* | Urgency assigned, rationale, routing decision |
| `IN-05` | Engagement type selection | Map the enquiry to an engagement type. Where the client selected "Other / Not Sure", run the Service Selection decision tree | Type selected, decision path, who decided |
| `IN-06` | Qualification decision | Qualify in or out against capability, capacity, conflict and risk appetite. ▲ Management for declines on risk grounds | Decision, reason, decided by. **Declines are retained** |

> **Why declines are retained.** A record of what Sleuth turned away and why is valuable — for
> pattern-spotting, for consistency, and because a declined enquiry occasionally comes back.

---

## `core.commercial` — Phase 1, Qualification & Commercials

| ID | Procedure | Objective / key steps | Records |
|---|---|---|---|
| `CM-01` | NDA issue & execution | Issue from the controlled template. Mutual or one-way. ⚠ Template `legal_review_status` shown | Document instance, template version, signatories, roles, execution date |
| `CM-02` | Master agreement | For repeat clients, once per client rather than per engagement. Skipped for `client_type = Individual` | MSA instance, validity period |
| `CM-03` | Scope-to-SOW drafting | Draft the Statement of Work from the scope definition. Variables resolved from engagement data, not retyped | SOW draft, variable resolution, scope reference |
| `CM-04` | Commercial approval | ✋ Internal approval of commercial terms before issue | Approver, date, terms approved |
| `CM-05` | Engagement creation & team assignment | Create the engagement record. Assign manager and team with roles and date ranges | Engagement ID, team membership with effective dates |
| `CM-06` | Contact & distribution register | Record client contacts, their roles, who may authorise, who receives reports, **and who must be excluded** | Contact records, authority flags, exclusions with reason |

> `CM-06`'s exclusion flag matters in investigations: the subject of an internal investigation may be
> a normal day-to-day contact for that client. Recording the exclusion once prevents a serious
> disclosure error at delivery.

---

## `core.authorisation` — Phase 2

The most consequential module in the spine.

| ID | Procedure | Objective / key steps | Records |
|---|---|---|---|
| `AU-01` | Define scope | Enumerate in-scope assets **and explicitly out-of-scope assets with reasons**. Classify each: environment (prod/staging/dev/unknown), ownership (client/third-party/SaaS), criticality, fragility. ⟪scope_extension⟫ | Asset schedule, per-asset classification, exclusions with reasons |
| `AU-02` | Verify signatory authority | Identify who will sign, their role, **and how their authority to give that authorisation was verified**. A signature from someone without authority offers no protection | Signatory, role, verification method, verified by, date |
| `AU-03` | Letter of Authorisation | Issue and execute. Records authorised scope, prohibited actions, validity dates. ⚠ Expiry re-blocks the gate automatically | LoA instance, template version, validity window, scope reference |
| `AU-04` | Third-party authorisation | Where assets are not client-owned, obtain authorisation from the owner or provider, and check provider testing policy. ⊗ any third-party asset without authorisation is removed from scope | Per-asset authorisation status, evidence, provider policy check |
| `AU-05` | Emergency contacts | Record Sleuth-side and client-side contacts, including out-of-hours numbers. Confirm reachability, do not assume it | Contacts both sides, reachability confirmed, date |
| `AU-06` | Rules of Engagement | ⟪roe_extension⟫ — A2 archetype populates. Not used by A1/A3/A4 | RoE instance, approval, prohibited actions |
| `AU-07` | Emergency authorisation | Capture verbal/written authority to begin immediately. Records approver, role, how identity was verified, the scope of authority granted, and what it does **not** permit. Auto-creates a 24-hour ratification task ✋ | Emergency record, ratification task, expiry |
| `AU-08` | ⟨ **Authorisation Gate** ⟩ | Evaluate all conditions. See `28-checklist-and-gate-architecture.md` §3 | Gate evaluation snapshot, passed by, timestamp |

### The emergency path, precisely

> **In plain terms:** if a client's systems are being encrypted right now, they cannot wait for
> contracts. So Sleuth can start — but only the part that *understands and preserves*, never the part
> that *changes or tells anyone*.

```
UNBLOCKED by emergency authorisation
  · triage and assessment
  · containment ADVICE (the client acts, not Sleuth)
  · forensic acquisition  — ⟨Custody Gate⟩ still applies, and cannot be overridden

STILL BLOCKED until full authorisation
  · any active testing
  · any change Sleuth makes to a client system
  · any communication on the client's behalf
  · report delivery

RATIFICATION  within 24h → normal lifecycle resumes
              not done   → ▲ Management · work pauses · the lapse is recorded
                           and appears in the report's limitations
```

---

## `core.readiness` — Phase 3, Understand

| ID | Procedure | Objective / key steps | Records |
|---|---|---|---|
| `RD-01` | Issue questionnaire | Compose from universal + archetype + service + triggered context blocks. Consultant-mediated by default *(Decision D3)* | Questionnaire instance, template version, issued date |
| `RD-02` | Review responses | Review for completeness and plausibility. Mark each answer's source and confidence. ⚠ Answers that are client-stated but material must be flagged for verification | Answers with source, confidence, respondent, date |
| `RD-03` | Verify critical answers | Independently verify the answers work depends on — asset ownership, environment classification, access | Verified by, method, date, discrepancies found |
| `RD-04` | Confirm prerequisites | Confirm everything needed is in place: access, accounts, documents, physical items, site access. ⟪prereq_extension⟫ | Per-prerequisite status, blockers with owners |
| `RD-05` | Verify access works | Actually test the access before day one. ⊗ if access cannot be established, work does not start | Access test results, date, tested by |
| `RD-06` | Tool readiness check | Confirm every planned tool is `Approved` and within validation date. ✋ exception required otherwise | Tool list with versions, approval status, exceptions |
| `RD-07` | Pin runbook version | Bind the engagement to the currently Approved runbook version. **Immutable thereafter** | Runbook ID, version, composition manifest, pinned at |
| `RD-08` | Kickoff | Confirm scope, dates, contacts, communication protocol and escalation path with the client | Attendees, decisions, confirmations, date |
| `RD-09` | Team briefing | Brief every assigned member on scope boundaries, stop conditions and escalation contacts — **before** work starts. Each acknowledges | Per-person acknowledgement with timestamp |
| `RD-10` | ⟨ **Readiness Gate** ⟩ | Evaluate all conditions | Gate evaluation snapshot |

> `RD-09` is deliberately a per-person acknowledgement rather than a team-level tick. Stop conditions
> only work if the individual who encounters one already knows it exists.

---

## `core.evidence` — cross-phase

Depth varies by archetype; the procedures do not. **Register-only per Rule 3** — the platform records
*about* evidence, never holds it.

| ID | Procedure | Objective / key steps | Records |
|---|---|---|---|
| `EV-01` | Identify requirement | Determine what must be captured for this procedure, at what quality | Requirement, rationale, mandatory/optional |
| `EV-02` | Register item | Create the evidence record: ID, level (L0–L5), source, description, classification, personal-data flag | Evidence record, engagement-scoped ID |
| `EV-03` | Acquire / capture | ⟪acquisition_method⟫ — archetype supplies depth. A3: forensic acquisition with write-blocking. A2: tool output and request/response capture. A1: document, interview note, config export | Method, tool + version, examiner, timestamp **with timezone**, write-blocker used |
| `EV-04` | Compute acquisition hash | SHA-256 default. Legacy algorithms permitted only as *additional* values, never alone | Algorithm, hash, computed by, at |
| `EV-05` | Verify | Independently recompute and compare. ⊗ on mismatch — see below | Verification hash, result, verified by, at |
| `EV-06` | Open custody record | Record the `ACQUIRED` event and open the chain. ⟨ **Custody Gate** ⟩ — A3, **not overridable** | Custody chain opened, first event |
| `EV-07` | Maintain custody | Append transfer, receipt, storage, seal, hold events. Never edit, never delete | Append-only event stream |
| `EV-08` | Derive working copy | Verify the parent hash **first**, then derive. Record parent-child provenance | Parent ID, child ID, method, child hash |
| `EV-09` | Record access | Every read, preview or export. Purpose selected, not free text | User, role, purpose, timestamp, action |
| `EV-10` | Re-verify integrity | Periodically, and before evidence supports a finding | Check result, date, by whom |
| `EV-11` | Detect custody gaps | Continuous computation: is every interval attributable to a named holder? | Gap detected, duration, documented as limitation |
| `EV-12` | Plan disposition | At closure: return, destroy or retain. ⊗ Closure Gate blocks without an instruction | Instruction, authority, deadline, personal-data considerations |
| `EV-13` | Execute disposition | Return with acknowledgement, or destroy with a **witness** and a certificate. Enumerate and handle derived items | Method, performed by, witnessed by, certificate, date |

### Integrity failure — a system event, not a field update

```
verification_hash ≠ acquisition_hash
  → integrity_status = FAILED        (irreversible; no role can clear it)
  → all derived items marked provenance-suspect
  → all findings referencing affected items flagged and removed from the report draft
  → ⟨Evidence Integrity Gate⟩ blocks
  → ▲ Reviewer + Engagement Manager. Work does not continue quietly
  → recorded permanently; appears in the report's limitations
```

> **Standards baseline — `EXTERNAL-STANDARD`, Needs Sleuth Confirmation.** This module is written
> against **ISO/IEC 27037** (identification, collection, acquisition and preservation of digital
> evidence), with **ISO/IEC 27041–27043** for assurance, analysis and investigation principles.
> Whether Sleuth formally adopts these — and whether any Indian evidentiary requirement adds to them —
> is a question for Sleuth and its counsel, not an assumption I should make.

---

## `core.qa` — Phase 6

| ID | Procedure | Objective / key steps | Records |
|---|---|---|---|
| `QA-01` | Author self-check | Author works a completion checklist before submitting. Reduces reviewer time spent on mechanical defects | Self-check completion, by whom |
| `QA-02` | Assign reviewer | System enforces `author_id ≠ reviewer_id`. ⊗ assignment refused otherwise | Reviewer, assigned at, by whom |
| `QA-03` | Evidence sufficiency | Every finding has ≥1 evidence link; every A1 maturity rating cites its source. ⟨ **Evidence Integrity Gate** ⟩ | Per-finding evidence check |
| `QA-04` | Finding review | Claim and evidence side by side. Approve, change severity, or reject with a coded reason | Per-finding outcome, reason code, reviewer, date |
| `QA-05` | Severity moderation | Reviewer moderates against calibration data from comparable prior findings | Severity changes with rationale, full history |
| `QA-06` | Report review | Sections complete, scope statement matches approved scope, limitations contextualised | Section-level review outcomes |
| `QA-07` | Rework loop | Rejections return an itemised worklist, not a comment thread. No round limit | Rework items, resolution, iteration count |
| `QA-08` | ⟨ **QA Gate** ⟩ | Evaluate all conditions | Gate evaluation snapshot |

---

## `core.reporting` — Phase 6

| ID | Procedure | Objective / key steps | Records |
|---|---|---|---|
| `RP-01` | Select template version | Pin the report template version for this report | Template ID, version |
| `RP-02` | Generate structured sections | Findings, evidence inventory, scope, assets, timeline generated from records — never retyped | Generation source, timestamp |
| `RP-03` | Author narrative | Narrative sections written with underlying structured data visible beside the editor. ⟪report_extension⟫ | Author, versions |
| `RP-04` | Complete limitations | **Auto-seeded** from unverified answers, custody gaps, unavailable evidence, N/A procedures, gate overrides, deltas, unvalidated runbook content. Editable, **not deletable** | Auto-seeded items, author contextualisation |
| `RP-05` | Executive summary | Written for a non-technical audience. Required on all report types | Author, review status |
| `RP-06` | Consistency check | Severity counts, asset references, scope statement and finding IDs reconciled against the records | Discrepancies found and resolved |
| `RP-07` | Version & freeze | Freeze the delivered version byte-identical. Record hash | Version, hash, frozen at |

> `RP-04` is the procedure I would defend hardest. Auto-seeding limitations makes honest reporting the
> path of least resistance rather than an act of discipline under deadline — and it is what protects
> Sleuth when someone later asks what was and was not covered.

---

## `core.delivery` — Phase 7

| ID | Procedure | Objective / key steps | Records |
|---|---|---|---|
| `DL-01` | Verify recipients | Check against the contact register, including exclusions from `CM-06`. ✋ Engagement Manager approves the list | Recipient list, approved by, exclusions honoured |
| `DL-02` | Apply classification | Classification header/footer, watermark, page numbering | Classification applied, watermark reference |
| `DL-03` | ⟨ **Release Gate** ⟩ | Evaluate all conditions | Gate evaluation snapshot |
| `DL-04` | Deliver | Via the approved channel. ⊗ never an unapproved channel, whatever the client asks for | Channel, delivered at, by whom, confirmation |
| `DL-05` | Walkthrough | Present findings; capture questions, disputes and client context | Attendees, questions, disputes raised |
| `DL-06` | Record acceptance | Formal acceptance, or record the dispute and its resolution path | Acceptance or dispute, by whom, date |

---

## `core.remediation` — Phase 8

| ID | Procedure | Objective / key steps | Records |
|---|---|---|---|
| `RM-01` | Issue remediation guidance | Remediation as structured items with owner, priority and target date — not prose in a PDF | Items, owners, targets |
| `RM-02` | Track remediation | Client-reported status per item | Status changes, dates, source |
| `RM-03` | Clarification support | Answer technical questions during remediation. ⊗ advice must not stray into unauthorised testing | Questions, answers, date |
| `RM-04` | Re-prioritise | Adjust as the client's context changes | Changes with rationale |

---

## `core.closure` — Phase 10

| ID | Procedure | Objective / key steps | Records |
|---|---|---|---|
| `CL-01` | Confirm acceptance | Acceptance recorded, or dispute formally resolved | Acceptance reference |
| `CL-02` | Confirm retest state | Complete, or formally waived by the client in writing | Retest outcome or waiver |
| `CL-03` | Execute disposition | Runs `EV-12`/`EV-13` for every item. ⊗ Closure Gate blocks on any item without a disposition | Per-item disposition status |
| `CL-04` | Revoke Sleuth access | Sleuth-side access to client systems removed and confirmed | Per-access revocation confirmed |
| `CL-05` | Confirm credential revocation | **Client confirms** test accounts and credentials issued to Sleuth are disabled. The platform tracked that access existed *(Rule 4)*, so it can confirm withdrawal | Per-account revocation, confirmed by, date |
| `CL-06` | Remove Sleuth artefacts | Anything Sleuth created in client systems — test accounts, implants, files, rules — removed and **verified removed** | Artefact list, removal verified by, date |
| `CL-07` | Capture lessons learned | What worked, what did not, what surprised us | Lessons, author, linked KB articles |
| `CL-08` | Raise runbook improvements | Proposals raised **against the version that was executed** | Proposals, target module, raised by |
| `CL-09` | ⟨ **Closure Gate** ⟩ | Evaluate all conditions | Gate evaluation snapshot |
| `CL-10` | Archive engagement | Closed, not deleted. Retention clock starts | Archive date, retention class, review date |

> `CL-06` is routinely skipped in practice and occasionally becomes a serious problem — a forgotten
> tester-created domain admin account is a real finding in someone else's later assessment. Making it
> a gate condition with explicit verification is cheap insurance.

---

## Extension points declared by the spine

Where archetype, service and context modules inject without forking core content
(`20-shared-module-inheritance.md` §4).

| Slot | On | Typical injector |
|---|---|---|
| `⟪scope_extension⟫` | `AU-01` | A2 adds testing-window and intrusiveness fields |
| `⟪roe_extension⟫` | `AU-06` | A2 populates; A1/A3/A4 leave empty |
| `⟪prereq_extension⟫` | `RD-04` | Service modules add domain-specific prerequisites |
| `⟪acquisition_method⟫` | `EV-03` | A3 forensic acquisition; A2 capture standard; A1 document/interview |
| `⟪report_extension⟫` | `RP-03` | Archetype and service report sections |
| `⟪closure_extension⟫` | `CL-06` | Service-specific artefact types to remove |

---

## Validation status

| | Count |
|---|---|
| Procedures specified | 59 |
| `SME-VALIDATED` | **0** |
| `DRAFT — NEEDS SME VALIDATION` | 59 |
| Blocking `GAP`s | 0 — the spine is process, not technical method, so it is specifiable from standard practice |

The spine is the part I can responsibly draft in full: it is engagement process, where standard
professional practice is well established and Sleuth-specific technical method is not yet required.
The gaps appear in `24`–`27`, where service-specific technical procedures live.
