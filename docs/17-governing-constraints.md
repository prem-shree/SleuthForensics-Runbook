# 17 — Governing Constraints

**Status: BINDING.** Issued by Sleuth Forensics, 2026-09-20. These override anything in docs 00–16
that conflicts with them, and they bind all future work in this repository.

Where an earlier document offered something as a *recommendation*, and a rule below settles it, the
rule wins and the recommendation is now a decision. Those are noted per rule.

---

## The seven rules

### Rule 1 — Default validation state is Draft / Needs SME Validation

> All technical methodologies, procedures, tools, legal requirements, certifications, credentials and
> operational practices not explicitly confirmed by Sleuth are **Draft / Needs SME Validation**.

**This is not a documentation convention. It is a data-model requirement.** Validation state is a
field on every piece of content in the platform — procedure, task, checklist item, question, tool,
template, report section, decision tree, gate condition — and it is visible to the analyst at the
point of use.

**Enforcement**
- Every content object carries `validation_status` and `provenance`. See `18-content-provenance-and-validation.md`.
- A runbook version **cannot reach `Approved`** while any procedure it composes is unvalidated.
- An unvalidated procedure rendered to an analyst is visibly marked as such, and the fact is recorded
  on the engagement.
- Documents 00–16 have been retro-marked. Anything not explicitly marked otherwise is Draft.

### Rule 2 — Do not invent technical procedures to complete a runbook

> No procedure is written merely to fill a gap in a runbook's structure.

A runbook with a declared, visible gap is a correct runbook. A runbook with a plausible-sounding
invented procedure is a defect, and a dangerous one — an analyst following an unvalidated invented
step believes they are following Sleuth's method.

**Enforcement**
- A runbook may contain `GAP` placeholders: a named, described hole with an owner, awaiting SME input.
  A gap is a first-class content object, not a TODO comment.
- Composition completeness and validation completeness are **separate** measures. A runbook can be
  structurally complete and 40% validated; the platform reports both and never conflates them.
- The runbook editor does not offer generated procedure text.

### Rule 3 — Evidence model is register-only

> Register only. No client evidence storage in the initial platform.

**This settles Decision D1.** It is no longer a recommendation — it is the design.

**Enforcement**
- The platform records evidence metadata, hashes, provenance, custody, access history and disposition.
  It does not hold forensic images, memory dumps, collected data sets or any client evidence content.
- `storage_location` points *outward* — to Sleuth's lab storage, evidence safe or medium. It is a
  reference, never an upload target.
- No evidence upload path, no evidence object store, no signed-download infrastructure in the build.
- Screenshots and small contemporaneous records are the boundary case and are **also excluded** until
  Sleuth says otherwise, because "just screenshots" is how an evidence store starts.
  *Open: whether contemporaneous records are attached or referenced — see `15` NC list.*

### Rule 4 — No client secrets in the platform

> No client credentials, secrets, API keys, passwords, private keys or similar access material.

**This confirms the recommendation in `13-security-architecture.md` §6.** It is now a hard constraint.

**Enforcement**
- There is no field, anywhere in the schema, typed to hold a secret.
- The platform records the *facts about* access: that a test account exists, what it is for, that it
  was delivered, through which channel, by whom, that it was verified working, when it expires, and
  that it was revoked at closure. Never the secret itself.
- Questionnaires ask *whether* credentials exist and *how they will be delivered*, never *what they are*.
- Free-text fields that could be abused as a credential store (notes, descriptions) carry a
  detection check and a visible warning. This is a guard-rail, not a guarantee — the primary control
  is that there is no legitimate place to put one.

### Rule 5 — Legal templates are controlled drafts requiring legal review

> Every template in the library is an operational draft until qualified counsel says otherwise.

**Enforcement**
- `legal_review_status` on every document template: `Draft — not reviewed` · `Under legal review` ·
  `Counsel-approved YYYY-MM-DD` · `Counsel-approved, expired`.
