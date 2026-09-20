# 19 — Engagement Type Specification (ETS)

> The schema that will be populated once Sleuth supplies its actual engagement types.
> It is exactly the set of facts required by the operating goal in `17-governing-constraints.md`:
> *analyst selects an engagement type → the platform tells them what to collect, what documents are
> required, what needs approval, what to do next, what evidence to record, what output to produce,
> and what must be satisfied before moving forward.*

**Nothing is populated yet.** This document defines the format, the notation and the input Sleuth
needs to supply. It is deliberately published before the content so that Sleuth's engagement-type
information lands in a defined structure rather than being reshaped afterwards.

---

## 1. The central rule: common content is *derived*, never restated

The brief asks each engagement type to identify "what is common" and "what is service-specific".

The wrong way to do that is to write both out per engagement type. Forty engagement types each
restating the evidence-handling procedure is forty copies to update — precisely the failure the
"change once" requirement exists to prevent.

**So an ETS authors only the service-specific content. The common content is computed from the
composition and rendered read-only.**

```
ETS  =  reference to (Core spine + Archetype module)      ← derived, never authored here
     +  the Service module                                 ← the only part authored per type
     +  declared attachable Context modules                ← conditions, not content
     +  declared deltas against inherited content          ← explicit, approved, never silent
```

"What is common" is therefore answerable at any moment by resolving the composition, and it is
correct by construction. If the core evidence-handling procedure changes tomorrow, every ETS's
"what is common" changes with it, with no edits. See `20-shared-module-inheritance.md`.

### Notation

Used throughout every populated ETS:

| Marker | Meaning |
|---|---|
| `[CORE]` | Inherited from the core spine. Not authored here. Reference only |
| `[ARCH:A2]` | Inherited from the named archetype module |
| `[SERVICE]` | Specific to this engagement type. **The only content actually authored in an ETS** |
| `[CTX:Production]` | Conditional — attached when that context module's condition is met |
| `[EXTENDS: core.ev.04]` | Service content injected at a declared extension point on inherited content |
| `[DELTA: core.auth.02]` | An approved, recorded divergence from inherited content. Requires justification |
| `[GAP]` | A known hole. Rule 2's alternative to inventing content |

Every element additionally carries `provenance` and `validation_status` per `18-content-provenance-and-validation.md`.

---

## 2. ETS schema — the sixteen required facts

### Header

| Field | Notes |
|---|---|
| Engagement type ID | `SF-<PILLAR>-<SVC>-<TYPE>` |
| Display name | What Sleuth calls it internally |
| Public service | Which of the 21 site services it is sold under, if any *(`SITE-DERIVED`)* |
| Archetype | A1 / A2 / A3 / A4 — or a new one if Sleuth's reality needs it |
| Sold as | Fixed-scope project · time-boxed · retainer · emergency call-off |
| Typical duration | |
| Team shape | Roles and indicative count |
| Runbook ID + version | |
| Composition completeness / Validation completeness | Two separate figures, never merged |

### §1 What is common — `[DERIVED]`

Rendered from the composition, not authored. Resolves to the list of inherited core and archetype
procedures, checklists, gates, evidence rules, document requirements and closure obligations, each
with its current version. Read-only in the ETS.

### §2 What is service-specific — `[SERVICE]`

The service module: the procedures, checks, evidence requirements and outputs that exist *only* for
this engagement type. **This is the content Sleuth's SMEs author.** Everything else in an ETS is
either inherited, derived, or a declared condition.

### §3 Required client information

Questions this engagement type needs answered before work can start, split three ways:

| Layer | Source |
|---|---|
| Universal block | `[CORE]` |
| Archetype block | `[ARCH:*]` |
| Service block | `[SERVICE]` — authored here |

Each question: type · required/optional · **blocking** (holds the Readiness Gate) · `why_we_ask` ·
which context module it can trigger · whether an answer must be Sleuth-verified rather than
client-stated.

**Rule 4 constraint:** questions establish *whether* access material exists and *how it will be
delivered*. Never *what it is*.

### §4 Required documents

Per document: which template · mandatory or conditional · which phase it is needed by · which gate
it unblocks · who signs on the client side · whether signatory authority must be verified ·
`legal_review_status` of the template *(Rule 5)*.

### §5 Authorisation requirements

