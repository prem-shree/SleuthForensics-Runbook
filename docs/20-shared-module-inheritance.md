# 20 — Shared Modules & the "Change Once" Guarantee

> Sleuth's requirement: *"when a common procedure changes — evidence handling, authorization, QA,
> reporting, engagement closure — we can update it once rather than manually updating dozens of
> runbooks."*

This document specifies exactly how that is guaranteed, including the failure modes that quietly
break it in systems that claim to have it.

---

## 1. The guarantee, stated precisely

> A shared concern has **one definition**. Every runbook that uses it holds a **reference** to that
> definition, never a copy. Changing the definition changes every runbook that references it, in one
> edit, under one approval — while every engagement already in flight continues to execute exactly
> the version it pinned.

Both halves matter. The first half is the efficiency requirement. The second half is the
defensibility requirement from `04-runbook-architecture.md` §4 — and a naive "update everything
everywhere" implementation would break it by silently rewriting the methodology of live engagements.

---

## 2. Single definition points

Each shared concern is defined once, owned by one person, versioned independently:

| Shared module | Covers | Referenced by |
|---|---|---|
| `core.intake` | Enquiry, triage, conflict check, client identity, qualification | All |
| `core.commercial` | NDA, MSA, SOW, commercial approval, team assignment | All |
| `core.authorisation` | Scope, signatory verification, LoA, Authorisation Gate | All |
| `core.readiness` | Questionnaire issue and review, prerequisites, access verification, runbook pinning, kickoff, Readiness Gate | All |
| `core.evidence` | Evidence registration, hashing, verification, custody, access, integrity | All (depth varies by archetype) |
| `core.qa` | Review workflow, segregation of duty, QA Gate | All |
| `core.reporting` | Report spine, document control, limitations, generation, versioning | All |
| `core.delivery` | Recipient verification, classification, release, acceptance, Release Gate | All |
| `core.remediation` | Remediation items, tracking, clarification support | All |
| `core.closure` | Acceptance, disposition, access and credential revocation, artefact removal, lessons learned, Closure Gate | All |
| `arch.A1` … `arch.A4` | Archetype-specific execution, phases 4–6 | Types of that archetype |
| `ctx.*` | The nine context modules | Conditionally |

Nine core modules plus four archetype modules plus nine context modules. **Twenty-two shared
definitions carry the common content of every engagement type Sleuth runs.**

---

## 3. Reference, not copy — and how that is enforced

A runbook version stores a **composition manifest**: module identity plus version. It does not store
module content.

```
SF-<type> v1.2 — composition manifest
  core.intake         v3.1
  core.commercial     v2.0
  core.authorisation  v4.2
  core.readiness      v3.0
  core.evidence       v5.1
  core.qa             v2.3
  core.reporting      v3.4
  core.delivery       v2.1
  core.remediation    v1.8
  core.closure        v3.2
  arch.<A?>           v2.x
  service.<svc>       v1.4      ← the only module this runbook owns
  ctx.<…>             declared, attached conditionally
```

Rendering a runbook resolves the manifest. There is no second copy of core content to drift.

**The failure mode this prevents, and how it is actively blocked.** Every system with an inheritance
model eventually acquires a service module that pastes a core procedure in to "just change one line".
The copy is invisible, and the next core update silently misses it. Countermeasures:

1. The runbook editor offers **reference, extend or delta** — there is no "copy into this module".
2. A near-duplicate check runs at authoring time: service content substantially matching a core
   procedure is flagged before it can be saved.
3. Composition manifests are reviewed at approval; an unexplained service procedure that duplicates
   core scope is a review rejection reason, aggregated like any other.

---

## 4. Extension points

Most real variation is not "replace the core procedure" but "core procedure, plus one thing that is
true only here". Handled by **declared extension points**: named slots a core procedure exposes.

```
core.evidence — procedure ev.04  "Acquire and verify"
  steps 1..6                                          [fixed]
  ⟨ extension: pre_acquisition_checks ⟩               ← declared slot
  steps 7..9                                          [fixed]
  ⟨ extension: additional_verification ⟩              ← declared slot
```

A service or context module injects into a slot. It cannot reach into the fixed steps. So a
service-specific pre-acquisition check lives beside the core procedure without forking it, and the
core steps keep improving underneath it.

Slots are part of the core module's public interface: adding one is routine, removing one is a
breaking change (§6).

---

## 5. Deltas — divergence that is explicit and approved

Occasionally a service genuinely must diverge from core. That is allowed, and it is never silent.

```
DELTA  service.<svc> against core.authorisation v4.2
  Diverges     <which inherited element>
  Reason       <why the inherited content cannot apply here>
  Approved by  <Management> on <date>
  Review by    <date>
  Visible on   the engagement header and the report's methodology section
```

Properties of a delta, all deliberate:

- It requires Management approval, not the module author's own say-so.
- It is **reported**: an Oversight panel lists every live delta across the practice. A concern with
  many deltas is a signal the core module is wrong, not that the services are unusual.
