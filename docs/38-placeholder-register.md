# 38 — Placeholder Register

> Sleuth's instruction: *"set placeholders if you're not sure."*
>
> A placeholder is **not** an invented answer. It is a typed slot with a stated default, so work
> continues and the thing that needs Sleuth's input stays visible. Rule 2 is intact: nothing here
> fills a technical procedure with plausible text.

**Three kinds, and the distinction matters:**

| Kind | Meaning | Risk of the default being wrong |
|---|---|---|
| **DEFAULT APPLIED** | A sensible professional default is in place and the platform works with it | Low — change it later at little cost |
| **SHAPE ONLY** | I have specified the *structure* of the answer but not the content | None — the slot is visibly empty |
| **BLOCKING** | No defensible default exists. The engagement type cannot be run through the platform | High — filling it with a guess would be worse than the gap |

---

## 1. Defaults applied — 17

These are live. The platform works. Change any of them cheaply.

| Ref | Placeholder | Default applied | Where |
|---|---|---|---|
| `PH-01` | Sleuth house report styling | Inherit the public site design system | `34` |
| `PH-03` | Attestation / certificate letters for compliance-driven tests | **Not offered** | `34` |
| `PH-04` | vCISO board pack format | One page: risk posture · top three · decisions needed | `34` |
| `PH-05` | Executive summary convention | One page, no unexplained technical terms | `34` |
| `PH-06` | Incident severity bands | Three: single system · multiple systems or one business process · enterprise-wide or safety-affecting | `35` |
| `PH-07` | Incident-type module set | Five named plus Unknown; supply chain folded into Web Compromise | `35` |
| `PH-08` | Routing for enquiries Sleuth does not serve | Qualify out, record the reason, refer where appropriate | `35` |
| `PH-11` | Tool revalidation trigger | Annually, or on version change for acquisition and integrity tools | `36` |
| `PH-12` | Client-provided tooling | Permitted with an exception record; **never** for acquisition or integrity | `36` |
| `PH-14` | Identity provider | Local accounts, OIDC-ready | `37` |
| `PH-16` | Classification vocabulary | Client Confidential · Restricted · Privileged · Personal Data | `37` |
| `PH-17` | Sector list | The 9 from the industries page | `37` |
| `PH-18` | Engagement ID format | `ENG-YYYY-NNNN`, per-year sequence | `10` |
| `PH-19` | Report retention in-platform | Indefinite until a retention policy is set *(E5)* | `37` |
| `PH-20` | Questionnaire delivery | Consultant-mediated. No client-facing surface in Phase 1 | `33` |
| `PH-21` | Maturity target state | Set per control with the client, **not assumed to be level 5** | `32` |
| `PH-22` | Coverage reporting for hunts and assessments | Percentage of intended estate, stated in the report | `34` |

---

## 2. Shape only — 5

Structure specified, content awaiting Sleuth. **When an SME sits down, they fill a form rather than
face a blank page.**

### `PH-09` — Tool inventory *(`36`)*
The catalogue ships empty. Shape supplied: 97 capabilities, the tool/version/validation schema, and
the two mandatory fields (`limitations`, `data_handling_notes`). Sleuth populates with what they own.

### `PH-10` — Tool validation method *(`36`)*
Shape: known-dataset test · documented expected vs actual result · dated · named examiner · stored
reference · next-due date. Referenced against SWGDE and NIST CFTT practice. **Sleuth defines the
datasets and the pass criteria.**

### `PH-13` — Retention periods *(`37`)*
Shape: a period per record class — evidence register · reports · audit log · questionnaire responses ·
closed engagements. Configurable; **no default hard-coded**, deliberately. Counsel matter E5.

### `PH-15` — Storage location vocabulary *(`37`)*
Shape: an enum of Sleuth's actual storage locations plus a medium identifier. Free text until Sleuth
describes what they have *(C3)*. The register's value depends on this matching reality.

