# 23 — Archetype Modules (A1–A4)

> **Status — Draft / Needs SME Validation.** Provenance: `INDUSTRY-PRACTICE` and
> `EXTERNAL-STANDARD`, never `SLEUTH-SUPPLIED`. These are recognised professional practice drafted
> as a starting point for Sleuth's SMEs to correct, not a claim about how Sleuth works.

Phases 4–6 — the execution shape. Each archetype module is inherited by every engagement type of
that archetype, alongside the core spine in `22-core-spine-specification.md`.

---

## In plain terms

The core spine covers the paperwork and process common to every job. These four modules cover
*doing the work*, and there are only four ways Sleuth does it:

- **A1** — look at how something is set up and judge it against a standard.
- **A2** — try to break in, with written permission and inside agreed limits.
- **A3** — find out what happened, and be able to prove it later.
- **A4** — watch something continuously and report what changed.

---

## Standards baseline

Each module is drafted against recognised public standards. **Needs Sleuth Confirmation** that these
are the ones Sleuth adopts — this is a policy choice, not a technical one, and it belongs to Sleuth.

| Archetype | Drafted against |
|---|---|
| A1 | NIST CSF 2.0 · ISO/IEC 27001/27002 · CIS Benchmarks · IEC 62443 and NIST SP 800-82 *(OT)* — all named or implied on the site |
| A2 | NIST SP 800-115 · PTES · OWASP WSTG · OWASP ASVS · OWASP API Security Top 10 · OWASP MASTG/MASVS · MITRE ATT&CK |
| A3 | NIST SP 800-61 *(incident handling)* · ISO/IEC 27037 *(evidence)* · ISO/IEC 27041–27043 · SWGDE and NIST CFTT *(tool validation)* |
| A4 | NIST CSF 2.0 Detect/Respond · MITRE ATT&CK for coverage mapping |

---

# `arch.A1` — Assessment & Advisory

**Used by:** `SF-A1-SPA` · `SF-A1-CRA` · `SF-A1-TCR` · `SF-A1-OTA` · `SF-A1-SOA` · `SF-A1-IRA`

| ID | Procedure | Objective / key steps | Records |
|---|---|---|---|
| `A1-01` | Framework selection & justification | Select the benchmark and record *why it fits this client*. A framework chosen by default rather than by fit produces findings the client cannot act on | Framework, version, scope of applicability, rationale |
| `A1-02` | Documentation request & tracking | Issue a structured request; track receipt, currency and sufficiency per item. ⊗ assessing a control with no documentation is a **gap finding**, not an assumed pass | Per-document: requested, received, date, currency, sufficiency |
| `A1-03` | Stakeholder interview protocol | Structured interviews with control owners. Same questions to comparable roles so answers are comparable | Interviewee, role, date, notes, statements relied upon |
| `A1-04` | Control walkthrough | Observe the control operating, not only its description. "Show me" beats "tell me" | Observation record, what was seen, by whom, date |
| `A1-05` | Configuration & artefact review | Review exported configuration against the benchmark. ⟪domain_pack⟫ — the service module supplies the control set | Artefacts reviewed, tool used, deviations found |
| `A1-06` | Maturity rating | Rate each control. **Every rating must cite its source** — document, interview, observation or artefact | Rating, scale, source citation, rated by, confidence |
| `A1-07` | ⟨ **Evidence Sufficiency check** ⟩ | No rating may stand without a source. An unsourced maturity score is an assumption wearing a number | Per-rating source check |
| `A1-08` | Gap identification | Difference between current and target state, per control | Gap, current, target, control reference |
| `A1-09` | Risk contextualisation | Translate gaps into business risk *for this client*. A gap in a control protecting nothing valuable is not a priority | Risk statement, business context, likelihood/impact basis |
| `A1-10` | Roadmap construction | Sequence remediation by risk, dependency and the client's actual capacity to deliver | Sequenced items, dependencies, effort, owner |
| `A1-11` | Quick wins | Identify low-effort, meaningful improvements deliverable immediately | Quick-win list with effort estimates |

