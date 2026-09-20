# 29 — Architecture Amendments (v2)

> **Status — `PROPOSED`, Draft / Needs SME Validation.**
> Amends docs 02, 08, 09, 10, 11, 14 and 16 for the v2 catalogue (`21`), the spine and archetype
> specifications (`22`, `23`), the ETS set (`24`–`27`), and the checklist/gate architecture (`28`).
> Where this document conflicts with an earlier one, **this document wins.**

---

## 1. Findings model — amends `08` §1

### Three finding kinds, not one

The v2 catalogue makes explicit what doc 08 only implied: the archetypes produce structurally
different assertions, and forcing them into one "finding" shape damages all three.

| Kind | Produced by | Core fields beyond the common set |
|---|---|---|
| **Vulnerability finding** | A2 | Severity + rationale · affected assets · reproduction steps · exploitation evidence · remediation effort · retest outcome |
| **Control gap** | A1 | Control reference · current state · target state · **source citation (mandatory)** · risk contextualisation · remediation effort · roadmap position |
| **Finding of fact** | A3 | The determination · supporting evidence · **confidence level** · **alternative explanations considered and why discounted** · which question posed it answers |

Common to all three: ID · title · description · impact · evidence links *(≥1, enforced)* ·
author ≠ reviewer · status · severity history · client response.

**A4 produces vulnerability findings** *(exposures)* plus **cycle deltas**, which are not findings but
change records.

### Severity

One scale across all three kinds, so a client with several engagement types gets consistent language:
`Critical · High · Medium · Low · Informational`, with **written rationale mandatory** and CVSS
optional and supplementary for A2.

