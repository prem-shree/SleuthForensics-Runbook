# 40 — Build & Operations

> **Status — `PROPOSED`, implementation-ready specification.** Rule 7: specification, not code.

How the platform is built, seeded, migrated, released, backed up and observed — and how it behaves
when it, or something around it, fails.

---

## 1. Environments

```
PRODUCTION    real client data · full controls · MFA enforced · restricted access
STAGING       synthetic data only · production-like configuration · used for release verification
DEVELOPMENT   synthetic data only · no production access of any kind
```

**No real client data leaves production. Ever.** Not "anonymised", not "just this once to reproduce a
bug". Anonymisation of forensic and incident data is unreliable — hostnames, IP ranges, timestamps
and file paths re-identify a client trivially, and an incident narrative is identifying on its own.

### The seeding guard

Non-production refuses data that looks real. Heuristics, applied at load:

| Check | Rejects |
|---|---|
| Domain realism | Anything not under `.example`, `.test`, `.invalid` |
| IP ranges | Anything outside RFC 5737 / RFC 3849 documentation ranges |
| Client names | Anything matching a production client name or a known company list |
| Email addresses | Anything not `@example.com` |
| Hashes | Anything matching a production evidence hash |

A rejected load fails loudly with the offending rows named. The guard is a control, not a
convenience: the common path to a leak is a developer loading a production export to reproduce
something, intending to delete it afterwards.

---

## 2. Two kinds of migration

The platform has an unusual property: **its content is versioned data, not code.** So there are two
migration systems, and conflating them causes real damage.

### Schema migrations — ordinary
Forward-only, one transaction each, reversible by a written-down plan rather than an automatic down
migration. Tested against a restored production-shaped dataset in staging before release.

Two schema objects need care because they are load-bearing for defensibility:

- **Append-only tables** (`custody_event`, `audit_event`). A migration must never rewrite history. If
  a column must be added, it is added nullable and back-filled as `NULL`, never inferred. An inferred
  custody event is a fabricated one.
- **Hash chains.** Adding a column that participates in the `audit_event` hash breaks verification of
  everything before it. So the chain hashes a **fixed, versioned field set**, and a change to that set
  starts a new chain segment with a recorded boundary, rather than invalidating the past.

### Content migrations — the unusual ones

When a shared module version changes, dependent runbooks and live engagements must be handled per
`20-shared-module-inheritance.md` §6. This is a *data* migration governed by approval, not a
deployment step:

```
module_version published
  ├─ editorial   → dependent runbooks auto-adopt. No approval. No engagement touched.
  ├─ substantive → dependent runbooks → pending_re_approval.
  │                Owners accept individually. Live engagements untouched.
  └─ breaking    → as above, flagged blocking, plus a per-engagement migration
                   decision: migrate, or continue pinned with a recorded reason.
```

**No deployment, at any approval level, rewrites what a live engagement is executing.** That property
is worth more than the convenience it costs.

---

## 3. Release process

1. Change merged behind a flag where it alters behaviour visible to an analyst.
2. Schema migration applied to staging; restored-production-shape test suite run.
3. **Gate-evaluation regression suite** — the highest-risk surface. Every gate, every condition, both
   outcomes, plus the non-overridable cases. A gate that wrongly passes is worse than a crash.
4. **Invariant suite** — all 15 from `37` §7, asserted at the database level, not the application.
5. Accessibility and print check on any changed view.
6. Deploy. Migration first, application second, both inside a maintenance window if the migration is
   not backward-compatible.
7. Post-deploy: verify audit chain continuity and RLS policy presence.

Step 7 is not ceremonial. A dropped RLS policy after a migration is silent, and it is the failure that
would matter most.

---

## 4. Backup and recovery

| | |
|---|---|
| Database | Continuous archiving plus daily full. Encrypted at rest with a separate key |
| Retention | Aligned to the longest applicable obligation *(`‹PH-13›`, counsel E5)* |
| **Restore testing** | **Quarterly, to an isolated environment, with a recorded result.** An untested backup is a hypothesis |
| RTO / RPO | `‹PH-24›` — proposed RTO 4h, RPO 15 min. **Needs Sleuth Confirmation** |

### Deletion must propagate

When an evidence *record* is dispositioned, its content was never in the platform *(Rule 3)*, so
nothing propagates — one of the quieter benefits of the register-only decision.

