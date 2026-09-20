# 08 — Findings, Reporting & QA

> "Clarity in communication — we prioritise clear reporting for both technical and non-technical audiences." — sleuthforensics.in/about
>
> 13 of the 21 services promise an executive summary alongside a technical body (research §6.1). The report is not an export. It is the product.

---

## 1. The finding

A finding is a claim Sleuth is prepared to defend. Its structure enforces that.

| Field | Notes |
|---|---|
| `finding_id` | `ENG-2026-0141-F012` — cited directly in the report and in retest |
| `title` | What is wrong, stated as a condition not a tool output |
| `severity` | Critical · High · Medium · Low · Informational |
| `severity_rationale` | **Mandatory.** Why *this* severity, for *this* client |
| `cvss_vector` | Optional, A2 only. Supplementary to, never a replacement for, rationale |
| `affected_assets[]` | Links to scope assets |
| `category` | Taxonomy per archetype |
| `description` | The condition |
| `impact` | What it means for this client's business |
| `evidence_refs[]` | **≥1 required.** A finding with none cannot enter a report |
| `reproduction_steps` | A2 |
| `recommendation` | Specific and actionable |
| `remediation_effort` | Low · Medium · High — clients prioritise on this |
| `status` | Draft · In review · Confirmed · Client-disputed · Withdrawn · Remediated · Risk accepted |
| `author_id` / `reviewer_id` | **Must differ.** Enforced at write time |
| `severity_history[]` | Every change, who, why — moderation is visible, not silent |
| `retest_outcome` | Resolved · Partially resolved · Not resolved · Risk accepted · Unable to verify |
| `client_response` | Accepted · Disputed with reason · Risk accepted with owner and date |

### 1.1 Severity is moderated, not decided alone

Severity assigned by a single analyst under deadline is the most common source of inconsistency across a consultancy's reports — and clients notice when the same issue is High in March and Medium in September.

Mitigations, in order of usefulness: a severity decision tree applied at drafting; mandatory written rationale; Reviewer moderation as part of the QA Gate; a visible severity history; and calibration — showing the analyst how comparable findings were rated on other engagements. The last one is the one that actually changes behaviour, and it costs nothing once findings are structured data.

### 1.2 Findings in A1 and A3

- **A1** produces *gaps* and *maturity ratings* rather than vulnerabilities: control reference, current state, target state, gap, risk, recommendation, effort — and a mandatory source citation, which is A1's version of the evidence link.
- **A3** produces *factual determinations* rather than findings: what was established, the evidence supporting it, the confidence level, and — critically — **alternative explanations considered and why they were discounted**. That last field is what separates an investigative conclusion from an assertion, and it belongs in the data model, not in an examiner's discipline.

---

## 2. Report composition

Reports compose exactly as runbooks and questionnaires do.

```
Report = Universal spine  +  Archetype sections  +  Service sections  +  Conditional sections
```

### 2.1 Universal spine (every report)

Cover & classification · Document control (version, date, author, reviewer, **runbook ID and version used**, distribution list) · Executive summary · Scope · **Limitations** · Conclusion · Appendices.

**Limitations is mandatory and non-removable.** It is populated in part automatically — from unverified questionnaire answers, custody gaps, unavailable evidence, procedures marked not-applicable, gate overrides and out-of-window constraints. The consultant edits and contextualises it; they cannot delete it. This is where "evidence over assumption" is most visible to the client, and it is also what protects Sleuth when a question arises later about what was and was not covered.

### 2.2 Archetype sections

| A1 — Assessment | A2 — Testing | A3 — Investigation | A4 — Continuous |
|---|---|---|---|
| Assessment approach | Methodology | **Instructions received** | Monitoring scope |
| Framework & rationale | Testing window | **Authority for examination** | Period covered |
| Maturity summary | Assets tested | **Evidence inventory** | Changes since last cycle |
| Domain-by-domain findings | Findings summary | **Chain of custody summary** | New exposures |
| Gap analysis | Detailed findings | **Acquisition & methods** | Resolved exposures |
| Prioritised roadmap | Evidence & PoC | **Tools & versions used** | Alerts raised & disposition |
| Quick wins | Risk analysis | **Timeline of events** | Recommendations |
| | Remediation | **Findings of fact** | |
| | **Retest** | **Supporting evidence** | |
| | | **Analysis & reasoning** | |
| | | **Alternative explanations considered** | |
| | | **Conclusion with confidence statement** | |

