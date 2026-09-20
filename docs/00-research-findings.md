# 00 — Research Findings: sleuthforensics.in

**Status:** Complete. Source of truth for everything downstream.
**Method:** Full retrieval of the services index, all 21 service detail pages, homepage, about, industries, contact, terms, privacy, and the site stylesheet.
**Date of research:** 2026-09-20

Everything in this document is *observed on the website*. Nothing here is inferred.
Anything the site does not state is recorded in `11-assumptions-and-open-questions.md` as **Needs Confirmation**.

---

## 1. Positioning (verbatim)

| Element | Text |
|---|---|
| Page title | "Sleuth Forensics — Cybersecurity Services & Digital Forensics \| India" |
| Hero headline | "Investigate. Respond. Strengthen." |
| Hero subheadline | "Understand where your environment is exposed, investigate what matters, and turn technical findings into a practical security improvement plan." |
| Tagline (footer) | "Cybersecurity services and digital forensics for organisations that take security, investigations, and resilience seriously." |
| Mission (about) | "Security improvement through evidence and clarity." |
| Self-description (about) | "a cybersecurity services and digital forensics firm that helps organisations understand their security exposure, investigate what matters, and build practical resilience." |
| Services intro | "Cybersecurity consulting, security assessments, digital forensics, incident response, and strategic advisory services for organisations across India." |

### 1.1 Stated principles (about page, verbatim)

1. **Evidence over assumption** — "Every finding is supported by evidence."
2. **Clarity in communication** — "we prioritise clear reporting for both technical and non-technical audiences."
3. **Practical improvement** — recommendations "account for your organisation's operational reality."
4. **Confidentiality and trust** — "We maintain strict confidentiality and handle all data with appropriate care."

> **Design consequence.** These four principles are not marketing copy to be ignored — they are the acceptance criteria for the platform.
> "Evidence over assumption" means a finding without a linked evidence record is an invalid record, not a warning.
> "Clarity" means the report engine is a first-class subsystem, not an export.
> "Practical improvement" means remediation and retest are lifecycle phases, not appendices.
> "Confidentiality" means least-privilege is the default access model, not a setting.

### 1.2 Published methodology — the six steps

The homepage and about page both publish the same six-step method:

```
Understand → Examine → Analyse → Report → Improve → Validate
```

> **Design consequence — the single most important one in this document.**
> Sleuth already publishes an engagement method. The platform's lifecycle must *be* that method, extended at both ends with the commercial/legal wrapper (pre-engagement) and closure (post-engagement).
> Inventing a different lifecycle would put the internal tool out of step with what clients are told. See `03-engagement-lifecycle.md`.

### 1.3 Three pillars

| Pillar | Site sub-label | Service count |
|---|---|---|
| Security | "Assess & Strengthen" | 10 |
| Investigation | "Investigate & Respond" | 6 |
| Resilience | "Prepare & Sustain" | 5 |

### 1.4 Stated differentiators (homepage)

"Evidence-Driven Analysis", "Technical Depth", "Clear, Actionable Reporting", "Structured Methodology", "Confidentiality", "Business-Aware Recommendations".

---

## 2. Service page template

All 21 service pages follow one template. This is the strongest structural signal on the site:

```
<Service Name>
  Overview
  Who This Is For              → engagement types / client situations
  What We <verb>               → scope of work  (verb varies: Assess / Examine /
                                 Test / Analyse / Cover / Do / Investigate)
  Our Approach                 → PRESENT ON ONLY 5 OF 21 PAGES
  What You Receive             → deliverables
  Related Services             → service adjacency graph
  Discuss This Service         → CTA
```

**"Our Approach" appears on only 5 pages:** Cybersecurity Consulting, Security Audits, Digital Forensics, DFIR, and (inline) VAPT. The other 16 services have **no published methodology**.

> **Design consequence.** The runbook library is not a re-statement of the website. For 16 of 21 services the methodology does not exist in written form anywhere public. The platform is where it gets written down for the first time. That raises the authoring effort and makes runbook ownership/approval (`Draft → Review → Approved`) a Phase 1 requirement, not a later nicety.