**A1 stop conditions**
⊗ The client asserts a control exists but can produce no evidence of it — record as a gap, do not
rate it as present.
⊗ Documentation provided is materially out of date and no current version exists.
⊗ Scope proves materially larger than agreed — ▲ Engagement Manager before continuing.

**A1 deliverable shape:** maturity scorecard → gap analysis → prioritised roadmap → executive summary.

> **Assumption AS-A1-1.** Maturity is expressed on a 5-level scale. Which scale (CMMI-style, NIST
> CSF tiers, or a Sleuth scale) is **Needs Sleuth Confirmation** — it must be consistent across
> engagements or year-on-year comparisons become meaningless.

---

# `arch.A2` — Authorised Technical Testing

**Used by:** `SF-A2-IPT` · `SF-A2-WAT` · `SF-A2-MAT` · `SF-A2-CPT` · `SF-A2-ATP` · `SF-A2-RED` · `SF-A2-SES`

| ID | Procedure | Objective / key steps | Records |
|---|---|---|---|
| `A2-01` | Rules of Engagement construction | Injects at `⟪roe_extension⟫`. Permitted and prohibited actions, intrusiveness ceiling, windows, deconfliction, emergency contacts, data-handling rule if live customer data is encountered. ✋ client approval | RoE instance, approval, prohibited actions |
| `A2-02` | Pre-test asset ownership verification | **Independently confirm every target belongs to the client** before touching it. ⊗ any unverified asset is removed from scope | Per-asset ownership verification, method, evidence |
| `A2-03` | Test account validation | Confirm accounts exist, work, and carry the intended privilege level. Records existence and delivery channel — **never the credential** *(Rule 4)* | Account ref, role, delivery channel, verified working, expiry |
| `A2-04` | Testing window open | Notify agreed parties, confirm client contacts reachable **now**, log start. ⊗ testing outside the window is an authorisation breach | Window open timestamp, notifications sent, contacts confirmed |
| `A2-05` | Reconnaissance | Passive information gathering within scope. ⟪service_recon⟫ | Sources, findings, tool + version, timestamps |
| `A2-06` | Enumeration | Active discovery of hosts, services, endpoints, functions. ⟪service_enum⟫ | Discovered assets, services, versions; comparison to the approved schedule |
| `A2-07` | Vulnerability identification | Automated and manual identification. ⟪service_vulnid⟫ | Candidate findings, source, tool + version |
| `A2-08` | Manual validation | Confirm exploitability without exceeding the intrusiveness ceiling. **Record non-exploitable candidates and why** | Per-candidate: confirmed/discounted, reasoning, evidence |
| `A2-09` | Controlled exploitation | Only to the depth the RoE permits, stopping at proof. ✋ where the RoE requires approval for a specific action | Action taken, authority relied on, timestamp, evidence |
| `A2-10` | Post-exploitation assessment | Demonstrate business impact within scope. ⊗ no pivoting outside scope; ⊗ no access to live customer data beyond what the RoE permits | Access achieved, impact demonstrated, boundaries respected |
| `A2-11` | Proof-of-concept capture | Request/response pairs, screenshots, command logs — captured **as the work happens** | Evidence items with capture timestamps |
| `A2-12` | Testing window close | Log stop, confirm no active sessions or running tools remain | Window close timestamp, confirmation |
| `A2-13` | Client artefact cleanup | Remove everything Sleuth created — accounts, files, shells, rules, scheduled tasks — and **verify removal**. Feeds `CL-06` | Artefact inventory, removal verified by, date |
| `A2-14` | Finding drafting & severity | Draft findings with severity, rationale and reproduction steps | Findings with evidence links |
| `A2-15` | Retest | Verify remediation. Outcome vocabulary: Resolved · Partially resolved · Not resolved · Risk accepted · Unable to verify | Per-finding retest outcome, date, tester |

