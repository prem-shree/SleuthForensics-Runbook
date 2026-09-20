# 01 — Service Catalogue & Engagement Types

> **Status — DRAFT / NEEDS SME VALIDATION.** Per Rule 1 of [`17-governing-constraints.md`](17-governing-constraints.md), nothing in this document is
> confirmed Sleuth practice. Procedures, tools, legal requirements and operational rules here are
> proposals for SME review, not internal SOP. Content drawn from the public website is
> `SITE-SUGGESTED` and carries no authority over internal method (Rule 6). Gaps are named rather
> than filled (Rule 2). Validation vocabulary: [`18-content-provenance-and-validation.md`](18-content-provenance-and-validation.md).
>
> **Superseded on arrival.** The 41 engagement types below are derived from the public
> catalogue. Sleuth's actual list replaces them; anything Sleuth does not sell is deleted,
> not merged. The four archetypes are re-tested against the real list (a fifth is a genuine
> possible outcome).


**Purpose:** Turn 21 marketed services into the unit the platform actually operates on.

---

## 1. The core modelling decision

> A runbook does **not** attach to a service. It attaches to an **engagement type**.

Research finding 4.1 showed that several services contain two incompatible workflows under one commercial name. Ransomware is sold as one service but the site itself splits its deliverables into "proactive engagements" and "reactive engagements". A single runbook cannot serve both: one starts with a scheduled kickoff and a maturity questionnaire, the other starts at 2am with encrypted servers.

So the catalogue has three levels:

```
Pillar            Security | Investigation | Resilience          (3, from the site)
  └─ Service      21 marketed services                            (21, from the site)
       └─ Engagement Type   the unit a client buys and a team runs (~30)
            └─ Runbook (versioned)  1 approved version per engagement type
```

An engagement type is defined by answering: *does this change what the consultant does on day one?* If yes, it is a separate engagement type. If it only changes scope size, it is the same type with different scope.

---

## 2. The four execution archetypes

Every engagement type belongs to exactly one archetype. The archetype determines the **shape** of the workflow: which gates apply, what counts as evidence, what the closure obligations are. This is what makes 21 services tractable without writing 21 unrelated systems.

| | **A1 — Assessment & Advisory** | **A2 — Authorised Technical Testing** | **A3 — Investigation & Response** | **A4 — Continuous & Readiness** |
|---|---|---|---|---|
| **Core question** | "How good is this, measured against what?" | "What can an attacker actually do?" | "What happened, and can we prove it?" | "What changed, and are we still ready?" |
| **Trigger** | Planned | Planned, windowed | Unplanned / suspicion | Recurring cycle |
| **Primary evidence** | Documents, interviews, config exports, screenshots | Tool output, request/response captures, PoC artefacts | Forensic images, memory, logs, artefacts — custody-critical | Monitoring output, findings deltas |
| **Authorisation** | Engagement agreement | **Letter of Authorisation + Rules of Engagement + testing window** | Authority to investigate; device/data ownership; may be **emergency** | Standing authorisation per cycle |
| **Chain of custody** | Not required | Light (artefact retention) | **Mandatory and gating** | Not required |
| **Defining risk** | Wrong benchmark, unsupported maturity claim | Damage to production, out-of-scope testing, untraceable action | Evidence spoliation, broken custody, unsupportable conclusion | Alert fatigue, silent lapse in coverage |
| **Output shape** | Maturity scorecard + gap analysis + roadmap | Findings register + PoC + remediation + **retest** | Narrative + timeline + evidence inventory + conclusion | Cycle report + delta + alert log |
| **Closure** | Report accepted | Retest closed out | **Evidence disposition executed** | Cycle ends; contract continues |

### Why four and not more

The temptation is to split further (e.g. "offensive" vs "configuration review"). Resist it. A fifth archetype means a fifth set of gates, a fifth report spine, and a fifth QA path to maintain. The differences inside an archetype are handled by **modules** (see §4), which are cheap. Differences *between* archetypes are expensive, so there should be as few as the work genuinely requires — and the work genuinely requires these four, because each has a different legal and evidentiary posture.

