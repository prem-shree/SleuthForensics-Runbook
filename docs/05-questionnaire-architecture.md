# 05 — Client Information & Questionnaire Architecture

> **Status — DRAFT / NEEDS SME VALIDATION.** Per Rule 1 of [`17-governing-constraints.md`](17-governing-constraints.md), nothing in this document is
> confirmed Sleuth practice. Procedures, tools, legal requirements and operational rules here are
> proposals for SME review, not internal SOP. Content drawn from the public website is
> `SITE-SUGGESTED` and carries no authority over internal method (Rule 6). Gaps are named rather
> than filled (Rule 2). Validation vocabulary: [`18-content-provenance-and-validation.md`](18-content-provenance-and-validation.md).
>
> **Rule 4 applies throughout.** Questions establish *whether* access material exists and
> *how it will be delivered* — never what it is.


> The brief: *"The platform must not simply tell consultants what technical work to perform. It must also tell them what to ask the client."*

This is the part most consultancies keep in someone's head, and it is where engagements are most often damaged before any technical work begins. A question not asked at intake becomes a limitation in the report.

---

## 1. Questionnaires are composed, not written 21 times

Same principle as runbooks:

```
Questionnaire (engagement type)
  =  Universal block        (every engagement — 1 definition)
   +  Archetype block       (A1 | A2 | A3 | A4 — 4 definitions)
   +  Service block         (the specific questions — 41 definitions)
   +  Context blocks        (triggered by earlier answers — 9 definitions)
```

Roughly 40% of any questionnaire is inherited. More importantly, an answer in an early block **changes which later blocks appear** — the questionnaire is a conditional instrument, not a static form.

### 1.1 Answers are structured, and structure is the point

Every answer carries:

| Field | Why it exists |
|---|---|
| `value` (typed: text, number, date, enum, multi-select, asset list, file) | So it can drive logic, not just be read |
| `respondent` | Who at the client said this |
| `answered_at` | When — a scope answer from six weeks ago may be stale |
| `source` | Stated by client · Observed by Sleuth · Inferred · Document |
| `confidence` | High · Medium · Low · **Unverified** |
| `verified_by` / `verified_at` | Set when Sleuth independently confirms it |
| `unavailable_reason` | Required if a mandatory question is unanswered |

The `source` and `confidence` fields do real work. "Client stated the backups are isolated" and "Sleuth verified the backups are isolated" are different facts, and in a ransomware engagement the difference can be the whole recovery plan. The report's limitations section is generated in part from unverified answers, which means honest reporting becomes the path of least resistance rather than an act of discipline.

### 1.2 A question can block a gate

Questions are flagged `blocking` when work genuinely cannot proceed without them. Unanswered blocking questions hold the **Readiness Gate**. This is how "we never got the asset list" stops being discovered on day one of testing.

---

## 2. The universal block (every engagement)

**Client & context** — legal entity name or individual name · client type (Organisation / Individual) · sector (9-value list from the industries page) · size · locations · regulated status and which regulator.
**Authority** — who is commissioning this and in what role · are they authorised to commission it · who signs the authorisation · who receives the report · is anyone excluded from receiving it.
**Objective** — what decision will this work inform · what does success look like · what question must be answered.
**Constraints** — deadline and what drives it (audit, board, regulator, litigation, incident) · budget envelope · blackout periods · internal parties who must not be informed and why.
**Confidentiality** — classification · third parties permitted to see the output · any legal proceedings current or anticipated (→ triggers **Legal Hold** context block).
**Logistics** — primary contact and hours · escalation contact and out-of-hours number · site access requirements · NDA status · preferred communication channel for sensitive material.

## 3. Archetype blocks

**A1 — Assessment & Advisory**
Which framework and why · prior assessments and their findings · what has changed since · document availability · who can be interviewed and their availability · is this for a certification and what is its deadline · known gaps the client already accepts · appetite for a hard assessment vs a confirmatory one.

**A2 — Authorised Technical Testing**
Complete asset inventory · asset ownership (client-owned / third-party hosted / SaaS) · production vs staging per asset · testing window with dates and hours · explicitly out-of-scope assets and why · credentials and test accounts (existence and delivery channel — **not the credentials themselves**, see `13-security-architecture.md`) · authenticated or unauthenticated · WAF/IPS present and whether it will be tuned or allow-listed · fragile systems that must not be touched · who to call if something breaks, 24/7 · is the blue team informed (no for red team) · permitted intrusiveness (identify only / validate safely / exploit) · data-handling rule if live customer data is encountered.

