# 04 — Runbook Architecture: Common vs Service-Specific

> **Status — DRAFT / NEEDS SME VALIDATION.** Per Rule 1 of [`17-governing-constraints.md`](17-governing-constraints.md), nothing in this document is
> confirmed Sleuth practice. Procedures, tools, legal requirements and operational rules here are
> proposals for SME review, not internal SOP. Content drawn from the public website is
> `SITE-SUGGESTED` and carries no authority over internal method (Rule 6). Gaps are named rather
> than filled (Rule 2). Validation vocabulary: [`18-content-provenance-and-validation.md`](18-content-provenance-and-validation.md).


> The brief's constraint: **"Do NOT create 21 giant documents."**
> The answer: a runbook is not a document. It is a **composition of versioned, reusable units**, rendered one step at a time.

---

## 1. Runbook anatomy

The brief's chain — Runbook → Phase → Procedure → Task → Checklist → Tool → Evidence → Decision → Escalation → Output — is correct, with one clarification: Tool, Evidence, Decision and Escalation are not *steps in sequence*. They are **facets of a procedure**. A procedure has tools, produces evidence, may contain decisions, and declares escalations.

```
RUNBOOK                        SF-SEC-VAP-EXT  v1.2  Approved
  ├─ metadata                  owner · reviewer · approver · effective · next review
  ├─ applicability             engagement type · archetype · attachable context modules
  │
  └─ PHASE (ordered, from the lifecycle)
       ├─ entry criteria       what must be true to start
       ├─ exit criteria        what must be true to finish
       ├─ gate reference       which gate guards this boundary
       │
       └─ PROCEDURE  ← the unit of real work; ~30–90 min of a consultant's time
            ├─ objective       one sentence: why this exists
            ├─ preconditions
            ├─ TASKS (ordered or parallel)
            │     └─ instruction · expected result · duration · role
            ├─ CHECKLIST       verification items with state + evidence + owner
            ├─ TOOLS           references into the tool catalogue (never hard-coded)
            ├─ INPUTS          what must exist before starting
            ├─ EVIDENCE REQ.   what must be captured, in what form, at what quality
            ├─ DECISIONS       branch points with recorded outcomes
            ├─ STOP CONDITIONS halt immediately
            ├─ ESCALATIONS     who is told, how fast
            ├─ APPROVALS       who must authorise before/after
            └─ OUTPUTS         what this procedure produces for the next one
```

**Why the procedure is the unit.** It is the smallest thing that is meaningful to hand to a person, to review, to mark complete, and to attach evidence to. Tasks are too small to govern; phases are too large to execute. A consultant's session in the platform is: open a procedure, do it, capture evidence, close it, get the next one.

---

## 2. Composition: what is shared and what is not

```
                  ┌───────────────────────────────────────────┐
                  │  CORE SPINE            1 definition       │  ← used by all 41
                  │  Phases 0–3 and 7–10, the commercial and  │
                  │  closure machinery, common to everything  │
                  └────────────────────┬──────────────────────┘
                                       │
          ┌──────────────┬─────────────┼─────────────┬──────────────┐
          │              │             │             │              │
     ┌────┴────┐   ┌─────┴────┐  ┌─────┴────┐  ┌─────┴────┐         │
     │   A1    │   │    A2    │  │    A3    │  │    A4    │  ← 4 archetype modules
     │Assessment│  │ Testing  │  │Investig. │  │Continuous│
     └────┬────┘   └─────┬────┘  └─────┬────┘  └─────┬────┘         │
          │              │             │             │              │
     ┌────┴──────────────┴─────────────┴─────────────┴──────┐       │
     │  SERVICE MODULES            41 definitions            │  ← the actual methodology
     │  "External Infra Testing", "Mobile Device Spyware",   │
     │  "OT Maturity", "Detection Engineering", …            │
     └───────────────────────┬───────────────────────────────┘
                             │
     ┌───────────────────────┴───────────────────────────────┐
     │  CONTEXT MODULES            9 definitions              │  ← conditionally attached
     │  Production · Third-Party · OT Safety · Individual     │
     │  Client · Legal Hold · Regulated · Emergency ·         │
     │  People-Targeting · Cross-Border                       │
     └───────────────────────────────────────────────────────┘
```

