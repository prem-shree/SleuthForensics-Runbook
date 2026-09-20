# 28 — Checklist & Gate Architecture

> **Status — `PROPOSED`, Draft / Needs SME Validation.**
> Specifies properly what earlier documents described only in outline.

---

## In plain terms

A **checklist** records that a person did something. A **gate** decides whether the engagement is
allowed to move forward.

They are related but not the same, and the difference matters: a checklist item can be ticked by
someone in a hurry. A gate should, wherever possible, check the *actual state of the record* rather
than trusting a tick.

---

## 1. The design rule: prefer facts over ticks

> **A gate condition should be evaluated from data wherever the data exists. A tick is the fallback,
> not the default.**

| Condition | Weak — a tick | Strong — a fact |
|---|---|---|
| NDA executed | ☑ "NDA signed" | An executed NDA document instance exists, with a verified signatory and an execution date |
| Evidence verified | ☑ "Hashes checked" | Every evidence item has `integrity_status = Verified` |
| Reviewer sign-off | ☑ "Reviewed" | A review record exists with `reviewer_id ≠ author_id` and an outcome |
| Access revoked | ☑ "Access removed" | Every recorded access entry has a revocation confirmation |

Ticks remain necessary where no system fact exists — "the team was briefed", "the client confirmed
the window", "the engineer accompanied us on site". Those are genuine human attestations, and the
platform records **who** attested and **when**, which is the accountability that makes a tick worth
anything.

**Roughly 70% of the gate conditions in this design are evaluable from data.** That proportion is
worth protecting: every condition converted from a tick to a fact is one fewer place the system can
be told something untrue.

---

## 2. Checklist item model

Exactly the states the brief specifies, plus the metadata that makes them accountable.

| Field | Values / notes |
|---|---|
| `requirement` | `Required` · `Optional` · `Conditional` *(with a condition expression)* |
| `state` | `Not started` · `Completed` · `Not applicable` · `Blocked` · `Needs review` |
| `evidence_ref` | Links to an evidence record. Mandatory where `evidence_required = true` |
| `note` | Free text |
| `na_reason` | **Mandatory** when `state = Not applicable` |
| `blocked_reason` + `blocked_owner` | **Mandatory** when `state = Blocked` |
| `owner` | Who is responsible |
| `completed_by` + `completed_at` | Set on completion. Never back-dateable |
| `attestation` | For human-attestation items: who is asserting this, and on what basis |

### The states that carry the most weight

**`Not applicable`** requires a reason. Without one it becomes a silent skip, and "N/A" is the most
commonly abused state on any checklist. The reason appears in the report's limitations when the item
was Required.

**`Blocked`** requires a reason and an owner. A blocker without an owner sits for three weeks. Blocked
items surface on the engagement's Now screen, on the owner's Today queue, and on the Oversight
dashboard once they age past a threshold.

**`Needs review`** is the analyst saying *"I did this but I am not certain."* It is deliberately
cheap to set and it holds the QA Gate. Making uncertainty easy to express is worth more than making
it look tidy — an analyst who has no low-cost way to flag doubt will simply mark the item complete.

---

## 3. Checklist types

| Type | Scope | Purpose |
|---|---|---|
| **Procedure checklist** | One procedure | Verification within the work. "Did I capture the evidence this procedure requires?" |
| **Phase checklist** | One phase | Phase exit criteria |
| **Gate checklist** | One gate | The human-attestation subset of a gate's conditions |
| **Engagement checklist** | Whole engagement | The aggregate view — and the primary Excel export *(`14-excel-exports.md` §2.1)* |

The engagement checklist is a **projection**, not a separate list. It aggregates every item from
every procedure, phase and gate. There is one source of truth; a tick in one place is the same tick
everywhere.

---

## 4. Gate model

```
GateInstance
  ├─ state          BLOCKED · READY · PASSED · OVERRIDDEN
  ├─ conditions[]   each: expression · result · evaluated_at · failure_message
  │                       · remediation_hint · owner · age
  ├─ evaluated      continuously — a gate re-blocks if a condition stops being true
  ├─ passed_by      role-restricted per gate
  ├─ snapshot       condition results captured at the moment of passing
  └─ override       requested_by · approved_by · justification · expires_at
                    · remediation_task_id        (absent where overridable = false)
```

