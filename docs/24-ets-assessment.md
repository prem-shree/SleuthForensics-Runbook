# 24 — Engagement Type Specifications: A1 Assessment & Advisory

> **Status — Draft / Needs SME Validation.** Provenance: `PROPOSED` (structure), `INDUSTRY-PRACTICE`
> (method), `SITE-SUGGESTED` (scope items drawn from service pages — candidates for SME review, not
> internal SOP). Nothing here is `SLEUTH-SUPPLIED` or validated.

Schema per `19-engagement-type-specification.md`. **§1 (what is common) is derived, never restated** —
it resolves to `core.*` (`22`) + `arch.A1` (`23`). Only deltas and service-specific content appear below.

---

# `SF-A1-SPA` — Security Programme & Maturity Assessment

**Public services:** 1 Cybersecurity Consulting · 2 Security Audits · **Archetype:** A1
**Modes:** full programme · targeted domain · M&A transaction review
**Sold as:** fixed-scope project · **Team:** lead consultant + analyst

### §2 Service-specific procedures `[SERVICE]`

| ID | Procedure | Records |
|---|---|---|
| `SPA-01` | Business & risk context establishment — what the organisation does, what would hurt it, what it is trying to achieve | Context statement, sources |
| `SPA-02` | Security function & resourcing review — who owns security, reporting line, headcount, skills | Structure, gaps |
| `SPA-03` | Governance & policy set review — what exists, currency, approval, communication | Policy inventory with status |
| `SPA-04` | Domain-by-domain capability assessment ⟪domain_pack⟫ | Per-domain rating + source citation |
| `SPA-05` | Security architecture review — controls in place and how they fit together | Architecture observations |
| `SPA-06` | Third-party & vendor risk practice review | Practice maturity, inventory coverage |
| `SPA-07` | Security investment review — where money goes vs where risk is | Spend/risk alignment |
| `SPA-08` | Board & executive reporting review | Current reporting, gaps |
| `SPA-09` | Target operating model definition | Target state per domain |
| `SPA-10` | Roadmap & investment sequencing | Sequenced plan, dependencies, effort |

### §3 Client information `[SERVICE]`
Business objectives and horizon · security function structure and headcount · current budget · prior
assessments and closure status · board reporting today · stated risk appetite · planned change
(cloud migration, M&A, new markets) · **what decision this assessment supports**.

### §4–§6 Documents · Authorisation · Preconditions
`[CORE]` no delta. No Letter of Authorisation required — no system is touched.
**Precondition `[SERVICE]`:** named control owners identified and available for interview.

### §7 Phases
`[CORE]` no deviation.

### §9 Evidence `[ARCH:A1]`
Documents received · interview records · observation notes · configuration artefacts where supplied.
Every rating cites one. **Register-only** *(Rule 3)*.

### §10 Decisions
Framework selection *(→ `A1-01`)* · full vs targeted scope · whether unevidenced controls are rated
or gapped **(policy: gapped)**.

### §11–§12 Stops · Escalations
`[ARCH:A1]` no delta.

### §13 QA `[CORE]` + `[ARCH:A1]`
Evidence Sufficiency check is mandatory. No rating without a cited source.

### §14 Deliverables
Maturity scorecard · gap analysis · prioritised roadmap · executive summary · quick wins.
*(`SITE-DERIVED` deliverable language: "maturity scorecard against selected frameworks",
"prioritised improvement roadmap", "executive summary suitable for leadership and board reporting")*

### §15 Retest
Not applicable. Re-assessment is a new engagement — typically annual. **Needs Sleuth Confirmation**
whether a lighter "progress review" product should exist.

### §16 Closure `[CORE]` no delta.

**`[GAP]` maturity scale — ✓ **CLOSED 2026-09-21**** (`32` §9). **`[GAP]` non-blocking:** the domain set for `SPA-04`.

---

# `SF-A1-CRA` — Compliance Readiness Assessment

**Public services:** 21 Compliance/GRC · 2 Audits (pre-certification) · **Archetype:** A1
**Framework packs:** ISO 27001 · SOC 2 · NIST CSF *(the three named on the site)*

### §2 Service-specific procedures `[SERVICE]`

