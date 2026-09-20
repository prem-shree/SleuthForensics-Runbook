# 09 — Information Architecture & Navigation

> The brief lists 17 candidate areas and then says: *"Do not blindly make all of these top-level navigation items. Design the information architecture properly."*

---

## 1. The organising insight

Those 17 concepts are not peers. They divide cleanly into three kinds of thing, and the division does the architectural work:

| | **Work** | **Content** | **Governance** |
|---|---|---|---|
| What it is | An engagement in flight | Versioned, approved material reused across engagements | Oversight and control of the platform |
| Changes | Constantly, by the hour | Rarely, under approval | Rarely, by Admin |
| Scoped to | One client, one engagement | The whole practice | The whole practice |
| Who lives here | Analyst, Reviewer | Runbook Author | Management, Admin |
| Contains | Tasks, Checklists, Questionnaire responses, Evidence, Findings, Reports, Documents | Services, Runbooks, Questionnaire templates, Tools, Document templates, Knowledge Base | Users, Roles, Audit log, Settings, Metrics |

**Evidence, Findings, Tasks, Checklists and Questionnaires are not destinations.** They are always *of* an engagement. Making them top-level would force the consultant to answer "which engagement?" on every navigation — the exact friction the brief says to remove, and a confidentiality risk besides, since a global Evidence list is a list of every client's material in one view.

They surface globally only as **registers**: deliberate, filtered, cross-engagement views for Reviewers and Managers who genuinely work across engagements.

---

## 2. Top-level navigation: seven items

```
┌──────────────────────┐
│  SLEUTH              │
│  ──────────────────  │
│  ▸ Today             │   personal work queue — the default landing
│  ▸ Engagements       │   portfolio → engagement workspace
│  ▸ Clients           │   client record, history, contacts, contracts
│  ▸ Registers         │   cross-engagement: Evidence · Findings · Reports · Documents
│  ▸ Library           │   Services · Runbooks · Questionnaires · Tools · Templates · KB
│  ▸ Oversight         │   practice state, metrics, obligations      (Mgmt/EM)
│  ▸ Administration    │   users, roles, config, audit log           (Admin)
└──────────────────────┘
```

Seven items, of which most roles see four or five (`02-users-and-roles.md` §4). Everything else is reached in context.

### Why each earns its place

- **Today** — answers "what do I do next" across engagements. It is the North Star at the personal scale, and it is why an Analyst never has to navigate to start work.
- **Engagements** — the portfolio. Filterable by state, gate status, service, client, team, urgency.
- **Clients** — clients persist across engagements. Contracts, contacts, history, standing authorisations, prior findings and open remediation all belong to the client, not to any one engagement. Without this, the second engagement for a client repeats the first engagement's discovery work.
- **Registers** — the cross-engagement views, each existing for a specific real question: *Evidence* → "what are we holding, and what is overdue for disposition?" *Findings* → "have we seen this before, and how did we rate it?" *Reports* → "what is in QA and what is late?" *Documents* → "what is unsigned or expiring?"
- **Library** — the controlled content plane. Separated from work because it changes under a different regime and by different people.
- **Oversight** — read-only practice state for Management.
- **Administration** — platform control, deliberately distant from client work.

### What was deliberately *not* made top-level

| Concept | Where it lives instead | Why |
|---|---|---|
| Tasks | Engagement → Now / Runbook; aggregated in Today | Only meaningful inside an engagement |
| Checklists | Engagement → Checklists & Gates | Same |
| Questionnaires (responses) | Engagement → Questionnaire | Same. *Templates* live in Library |
| Evidence | Engagement → Evidence; register for cross-view | A global evidence list is a confidentiality hazard |
| Findings | Engagement → Findings; register for cross-view | Same |
| Reports | Engagement → Report; register for QA queue | Same |
| Documents | Engagement → Documents; templates in Library | Instances belong to engagements |
| Services | Library → Services | Reference content |
| Runbooks | Library → Runbooks | Content plane |
| Tools | Library → Tools | Content plane |
| Knowledge Base | Library → KB, and contextually inside procedures | Its highest value is *in situ*, not as a destination |
| Reviews / QA | Today (queue) + Engagement → Report | A queue, not a place |
| Audit Log | Administration; scoped view inside each engagement | Two different audiences, two different scopes |
| Dashboard | Split into Today (personal) and Oversight (practice) | "Dashboard" is not a user need; it is two different user needs wearing one word |

---

## 3. The engagement workspace