---

## 3. Full catalogue: 21 services → engagement types

`SF-<PILLAR>-<SERVICE>-<TYPE>` is the proposed runbook ID scheme. Pillar codes: `SEC`, `INV`, `RES`.

### SECURITY

| Service | Engagement type | Archetype | Runbook ID | Notes |
|---|---|---|---|---|
| 1. Cybersecurity Consulting & Advisory | Posture & Maturity Assessment | A1 | `SF-SEC-CON-MAT` | Site publishes an "Our Approach" for this |
| | Security Programme & Roadmap Development | A1 | `SF-SEC-CON-PRG` | |
| | Security Architecture Review | A1 | `SF-SEC-CON-ARC` | |
| 2. Cybersecurity Audits & Security Reviews | Framework-Based Security Audit | A1 | `SF-SEC-AUD-FWK` | Framework selected at scoping |
| | Pre-Certification Readiness Review | A1 | `SF-SEC-AUD-CRT` | |
| | M&A / Transaction Security Review | A1 | `SF-SEC-AUD-MNA` | Site names M&A explicitly |
| 3. VAPT | External Infrastructure Test | A2 | `SF-SEC-VAP-EXT` | |
| | Internal Infrastructure Test | A2 | `SF-SEC-VAP-INT` | |
| | Vulnerability Assessment (non-exploitative) | A2‑lite | `SF-SEC-VAP-VAS` | No exploitation; lighter RoE, still needs LoA |
| 4. Network Security | Architecture & Segmentation Review | A1 | `SF-SEC-NET-ARC` | Config/documentation-led |
| | Network Penetration Test | A2 | `SF-SEC-NET-PEN` | |
| | Wireless Security Assessment | A2 | `SF-SEC-NET-WIF` | Site lists wireless under both NET and VAPT |
| 5. Web App & API Security | Web Application Test | A2 | `SF-SEC-APP-WEB` | |
| | API Security Test | A2 | `SF-SEC-APP-API` | REST / GraphQL / SOAP |
| 6. OT Security | OT/ICS Maturity Assessment | A1 | `SF-SEC-OTS-MAT` | IEC 62443 / NIST SP 800‑82 / SANS ICS |
| | OT Passive Assessment (live environment) | A1+ | `SF-SEC-OTS-PAS` | Safety-gated; strictly non-intrusive |
| 7. Mobile App Security | Mobile Application Test (iOS) | A2 | `SF-SEC-MOB-IOS` | |
| | Mobile Application Test (Android) | A2 | `SF-SEC-MOB-AND` | |
| 8. Cloud Security | Cloud Configuration Review | A1 | `SF-SEC-CLD-CFG` | Read-only access to AWS/Azure/GCP |
| | Cloud Penetration Test | A2 | `SF-SEC-CLD-PEN` | Provider-policy check required |
| 9. Identity & AD | AD Configuration & Hygiene Review | A1 | `SF-SEC-IDM-CFG` | |
| | Attack Path Assessment | A2 | `SF-SEC-IDM-ATP` | "standard user → domain admin" |
| 10. Endpoint Security | Endpoint Hardening Baseline Review | A1 | `SF-SEC-END-CFG` | |
| | Endpoint Control Validation | A2 | `SF-SEC-END-VAL` | Active bypass testing of EPP/whitelisting |

### INVESTIGATION