**Maintenance arithmetic.** Definitions to maintain: 1 + 4 + 41 + 9 = **55 units**, of which only the 41 service modules are genuinely service-specific — and most of those are 6–12 procedures, not a document. Against the naive alternative of 41 standalone runbooks, the shared portion (roughly 40% of every runbook's content by volume) is written and improved **once**. Correcting a chain-of-custody procedure improves all nine A3 runbooks in one edit, with one approval, under one version bump.

### 2.1 The core spine (every engagement, without exception)

| Phase | Procedures in the spine |
|---|---|
| 0 Enquiry & Triage | Record enquiry · Conflict check · Client identity verification · Service selection (decision tree when "Not Sure") · Urgency triage · Qualify in/out |
| 1 Qualification & Commercials | NDA issue & execution · MSA (repeat clients) · SOW drafting & execution · Commercial approval · Team assignment |
| 2 Authorisation & Scope | Scope definition (in **and** out) · Authorised signatory verification · Letter of Authorisation · Client emergency contacts · **Authorisation Gate** |
| 3 Understand | Issue questionnaire · Review responses · Confirm prerequisites · Verify access · Pin runbook version · Kickoff · Brief team on stop conditions · **Readiness Gate** |
| 7 Deliver | Verify recipients · Apply classification · Release · Walkthrough · Record acceptance · **Release Gate** |
| 8 Improve | Issue remediation guidance · Clarification support · Track remediation status |
| 9 Validate | Plan retest · Execute retest · Record per-finding outcome · Issue addendum |
| 10 Close | Record acceptance · Execute evidence disposition · Revoke access · Disable test accounts · Remove tester artefacts · Capture lessons learned · Raise runbook improvements · **Closure Gate** |

That is ~35 procedures written once and reused 41 times.

### 2.2 Archetype modules (Phases 4–6, the shape of the work)

**A1 — Assessment & Advisory**
Framework selection & justification · Documentation request & tracking · Stakeholder interview protocol · Control walkthrough · Configuration/artefact review · Maturity rating with mandatory source citation · Gap identification · Roadmap construction & sequencing · Evidence Sufficiency check.

**A2 — Authorised Technical Testing**
Rules of Engagement construction · Pre-test asset verification (*is this IP actually theirs?*) · Test account validation · Testing window open/close ritual · Reconnaissance → enumeration → vulnerability identification → exploitation → post-exploitation (the site's own published VAPT sequence) · Proof-of-concept capture standard · Finding drafting & severity · Client-artefact cleanup · Retest procedure.

**A3 — Investigation & Response**
Instruction & authority capture (*what exactly are we asked to determine?*) · Evidence identification & preservation · **Acquisition with hashing (Custody Gate)** · Verification · Working-copy derivation · Custody record maintenance · Artefact processing · Timeline construction · Hypothesis formulation & testing · Alternative-explanation consideration · Conclusion formulation with confidence statement · Limitations documentation · Disposition.

**A4 — Continuous & Readiness**
Baseline establishment · Collection cycle · Delta analysis vs previous cycle · Alert triage & disposition · Escalation to incident where warranted · Cycle reporting · Periodic re-authorisation · Coverage review.

### 2.3 Service modules (what makes VAPT ≠ Cloud ≠ Spyware)

Each service module is 6–12 procedures derived from that service's "What We Examine/Test/Analyse" list on the website, expanded into executable method. Example shapes:

| Service module | Representative procedures (seeded from the site) |
|---|---|
| External Infrastructure Testing | Scope validation & ownership confirmation · Passive reconnaissance · Active host & service discovery · Service enumeration · Vulnerability identification · Manual validation · Controlled exploitation · Post-exploitation assessment |
| Web Application & API Testing | Application mapping · Authentication testing · Session management · Authorisation & access control · Input validation & injection · Business logic · API-specific testing (REST/GraphQL/SOAP) · File upload & data handling · SSRF · Headers & transport |
| Mobile Device Spyware Examination | Pre-contact safety briefing (*do not discuss on the device*) · Consent & ownership verification · Device isolation · Forensic acquisition (iOS/Android) · Known-family indicator sweep (Pegasus/Predator/Hermit-class) · Commercial stalkerware sweep · MDM profile & certificate inspection · Network & permission audit · Jailbreak/root & exploit artefact analysis · Message link forensics · Assessment formulation · Hardening guidance |
| OT/ICS Maturity | Safety briefing & engineer pairing · Asset inventory review · Purdue-level segmentation review · IT/OT convergence point mapping · Remote & vendor access governance · Patch & vulnerability practice review · Monitoring capability review · OT incident readiness review · Maturity scoring against IEC 62443 / NIST SP 800-82 |
| Ransomware Investigation | Encryption scope determination · Variant identification · Initial access reconstruction · Dwell-time analysis · Exfiltration assessment (*was data stolen as well as encrypted?*) · Backup integrity & isolation verification · Recovery sequencing advice |

### 2.4 Context modules

As defined in `01-service-catalogue.md` §4. A context module injects procedures, checklist items, gate conditions and questionnaire sections into an already-composed runbook when its attach condition is met.

The attach condition is evaluated from **questionnaire answers and scope data**, so the runbook a consultant sees is already shaped by what the client told us. Example:

```
IF  questionnaire.assets[].environment contains "production"
THEN attach CONTEXT_PRODUCTION
     → +4 procedures, +6 checklist items,
       +1 Authorisation Gate condition (change-window approval),
       swaps 3 procedures for production-safe variants
```

---

## 3. Decision trees

A decision tree is a first-class content object, not prose inside a procedure. It has typed nodes so the system can render it as a guided flow and record the path taken.

```
DECISION TREE: Evidence Availability            (A3 — used by 9 runbooks)

   ┌─────────────────────────────────┐
   │ Is the source evidence          │
   │ available and accessible?       │
   └────────┬───────────────┬────────┘
          YES              NO
            │               │
            ▼               ▼
  ┌──────────────────┐  ┌────────────────────────────────┐
  │ Is it volatile?  │  │ Document the limitation        │
  └───┬──────────┬───┘  │ Identify alternative sources   │
    YES         NO      │ (backups, logs, cloud, other   │
      │          │      │  endpoints, network telemetry) │
      ▼          ▼      └───────────┬────────────────────┘
 ┌─────────┐ ┌─────────┐            │
 │ Capture │ │ Write-  │     ┌──────┴───────┐
 │ volatile│ │ protect │   found          none
 │ FIRST   │ │ source  │     │              │
 └────┬────┘ └────┬────┘     ▼              ▼
      └─────┬─────┘     ┌─────────┐  ┌──────────────────┐
            ▼           │ Proceed │  │ ESCALATE:        │
   ┌──────────────────┐ │ with    │  │ investigation    │
   │ ACQUIRE → HASH   │ │ reduced │  │ objective may be │
   │ → VERIFY → LOG   │ │ scope;  │  │ unachievable —   │
   │ ⟨ CUSTODY GATE ⟩ │ │ state   │  │ Eng. Mgr decision│
   └────────┬─────────┘ │ in      │  │ before continuing│
            ▼           │ limits  │  └──────────────────┘
      ┌──────────┐      └─────────┘
      │ ANALYSE  │
      └──────────┘

Every traversal records: node, branch taken, decided_by, timestamp, rationale.
```

Trees in the initial library:

| Tree | Archetype | Purpose |
|---|---|---|
| Service Selection | Spine | Client said "Other / Not Sure" at intake |
| Urgency Triage | Spine | Route active incidents to the emergency path |
| Production Systems | A1/A2 | Choose production-safe vs standard procedures |
| Asset Ownership | A2 | Third-party hosting → authorisation requirements |
| Exploitation Authorisation | A2 | How far validation may go |
| Pre-existing Compromise Discovered | A2 | **Mandatory stop + escalate + propose IR engagement** |
| Evidence Availability | A3 | Above |
| Device Handling — Powered On/Off | A3 | Volatile capture vs immediate imaging |
| Legal Authority | A3 | Is there sufficient authority to examine this? |
| Incident Severity Classification | A3 | Team size, escalation, client notification cadence |
| Data Exfiltration Suspected | A3 | Breach-notification assessment path |
| Backup Viability | A3 | Ransomware recovery sequencing |
| Finding Severity Moderation | All | Consistent severity across engagements and analysts |
| Retest Outcome | All | Resolved / Partial / Not Resolved / Accepted / Unverifiable |

---

## 4. Version control and pinning

The brief (§18) requires that an active engagement retains the runbook version it used. This is the mechanism.

```
Runbook: SF-INV-DFIR-FULL
  ├─ v1.0  Deprecated   effective 2026-01-15 → 2026-06-30
  ├─ v1.1  Deprecated   effective 2026-07-01 → 2026-09-14
  ├─ v1.2  Approved     effective 2026-09-15   next review 2027-03-15
  └─ v1.3  Draft        owner: <Needs Confirmation>

ENG-2026-0113  started 2026-08-02  →  pinned to v1.1   ← keeps executing v1.1
ENG-2026-0141  started 2026-09-18  →  pinned to v1.2
```

**Rules**
1. On leaving Phase 3, the engagement pins the currently Approved version. The pin is immutable.
2. Approved versions are immutable. A change produces a new version, always.
3. Deprecating a version never affects engagements already pinned to it.
4. A mid-engagement version bump is a **deliberate, logged migration**, requested by the Engagement Manager and approved by Management, with an impact summary of what changed. It never happens silently.
5. Every report states the runbook ID and version used — so a report delivered in 2026 remains explicable in 2029.
6. Status flow: `Draft → In Review → Approved → Deprecated`. Only Management approves; only an Author drafts (`02-users-and-roles.md`).
7. Every version carries a change history entry: what changed, why, who, when.

### Why pinning matters more than it first appears
Without it, a runbook improvement rewrites the methodology of engagements already in flight. A client asking "what process did you follow?" eighteen months later would get an answer describing a process nobody actually ran. Pinning makes the honest answer retrievable, and that is the entire point of a defensible methodology.

---

## 5. Answering the brief's seven questions

Every procedure view answers these by construction, because each maps to a required field:

| Question | Field |
|---|---|
| Where am I? | Phase + procedure position + engagement breadcrumb |
| What am I doing? | Procedure objective + current task |
| Why am I doing it? | Objective rationale + the output it feeds |
| What do I need? | Inputs + preconditions + tools + access |
| What evidence do I capture? | Evidence requirements, with capture action inline |
| What should I produce? | Outputs |
| What happens next? | Next procedure, or the gate that is now in the way |
| *(plus)* What if something unexpected happens? | Stop conditions + escalations, always visible |
| *(plus)* Who needs to review this? | Approvals |

A procedure that cannot fill all nine fields is not ready to be approved. That is the authoring quality bar, enforced by the runbook editor.
