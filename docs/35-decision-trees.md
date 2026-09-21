# 35 — Decision Trees

> **Status — Draft / Needs SME Validation.** Provenance: `INDUSTRY-PRACTICE` and `SLEUTH-CONFIRMED`
> where a tree encodes a confirmed policy from `32-operating-policies.md`.

A decision tree is a content object, not prose inside a procedure. Typed nodes let the platform render
it as a guided flow and **record the path taken** — node, branch, who decided, when, and why.

**Node types:** `QUESTION` · `ACTION` · `STOP` · `ESCALATE` · `TERMINAL`
Every traversal writes a `DecisionRecord` (`10-data-model.md`).

---

## 1. Tree inventory — 16 trees

| ID | Tree | Used by | Encodes |
|---|---|---|---|
| `DT-01` | Service selection | Spine | Intake when the client said "Other / Not Sure" |
| `DT-02` | Urgency triage | Spine | Routing to the emergency path |
| `DT-03` | Client type & contracting | Spine | Organisation vs individual |
| `DT-04` | Asset ownership | A2, A4 | Third-party authorisation requirements |
| `DT-05` | Production systems | A1, A2 | Production-safe variants |
| `DT-06` | **Intrusiveness level** | A2 | `32` §1 — `SLEUTH-CONFIRMED` |
| `DT-07` | **Pre-existing compromise discovered** | A2, A1-SOA | Mandatory stop and escalate |
| `DT-08` | Evidence availability | A3 | Preserve, or document the limitation |
| `DT-09` | Device handling — powered on/off | A3 | Volatile capture vs immediate imaging |
| `DT-10` | Legal authority to examine | A3 | Is there sufficient authority? |
| `DT-11` | Incident type determination | `SF-A3-IRE` | Which incident module attaches |
| `DT-12` | Incident severity classification | A3 | Team size, cadence, notification |
| `DT-13` | Data exfiltration suspected | A3 | Breach-scope path |
| `DT-14` | Backup viability | `SF-A3-IRE` ransomware | Recovery sequencing |
| `DT-15` | **Finding severity** | All | `32` §2 — `SLEUTH-CONFIRMED` |
| `DT-16` | Retest outcome | A2 | Outcome vocabulary |

---

## 2. The trees that encode confirmed policy

### `DT-06` — Intrusiveness level `SLEUTH-CONFIRMED`

```
Is any in-scope asset production, safety-critical, or flagged fragile?
├─ YES ─► Has the client explicitly authorised action against it?
│          ├─ NO  ─► LEVEL 1 for that asset. Identify only.
│          └─ YES ─► Is a change window and rollback confirmed?
│                     ├─ NO  ─► LEVEL 1 for that asset.
│                     └─ YES ─► continue below, per asset
└─ NO  ─► Does the engagement require business impact to be demonstrated?
           ├─ NO  ─► ■ LEVEL 2 — VALIDATE SAFELY  (firm default)
           └─ YES ─► Is Level 3 authorised in the Rules of Engagement,
                     naming the assets and the ceiling?
                      ├─ NO  ─► LEVEL 2. Raise a scope change if L3 is needed.
                      └─ YES ─► LEVEL 3 — within the named ceiling only
                                ✋ approval required per action class

At every level, the seven absolute rules apply and cannot be overridden (32 §1).
Recorded: level per asset, who set it, when, and the authority relied on.
```

### `DT-15` — Finding severity `SLEUTH-CONFIRMED`

```
What is the consequence to THIS client if this is exploited?
│
├─ Severe and immediate — full environment compromise · unauthenticated access to
│  bulk personal or regulated data · a core business process can be halted ·
│  the identity system is compromised
│     └─ Reachable now, by a realistic attacker, with no meaningful barrier?
│          ├─ YES ─► CRITICAL
│          └─ NO  ─► HIGH
│
├─ Serious, but requires a condition (authentication · a chained step ·
│  a specific network position)
│     └─► HIGH   (MEDIUM if the condition is genuinely hard to meet)
│
├─ Real, but bounded in scope, or meaningful barriers exist
│     └─► MEDIUM
│
├─ Limited — contributes to risk rather than causing it
│     └─► LOW
│
└─ No direct consequence — hygiene, hardening, an observation
      └─► INFORMATIONAL

Anchors, enforced:
  · rationale is mandatory and must state the consequence, not the technique
  · severity NEVER falls because remediation is difficult or expensive
  · severity NEVER rises because a tool labelled it so
  · two clients with the identical flaw may differ — the rationale says why
  · reviewer moderates against comparable prior findings at QA
```

---

## 3. The trees that stop work

### `DT-07` — Pre-existing compromise discovered

The highest-stakes moment in A2 work: the tester is now a witness to someone else's intrusion.