**A2 stop conditions** — these halt work immediately, with no judgement call required:

| ⊗ | Why it is absolute |
|---|---|
| **Evidence of a pre-existing compromise is found** | The highest-stakes moment in this work. Sleuth is now a witness to someone else's intrusion. ▲ Engagement Manager → client emergency contact, immediately. Propose an IR child engagement |
| A production system becomes unstable or unavailable | ▲ client on-call immediately. Preserve what was being done at the moment it occurred |
| Testing reaches an asset not on the approved schedule | Stop, do not proceed, record how it was reached |
| The testing window has expired | Continuing is testing without authorisation |
| Live customer personal data is encountered beyond what the RoE contemplates | Stop, do not copy, ▲ Engagement Manager |
| Authorisation lapses or is withdrawn | Absolute, at any point |

**A2 deliverable shape:** findings register with evidence → risk analysis → prioritised remediation → retest.

---

# `arch.A3` — Investigation & Response

**Used by:** `SF-A3-IRE` · `SF-A3-DFE` · `SF-A3-SPY` · `SF-A3-CTH` · `SF-A3-MAL`

| ID | Procedure | Objective / key steps | Records |
|---|---|---|---|
| `A3-01` | Instruction & authority capture | **What exactly are we asked to determine?** Record the questions posed, in the client's words, and the authority to examine. ⊗ no examination without recorded authority | Questions posed, instructing party, authority basis |
| `A3-02` | Initial triage & scoping | Establish what is known, what is suspected, and what is at stake right now | Initial picture, working hypotheses, priority |
| `A3-03` | Prior-handling enquiry | **What has already been done?** Reboots, reimaging, AV cleaning, password resets, rebuilds — all destroy evidence. Frequently under-asked and decisive | Actions taken by others, by whom, when, impact on evidence |
| `A3-04` | Evidence identification & preservation | Identify all potential sources; issue preservation instruction to the client immediately | Source inventory, preservation instruction, issued to, at |
| `A3-05` | Volatility decision | Powered on or off? Capture volatile data first, or write-protect and image. Recorded traversal of the handling decision tree | Decision, branch, rationale, decided by |
| `A3-06` | Acquisition | Runs `EV-03`–`EV-06`. Write-blocking, hashing, verification, custody opened. ⟨ **Custody Gate** — not overridable ⟩ | Full acquisition record |
| `A3-07` | Working copy derivation | Runs `EV-08`. **All analysis is on working copies. Never the source** | Parent-child provenance |
| `A3-08` | Artefact processing | Parse, normalise, index. ⟪service_processing⟫ | Tool + version + parameters, outputs, reproducibility |
| `A3-09` | Timeline construction | Build a normalised timeline across sources. **All times normalised to a single stated timezone**, with source timezone retained | Timeline, sources, normalisation basis |
| `A3-10` | Hypothesis formulation & testing | State hypotheses explicitly; test each against evidence. Structured rather than narrative investigation | Hypotheses, tests applied, supporting/contradicting evidence |
| `A3-11` | Alternative explanation consideration | **Mandatory.** What else could explain this, and why was it discounted? | Alternatives considered, basis for discounting |
| `A3-12` | Containment advisory | *(IR only)* Advise; the client acts. Sleuth changes nothing without explicit authorisation | Advice given, to whom, when, client action taken |
| `A3-13` | Eradication verification | *(IR only)* Verify the threat is actually gone before recovery is declared | Verification method, result, residual risk |
| `A3-14` | Conclusion formulation | State conclusions **with a confidence level**, answering the questions from `A3-01` | Per-question conclusion, confidence, supporting evidence |
| `A3-15` | Limitations documentation | What could not be determined, and why. Feeds `RP-04` | Limitations with causes |

**A3 stop conditions**