> **`[GAP]` blocking.** Sleuth's severity definitions — what makes something Critical rather than
> High *for this firm*. Without them, calibration (`08` §1.1) has nothing to calibrate against.
> **Needs Sleuth Confirmation.** My recommendation: define it by *business consequence* rather than
> technical severity, because that is how the site positions its reporting ("risk-rated vulnerabilities
> with business impact context").

---

## 2. Reporting model — amends `08` §2–§3

**One report template per engagement type: 20, not 21.** Composition unchanged:
`universal spine + archetype sections + service sections + conditional sections`.

Two amendments:

**Report templates are versioned and pinned** like runbooks, and composed from the same shared
modules — so a change to the universal spine's limitations section propagates to all 20 templates in
one edit *(`20-shared-module-inheritance.md`)*.

**Limitations auto-seeding extends** *(amends `RP-04`)*. It now also draws from:
- procedures executed under `DRAFT — NEEDS SME VALIDATION` runbook content *(new, from Rule 1)*
- active deltas against inherited content *(`20` §5)*
- checklist items marked `Not applicable` that were `Required`
- coverage shortfalls in A3 hunts and A1 assessments

> The first of those is the one worth noting. If Sleuth runs an engagement on a runbook containing
> unvalidated procedures, the client's report says so. That is uncomfortable, and it is correct — and
> it creates a strong internal incentive to get runbooks validated.

---

## 3. Roles & permissions — amends `02`

### Role added: SME Validator

Rule 1 is inert without named people *(NC-28)*. Distinct from Runbook Author: an author *writes*,
a validator *confirms it is how Sleuth actually works*.

| Capability | SME Validator |
|---|---|
| Set `validation_status` to `SME-VALIDATED` or `REJECTED` | ✓ within their pillar |
| Author runbook content | ✓ |
| Approve a runbook to `Approved` | ⊘ — Management |
| Access engagements | ⊘ unless separately a member |

**One person may hold several roles.** The system enforces the object-level rules regardless —
`author_id ≠ reviewer_id` holds even when the same human is both an Analyst and a Reviewer on
different engagements.

### Two amendments to the existing matrix

**Direct-to-Management escalation.** A3 stop conditions include *"findings implicate the person who
commissioned the investigation"*. That escalation must **bypass the Engagement Manager**, who may be
the person in contact with the implicated party. The platform needs a confidential escalation channel
visible only to Management, and it must be reachable in one action from the Now screen.

**vCISO independence.** Where Sleuth provides `SF-A4-VCI` to a client, **the vCISO cannot be the
authoriser for Sleuth's own testing engagements at that client** *(`27`, `SF-A4-VCI` §5)*. Enforced
as a rule on the Authorisation Gate: the client-side signatory must not be a Sleuth-supplied vCISO.

---

## 4. Data model — amends `10`

### Content plane additions

| Entity / field | Purpose | Source |
|---|---|---|
| `provenance`, `provenance_ref` on every content object | Rule 6 — where did this come from | `18` |
| `validation_status` + validator, date, note, revalidation due | Rule 1 | `18` |
| **`Gap`** entity — description, consequence, owner, blocking | Rule 2's alternative to invention | `18` |
| `CompositionManifest` on RunbookVersion — module + version per slot | The "change once" guarantee | `20` |
| `ExtensionPoint` on Procedure | Injection without forking | `20` |
| **`Delta`** entity — target, reason, approver, review date | Explicit, approved divergence | `20` |
| `ChangeClass` on ModuleVersion — editorial / substantive / breaking | Propagation control | `20` |
| `EngagementTypeMode` | IPT external/internal/wireless/VA; IRA assessment/exercise | `21` |
| `DomainPack` | TCR cloud/identity/endpoint/network; A1 assessment domains | `21` |
| `IncidentTypeModule` | IRE ransomware/BEC/data theft/insider/web/unknown | `21` |

### Execution plane additions

| Entity / field | Purpose |
|---|---|
| `Attestation` on checklist items — who asserted, on what basis | `28` §2 |
| `selected_mode`, `selected_packs[]`, `selected_incident_module` on Engagement | Which variant is running |
| `incident_module_history[]` | **Records when the incident type changed and why** — the early hypothesis is often wrong |
| `AccessGrant` — account ref, purpose, delivery channel, verified, expiry, **revocation confirmed** | Rule 4: track access without holding secrets |
| `QuestionPosed` on A3 engagements | `DFE-01` → `DFE-12` bookend |
| `CoverageStatement` on A3 hunts and A1 assessments | What was checked, not only what was found |
| `ConfidenceLevel` on findings of fact | A3 |

### Invariants added to `10` §4

9. No entity or field may store a credential, key, password or secret *(Rule 4)*.
10. No entity stores evidence content; `storage_location` is an outward reference only *(Rule 3)*.
11. A `RunbookVersion` cannot reach `Approved` while any composed procedure is `DRAFT` or `IN SME REVIEW` *(Rule 1)*.
12. A `Delta` requires an approver distinct from its author, and a review date.
13. A client-side authoriser on the Authorisation Gate must not be a Sleuth-supplied vCISO for that client.

---

## 5. Navigation — amends `09`

Top-level navigation is unchanged at seven items. Two additions **inside Library**:

| Addition | Why |
|---|---|
| **Validation Queue** | The SME work queue *(`18` §3)*. Per pillar: draft / in review / validated / gaps. This is where runbook readiness is actually managed |
| **Gap Register** | Every `GAP`, ordered by how many engagement types it blocks. The single best view of "what stops us selling this through the platform" |

One addition **inside Oversight**: **Deltas & Overrides** — every live delta and every active gate
override, with expiry dates. Both are deliberately made visible because both are ways the system's
rules get bent, and bending should be seen.

---

## 6. UX — amends `11`

### New: validation banner on procedure execution
Specified in `18` §3. Non-dismissible, above the procedure content, naming the provenance and the
owner. Analysts must know when they are working from unvalidated content.

### New: engagement configuration step at scoping
Between engagement type selection and the questionnaire, the Engagement Manager selects **mode**,
**domain packs** and **incident-type module**. These choices change which procedures, questions,
documents and gate conditions apply — so they belong at scoping, visibly, not buried in a settings tab.

### New: Questions Posed panel — A3 only
`DFE-01`'s agreed questions pinned to the engagement header throughout, and each conclusion in
`DFE-12` mapped back to one. It keeps the examination anchored to what it was commissioned to answer.

### New: confidential escalation action
On the Now screen for A3 engagements, alongside the normal escalation contacts: a direct-to-Management
route that does not notify the Engagement Manager. Present without drama, reachable in one action.

### Amended: Now screen stop conditions
Now rendered from the composed set — core + archetype + service + active context modules — rather
than a static list. `SF-A1-OTA` shows safety stops; `SF-A2-RED` shows deconfliction; `SF-A3-SPY`
shows personal-safety stops.

---

## 7. Exports — amends `14`

Three workbooks added:

| Workbook | Contents | For |
|---|---|---|
| **Gap Register** | Gap · engagement types blocked · consequence · owner · blocking Y/N | Sleuth's SME planning |
| **Validation Status** | Module · procedure · provenance · validation status · validator · date · revalidation due | Practice readiness reporting |
| **Access & Revocation** | Account ref · purpose · delivery channel · verified · expiry · revocation confirmed | Closure assurance *(Rule 4)* — **and a genuinely useful client deliverable** |

The Evidence Register export gains a **Custody Completeness** column *(gaps detected, per `EV-11`)*,
and the Findings Register gains **Confidence** for A3 findings of fact.

---

## 8. Implementation plan — amends `16`

### Phase scope changes

| Phase | Change |
|---|---|
| **0** | Add provenance and validation fields from the start — they touch every content object and cannot be retrofitted |
| **1** | Add composition manifests, extension points, change classification and impact analysis *(`20` §10 — all four are foundational)*. Add mode/pack/module selection |
| **2** | Add the three finding kinds *(§1)*. Findings Register export pulled forward |
| **3** | **Reduced** — register, custody and disposition only. No storage subsystem |
| **4** | Add the confidential escalation channel and the Questions Posed panel |
| **7** | Add Gap Register, Validation Status and Access & Revocation exports |

### First vertical slice — recommendation

**`SF-A2-IPT` in external mode.** Unchanged reasoning: A2 carries the most externally-imposed
structure, so building it first exercises authorisation, scope, gates, findings, reporting and retest
— machinery every other archetype reuses.

> **But there is a real question underneath this, and it is for Sleuth.** The firm is called Sleuth
> *Forensics*, and its positioning leads with investigation — yet 10 of the 21 public services are
> security assessment and testing. If the actual revenue is dominated by A3 investigation work, the
> first slice should be `SF-A3-DFE` instead.
>
> The trade-off is real: A3 first means building custody and evidence machinery before findings and
> reporting exist, which is a harder, slower start — but it would be the right call if that is where
> the business is. **I cannot tell from the website which it is.** See the decision list.

---

## 9. Amendment summary

| Amended | Sections |
|---|---|
| `02` Users & Roles | SME Validator role · direct-to-Management escalation · vCISO independence |
| `08` Findings & Reporting | Three finding kinds · severity gap · extended limitations auto-seeding |
| `09` Information Architecture | Validation Queue · Gap Register · Deltas & Overrides |
| `10` Data Model | 11 content/execution additions · 5 new invariants |
| `11` UX | Validation banner · configuration step · Questions Posed · confidential escalation · composed stop conditions |
| `14` Excel Exports | 3 new workbooks · 2 amended |
| `16` Implementation Plan | Phase scope changes · first-slice question raised |