| ID | Procedure | Records |
|---|---|---|
| `CRA-01` | Framework & applicability determination — which framework, which version, what is in scope | Framework, scope of applicability |
| `CRA-02` | Control applicability statement — which controls apply and which are excluded, **with justification** | Applicability statement, exclusions |
| `CRA-03` | Evidence-for-certification mapping — **what the auditor will actually ask for**, per control | Evidence map, availability status |
| `CRA-04` | Control-by-control gap analysis | Per-control: conformant / partial / non-conformant, with evidence |
| `CRA-05` | Policy & documentation gap analysis | Required vs existing documents |
| `CRA-06` | Risk assessment & register review or build | Risk register, methodology |
| `CRA-07` | Vendor & third-party register review | Inventory coverage, tiering |
| `CRA-08` | Internal audit readiness check | Readiness rating |
| `CRA-09` | Remediation roadmap to the certification date | Sequenced plan against the deadline |
| `CRA-10` | Audit preparation pack | Evidence index, owner map |

### §3 Client information `[SERVICE]`
Target framework and version · **certification deadline and what drives it** · current certification
state · auditor engaged and who · policy set maturity · risk register existence and format · risk
appetite statement · vendor inventory · in-scope entities, systems and locations.

### §4 Documents
`[CORE]` + `[SERVICE]` applicability statement (client-owned, Sleuth-assisted).

### §5–§7 `[CORE]` no delta.

### §9 Evidence `[ARCH:A1]` — with one addition: `CRA-03` records evidence *availability*, distinct
from evidence *sufficiency*. A control can be well implemented and still fail an audit for want of
demonstrable evidence, and clients are routinely surprised by this.

### §10 Decisions
Conformant vs partial vs non-conformant per control · whether an exclusion is defensible · whether
the certification date is achievable **(if not, say so early — this is the finding clients most need
and least want)**.

### §14 Deliverables
Gap analysis · applicability statement · risk register · policy gap list · roadmap to certification ·
audit preparation pack · board summary.

### §15 Retest
Pre-audit verification review. **Needs Sleuth Confirmation** whether this is included or sold separately.

**`[GAP]` non-blocking:** framework pack content per framework — substantial authoring, one pack at a time.

---

# `SF-A1-TCR` — Technical Configuration Review

**Public services:** 4 Network · 8 Cloud · 9 Identity · 10 Endpoint · **Archetype:** A1
**Domain packs:** Cloud · Identity/AD · Endpoint · Network — **one engagement may run several**

### §2 Service-specific procedures `[SERVICE]`

| ID | Procedure | Records |
|---|---|---|
| `TCR-01` | Read-only access establishment & verification — **access must be genuinely read-only** | Access method, permissions granted, verified by |
| `TCR-02` | Configuration extraction ⟪domain_pack⟫ | Extraction method, tool + version, timestamp, completeness |
| `TCR-03` | Benchmark selection & deviation analysis | Benchmark, version, deviations found |
| `TCR-04` | Manual review of high-risk settings — benchmarks miss context | Settings reviewed, judgement applied |
| `TCR-05` | **Exception validation** — is a deviation deliberate, understood and compensated? | Per-deviation: defect vs accepted risk, basis |
| `TCR-06` | Finding drafting with implementation guidance | Findings with specific remediation steps |

`TCR-05` is what separates a configuration review from a scanner report. A deviation the client made
knowingly, with a compensating control, is not a finding — and reporting it as one erodes trust in
everything else in the report.

### Domain pack scope *(all `SITE-SUGGESTED` — candidate scope items awaiting SME confirmation)*

| Pack | Candidate scope |
|---|---|
| **Cloud** | IAM · storage and database access · network security groups and VPC · encryption at rest and in transit · logging, monitoring and alerting · serverless and container · secrets management · resource exposure and public accessibility |
| **Identity/AD** | forest and domain configuration · trusts and delegation · GPO and security settings · privileged accounts and Tier 0 exposure · Kerberos configuration · password policy and credential hygiene · service accounts and SPNs |
| **Endpoint** | OS hardening · patch management · EPP/EDR deployment and configuration · local administrator management · application control · USB and removable media · browser and email client settings · endpoint logging |
| **Network** | architecture and topology · firewall rules and ACLs · segmentation and VLANs · VPN and remote access · wireless · DNS/DHCP and core services · internal and external exposure · device hardening and management interfaces |

### §3 Client information `[SERVICE]`
Per pack: inventory and scale · platform and versions · management tooling · existing baseline and
its source · **read-only assessment access availability (blocking)** · known accepted deviations.

### §5 Authorisation `[CORE]` + `[SERVICE]`
No Letter of Authorisation — read-only, non-intrusive. **⊗ If the work would require any active
testing, it is out of scope and becomes an A2 engagement.** This boundary must be explicit at
scoping, because it is where scope creep most often becomes an authorisation breach.