The three structures the brief supplied (VAPT, Digital Forensics, Incident Response) are reproduced by this composition — which was the test of whether the model is real rather than tidy.

### 2.3 Conditional sections

Attached by context module: Regulatory considerations *(regulated sector)* · Safety considerations *(OT)* · Personal data impact *(personal data present)* · Notification assessment *(breach suspected)* · Detection & response analysis *(red team)* · Deviations from standard methodology *(any gate override)*.

That last one closes a loop: an override granted under commercial pressure in Phase 2 automatically surfaces as a paragraph in the client's report. Overrides that nobody wants to explain to the client tend not to be requested.

---

## 3. Report structures — all 21 services

Universal spine assumed throughout; archetype sections per §2.2. Listed below is the **service-specific delta**.

### SECURITY

| Service | Service-specific sections |
|---|---|
| 1. Cybersecurity Consulting | Business & risk context · Current-state capability summary · Maturity scorecard by domain · Target operating model · Investment & sequencing roadmap · Board summary |
| 2. Security Audits | Framework & control set · Control-by-control results · Evidence index by control · Maturity comparison (prior vs current) · Non-conformities · Audit trail of sampling |
| 3. VAPT | Reconnaissance summary · Attack surface overview · Exploitation narrative · Chained attack paths · Vulnerability register by asset · Remediation priority matrix · Retest results |
| 4. Network Security | Topology assessment · Segmentation analysis · **Lateral movement paths** · Firewall & ACL findings · Remote access findings · Wireless findings · Device hardening summary |
| 5. Web App & API Security | Application & endpoint inventory · Authentication & session analysis · Authorisation matrix testing results · Injection & input handling · **Business logic findings** · API-specific findings (REST/GraphQL/SOAP) · Developer remediation guide |
| 6. OT Security | **Safety statement & constraints observed** · Asset inventory assessment · Purdue-level architecture review · IT/OT convergence risk · Vendor & remote access governance · Maturity scorecard (IEC 62443 / NIST SP 800-82) · OT incident readiness · Convergence risk assessment |
| 7. Mobile App Security | Platform-specific findings (iOS / Android) · Local storage analysis · Transport & certificate validation · Binary protection assessment · Backend API findings from client perspective · Per-platform developer guidance |
| 8. Cloud Security | Account/subscription inventory · IAM analysis · **Public exposure register** · Data protection & encryption · Logging & monitoring coverage · Benchmark comparison · Architecture recommendations |
| 9. Identity & AD | Forest & domain summary · Privileged account analysis · Tier 0 exposure · **Attack path visualisation (standard user → domain admin)** · Kerberos findings · Service account & SPN findings · Trust & delegation findings · Hardening roadmap |
| 10. Endpoint Security | Estate & coverage summary · Baseline conformance by group · EPP/EDR deployment gaps · Local privilege findings · Execution control assessment · Removable media controls · Endpoint telemetry gaps · Hardening implementation guide |

### INVESTIGATION

| Service | Service-specific sections |
|---|---|
| 11. Digital Forensics | Examination request & questions posed · Devices & evidence examined · Acquisition details per item · **Artefact analysis by category** · Reconstructed timeline · Findings of fact · Documents/communications recovered · Deleted & recovered data · Attribution analysis where supportable · Conclusion per question posed |
| 12. Mobile Spyware | **Device & account profile** · Acquisition method & completeness (what could not be acquired, and why) · Known-family indicator results (per family checked, including negatives) · Commercial stalkerware results · Configuration profile & certificate analysis · Network & permission analysis · Exploitation artefact analysis · **Assessment: compromised / not detected / inconclusive** · Timeline of suspected activity · Hardening & monitoring guidance |
| 13. DFIR | Incident overview · Detection & notification · **Full attacker timeline** · Initial access · Affected assets & data · Attack path · Persistence · Lateral movement · Privilege escalation · Command & control · Data access & exfiltration assessment · Containment actions · Eradication verification · Recovery guidance · IOCs · Root cause · Lessons learned |
| 14. Incident Response | As DFIR, plus: **Breach scope determination** · Data classes affected · Individuals potentially affected · **Notification assessment** *(counsel-dependent — see open questions)* · Containment confirmation · Eradication confirmation · Restoration validation |
| 15. Compromise Assessment | Hunt scope & coverage achieved · Hypotheses tested · **Negative findings (what was checked and found clean)** · IOCs identified · Suspicious-but-unconfirmed observations · Detection gaps discovered · Escalation record if compromise was confirmed |
| 16. Malware Analysis | Sample identification & hashes · Static analysis · Dynamic analysis & environment used · Capability assessment · Persistence mechanisms · Network & C2 infrastructure · Obfuscation & anti-analysis techniques · **IOC package (hashes, network, host, registry)** · Detection recommendations · YARA/detection content where produced |

