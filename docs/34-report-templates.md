# 34 — Report Templates

> **Status — Draft / Needs SME Validation.** Structure is `PROPOSED`; client-facing deliverable
> language is `SITE-DERIVED`. Supersedes `08-reporting-architecture.md` §3, which was organised by
> the 21 public services rather than the 20 engagement types.

**Composition:** `Universal spine + Archetype sections + Service sections + Conditional sections`.
Templates are versioned and pinned like runbooks, and compose from shared modules — so a change to
the universal spine reaches all 20 templates in one edit (`20-shared-module-inheritance.md`).

**Legend:** **G** = generated from records, never typed · **A** = authored · **R** = required,
non-removable · `‹PH-nn›` = placeholder.

---

## 1. Universal spine — every report

| § | Section | | Notes |
|---|---|---|---|
| 0 | Cover & classification | **G R** | Client, engagement ID, classification, version, date |
| 0.1 | Document control | **G R** | Version · author · reviewer · **runbook ID and version executed** · report template version · distribution list · file hash |
| 1 | Executive summary | **A R** | Non-technical audience. Present on all 20 — 13 of 21 service pages promise one |
| 2 | Scope | **G R** | Generated from the approved asset schedule. **Must match the signed scope exactly** |
| 3 | Approach | **G+A R** | Method summary, runbook version, standards applied, tools and versions |
| 4 | **Limitations** | **G+A R** | **Auto-seeded, editable, not deletable.** See §5 |
| 5 | Conclusion | **A R** | |
| 6 | Appendices | **G** | Evidence index · tool versions · glossary |

**Why document control carries the runbook version.** A report delivered in 2026 must remain
explicable in 2029. Without the version, "what process did you follow?" has no retrievable answer.

---

## 2. Archetype sections

### A1 — Assessment & Advisory
Assessment approach and framework rationale **A** · Framework and control set **G** · Maturity summary
**G R** · Domain-by-domain results with source citations **G R** · Gap analysis **G** · Risk
contextualisation **A** · Prioritised roadmap **G+A R** · Quick wins **G** · Board summary **A**

### A2 — Authorised Technical Testing
Methodology **G+A** · **Intrusiveness level applied** **G R** *(new — `32` §1)* · Testing window **G R** ·
Assets tested, with any not reached **G R** · Findings summary by severity **G R** · Detailed findings
with evidence **G R** · Risk analysis **A** · Prioritised remediation **G R** · Retest results **G**
*(on addendum)*

### A3 — Investigation & Response
**Instructions received** **G R** · **Authority for examination** **G R** · Evidence inventory **G R** ·
Chain of custody summary **G R** · Acquisition and methods **G R** · Tools and versions used **G R** ·
Timeline of events **G R** · Findings of fact **G R** · Supporting evidence **G** · Analysis and
reasoning **A R** · **Alternative explanations considered** **A R** · Coverage statement **G** ·
Conclusion with confidence level **A R**

### A4 — Continuous & Readiness
Monitoring scope **G** · Period covered **G R** · Changes since last cycle **G R** · New exposures
**G** · Resolved exposures **G** · Alerts raised and disposition **G** · Recommendations **A**

---

## 3. Service sections — all 20 engagement types

### A1

| Type | Service-specific sections |
|---|---|
| `SF-A1-SPA` | Business and risk context · current-state capability summary · maturity scorecard by domain · security function assessment · architecture observations · investment and spend alignment · target operating model · sequencing roadmap |
| `SF-A1-CRA` | Framework and scope of applicability · **control applicability statement with exclusions justified** · control-by-control gap analysis · **evidence-for-certification map** · policy and documentation gaps · risk register · vendor register · readiness rating against the deadline · audit preparation pack |
| `SF-A1-TCR` | Per pack: extraction summary and completeness · benchmark comparison · deviation register · **accepted-deviation validation** · high-risk settings reviewed manually · implementation guidance. Cross-pack: consolidated priority view |
| `SF-A1-OTA` | **Safety statement and constraints observed** · site and process overview · asset inventory assessment · Purdue-level architecture review · **IT/OT convergence risk** · vendor and remote access governance · monitoring capability · OT incident readiness · maturity scorecard *(IEC 62443 / NIST SP 800-82)* · OT-specific playbook recommendations |
| `SF-A1-SOA` | SOC model and staffing assessment · log source coverage — onboarded vs expected · data quality findings · **detection coverage mapped to MITRE ATT&CK** · alert quality and false-positive analysis · triage and escalation assessment · **detection validation results — what fired, what did not, how fast** · SIEM architecture findings · detection content delivered |
| `SF-A1-IRA` | Readiness scorecard · backup architecture and isolation · **restore capability — tested versus claimed** · blast radius analysis · detection coverage for likely paths · playbook review · crisis communication and decision authority · exercise report *(exercise mode)* · improvement plan |