### 2.1 Mapping site sections onto platform objects

| Site section | Becomes |
|---|---|
| "Who This Is For" | Engagement **types** and qualification criteria |
| "What We Examine / Test / Analyse" | **Procedures** and **tasks** within the runbook |
| "Our Approach" | The runbook **phase** sequence (where it exists) |
| "What You Receive" | The **report structure** and **deliverable** definitions |
| "Related Services" | Cross-sell / scope-expansion prompts, and **child engagement** suggestions |

---

## 3. The 21 services as published

Exact names and URLs as they appear on `/services/index.html`.

### SECURITY

| # | Site name | Slug |
|---|---|---|
| 1 | Cybersecurity Consulting & Advisory | `cybersecurity-consulting` |
| 2 | Cybersecurity Audits & Security Reviews | `security-audits` |
| 3 | Vulnerability Assessment & Penetration Testing | `vapt` |
| 4 | Network Security Assessment & Testing | `network-security` |
| 5 | Web Application & API Security Testing | `application-security` |
| 6 | OT Security Maturity Assessment | `ot-security` |
| 7 | Mobile Application Security Testing | `mobile-security` |
| 8 | Cloud Security Assessment & Testing | `cloud-security` |
| 9 | Active Directory & Identity Security | `identity-security` |
| 10 | Endpoint Security Assessment & Hardening | `endpoint-security` |

### INVESTIGATION

| # | Site name | Slug |
|---|---|---|
| 11 | Digital Forensics & Cyber Investigations | `digital-forensics` |
| 12 | Mobile Phone Spyware Detection | `mobile-spyware` |
| 13 | Digital Forensics & Incident Response | `dfir` |
| 14 | Incident Response & Breach Investigation | `incident-response` |
| 15 | Compromise Assessment & Threat Hunting | `compromise-assessment` |
| 16 | Malware Analysis & Reverse Engineering | `malware-analysis` |

### RESILIENCE

| # | Site name | Slug |
|---|---|---|
| 17 | Ransomware Investigation & Readiness | `ransomware` |
| 18 | Threat Intelligence & Attack Surface Monitoring | `threat-intelligence` |
| 19 | Security Operations Maturity Assessment / SIEM / SOC Consulting | `security-operations` |
| 20 | Red Teaming & Adversary Simulation | `red-team` |
| 21 | Cybersecurity Compliance, GRC & vCISO | `compliance` |

> **Naming note.** The brief's shortened names (e.g. "Network Security", "Cloud Security") differ slightly from the site's full names ("Network Security Assessment & Testing"). The platform should store both: `display_name` (site-exact, used in client-facing output) and `short_name` (used in dense internal UI). This avoids a slow drift between what the site sells and what the report says.

---

## 4. Findings that directly shape the architecture

### 4.1 Several services are two services wearing one name

The site itself splits them.

- **Ransomware Investigation & Readiness** — the deliverables list distinguishes "Assessment reports (proactive engagements)" from "Incident investigation reports (reactive engagements)". These are opposite workflows: one is a scheduled maturity review, the other is a live crisis.
- **Compliance, GRC & vCISO** — "compliance readiness assessment" is a project; "Virtual CISO" is an ongoing retainer with board reporting. Different cadence, different closure semantics.
- **Active Directory & Identity Security** — "AD forest and domain configurations" (review) vs "Attack path analysis from standard user to domain admin" (active testing requiring authorisation).
- **Endpoint Security** — hardening-baseline review vs active local privilege-escalation validation.
- **Compromise Assessment** — reactive ("suspect compromise") vs scheduled/periodic ("periodic threat hunting as a proactive measure").

> **Design consequence.** A runbook cannot attach to a *service*. It must attach to an **engagement type**, and a service has one or more engagement types. This single decision resolves most of the "common vs service-specific" tension in the brief. See `01-service-catalogue.md` and `04-workflow-archetypes.md`.

### 4.2 Individuals are clients, not only organisations

The Mobile Spyware Detection page targets "C-suite executives, board members, and high-net-worth individuals", "Journalists, activists, and individuals in sensitive roles", and "Individuals concerned about domestic surveillance or stalkerware".