### RESILIENCE

| Service | Service-specific sections |
|---|---|
| 17. Ransomware — Investigation | Encryption scope & impact · Variant identification · Initial access vector · Dwell time · Lateral movement · **Exfiltration assessment** · Ransom note & actor communications analysis · Backup integrity assessment · Recovery sequencing recommendation · Reinfection risk assessment |
| 17. Ransomware — Readiness | Readiness scorecard · Backup architecture & isolation assessment · **Restore capability assessment** (tested vs claimed) · Segmentation & blast radius analysis · Detection coverage · Playbook review · Crisis communication readiness · Prioritised improvements · Scenario walkthrough results |
| 18. Threat Intelligence | Attack surface inventory · **Exposure register with severity** · Credential exposure findings · Brand & domain impersonation · Threat actor landscape for this sector · Vulnerability intelligence relevant to discovered assets · Monitoring recommendations · Cycle delta *(A4 cycles)* |
| 19. Security Operations | Maturity scorecard · Log source coverage vs expected · **Detection coverage mapped to adversary techniques** · Alert quality & false-positive analysis · Triage & escalation process assessment · SIEM architecture findings · Staffing & shift model assessment · Detection engineering recommendations · Rule improvements delivered |
| 20. Red Teaming | Objectives & outcome per objective · **Attack narrative (chronological)** · Initial access · Full kill-chain walkthrough · **Detection timeline: what was detected, when, by what, and what was missed** · Blue team response assessment · Deconfliction events · Social engineering results *(aggregated, never naming individuals)* · Physical results where applicable · Purple team outcomes · Detection improvement recommendations |
| 21. Compliance / GRC | Framework & scope of applicability · **Control-by-control gap analysis** · Compliance readiness rating · Policy & documentation gaps · Risk register (delivered as an artefact) · Remediation roadmap to certification · Audit preparation checklist · Board summary · *(vCISO: period activity, risk posture change, programme status, metrics, next-period priorities)* |

---

## 4. Report generation

Reports are assembled from structured data, not typed into a word processor.

- Findings, evidence, scope, timeline, assets and remediation items are **generated** — a finding's severity is never manually re-typed into a table where it can drift from the record.
- Narrative sections are authored, with the underlying structured data visible beside the editor.
- Changing a finding's severity updates every place it appears. There is no second source of truth.
- Every report version is retained; delivered versions are frozen byte-identical.
- The report states the runbook ID and version used, the tools and versions used, and the evidence items relied upon.

---

## 5. QA: the review workflow

```
Draft ──submit──► In Technical Review ──┬── Rejected ──► back to Draft
                                        │                (with specific,
                                        │                 itemised reasons)
                                        └── Approved ──► ⟨ QA GATE ⟩ ──► Ready for Release
```

**QA Gate conditions** (from `03-engagement-lifecycle.md`, restated with the report-specific checks):

- Reviewer ≠ author, on the report and on every finding
- Every finding: evidence linked, severity set, rationale written
- Every required section present and non-empty
- Scope statement matches the approved scope exactly
- Limitations section reviewed and contextualised
- No open `Needs Review` checklist items anywhere in the engagement
- Evidence Integrity Gate previously passed
- No unresolved reviewer rejections

**Review is itemised, not conversational.** A reviewer rejects specific findings or sections with a reason code and a note, producing a worklist rather than a paragraph of feedback to interpret. Review time is the scarcest resource in a consultancy; the interface should spend it on judgement, not on locating what changed.

**Rework signal.** Rejection reasons are aggregated — by analyst, by service, by finding category. Consistently rejected categories indicate a runbook or training gap, not an individual problem, and that feedback loop is one of the more valuable things a platform like this produces over time.