- It carries a **review date**. Deltas are meant to be temporary; most should resolve into a change
  to the core module.
- It is surfaced to the client in the report's methodology section, for the same reason gate
  overrides are.

---

## 6. Change classification and propagation

Not every change carries the same consequence, so not every change needs the same approval weight.
The author classifies; the system enforces.

| Class | Definition | Dependent runbooks | In-flight engagements |
|---|---|---|---|
| **Editorial** | Wording, typo, clarification. **No change to what a person does** | Auto-propagate. Manifests move to the new patch version. No re-approval | Untouched. Still pinned |
| **Substantive** | Changes what a person does, in what order, or what they must record | Each dependent runbook enters `Pending re-approval`. It stays `Approved` on its current manifest until its owner accepts the new module version | Untouched. Still pinned |
| **Breaking** | Adds or removes a gate condition, a mandatory evidence requirement, a stop condition, an approval, or an extension slot | Dependent runbooks enter `Pending re-approval` and are **flagged as blocking** — the new version is not adoptable without an explicit decision | Untouched by default, **plus** a migration decision is raised per live engagement: migrate, or continue on the pinned version with the reason recorded |

Misclassification is the obvious risk. Two mitigations: the system derives a **suggested class** by
diffing structural elements (a changed gate condition cannot be classified Editorial — the classifier
refuses it), and the class is visible at review.

### The safety property

**No class of change, at any approval level, rewrites what an in-flight engagement is executing.**
Migration is always an explicit, per-engagement, recorded decision. The "change once" guarantee
applies to the library, never retroactively to work already under way.

---

## 7. Impact analysis before publishing

A module author sees the full consequence before the change is published — not after.

```
PUBLISH  core.evidence  v5.1 → v5.2                    class: SUBSTANTIVE (suggested)

WHAT CHANGED
  ~ ev.04  "Acquire and verify"     verification step reordered before custody open
  + ev.07  "Record acquisition environment"                            NEW — mandatory

AFFECTS
  Runbooks           <n> referencing core.evidence     → Pending re-approval
    of which             <n> currently Approved
                         <n> in Draft (adopt automatically)
  Engagements        <n> in flight, pinned to manifests containing v5.1
                     → unaffected. Migration offered per engagement.
  Checklists         <n> instances gain 1 required item on adoption
  Gates              Evidence Integrity Gate — no condition change
  Excel exports      Evidence Register gains 1 column

APPROVAL         module owner + Management
NOTIFIES         owners of <n> dependent runbooks
```

The number in "affects `<n>` runbooks" is the whole argument for this architecture, made visible at
the moment of the edit. It is also the honest cost signal: a change touching thirty runbooks deserves
more care than one touching two.

---

## 8. Worked example — the requirement's own example

*Sleuth changes how evidence handling works: verification must now be recorded before the custody
record opens, and the acquisition environment must be captured.*

```
1  SME edits  core.evidence  — one module, one editor, one place
2  Classifier reads the diff: a new mandatory evidence requirement → SUBSTANTIVE
3  Impact analysis shows every dependent runbook and every live engagement
4  Module owner + Management approve.  core.evidence v5.2 published
5  Draft runbooks adopt v5.2 automatically
   Approved runbooks enter Pending re-approval; each owner accepts, bumping that
   runbook's version with a change-history entry naming the module change
6  Live engagements continue on their pinned manifests. A migration is offered
   per engagement; declining is recorded with a reason
7  From adoption, every affected runbook renders the new procedure — with no
   edit made to any of them
```

**Edits made to individual runbooks: zero.** Approvals: one module approval, plus one acceptance per
Approved runbook — and that acceptance is a deliberate control, not busywork. A runbook owner should
know their methodology changed.

### Why acceptance is not automatic for Approved runbooks

Auto-propagating a substantive change into approved methodology would mean a runbook's owner could
discover that their approved method had changed without their knowledge. The efficiency gain is real
— one edit instead of thirty — but the approval is what makes the library trustworthy, and removing
it would trade the wrong thing away.

---

## 9. What the analyst sees

None of this. They open a procedure and it is correct.

The machinery surfaces in exactly two places: the runbook ID and version stamped on the engagement
and in the report, and a delta or unvalidated-content banner where one applies
(`18-content-provenance-and-validation.md` §3).

---

## 10. Consequences for the build

| Requirement | Phase |
|---|---|
| Composition manifests on runbook versions | Phase 1 — foundational, cannot be retrofitted |
| Extension points on core procedures | Phase 1 |
| Change classification with structural diffing | Phase 1 |
| Impact analysis view | Phase 1 |
| Delta workflow with approval and review dates | Phase 2 |
| Near-duplicate detection in the editor | Phase 2 |
| Per-engagement migration decisions | Phase 2 |
| Delta and validation reporting on Oversight | Phase 7 |

The first four are Phase 1 because a runbook engine that stores content by copy cannot be converted
into one that stores it by reference without rewriting every runbook authored in the meantime.