> **Design consequence.** The `Client` entity cannot assume an organisation. It needs a `client_type` of `Organisation | Individual`, and the individual path has different contracting (no MSA/SOW against a company), different authority (device ownership and consent rather than corporate authorisation), and materially higher personal-safety sensitivity. The spyware page's own warning — "If you suspect your phone is being monitored, do not discuss it on that device" — is an operational instruction that belongs in the runbook's intake step.

### 4.3 The contact form already defines intake triage

The contact form has an **Urgency** field with exactly four values:

- General Enquiry
- Planning — Next 1–3 Months
- Upcoming — Within Weeks
- **Urgent — Active Incident or Immediate Need**

and an **Area of Interest** dropdown with 22 options (the 21 services + "Other / Not Sure"). Stated response commitment: "We will get back to you within one business day."

> **Design consequence.** Intake is not a blank form to design from scratch — it already exists and has a shape. The platform's Enquiry object should mirror these fields so a web enquiry maps 1:1 into the platform. The "Urgent — Active Incident" value is the trigger for the **emergency authorisation path** (see `03-engagement-lifecycle.md`), because an active incident cannot wait for a full contracting cycle before triage begins. "Other / Not Sure" is the trigger for a **service-selection decision tree** at intake.

### 4.4 The site names very few standards — and no credentials at all

**Standards / frameworks named anywhere on the site:**
- ISO 27001, SOC 2, NIST (compliance page)
- IEC 62443, NIST SP 800-82, "SANS ICS security model" (OT page)
- Cloud providers: AWS, Azure, GCP
- API styles: REST, GraphQL, SOAP
- Spyware families named: Pegasus, Predator, Hermit, "NSO/Cytrox-class tools", FlexiSPY, mSpy, Cocospy
- Mobile platforms: iOS, Android; Host OS: Windows, Linux, macOS
- OT technology: SCADA, PLCs, DCS, HMIs

**Conspicuously absent from the entire site:** named individuals, team size, years of experience, certifications (no CREST/OSCP/GCFA/EnCE/CISSP/ISO-lab accreditation claims), partnerships, tool vendors, client names, case studies, office address, phone number, public email, registered legal entity name.

> **Design consequence.** The tool catalogue, the examiner-competency model, and any "approved by a certified examiner" concept must be built as **configurable and empty**, seeded only by Sleuth. The platform must not ship with assumed certifications or an assumed tool stack. Every such field starts as Needs Confirmation.

### 4.5 Jurisdiction is India, and only India is stated

- Terms: "These terms are governed by the laws of India. Any disputes arising from the use of this website shall be subject to the jurisdiction of the courts in India."
- Services intro: "for organisations across India."
- Privacy policy: names **no** specific legislation (no DPDP Act, no IT Act, no GDPR), no registered entity, no address, no contact email. Last updated "September 2026".

> **Design consequence.** Indian legal context is the working assumption for data residency and for evidence-admissibility features, but the *specific* obligations Sleuth operates under (CERT-In incident reporting directions, DPDP Act 2023 duties, whether Sleuth issues electronic-record certificates under the Bharatiya Sakshya Adhiniyam 2023, whether examiners give expert testimony) are **not stated anywhere** and must be confirmed with qualified counsel before any of it is encoded. Recorded in the open-questions register.

### 4.6 Industries: the homepage and the industries page disagree

Homepage lists 6. The industries page lists 9: Technology & SaaS, Financial Services, Healthcare, Manufacturing, Professional Services, Retail & E-Commerce, **Education**, **Government & Public Sector**, **Other Regulated Industries**.

> **Design consequence.** Minor, but worth flagging to Sleuth: the platform should hold one canonical sector list (the 9) and the website should be reconciled to it. Sector matters operationally because it drives regulatory context in the intake questionnaire.

### 4.7 "Insights" is in the navigation but does not resolve

`/insights.html` and `/insights/index.html` both return HTTP 404 while "Insights" appears in the main menu. Reported as an observation about the public site; not a platform concern. Social media URLs in the footer are placeholders.

---

## 5. The existing design system (extracted from `/css/main.css`)

Sleuth already has a documented design system. The stylesheet's own header comment reads:

```
/* SLEUTH FORENSICS — Design System
   Flat color palette. No gradients. Enterprise-grade. */
```

That instruction matches the brief's design direction almost word for word. The internal platform should **inherit these tokens**, not invent a new look.

| Token group | Values |
|---|---|
| Navy | `--navy #0f1b2d` · `--navy-light #1a2b42` · `--navy-mid #253d5b` |
| Brand blue | `--blue-primary #2b5ea7` · `--blue-accent #5b9bd5` · `--blue-pale #e8f0fa` · `--blue-hover #1e4a8a` |
| Neutrals (warm cream) | `#fdfbf7` → `#faf8f4` → `#f5f2ec` → `#e8e4dd` → `#d4cfc7` → `#b0a99e` → `#8a8278` → `#6b6358` → `#4d4640` |
| Text | primary `#1d1c1a` · secondary `#36322e` · muted `#6b6358` · inverse `#fdfbf7` · link `#2b5ea7` |
| Semantic | border `#e2ded7` · border-strong `#d4cfc7` · success `#16a34a` · error `#dc2626` · warning `#d97706` |
| Type | `Inter` (400/500/600/700) · `IBM Plex Mono` (400/500/600) |
| Radius | 4 / 6 / 8 px only |
| Shadow | very subtle, navy-tinted, three steps |
| Transitions | 150 / 250 / 400 ms ease |

> **Design consequence.** The warm-cream neutral base (`#fdfbf7`, `#f5f2ec`) rather than cold grey is a distinctive and deliberate brand choice — it reads as paper/laboratory rather than generic SaaS. Keep it. The internal platform extends this system with a **status palette** and a **severity palette** that the public site does not need, plus a density scale for tables. See `08-visual-design-direction.md`.

---

## 6. Per-service research extract

Condensed "What We <verb>" and "What You Receive" per service. These are the seeds for procedures and report sections respectively. Full verbatim text is preserved in the notes below each heading where it materially affects design.

