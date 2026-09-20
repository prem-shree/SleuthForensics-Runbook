# 21 — Engagement Catalogue v2 (Recommended)

> **Status — `PROPOSED` by Claude, **Draft / Needs SME Validation**.** This is my professional
> recommendation for what Sleuth should actually run engagements against. It **supersedes the 41
> types in `01-service-catalogue.md`**, which were a ceiling derived from website copy rather than a
> deliverable catalogue.
>
> Provenance of the *service names and public descriptions* remains `SITE-DERIVED`. The
> **consolidation, the engagement types and the archetype assignments are my judgement**, marked as
> assumptions throughout and flagged **Needs Sleuth Confirmation** where only Sleuth can decide.

---

## In plain terms

The website sells 21 services. But several of them are the *same job* with a different label on the
invoice, and a few are two completely different jobs sharing one label.

What matters operationally is: **how many genuinely different ways of working are there?** Because
each one needs its own step-by-step runbook, and each runbook needs a senior person to write and
validate it. Writing 41 is unrealistic. Writing 6 would be so generic it would help nobody.

My recommendation is **20**. All 21 public services are still sold — nothing disappears from the
website. They just map onto 20 ways of working underneath.

---

## 1. How I consolidated, and why

Four tests, applied to each candidate type:

| Test | Question |
|---|---|
| **Day-one test** | Does an analyst do something materially different on day one? If not, same type |
| **Authorisation test** | Does it need different legal authority or approvals? If yes, likely a different type |
| **Evidence test** | Is what must be recorded, and how carefully, different? If yes, likely different |
| **Deliverable test** | Is the output structurally different — a register vs a narrative vs a scorecard? |

If all four say "same", it is one engagement type with a **mode** or **module**, not two runbooks.

### What that collapsed

| Collapsed | Into | Reasoning |
|---|---|---|
| VAPT External · VAPT Internal · Network Pen Test · Wireless · Vulnerability Assessment | **Infrastructure Penetration Test** with modes | Same authorisation posture, same evidence, same deliverable shape. Scope and intrusiveness differ — that is a mode switch, not a different job |
| Consulting maturity · Security audit · Pre-certification review | **Security Programme & Maturity Assessment** + **Compliance Readiness Assessment** | Two genuinely different drivers: "how good are we?" vs "will we pass an audit?". The second is auditor-facing and evidence-for-certification; that changes the work |
| Cloud config review · AD config review · Endpoint hardening review · Network architecture review | **Technical Configuration Review** with domain packs | Identical process — obtain read-only access, extract config, compare to benchmark, rate, recommend. The *domain pack* carries the specificity |
| Ransomware Investigation · DFIR · Incident Response · Breach Scope Assessment | **Incident Response** with incident-type modules | This is how real response teams work: one process, modules for ransomware, business email compromise, data theft, insider, web compromise. Ransomware is still sold by name |
| Ransomware Readiness · Tabletop & Playbook Development | **Incident Readiness Assessment & Exercise** with two modes | Usually sold together; the exercise validates the assessment |
| Periodic Threat Hunt | **Compromise Assessment & Threat Hunt**, run on a recurring schedule | A cadence, not a different job |

### What I deliberately kept separate

| Kept apart | Why |
|---|---|
| Web/API testing vs Mobile app testing | Different tooling, different skills, different standards, different findings. Genuinely different work |
| Cloud *configuration review* vs Cloud *penetration test* | One is read-only against a benchmark; the other is active testing needing a Letter of Authorisation and a provider-policy check. Fails the authorisation test |
| Identity config review vs **Attack Path Assessment** | Same split: reading AD settings vs actively proving a path from standard user to domain admin |
| Social Engineering vs Red Team | People are the target. Needs HR and legal approval, staff-welfare handling, and a different reporting rule (never name individuals). Fails the authorisation test |
| OT/ICS Assessment | Safety-critical. Passive by default, engineer-accompanied, physical site, stop-on-anomaly. Fails all four tests |
| Mobile Device Spyware Examination | Often an **individual** client, not a company. Different contracting, different consent, genuine personal-safety handling |
| Malware Analysis | Usually a *child* of another engagement, inheriting its authority and custody. Structurally distinct |

