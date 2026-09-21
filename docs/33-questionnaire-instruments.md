# 33 — Questionnaire Instruments

> **Status — Draft / Needs SME Validation.** Question *wording* is `PROPOSED`; the underlying
> information needs are `INDUSTRY-PRACTICE` and `SITE-SUGGESTED`.
> Implements `05-questionnaire-architecture.md` with actual instruments.

**Composition:** `Universal (30) + Archetype (17–19) + Service (10–18) + Context blocks (conditional)`.
Roughly 60% of any instrument is inherited — written once here, improved once.

**Legend:** **B** = blocking (holds the Readiness Gate) · **V** = must be Sleuth-verified, not
client-stated · **→** triggers a context module · `‹PH-nn›` = placeholder, see `38`.

> **Rule 4 throughout.** Questions establish *whether* access material exists and *how it will be
> delivered*. Never what it is. There is no question anywhere in this document whose answer is a
> credential.

---

## 1. Universal block — every engagement

### U1 · Client & context
| Question | Type | Flags |
|---|---|---|
| Legal entity name, or individual's name | text | required |
| Is the client an organisation or an individual? | enum | → Individual Client |
| Sector | enum *(9 values)* | → Regulated Sector |
| Subject to sector regulation? Which regulator? | multi | → Regulated Sector |
| Approximate size — headcount and turnover band | enum | |
| Locations in scope | list | |

### U2 · Authority
| Question | Type | Flags |
|---|---|---|
| Who is commissioning this work? Name and role | text | **B** |
| Are they authorised to commission it on the organisation's behalf? | bool | **B** |
| Who will sign the engagement authorisation? Name and role | text | **B** |
| **How has that person's authority to authorise been verified?** | text | **B V** |
| Who receives the final report? | contacts | required |
| **Is anyone who would normally receive it to be excluded — and why?** | contacts | sets exclusion flags |

> The last question is asked of every client, not only investigations. It costs one line and it is
> the control that stops a report on an internal matter reaching its own subject.

### U3 · Objective
| Question | Type | Flags |
|---|---|---|
| What decision will this work inform? | text | required |
| What question must we answer for you? | text | required |
| What does a good outcome look like? | text | |

### U4 · Constraints
| Question | Type | Flags |
|---|---|---|
| Is there a deadline, and what drives it? | text + enum *(audit · board · regulator · litigation · incident · none)* | |
| Blackout periods or dates to avoid | list | |
| Budget envelope we should design to | text | |
| Internal parties who must not be informed, and why | text | sets confidentiality handling |

### U5 · Confidentiality & legal
| Question | Type | Flags |
|---|---|---|
| Classification applying to this work | enum | required |
| Third parties permitted to see the output | list | |
| Current or anticipated legal proceedings connected to this? | bool | → Legal Hold |
| Is privilege being asserted over this work? | bool | |
| Will any data or evidence leave India? | bool | → Cross-Border |

### U6 · Logistics
| Question | Type | Flags |
|---|---|---|
| Primary contact, role, working hours | contact | required |
| Escalation contact and out-of-hours number | contact | **B** |
| **Has that out-of-hours number been tested and confirmed reachable?** | bool | **B V** |
| Preferred secure channel for sensitive material | enum | required |
| Site access requirements | text | |
| NDA status | enum | **B** |

---

## 2. Archetype blocks

### A1 — Assessment & Advisory (9)
Which framework or benchmark, and why that one? · Is this driven by certification, an audit, or an
internal need? · Previous assessment — when, by whom, what did it find? · What has changed since? ·
Which documents can you provide, and how current are they? · Who are the control owners we need to
interview, and are they available *(dates)*? · Gaps you already know about and have accepted ·
**Do you want a confirmatory assessment or a hard one?** · What target state is realistic for you —
is "fully mature everywhere" the goal, or not?

> The eighth question is asked deliberately and early. Some clients want a document that says they
> are fine. Knowing that at scoping is better than discovering it at delivery.