### §6 Preconditions `[SERVICE]`
Read-only access provisioned and **verified working** · extraction method agreed · a client technical
contact available during extraction.

### §9 Evidence
Configuration exports · extraction logs · screenshots. Hashed at capture. **Register-only.**

### §11 Stops `[SERVICE]`
⊗ Access granted exceeds read-only — stop, report, have it corrected before proceeding.
⊗ Extraction would affect system availability.

### §14 Deliverables
Configuration findings report · benchmark comparison · prioritised remediation with implementation
steps · architecture recommendations *(`SITE-DERIVED` language)*.

### §15 Retest
Re-extraction and comparison after remediation. **Recommended as standard** — it is cheap and the
client values it. **Needs Sleuth Confirmation.**

**`[GAP]` benchmark source — ✓ **CLOSED 2026-09-21**:** **CIS Benchmarks** baseline, vendor guidance where CIS has no
coverage (`32` §9). **Now authoring work rather than a decision** — each pack's control set and
extraction method still needs writing and SME validation. **This remains the single largest authoring
item in A1.**

---

# `SF-A1-OTA` — OT/ICS Security Assessment

**Public service:** 6 OT Security · **Archetype:** A1 + mandatory OT/Safety context module

> **Safety governs everything here.** These environments control physical processes. An assessment
> that disrupts one can hurt someone.

### §2 Service-specific procedures `[SERVICE]`

| ID | Procedure | Records |
|---|---|---|
| `OTA-01` | **Safety briefing & engineer pairing (blocking)** — site induction; a client engineer accompanies all OT work | Briefing completed, engineer named, per-person acknowledgement |
| `OTA-02` | Site walkdown & physical integration review | Observations, physical/logical boundaries |
| `OTA-03` | Asset inventory review & validation — inventories are usually incomplete; that is itself a finding | Inventory coverage, confidence, gaps |
| `OTA-04` | Purdue-level architecture & segmentation review | Level mapping, segmentation reality vs design |
| `OTA-05` | IT/OT convergence point mapping | Every interconnect, its controls |
| `OTA-06` | Remote & vendor access governance review | Access paths, controls, monitoring |
| `OTA-07` | Patch & vulnerability practice review — **including why patching is constrained** | Practice, constraints, compensating controls |
| `OTA-08` | Monitoring & detection capability review | Coverage, tooling, blind spots |
| `OTA-09` | OT incident readiness review | Playbooks, roles, safety interaction |
| `OTA-10` | **Passive network observation — strictly non-intrusive, safety-gated, optional** ✋ | Method, approval, engineer present, duration |
| `OTA-11` | Maturity scoring vs IEC 62443 / NIST SP 800-82 *(both `SITE-DERIVED`)* | Per-domain rating with citation |

### §3 Client information `[SERVICE]`
Sites and processes · OT vendors and system types (SCADA/PLC/DCS/HMI) · asset inventory existence and
confidence · Purdue architecture · IT/OT interconnects · remote vendor access · patching constraints
and safety approval process · **safety-critical processes that must never be interrupted (blocking)** ·
engineer availability · regulatory context · planned maintenance windows.

### §5 Authorisation `[CORE]` + `[SERVICE]`
✋ **Site safety authorisation from the operations/plant authority, separate from IT authorisation.**
IT cannot authorise work on a plant floor.

### §6 Preconditions `[SERVICE]`
Safety induction completed · engineer assigned and available · PPE requirements met · `OTA-10`
separately approved if in scope.

### §11 Stops `[SERVICE]` — all absolute
⊗ Any indication of process disturbance — stop immediately, notify the engineer.
⊗ The accompanying engineer is unavailable — **OT work does not continue unaccompanied.**
⊗ Any activity that would require touching a live control system beyond what was approved.
⊗ A safety concern of any kind — ▲ Management and the client's safety authority.

### §14 Deliverables
Maturity scorecard · gap analysis · risk-prioritised roadmap · **convergence risk assessment** ·
executive summary · OT-specific incident response playbook recommendations *(`SITE-DERIVED`)*.

**`[GAP]` blocking:** the passive-observation method and its safety approval process (`OTA-10`) —
**must not be drafted from general practice; it is site- and vendor-specific.**

---

# `SF-A1-SOA` — Security Operations & Detection Assessment

**Public service:** 19 SecOps/SIEM/SOC · **Archetype:** A1

### §2 Service-specific procedures `[SERVICE]`