Once inside an engagement, the whole context changes. This is where a consultant spends the overwhelming majority of their time.

```
┌────────────────────────────────────────────────────────────────────────────────┐
│ CLIENT CONFIDENTIAL · ENG-2026-0141 · Meridian Logistics · VAPT External       │  ← classification bar
├────────────────────────────────────────────────────────────────────────────────┤
│ Phase 4 Examine · SF-SEC-VAP-EXT v1.2 · Window closes in 2d 4h · ● 2 gates open│  ← engagement header
├────────────────────────────────────────────────────────────────────────────────┤
│  Now │ Runbook │ Checklists & Gates │ Questionnaire │ Evidence │ Findings │     │
│      │         │                    │               │          │          │     │
│  Report │ Documents │ Activity                                                  │
└────────────────────────────────────────────────────────────────────────────────┘
```

| Tab | Purpose | Default for |
|---|---|---|
| **Now** | The next action, in context. The North Star screen. | Analyst |
| Runbook | The full phase/procedure structure — progress and navigation | |
| Checklists & Gates | Gate status and blockers; every checklist in one place | Engagement Manager |
| Questionnaire | Client information: asked, answered, verified, outstanding | |
| Evidence | Register, custody, integrity, disposition | |
| Findings | Draft, review, confirm, retest | |
| Report | Build, review, release, acceptance | Reviewer |
| Documents | Contracts, authorisations, executed instances | |
| Activity | Immutable timeline of everything that happened | |

**The classification bar is persistent and cannot be dismissed.** It names the client and engagement on every screen, and it is carried into print and export. Working on two engagements in two browser tabs is normal; attaching evidence to the wrong one is a serious incident. A permanently visible client name is a cheap and effective defence.

---

## 4. Navigation depth and progressive disclosure

The brief: *"A consultant under time pressure should not be forced to read an enormous page to find the next action."*

Three depths, with a hard rule about which is the default:

```
DEPTH 1 — DIRECTIVE        one action, one line, always visible
  "Acquire memory from SRV-DB-02 before shutdown."
  [ Start ]  [ Blocked ]  [ Not applicable ]

DEPTH 2 — PROCEDURE        expanded on demand, or automatically on Start
  steps · inputs · approved tools · evidence to capture · expected output ·
  stop conditions · escalation contacts

DEPTH 3 — REFERENCE        one click further
  full rationale · KB articles · standards references · prior engagement
  examples · runbook version notes · training material
```

**Depth 1 is the default. Always.** Depth 2 opens on demand or when work starts. Depth 3 is never automatic.

The exception, and it is the important one: **stop conditions and escalation contacts are promoted to Depth 1** whenever a procedure carries them. They are the information a consultant needs at the exact moment they are least able to go looking for it.

### Navigation rules

1. **Two clicks to the next action** from anywhere: `Today → task`, or `Engagement → Now`.
2. **The engagement is never lost.** Client and engagement identity are present on every screen inside an engagement.
3. **Deep-linkable.** Every procedure, finding, evidence item and gate has a stable URL. Consultants share links in chat; the platform should make that reliable rather than fight it.
4. **The back button works.** Modals are for confirmation and capture, never for navigation or extended work.
5. **Blocked is a state, not a dead end.** Every block names a reason, an owner and a next action.

---

## 5. Search

One search across everything the user is permitted to see, scoped by default to the current engagement with an explicit widening step. Typed results — Engagement · Client · Procedure · Evidence · Finding · Runbook · Tool · Document · KB — with the type visible in the result row.

Identifier search must be exact-match and instant: `ENG-2026-0141`, `F012`, `E007`, `SF-SEC-VAP-EXT`, a SHA-256 prefix, an IP, a hostname. These are how consultants actually refer to things to each other, which is precisely why the ID scheme is short, typeable and rendered in monospace.

---

## 6. Mobile and field use

Not a responsive afterthought — a specific, narrow set of situations:

| Situation | Need |
|---|---|
| Evidence collection at a client site | Capture custody events, photograph an item, record a transfer, scan a seal number |
| A consultant challenged on site | Retrieve the Letter of Authorisation **immediately** |
| An incident at 2am | Read the runbook, see stop conditions, reach the escalation contact in one tap |
| A manager away from a desk | Approve a gate, read a blocker, respond to an escalation |

Everything else — report authoring, analysis, runbook editing — is desktop work and should not be compromised to accommodate a phone. The mobile surface is small, deliberate, and built for the four situations above.