---

## 2. The recommended catalogue — 20 engagement types

`SF-<archetype>-<code>`. Archetype-first IDs, because the archetype determines gates and obligations,
and that is what an analyst most needs to recognise at a glance.

### A1 — Assessment & Advisory (6)

| ID | Engagement type | Public services covered | Notes |
|---|---|---|---|
| `SF-A1-SPA` | Security Programme & Maturity Assessment | 1 Consulting · 2 Audits | Modes: full programme · targeted domain · M&A review |
| `SF-A1-CRA` | Compliance Readiness Assessment | 21 Compliance/GRC · 2 Audits (pre-cert) | Framework packs: ISO 27001, SOC 2, NIST CSF *(named on site)* |
| `SF-A1-TCR` | Technical Configuration Review | 4 Network · 8 Cloud · 9 Identity · 10 Endpoint | **Domain packs** carry the specificity. Read-only, non-intrusive |
| `SF-A1-OTA` | OT/ICS Security Assessment | 6 OT Security | Safety-gated, passive default, engineer-accompanied |
| `SF-A1-SOA` | Security Operations & Detection Assessment | 19 SecOps/SIEM/SOC | Includes detection-coverage testing against ATT&CK *(assumption — §5)* |
| `SF-A1-IRA` | Incident Readiness Assessment & Exercise | 17 Ransomware (readiness half) | Modes: readiness assessment · tabletop exercise · playbook development |

### A2 — Authorised Technical Testing (7)

| ID | Engagement type | Public services covered | Notes |
|---|---|---|---|
| `SF-A2-IPT` | Infrastructure Penetration Test | 3 VAPT · 4 Network | Modes: external · internal · wireless · **non-exploitative VA** |
| `SF-A2-WAT` | Web Application & API Security Test | 5 App Security | Variants: web · API (REST/GraphQL/SOAP) |
| `SF-A2-MAT` | Mobile Application Security Test | 7 Mobile App Security | Variants: iOS · Android |
| `SF-A2-CPT` | Cloud Penetration Test | 8 Cloud Security | Provider-policy check is a blocking gate condition |
| `SF-A2-ATP` | Identity & Attack Path Assessment | 9 Identity/AD | Active path validation, standard user → domain admin |
| `SF-A2-RED` | Red Team & Adversary Simulation | 20 Red Teaming | Modes: full red team · purple team · assumed breach |
| `SF-A2-SES` | Social Engineering Simulation | 20 Red Teaming | Phishing, vishing, physical. Separate legal/HR approval |

### A3 — Investigation & Response (5)

| ID | Engagement type | Public services covered | Notes |
|---|---|---|---|
| `SF-A3-IRE` | Incident Response | 13 DFIR · 14 IR · 17 Ransomware (reactive half) | **Incident-type modules:** ransomware · BEC · data theft · insider · web compromise · unknown |
| `SF-A3-DFE` | Digital Forensic Examination | 11 Digital Forensics | Variants: internal/HR · independent review · litigation support |
| `SF-A3-SPY` | Mobile Device Spyware Examination | 12 Mobile Spyware | **Individual clients supported.** Safety handling from first contact |
| `SF-A3-CTH` | Compromise Assessment & Threat Hunt | 15 Compromise Assessment | Runs one-off or on a recurring schedule |
| `SF-A3-MAL` | Malware Analysis | 16 Malware Analysis | Usually a **child engagement** inheriting parent authority and custody |

### A4 — Continuous & Readiness (2)

| ID | Engagement type | Public services covered | Notes |
|---|---|---|---|
| `SF-A4-ASM` | Attack Surface & Threat Intelligence Monitoring | 18 Threat Intelligence | Recurring cycles; alert-driven escalation |
| `SF-A4-VCI` | vCISO Retainer | 21 Compliance/GRC (vCISO half) | Periodic board reporting; no closure while the contract runs |

**20 engagement types. All 21 public services covered. No service is dropped.**

### Service → engagement type map

