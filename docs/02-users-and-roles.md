# 02 — Users, Roles & Access Model

> **Status — `PROPOSED`, awaiting approval.** Structural and design proposals, not confirmed
> Sleuth practice. See [`17-governing-constraints.md`](17-governing-constraints.md). Partly superseded on arrival of Sleuth's engagement-type list —
> [`19-engagement-type-specification.md`](19-engagement-type-specification.md) §5.


**Note on evidence:** the website names no individuals, no team size and no certifications (research §4.4). Everything about *who actually exists* at Sleuth is **Needs Confirmation**. What follows is a role model derived from the brief and from the work the services describe, not a claim about Sleuth's staffing.

---

## 1. The five roles, and what each one is actually doing

Roles are defined by the question the person is trying to answer, because that determines the screen they need.

### Analyst
> *"What do I need to do next, and how exactly do I do it?"*

Executes procedures, captures evidence, drafts findings. Usually working inside **one** engagement at a time, often under time pressure, sometimes on a client site, sometimes at 3am during an incident. Frequently the least-senior person in the room and the one making the most consequential small decisions.

- **Needs:** a single unambiguous next action; the procedure detail on demand, not by default; frictionless evidence capture; a visible way to say "I am blocked" or "this needs review" without stopping work.
- **Must not be able to:** approve their own work, pass a gate, release a report, dispose of evidence, or see engagements they are not assigned to.
- **Biggest failure mode this role causes:** doing correct technical work that is later unusable because the evidence trail or authorisation was incomplete at the time.

### Reviewer
> *"Is this defensible?"*

Technical quality control. Reviews evidence integrity, analytical reasoning, finding severity and report accuracy. May be a senior analyst wearing a second hat on someone else's engagement — but **never on their own**.

- **Needs:** a review queue; a diff of what changed since last review; the finding *and its evidence* side by side; a way to reject with a specific, actionable reason rather than a comment thread.
- **Must not be able to:** review work they authored. This is enforced by the system, not by convention.
- **Biggest failure mode this role prevents:** a conclusion that outruns its evidence.

### Engagement Manager
> *"Is this engagement on track, in scope, and safe to proceed?"*

Owns scope, authorisation, schedule, client communication and delivery. Runs several engagements at once. The person a client calls.

- **Needs:** gate status across a portfolio at a glance; what is blocked and on whom; scope-change control; delivery and acceptance tracking.
- **Can:** approve gates (within limits), request overrides, approve scope changes, release deliverables.
- **Biggest failure mode this role causes:** scope creep that was never re-authorised, and delivery to the wrong recipient.

### Management
> *"What is the state of the practice?"*

Operational and commercial oversight. Reads, does not execute.

- **Needs:** pipeline, capacity, gate bottlenecks, overdue items, evidence-disposition liabilities, quality signals (rework rate, review rejections).
- **Should be read-only by default over engagement content**, with deliberate escalation to read specific evidence — because "the boss can see everything" is how least-privilege quietly dies.

### Administrator
> *"Is the platform itself trustworthy?"*

Manages users, roles, the service catalogue, runbook publication, tool approvals, templates and configuration.

- **Critically: Administrator is a platform role, not an engagement role.** An administrator can grant themselves access to an engagement, but that act is logged, visible to Management, and notifies the Engagement Manager. Admin power should be *auditable*, not *invisible*.
- **Must not be able to:** silently read client evidence, edit an audit log, or alter an approved runbook version in place.

### Two roles the brief does not name but the work requires

| Proposed role | Why | Recommendation |
|---|---|---|
| **Runbook Author / Practice Lead** | 16 of 21 services have no published methodology (research §2). Someone must own writing and approving each runbook, and that is a different authority from platform administration. | Add as a distinct role. It maps directly to the Owner/Reviewer/Approver fields the brief already requires on every runbook (§18). |
| **Client Contact** | Questionnaires must be answered by the client; prerequisites must be supplied by the client. | **Do not build this in Phase 1.** Record client contacts as data; keep questionnaire capture consultant-mediated until the platform has earned a security review. See `11-assumptions-and-open-questions.md`, Decision D3. |

---

## 2. Access model: role plus reach

A role alone is the wrong unit of access. An Analyst on the Acme DFIR engagement should have no visibility whatsoever into the Contoso spyware examination — different client, different confidentiality, possibly a personal-safety matter.

So access is two-dimensional:

```
CAN THIS PERSON DO IT?      → Role         (capability)
CAN THEY DO IT *HERE*?      → Membership   (reach)

Permission = Role capability  ∧  Engagement membership  ∧  Object-level rule
```

**Engagement membership** is explicit and time-bounded. Nobody has standing access to all engagements — not Management, not Administrators. Access to an engagement you are not a member of requires a break-glass action that is logged and notified.