| Service | Engagement type | Archetype | Runbook ID | Notes |
|---|---|---|---|---|
| 11. Digital Forensics | Forensic Examination (device/host) | A3 | `SF-INV-DFX-EXAM` | Site publishes an "Our Approach" |
| | Internal / HR / Employee Investigation | A3 | `SF-INV-DFX-HR` | Site names "Legal and HR teams" |
| | Independent / Second-Opinion Examination | A3 | `SF-INV-DFX-IND` | Site: "independent forensic examination" |
| 12. Mobile Spyware Detection | Device Spyware Examination | A3 | `SF-INV-SPY-EXAM` | **Individual clients supported** |
| 13. DFIR | Full-Scope DFIR Engagement | A3 | `SF-INV-DFIR-FULL` | Site publishes an "Our Approach" |
| 14. Incident Response | Emergency Incident Response | A3‑E | `SF-INV-IR-EMG` | **Emergency authorisation path** |
| | Breach Scope & Notification Assessment | A3 | `SF-INV-IR-BSA` | Site: "breach notification assessment support" |
| 15. Compromise Assessment | Compromise Assessment (suspicion-driven) | A3 | `SF-INV-CMP-SUS` | |
| | Periodic Threat Hunt | A4 | `SF-INV-CMP-HUNT` | Site: "periodic threat hunting as a proactive measure" |
| 16. Malware Analysis | Malware Analysis (standalone) | A3 | `SF-INV-MAL-STD` | |
| | Malware Analysis (child of an investigation) | A3‑C | `SF-INV-MAL-CHILD` | Inherits parent custody & authorisation |

### RESILIENCE

| Service | Engagement type | Archetype | Runbook ID | Notes |
|---|---|---|---|---|
| 17. Ransomware | Active Ransomware Investigation | A3‑E | `SF-RES-RAN-INV` | Emergency path; overlaps IR |
| | Ransomware Readiness Assessment | A1 | `SF-RES-RAN-RDY` | Site: "proactive engagements" |
| | Playbook & Tabletop Development | A1 | `SF-RES-RAN-TTX` | Facilitated exercise, not an assessment |
| 18. Threat Intelligence | Attack Surface Baseline | A1 | `SF-RES-TIA-BASE` | One-off discovery/mapping |
| | Continuous Monitoring Cycle | A4 | `SF-RES-TIA-MON` | Recurring; alert-driven |
| 19. Security Operations / SOC | SecOps Maturity Assessment | A1 | `SF-RES-SOC-MAT` | |
| | SIEM Architecture & Coverage Review | A1 | `SF-RES-SOC-SIEM` | |
| | Detection Engineering Engagement | A1+ | `SF-RES-SOC-DET` | Builds artefacts (rules), not just findings |
| 20. Red Teaming | Objective-Based Red Team | A2+ | `SF-RES-RED-OBJ` | Deconfliction + detection tracking |
| | Purple Team Exercise | A2+ | `SF-RES-RED-PUR` | Site names "Purple team collaboration" |
| | Social Engineering / Phishing Simulation | A2+ | `SF-RES-RED-SE` | People are the target → extra approval |
| 21. Compliance / GRC / vCISO | Compliance Readiness & Gap Analysis | A1 | `SF-RES-GRC-GAP` | |
| | Policy & Documentation Development | A1 | `SF-RES-GRC-POL` | Output is documents, not findings |
| | Risk Assessment & Register Build | A1 | `SF-RES-GRC-RSK` | |
| | vCISO Retainer | A4 | `SF-RES-GRC-VCISO` | Recurring board reporting; no closure |

**Totals: 21 services → 41 engagement types → 4 archetypes.**

> 41 is a ceiling, not a commitment. Several types (e.g. `VAP-EXT` / `VAP-INT`, `MOB-IOS` / `MOB-AND`) may be better as one runbook with a variant switch. That is a content decision for Sleuth's practice leads, and it is deliberately cheap to change because the runbook is data, not code. **Needs Confirmation:** which of these Sleuth actually sells as distinct engagements, and in what volume.

### Archetype distribution

| Archetype | Engagement types | Share |
|---|---|---|
| A1 — Assessment & Advisory | 20 | 49% |
| A2 — Authorised Technical Testing | 13 | 32% |
| A3 — Investigation & Response | 9 | 22% |
| A4 — Continuous & Readiness | 4 | 10% |

(Types marked `A2+`, `A3-E` etc. count under their base archetype; percentages exceed 100% only through rounding of the hybrid labels.)

> **Sequencing consequence.** A1 is the largest bucket, but **A2 is the right first build**. A2 has the most externally-enforced structure (authorisation, scope, window, findings, retest), so building it first exercises gates, findings, reporting and retest — the machinery A1 and A3 both reuse. A1 built first would produce a document-management tool that later has to be retrofitted with authorisation and evidence semantics. See `12-implementation-plan.md`.