| # | Public service *(`SITE-DERIVED`)* | Primary type | Also |
|---|---|---|---|
| 1 | Cybersecurity Consulting & Advisory | `SF-A1-SPA` | `SF-A4-VCI` |
| 2 | Cybersecurity Audits & Security Reviews | `SF-A1-SPA` | `SF-A1-CRA` |
| 3 | Vulnerability Assessment & Penetration Testing | `SF-A2-IPT` | `SF-A2-WAT`, `SF-A2-MAT`, `SF-A2-CPT` |
| 4 | Network Security Assessment & Testing | `SF-A2-IPT` | `SF-A1-TCR` (network pack) |
| 5 | Web Application & API Security Testing | `SF-A2-WAT` | |
| 6 | OT Security Maturity Assessment | `SF-A1-OTA` | |
| 7 | Mobile Application Security Testing | `SF-A2-MAT` | |
| 8 | Cloud Security Assessment & Testing | `SF-A1-TCR` (cloud pack) | `SF-A2-CPT` |
| 9 | Active Directory & Identity Security | `SF-A1-TCR` (identity pack) | `SF-A2-ATP` |
| 10 | Endpoint Security Assessment & Hardening | `SF-A1-TCR` (endpoint pack) | |
| 11 | Digital Forensics & Cyber Investigations | `SF-A3-DFE` | |
| 12 | Mobile Phone Spyware Detection | `SF-A3-SPY` | |
| 13 | Digital Forensics & Incident Response | `SF-A3-IRE` | `SF-A3-DFE` |
| 14 | Incident Response & Breach Investigation | `SF-A3-IRE` | |
| 15 | Compromise Assessment & Threat Hunting | `SF-A3-CTH` | |
| 16 | Malware Analysis & Reverse Engineering | `SF-A3-MAL` | |
| 17 | Ransomware Investigation & Readiness | `SF-A3-IRE` (ransomware module) | `SF-A1-IRA` |
| 18 | Threat Intelligence & Attack-Surface Monitoring | `SF-A4-ASM` | |
| 19 | SIEM / SOC Consulting | `SF-A1-SOA` | |
| 20 | Red Teaming & Adversary Simulation | `SF-A2-RED` | `SF-A2-SES` |
| 21 | Cybersecurity Compliance, GRC & vCISO | `SF-A1-CRA` | `SF-A4-VCI`, `SF-A1-SPA` |

> **Needs Sleuth Confirmation.** Which of these 20 Sleuth actually sells today, which are aspirational,
> and rough annual volume for each. This does not block the design — it sets the *order* in which
> runbooks get authored and validated, which is the real critical path.

---

## 3. Archetype revalidation

The four archetypes were inferred from marketing copy. I said the real catalogue would be the first
proper test of whether they hold. Re-tested against the 20 above:

| Archetype | Types | Holds? |
|---|---|---|
| A1 Assessment & Advisory | 6 | ✔ Yes |
| A2 Authorised Technical Testing | 7 | ✔ Yes |
| A3 Investigation & Response | 5 | ✔ Yes |
| A4 Continuous & Readiness | 2 | ✔ Yes, though thin |

### The one case that argued for a fifth: Red Team

Red teaming differs from a penetration test in real ways — the blue team is deliberately not told,
deconfliction contacts exist for when something goes wrong, detection is tracked as a *finding in
itself*, and the deliverable is a narrative of an attack rather than a register of vulnerabilities.

**Decision: it stays in A2, with a mandatory Adversary Simulation module.**

Reasoning: an archetype governs **authorisation posture, evidence semantics and closure
obligations**. On all three, red teaming is identical to a penetration test — Letter of
Authorisation, Rules of Engagement, testing window, artefact cleanup, retention of proof. What
differs is *execution style* and *deliverable shape*, and modules exist precisely for that. Creating
a fifth archetype would duplicate the entire A2 gate set to accommodate differences that modules
already handle cleanly.

### The case that nearly argued for merging: A4

Only two engagement types, and both could arguably be modelled as repeating A1 engagements.

**Decision: A4 stays.** The distinguishing property is that **there is no closure** — the contract
continues, so evidence disposition and lessons-learned never fire, and authorisation must be
periodically *renewed* rather than granted once. Modelling those as A1 engagements would mean either
a standing authorisation nobody ever revisits, or a closure gate that never passes. Both are wrong in
ways that matter.

