# 03 — Engagement Lifecycle & Gates

---

## 1. The lifecycle is Sleuth's own published method

The homepage and about page both publish a six-step method: **Understand → Examine → Analyse → Report → Improve → Validate**.

The platform's lifecycle *is* that method, wrapped at both ends with what the six steps do not cover: getting lawfully and commercially authorised to start, and properly finishing.

```
┌─ PRE-ENGAGEMENT ──────────────┐ ┌─ SLEUTH'S PUBLISHED METHOD ─────────────────────────┐ ┌─ CLOSURE ─┐
│                               │ │                                                     │ │           │
│  0        1          2        │ │  3          4         5        6        7      8    │ │     9     │
│ Enquiry  Qualify  Authorise   │ │ Understand Examine  Analyse  Report  Improve Validate│ │   Close   │
│    &        &        &        │ │                                                     │ │           │
│  Triage  Contract   Scope     │ │                                                     │ │           │
└───────────────────────────────┘ └─────────────────────────────────────────────────────┘ └───────────┘
             ▲                                 ▲          ▲         ▲                            ▲
        ╔════╧═════╗                      ╔════╧════╗ ╔═══╧════╗╔═══╧════╗                  ╔════╧════╗
        ║   AUTH   ║                      ║READINESS║ ║EVIDENCE║║   QA   ║                  ║ CLOSURE ║
        ║   GATE   ║                      ║  GATE   ║ ║INTEGRITY║║  GATE  ║                  ║  GATE   ║
        ╚══════════╝                      ╚═════════╝ ╚════════╝╚════════╝                  ╚═════════╝
                                                                     │
                                                                ╔════╧════╗
                                                                ║ RELEASE ║
                                                                ║  GATE   ║
                                                                ╚═════════╝
```

Report is split into **Report** (build + QA) and **Deliver** (release + acceptance) because they fail differently and therefore need different gates: a report can be technically sound but sent to the wrong recipient.

---

## 2. Phase by phase

### Phase 0 — Enquiry & Triage
**Ends when:** qualified in or out.

Mirrors the live contact form (research §4.3): name, company, work email, phone, **Area of Interest** (21 services + Other/Not Sure), **Urgency** (4 values), message. Stated commitment: response within one business day.

- If Area of Interest = "Other / Not Sure" → run the **service-selection decision tree** rather than guessing.
- If Urgency = **"Urgent — Active Incident or Immediate Need"** → immediately branch to the emergency path (§4). Triage begins before contracting completes.
- Conflict check and client identity check happen here, before any confidential detail is taken.

### Phase 1 — Qualification & Commercials
**Ends when:** NDA and engagement agreement are executed.
NDA → MSA (if a repeat client) → SOW. For `client_type = Individual`, a simplified single agreement replaces MSA/SOW. Commercial terms, team assignment, indicative dates.

### Phase 2 — Authorisation & Scope
**Ends when:** the **Authorisation Gate** passes.
The most important phase in the system and the one most often compressed in practice. Letter of Authorisation with a named signatory and their authority to give it; scope definition (in-scope *and* explicitly out-of-scope); Rules of Engagement for A2; testing window; third-party authorisation where assets are not client-owned; emergency contacts on both sides.

### Phase 3 — Understand
**Ends when:** the **Readiness Gate** passes.
The service questionnaire is completed and reviewed. Prerequisites confirmed (access, credentials delivered, test accounts, point of contact available). Kickoff held. Runbook version **pinned** to the engagement. Team briefed on stop conditions and escalation contacts — before, not during.

### Phase 4 — Examine
**Ends when:** all required procedures are complete, deferred with reason, or marked not-applicable with reason.
Technical execution against the pinned runbook. Evidence captured as work happens, not reconstructed afterwards. Decision points recorded with who decided and why. Stop conditions live and visible throughout.

### Phase 5 — Analyse
**Ends when:** the **Evidence Integrity Gate** passes and findings are drafted.
Correlation, timeline construction, hypothesis testing, finding drafting. Every finding must reference at least one evidence record — this is "evidence over assumption" made structural rather than aspirational.