### A2 — Authorised Technical Testing (19)
| Question | Type | Flags |
|---|---|---|
| Complete asset inventory | asset list | **B** |
| Per asset: environment — production / staging / dev / unknown | enum | **B** → Production |
| Per asset: ownership — client / third-party hosted / SaaS | enum | **B** → Third-Party |
| **Per asset: can you confirm you own or control it?** | bool | **B V** |
| Assets explicitly **out** of scope, and why | list | required |
| Testing window — dates, hours, **timezone** | window | **B** |
| Fragile systems that must not be touched | list | |
| Maintenance windows to avoid | list | |
| Do test accounts exist for each required role? | bool per role | **B** |
| **How will access material be delivered to us?** *(channel only)* | enum | **B** |
| WAF/IPS in front — will it be tuned or allow-listed? | enum | |
| Blind testing, or allow-list our source IPs? | enum | |
| Is denial-of-service testing permitted? | bool | **default NO** |
| **Permitted intrusiveness level** | enum L1/L2/L3 | **B** · default **L2** *(`32` §1)* |
| Who do we call 24/7 if something breaks? | contact | **B** |
| Is your security team informed this is happening? | bool | *(no for red team)* |
| What should we do if we encounter live customer personal data? | text | required |
| Monitoring that will alarm, and who is informed | text | |
| Is a specific compliance requirement being satisfied? Which? | text | |

### A3 — Investigation & Response (17)
| Question | Type | Flags |
|---|---|---|
| In your own words, what happened? | text | required |
| When did it occur? When was it discovered? | datetime ×2 | required |
| How was it discovered? | text | required |
| **Is it still ongoing right now?** | bool | **B** |
| **What has already been done?** *(reboots · reimaging · AV cleaning · password resets · rebuilds · restores)* | multi + text | **B** |
| Who has handled the affected systems since, and what did they do? | text | **B** |
| Which systems and devices are involved? | list | **B** |
| What evidence exists, and where is it now? | list | **B** |
| What logs exist, and what is their retention window? | list | required |
| **Who owns the devices? Who owns the data on them?** | text | **B** |
| **What authority exists for us to examine them?** | text | **B** |
| Is law enforcement or a regulator involved? | bool + text | → Regulated |
| Is litigation current or anticipated? | bool | → Legal Hold |
| What is the objective of this investigation? | text | required |
| What must you decide as a result? | text | required |
| **Who must not know this investigation is happening?** | list | sets exclusions |
| Who is coordinating on your side, including out of hours? | contact | **B** |

> The fifth question is the one most often skipped and the one that most often decides whether an
> investigation can succeed. A machine that was reimaged on Tuesday has no answers left in it.

### A4 — Continuous & Readiness (7)
What is the monitored perimeter? · Known exposures you already accept · Where should alerts go, and
who acts on them? · Desired cycle frequency · **What threshold moves something from monitoring to an
incident?** *(agreed now, never negotiated mid-incident)* · Who receives the cycle report? ·
How often should the standing authorisation be re-confirmed?

---

## 3. Service blocks — all 20 engagement types

### A1

**`SF-A1-SPA` Security Programme & Maturity Assessment (10)**
Business objectives and planning horizon · security function structure, reporting line, headcount ·
skills and gaps in the team · current security budget and where it goes · board reporting today —
format and cadence · stated risk appetite, if documented · planned change *(cloud migration, M&A, new
markets, new products)* · prior incidents that shaped current posture · which domains matter most to
you · what decision this assessment supports.

**`SF-A1-CRA` Compliance Readiness Assessment (11)**
Target framework and version · **certification deadline and what drives it** *(B)* · current
certification state · auditor engaged, and who · scope of applicability — which entities, systems,
locations · policy set maturity · does a risk register exist, and in what format · documented risk
appetite · vendor inventory and tiering · who owns each control · prior audit findings and their
closure status.

