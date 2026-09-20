# 15 — Assumptions, Open Questions & Decisions Needed

> **Status — `PROPOSED`, awaiting approval.** Structural and design proposals, not confirmed
> Sleuth practice. See [`17-governing-constraints.md`](17-governing-constraints.md). Partly superseded on arrival of Sleuth's engagement-type list —
> [`19-engagement-type-specification.md`](19-engagement-type-specification.md) §5.
>
> **D1 is closed by Rule 3** (register-only). D2 and D3 are unaffected. New entries NC-26 to
> NC-32 arising from the rules are recorded in [`18-content-provenance-and-validation.md`](18-content-provenance-and-validation.md) §6.


Two kinds of entry here:

- **Needs Confirmation (NC)** — a fact about Sleuth that the website does not state and that I have not invented. Each one has a working assumption used in the design, and a note on what changes if the assumption is wrong.
- **Decisions (D)** — architectural choices that genuinely change the build. Each has a recommendation. **These are the items I need answers to before implementation.**

---

## PART A — Decisions needed before building

### D1 — Does the platform store evidence content, or only the evidence register? · **CLOSED by Rule 3 — register-only**

This is the biggest single scoping decision in the product.

| | Register only | Managed storage |
|---|---|---|
| Platform holds | Metadata, hashes, custody, provenance, access log | The above **plus the forensic images and collected data** |
| Evidence lives in | Sleuth's existing lab storage / evidence safes | The platform's object store |
| Infrastructure | Modest | Substantial — terabytes per engagement, per-engagement keys, secure transfer, backup propagation for destruction |
| Risk if breached | Metadata exposure — serious | **Every client's forensic evidence in one place — existential** |
| Delivers | ~90% of the brief's evidence requirements | The remaining 10% |

**Decided by Sleuth (Rule 3): register-only.** Not revisited unless Sleuth reopens it. The custody, integrity, provenance and access-history requirements — which is what makes forensic work defensible — are all satisfied by the register. Centralising the images themselves adds enormous infrastructure cost and concentrates catastrophic risk to buy comparatively little. *(Assumed throughout `06-evidence-model.md` and `10-data-model.md`.)*

### D2 — Build target: internal-only, or eventually client-facing?

**Recommendation: internal-only, with a designed seam.** Keep all client-facing capability behind a single boundary (delivery, questionnaire links, remediation tracking) so it can be opened later without re-architecting. Do not build it in Phase 1. Every client-facing surface is internet-exposed attack surface on a platform holding investigation data.

### D3 — Do clients fill questionnaires directly?

**Recommendation: no, not initially.** Consultant-mediated in Phase 1; exported form in Phase 2; secure client link in Phase 7 and only after an independent security review. Rationale in `05-questionnaire-architecture.md` §6.

### D4 — Does the platform track time and cost?

The brief does not mention it. Management oversight would benefit; it also changes the product's character considerably — consultants' relationship with a tool that times them is different, and it draws the platform toward being a PSA/billing system.

**Recommendation: no.** Track engagement *phases* and *durations* for operational insight, not billable hours. Integrate with whatever Sleuth uses for billing if needed. **Needs Sleuth's decision** — if they want it, it should be in from Phase 0, since retrofitting time tracking is unpleasant.

### D5 — Technology stack

**Recommendation:** PostgreSQL; server-rendered application with targeted interactivity; object storage for files; self-hosted in an India region. Rationale in `10-data-model.md` §6. **Needs confirmation of:** existing Sleuth infrastructure and hosting preferences, in-house maintenance capability, and any client contractual constraints on where their data may reside.

### D6 — Hosting and data residency

**Assumption:** India region, self-hosted or on an Indian cloud region, given "organisations across India" and Indian governing law. **Needs Confirmation** — and it must be confirmed early, because it constrains D5 and cannot be changed cheaply once real data exists.

### D7 — Retention periods

**Assumption used in the design:** retention is fully configurable with no hard-coded default. **Needs Confirmation with qualified counsel** for: evidence, reports, audit logs, questionnaire responses, and closed-engagement records. Different classes will likely have different periods, and some may have *maximum* as well as minimum periods where personal data is involved.

### D8 — Runbook authoring: who, and starting when?

41 engagement types need runbooks. 16 of 21 services have no published methodology anywhere (research §2), so much of this is genuine first-time authoring by subject-matter experts, not transcription.

**This is the critical path for the whole programme — not the software.** A perfect platform with three runbooks is not usable; a modest platform with twenty good runbooks is.

**Recommendation:** name a Runbook Author per pillar now, and begin authoring in parallel with Phase 0. **Needs Sleuth's decision** on who owns authoring and how much of their time it gets.

### D9 — Which engagement types are actually sold, and in what volume?

The 41 types in `01-service-catalogue.md` are derived from what the website describes, not from Sleuth's sales data. Some may never be sold separately; others may be the bulk of revenue.

**Needs Confirmation.** This directly determines runbook authoring order and the choice of the Phase 1 vertical slice. The proposal assumes VAPT is high-volume and structurally representative; if Sleuth's actual volume is dominated by, say, DFIR or compliance work, the Phase 1 slice should change accordingly. **This is the single most useful answer Sleuth can give.**

---

## PART B — Needs Confirmation

### About the firm