**Conclusion: four archetypes hold. No change.**

---

## 4. Modes, packs and modules

Three mechanisms keep 20 types from becoming 40.

**Modes** — a switch chosen at scoping that changes scope and intensity but not the process.
`SF-A2-IPT` external vs internal: same procedures, different targets and different pre-test checks.

**Domain packs** — for `SF-A1-TCR`, the control set being reviewed: Cloud (AWS/Azure/GCP), Identity
(Active Directory / Entra ID), Endpoint, Network. The pack carries the benchmark, the config
extraction method, the review checklist and the finding categories. The runbook carries the process.

**Incident-type modules** — for `SF-A3-IRE`: ransomware, business email compromise, data theft,
insider, web/application compromise, or unknown-at-intake. Selected during triage, changeable as
understanding improves, and **the platform records when it changed and why** — which matters, because
the early hypothesis in an incident is often wrong.

> **Assumption.** That `SF-A3-IRE` should be one runbook with incident-type modules rather than
> separate runbooks per incident type. This follows standard incident-handling practice (NIST SP
> 800-61 structures response as one process regardless of incident type). **Needs SME Validation.**

---

## 5. Assumptions in this catalogue

Every one is my judgement, not a fact about Sleuth.

| # | Assumption | Plain-English | If wrong |
|---|---|---|---|
| AS-01 | 20 engagement types is the right granularity | Enough detail to be useful, few enough to actually write and maintain | Split or merge specific types. The architecture absorbs this cheaply |
| AS-02 | Config review and penetration testing are different engagement types | "Look at the settings" and "try to break in" need different permissions and different paperwork | Merge, with an intrusiveness switch |
| AS-03 | One Incident Response runbook with incident-type modules | Responders follow one process; ransomware just adds extra steps | Separate runbooks per incident type — costly but possible |
| AS-04 | Ransomware Investigation is sold by name but runs as IR + ransomware module | The invoice says ransomware; the process is incident response | Make it a standalone type |
| AS-05 | Social engineering is separate from red team | Targeting people needs HR and legal approval that targeting servers does not | Fold into red team with a people-targeting module |
| AS-06 | Wireless folds into Infrastructure Penetration Test | Low volume, same paperwork, different kit | Separate type |
| AS-07 | Non-exploitative vulnerability assessment is a *mode* of IPT, not a type | Same job, told to stop earlier | Separate type — it is a common recurring product |
| AS-08 | Malware Analysis is usually a child engagement | It normally arises inside an investigation, not as a standalone sale | Standalone-first, with child as the exception |
| AS-09 | Detection-coverage testing belongs in `SF-A1-SOA` | Assessing a SOC properly means testing whether it detects things, not just reading its config | Split into an assessment type and a separate validation type |
| AS-10 | Four archetypes hold | The four workflow shapes cover everything Sleuth does | A fifth archetype; the module system absorbs most alternatives |

> **Needs Sleuth Confirmation (does not block design work):**
> which types are live vs aspirational · annual volume per type · whether retest is standard across
> all A2 types or only where the website promises it · whether Sleuth accepts individual (non-company)
> clients beyond spyware examinations · whether Sleuth takes emergency incident work from
> non-clients · whether physical security testing is offered *(the site says "where applicable")*.

---

## 6. What this changes downstream

| Document | Change |
|---|---|
| `01-service-catalogue.md` | **Superseded by this document.** Retained for the research trail and the four-test derivation |
| `22-core-spine-specification.md` | New — the ~60 procedures every one of the 20 types inherits |
| `23-archetype-modules.md` | New — A1–A4 execution modules |
| `24`–`27` | New — a populated Engagement Type Specification for all 20 |
| `28-checklist-and-gate-architecture.md` | New — checklists and gates specified properly |
| `29-architecture-amendments.md` | Deltas to findings, reporting, roles, data model, navigation, UX and exports |
| `16-implementation-plan.md` | First vertical slice re-recommended — see `29` §9 |
