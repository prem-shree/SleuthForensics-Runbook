# 25 — Engagement Type Specifications: A2 Authorised Technical Testing

> **Status — Draft / Needs SME Validation.** Provenance: `PROPOSED` (structure), `INDUSTRY-PRACTICE`
> and `EXTERNAL-STANDARD` (method), `SITE-SUGGESTED` (scope items from service pages).
> Nothing is `SLEUTH-SUPPLIED` or validated.

**§1 derived** from `core.*` (`22`) + `arch.A2` (`23`). Only deltas and service-specific content below.

> **Every A2 engagement inherits the same non-negotiables:** Letter of Authorisation, Rules of
> Engagement, agreed testing window, independent asset-ownership verification, artefact cleanup with
> verification, and the six A2 stop conditions. None of that is restated per type — it is inherited,
> and improving it improves all seven at once.

---

# `SF-A2-IPT` — Infrastructure Penetration Test

**Public services:** 3 VAPT · 4 Network · **Archetype:** A2
**Modes:** external · internal · wireless · **non-exploitative VA** *(assumption AS-07)*

### §2 Service-specific procedures `[SERVICE]`

| ID | Procedure | Injects at | Records |
|---|---|---|---|
| `IPT-01` | Scope & ownership confirmation — every IP, CIDR and hostname independently verified | `A2-02` | Per-asset verification, method |
| `IPT-02` | Passive reconnaissance — public sources only, no contact with targets | `⟪service_recon⟫` | Sources, findings |
| `IPT-03` | Host discovery & port scanning | `⟪service_enum⟫` | Live hosts, open ports, method |
| `IPT-04` | Service enumeration & version identification | `⟪service_enum⟫` | Services, versions, banners |
| `IPT-05` | Vulnerability identification — automated and manual | `⟪service_vulnid⟫` | Candidates, source, tool + version |
| `IPT-06` | Configuration and patch-level assessment | `⟪service_vulnid⟫` | Deviations, missing patches |
| `IPT-07` | Manual validation of candidates | `A2-08` | Confirmed / discounted with reasoning |
| `IPT-08` | Controlled exploitation to proof of access ✋ | `A2-09` | Action, authority, evidence |
| `IPT-09` | Lateral movement assessment *(internal mode)* — segmentation reality vs design | `A2-10` | Paths found, boundaries respected |
| `IPT-10` | Wireless assessment *(wireless mode)* — encryption, authentication, rogue/evil-twin exposure, guest isolation | `⟪service_enum⟫` | SSIDs, findings, physical boundary respected |

**Mode differences**

| Mode | Differs by |
|---|---|
| External | Internet-facing only. No client network access. Source IPs may be allow-listed or blind |
| Internal | Requires network access and a position. Adds `IPT-09`. Usually assumed-breach positioning |
| Wireless | Adds `IPT-10`. **Physical site access required; scope has a geographic boundary** — testing a neighbouring tenant's network is a serious breach |
| Non-exploitative VA | Stops at `IPT-06`. No `IPT-07`–`IPT-09`. Lighter RoE, still requires a Letter of Authorisation |

### §3 Client information `[SERVICE]`
IP ranges in CIDR · domains and subdomains · **whether enumeration may expand scope or scope is
fixed** · cloud-hosted assets and provider · shared hosting · CDN/WAF in front and whether it will
be tuned · legacy or unsupported systems in scope · systems with known stability problems · maintenance
windows to avoid · monitoring that will alarm and who is informed · **DoS testing permitted (default
no)** · source IP allow-listing or blind testing · for internal/wireless: site access and escort.

### §4 Documents `[CORE]` + `[ARCH:A2]`
Letter of Authorisation · Rules of Engagement · signed asset schedule. **Testers carry a retrievable
copy of the LoA on site** *(internal/wireless modes)*.

### §6 Preconditions `[SERVICE]`
Ownership verified for every asset · third-party authorisation complete or assets removed ·
window agreed with timezone · client on-call contact confirmed reachable · test accounts verified
*(authenticated scope)* · site access arranged *(internal/wireless)*.