| # | Question | Working assumption | Impact if wrong |
|---|---|---|---|
| NC-01 | Team size and structure | Small team; individuals hold multiple roles | RBAC must permit one person holding several roles while still enforcing author ≠ reviewer on any single item. **Already designed for this.** If the team is very small, segregation of duty on every finding may be impractical and needs an explicit, documented exception policy rather than silent non-compliance |
| NC-02 | Named individuals, certifications, accreditations | None assumed; none appear on the site | Examiner-competency fields ship empty and configurable. If Sleuth holds lab accreditation, its requirements may add mandatory procedures |
| NC-03 | Existing tooling — ticketing, storage, document management, identity provider | Greenfield; SSO preferred if available | Integration scope. Possible duplication with systems already in use |
| NC-04 | Existing report templates and their format | None assumed; structures proposed from the site's "What You Receive" lists | Report templates should start from Sleuth's real ones if they exist |
| NC-05 | Laboratory facilities, evidence safe, write-blockers | Assumed to exist for A3 work | Affects D1 and physical custody procedures |
| NC-06 | Whether Sleuth subcontracts any work | Assumed not | Would need external-party roles and custody transfer to third parties |
| NC-07 | On-call rota for active incidents | Assumed to exist informally | Affects escalation routing and the emergency path |
| NC-08 | Approved tool stack | None assumed — catalogue ships empty | Phase 1 seeding effort |

### Legal and regulatory *(for qualified counsel, not assumption)*

| # | Question | Working assumption | Impact if wrong |
|---|---|---|---|
| NC-09 | Does Sleuth issue certificates for electronic records, or provide expert testimony? | Not assumed | Would materially change forensic report format and custody documentation; likely adds mandatory procedures and a certificate template |
| NC-10 | Which incident-reporting obligations bind Sleuth, and which bind its clients? | Configurable; none hard-coded | Reporting timers in incident runbooks |
| NC-11 | Personal-data obligations for forensic images containing third parties' data | Configurable retention and disposition | Disposition defaults and possibly mandatory minimisation steps |
| NC-12 | Cross-border transfer where evidence originates outside India | Cross-Border context module exists but is unspecified | Residency architecture |
| NC-13 | Professional indemnity constraints on record-keeping | None assumed | May mandate retention minimums |
| NC-14 | Position on ransom payment advice and recording it | Questionnaire flags it as sensitive; nothing assumed | Whether the platform records this at all |
| NC-15 | Safeguarding policy for individual clients in domestic-abuse contexts | Flagged in the spyware runbook; no policy assumed | Real duty-of-care implications for an examination that may itself put someone at risk |

### Operational

| # | Question | Working assumption | Impact if wrong |
|---|---|---|---|
| NC-16 | Is retest standard across all testing services, or only VAPT and Web/API? | Retest exists for all A2; mandatory only where the site promises it | Lifecycle Phase 9 requirements per engagement type |
| NC-17 | Does Sleuth perform takedowns (brand/phishing)? | Not assumed | Threat Intelligence procedures and deliverables |
| NC-18 | Does Sleuth issue attestation letters or testing certificates? | Not assumed | Compliance-driven VAPT deliverables — clients frequently ask |
| NC-19 | Typical engagement durations per type | None assumed | Scheduling, capacity views, "days in phase" thresholds |
| NC-20 | Severity methodology — CVSS, proprietary, or hybrid? | Severity with mandatory rationale; CVSS optional | Finding model and calibration |
| NC-21 | Maturity model for A1 — which scale? | Configurable per framework | Scorecard structure |
| NC-22 | Client acceptance process — formal sign-off or informal? | Formal acceptance record assumed | Closure Gate conditions |
| NC-23 | Should the platform hold prior engagement history to inform new ones? | Yes — a key benefit of the Clients area | Privacy and access design within a client's own history |
| NC-24 | Canonical industry list — 6 (homepage) or 9 (industries page)? | 9 | Minor; also worth reconciling on the public site |
| NC-25 | Is "Insights" intended to exist? Both URLs 404 | Out of scope for this platform | Public site only; flagged as an observation |

---

## PART C — Explicit non-inventions

Stated so the boundary of the research is visible. The following appear nowhere on the website and have **not** been invented anywhere in this proposal: employee names, roles or headcount; certifications held by the firm or individuals; client names, case studies or references; partnerships or vendor relationships; office addresses, phone numbers or public email addresses; the registered legal entity; pricing, rate cards or commercial terms; tools owned or licensed; laboratory accreditation; years in operation; industry awards or memberships.

Where the design needed one of these, it is a configurable field that ships empty, or a Needs Confirmation entry above.

---

## PART D — Risks to the programme

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| **Runbook content never gets written** | **High** | **Fatal** | Name owners now (D8). Ship a thin slice early so authoring has a real target. Measure progress in approved runbooks, not features |
| Platform becomes a compliance burden consultants route around | Medium | High | The Phase 1 test is whether an Analyst *prefers* it to a checklist in a document. If not, stop and fix that before building more |
| Gate overrides become routine | Medium | High | Two-person approval, expiry, client-report visibility, Oversight tracking — all already designed in. Watch the override rate as a health metric |
| Scope expands toward a general PSA/billing system | Medium | Medium | D4 says no. Hold that line |
| The platform itself is breached | Low | **Existential** | `13-security-architecture.md`. Assess before it holds real data, and annually |
| ~~Evidence storage costs exceed expectation~~ | — | — | **Removed.** Rule 3 eliminates this risk entirely |
| Built for the wrong archetype first | Low | High | D9 — confirm real engagement volumes before committing to the Phase 1 slice |
