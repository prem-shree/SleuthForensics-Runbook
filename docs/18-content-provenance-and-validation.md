# 18 — Content Provenance & Validation

> Implements **Rule 1** (default Draft), **Rule 2** (no invented procedures) and **Rule 6**
> (website ≠ SOP) from `17-governing-constraints.md`.

The requirement "mark anything that requires confirmation from Sleuth" cannot live in document
footnotes. It has to be a property of every piece of content, queryable, and visible to the analyst
at the moment they rely on it.

---

## 1. Two independent axes

Conflating these is the mistake to avoid. *Where content came from* and *whether it has been validated*
are different questions with different answers.

### Axis 1 — Provenance: where did this come from?

| Value | Meaning | Authority |
|---|---|---|
| `SLEUTH-SUPPLIED` | Sleuth wrote it or supplied it directly | Authoritative |
| `SITE-DERIVED` | Reproduced from sleuthforensics.in | Authoritative **for the public catalogue only** — service names, pillar grouping, public descriptions, client-facing deliverable language, contact-form taxonomy |
| `SITE-SUGGESTED` | A candidate inferred from site copy | **No authority over internal method.** A prompt for the SME, nothing more |
| `PROPOSED` | Architectural or structural proposal by Claude | No authority. Awaiting decision |
| `EXTERNAL-STANDARD` | From a named public standard or framework | Authoritative only for what that standard says, and only once Sleuth confirms it applies |

### Axis 2 — Validation: has Sleuth confirmed it?

| Value | Meaning |
|---|---|
| `DRAFT — NEEDS SME VALIDATION` | **The default for everything.** Not confirmed Sleuth practice |
| `IN SME REVIEW` | Assigned to a named SME, in progress |
| `SME-VALIDATED` | A named SME confirmed it, with a date |
| `APPROVED` | SME-validated *and* approved for use by Management |
| `REJECTED` | SME determined it is wrong. Retained with the reason — rejections are useful content |
| `NEEDS CONFIRMATION` | A factual gap about the firm, not a methodology question (the existing doc-15 vocabulary) |
| `GAP` | A known, named hole. Rule 2's alternative to inventing something |

**Nothing is `SME-VALIDATED` today.** Everything produced so far is `DRAFT` or `NEEDS CONFIRMATION`.

### Why two axes and not one combined status

`SITE-DERIVED` + `APPROVED` is a legitimate combination — the service name "Vulnerability Assessment
& Penetration Testing" is both from the site and confirmed. `SITE-SUGGESTED` + `SME-VALIDATED` is
also legitimate, and is the normal path for a candidate procedure that turns out to be right.
`SITE-DERIVED` + `DRAFT` is the state of most of the current catalogue. A single flattened status
cannot express these, and would force exactly the confusion Rule 6 exists to prevent.

---

## 2. Validation metadata on every content object

Carried by: Procedure · Task · ChecklistItem · Question · Tool · DocumentTemplate · ReportSection ·
DecisionNode · GateCondition · EvidenceRequirement · StopCondition · EscalationRule · KnowledgeArticle.

| Field | Notes |
|---|---|
| `provenance` | Axis 1 |
| `provenance_ref` | The specific source — a site URL, a standard clause, a Sleuth message |
| `validation_status` | Axis 2 |
| `validated_by` | Named SME. Not a team, a person |
| `validated_at` | |
| `validation_note` | What the SME changed, confirmed or qualified |
| `revalidation_due` | Methodology decays. Tooling changes, techniques change |
| `rejection_reason` | Populated on `REJECTED` |
| `gap_description` | Populated on `GAP` — what is missing and why it matters |
| `gap_owner` | Who is expected to fill it |
| `blocking` | Does this gap block the engagement type from being sellable through the platform? |

---

## 3. What validation state does at runtime

This is the part that makes Rule 1 real rather than decorative.

### It gates runbook approval

```
A RunbookVersion may reach `Approved` only when:
  · every composed procedure is SME-VALIDATED or APPROVED
  · no composed procedure is DRAFT or IN SME REVIEW
  · every remaining GAP is explicitly non-blocking and acknowledged by the approver
```

A runbook with unvalidated content can still exist, still be composed, still be read, and still be
used in a **pilot** engagement — but it cannot be `Approved`, and an engagement running an
unapproved runbook is visibly flagged as a pilot on the engagement header and in the report's
methodology section.