| # | Service | Scope of work (site) | Deliverables (site) |
|---|---|---|---|
| 1 | Cybersecurity Consulting | posture/maturity assessment; programme development & roadmap; security architecture review; policy & procedure development; risk framework alignment; technology evaluation; board briefings; vendor/third-party risk | assessment report; maturity scorecard; prioritised roadmap; executive summary; follow-up support |
| 2 | Security Audits & Reviews | policies/procedures/governance; access control & identity; network architecture & segmentation; endpoint protection & config mgmt; data protection & encryption; logging/monitoring/IR; third-party risk; awareness & training | audit report with findings, evidence, risk ratings; maturity assessment vs frameworks; gap analysis with prioritised remediation; executive summary |
| 3 | VAPT | external/internal network; web apps & APIs; mobile apps; cloud; wireless; authn/access control; configuration & patch mgmt | findings with exploitation evidence & PoC; risk-rated vulns with business impact; prioritised remediation; executive summary; **retest support** |
| 4 | Network Security | architecture & topology; firewall rules & ACLs; segmentation & VLANs; VPN/remote access; wireless; DNS/DHCP/core services; internal & external exposure; device hardening & mgmt interfaces | assessment report with topology findings; config review findings; segmentation & lateral-movement risk analysis; prioritised remediation |
| 5 | Web App & API Security | authn & session mgmt; authorisation & access control; input validation & injection; XSS/content injection; business logic; API (REST/GraphQL/SOAP); file upload & data handling; SSRF; security headers & transport | vulnerability report with evidence & reproduction steps; risk ratings with business impact; developer-friendly remediation; executive summary; **retest support** |
| 6 | OT Security Maturity | network architecture & segmentation; IT/OT convergence points; asset inventory completeness; patch & vuln mgmt; remote access; monitoring; IR readiness; vendor access governance; physical security integration; personnel training | maturity scorecard; gap analysis; risk-prioritised roadmap; convergence risk assessment; executive summary; OT-specific IR playbook recommendations |
| 7 | Mobile App Security | local storage & caching; network comms & cert validation; authn & session; cryptographic implementation; binary protections & obfuscation; sensitive data in logs/memory; IPC security; backend API from client perspective | platform-specific findings report; risk ratings aligned to mobile standards; per-platform developer remediation; executive summary |
| 8 | Cloud Security | IAM configurations; storage & database access controls; network security groups & VPC; encryption at rest/in transit; logging/monitoring/alerting; serverless & container; secrets management; resource exposure & public accessibility | assessment report with configuration findings; benchmark comparison; prioritised remediation with implementation steps; architecture recommendations |
| 9 | Identity / AD | forest & domain config; trusts & delegation; GPO & security settings; privileged accounts & Tier 0 exposure; Kerberos abuse paths; password policy & credential hygiene; service accounts & SPNs; attack path analysis standard user → domain admin | AD security assessment report with attack paths; privilege escalation analysis with visual path mapping; hardening recommendations; prioritised roadmap |
| 10 | Endpoint Security | OS hardening; patch mgmt; EPP deployment & config; local admin account mgmt; application whitelisting/execution control; USB & removable media; browser & email client settings; endpoint logging & visibility | assessment report with configuration findings; benchmark comparison; prioritised hardening recommendations; implementation guidance |
| 11 | Digital Forensics | computer/server forensics (Windows, Linux, macOS); mobile device forensics; email & communication analysis; log analysis & event correlation; file system & metadata; timeline reconstruction; data recovery & deleted files; cloud/SaaS evidence collection | forensic investigation report with findings & supporting evidence; event timeline reconstruction; technical artefact analysis; executive summary & conclusions; containment/improvement recommendations where applicable |
| 12 | Mobile Spyware Detection | iOS/Android filesystem forensic acquisition; Pegasus/Predator/Hermit/NSO-Cytrox-class detection; commercial stalkerware (FlexiSPY, mSpy, Cocospy); MDM profile & enterprise certificate inspection; network traffic & app permission audit; jailbreak/root & exploit artefacts; SMS & messaging link forensics | definitive assessment of compromise status; forensic report with evidence & indicators; tool identification where possible; timeline of suspected surveillance; remediation & hardening guidance; ongoing monitoring suggestions |
| 13 | DFIR | rapid forensic triage & evidence collection; scope determination; attacker activity reconstruction & timeline; containment guidance & eradication support; malware & artefact analysis; root cause identification; recovery guidance; stakeholder communication support | incident investigation report; complete attacker timeline; scope assessment of affected systems and data; root cause analysis; containment & recovery recommendations; post-incident improvements |
| 14 | Incident Response | initial assessment & triage; containment strategy; forensic evidence collection; breach scope determination; affected data identification; persistence eradication; recovery planning; post-incident recommendations | IR report with timeline & findings; breach scope assessment; containment & eradication confirmation; recovery & restoration guidance; post-incident improvement recommendations |
| 15 | Compromise Assessment | endpoint telemetry & forensic artefacts; network traffic anomalies; authentication logs & access patterns; known TTPs; persistence & scheduled tasks; unusual process execution & services; IOCs from threat intel; email & communication artefacts | compromise assessment report; IOCs identified; threat hunting analysis & methodology documentation; detection improvement recommendations; **escalation support if active compromise is confirmed** |
| 16 | Malware Analysis | executables & compiled binaries; scripts & document-based malware; memory forensics & in-memory malware; network protocols & C2 infrastructure; persistence mechanisms; encryption & obfuscation; payload delivery & exploitation | malware analysis report with behavioural findings; technical IOCs (hashes, network indicators, registry artefacts); capability assessment & threat characterisation; detection & mitigation recommendations |
| 17 | Ransomware | readiness assessment & gap analysis; backup & recovery capability evaluation; active incident investigation; variant identification & analysis; encryption scope & impact determination; recovery planning & secure restoration; playbook & tabletop development; post-incident improvements | assessment reports (proactive); incident investigation reports (reactive); recovery & restoration guidance; response playbooks with decision frameworks |
| 18 | Threat Intelligence | external attack surface discovery & mapping; exposed asset identification (domains, IPs, services, cloud); leaked credential monitoring; dark web & underground forum monitoring; brand impersonation & phishing detection; threat actor tracking by industry; vulnerability intelligence & prioritisation | attack surface assessment report; exposed asset inventory & risk assessment; threat intelligence briefings; monitoring alerts & notifications; remediation recommendations |
| 19 | Security Operations / SIEM / SOC | secops maturity assessment; SIEM architecture & deployment review; log source coverage & data quality; detection rule development & tuning; alert triage process design; escalation & response procedures; SOC staffing/tooling/process; detection engineering & use case development | secops assessment report; detection coverage analysis & gap identification; SIEM optimisation recommendations; process & workflow improvement guidance; detection rule library or improvement recommendations |
| 20 | Red Teaming | objective-based attack simulation; realistic attack chain (initial access → impact); social engineering & phishing; physical security testing where applicable; detection & response capability assessment; purple team collaboration; post-engagement debrief & knowledge transfer | engagement report with complete attack narrative; **detection gap analysis showing what was and was not detected**; detection & response improvement recommendations; technical debrief; executive summary |
| 21 | Compliance / GRC / vCISO | compliance readiness & gap analysis; policy & procedure development; risk assessment & risk register management; framework alignment (ISO 27001, SOC 2, NIST); vendor & third-party risk; board & executive reporting; programme oversight & strategic direction; audit preparation & support | compliance gap analysis & roadmap; policy & procedure documentation; risk assessment reports & risk register; ongoing vCISO advisory & reporting; board-ready security reports and metrics |

