# 27 — Engagement Type Specifications: A4 Continuous & Readiness

> **Status — Draft / Needs SME Validation.** Provenance: `PROPOSED` (structure),
> `INDUSTRY-PRACTICE` (method), `SITE-SUGGESTED` (scope items). Nothing is validated.

**§1 derived** from `core.*` (`22`) + `arch.A4` (`23`).

> **A4's defining property: there is no closure while the contract runs.** No disposition, no
> lessons-learned, no Closure Gate. Instead each cycle closes, and authorisation is periodically
> *renewed* — which is the failure mode this archetype is most prone to, and `A4-07` exists to
> prevent it.

---

# `SF-A4-ASM` — Attack Surface & Threat Intelligence Monitoring

**Public service:** 18 Threat Intelligence & Attack-Surface Monitoring · **Archetype:** A4

### §2 Service-specific procedures `[SERVICE]`

| ID | Procedure | Records |
|---|---|---|
| `ASM-01` | Perimeter definition — domains, IP ranges, brands, subsidiaries, acquisitions | Monitored scope, ownership basis |
| `ASM-02` | **Ownership verification for every monitored asset** — monitoring something the client does not own creates its own problems | Per-asset ownership, verified |
| `ASM-03` | External attack surface discovery and mapping | Assets discovered, method |
| `ASM-04` | Exposed service and resource identification | Exposures with severity |
| `ASM-05` | Leaked credential monitoring — **the fact and source of exposure, never the credential** *(Rule 4)* | Account identifier, source, date, **no credential value** |
| `ASM-06` | Dark web and underground forum monitoring *(`SITE-DERIVED`)* | Mentions, context, source class |
| `ASM-07` | Brand impersonation and phishing domain detection | Domains, similarity, status |
| `ASM-08` | Threat actor tracking relevant to the client's sector | Actors, activity, relevance basis |
| `ASM-09` | Vulnerability intelligence prioritised against discovered assets | Vulnerabilities, affected assets, urgency |
| `ASM-10` | Cycle delta analysis *(runs `A4-03`)* | New, changed, resolved |
| `ASM-11` | Alert triage and disposition *(runs `A4-04`)* | Per-alert outcome |

### §3 Client information `[SERVICE]`
Known domains, brands and IP ranges · subsidiaries and acquisitions · **executive names to monitor
and their consent** · sectors and regions of concern · known threat actors of concern · existing
intelligence feeds · alert routing and tolerance · monitoring frequency · takedown expectations.

> **`ASM-05` and Rule 4.** Where a credential exposure is detected, the platform records *that an
> account's credential was exposed, in which breach or source, and when*. It never records the
> credential. The client is told to rotate it. This is the correct handling regardless of Rule 4 —
> a monitoring service that accumulates its clients' leaked passwords has built a liability.

### §5 Authorisation `[SERVICE]`
Standing authorisation for passive monitoring. ⊗ **Any active interaction with a discovered asset is
out of scope** — that is an A2 engagement. This boundary blurs easily and should be explicit in the
scoping document.
✋ Executive-name monitoring requires the individual's consent, not only the employer's.
`A4-07` re-authorisation each period.

### §7 Phases
Continuous cycles. No Phase 9 Validate, no Phase 10 Close.

### §9 Evidence `[ARCH:A4]`
Cycle snapshots · screenshots of exposures as observed · source references. Retained so a "this was
exposed on this date" claim is supportable later. **Register-only.**

### §10 Decisions
Alert severity and routing · what constitutes escalation to an incident *(pre-agreed)* · whether a
discovered asset is in scope · takedown pursuit.

### §11 Stops `[SERVICE]`
⊗ Evidence of active compromise discovered — ▲ immediately, propose an IR engagement *(`A4-05`)*.
⊗ A discovered asset proves to belong to a third party — remove from monitoring, notify the client.

### §14 Deliverables
Attack surface assessment report · exposed asset inventory with risk assessment · threat intelligence
briefings · monitoring alerts and notifications · remediation recommendations *(`SITE-DERIVED`)* ·
per-cycle delta report.

### §15 Follow-up
Each cycle validates the last. Coverage review per `A4-08`.

### §16 Closure
**None while the contract runs.** On contract end: final cycle report · monitoring withdrawn and
confirmed · retained snapshots dispositioned · standing authorisation formally ended.