What authority is needed before any work touches a client system or a client's data. Who may grant
it. How their authority to grant it is verified. Validity period. What happens on expiry. Whether an
emergency path exists for this engagement type, and precisely what it does and does not unblock.

### §6 Preconditions

What must be true before Phase 4 opens: access verified working, environment confirmed, tooling
approved and in validation date, team briefed on stop conditions, client contacts confirmed
reachable. Each precondition is a checkable condition on the Readiness Gate, not prose.

### §7 Major phases

The lifecycle phases this engagement type actually uses, with any reordering, parallelism or
omission relative to the common lifecycle — and **the reason for each deviation**. Deviation without
a stated reason is a drafting error, not a variation.

### §8 Technical procedures — `[SERVICE]` — *this is the SME content*

Per procedure: objective · rationale · preconditions · inputs · tasks · checklist · required tool
capabilities *(never product names — see `07-tools-and-templates.md`)* · evidence requirements ·
decision points · stop conditions · escalations · approvals · outputs · estimated duration · role.

Subject to **Rule 2**: where the method is not known and confirmed, the entry is a `[GAP]` with a
description, a consequence and an owner. It is not filled with plausible text.

### §9 Evidence requirements

What must be captured, at what quality, at which point. Per item: evidence level (L0–L5), capture
method, whether custody applies, whether it is mandatory for a finding, and retention class.

**Rule 3 constraint:** these are *register* requirements. The platform records that the evidence
exists, its hash, its custody and where it is held. It does not hold the content.

### §10 Decision points

Branches with recorded outcomes. Per decision: the question, the branches, what each branch changes
(procedures substituted, context modules attached, approvals required), who decides, and what is
recorded.

### §11 Stop conditions

Conditions on which work halts immediately, without a judgement call. Per condition: the trigger,
what stops, what must be preserved at the moment of stopping, who is notified, and how work resumes.

### §12 Escalation points

Per escalation: trigger · who is notified · target time · whether work pauses · whether the client
is informed and by whom · whether it bypasses the normal chain *(some must — see
`03-engagement-lifecycle.md` §6)*.

### §13 QA gates

Which gates apply, and any engagement-type-specific conditions added to them. Who passes each.
Segregation-of-duty requirements. Whether any gate is non-overridable for this type.

### §14 Deliverables

Per deliverable: report or artefact · its template and version · required sections · audience ·
classification · delivery channel · acceptance mechanism. Client-facing deliverable *language* may
be `SITE-DERIVED`; the *structure* is `[SERVICE]` and Draft until validated.

### §15 Retest / follow-up

Whether retest applies · what triggers it · what is retested and what is not · the outcome vocabulary ·
whether it is in the original scope or separately authorised · whether a separate authorisation or
window is required · what document is issued.

### §16 Closure requirements

Acceptance · evidence disposition (the instruction, the deadline, the witness requirement) · client
access revocation · **test account and credential revocation confirmed** *(Rule 4 — the platform
tracked that access existed, so it can confirm it was withdrawn)* · removal of any artefacts Sleuth
created in client systems · lessons learned · runbook improvement proposals raised against the
version that was executed.

---

## 3. Skeleton — the notation in use

Illustrative only. Content is deliberately left as `[GAP]` rather than invented (**Rule 2**), which
is what a genuine pre-validation ETS looks like.

