# Sleuth Forensics — Internal Runbook & Engagement Platform

**Status: ON HOLD — awaiting Sleuth's engagement-type list. No application code has been written.**

Seven governing constraints issued by Sleuth on 2026-09-20 are **binding** on all work here:
see [`docs/17-governing-constraints.md`](docs/17-governing-constraints.md). In short — everything
unconfirmed is *Draft / Needs SME Validation*; no invented procedures; evidence model is
register-only; no client secrets in the platform; legal templates are controlled drafts; the public
website is the catalogue but **not** the internal SOP; and no implementation until the revised
architecture is approved.

This repository currently contains research and a proposed architecture for an internal
platform that guides Sleuth Forensics consultants through cybersecurity, digital-forensics,
investigation and resilience engagements from client intake to closure.

The product question the platform exists to answer:

> **"What exactly do I need to do next to execute this engagement correctly?"**

---

## The proposal in one page

**Research.** All 21 service pages, the homepage, about, industries, contact, terms, privacy
and the site's stylesheet were retrieved and analysed. No company facts have been invented;
everything unknown is recorded as *Needs Confirmation*.

**Four findings that shape everything downstream.**

1. Sleuth already publishes a six-step method — *Understand → Examine → Analyse → Report →
   Improve → Validate*. The platform's lifecycle **is** that method, wrapped with pre-engagement
   and closure. Inventing a different one would put the internal tool out of step with what
   clients are told.
2. Several services contain two incompatible workflows under one commercial name — the
   Ransomware page splits its own deliverables into "proactive" and "reactive". So a runbook
   attaches to an **engagement type**, not a service. 21 services → **41 engagement types**.
3. Those 41 types reduce to **4 execution archetypes** (Assessment, Testing, Investigation,
   Continuous), each with its own gates, evidence semantics and closure obligations. This is
   what makes the system tractable without writing 21 unrelated workflows.
4. **16 of the 21 services have no published methodology anywhere.** The platform is where it
   gets written down for the first time — which makes runbook authoring, not engineering,
   the critical path.

**The architecture.** A content plane (versioned, approved runbooks, questionnaires, tools,
templates) and an execution plane (engagements that **pin** a runbook version at kickoff and
retain it forever). Runbooks, questionnaires and reports are all *composed* from a shared core
plus an archetype module plus a service module plus conditionally-attached context modules —
so 55 maintained units cover 41 engagement types, and fixing a custody procedure once improves
all nine investigation runbooks.

**Six gates** enforce the things that must not be skipped: Authorisation, Readiness, Evidence
Integrity, QA, Release, Closure. Overrides are possible, expensive and visible — two people,
a written justification, an expiry, and a paragraph in the client's report.

**Seven top-level navigation items**, not seventeen. Evidence, Findings, Tasks and Checklists
live *inside* an engagement; they surface globally only as deliberate cross-engagement registers.

**Visual direction inherits Sleuth's existing design system** — navy, brand blue, warm cream
neutrals, Inter and IBM Plex Mono, flat, no gradients. The site's own stylesheet already says
*"Flat color palette. No gradients. Enterprise-grade."*

---

## Read in this order

| Doc | Contents |
|---|---|
| [00 — Research Findings](docs/00-research-findings.md) | What the website actually says. Source of truth |
| [01 — Service Catalogue](docs/01-service-catalogue.md) | 21 services → 41 engagement types → 4 archetypes |
| [02 — Users & Roles](docs/02-users-and-roles.md) | Personas, RBAC matrix, segregation of duty |
| [03 — Engagement Lifecycle](docs/03-engagement-lifecycle.md) | 11 phases, 6 gates, the emergency path |
| [04 — Runbook Architecture](docs/04-runbook-architecture.md) | Common vs service-specific; composition; versioning |
| [05 — Questionnaires](docs/05-questionnaire-architecture.md) | What to ask the client, per service |
| [06 — Evidence Model](docs/06-evidence-model.md) | Provenance ladder, custody, integrity, disposition |
| [07 — Tools & Templates](docs/07-tools-and-templates.md) | Tool catalogue; document template library |
| [08 — Findings & Reporting](docs/08-reporting-architecture.md) | Report structures for all 21 services; QA |
| [09 — Information Architecture](docs/09-information-architecture.md) | Navigation, and what deliberately isn't top-level |
| [10 — Data Model](docs/10-data-model.md) | Entities, relationships, invariants |
| [11 — UX Structure](docs/11-ux-structure.md) | Screen-by-screen, worked through Message/User/Context/Priority/Risk/UI |
| [12 — Visual Design Direction](docs/12-visual-design-direction.md) | Design language extended from the live brand |
| [13 — Security Architecture](docs/13-security-architecture.md) | Threat model, RBAC, evidence protection, audit |
| [14 — Excel Exports](docs/14-excel-exports.md) | The future output layer |
| [15 — Assumptions & Open Questions](docs/15-assumptions-and-open-questions.md) | **Decisions needed before building** |
| [16 — Implementation Plan](docs/16-implementation-plan.md) | Phased delivery; the two tracks |
| **[17 — Governing Constraints](docs/17-governing-constraints.md)** | **Sleuth's seven binding rules, and how each is enforced** |
| [18 — Provenance & Validation](docs/18-content-provenance-and-validation.md) | How "needs confirmation" becomes a data field, not a footnote |
| [19 — Engagement Type Specification](docs/19-engagement-type-specification.md) | The schema awaiting Sleuth's engagement types |
| [20 — Shared Modules](docs/20-shared-module-inheritance.md) | The "change once" guarantee, specified precisely |

---

## Decisions needed before implementation

Detail in [doc 15](docs/15-assumptions-and-open-questions.md). The four that matter most:

| | Decision | State |
|---|---|---|
| **D9** | Which engagement types are actually sold, and in what volume? | **Sleuth is supplying these.** Everything downstream waits on it |
| ~~D1~~ | Evidence content storage | **Closed by Rule 3 — register-only** |
| **D8** | Who authors and validates the runbooks, starting when? | Open. Name an SME per pillar — this is the critical path |
| **D6** | Hosting and data residency | Open. India assumed; confirm early |

Plus **NC-26 to NC-32**, newly raised by the constraints — chiefly: who the validating SMEs are
(Rule 1 is inert without named people), where Sleuth actually holds evidence today (the register's
vocabulary must match reality), and whether contemporaneous records are referenced like all other
evidence or attached.

**NC-09 to NC-15** remain questions for qualified legal counsel; several change the forensic report
format.

## What happens when the engagement types arrive

Per [`docs/19`](docs/19-engagement-type-specification.md) §5: reconcile against the proposed 41
(superseded, not merged) → **re-test the four archetypes against the real list** → re-derive the
common lifecycle → populate one Engagement Type Specification per type → update all sixteen
architecture areas → publish the gap register as the SME work queue.

The archetypes are the load-bearing abstraction here and were inferred from marketing copy. Sleuth's
actual catalogue is the first real test of whether they hold; a fifth archetype is a genuine possible
outcome and would be the right answer rather than a setback.

---

## Scope note

Nothing here invents company facts. The website names no individuals, no certifications, no
clients, no partnerships, no tools and no registered entity — so none appear in this proposal.
Where the design needed such a fact, it is a configurable field that ships empty and a
*Needs Confirmation* entry in doc 15.

Document templates described here are **operational templates**. They must be reviewed by
qualified legal counsel before being treated as legal documents.