### It is visible to the analyst

An analyst executing an unvalidated procedure must know. Not in a tooltip — on the procedure.

```
┌──────────────────────────────────────────────────────────────────────┐
│  DRAFT — NEEDS SME VALIDATION                                        │
│  This procedure has not been confirmed as Sleuth method.             │
│  Source: candidate derived from the public service page.             │
│  Owner: <unassigned>                       [ Flag an issue ]         │
├──────────────────────────────────────────────────────────────────────┤
│  Manual validation of identified vulnerabilities                     │
│  …                                                                   │
```

Two consequences follow, and both are deliberate. The analyst applies their own judgement rather than
trusting the text, which is the correct behaviour when the text is unvalidated. And the fact that the
engagement ran unvalidated content is recorded, so it reaches the report's limitations rather than
being discovered later.

### It is visible to the SME as a work queue

Validation is a backlog with an owner, a count and a rate — the same discipline as the review queue
in `08-reporting-architecture.md`. Practice progress is measured in validated procedures, not in
documents written.

```
VALIDATION QUEUE — Investigation pillar          owner: <Needs Confirmation>
  ●  7 procedures  DRAFT
  ◐  2 procedures  IN SME REVIEW
  ✓ 11 procedures  SME-VALIDATED
  ▲  3 GAPS        2 blocking
                                        runbook cannot be Approved
```

### It drives the gap register

Rule 2 forbids inventing a procedure to fill a hole. The `GAP` object is what replaces invention:

```
GAP — SF-SEC-VAP-EXT, Phase 4
  What is missing   The exploitation-depth standard: how far validation may go before it
                    becomes exploitation, and what requires additional approval
  Why it matters    Blocks a stop condition and an approval requirement. An analyst cannot
                    be told "do not exploit beyond proof of access" without a definition of
                    proof of access that Sleuth stands behind
  Blocking          YES — the runbook cannot be Approved without it
  Owner             <Needs Confirmation>
```

A visible gap with a stated consequence is more useful than plausible text nobody validated.

---

## 4. Reporting on validation state

Two numbers, never merged, at every level — engagement type, pillar, practice:

- **Composition completeness** — does the runbook have all its structural parts?
- **Validation completeness** — how much of it has Sleuth actually confirmed?

A runbook can be 100% composed and 30% validated. Reporting a single "80% complete" figure would
hide exactly the thing that matters. The Oversight dashboard shows both, and shows blocking gaps
separately again, because one blocking gap makes an otherwise-complete runbook unusable.

---

## 5. Retro-marking of docs 00–16

Applied. Every document now carries a status banner. Summary:

| Provenance | Where |
|---|---|
| `SITE-DERIVED` | Doc 00 §1–§6 — verbatim site content. Authoritative for the public catalogue only |
| `SITE-SUGGESTED` | Service module procedure candidates (04 §2.3), questionnaire service blocks (05 §5), report service sections (08 §3) |
| `PROPOSED` | Everything structural — archetypes, lifecycle, gates, IA, data model, UX, visual direction, phasing |

| Validation | Count |
|---|---|
| `SME-VALIDATED` | **0** |
| `DRAFT — NEEDS SME VALIDATION` | All technical, operational and legal content |
| `NEEDS CONFIRMATION` | 25 entries in `15-assumptions-and-open-questions.md`, plus new Rule 3 boundary cases |

---

## 6. New Needs-Confirmation entries arising from the rules

| # | Question | Arising from |
|---|---|---|
| NC-26 | Are contemporaneous records (screenshots, tool logs, examiner notes) attached to the platform, or referenced like all other evidence? Rule 3 currently excludes them | Rule 3 |
| NC-27 | Where does Sleuth hold evidence today — lab NAS, evidence safe, encrypted volumes? The register's `storage_location` vocabulary must match reality | Rule 3 |
| NC-28 | Who are the SMEs per pillar, and what validation authority do they hold? Rule 1 is inert without named people | Rule 1 |
| NC-29 | What is Sleuth's revalidation cadence for methodology — annual, on tooling change, on incident? | Rule 1 |
| NC-30 | Which counsel reviews the document templates, and on what cycle? | Rule 5 |
| NC-31 | Is a pilot engagement on an unapproved runbook acceptable, and if so under what conditions? | Rule 1 |
| NC-32 | Where the internal SOP diverges from the public site, who owns reconciling it? | Rule 6 |