But when a **record** must genuinely be erased — a retention period expiring, or a legal requirement —
the erasure must reach backups, or the destruction certificate asserts something untrue. Mechanism:
crypto-shredding. Per-engagement keys mean destroying the key renders that engagement's archived rows
unrecoverable without rewriting every backup.

**What is never erased:** the evidence record's identifier, hashes, custody chain and disposition
certificate. Content is destroyed; provenance is not. That distinction is the whole point.

---

## 5. Continuity during an incident

The platform being unavailable during a client's ransomware incident would be a serious failure — the
tool would have made things worse than no tool.

**Required offline path.** For any active A3 engagement, exportable to PDF and usable with no
platform:

- the pinned runbook, rendered in full
- current stop conditions and escalation contacts
- the chain-of-custody form, in a signature-ready layout
- the evidence register as it stands
- the questionnaire responses captured so far

Regenerated automatically whenever the engagement's state materially changes, and held by the
Engagement Manager. **A consultant standing in a server room at 3am must not be blocked by an
authentication service.**

On recovery, offline custody events are entered with their true `occurred_at` and a recorded
`entered_at` — never back-dated silently. The gap between the two is visible and is exactly the kind
of thing a report's limitations section should carry.

---

## 6. Observability

### Logged
Request identity, route, outcome, duration · every authorisation denial · every gate evaluation and
result · every state transition · every export · every break-glass · job outcomes · **audit chain
verification results**.

### Never logged
Client evidence detail · finding content · questionnaire answers · report text · anything from an
`access_grant` beyond the reference · personal data of any kind.

> Application logs are the most commonly over-shared artefact in any system — shipped to a vendor,
> read by a contractor, retained for years in a different jurisdiction. Whatever is safe in the
> database may not be safe in a log line, so the boundary is drawn deliberately rather than inherited.

### Alerts that matter
Audit chain verification failure *(page immediately)* · RLS policy missing after deploy *(page)* ·
evidence integrity failure recorded · break-glass used · gate override approved · emergency
authorisation approaching its 24-hour ratification deadline · evidence disposition overdue.

Every one of those is a business event, not a technical one. The platform's monitoring is mostly
about obligations, not uptime.

---

## 7. Failure scenarios worked through

| Scenario | Behaviour |
|---|---|
| Platform unavailable mid-incident | Offline pack (§5). Custody continues on paper, entered on recovery with true times |
| A tool version is found defective | Query `evidence_item` by `tool_version_id`. Every affected engagement identified in seconds — the reason the field exists |
| An analyst leaves mid-engagement | Membership expires. Their work, evidence and findings remain attributed. Reassignment is a logged act |
| A client disputes a finding months later | Evidence retained per A2 retention; request/response settles it. Without it, credibility rests on recollection |
| A runbook is found wrong after use | New version. Engagements that ran the old one keep it, and their reports still describe what was actually done |
| Audit chain verification fails | Page. Freeze writes to the affected range. Treat as a security incident until disproven |
| Someone must be removed for cause | Access revoked; audit retained; any engagement they touched is flagged for review. The record is the point |

---

## 8. What is deliberately not built

| Excluded | Why |
|---|---|
| Multi-tenancy | One firm. Do not build for a market that does not exist |
| High availability across regions | Residency is unresolved *(C4)* and the cost is unjustified at this scale |
| Real-time collaborative editing | Optimistic locking is sufficient and far simpler to reason about |
| Mobile app | A narrow responsive surface covers the four field situations *(`09` §6)* |
| Automated tool orchestration | Different product. The catalogue references tools; it does not run them |
| AI assistance | Not ruled out, but on a platform whose value is evidentiary defensibility, generated content needs a far clearer provenance story before it goes near a finding or a report |

---

## 9. Placeholders

| Ref | Placeholder | Default |
|---|---|---|
| `‹PH-24›` | RTO / RPO | Proposed 4h / 15 min. **Needs Sleuth Confirmation** |
| `‹PH-25›` | Offline pack regeneration trigger | On phase change, gate change, or every 4h during an active A3 engagement |
| `‹PH-26›` | Log retention | 90 days hot, 1 year cold — pending E5 |
| `‹PH-27›` | Hosting model | Self-hosted, India region assumed *(C4)* |