### 6.1 Deliverable patterns visible across the table

Three deliverable shapes recur, and they predict the report architecture exactly:

1. **Executive summary** — present in 13 of 21. Always paired with a technical body. Confirms a two-audience report model.
2. **Prioritised remediation / roadmap** — present in 16 of 21. Confirms remediation is a structured object (not prose) and must be exportable and trackable to retest.
3. **Evidence-backed findings** — VAPT ("evidence of exploitation and proof-of-concept"), Audits ("findings, evidence, and risk ratings"), App Sec ("evidence and reproduction steps"), Forensics ("supporting evidence"), Malware ("technical indicators"). Confirms the Finding→Evidence link is mandatory, matching the "evidence over assumption" principle.

Only two services promise **retest** explicitly (VAPT, Web/API). Whether retest is standard across all testing services is **Needs Confirmation**.
Only one service promises **escalation** explicitly (Compromise Assessment: "Escalation support if active compromise is confirmed"). That is a runbook decision point with a defined branch into an Incident Response engagement.

### 6.2 The service adjacency graph ("Related Services")

Observed edges, which the platform should use to suggest scope expansion and child engagements:

```
VAPT ↔ Network Security, App Security, Cloud Security, Red Team
App Security ↔ Mobile App Security, VAPT, Cloud Security
Cloud Security ↔ Identity Security, VAPT, Security Audits
Identity Security ↔ Endpoint Security, VAPT, Compromise Assessment
Endpoint Security ↔ Identity Security, Network Security, Compromise Assessment
Network Security ↔ VAPT, Cloud Security, Endpoint Security
Digital Forensics ↔ DFIR, Incident Response, Malware Analysis, Compromise Assessment
DFIR ↔ Digital Forensics, Incident Response, Compromise Assessment, Malware Analysis, Ransomware
Incident Response ↔ DFIR, Digital Forensics, Compromise Assessment, Ransomware
Compromise Assessment ↔ DFIR, Threat Intelligence, Malware Analysis, Security Operations
Threat Intelligence ↔ Compromise Assessment, Security Operations, Red Team
Red Team ↔ VAPT, Security Operations, Compromise Assessment
Security Audits ↔ Cybersecurity Consulting, Compliance, VAPT
Cybersecurity Consulting ↔ Security Audits, Compliance, VAPT, Cloud Security
Compliance ↔ Cybersecurity Consulting, Security Audits, Security Operations
Security Operations ↔ Threat Intelligence, Compromise Assessment, Cybersecurity Consulting
```

Note the graph is almost perfectly clustered into three components matching the three pillars, with **Malware Analysis** acting as a service that is nearly always reached *from inside another engagement* rather than sold alone. That is strong evidence for the **child engagement** concept in the data model.