### §9 Evidence `[ARCH:A2]` + `[SERVICE]`
Tool output with version · scan logs · request/response pairs for each confirmed finding · screenshots
of proof of access · command logs with timestamps. **Retained so a disputed finding can be reproduced.**

### §10 Decisions
Intrusiveness ceiling per asset · whether a discovered asset is in scope *(default: no)* · whether to
exploit or stop at identification · production vs non-production handling.

### §14 Deliverables
Findings with exploitation evidence and proof-of-concept · risk-rated vulnerabilities with business
impact · prioritised remediation · executive summary · **retest support** *(all `SITE-DERIVED`)*.

### §15 Retest
**In scope by default** — the website promises it for VAPT. Retest only remediated findings; new
findings discovered during retest are reported but flagged as out of the original scope.

**`[GAP]` intrusiveness ceiling — ✓ **CLOSED 2026-09-21**.** Default **Level 2 Validate safely**; Level 3 available with
RoE authorisation; VA mode is Level 1 (`32` §1).
**`[GAP]` non-blocking:** wireless physical-boundary procedure.

---

# `SF-A2-WAT` — Web Application & API Security Test

**Public service:** 5 App Security · **Archetype:** A2 · **Variants:** web · API

### §2 Service-specific procedures `[SERVICE]`

| ID | Procedure | Records |
|---|---|---|
| `WAT-01` | Application mapping & functionality inventory | Endpoints, functions, roles |
| `WAT-02` | Authentication testing — credential handling, MFA, recovery, lockout | Findings, evidence |
| `WAT-03` | Session management testing — token handling, fixation, expiry, invalidation | Findings |
| `WAT-04` | **Authorisation & access control matrix testing** — every role against every function | Role/function matrix with results |
| `WAT-05` | Input validation & injection testing | Findings with PoC |
| `WAT-06` | Cross-site scripting & content injection | Findings with PoC |
| `WAT-07` | **Business logic testing** — the part tools cannot do | Logic flaws, reasoning |
| `WAT-08` | API-specific testing — REST, GraphQL, SOAP *(`SITE-DERIVED`)* | Per-style findings |
| `WAT-09` | File upload & data handling | Findings |
| `WAT-10` | SSRF and server-side request testing | Findings |
| `WAT-11` | Security headers & transport security | Configuration findings |

`WAT-04` deserves emphasis: broken access control is consistently the most impactful web finding, and
it is only found by systematically testing each role against each function. It is tedious, it is
manual, and it is where the value is.

### §3 Client information `[SERVICE]`
Application inventory and business criticality · technology stack · authentication model (SSO/MFA/social) ·
**role matrix and a test account per role (blocking)** · API style and documentation availability ·
multi-tenancy model · payment and personal-data flows · rate limiting · **staging environment fidelity
to production** · WAF present and whether it will be tuned.

### §6 Preconditions `[SERVICE]`
Test accounts for **every** role, verified working · environment confirmed (staging or production,
explicitly) · API documentation or collection supplied · WAF handling agreed.

### §11 Stops `[SERVICE]`
⊗ Real customer personal data encountered in a non-production environment — stop, do not copy, ▲.
⊗ A test action causes data corruption — stop, notify immediately, preserve the request.

### §14 Deliverables
Vulnerability report with evidence and **reproduction steps** · risk ratings with business impact ·
**developer-friendly remediation guidance** · executive summary · retest support *(`SITE-DERIVED`)*.

### §15 Retest In scope by default — promised on the site.

**`[GAP]` testing standard and depth — ✓ **CLOSED 2026-09-21**:** **OWASP WSTG** for coverage, **ASVS Level 2** as
default depth (`32` §9). Intrusiveness **Level 2**.

---

# `SF-A2-MAT` — Mobile Application Security Test

**Public service:** 7 Mobile App Security · **Archetype:** A2 · **Variants:** iOS · Android

### §2 Service-specific procedures `[SERVICE]`