```
ENGAGEMENT TYPE   <id>                       ARCHETYPE  <A1|A2|A3|A4>
PUBLIC SERVICE    <site service>             SITE-DERIVED
COMPOSITION       78% structurally complete  VALIDATION  0% — nothing SME-validated
BLOCKING GAPS     4                          RUNBOOK     cannot be Approved

§1  WHAT IS COMMON                                            [DERIVED — read only]
    core.spine v—      35 procedures, phases 0-3 and 7-10
    arch.<A?> v—       archetype procedures, phases 4-6
    → resolved live from the composition; never restated here

§3  REQUIRED CLIENT INFORMATION
    [CORE]     universal block — client, authority, objective, constraints, logistics
    [ARCH:A?]  archetype block
    [SERVICE]  [GAP] service questions — awaiting SME
               owner: <Needs Confirmation> · blocking: YES

§5  AUTHORISATION REQUIREMENTS
    [CORE]     engagement agreement executed
    [CORE]     authorised signatory verified
    [ARCH:A?]  [GAP] archetype-specific authority — awaiting SME confirmation
    [CTX:Emergency] emergency record + 24h ratification   (if applicable to this type)

§8  TECHNICAL PROCEDURES                                      [SERVICE] — SME content
    01  [GAP]  <candidate scope item from the public service page>
               provenance: SITE-SUGGESTED  ·  validation: DRAFT
               ⚠ Rule 6 — site copy is not evidence of internal SOP.
                 This is a prompt for the SME, not a procedure.
    02  [GAP]  …
               blocking: YES — the engagement type is not sellable through the
                              platform until this exists

§11 STOP CONDITIONS
    [CORE]     authorisation lapses or is withdrawn
    [CORE]     safety risk to people identified
    [ARCH:A?]  [GAP] archetype stop conditions — awaiting SME
    [SERVICE]  [GAP]

§16 CLOSURE REQUIREMENTS
    [CORE]     acceptance · disposition · access revocation · credential revocation
               confirmed · artefact removal · lessons learned
    [SERVICE]  [GAP] any type-specific closure obligation
```

A populated ETS is the same skeleton with `[GAP]` replaced by SME-validated content, and with the
validation figure moving off zero.

---

## 4. What Sleuth needs to supply per engagement type

Answering these is enough to populate §1–§7 and §9–§16. §8 (technical procedures) is the SME
authoring work that follows, and is expected to take longer.

**Short answers are fine. "Don't know yet" is a valid answer and produces a `[GAP]`, which is the
correct outcome under Rule 2.**

| # | Question |
|---|---|
| 1 | What do you call this internally, and which of the 21 public services is it sold under? |
| 2 | One sentence: what does the client get, and what question does it answer for them? |
| 3 | Is it planned or reactive? Fixed-scope, time-boxed, retainer, or emergency call-off? |
| 4 | Roughly how often do you sell it, and what is a typical duration and team shape? |
| 5 | Does Sleuth actively test, touch or change client systems? Does it acquire client data or devices? |
| 6 | What authority do you require before starting, and who at the client can give it? |
| 7 | What must the client give you before you can start — information, access, documents, physical items? |
| 8 | What are the major stages of the work, in your words? |
| 9 | What do you have to record as you go, to stand behind the output later? |
| 10 | What makes you stop, or pick up the phone? |
| 11 | Who reviews the work before it goes out, and what do they check? |
| 12 | What does the client receive, and in what form? |
| 13 | Is there a retest or follow-up, and is it in scope or sold separately? |
| 14 | What has to happen for you to consider it finished? |
| 15 | What most often goes wrong on this type of engagement? |

Question 15 is not in the brief's sixteen fields, and it is the most valuable one. It surfaces the
stop conditions, gate conditions and checklist items that matter in practice — the things a
methodology document written from first principles reliably misses.

---

## 5. What happens when Sleuth supplies the list

In this order:

1. **Reconcile** the supplied engagement types against the proposed 41 in `01-service-catalogue.md`.
   The proposed list is superseded, not merged. Anything Sleuth does not sell is deleted rather than
   kept "for later".
2. **Re-test the four archetypes** against the real list. If a supplied engagement type does not fit
   A1–A4, the archetypes change — they were derived from the public catalogue, and the real catalogue
   is the better evidence. A fifth archetype is a real possible outcome, and forcing a bad fit to
   preserve a diagram would be the wrong trade.
3. **Re-derive the common lifecycle** from what is genuinely common across the real types, rather
   than from what looked common across the site.
4. **Create one ETS per engagement type**, populated to §1–§7 and §9–§16 from Sleuth's answers, with
   `[GAP]` everywhere the answer is not yet known.
5. **Update the sixteen architecture areas** listed by Sleuth — catalogue, types, archetypes, common
   lifecycle, service variations, runbook architecture, questionnaires, checklists, evidence
   register, findings, reporting, roles, data model, navigation, UX, exports.
6. **Publish the gap register** — every blocking gap, with an owner, ordered by which engagement
   types it blocks. This becomes the SME work queue and the real measure of readiness.

Step 2 is the one worth flagging. The archetypes are the load-bearing abstraction in this
architecture, and they were inferred from marketing copy. Sleuth's actual list is the first real
test of whether they hold.