**A3 — Investigation & Response**
What happened, in the client's own words · when did it occur, when was it discovered, how · who discovered it · is it ongoing right now · what has already been done (this is critical and frequently under-asked: reboots, reimaging, AV cleaning, password resets, system rebuilds all destroy evidence) · who has handled the systems since · what systems and devices are involved · what evidence exists and where · what logs exist and what is their retention · who owns the devices and data · what authority exists for examination · is law enforcement or a regulator involved · is litigation current or anticipated · what is the investigation objective · what must be decided as a result · who must not know about this investigation.

**A4 — Continuous & Readiness**
What is the monitored perimeter · known and accepted exposures · alert routing and who acts on them · cycle frequency · escalation thresholds · what triggers a move from monitoring to incident · who receives the cycle report · re-authorisation cadence.

---

## 4. Worked examples

### 4.1 VAPT — External Infrastructure (`SF-SEC-VAP-EXT`)
Universal + A2 + service block:

**Targets** — IP ranges in CIDR · domains and subdomains · whether subdomain enumeration may expand scope or scope is fixed · cloud-hosted assets and provider (AWS/Azure/GCP) · shared hosting present · CDN/WAF in front and which.
**Ownership verification** *(blocking)* — can the client confirm ownership of every listed IP and domain · for third-party hosted assets, is provider authorisation obtained *(blocking → Authorisation Gate)*.
**Testing parameters** — window start/end with timezone · permitted intensity · denial-of-service testing permitted (default **no**) · social engineering in scope (default **no**) · physical in scope (default **no**) · source IPs to allow-list or should testing be blind.
**Applications behind the perimeter** — login portals present · registration/self-service functions · payment functions · file upload endpoints · rate limiting present.
**Operational safety** — legacy or unsupported systems in scope · systems with known stability problems · maintenance windows to avoid · monitoring that will alarm · who is informed.
**Deliverable expectations** — report audience · format · is a specific compliance framework being satisfied and which · retest expected and when · certificate/attestation letter required *(**Needs Confirmation:** does Sleuth issue these?)*.

### 4.2 Digital Forensics — Examination (`SF-INV-DFX-EXAM`)
Universal + A3 + service block. The brief's own list, made operational:

**The matter** — describe what is alleged or suspected · what period does it concern · who are the subjects of the examination · are the subjects aware · what is the specific question the examination must answer.
**Authority** *(blocking)* — who owns the devices · who owns the data on them · is there an employment policy or consent covering examination · has legal counsel been consulted · is there a court order or regulatory direction · is this for internal decision-making, disciplinary action, or proceedings.
**Devices and evidence** — list every device with make/model/identifier · current physical location · powered on or off *(drives the handling decision tree)* · encrypted and is the key available · in whose possession since the relevant period.
**Prior handling** *(critical)* — has anyone accessed, used, powered on, imaged, "cleaned", reset or reimaged any device since the events · who, when, and what did they do · has any third party already examined it · has any evidence already been collected and how.
**Available evidence** — email/collaboration platform and retention · logs and retention · backups and their range · cloud/SaaS accounts in scope · CCTV or physical access records · mobile devices.
**Chain of custody to date** — who has held each item and when · was custody documented · how will items be transferred to Sleuth.
**Output** — is a formal expert report required · will findings be relied on in proceedings *(**Needs Confirmation:** does Sleuth provide expert testimony or issue electronic-record certificates? This changes the report format materially)* · who receives the report · is a privilege claim asserted over the work.

### 4.3 Ransomware — Active Investigation (`SF-RES-RAN-INV`)
Universal + A3 + Emergency context + service block. Sequenced for speed: the first six are asked in the first phone call.