### A2

| Type | Service-specific sections |
|---|---|
| `SF-A2-IPT` | Reconnaissance summary · attack surface overview · host and service inventory · exploitation narrative · **chained attack paths** · vulnerability register by asset · *(internal)* lateral movement and segmentation findings · *(wireless)* wireless findings and physical boundary respected · remediation priority matrix |
| `SF-A2-WAT` | Application and endpoint inventory · authentication and session analysis · **authorisation matrix results — every role against every function** · injection and input handling · business logic findings · API-specific findings by style · file handling and SSRF · headers and transport · **developer remediation guide** |
| `SF-A2-MAT` | Platform-specific findings *(iOS / Android)* · build integrity · local storage analysis · transport and certificate validation · cryptographic implementation · binary protections · data exposure in logs and memory · IPC findings · backend API findings from the client perspective · **MASVS alignment summary** |
| `SF-A2-CPT` | Account and subscription inventory · **IAM privilege escalation paths** · public exposure register with confirmed reachability · storage and data access · network and segmentation · serverless and container · **secrets exposure — type and location only, never values** · cross-account movement · architecture recommendations |
| `SF-A2-ATP` | Forest and domain summary · privileged account analysis · Tier 0 exposure · **attack path visualisation, standard user → domain admin** · **validated versus theoretical paths** · Kerberos findings · delegation and trust findings · service account and SPN findings · credential hygiene · hardening roadmap |
| `SF-A2-RED` | Objectives and outcome per objective · **attack narrative, chronological** · initial access · full kill-chain walkthrough · **detection timeline: what was detected, when, by what, and what was missed** · blue team response assessment · deconfliction events · social engineering results *(aggregated)* · physical results · purple-team outcomes · **artefact removal confirmation** · detection improvement recommendations |
| `SF-A2-SES` | Campaign design and pretext · target population **by group** · **aggregate results only — no individual named** · click, submission and **report** rates · time to first report · pretext effectiveness · process gaps revealed · infrastructure teardown confirmation · awareness recommendations |

### A3

| Type | Service-specific sections |
|---|---|
| `SF-A3-IRE` | Incident overview · detection and notification · **full attacker timeline** · initial access · affected assets and data · attack path · persistence · lateral movement · privilege escalation · command and control · **data access assessment** and **data exfiltration assessment — stated separately** · containment actions · eradication verification · recovery guidance · IOC package · root cause · lessons learned. *Ransomware module adds:* encryption scope · variant identification · ransom note and actor communications analysis · **backup integrity and isolation** · decryption feasibility · recovery sequencing · reinfection risk. *BEC adds:* mailbox rule and forwarding analysis · authentication log analysis · OAuth grants · financial transaction tracing. *Data theft adds:* data classification of affected stores · staging artefacts · egress analysis · **breach scope determination**. *Insider adds:* account activity profile · data movement to removable media and personal cloud. *Web compromise adds:* webshell analysis · application log analysis · vulnerability determination |
| `SF-A3-DFE` | **Questions posed** · devices and evidence examined · acquisition details per item · file system and metadata analysis · deleted data recovery and its limits · email and communication analysis · internet and application artefacts · external device and data movement · documents relevant to the questions · reconstructed timeline · **one conclusion per question posed, each with a confidence level** |
| `SF-A3-SPY` | Device and account profile · **acquisition method and completeness — what could not be acquired, and why** · known-family indicator results **including negatives** · commercial stalkerware results · configuration profile and certificate analysis · network and permission analysis · exploitation artefact analysis · **assessment: compromised / not detected / inconclusive** · timeline of suspected activity · hardening, replacement and monitoring guidance · **safety considerations** *(where applicable, and only to the person)* |
| `SF-A3-CTH` | Hunt scope and **coverage achieved** · telemetry availability and gaps · hypotheses tested · **negative findings — what was checked and found clean** · IOCs identified · suspicious-but-unconfirmed observations · persistence review · authentication anomalies · detection gaps discovered · escalation record if compromise was confirmed |
| `SF-A3-MAL` | Sample identification and hashes · **sharing permission and what was shared** · static analysis · dynamic analysis and environment used · memory analysis · capability assessment · persistence mechanisms · network and C2 infrastructure · obfuscation and anti-analysis · **IOC package (host · network · registry · file)** · detection content delivered · sample disposition |