---

## 4. Modules: how services stay distinct without 41 separate systems

An engagement type's runbook is **composed**, not written from scratch:

```
Runbook (engagement type)
  =  Core spine            (every engagement, all archetypes)
   +  Archetype module      (A1 | A2 | A3 | A4)
   +  Service module        (the specific technical methodology)
   +  Context modules       (conditionally attached)
```

**Context modules** attach based on facts established at intake and scoping. They are the mechanism for handling real-world variation without branching the runbook:

| Context module | Attach condition | Adds |
|---|---|---|
| Production Systems | Any in-scope asset is production | Production-safe procedure variants, change-window approval, rollback requirement, client on-call contact |
| Third-Party Hosted | Assets not owned by the client | Third-party authorisation task, provider-policy check, blocking gate condition |
| OT / Safety-Critical | OT or ICS in scope | Safety review, passive-only default, engineer-present requirement, stop-on-anomaly condition |
| Individual Client | `client_type = Individual` | Consent & device-ownership verification, simplified contracting, personal-safety handling notes |
| Legal Hold / Litigation | Client indicates proceedings | Stricter custody, no-deletion hold on disposition, counsel-contact escalation |
| Regulated Sector | Sector in the regulated list | Sector notification questions, regulator timeline awareness, retention overrides |
| Emergency | Urgency = active incident | Emergency authorisation record, ratification task with deadline, abbreviated pre-engagement |
| People-Targeting | Social engineering / phishing in scope | HR & legal approval, staff-welfare notes, debrief obligation, no-credential-capture rule |
| Cross-Border Data | Evidence or data leaves India | Transfer authorisation, residency check, counsel review |

This is why the architecture does not need 41 hand-written documents. A new engagement type is typically: pick an archetype, write the service module, declare which context modules can attach. The core spine and archetype module are inherited and centrally maintained — fix a custody procedure once and all nine A3 runbooks improve.

### Worked composition examples

```
SF-SEC-VAP-EXT   = Core + A2 + [External Infrastructure Methodology]
                          + {Production Systems?, Third-Party Hosted?, Regulated Sector?}

SF-INV-IR-EMG    = Core + A3 + [Incident Response Methodology]
                          + {Emergency (always), Legal Hold?, Regulated Sector?,
                             Cross-Border Data?}

SF-INV-SPY-EXAM  = Core + A3 + [Mobile Device Spyware Methodology]
                          + {Individual Client?, Legal Hold?}

SF-SEC-OTS-PAS   = Core + A1 + [OT Maturity Methodology]
                          + {OT/Safety-Critical (always), Production Systems (always)}

SF-RES-RED-SE    = Core + A2 + [Adversary Simulation Methodology]
                          + {People-Targeting (always), Production Systems?}
```

---

## 5. Child engagements

Research finding 6.2 showed Malware Analysis is nearly always reached from inside another engagement. The model therefore supports a **child engagement**: a scoped piece of work spawned from a parent, which inherits the parent's client, authorisation, custody chain and classification, but has its own runbook, tasks and output.

Primary child-engagement paths observed in the site's own "Related Services" graph:

| Parent | Spawns child | Trigger |
|---|---|---|
| DFIR / IR / Compromise Assessment | Malware Analysis | Suspicious binary recovered |
| Compromise Assessment | Incident Response | "Escalation support if active compromise is confirmed" — the site's own words |
| Incident Response | Digital Forensics | Formal examination needed for legal/HR purposes |
| Ransomware Investigation | Malware Analysis | Variant identification |
| Any A2 test | Incident Response | Tester discovers a **pre-existing** compromise — a mandatory stop-and-escalate condition |

That last row deserves emphasis: a penetration tester finding evidence that someone else is already inside is one of the highest-stakes moments in this line of work. It is a hard stop condition in the A2 archetype with a defined escalation path, not a judgement call left to the individual under time pressure.
