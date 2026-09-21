# 39 — API Surface & Permission Enforcement

> **Status — `PROPOSED`, implementation-ready specification.**
> **Rule 7 holds: this is a specification, not code.** No source is committed.

---

## 1. Shape

Server-rendered pages for the operational surface, with a JSON API beneath for the interactive parts
(gate evaluation, evidence capture, search, checklist state). One route table serves both — an HTML
request and a JSON request hit the same handler and the same authorisation.

**Why not a single-page app.** Correctness here depends on the server's view of state: whether a gate
passes, whether a finding may enter a report, whether an override has expired. A client-side cache of
those answers is a cache of security decisions. Dense tables, print-quality output and strong URL
semantics also favour server rendering.

---

## 2. Route table

`{eng}` = engagement code. All routes are engagement-scoped unless marked *(global)*.

### Work
| Method | Route | Purpose |
|---|---|---|
| GET | `/today` | Personal queue *(global)* |
| GET | `/e/{eng}` | Engagement → Now |
| GET | `/e/{eng}/runbook` | Phase/procedure tree |
| GET | `/e/{eng}/p/{proc}` | Procedure execution view |
| POST | `/e/{eng}/p/{proc}/start` | Begin — records actor and time |
| POST | `/e/{eng}/p/{proc}/complete` | Complete. **Rejected if required evidence is missing** |
| POST | `/e/{eng}/p/{proc}/block` | Requires reason + owner |
| POST | `/e/{eng}/p/{proc}/na` | Requires reason |
| PATCH | `/e/{eng}/checklist/{item}` | State change. Reason required for `blocked` / `not_applicable` |
| POST | `/e/{eng}/decision/{tree}` | Record a traversal |

### Gates
| Method | Route | Purpose |
|---|---|---|
| GET | `/e/{eng}/gates` | All gates, live evaluation |
| GET | `/e/{eng}/gates/{gate}` | One gate, per-condition detail |
| POST | `/e/{eng}/gates/{gate}/evaluate` | Force re-evaluation |
| POST | `/e/{eng}/gates/{gate}/pass` | Role-restricted per gate |
| POST | `/e/{eng}/gates/{gate}/override/request` | Manager. Justification + expiry required |
| POST | `/e/{eng}/gates/{gate}/override/approve` | Management. **`requested_by ≠ approved_by`** |

**Gate evaluation is never cached.** It reads current state on every request. A gate that passed an
hour ago may be blocked now — an expired Letter of Authorisation, a failed integrity check, a
withdrawn approval.

### Evidence
| Method | Route | Purpose |
|---|---|---|
| GET | `/e/{eng}/evidence` | Register |
| POST | `/e/{eng}/evidence` | Register an item |
| GET | `/e/{eng}/evidence/{id}` | Record + custody strip |
| POST | `/e/{eng}/evidence/{id}/verify` | Record verification hash. **Mismatch is terminal** |
| POST | `/e/{eng}/evidence/{id}/custody` | Append a custody event *(insert-only)* |
| POST | `/e/{eng}/evidence/{id}/derive` | Create a working copy. Verifies parent first |
| POST | `/e/{eng}/evidence/{id}/disposition` | Manager only. Step-up auth |

> **There is no evidence content endpoint.** No upload, no download, no signed URL *(Rule 3)*.
> `GET /evidence/{id}` returns the record; the content lives in Sleuth's lab storage and
> `storage_location` says where.

### Findings, reports, documents
`/e/{eng}/findings` · `/findings/{id}` · `/findings/{id}/review` *(Reviewer, non-author)* ·
`/findings/{id}/severity` *(rationale required)* · `/findings/{id}/retest`
`/e/{eng}/report` · `/report/build` · `/report/review` · `/report/release` *(Release Gate + step-up)* ·
`/report/acceptance`
`/e/{eng}/documents` · `/documents/{id}/execute`

### Library *(global)*
`/library/runbooks` · `/runbooks/{code}/v/{ver}` · `/runbooks/{code}/v/{ver}/publish` *(Management)* ·
`/library/modules/{code}/impact` *(pre-publish impact analysis)* · `/library/validation` *(SME queue)* ·
`/library/gaps` *(gap register)* · `/library/tools` · `/library/templates`

### Oversight & admin *(global)*
`/oversight` · `/oversight/obligations` · `/oversight/overrides` · `/oversight/deltas` ·
`/admin/users` · `/admin/audit` · `/admin/break-glass` *(logged, notified)*

### Exports
`POST /e/{eng}/export/{workbook}` · `POST /export/{register}` *(global registers)*.
Every export writes an `audit_event` with the filters applied. Bulk export requires Manager approval.

---

## 3. Permission enforcement — four layers