### Phase 6 — Report
**Ends when:** the **QA Gate** passes.
Report assembled from the service's report template. Technical review by someone who did not author the work. Severity moderation. Limitations section completed honestly — including what could *not* be tested and why.

### Phase 7 — Deliver
**Ends when:** the **Release Gate** passes and delivery is acknowledged.
Recipient list verified. Classification and watermarking applied. Delivery via the approved channel. Walkthrough session. Client acceptance recorded.

### Phase 8 — Improve
**Ends when:** remediation guidance is delivered and, where in scope, client remediation is reported complete.
Remediation items tracked as structured objects with owner and target date, not prose in a PDF. Clarification support. Re-prioritisation as the client's context changes.

### Phase 9 — Validate
**Ends when:** retest is complete, or formally waived.
Retest of remediated findings; each gets a verified outcome: `Resolved` / `Partially Resolved` / `Not Resolved` / `Risk Accepted` / `Unable to Verify`. A retest report or an addendum is issued. Only VAPT and Web/API Security promise retest on the website — whether it is standard elsewhere is **Needs Confirmation**.

### Phase 10 — Close
**Ends when:** the **Closure Gate** passes.
Evidence disposition executed (return, secure destruction, or retention under a documented policy with a review date). Client access revoked, test accounts disabled, any tester-created artefacts removed from client systems. Lessons learned captured into the Knowledge Base. Runbook improvement proposals raised against the runbook that was used.

---

## 3. The gates

A gate is not a checkbox. It is a **live evaluation of engagement state**: a set of conditions the system can actually check, evaluated continuously, showing `BLOCKED` or `READY` with a specific reason for every unmet condition.

The brief's own example is the model:

```
╔══════════════════════════════════════════════════════════════╗
║  AUTHORISATION GATE                             ● BLOCKED    ║
╠══════════════════════════════════════════════════════════════╣
║  ✓  NDA executed                    2026-09-02 · A. Rao      ║
║  ✓  SOW executed                    2026-09-09 · A. Rao      ║
║  ✕  Letter of Authorisation         Not received             ║
║  ✓  Scope approved                  2026-09-11 · 14 assets   ║
║  ✕  Rules of Engagement approved    Draft — awaiting client  ║
║  ✓  Testing window agreed           22–26 Sep, 09:00–18:00   ║
║  ✕  Third-party authorisation       2 assets on AWS —        ║
║                                     provider check pending   ║
╠══════════════════════════════════════════════════════════════╣
║  3 conditions unmet. Technical execution cannot begin.       ║
║  [ Request override ]          Requires Management approval  ║
╚══════════════════════════════════════════════════════════════╝
```

### Gate definitions

| Gate | Blocks | Conditions | Who passes it |
|---|---|---|---|
| **Authorisation** | Any technical execution (Phase 4) | NDA executed · Engagement agreement executed · LoA signed by verified authorised signatory · Scope approved with explicit out-of-scope list · RoE approved *(A2 only)* · Testing window agreed *(A2)* · Third-party authorisation obtained where assets are not client-owned · Emergency contacts recorded both sides | Engagement Manager |
| **Readiness** | Start of execution | Questionnaire complete (all required answered, or marked unavailable with reason) · Prerequisites confirmed · Access verified working · Runbook version pinned · Stop conditions acknowledged by every assigned team member · Tools for this engagement are Approved and validated | Engagement Manager |
| **Evidence Integrity** | Findings → Report (Phase 5→6) | Every evidence item has acquisition hash + algorithm · Verification hash recorded and matching · No custody gaps · Working copies derived from verified sources · Examiner recorded for each acquisition · Every finding references ≥1 evidence item | Reviewer |
| **QA** | Report → Delivery (Phase 6→7) | Technical review complete by a non-author · Every finding has severity + rationale + evidence · All required report sections complete · Scope statement matches approved scope · Limitations section completed · No open `Needs Review` items · No unresolved reviewer rejections | Reviewer |
| **Release** | Delivery to client | Recipient list approved by Engagement Manager · Recipients verified against client contact record · Classification applied · Watermark applied · Delivery channel approved · Report version frozen | Engagement Manager |
| **Closure** | Engagement → Closed | Client acceptance recorded · Retest complete or formally waived · Evidence disposition executed or scheduled with a date · Client access revoked · Test accounts disabled · Tester artefacts removed from client systems · Lessons learned captured · Invoicing complete | Engagement Manager |