**The snapshot matters.** It records *why the gate was passable at that moment* — which is precisely
the question asked later when something turns out to have been wrong.

**Re-blocking is real.** An expired Letter of Authorisation, a withdrawn approval or a failed
integrity check re-blocks a gate that had already passed. Passing a gate is not a permanent state.

---

## 5. The seven gates, fully specified

`[F]` = evaluated from a fact · `[A]` = human attestation · `[C]` = conditional on archetype or context

### ⟨ Authorisation Gate ⟩ — blocks all technical execution
**Passed by:** Engagement Manager · **Overridable:** yes, Management approval

| Condition | | |
|---|---|---|
| NDA executed with verified signatory | `[F]` | All |
| Engagement agreement executed | `[F]` | All |
| Letter of Authorisation executed and within validity dates | `[F]` | `[C]` A2, A3 |
| Signatory authority verified and recorded | `[F]` | A2, A3 |
| Scope approved, with explicit out-of-scope list | `[F]` | All |
| Every in-scope asset has verified ownership | `[F]` | `[C]` A2 |
| Third-party authorisation obtained, or asset removed from scope | `[F]` | `[C]` A2 |
| Rules of Engagement approved | `[F]` | `[C]` A2 |
| Testing window agreed with timezone | `[F]` | `[C]` A2 |
| Provider policy check complete | `[F]` | `[C]` `SF-A2-CPT` |
| Legal and HR approval obtained | `[F]` | `[C]` `SF-A2-SES` |
| Site safety authorisation obtained | `[A]` | `[C]` `SF-A1-OTA` |
| Consent and device ownership verified | `[F]` | `[C]` `SF-A3-SPY` |
| Authority to examine recorded | `[F]` | `[C]` A3 |
| Emergency contacts recorded and reachability confirmed | `[A]` | All |

### ⟨ Readiness Gate ⟩ — blocks the start of execution
**Passed by:** Engagement Manager · **Overridable:** yes

| Condition | | |
|---|---|---|
| All blocking questionnaire questions answered, or marked unavailable with reason | `[F]` | All |
| Material client-stated answers independently verified | `[F]` | All |
| Prerequisites confirmed | `[F]` | All |
| Access verified working | `[A]` | `[C]` where access is needed |
| All planned tools `Approved` and within validation date, or exception approved | `[F]` | All |
| Runbook version pinned | `[F]` | All |
| Kickoff held | `[A]` | All |
| **Every assigned team member has acknowledged the stop conditions** | `[F]` | All |
| Safety induction completed and engineer assigned | `[A]` | `[C]` `SF-A1-OTA` |
| Test accounts verified for every role | `[F]` | `[C]` `SF-A2-WAT` |
| Deconfliction procedure established and tested | `[A]` | `[C]` `SF-A2-RED` |
| Safe communication channel established | `[A]` | `[C]` `SF-A3-SPY` |
| Sharing permission recorded | `[F]` | `[C]` `SF-A3-MAL` |

### ⟨ Custody Gate ⟩ — blocks any analysis of acquired evidence
**Passed by:** Reviewer · **Overridable: NO** · **Archetype: A3**

| Condition | |
|---|---|
| Source write-protected, or the absence justified and recorded | `[F]` |
| Acquisition hash computed with an approved algorithm | `[F]` |
| Verification hash computed independently and matching | `[F]` |
| Custody record opened with an `ACQUIRED` event | `[F]` |
| Examiner recorded | `[F]` |
| Acquisition tool and version recorded | `[F]` |

> **Why this one cannot be overridden.** Evidence acquired without an integrity record is not weaker
> evidence — it is no evidence. There is no business justification that changes that, so the system
> does not offer the option. This is the only gate in the design with `overridable = false`.

### ⟨ Evidence Integrity Gate ⟩ — blocks findings moving to report
**Passed by:** Reviewer · **Overridable:** yes, with the failure disclosed in the report

| Condition | | |
|---|---|---|
| Every evidence item has acquisition hash and algorithm | `[F]` | All |
| Every item verified, with matching hashes | `[F]` | All |
| No item in `integrity_status = FAILED` | `[F]` | All |
| No unexplained custody gaps | `[F]` | `[C]` A3 |
| All working copies traceable to a verified parent | `[F]` | `[C]` A3 |
| Every finding references ≥1 evidence item | `[F]` | All |
| Every maturity rating cites a source *(Evidence Sufficiency)* | `[F]` | `[C]` A1 |