```
Indication of a compromise NOT caused by our testing
│
├─► ■ STOP. Cease all testing activity immediately.
├─► Do NOT interact further with the affected system.
│   Do not "check", do not collect, do not remediate.
├─► Preserve exactly what was being done at the moment of discovery.
├─► ▲ Engagement Manager — immediately, by phone.
│
└─► Engagement Manager ─► client emergency contact, immediately
     │
     ├─ Client engages Sleuth for response
     │    └─► open SF-A3-IRE as a CHILD engagement
     │        (inherits client, authority, custody, classification)
     │
     ├─ Client engages another responder
     │    └─► hand over findings; record the handover; testing resumes
     │        only on written instruction
     │
     └─ Client instructs testing to continue regardless
          └─► ▲ MANAGEMENT. Do not resume on the Engagement Manager's
              authority alone. Record the instruction and the decision.
              The discovery appears in the report's limitations regardless.
```

> The last branch is the uncomfortable one, and it is why this is a tree rather than a note.
> A client under commercial pressure may prefer the finding not to exist.

### `DT-10` — Legal authority to examine

```
Who owns the device?
├─ Client-owned ──► Who owns the DATA on it?
│                    ├─ Client ──────► Is there policy or consent covering examination?
│                    │                  ├─ YES ─► PROCEED
│                    │                  └─ NO  ─► ■ STOP. Obtain consent or
│                    │                            counsel's instruction.
│                    └─ Mixed/personal ► ■ STOP. Scope the examination to
│                                        client data only, in writing, with
│                                        counsel. Record the limitation.
├─ Personally owned ► Does the individual consent, in writing?
│                      ├─ YES ─► PROCEED, scoped to the consent given
│                      └─ NO  ─► ■ STOP. No examination.
└─ Employer-owned,    ► ■ STOP. Employer authorisation required before
   individual client     any examination. (SF-A3-SPY — common case.)

At any point, if authority proves insufficient AFTER acquisition:
  ■ STOP analysis · preserve · ▲ Engagement Manager · seek instruction.
  Do not delete — that may itself be spoliation.
```

---

## 4. The operational trees

### `DT-09` — Device handling

```
Is the device powered on?
├─ YES ─► Is volatile data relevant to the questions posed?
│          ├─ YES ─► Capture volatile data FIRST (memory, running state,
│          │         network connections, logged-on sessions, encryption keys)
│          │         └─► then shut down per the device's safe method
│          └─ NO  ─► Is the device encrypted with keys only available while running?
│                     ├─ YES ─► capture volatile / acquire live. Do not power off.
│                     └─ NO  ─► shut down per safe method
└─ NO  ─► ■ DO NOT POWER ON.
           └─► Write-protect · acquire · hash · verify · open custody
               ⟨ CUSTODY GATE — not overridable ⟩

Recorded: state on receipt, decision, rationale, who decided, timestamp.
```

### `DT-08` — Evidence availability

```
Is the source evidence available and accessible?
├─ YES ─► Is it volatile? ──YES──► capture volatile first
│         │                └─NO──► write-protect source
│         └─► ACQUIRE → HASH → VERIFY → LOG   ⟨ CUSTODY GATE ⟩ ─► ANALYSE
└─ NO  ─► Document the limitation.
           └─► Identify alternatives (backups · logs · cloud · other endpoints ·
               network telemetry · collateral devices)
                ├─ Found ─► proceed with reduced scope; state it in limitations
                └─ None  ─► ▲ ESCALATE: the investigation objective may be
                            unachievable. Engagement Manager decides before
                            further cost is incurred.
```

### `DT-11` — Incident type determination

```
What is the dominant observable?
├─ Files encrypted / ransom note ──────────► RANSOMWARE module
├─ Mailbox anomalies / fraudulent payment ─► BEC module
├─ Data staged, archived or egressed ──────► DATA THEFT module
├─ Authorised account acting abnormally ───► INSIDER module
│                                             ⚠ heightened confidentiality
├─ Web/application server compromise ──────► WEB COMPROMISE module
└─ Not yet determinable ───────────────────► UNKNOWN module
                                              broad triage until determinable

The type is PROVISIONAL and revisable.
Every change records: previous type, new type, what changed the assessment,
who decided, when. The early hypothesis in an incident is frequently wrong,
and pretending otherwise hides the reasoning.
```

### `DT-14` — Backup viability

```
Do backups exist for the affected systems?
├─ NO ──► Recovery is rebuild-only. ▲ Engagement Manager. Reset expectations early.
└─ YES ─► Were they network-reachable from the compromised environment?
           ├─ YES ─► ⚠ Treat as potentially compromised.
           │         Verify integrity before ANY restore.
           │         Restoring a compromised backup reinfects.
           └─ NO  ─► Isolated. Date of last known-good?
                      └─► Has a restore been tested at this scale before?
                           ├─ NO ─► ⚠ Untested at scale. State the risk.
                           │        Recovery time is unknown, not the RTO target.
                           └─ YES ► Sequence recovery: identity first,
                                    then critical dependencies, then the rest.
                                    ⊗ Do not restore into an environment where
                                      eradication is unverified.
```

### `DT-13` — Data exfiltration suspected