### `PH-23` — Runbook authoring order
Shape: 20 engagement types ranked by annual volume × blocking-gap count. **Volumes are the missing
input** *(C1)*. Interim order applied: `SF-A2-IPT` → `SF-A2-WAT` → `SF-A3-IRE` → `SF-A1-TCR` → rest.

---

## 3. Blocking — 7

**No defensible default exists.** Each one depends on Sleuth's tooling, infrastructure, risk appetite
or legal position. A plausible-looking guess would be actively dangerous: an analyst following an
invented procedure believes they are following Sleuth's method.

| # | Placeholder | Engagement type | Why only Sleuth can supply it | Shape I have specified |
|---|---|---|---|---|
| 1 | **Triage collection scope and order** | `SF-A3-IRE` | Depends on Sleuth's tooling and what their responders collect first, under time pressure. **The most operationally important remaining gap** | A priority table: rank · system class · artefacts to collect · capability required · time budget · fallback if unavailable |
| 2 | **Hunt hypothesis library and sweep set** | `SF-A3-CTH` | Depends on telemetry access, tooling and intelligence sources | Per hypothesis: statement · data sources required · query shape · what a positive looks like · what coverage it claims |
| 3 | **Isolated analysis environment specification** | `SF-A3-MAL` | Sleuth's own infrastructure. Getting it wrong risks Sleuth's network | Network policy · snapshot/revert method · egress rules · sample handling · sanitisation and verification |
| 4 | **OT passive observation method and safety approval** | `SF-A1-OTA` | Site- and vendor-specific. **Must not be drafted from general practice** | Method · approval chain · engineer role · abort conditions · what may never be connected |
| 5 | **Safeguarding position sign-off** | `SF-A3-SPY` | Duty of care. Principle confirmed; needs a named owner, counsel review, and **a referral list of support organisations in India** | Drafted in full at `32` §3. Referral list deliberately empty — a wrong referral here is worse than none |
| 6 | **Red team permitted-technique sign-off** | `SF-A2-RED` | Firm risk appetite. Baseline drafted; needs the person who carries that risk to own it | Drafted in full at `32` §5 |
| 7 | **Expert reports, testimony, electronic-record certificates** | `SF-A3-DFE` | Counsel *(E4)*. Changes the report format and custody documentation materially | Two template variants prepared; which one applies is unknown |

### Consequence, stated plainly

**14 of 20 engagement types carry no blocking placeholder.** Those 14 can be built and run once their
procedures are SME-validated.

The six that cannot: `SF-A3-IRE` · `SF-A3-CTH` · `SF-A3-MAL` · `SF-A1-OTA` · `SF-A3-SPY` ·
`SF-A3-DFE`. Five of those six are investigation work.

> That pattern is worth noticing. The gaps cluster exactly where Sleuth's own expertise is
> irreplaceable — and, if investigation is the core of the business, exactly where the platform most
> needs their input. It is also the strongest argument for answering the investigation-versus-testing
> split question *(C, `30` Part D)*: if forensics is the bulk of the work, these six become the
> priority rather than the remainder.

---

## 4. Facts still outstanding — 5

Not placeholders. Requests for information, unanswerable by anyone but Sleuth.

| Ref | Needed | Blocks |
|---|---|---|
| **C2** | **Validating SME per pillar** | **Everything.** Rule 1 is inert without named people, and SME validation stands at 0% |
| C1 | Which of the 20 types are live, and annual volume | Authoring order *(`PH-23`)* |
| C3 | Where evidence is physically held today | `PH-15` |
| C4 | Hosting and data residency | Infrastructure decisions |
| D | Investigation vs security-testing revenue split | First build target; priority of the six blocked types |

---

## 5. Summary

| | Count |
|---|---|
| Defaults applied — platform works | **17** |
| Shape specified, content awaited | **5** |
| Blocking — no defensible default | **7** |
| Facts outstanding | **5** |
| **Engagement types with no blocking placeholder** | **14 of 20** |

Nothing in this repository invents a technical procedure, a fact about Sleuth, or a legal position.
Where I was not sure, there is a placeholder with its kind, its default, and who can close it.