### A4

| Type | Service-specific sections |
|---|---|
| `SF-A4-ASM` | Attack surface inventory · **exposure register with severity and confirmed reachability** · credential exposure findings *(account and source only — never values)* · brand and domain impersonation · threat actor landscape for the sector · vulnerability intelligence against discovered assets · monitoring coverage · **cycle delta** |
| `SF-A4-VCI` | Period activity summary · risk posture change since last period · programme status against plan · risk register movement · **advisory record — advice given and decisions taken, stated separately** · metrics · next-period priorities · board summary · **independence declaration** where Sleuth provides other services |

---

## 4. Conditional sections

Attached by context module, in every template:

| Section | Attached when |
|---|---|
| Regulatory considerations | Regulated Sector |
| Safety considerations | OT / Safety-Critical |
| Personal data impact | Personal data present in scope or evidence |
| Notification assessment | Breach suspected *(counsel-dependent — see `31` §3.2)* |
| Cross-border handling | Cross-Border Data |
| **Deviations from standard methodology** | **Any gate override, delta, or unvalidated runbook content** |

---

## 5. The limitations section

Auto-seeded from ten sources, then contextualised by the author. **Editable, never deletable.**

| Seeded from | Produces |
|---|---|
| Unverified answers to `V`-flagged questions | "The following were stated by the client and not independently verified: …" |
| Custody gaps detected | "An unattributed interval of N hours exists for item E00n" |
| Evidence unavailable | "The following sources could not be obtained: …" |
| Required procedures marked N/A | "The following were not performed: … because …" |
| Required checklist items marked N/A | As above |
| **Gate overrides** | "This engagement proceeded under an approved override of the … gate" |
| **Active deltas** | "This engagement diverged from standard method in the following respect …" |
| **Unvalidated runbook content** | "Procedures marked as draft were executed …" *(Rule 1)* |
| Coverage shortfall *(A1, A3 hunts)* | "Coverage achieved was N% of the intended estate" |
| Assets not reached *(A2)* | "The following in-scope assets could not be tested: …" |

> This is the section I would defend hardest. Auto-seeding makes honest reporting the path of least
> resistance under deadline, rather than an act of discipline — and it is precisely what protects
> Sleuth when someone asks, eighteen months later, what was and was not covered.

---

## 6. Generation rules

- Findings, evidence inventory, scope, assets, timeline and remediation are **generated**. A severity
  is never retyped into a table where it can drift from the record.
- Narrative sections are authored with the underlying structured data visible beside the editor.
- Changing a finding updates every place it appears. **There is no second source of truth.**
- Every report version is retained; the delivered version is frozen byte-identical with its hash recorded.
- Every report states the runbook ID and version, the report template version, the tools and versions
  used, and the evidence relied upon.

---

## 7. Placeholders

| Ref | Placeholder | Default applied |
|---|---|---|
| `‹PH-01›` | Sleuth house report styling — cover, typography, headers | Inherit the site design system (`12`); Sleuth to confirm |
| `‹PH-02›` | Standard legal wording — confidentiality, disclaimer, limitation of liability | **Counsel. Not drafted** *(Rule 5)* |
| `‹PH-03›` | Whether an attestation or certificate letter is issued for compliance-driven tests | Assumed **not** offered *(NC-18)* |
| `‹PH-04›` | Board summary pack format for `SF-A4-VCI` | One page, risk posture + top three + decisions needed |
| `‹PH-05›` | Client-facing executive summary length convention | One page, no technical terms unexplained |

---

## 8. Counts

| | |
|---|---|
| Report templates | **20** |
| Universal spine sections | 7, all required |
| Archetype section sets | 4 |
| Service section groups | 20 *(≈180 distinct sections)* |
| Conditional sections | 6 |
| Generated vs authored | **~65% generated** |
| `SME-VALIDATED` | **0** |