### Gates for A1, A3 and A4

The six gates above are the full set for A2. Other archetypes use a subset, plus their own:

- **A1** — Authorisation Gate is lighter (no RoE, no testing window) but still requires the agreement and scope. No Evidence Integrity Gate in the forensic sense; instead an **Evidence Sufficiency** check: every maturity rating must cite the document, interview or observation supporting it. A maturity score with no source is the A1 equivalent of a finding with no evidence.
- **A3** — adds a **Custody Gate** at the point of acquisition (before any analysis touches an image): source write-protected, acquisition hash computed, verification hash matched, custody record opened. This gate sits *earlier* than the Evidence Integrity Gate and is unskippable, including on the emergency path.
- **A4** — has no Closure Gate (the contract continues). Instead each cycle has a **Cycle Close** checkpoint, and the *contract* has a periodic re-authorisation gate so a standing authorisation cannot quietly run for years.

### Override semantics

Overrides exist because reality does. They are designed to be *possible, expensive and visible*:

- Requested by the Engagement Manager, approved by Management. Never one person.
- A written justification is mandatory and becomes part of the engagement record.
- **Every override is time-boxed.** It carries an expiry and a mandatory remediation task ("obtain the signed LoA by 2026-09-23"). When the clock runs out, the gate re-blocks.
- The override appears on the engagement header, in the report's limitations section draft, on the Oversight dashboard, and in the audit log.
- **The Custody Gate cannot be overridden.** Acquiring evidence without an integrity record does not produce weaker evidence; it produces no evidence. There is no business justification that changes that, so the system does not offer the option.

---

## 4. The emergency path

The contact form's "Urgent — Active Incident or Immediate Need" is a real intake route, and an organisation whose servers are encrypting cannot wait for a contracting cycle. Modelling this honestly is better than pretending every engagement starts on a Monday.

```
Enquiry (Urgent)
   │
   ├─► IMMEDIATE:  Emergency Authorisation record
   │               · named client approver + their role + how identity was verified
   │               · verbal/written authority scope — what Sleuth may and may not do
   │               · timestamp, taken by
   │               · auto-created RATIFICATION TASK, due in 24h, owner = Eng. Manager
   │
   ├─► Triage and CONTAINMENT ADVICE may begin
   │   Forensic ACQUISITION may begin — Custody Gate still applies, un-overridable
   │
   ├─► BLOCKED until full authorisation:
   │       · any active testing
   │       · any change to client systems made by Sleuth
   │       · any external communication on the client's behalf
   │       · report delivery
   │
   └─► Ratification: NDA + agreement + written LoA executed retrospectively
           │
           ├─ done within 24h  → normal lifecycle resumes, override closes
           └─ not done         → ESCALATE to Management; work pauses; the lapse is
                                 recorded and appears in the report's limitations
```

The emergency path is deliberately narrow: it unblocks *understanding and preserving*, never *changing or disclosing*.

---

## 5. Lifecycle variation by archetype

Same spine, different emphasis. This is the whole argument for four archetypes rather than 41 workflows.