**Immediate (first contact)** *(all blocking)* — when was encryption first observed · is encryption still spreading right now · what has been isolated so far · are domain controllers affected · are backups affected · is anyone already engaged (insurer, law enforcement, another responder).
**Scope** — which systems are encrypted · which are still operational · which are business-critical and in what order · is the network segmented and did it hold · are OT/ICS systems affected *(→ OT Safety context)*.
**Backups** — do backups exist · date of last known-good · are they isolated or were they network-reachable · have they been tested for restoration · has anyone attempted a restore already.
**The actor** — is there a ransom note and what does it say · was contact made by the attacker · **has anyone at the client communicated with them** · is a named group claiming it · is there a leak site posting.
**Data theft** — evidence of exfiltration · unusual outbound transfer volumes · what data classes were on affected systems · personal data of individuals involved · **any regulatory notification clock already running** *(**Needs Confirmation:** which notification obligations apply to Sleuth's clients — for confirmation with counsel, not assumption)*.
**Preservation** *(blocking)* — have any systems been reimaged, rebuilt or wiped · are affected systems preserved or has recovery already started · are volatile memory and logs still available.
**Coordination** — who is the incident commander on the client side · who is making decisions out of hours · is cyber insurance involved and has the insurer been notified · are legal counsel and PR engaged · has anyone communicated externally.
**Decision context** — is the client considering payment *(**Needs Confirmation:** Sleuth's policy and whether the platform should record this at all — it is legally sensitive in several jurisdictions and the site takes no position)*.

### 4.4 Mobile Spyware Detection (`SF-INV-SPY-EXAM`) — the individual-client case

Included to show the model handling a client type that is not a company at all.

**Safety first** *(before any other question)* — the website's own instruction becomes the first procedure: *"If you suspect your phone is being monitored, do not discuss it on that device."* The questionnaire opens with establishing a safe communication channel, off the suspect device. No other question is asked on that channel until this is done.
**Consent and ownership** *(blocking)* — who owns the device · who pays the account · is it enrolled in an employer MDM · is the person requesting the examination the user of the device · if not, what authority exists · **is there any indication of a domestic or intimate-partner context** *(changes handling, disclosure and the safety plan; the site explicitly names domestic surveillance and stalkerware)*.
**Observations** — what behaviours prompted concern · when did they start · battery/heat/data anomalies · unexpected messages or links received · who might have had physical access to the device and when · has the device ever been out of the person's possession.
**Device facts** — make, model, OS version · passcode/biometrics · jailbroken or rooted to the owner's knowledge · MDM profiles or enterprise certificates installed · backups available and where.
**Risk profile** — role or circumstance that could attract targeting (the site names executives, board members, journalists, activists, legal professionals, high-net-worth individuals) · travel to high-risk regions · prior incidents.
**Outcome** — what will the person do with the result · is a report needed for anyone else and whom · do they need a device-hardening or device-replacement plan · is there a personal-safety concern requiring a referral *(**Needs Confirmation:** Sleuth's safeguarding policy for individual clients in domestic-abuse contexts)*.

---

## 5. Questionnaire index — all 21 services

Each entry lists the **service-specific block** only; the universal and archetype blocks are inherited.

| # | Service | Service-specific question areas |
|---|---|---|
| 1 | Cybersecurity Consulting | Business objectives & strategy horizon · current security function & headcount · existing budget & spend · prior assessments · board reporting today · risk appetite · planned transformation (cloud migration, M&A, new markets) · what decision this advice supports |
| 2 | Security Audits | Target framework & version · certification deadline · prior audit findings & closure status · policy set maturity · control owners · documentation availability · in-scope business units & locations · sampling expectations |
| 3 | VAPT | §4.1 |
| 4 | Network Security | Topology diagrams available & current · site count · segmentation intent vs reality · firewall vendors & rule volume · VPN & remote access model · wireless estate · legacy protocols knowingly in use · management network separation |
| 5 | Web App & API Security | Application inventory & business criticality · technology stack · authentication model (SSO/MFA/social) · role matrix & test accounts per role · API style (REST/GraphQL/SOAP) & documentation availability · multi-tenancy · payment & PII flows · rate limiting · staging fidelity to production |
| 6 | OT Security | Sites & processes · OT vendors & system types (SCADA/PLC/DCS/HMI) · asset inventory existence & confidence · Purdue-level architecture · IT/OT interconnects · remote vendor access · patching constraints & safety approvals · **safety-critical processes that must never be interrupted** · engineer availability to accompany · regulatory context |
| 7 | Mobile App Security | Platforms & minimum OS versions · distribution (store/enterprise/MDM) · build availability (IPA/APK) & source access · backend environment for testing · test devices — physical or emulator · jailbreak/root detection present · certificate pinning present · offline functionality · SDK & third-party library inventory |
| 8 | Cloud Security | Providers & account/subscription/project inventory · landing zone or organic growth · IaC in use & repository access · read-only assessment role availability *(blocking)* · CSPM tooling present · multi-tenancy model · data residency requirements · serverless & container platforms · secrets management approach |
| 9 | Identity & AD | Forest/domain/OU structure · user & privileged account counts · Entra ID / hybrid identity · trust relationships & to whom · Tier model in place · PAM solution present · service account inventory & rotation practice · prior credential incidents · domain admin count |
| 10 | Endpoint Security | Estate size & OS mix · management platform (Intune/SCCM/Jamf) · EPP/EDR vendor & coverage · hardening baseline & source (CIS/vendor/custom) · local admin prevalence · application control present · USB policy · patch cadence & exceptions · endpoint log forwarding |
| 11 | Digital Forensics | §4.2 |
| 12 | Mobile Spyware | §4.4 |
| 13 | DFIR | Incident narrative & current status · detection source · containment already performed · affected system inventory & criticality · EDR/SIEM present & retention · network telemetry available · account compromise indicators · business impact & operational priority · stakeholder communication state |
| 14 | Incident Response | As DFIR, plus: third-party notification received & from whom · data classes potentially affected · **notification clocks the client believes are running** · insurer & counsel engagement · prior incidents this quarter · internal communications sent so far |
| 15 | Compromise Assessment | Why now (suspicion, M&A, periodic, post-incident) · specific concerns or named threats · estate scope & agent deployment feasibility · telemetry sources & retention · prior hunts & findings · acceptable business disruption · what happens if compromise **is** confirmed *(pre-agreed escalation — do not negotiate this mid-incident)* |
| 16 | Malware Analysis | Sample provenance & how obtained · **safe transfer channel** · is it live in the environment right now · affected systems · desired output (IOCs / behaviour / attribution / decryption feasibility) · sharing permission (VirusTotal, vendors, CERT) *(blocking — uploading client malware is a disclosure)* · analysis depth required · urgency driver |
| 17 | Ransomware — Investigation | §4.3 |
| 17 | Ransomware — Readiness | Backup architecture & isolation · restore testing history & RTO/RPO targets · segmentation · EDR coverage · privileged access controls · existing playbook & last exercise · crisis communication plan · insurance · critical-system dependency mapping · prior incidents |
| 18 | Threat Intelligence | Known domains, brands & IP ranges · subsidiaries & acquisitions · executive names to monitor *(consent required)* · sectors & regions of concern · known threat actors of concern · existing intel feeds · alert routing & tolerance · monitoring frequency · takedown expectations *(**Needs Confirmation:** does Sleuth perform takedowns?)* |
| 19 | Security Operations | SOC model (in-house/MSSP/hybrid) · staffing & shift coverage · SIEM platform & licensing model · log sources onboarded vs expected · daily alert volume & false-positive rate · MTTD/MTTR if measured · detection content source · runbook maturity · escalation path · tooling (SOAR/EDR/NDR) |
| 20 | Red Teaming | Defined objectives ("flags") · assumed starting position (external/assumed breach) · blue team awareness *(usually **no**)* · **deconfliction contacts & procedure** *(blocking)* · permitted TTPs & explicit prohibitions · social engineering permitted & pretext approval process · physical permitted & site details · duration · legal sign-off for people-targeting *(blocking)* · evidence of authorisation testers must carry on site · what triggers an immediate stop |
| 21 | Compliance / GRC | Target frameworks & deadlines · current certification state · auditor engaged & who · policy set maturity · risk register exists & its format · risk appetite statement · vendor inventory & tiering · board reporting cadence · for vCISO: time commitment, decision authority, reporting line, first 90-day priorities |

---

## 6. How the questionnaire reaches the client

Three modes, with a deliberate Phase 1 recommendation:

| Mode | How | Phase |
|---|---|---|
| **Consultant-mediated** | Consultant fills it during a call or workshop; the instrument is the interview guide | **Phase 1 — recommended start** |
| **Exported form** | Structured export sent by an existing secure channel; answers keyed back in | Phase 2 |
| **Secure client link** | Time-limited, single-questionnaire link; client answers directly | Phase 7, and only after security review |

Starting consultant-mediated is the right call. It requires no external attack surface, it keeps a human judging answer quality and confidence, and it reflects how these conversations actually go — a client under incident pressure does not fill in forms. The client-link mode is genuinely useful later for long asset inventories, but it is an internet-facing endpoint on a platform holding investigation data, and that deserves its own review rather than a Phase 1 shortcut. See Decision D3 in `15-assumptions-and-open-questions.md`.