| ID | Procedure | Records |
|---|---|---|
| `MAT-01` | Build acquisition & integrity verification | Build ref, version, hash, source |
| `MAT-02` | Static analysis — binary, resources, embedded secrets | Findings, tool + version |
| `MAT-03` | Local data storage & caching review | Storage locations, sensitive data found |
| `MAT-04` | Network communication & certificate validation testing | Transport findings, pinning behaviour |
| `MAT-05` | Authentication & session management testing | Findings |
| `MAT-06` | Cryptographic implementation review | Algorithms, key handling, findings |
| `MAT-07` | Binary protections & obfuscation assessment | Protections present, bypass difficulty |
| `MAT-08` | Sensitive data exposure in logs and memory | Findings with evidence |
| `MAT-09` | Inter-process communication security | Exported components, findings |
| `MAT-10` | Backend API testing from the mobile client perspective | Findings *(may hand off to `SF-A2-WAT`)* |

### §3 Client information `[SERVICE]`
Platforms and minimum OS versions · distribution (store / enterprise / MDM) · **build availability
(IPA/APK) and whether source is provided** · backend test environment · test devices — physical or
emulator, and who supplies them · jailbreak/root detection present · certificate pinning present ·
offline functionality · SDK and third-party library inventory.

### §6 Preconditions `[SERVICE]`
Testable build supplied · backend environment reachable and confirmed non-production, or production
explicitly authorised · **test devices available — jailbroken/rooted where required, and that
requirement agreed in advance**.

### §14 Deliverables
Platform-specific findings · risk ratings aligned with **industry mobile security standards** ·
per-platform developer remediation guidance · executive summary *(`SITE-DERIVED`)*.