### ⟨ QA Gate ⟩ — blocks report moving to delivery
**Passed by:** Reviewer · **Overridable:** yes, disclosed in the report

| Condition | |
|---|---|
| Reviewer assigned and `reviewer_id ≠ author_id` | `[F]` |
| Every finding reviewed, with an outcome | `[F]` |
| Every finding has severity and written rationale | `[F]` |
| All required report sections complete | `[F]` |
| Scope statement matches the approved scope | `[F]` |
| Limitations section reviewed and contextualised | `[A]` |
| No open `Needs review` items anywhere in the engagement | `[F]` |
| No unresolved reviewer rejections | `[F]` |
| Evidence Integrity Gate passed | `[F]` |

### ⟨ Release Gate ⟩ — blocks delivery to the client
**Passed by:** Engagement Manager · **Overridable:** no *(but conditions are few and achievable)*

| Condition | |
|---|---|
| Recipient list approved | `[F]` |
| Every recipient exists in the contact register | `[F]` |
| **No recipient is flagged as excluded** | `[F]` |
| Classification applied | `[F]` |
| Delivery channel approved | `[F]` |
| Report version frozen with hash recorded | `[F]` |
| QA Gate passed | `[F]` |

> Release is not overridable because every condition is achievable in minutes, and the failure mode —
> a forensic report on an internal investigation reaching its own subject — is among the most
> damaging outcomes in this entire product.

### ⟨ Closure Gate ⟩ — blocks engagement closure
**Passed by:** Engagement Manager · **Overridable:** yes, with a scheduled remediation task

| Condition | | |
|---|---|---|
| Client acceptance recorded, or dispute resolved | `[F]` | All |
| Retest complete or formally waived in writing | `[F]` | `[C]` A2 |
| **Every evidence item has a disposition instruction** | `[F]` | All |
| Disposition executed or scheduled with a date | `[F]` | All |
| Destruction certificates recorded with witness | `[F]` | `[C]` where destroyed |
| Sleuth access to client systems revoked and confirmed | `[F]` | All |
| **Client has confirmed test accounts and credentials revoked** | `[F]` | `[C]` where issued |
| Sleuth-created artefacts removed and removal verified | `[F]` | `[C]` A2 |
| Analysis environment sanitised | `[A]` | `[C]` `SF-A3-MAL` |
| Lessons learned captured | `[F]` | All |
| Runbook improvement proposals raised or explicitly none | `[F]` | All |

---

## 6. Override semantics

```
REQUEST          Engagement Manager
APPROVE          Management                    — never the same person
JUSTIFICATION    written, mandatory, becomes part of the engagement record
EXPIRY           mandatory. The gate RE-BLOCKS when it lapses
REMEDIATION      an auto-created task with an owner and a due date
VISIBILITY       engagement header · Oversight dashboard · audit log
                 · AND auto-seeded into the report's limitations section
```

That last line is the effective control. An override granted under commercial pressure in Phase 2
becomes a paragraph the client reads in Phase 7. Overrides nobody wants to explain tend not to be
requested — which is a better outcome than a system that simply forbids them and gets worked around
outside the platform.

**Override rate is a practice health metric**, reported on Oversight. A rising rate on one gate means
either the gate is wrong or the process is under strain; both are worth knowing.

---

## 7. What a blocked gate looks like to different people

| Role | Sees |
|---|---|
| **Analyst** | On their Now screen: what is blocked, which assets it affects, and that it is not theirs to fix |
| **Engagement Manager** | The full gate panel with per-condition owner and age, and the actions available |
| **Reviewer** | Only the gates they pass — Custody, Evidence Integrity, QA |
| **Management** | Aggregate: how many engagements blocked, on which conditions, for how long, and every live override |

---

## 8. Validation status

| | Count |
|---|---|
| Gates specified | 7 |
| Conditions specified | 63 |
| Fact-evaluated `[F]` | 45 *(71%)* |
| Attestation `[A]` | 18 |
| Non-overridable gates | 2 *(Custody, Release)* |
| `SME-VALIDATED` | **0** |

**`[GAP]` non-blocking:** threshold values — how long a blocked item may age before escalating, and
how long an override may run. **Needs Sleuth Confirmation.**