**`SF-A1-TCR` Technical Configuration Review (12 + per pack)**
Which domain packs are in scope · estate scale per pack · platforms and versions · management
tooling · existing hardening baseline and its source · **read-only assessment access available?**
*(B)* · how will configuration be extracted · known deviations you have accepted and why · technical
contact available during extraction *(B)* · change-freeze periods · is any pack's estate mid-migration ·
who owns remediation per pack.
*Per pack:* Cloud — providers, account/subscription/project inventory, IaC, residency requirements ·
Identity — forest/domain/OU structure, hybrid identity, trusts, PAM · Endpoint — OS mix, management
platform, EPP/EDR vendor, local admin prevalence · Network — topology diagrams and currency, site
count, firewall vendors, VPN model, wireless estate.

**`SF-A1-OTA` OT/ICS Security Assessment (14)**
Sites and the processes they run · OT vendors and system types *(SCADA · PLC · DCS · HMI)* · does an
asset inventory exist, and how confident are you in it · Purdue-level architecture, if mapped ·
IT/OT interconnects · remote and vendor access paths · patching constraints and the safety approval
process · **safety-critical processes that must never be interrupted** *(B)* · **who is the plant or
operations safety authority** *(B)* · engineer availability to accompany us *(B)* · PPE and induction
requirements · planned maintenance windows · regulatory context · prior OT incidents.

**`SF-A1-SOA` Security Operations & Detection Assessment (12)**
SOC model — in-house, MSSP, hybrid · staffing and shift coverage · SIEM platform and licensing model ·
log sources onboarded versus expected · daily alert volume · false-positive rate, if measured ·
MTTD/MTTR, if measured · detection content source — vendor, community, in-house · runbook maturity ·
escalation path · tooling *(SOAR · EDR · NDR)* · **is detection-validation testing in scope?**
*(B — carries a Letter of Authorisation requirement, `32` §1)*.

**`SF-A1-IRA` Incident Readiness Assessment & Exercise (12)**
Backup architecture · **are backups isolated from the production domain?** · restore testing history —
when, at what scale · RTO and RPO targets, and whether they have been met in a real test ·
segmentation and expected blast radius · EDR coverage · privileged access controls · existing playbook
and date last exercised · crisis communication plan · **who decides, out of hours** · cyber insurance
and notification requirements · critical-system dependency mapping.

### A2

**`SF-A2-IPT` Infrastructure Penetration Test (13)**
IP ranges in CIDR · domains and subdomains · **may enumeration expand scope, or is scope fixed?** ·
cloud-hosted assets and provider · shared hosting present · CDN or WAF in front, and which · legacy
or unsupported systems in scope · systems with known stability problems · *(internal mode)* network
access method and starting position · *(internal)* site access and escort · *(wireless)* site
addresses and **the geographic boundary of permitted testing** *(B)* · *(wireless)* neighbouring
tenants · mode required — external / internal / wireless / non-exploitative VA *(B)*.

**`SF-A2-WAT` Web Application & API Security Test (12)**
Application inventory and business criticality · technology stack · authentication model *(SSO · MFA ·
social)* · **role matrix, and a test account per role** *(B)* · API style *(REST · GraphQL · SOAP)* ·
API documentation or collection available *(B)* · multi-tenancy model · payment flows · personal-data
flows · rate limiting present · **is the test environment staging or production?** *(B)* · if staging,
how faithful is it to production.

**`SF-A2-MAT` Mobile Application Security Test (11)**
Platforms and minimum OS versions · distribution — store, enterprise, MDM · **build available
(IPA/APK)?** *(B)* · is source code provided · backend environment for testing, and is it production
*(B)* · test devices — who supplies them · **may devices be jailbroken/rooted?** *(B)* · jailbreak or
root detection present · certificate pinning present · offline functionality · SDK and third-party
library inventory.

**`SF-A2-CPT` Cloud Penetration Test (11)**
Providers and account/subscription/project inventory *(B)* · landing zone or organic growth ·
IaC in use, and repository access · **has the provider's testing policy been checked, and is
notification required?** *(B)* · multi-tenancy model · data residency requirements · production
versus non-production per account · existing CSPM tooling · shared-responsibility boundary as you
understand it · serverless and container platforms · secrets management approach.