**`[GAP]` cycle cadence and alert severity — ✓ **CLOSED 2026-09-21**:** continuous discovery · weekly delta · monthly
report · quarterly coverage review; alert response Critical immediate / High 24h / Medium-Low in cycle
(`32` §11).
**`[GAP]` takedowns — ✓ **CLOSED 2026-09-21**: not offered.** `SF-A4-ASM` reports and advises on the takedown route; it
does not pursue takedowns on the client's behalf (`32` §8).

---

# `SF-A4-VCI` — vCISO Retainer

**Public service:** 21 Compliance, GRC & vCISO *(vCISO half)* · **Archetype:** A4

> Structurally unlike everything else in the catalogue: the deliverable is **ongoing judgement**
> rather than a report. The platform's job here is continuity and accountability — what was advised,
> when, and what happened — not procedural guidance.

### §2 Service-specific procedures `[SERVICE]`

| ID | Procedure | Records |
|---|---|---|
| `VCI-01` | Engagement charter — time commitment, decision authority, reporting line, boundaries | Charter, approved by |
| `VCI-02` | First-90-days baseline and priorities | Baseline, priorities, agreed by |
| `VCI-03` | Security strategy development and maintenance | Strategy, versions, approval |
| `VCI-04` | Risk register ownership and periodic review | Register, review dates, changes |
| `VCI-05` | Programme oversight — tracking initiatives against plan | Status per initiative |
| `VCI-06` | **Advisory record** — material advice given, when, to whom, and the decision taken | Advice log with outcomes |
| `VCI-07` | Board and executive reporting | Reports, cadence, recipients |
| `VCI-08` | Incident escalation participation | Involvement record |
| `VCI-09` | Period review and re-prioritisation | Period outcomes, next priorities |
| `VCI-10` | Handover documentation — maintained continuously, not written at the end | Current handover pack |

`VCI-06` is the procedure that protects both parties. A vCISO advises; the client decides. Recording
what was advised and what was decided — separately — is what makes the relationship accountable, and
it is what a vCISO will want if a decision they advised against later goes wrong.

`VCI-10` is maintained continuously for the same reason a handover written in the final week is
always inadequate: nobody remembers the context by then, and a retainer can end abruptly.

### §3 Client information `[SERVICE]`
Time commitment expected · decision authority granted · reporting line · board cadence · existing
security function and its maturity · current initiatives and budget · risk appetite · **what the
client expects the vCISO to own versus advise on** — the most common source of friction in this
engagement type, and worth settling in writing at `VCI-01`.

### §4 Documents `[SERVICE]`
Retainer agreement · engagement charter · **conflict and independence declaration** *(a vCISO sits
inside the client's governance; where Sleuth also delivers testing or assessment work to the same
client, that overlap must be declared and managed)*.

### §5 Authorisation `[SERVICE]`
Standing, per the retainer. `A4-07` re-authorisation at each renewal.
⊗ **The vCISO does not authorise Sleuth's own testing engagements for the same client** —
self-authorisation is exactly the conflict `02-users-and-roles.md` separates elsewhere. A client-side
authoriser independent of the vCISO must sign.

### §7 Phases
Recurring periods. No Examine/Analyse/Report cycle in the usual sense — `VCI-07` reporting replaces it.

### §9 Evidence
Advisory records · reports issued · decisions taken by the client. **Register-only.**

### §11 Stops `[SERVICE]`
⊗ The client instructs an action the vCISO considers materially unsafe — record the advice and the
decision, ▲ Management, and consider whether the engagement remains tenable.
⊗ An independence conflict arises that cannot be managed.

### §14 Deliverables
Security strategy · risk register · programme status · **board-ready security reports and metrics** ·
ongoing advisory *(`SITE-DERIVED`)* · maintained handover pack.

### §16 Closure
On retainer end: handover pack delivered · access revoked · advisory record closed · client
confirms transition of ownership.

**`[GAP]` non-blocking:** board reporting pack format.
**`[GAP]` independence policy — ✓ **CLOSED 2026-09-21**:** a Sleuth-supplied vCISO may not authorise Sleuth's own testing
at that client; an independent client-side signatory is required, enforced on the Authorisation Gate
(`32` §7).

---

## A4 summary

| | `SF-A4-ASM` | `SF-A4-VCI` |
|---|---|---|
| Service procedures | 11 | 10 |
| Cycle | Configurable *(gap)* | Monthly/quarterly *(assumption)* |
| Deliverable | Cycle report + alerts | Board reports + advisory |
| Distinct risk | Alert fatigue; silent coverage lapse | Independence conflict; ownership ambiguity |
| Blocking gaps | 0 | 0 |