- **No workflow inside the platform can set `Counsel-approved`.** It is set only on recorded evidence
  of external review, by an Administrator, with the reviewing party and date captured.
- A non-dismissible banner on every template and every generated instance states the status.
- Generating a document from an unreviewed template is permitted — Sleuth has to operate — but the
  instance records which template version and review status it was generated under, and that is
  visible on the engagement.

### Rule 6 — The website is the public catalogue, not the internal SOP

> sleuthforensics.in remains the source of truth for the **current public service catalogue**.
> It is **not** evidence of how Sleuth actually delivers the work.

This sharpens a boundary that docs 00–16 blurred. Earlier documents described the site's
"What We Examine / Test / Analyse" lists as *seeding* procedures. Under this rule they are
**candidate scope items awaiting SME confirmation**, and nothing more.

**Enforcement — two distinct provenance values**
- `SITE-DERIVED` — authoritative for: service names, pillar grouping, public descriptions,
  client-facing deliverable language, the contact-form taxonomy. Reproduced verbatim.
- `SITE-SUGGESTED` — a candidate drawn from site copy but carrying **no** authority over internal
  method. Always also `Draft / Needs SME Validation`.
- The platform must be able to answer, for any procedure: *where did this come from, and who validated it?*

**Corollary:** where the internal SOP and the public description diverge, that is a finding worth
surfacing to Sleuth — either the site needs updating or the SOP does. The platform should make the
divergence visible rather than quietly resolving it.

### Rule 7 — Do not implement the application

> No application code until the revised architecture is approved.

**Enforcement**
- This repository contains documentation only. No source, no scaffolding, no schema DDL, no
  package manifests, no "just the design system to get started".
- Work continues on architecture, specification and content structure.

---

## The "change once" guarantee

Stated as a requirement by Sleuth alongside the rules:

> When a common procedure changes — evidence handling, authorisation, QA, reporting, closure — we
> update it once, not across dozens of runbooks.

This is specified precisely in `20-shared-module-inheritance.md`: single definition point, reference
not copy, declared extension points, no silent override, classified change propagation with impact
analysis, and pinned engagements left untouched.

---

## The operating goal, restated

> An analyst selects an engagement type → the platform tells them exactly what information to collect,
> what documents are required, what needs to be approved, what to do next, what evidence to record,
> what output to produce, and what conditions must be satisfied before moving forward.

Every architectural decision from here is tested against that sentence. `19-engagement-type-specification.md`
is the schema that makes it deliverable: it is precisely the set of facts that sentence requires,
expressed as a populated specification per engagement type.

---

## What changes in docs 00–16

| Doc | Change |
|---|---|
| 00 | Marked `SITE-DERIVED`. Its *design consequences* are Draft. Rule 6 narrows the authority of its "What We Examine" extracts to candidate scope items |
| 01 | The 41 engagement types are **superseded on arrival** of Sleuth's actual list. Until then, Draft |
| 03 | Lifecycle and gate conditions are Draft proposals for SME validation |
| 04 | Service module procedure lists are `SITE-SUGGESTED` candidates, not method. Gap objects added (Rule 2) |
| 05 | All questionnaire content is Draft. Credential questions restricted per Rule 4 |
| 06 | **Register-only is now decided, not recommended** (Rule 3). Storage sections revised accordingly |
| 07 | Tool catalogue ships empty — unchanged. Legal templates: `legal_review_status` now mandatory (Rule 5) |
| 08 | Report structures are Draft; the site-derived deliverable language is `SITE-DERIVED` |
| 13 | §6 "no credential store" is now a hard constraint (Rule 4), not a recommendation |
| 15 | D1 is closed by Rule 3. D2/D3 unaffected. New NC entries added for Rule 3's boundary cases |
| 16 | Phase 3 scope reduced — no evidence storage subsystem. Phasing otherwise holds |