| ⊗ | Why |
|---|---|
| Evidence integrity cannot be established, or is found broken | The work cannot support a conclusion |
| Material conflict of interest emerges | |
| **Findings implicate the person who commissioned the investigation** | ▲ **Management directly, bypassing the Engagement Manager.** An examiner at 11pm must not have to decide this alone |
| Authority to examine is withdrawn or proves insufficient | |
| A safety risk to a person is identified | Particularly `SF-A3-SPY` — an examination can itself put someone at risk |

> `A3-11` is the procedure that separates an investigative conclusion from an assertion, and it is a
> required field rather than a matter of examiner discipline. It is also the first thing a competent
> opposing expert will look for.

**A3 deliverable shape:** instructions and authority → evidence inventory → custody summary →
acquisition and methods → timeline → findings of fact → analysis → alternatives considered →
limitations → conclusion with confidence.

---

# `arch.A4` — Continuous & Readiness

**Used by:** `SF-A4-ASM` · `SF-A4-VCI`

| ID | Procedure | Objective / key steps | Records |
|---|---|---|---|
| `A4-01` | Baseline establishment | Establish the first-cycle baseline. Everything afterwards is measured against it | Baseline snapshot, date, scope |
| `A4-02` | Collection cycle | Run the scheduled collection. ⟪service_collection⟫ | Cycle ID, period, sources, completeness |
| `A4-03` | Delta analysis | What is new, changed, resolved since last cycle | Deltas by category, comparison basis |
| `A4-04` | Alert triage | Triage and dispose of each alert: actioned, accepted, false positive, escalated | Per-alert outcome, rationale, by whom |
| `A4-05` | Escalation to incident | Where a finding indicates active compromise, ▲ and propose an IR engagement. **Pre-agreed at scoping, never negotiated mid-incident** | Trigger, escalation, client notified, at |
| `A4-06` | Cycle report | Report the cycle: deltas, alerts, recommendations | Cycle report, period, recipients |
| `A4-07` | Periodic re-authorisation | Re-confirm scope and authority each period. ⊗ an expired standing authorisation blocks the next cycle | Re-authorisation date, by whom, scope changes |
| `A4-08` | Coverage review | Is the monitored perimeter still the right perimeter? Clients acquire, divest and migrate | Coverage changes, gaps identified |
| `A4-09` | Cycle close | Close the cycle. **Not engagement closure** — no disposition, no lessons-learned | Cycle closed, next cycle scheduled |

**A4's defining property:** there is no Closure Gate while the contract runs. `A4-07` exists so a
standing authorisation cannot quietly run for years — the failure mode this archetype is most prone to.

---

## Archetype comparison — what actually differs

| | A1 | A2 | A3 | A4 |
|---|---|---|---|---|
| Procedures | 11 | 15 | 15 | 9 |
| Additional gates | Evidence Sufficiency | — | **Custody (un-overridable)** | — |
| Evidence depth | Source citation | Capture + retain | **Full custody ladder** | Snapshot retention |
| Own stop conditions | 3 | 6 | 5 | 2 |
| Deliverable | Scorecard + roadmap | Findings register | Narrative + timeline | Cycle delta |
| Closure | Report accepted | Retest closed | **Disposition executed** | None — cycle close only |

---

## Validation status

| | A1 | A2 | A3 | A4 |
|---|---|---|---|---|
| Procedures specified | 11 | 15 | 15 | 9 |
| `SME-VALIDATED` | 0 | 0 | 0 | 0 |
| `DRAFT` | 11 | 15 | 15 | 9 |
| Blocking `GAP`s | 1 | 1 | 0 | 1 |

**Blocking gaps at archetype level:**

| Gap | Consequence |
|---|---|
| `A1-06` maturity scale not defined | Ratings are not comparable across engagements or over time until Sleuth chooses one |
| `A2-09` intrusiveness ceiling not defined | An analyst cannot be told "stop at proof of access" without a definition of proof of access that Sleuth stands behind. **This is the most important single gap in the current design** |
| `A4-02` collection cadence not defined | Cycle scheduling is unspecified |