### Object-level rules that override everything

Three rules sit above the matrix and cannot be granted away:

1. **Segregation of duty.** `author_id ≠ reviewer_id` on every finding, report and gate approval. Enforced at write time.
2. **Append-only audit.** No role can modify or delete an audit event. The Administrator role included.
3. **Version immutability.** No role can edit an Approved runbook version, an executed document, or a delivered report. Changes create a new version; the old one remains retrievable for the engagements that used it.

---

## 3. Capability matrix

`✓` = permitted · `M` = permitted only within engagements the user is a member of · `R` = read only · `⊘` = explicitly denied · `!` = permitted but logged as a privileged action and notified

| Capability | Analyst | Reviewer | Eng. Manager | Management | Admin | Runbook Author |
|---|---|---|---|---|---|---|
| View assigned engagement | M | M | M | R | ! | ⊘ |
| View any engagement | ⊘ | ⊘ | ⊘ | R (metadata) | ! | ⊘ |
| Execute task / update checklist | M | M | M | ⊘ | ⊘ | ⊘ |
| Register evidence | M | M | M | ⊘ | ⊘ | ⊘ |
| **Download / open evidence content** | M ! | M ! | M ! | ⊘ | ! | ⊘ |
| Record custody transfer | M | M | M | ⊘ | ⊘ | ⊘ |
| Authorise evidence **disposition** | ⊘ | ⊘ | M ! | ⊘ | ⊘ | ⊘ |
| Draft finding | M | M | M | ⊘ | ⊘ | ⊘ |
| Approve finding severity | ⊘ | M | ⊘ | ⊘ | ⊘ | ⊘ |
| Complete technical review (QA) | ⊘ | M | ⊘ | ⊘ | ⊘ | ⊘ |
| Pass **Authorisation Gate** | ⊘ | ⊘ | M | ⊘ | ⊘ | ⊘ |
| Pass **QA Gate** | ⊘ | M | ⊘ | ⊘ | ⊘ | ⊘ |
| **Override any gate** | ⊘ | ⊘ | request | approve ! | ⊘ | ⊘ |
| Approve scope change | ⊘ | ⊘ | M | ⊘ | ⊘ | ⊘ |
| Release report to client | ⊘ | ⊘ | M | ⊘ | ⊘ | ⊘ |
| Close engagement | ⊘ | ⊘ | M | ⊘ | ⊘ | ⊘ |
| Author runbook (Draft) | ⊘ | ⊘ | ⊘ | ⊘ | ⊘ | ✓ |
| Approve runbook → Approved | ⊘ | ⊘ | ⊘ | ✓ | ⊘ | ⊘ |
| Approve a tool for use | ⊘ | ⊘ | ⊘ | ⊘ | ✓ | propose |
| Manage users & roles | ⊘ | ⊘ | ⊘ | ⊘ | ✓ | ⊘ |
| Read audit log | ⊘ | ⊘ | M | R | ✓ | ⊘ |
| Modify audit log | ⊘ | ⊘ | ⊘ | ⊘ | ⊘ | ⊘ |
| Export Excel register | M | M | M | R | ⊘ | ⊘ |
| Bulk export / full engagement archive | ⊘ | ⊘ | M ! | ⊘ | ! | ⊘ |

### Three deliberate choices in that matrix

**Gate override requires two people at different levels.** The Engagement Manager — the person under client pressure — can request an override but cannot grant it. Management grants it. This matters most for the Authorisation Gate, where the pressure to "start Monday, paperwork follows" is strongest and the consequence of yielding is the most serious.

**Runbook approval sits with Management, not Administrators.** Approving a methodology is a professional judgement about how Sleuth does its work. Administering a platform is not. Separating them stops the runbook library from being quietly edited by whoever has the keys.

**Evidence download is always a logged, privileged action — for everyone.** Not because colleagues are untrusted, but because the ability to state precisely who opened an item and when is exactly what makes a forensic report defensible. The log is the product, not an overhead.

---

## 4. What each role sees when they log in

| Role | Lands on | Because |
|---|---|---|
| Analyst | **Today** — my tasks across my engagements, single next action surfaced first | They want one answer: what now |
| Reviewer | **Today**, filtered to the review queue, oldest-blocking first | They are a bottleneck; queue order is the job |
| Engagement Manager | **Engagements** portfolio, sorted by gate risk then by date | They manage exceptions, not tasks |
| Management | **Oversight** dashboard | They read state, not content |
| Administrator | **Administration** | They should have to navigate deliberately into client work, never land in it |
| Runbook Author | **Practice Library → Runbooks**, filtered to those they own with a review date approaching | Their work is content, not engagements |