**`SF-A2-ATP` Identity & Attack Path Assessment (11)**
Forest, domain and OU structure · user and privileged account counts · Entra ID or hybrid identity ·
trust relationships, **and to whom** *(B — trusts routinely lead somewhere the client forgot)* ·
Tier model in place · PAM solution present · service account inventory and rotation practice ·
domain admin count · prior credential incidents · **standard user account for the starting position**
*(B)* · **is path validation to domain admin authorised?** *(B — Level 3, `32` §1)*.

**`SF-A2-RED` Red Team & Adversary Simulation (14)**
Defined objectives — the flags *(B)* · assumed starting position · **is the blue team aware?**
*(B — usually no)* · **deconfliction contacts and procedure** *(B)* · has the deconfliction number
been tested *(B V)* · permitted techniques, narrowed from `32` §5 *(B)* · explicit prohibitions ·
is social engineering in scope · is physical entry in scope, and at which sites · duration ·
**legal sign-off where people are targeted** *(B)* · what evidence of authorisation must testers
carry on site · **what triggers an immediate stop** · purple-team mode or full red team · who
receives the debrief.

**`SF-A2-SES` Social Engineering Simulation (11)**
**Legal approval obtained** *(B)* · **HR approval obtained** *(B)* · target population — roles or
groups · **individuals to exclude, and the reason** *(B)* · pretext themes acceptable and
unacceptable · channels in scope — email, phone, SMS, physical · campaign timing and volume ·
**is any staff member in sensitive circumstances we should know about?** · how should we handle a
target who becomes distressed · what awareness follow-up do you want · who receives aggregate results
*(no individual is ever named — `32` §4)*.

### A3

**`SF-A3-IRE` Incident Response (14 — first six in the opening call)**
**When was it first observed?** · **Is it spreading right now?** · **What has been isolated?** ·
**Are domain controllers affected?** · **Are backups affected?** · **Is anyone else already engaged
— insurer, law enforcement, another responder?** — then: affected system inventory and criticality ·
EDR/SIEM present and retention · network telemetry available · data classes on affected systems ·
**notification clocks you believe are running** · insurer and counsel engagement · incident commander
and out-of-hours decision authority · has anything been communicated externally yet.
*Ransomware module adds:* is there a ransom note, what does it say · **has anyone at your organisation
communicated with the attacker?** · is a named group claiming it · is there a leak-site posting ·
evidence of unusual outbound transfer · date of last known-good backup · **are backups isolated or
were they network-reachable** · has a restore been attempted.
*BEC module adds:* mailbox rules and forwarding found · MFA in place · OAuth grants reviewed ·
financial transactions attempted or completed.
*Insider module adds:* **is the subject still employed and still has access** · HR involvement ·
**who must not know**.

**`SF-A3-DFE` Digital Forensic Examination (15)**
**The precise questions the examination must answer** *(B — agreed in writing, `DFE-01`)* · the matter
and the period it concerns · subjects of the examination · **are the subjects aware?** · employment
policy or consent covering examination *(B)* · has counsel been consulted · court order or regulatory
direction · device list — make, model, identifier · current physical location · **powered on or off**
*(B)* · encryption present and key availability *(B)* · possession history · **prior handling by
anyone** *(B)* · available collateral evidence — email, logs, backups, CCTV · **will findings be
relied on in proceedings?** *(B — see `31` §3.2)*.

**`SF-A3-SPY` Mobile Device Spyware Examination (16)**
**Is there a safe way to contact you that is not this device?** *(B — asked first, `SPY-01`)* ·
**who owns the device? who pays the account?** *(B)* · is it enrolled in an employer MDM *(B)* ·
are you the user of this device *(B)* · **is there a domestic or intimate-partner situation involved?**
*(B — asked neutrally, `32` §3)* · what behaviours prompted your concern · when did they start ·
battery, heat or data anomalies · unexpected messages or links received · **who has had physical
access to the device, and when** · has the device been out of your possession · make, model, OS
version · jailbroken or rooted to your knowledge · MDM profiles or enterprise certificates you know
of · backups available and where · role or circumstance that could attract targeting · **is there a
personal safety concern we should know about?** *(B)* · what will you do with the result.