**`[GAP]` mobile standard — ✓ **CLOSED 2026-09-21**: OWASP MASVS** (`32` §9). Intrusiveness **Level 2**.
*(Worth reconciling the website's unnamed "industry mobile security standards" with this.)*

---

# `SF-A2-CPT` — Cloud Penetration Test

**Public service:** 8 Cloud Security · **Archetype:** A2

### §2 Service-specific procedures `[SERVICE]`

| ID | Procedure | Records |
|---|---|---|
| `CPT-01` | **Provider policy check (blocking)** — confirm the test is permitted under the provider's terms, and notify where required | Policy checked, permission basis, notification |
| `CPT-02` | Account and subscription inventory validation | Accounts, subscriptions, projects in scope |
| `CPT-03` | Identity and access exploitation — privilege escalation paths through IAM | Paths found, evidence |
| `CPT-04` | Public exposure validation — confirm what is genuinely reachable | Exposed resources, confirmed reachability |
| `CPT-05` | Storage and data access testing | Findings |
| `CPT-06` | Network and segmentation testing within the cloud estate | Findings |
| `CPT-07` | Serverless and container testing | Findings |
| `CPT-08` | Secrets exposure assessment — in code, images, metadata, environment | Findings *(handled per Rule 4 — see below)* |
| `CPT-09` | Lateral movement between accounts, subscriptions or tenancies | Paths, boundaries respected |

> **Rule 4 and `CPT-08`.** Where testing discovers an exposed client secret, the platform records
> **that a secret of a given type was exposed, where, and how it was discovered — never its value**.
> The finding is evidenced by a redacted capture. The client is notified immediately to rotate it.

### §3 Client information `[SERVICE]`
Providers and account/subscription/project inventory · landing zone or organic growth · IaC in use ·
multi-tenancy model · **data residency requirements** · production vs non-production per account ·
existing CSPM tooling · shared-responsibility boundary understanding.

### §5 Authorisation `[CORE]` + `[ARCH:A2]` + `[SERVICE]`
⊗ **Provider policy check is a blocking Authorisation Gate condition.** The client cannot authorise
testing that breaches their provider's terms.

### §14 Deliverables
Findings with exploitation evidence · public exposure register · IAM path analysis · prioritised
remediation with implementation steps · architecture recommendations *(`SITE-DERIVED`)*.

**`[GAP]` non-blocking:** per-provider policy and notification process — changes over time, so it
should be a maintained reference rather than runbook text.

---

# `SF-A2-ATP` — Identity & Attack Path Assessment

**Public service:** 9 Identity/AD · **Archetype:** A2

### §2 Service-specific procedures `[SERVICE]`

| ID | Procedure | Records |
|---|---|---|
| `ATP-01` | Domain and forest enumeration from an authenticated position | Structure, trusts, delegation |
| `ATP-02` | Privileged account and Tier 0 exposure analysis | Privileged inventory, exposure |
| `ATP-03` | **Attack path analysis — standard user to domain admin** *(`SITE-DERIVED`)* | Paths with each hop evidenced |
| `ATP-04` | Kerberos abuse path validation | Findings with evidence |
| `ATP-05` | Delegation and trust abuse validation | Findings |
| `ATP-06` | Service account and SPN exposure assessment | Findings |
| `ATP-07` | Credential hygiene assessment | Findings *(no credential values recorded — Rule 4)* |
| `ATP-08` | Path validation — **confirm each path works, do not report theoretical paths** ✋ | Per-path: validated / theoretical, evidence |

`ATP-08` matters because attack-path tools generate large numbers of theoretical paths, many of which
do not work in practice. Reporting unvalidated paths inflates severity and wastes the client's
remediation effort on routes nobody could take.

### §3 Client information `[SERVICE]`
Forest/domain/OU structure · user and privileged account counts · Entra ID or hybrid identity ·
trust relationships and to whom · Tier model in place · PAM solution present · service account
inventory and rotation practice · prior credential incidents · domain admin count · **a standard
user account for the starting position (blocking)**.

### §11 Stops `[SERVICE]`
⊗ A path reaches a domain or forest outside the approved scope — stop before traversing it. Trust
relationships routinely lead somewhere the client did not think to mention.

### §14 Deliverables
Attack paths with evidence · **privilege escalation analysis with visual path mapping** ·
configuration hardening recommendations · prioritised roadmap *(`SITE-DERIVED`)*.

**`[GAP]` path validation depth — ✓ **CLOSED 2026-09-21**.** Default **Level 2**; **validation of a path to domain admin
is Level 3 and requires explicit RoE authorisation naming that ceiling** — because proving the path
means becoming domain admin (`32` §1).

---

# `SF-A2-RED` — Red Team & Adversary Simulation

**Public service:** 20 Red Teaming · **Archetype:** A2 + mandatory Adversary Simulation module
**Modes:** full red team · purple team · assumed breach

### §2 Service-specific procedures `[SERVICE]`

| ID | Procedure | Records |
|---|---|---|
| `RED-01` | Objective definition — the "flags", agreed with leadership | Objectives, success criteria |
| `RED-02` | **Deconfliction procedure establishment (blocking)** — named contacts, 24/7, and a code word | Contacts, procedure, tested |
| `RED-03` | Threat actor profile selection — which adversary is being simulated and why | Profile, TTP set, rationale |
| `RED-04` | Initial access attempt | Method, success/failure, evidence |
| `RED-05` | Establish foothold and persistence ✋ | Mechanisms used, **inventoried for cleanup** |
| `RED-06` | Privilege escalation and lateral movement | Path, evidence |
| `RED-07` | Objective pursuit | Progress per objective |
| `RED-08` | **Detection tracking — what was detected, when, by what, and what was missed** | Detection timeline against the action timeline |
| `RED-09` | Purple team collaboration *(purple mode)* — work alongside the blue team, improving live | Joint findings, improvements made |
| `RED-10` | **Full artefact inventory and removal verification** — extends `A2-13` | Every implant, account, file, rule; removal verified individually |
| `RED-11` | Technical debrief and knowledge transfer *(`SITE-DERIVED`)* | Attendees, content |

### §3 Client information `[SERVICE]`
Defined objectives · assumed starting position · **blue team awareness (usually no)** ·
**deconfliction contacts and procedure (blocking)** · permitted TTPs and explicit prohibitions ·
social engineering permitted and pretext approval process · physical permitted and site details ·
duration · **legal sign-off where people are targeted (blocking)** · evidence of authorisation
testers must carry on site · what triggers an immediate stop.

### §5 Authorisation `[SERVICE]`
✋ Leadership-level authorisation, not IT-level — the blue team is deliberately uninformed.
✋ A **carry letter** testers hold physically, with a 24/7 verification number, wherever physical
access is in scope.

### §11 Stops `[SERVICE]`
⊗ Deconfliction is invoked by either side.
⊗ A real incident is triggered and the blue team is expending genuine resource — deconflict immediately.
⊗ An action would affect a production system beyond what the RoE permits.
⊗ A real compromise by a genuine third party is discovered — **stop, escalate, do not touch**.

### §14 Deliverables
Attack narrative · **detection gap analysis showing what was and was not detected** · detection and
response improvement recommendations · technical debrief · executive summary *(`SITE-DERIVED`)*.

### §16 Closure `[SERVICE]`
`RED-10` is a Closure Gate condition with **individual verification per artefact**. A forgotten red
team implant is a genuine and recurring industry failure.

**`[GAP]` permitted techniques — ✓ **CLOSED 2026-09-21** in principle; baseline drafted at `32` §5 and awaiting a named
owner's sign-off.** Intrusiveness **Level 3, mandatory**. Persistence requires explicit per-engagement
approval and every mechanism is inventoried at deployment for individually verified removal.

---

# `SF-A2-SES` — Social Engineering Simulation

**Public service:** 20 Red Teaming *(social engineering element)* · **Archetype:** A2 + mandatory
People-Targeting context module

> **People are the target here.** That changes the approvals, the handling and the reporting.

### §2 Service-specific procedures `[SERVICE]`

| ID | Procedure | Records |
|---|---|---|
| `SES-01` | **Legal and HR approval (blocking)** — separate from technical authorisation | Approvals, approvers, date |
| `SES-02` | Pretext development and approval ✋ | Pretext, approved by |
| `SES-03` | Target population definition — **roles or groups, with exclusions** | Population, exclusions with reasons |
| `SES-04` | Campaign infrastructure preparation | Domains, infrastructure, inventoried for cleanup |
| `SES-05` | Campaign execution | Timing, volumes, delivery confirmation |
| `SES-06` | Interaction recording — **aggregate metrics only** | Click/submit/report rates by group |
| `SES-07` | Detection and reporting-rate measurement — **who reported it is a positive finding** | Report rate, time to first report |
| `SES-08` | Infrastructure teardown and verification | Removal verified |
| `SES-09` | Awareness debrief | Content, delivery method |

### §5 Authorisation `[SERVICE]` — the strictest in the catalogue
✋ Legal approval · ✋ HR approval · ✋ leadership authorisation · **exclusions honoured** (individuals
in sensitive circumstances, on leave, or in protected roles).

### §11 Stops `[SERVICE]`
⊗ A target experiences genuine distress — stop that thread, notify HR.
⊗ A pretext is causing real operational disruption.
⊗ Credentials are actually captured in a way not covered by the RoE — **the default rule is that
credentials are never captured or stored; only the fact of submission is recorded** *(Rule 4)*.

### §14 Deliverables
**Aggregate results only — no individual is ever named.** Detection and reporting rates · pretext
effectiveness · process gaps · awareness recommendations.

> This is a firm rule, not a preference. A simulation that produces a list of individuals who failed
> is a disciplinary instrument, not a security assessment, and it destroys the trust the exercise
> depends on. **If a client requests named results, that is a scoping conversation before the
> engagement, never a reporting decision afterwards. Recommended position: decline.**
> **Needs Sleuth Confirmation.**

**`[GAP]` credential capture and individual naming — ✓ **CLOSED 2026-09-21**: no to both** (`32` §4). Credentials are
never captured or stored — only the fact of submission. Reporting is aggregate; no individual is
ever named, for any client, at any severity.