| Phase | A1 Assessment | A2 Testing | A3 Investigation | A4 Continuous |
|---|---|---|---|---|
| 0 Enquiry | Standard | Standard | **Often urgent** | Contract-initiated |
| 1 Commercials | Standard | Standard | May be **retrospective** | Once, then dormant |
| 2 Authorise | Agreement + scope | **+ LoA, RoE, window, 3rd-party** | Authority to investigate; data/device ownership; **may be emergency** | Standing, **re-authorised per period** |
| 3 Understand | Framework selection, doc request | Asset confirmation, access, test accounts | **What happened? who touched it?** | Baseline carried forward from last cycle |
| 4 Examine | Interviews, doc review, config review | Active testing in window | **Acquire → verify → preserve → analyse** | Scheduled collection |
| 5 Analyse | Control maturity rating | Exploitability & business impact | **Timeline & hypothesis testing** | Delta vs previous cycle |
| 6 Report | Scorecard + gap analysis | Findings register | **Narrative + timeline + inventory** | Cycle report |
| 7 Deliver | Workshop | Debrief | **Often to legal/HR/board** | Automated + periodic briefing |
| 8 Improve | Roadmap | Remediation guidance | Containment / hardening | Continuous recommendations |
| 9 Validate | Re-assessment (often next year) | **Retest** | Verification of eradication | Next cycle *is* the validation |
| 10 Close | Report accepted | Retest closed | **Evidence disposition — the critical step** | No closure; contract continues |

---

## 6. Decision points, stop conditions and escalation

Every procedure in a runbook declares four things. They are fields, not prose, so the system can surface them at the right moment.

**Decision points** — a branch with recorded outcome:
```
Is any in-scope asset a production system?
  YES → attach Production Systems context module
        → require change-window approval
        → substitute production-safe procedure variants
        → record client on-call contact
  NO  → standard procedure
Recorded: decision, decided_by, timestamp, rationale.
```

**Stop conditions** — work halts immediately, no judgement call required. Archetype-level examples:

| Archetype | Stop condition |
|---|---|
| A2 | Evidence of a **pre-existing compromise** is discovered |
| A2 | A production system becomes unstable or unavailable |
| A2 | Testing reaches an asset that is not in the approved scope |
| A2 | The testing window has expired |
| A3 | Evidence integrity cannot be established or is found broken |
| A3 | Material conflict of interest emerges |
| A3 | Findings implicate the person who commissioned the investigation |
| A1 | Client cannot provide evidence for a control they assert exists |
| All | Authorisation lapses or is withdrawn |
| All | A safety risk to people is identified (OT, physical, social engineering) |

The third A3 row is the uncomfortable one and the reason it must be a *system* stop condition rather than an individual's judgement: an examiner discovering that the sponsoring executive is implicated should be routed to a pre-agreed escalation path, not left to decide alone at 11pm.

**Escalation conditions** — who is woken, and how fast:

| Trigger | Escalate to | Target |
|---|---|---|
| Pre-existing compromise found during testing | Engagement Manager → client emergency contact | Immediate |
| Active compromise confirmed in a compromise assessment | Engagement Manager; propose IR child engagement | Immediate |
| Evidence integrity failure | Reviewer + Engagement Manager | Immediate, work paused |
| Safety risk identified | Engagement Manager → Management | Immediate |
| Authorisation lapse or scope dispute | Engagement Manager → Management | Same day |
| Findings implicate the engagement sponsor | Management directly, bypassing the Engagement Manager | Immediate, confidential |
| Client requests something outside approved scope | Engagement Manager; scope change or refusal | Before acting |
| Gate override requested | Management | Before proceeding |

**Approval requirements** — declared per procedure: none / Reviewer / Engagement Manager / Management / client-side named approver.

---

## 7. What an engagement record retains forever

When an engagement closes, these must remain reconstructable — this is the difference between a workflow tool and a defensible record:

- The **runbook version** that was executed, in full, as it read at the time
- Every gate evaluation, including passes, blocks and overrides with their justifications
- Every decision point outcome with who decided and why
- The complete evidence register and custody chain, including items later destroyed
- Every finding with its evidence links and severity history
- The delivered report version, byte-identical
- The disposition record for every evidence item
- The full audit log

The engagement is closed, not deleted. Deletion is a separate, deliberate, policy-driven act with its own retention schedule — see `09-security-architecture.md`.