Each layer independently sufficient to deny. **Defence in depth is the point: any single layer being
wrong should not open access.**

```
1  ROUTE GUARD      Does this role hold the capability at all?
                    Fails fast, before any query runs.
                    Source: the capability matrix (02 §3).

2  MEMBERSHIP       Is the user a member of this engagement, in date?
                    Or an approved, logged break-glass session?

3  OBJECT RULE      The rules no role can be granted past:
                    · author ≠ reviewer
                    · append-only audit and custody
                    · version immutability
                    · non-overridable gates
                    · vCISO cannot authorise own-firm testing

4  ROW-LEVEL        PostgreSQL RLS. The database refuses even when a
   SECURITY         WHERE clause is forgotten.
```

Layer 4 exists because layers 1–3 are application code, and application code has bugs. A missed
`WHERE engagement_id = ?` in a reporting query is the single most common way a system like this leaks
one client's data into another client's view. RLS makes that failure mode impossible rather than
unlikely.

### Denials are logged

Every denial writes an `audit_event` with the attempted action. A pattern of denials is a signal —
either someone needs access they do not have, or something is wrong. Silent denials hide both.

---

## 4. Step-up authentication

Re-authentication within the last 5 minutes, required for:

| Action | Why |
|---|---|
| Evidence disposition | Irreversible. Destroys client property |
| Gate override approval | Bypasses a control |
| Report release | Sends client-confidential material externally |
| Bulk export | Concentrates data |
| User or role change | Changes who can do what |
| Break-glass access | Reaches into an engagement the user is not on |
| Runbook version publish | Changes practice-wide methodology |

**Deliberately not step-up:** anything on the critical path during an active incident — evidence
registration, custody events, procedure completion. Forcing re-authentication at 4am mid-acquisition
creates worse risks than it removes. The protection there is the audit trail, not friction.

---

## 5. Concurrency

Two people editing the same engagement is normal; two people editing the same finding is not.

| Object | Strategy |
|---|---|
| Finding, report section, questionnaire answer | **Optimistic locking** on `version`. Conflict returns both versions and the diff |
| Checklist item, task state | Last-write-wins, but every transition is audited, so the history is recoverable |
| Custody and audit events | Append-only. No conflict is possible |
| Gate pass | **Serialised.** A gate cannot be passed twice; the second attempt sees the first's snapshot |
| Runbook version publish | Advisory lock on the module. Impact analysis and publish are one transaction |

Writes that change engagement state are **idempotent by client-supplied key**, so a retried request
after a dropped connection does not double-register evidence or double-pass a gate. This matters
disproportionately during incidents, which is exactly when connections are flaky and people retry.

---

## 6. Errors

Errors are operational instructions, not status codes. Every 4xx names what is wrong, what would fix
it, and who owns it.

```json
{
  "error": "gate_blocked",
  "gate": "authorisation",
  "message": "Technical execution cannot begin. 3 conditions unmet.",
  "conditions": [
    { "code": "loa_executed", "state": "failed",
      "detail": "Letter of Authorisation not received. Issued 8 days ago.",
      "owner": "R. Mehta", "remediation": "Record as received, or resend." }
  ],
  "override_available": true,
  "override_requires": "Management approval, written justification, expiry date"
}
```

Never leak across the boundary: another engagement's existence, another client's name, whether a
record exists when the user lacks reach. **Not-permitted and not-found return the same shape** — the
distinction is in the audit log, not the response.

---

## 7. Integration surface — deliberately small

| Integration | Direction | Phase |
|---|---|---|
| Identity provider (OIDC) | in | 0 |
| Enquiry intake from the website contact form | in | 1 — mirrors the live field set |
| Calendar (testing windows, cycles) | out | 6 |
| Notification (escalations, gate blocks, review queue) | out | 1 |

**Explicitly not integrated:** scanners and testing tools *(the catalogue references tools, it does
not run them)* · SIEM *(the platform is not a detection system)* · billing *(Decision D4)* · client
systems of any kind.

Webhooks are outbound-only, signed, with no client-confidential content in the payload — an
identifier and an event type, never a finding or an evidence detail. A notification that leaks its
subject is a disclosure.

---

## 8. Rate limiting and abuse

Authentication endpoints rate-limited per account and per source. Export endpoints limited per user
per hour — a legitimate user does not need forty exports in an hour, and an exfiltrating one does.
Search is limited to prevent enumeration of identifiers the user cannot reach.

---

## 9. Counts

| | |
|---|---|
| Routes specified | **58** |
| Enforcement layers | 4, independently sufficient |
| Step-up actions | 7 |
| Explicitly excluded integrations | 4 |
| Endpoints serving evidence content | **0** *(Rule 3)* |