```
Is there evidence data was ACCESSED?
├─ NO  ─► State "no evidence of access found", with the coverage that
│         supports that statement. Absence of evidence ≠ evidence of absence,
│         and the report must say which one this is.
└─ YES ─► Is there evidence data was TAKEN (egress, staging, archive, C2 transfer)?
           ├─ NO  ─► Report ACCESS only. Do NOT report exfiltration.
           │         These are separate findings with separate consequences.
           └─ YES ─► Determine: what data classes · volume · destination · window
                      └─► Personal or regulated data involved?
                           ├─ YES ─► ▲ Engagement Manager → client counsel.
                           │         Notification assessment is a LEGAL
                           │         determination, not Sleuth's. We supply facts.
                           └─ NO  ─► Report scope and impact.
```

> `DT-13` exists because conflating "could have been accessed" with "was taken" is among the most
> damaging errors in incident reporting. The tree forces them apart.

---

## 5. The intake trees

### `DT-01` — Service selection

Runs when the enquiry's Area of Interest is "Other / Not Sure" *(a live contact-form value)*.

```
Has something already happened, or might it have?
├─ YES ─► Is it happening right now? ──YES──► SF-A3-IRE  (→ DT-02 emergency)
│          └─ NO ─► Do you know what happened?
│                    ├─ YES, a specific matter ─► SF-A3-DFE
│                    ├─ Suspect a device is monitored ─► SF-A3-SPY
│                    ├─ Suspect but unconfirmed ──────► SF-A3-CTH
│                    └─ Have a suspicious file ───────► SF-A3-MAL
└─ NO  ─► What do you need to know?
           ├─ "Can someone break in?" ──────► A2 — DT: which surface?
           │     web/API → WAT · mobile → MAT · cloud → CPT
           │     AD/identity → ATP · network/infra → IPT
           │     "everything, realistically" → RED
           │     "will staff fall for it?" → SES
           ├─ "How good are we?" ───────────► SF-A1-SPA
           ├─ "Will we pass an audit?" ─────► SF-A1-CRA
           ├─ "Is this configured correctly?" ─► SF-A1-TCR (+ pack)
           ├─ "Is our OT secure?" ──────────► SF-A1-OTA
           ├─ "Does our SOC work?" ─────────► SF-A1-SOA
           ├─ "Are we ready for ransomware?" ► SF-A1-IRA
           ├─ "What's exposed externally?" ─► SF-A4-ASM
           └─ "We need security leadership" ► SF-A4-VCI
```

### `DT-02` — Urgency triage

```
Urgency from the enquiry (four live contact-form values)
├─ "Urgent — Active Incident or Immediate Need"
│    └─► Is a system compromised, encrypting, or actively under attack NOW?
│         ├─ YES ─► EMERGENCY PATH
│         │         · Emergency Authorisation record (AU-07)
│         │         · 24h ratification task, owner = Engagement Manager
│         │         · UNBLOCKS: triage · containment ADVICE · acquisition
│         │           (⟨Custody Gate⟩ still applies, un-overridable)
│         │         · STILL BLOCKED: active testing · changes to client
│         │           systems · external communication · report delivery
│         └─ NO  ─► expedited standard path
├─ "Upcoming — Within Weeks"  ─► standard path, prioritised
├─ "Planning — Next 1-3 Months" ─► standard path
└─ "General Enquiry" ───────────► qualification only

Commitment: respond within one business day (SITE-DERIVED).
```

---

## 6. The remaining trees, in brief

| Tree | Shape |
|---|---|
| `DT-03` Client type | Organisation → NDA/MSA/SOW · Individual → single agreement + consent declaration + safeguarding assessment *(`32` §3)* |
| `DT-04` Asset ownership | Client-owned → proceed · Third-party hosted → authorisation required, **blocking** · SaaS → provider policy check · Unverifiable → **remove from scope** |
| `DT-05` Production systems | Production in scope → attach Production context · require change window and rollback · substitute production-safe variants · record client on-call · default intrusiveness drops to L1 unless explicitly authorised |
| `DT-12` Incident severity | Business impact × spread × data sensitivity → team size, client cadence, whether Management is engaged, whether 24/7 running |
| `DT-16` Retest outcome | Re-test performed? → Resolved · Partially resolved · Not resolved · Risk accepted *(needs a named owner and date)* · Unable to verify *(state why)* |

---

## 7. Placeholders

| Ref | Placeholder | Default applied |
|---|---|---|
| `‹PH-06›` | `DT-12` severity thresholds — what makes an incident "major" for Sleuth's staffing | Three bands: single system · multiple systems or one business process · enterprise-wide or safety-affecting |
| `‹PH-07›` | `DT-11` incident-type list completeness — is a sixth module needed *(e.g. supply chain, DDoS)* | Five plus Unknown. Supply chain folded into Web Compromise for now |
| `‹PH-08›` | `DT-01` routing for enquiries Sleuth does not serve | Qualify out, record the reason, refer where appropriate |

---

## 8. Counts

| | |
|---|---|
| Trees specified | **16** |
| Encoding confirmed policy | 2 *(`DT-06`, `DT-15`)* |
| Containing a mandatory stop | 5 |
| Containing a mandatory escalation | 7 |
| Placeholders | 3 |
| `SME-VALIDATED` | **0** |