| ID | Procedure | Records |
|---|---|---|
| `SOA-01` | SOC model, staffing & shift coverage review | Model, coverage gaps |
| `SOA-02` | Log source coverage — **what is onboarded vs what exists** | Expected vs actual inventory, gaps |
| `SOA-03` | Data quality & parsing validation — an onboarded source that parses badly detects nothing | Per-source quality findings |
| `SOA-04` | Detection rule inventory & coverage mapping to MITRE ATT&CK | Coverage map, gaps by technique |
| `SOA-05` | Alert volume & false-positive analysis | Volume, FP rate, analyst load |
| `SOA-06` | Triage & escalation process review | Process, decision points, handoffs |
| `SOA-07` | **Detection validation testing** — safe atomic tests to verify detections actually fire ✋ *(assumption AS-09)* | Tests run, detected/not, timing |
| `SOA-08` | SIEM architecture & licensing review | Architecture findings, cost implications |
| `SOA-09` | Detection engineering — rule improvements delivered as artefacts | Rules delivered, format |
| `SOA-10` | Maturity scoring | Per-domain rating with citation |

### §5 Authorisation `[SERVICE]`
✋ **`SOA-07` requires a Letter of Authorisation and Rules of Engagement** even though this is an A1
engagement — it executes activity on client systems. **This is the one A1 type that borrows A2's
authorisation posture, and only for that procedure.** If `SOA-07` is out of scope, standard A1
authorisation applies.

> **Assumption AS-09.** That detection validation belongs here. Assessing a SOC by reading its
> configuration tells you what it *should* detect; testing tells you what it *does*. **Needs Sleuth
> Confirmation** — it materially changes the engagement's authorisation requirements.

### §11 Stops `[SERVICE]`
⊗ A validation test causes a real incident response — stop, notify immediately, deconflict.
⊗ Testing reveals an actual compromise *(see A2 stop conditions — same handling)*.

### §14 Deliverables
Maturity scorecard · log source coverage analysis · **detection coverage map against ATT&CK** ·
alert quality analysis · process recommendations · SIEM optimisation recommendations · detection
rule library or improvements *(`SITE-DERIVED`)*.

**Detection validation in scope — ✓ **CLOSED 2026-09-21**** (B7). Note it carries a Letter of Authorisation requirement
into an otherwise non-intrusive engagement. Intrusiveness is L1/L2-equivalent: telemetry without real
impact (`32` §1).
**`[GAP]` remaining, non-blocking:** the atomic test set itself — authoring work for an SME.

---

# `SF-A1-IRA` — Incident Readiness Assessment & Exercise

**Public service:** 17 Ransomware (readiness half) · **Archetype:** A1
**Modes:** readiness assessment · tabletop exercise · playbook development

### §2 Service-specific procedures `[SERVICE]`

| ID | Procedure | Records |
|---|---|---|
| `IRA-01` | Backup architecture & isolation review | Architecture, isolation reality |
| `IRA-02` | **Restore capability assessment — tested vs claimed** | Restore test history, RTO/RPO actual vs target |
| `IRA-03` | Segmentation & blast radius analysis | Likely spread, critical dependencies |
| `IRA-04` | Detection & response coverage review | Coverage for likely attack paths |
| `IRA-05` | Playbook review or development | Playbooks, decision frameworks |
| `IRA-06` | Crisis communication & decision authority review — **who decides, out of hours** | Decision authority map, comms plan |
| `IRA-07` | Exercise scenario design | Scenario, injects, objectives |
| `IRA-08` | Exercise facilitation | Attendees, timeline, decisions taken |
| `IRA-09` | Exercise observation & findings | Observations, gaps revealed |
| `IRA-10` | Improvement plan | Prioritised actions |

`IRA-02` is the procedure that most often changes a client's mind. Almost every organisation believes
it can restore. Far fewer have tested it at the scale and under the conditions a real incident
imposes, and the gap between the two is usually where the real risk sits.

### §3 Client information `[SERVICE]`
Backup architecture and isolation · restore testing history · RTO/RPO targets · segmentation · EDR
coverage · privileged access controls · existing playbook and last exercise date · crisis
communication plan · cyber insurance · critical system dependency mapping · prior incidents.

### §5 Authorisation `[CORE]` no delta — no systems touched. Exercise mode is discussion-based.

### §14 Deliverables
Readiness scorecard · backup and restore assessment · blast radius analysis · playbooks with
**decision frameworks** *(`SITE-DERIVED`)* · exercise report · prioritised improvements.

### §15 Retest
Re-exercise after improvements. **Recommended annually. Needs Sleuth Confirmation.**

**`[GAP]` non-blocking:** scenario library for `IRA-07`.