**`SF-A3-CTH` Compromise Assessment & Threat Hunt (10)**
Why now — suspicion, M&A, periodic, post-incident · specific concerns or named threats · estate scope ·
**can collection agents be deployed, and by whom** *(B)* · telemetry sources and retention ·
prior hunts and what they found · acceptable business disruption · **what happens if we confirm
compromise — agreed now** *(B)* · who is notified, and how fast · coverage target you expect.

**`SF-A3-MAL` Malware Analysis (10)**
Sample provenance — where and how obtained *(B)* · **safe transfer channel** *(B)* · is it live in
the environment right now *(B)* · affected systems · desired output — IOCs, behaviour, attribution,
decryption feasibility · **may the sample be shared with third-party services?** *(B — `MAL-03`;
uploading is a disclosure, and can alert a targeted adversary)* · analysis depth required · urgency
driver · is this a child of an existing engagement · any known packing or protection.

### A4

**`SF-A4-ASM` Attack Surface & Threat Intelligence Monitoring (11)**
Known domains, brands and IP ranges *(B)* · subsidiaries and acquisitions · **can you confirm
ownership of each monitored asset?** *(B V)* · executive names to monitor · **have those individuals
consented?** *(B)* · sectors and regions of concern · known threat actors of concern · existing
intelligence feeds · alert routing and tolerance · expected cycle frequency · what you want us to do
about brand impersonation *(we report and advise; we do not pursue takedowns — `32` §8)*.

**`SF-A4-VCI` vCISO Retainer (11)**
Time commitment expected · **decision authority granted — what may the vCISO decide alone?** *(B)* ·
reporting line · board cadence and format · existing security function and maturity · current
initiatives and budget · documented risk appetite · **what do you expect the vCISO to own versus
advise on?** *(B — the most common source of friction)* · first-90-days priorities · **does Sleuth
provide other services to you?** *(B → independence declaration, `32` §7)* · who is the independent
authoriser for any Sleuth testing work.

---

## 4. Context block questions

| Context module | Adds |
|---|---|
| **Production Systems** | Change-window approval process · rollback capability · who authorises a change during testing · on-call contact during the window |
| **Third-Party Hosted** | Provider name · contract terms on testing · has authorisation been requested and granted · provider notification requirements |
| **OT / Safety-Critical** | Safety authority · engineer assignment · permitted activity list from the operations team · emergency stop procedure |
| **Individual Client** | Safe channel · consent · device and account ownership · safety considerations *(`32` §3)* |
| **Legal Hold** | Counsel contact · hold scope · preservation instruction issued · no-deletion confirmation |
| **Regulated Sector** | Regulator · notification obligations the client believes apply · reporting timelines · prior regulatory engagement |
| **Emergency** | Verbal authority given by whom · how identity was verified · scope of authority · ratification owner and deadline |
| **People-Targeting** | HR and legal approval · exclusions · welfare handling · debrief obligation |
| **Cross-Border** | Which jurisdictions · transfer basis · residency constraints · counsel review status |

---

## 5. Answer metadata — every answer, every instrument

`value` *(typed)* · `respondent` · `answered_at` · `source` *(client-stated · Sleuth-observed ·
inferred · document)* · `confidence` *(high · medium · low · **unverified**)* · `verified_by` ·
`verified_at` · `unavailable_reason` *(required if a mandatory question is unanswered)*.

**Unverified answers to `V`-flagged questions auto-seed the report's limitations section**
(`22` `RP-04`). "The client stated backups were isolated" and "Sleuth verified backups were isolated"
are different facts, and in a ransomware engagement the difference can be the whole recovery plan.

---

## 6. Counts

| Block | Questions |
|---|---|
| Universal | 30 |
| Archetype — A1 / A2 / A3 / A4 | 9 / 19 / 17 / 7 |
| Service blocks — 20 types | 234 |
| Incident-type modules *(IRE)* | 16 |
| Context blocks — 9 modules | 36 |
| **Total authored** | **368** |
| Inherited share of a typical instrument | **~55–60%** |

`SME-VALIDATED`: **0**. Wording is a copy-editing pass an SME should own; the *information needs*
are what matter for review.
