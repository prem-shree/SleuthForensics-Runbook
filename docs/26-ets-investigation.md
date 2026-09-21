# 26 — Engagement Type Specifications: A3 Investigation & Response

> **Status — Draft / Needs SME Validation.** Provenance: `PROPOSED` (structure), `INDUSTRY-PRACTICE`
> and `EXTERNAL-STANDARD` (method — NIST SP 800-61, ISO/IEC 27037, 27041–27043),
> `SITE-SUGGESTED` (scope items). Nothing is `SLEUTH-SUPPLIED` or validated.

**§1 derived** from `core.*` (`22`) + `arch.A3` (`23`). Only deltas and service-specific content below.

> **Every A3 engagement inherits:** recorded instructions and authority, the prior-handling enquiry,
> the un-overridable Custody Gate, analysis on working copies only, mandatory consideration of
> alternative explanations, conclusions stated with confidence, and evidence disposition as a
> Closure Gate condition.

---

# `SF-A3-IRE` — Incident Response

**Public services:** 13 DFIR · 14 Incident Response · 17 Ransomware (reactive half) · **Archetype:** A3
**Incident-type modules:** ransomware · business email compromise · data theft · insider · web/application compromise · unknown
**Usually:** emergency authorisation path

### §2 Service-specific procedures `[SERVICE]`

| ID | Procedure | Records |
|---|---|---|
| `IRE-01` | Emergency triage call — the first six questions, inside the first contact | Initial picture, urgency, immediate advice |
| `IRE-02` | **Immediate preservation instruction** — issued before anything else, because recovery destroys evidence | Instruction issued, to whom, at what time |
| `IRE-03` | Incident-type determination ⟪incident_module⟫ — provisional, revisable | Type selected, basis, **changes recorded with reasons** |
| `IRE-04` | Scope determination — which systems, accounts and data are affected | Affected inventory, confidence per item |
| `IRE-05` | Rapid forensic triage — targeted collection from priority systems | Triage collections, prioritisation basis |
| `IRE-06` | Initial access determination | Vector, evidence, confidence |
| `IRE-07` | Attacker activity reconstruction | Timeline of adversary actions |
| `IRE-08` | Persistence identification | Mechanisms found, locations |
| `IRE-09` | Lateral movement and privilege escalation reconstruction | Path, accounts used |
| `IRE-10` | Command and control identification | Infrastructure, protocols, IOCs |
| `IRE-11` | **Data access and exfiltration assessment** | Evidence of access vs evidence of exfiltration — stated separately |
| `IRE-12` | Containment advisory ✋ *(client acts)* | Advice, timing, client action |
| `IRE-13` | Eradication verification | Method, result, residual risk |
| `IRE-14` | Recovery sequencing advice | Order, dependencies, reinfection risk |
| `IRE-15` | IOC package production | Hashes, network, host, account indicators |
| `IRE-16` | Root cause determination | Cause, evidence, confidence |

`IRE-11` is stated as two separate findings deliberately. "The attacker could have accessed this
data" and "the attacker did take this data" are different claims with very different consequences for
the client, and conflating them is among the most damaging errors in incident reporting.

### Incident-type modules ⟪incident_module⟫

| Module | Adds |
|---|---|
| **Ransomware** | Encryption scope determination · variant identification · ransom note and actor-communication analysis · **backup integrity and isolation verification** · leak-site monitoring · decryption feasibility assessment · recovery sequencing |
| **Business email compromise** | Mailbox rule and forwarding analysis · authentication log analysis · OAuth grant review · financial transaction tracing · onward-phishing assessment |
| **Data theft** | Data classification of affected stores · staging and archive artefact analysis · egress volume analysis · **breach scope determination** |
| **Insider** | Account activity profiling · data movement to removable media and personal cloud · **heightened confidentiality — the subject must not learn of the investigation** |
| **Web/application compromise** | Webshell identification · application log analysis · vulnerability determination · supply-chain assessment |
| **Unknown** | Broad triage until the type is determined; the module is switched once it is |

### §3 Client information `[SERVICE]` — sequenced for speed; the first six in the first call
**When was it detected · is it still ongoing right now · what has been isolated · are domain
controllers affected · are backups affected · is anyone else already engaged** — then: affected
systems and criticality · what has already been done *(reboots, reimaging, AV cleaning, password
resets, rebuilds)* · who has handled the systems · EDR/SIEM present and retention · network telemetry ·
data classes on affected systems · **regulatory notification clocks the client believes are running** ·
insurer and counsel engagement · incident commander and out-of-hours decision authority ·
**who must not know about this** *(insider module)*.

### §5 Authorisation `[CORE]` + `[SERVICE]`
Normally via `AU-07` emergency authorisation with 24-hour ratification. **What it unblocks and what
it does not is inherited from the spine and is not relaxed here.**

### §9 Evidence `[ARCH:A3]` + `[SERVICE]`
Triage collections · memory where captured · logs with retention windows recorded · malware samples
*(handed to `SF-A3-MAL` as a child engagement)* · network telemetry. **Register-only** *(Rule 3)* —
the platform records what was acquired, its hash and custody; Sleuth's lab holds the content.

### §10 Decisions
Preserve vs recover **(the central tension of every incident — and the client's decision, with
Sleuth advising)** · containment timing · whether to allow the adversary to remain under observation
· whether the incident is a breach for notification purposes *(counsel-dependent)* · whether to
escalate to a formal forensic examination.

### §11 Stops `[SERVICE]`
⊗ Evidence integrity fails.
⊗ The client begins recovery before preservation is complete — stop, escalate, document the loss.
⊗ Findings implicate the person commissioning the response — ▲ **Management directly**.
⊗ Authority to act is withdrawn mid-incident.

### §14 Deliverables
Incident report with full attacker timeline · scope assessment of affected systems and data · root
cause analysis · containment and eradication confirmation · recovery guidance · IOCs · post-incident
improvement recommendations *(all `SITE-DERIVED`)*. Ransomware module adds the ransomware-specific
sections in `08-reporting-architecture.md` §3.

### §15 Follow-up
Post-incident review · eradication verification after recovery · improvement engagement.
**Needs Sleuth Confirmation** whether a post-incident review is included or sold separately.

### §16 Closure `[SERVICE]`
Plus: confirm any Sleuth-provided monitoring is withdrawn · confirm IOCs were handed over · confirm
the client's own preservation obligations are understood before Sleuth's involvement ends.

**`[GAP]` ransom-payment position — ✓ **CLOSED 2026-09-21**:** Sleuth supplies facts; it does not advise on payment,
negotiate or facilitate (`32` §6).
**`[GAP]` BLOCKING — triage collection scope:** what Sleuth collects first, from which systems, in
what order. **Genuinely Sleuth-specific — it depends on their tooling and their responders'
judgement, and it is now the single most operationally important remaining gap in the whole design.**

---

# `SF-A3-DFE` — Digital Forensic Examination

**Public service:** 11 Digital Forensics · **Archetype:** A3
**Variants:** internal/HR investigation · independent second-opinion review · litigation support

### §2 Service-specific procedures `[SERVICE]`

| ID | Procedure | Records |
|---|---|---|
| `DFE-01` | **Questions-posed capture** — the precise questions the examination must answer, agreed in writing | Questions, instructing party, agreed date |
| `DFE-02` | Device receipt and physical custody | Condition, seals, photographs, receipt signed |
| `DFE-03` | Encryption and access assessment | Encryption present, key availability, method |
| `DFE-04` | Forensic acquisition *(runs `A3-06`)* | Full acquisition record |
| `DFE-05` | File system and metadata analysis | Findings, artefacts |
| `DFE-06` | Deleted data recovery and carving | Recovered items, method, limitations |
| `DFE-07` | Email and communication analysis | Messages, attachments, context |
| `DFE-08` | Internet and application artefact analysis | Browsing, application usage |
| `DFE-09` | External device and data movement analysis | USB history, cloud sync, transfers |
| `DFE-10` | Document and file analysis relevant to the questions posed | Relevant items with context |
| `DFE-11` | Timeline reconstruction *(runs `A3-09`)* | Normalised timeline |
| `DFE-12` | **Per-question conclusion with confidence** | One conclusion per question from `DFE-01` |

`DFE-01` and `DFE-12` bookend the engagement deliberately. A forensic examination that does not answer
the question it was commissioned to answer — however interesting its findings — has failed, and
agreeing the questions in writing at the start is what prevents that.

### §3 Client information `[SERVICE]`
The matter and period concerned · subjects of the examination and whether they are aware ·
**device ownership and data ownership (blocking)** · employment policy or consent covering
examination · counsel consulted · court order or regulatory direction · device list with
make/model/identifier · current location · **powered on or off** · encryption and key availability ·
possession history · **prior handling by anyone (critical)** · available collateral evidence ·
custody to date · whether findings will be relied on in proceedings.

### §5 Authorisation `[SERVICE]`
⊗ **No examination without recorded authority.** Device ownership, data ownership, and either policy
coverage or explicit consent. For litigation-support variant: counsel's instructions.

### §11 Stops `[SERVICE]`
⊗ Authority proves insufficient once the device is examined *(e.g. it is personally owned)*.
⊗ Material is encountered that is outside the scope of the questions posed and is privileged or
personal — stop, seek instruction.
⊗ Findings implicate the instructing party — ▲ **Management directly**.

### §14 Deliverables
Forensic investigation report with findings and supporting evidence · event timeline · technical
artefact analysis · executive summary and conclusions · recommendations where applicable
*(`SITE-DERIVED`)*. Structure per `08-reporting-architecture.md` §3.

### §16 Closure `[SERVICE]`
Device return with signed acknowledgement, or retention under legal hold with a review date.
⊗ **Closure is blocked until every device is dispositioned.**

**`[GAP]` BLOCKING — expert reports, testimony and electronic-record certificates.** Sleuth agreed to
obtain counsel's advice; the advice itself is outstanding. **Until it is answered, `SF-A3-DFE` can be
built but should not be run for any matter heading toward proceedings** — the report format and
custody documentation both depend on the answer *(NC-09 / E4)*.

---

# `SF-A3-SPY` — Mobile Device Spyware Examination

**Public service:** 12 Mobile Spyware Detection · **Archetype:** A3 + Individual Client context
**Clients are frequently individuals, not organisations.**

> **Safety comes before method here.** The site's own instruction — *"If you suspect your phone is
> being monitored, do not discuss it on that device"* — is the first operational step, not a
> marketing line. In a domestic-abuse context, an examination can itself place someone at risk.

### §2 Service-specific procedures `[SERVICE]`

| ID | Procedure | Records |
|---|---|---|
| `SPY-01` | **Safe channel establishment (before anything else)** — a communication channel off the suspect device | Channel agreed, method, confirmed safe |
| `SPY-02` | Risk and context assessment — **including whether this is a domestic or intimate-partner context** | Context, safety considerations, referrals |
| `SPY-03` | **Consent and ownership verification (blocking)** — who owns the device, who pays the account, employer MDM enrolment | Ownership, consent, authority |
| `SPY-04` | Device handling instruction — how to bring the device in without alerting an observer | Instruction given, method |
| `SPY-05` | Device isolation | Isolation method, timestamp |
| `SPY-06` | Forensic acquisition *(iOS / Android)* | Acquisition record, **completeness and what could not be acquired** |
| `SPY-07` | Known-family indicator sweep — Pegasus, Predator, Hermit, NSO/Cytrox-class *(`SITE-DERIVED`)* | **Per-family result, including negatives** |
| `SPY-08` | Commercial stalkerware sweep — FlexiSPY, mSpy, Cocospy *(`SITE-DERIVED`)* | Per-product result |
| `SPY-09` | MDM profile and enterprise certificate inspection | Profiles found, provenance |
| `SPY-10` | Network traffic and app permission audit | Findings |
| `SPY-11` | Jailbreak/root and exploit artefact analysis | Artefacts, interpretation |
| `SPY-12` | SMS and messaging link forensics | Suspicious links, timing |
| `SPY-13` | **Assessment formulation — compromised / not detected / inconclusive** | Assessment with confidence and its basis |
| `SPY-14` | Hardening, replacement and monitoring guidance | Guidance given, safety plan where relevant |

`SPY-13`'s middle value is deliberately "**not detected**", never "clean". Absence of evidence on a
modern mobile device — where acquisition is frequently incomplete — is not evidence of absence, and
telling a journalist or an at-risk individual that their device is "clean" is a claim the evidence
usually cannot support.

### §3 Client information `[SERVICE]`
What behaviours prompted concern and when they started · battery, heat and data anomalies ·
unexpected messages or links · **who had physical access to the device and when** · device make,
model, OS version · passcode and biometrics · jailbroken/rooted to the owner's knowledge · MDM
profiles · backups available · **role or circumstance that could attract targeting** *(the site names
executives, board members, journalists, activists, legal professionals, high-net-worth individuals)* ·
travel to high-risk regions · what the person will do with the result · **whether there is a personal
safety concern**.

### §4 Documents `[SERVICE]`
Individual Engagement Agreement *(replaces MSA/SOW)* · Consent & Device Ownership Declaration.

### §11 Stops `[SERVICE]`
⊗ Ownership or consent cannot be established.
⊗ The device is employer-owned and the employer has not authorised examination.
⊗ **A safety risk to the person is identified** — pause, ▲ Management, address safety before method.

### §14 Deliverables
Assessment of compromise status · forensic report with evidence and indicators · tool identification
where possible · timeline of suspected activity · remediation and hardening guidance · monitoring
suggestions *(`SITE-DERIVED`)*. **Including explicit statement of acquisition completeness and its
limits.**

**`[GAP]` safeguarding position — ✓ **CLOSED 2026-09-21** in principle; drafted at `32` §3.** Still requires a **named
Sleuth owner**, **counsel review**, and **a referral list of appropriate support organisations in
India** — which I will not invent, because a wrong referral in this context is worse than none.
**Until those three exist, this service should not run through the platform.**
**`[GAP]` non-blocking:** indicator sources and their currency for `SPY-07` — better maintained as a
living reference than as runbook text.

---

# `SF-A3-CTH` — Compromise Assessment & Threat Hunt

**Public service:** 15 Compromise Assessment · **Archetype:** A3 · Runs one-off or on a schedule

### §2 Service-specific procedures `[SERVICE]`

| ID | Procedure | Records |
|---|---|---|
| `CTH-01` | Hunt scope and coverage definition — **and what will not be covered** | Scope, coverage target, exclusions |
| `CTH-02` | Telemetry availability assessment | Sources, retention, gaps |
| `CTH-03` | Collection deployment | Method, systems covered, completeness |
| `CTH-04` | **Hypothesis-driven hunting** — stated hypotheses, tested individually | Hypotheses, tests, results |
| `CTH-05` | IOC sweep against current intelligence | Indicators used, matches |
| `CTH-06` | Persistence mechanism review | Findings |
| `CTH-07` | Authentication and access pattern analysis | Anomalies, context |
| `CTH-08` | Anomalous process and service analysis | Findings |
| `CTH-09` | **Negative findings documentation** — what was checked and found clean | Per-check coverage and result |
| `CTH-10` | Detection gap identification | Gaps found during hunting |
| `CTH-11` | Escalation determination — if compromise is confirmed | Determination, escalation, client notified |

`CTH-09` is what makes a compromise assessment worth buying. A report saying "we found nothing" is
almost worthless; one saying "we checked these 40 things across 94% of the estate and found nothing"
is a genuine assurance statement. Coverage is the product.

### §3 Client information `[SERVICE]`
Why now *(suspicion / M&A / periodic / post-incident)* · specific concerns or named threats ·
estate scope and agent deployment feasibility · telemetry sources and retention · prior hunts and
findings · acceptable business disruption · **what happens if compromise is confirmed — agreed in
advance, never negotiated mid-incident**.

### §11 Stops `[SERVICE]`
⊗ **Active compromise confirmed** — stop hunting, ▲ immediately, propose an IR child engagement.
*(The site itself promises "escalation support if active compromise is confirmed".)*

### §14 Deliverables
Assessment report with findings and evidence · IOCs identified · **threat hunting analysis and
methodology documentation** · coverage statement · detection improvement recommendations ·
escalation record if applicable *(`SITE-DERIVED`)*.

**`[GAP]` BLOCKING — hunt hypothesis library and standard sweep set.** Genuinely Sleuth-specific:
dependent on their telemetry access, tooling and intelligence sources. Cannot be drafted from general
practice.

---

# `SF-A3-MAL` — Malware Analysis

**Public service:** 16 Malware Analysis · **Archetype:** A3
**Usually a child engagement**, inheriting the parent's client, authority, custody chain and classification.

### §2 Service-specific procedures `[SERVICE]`

| ID | Procedure | Records |
|---|---|---|
| `MAL-01` | **Safe receipt and handling** — encrypted, password-protected, marked, never executed outside the lab | Receipt method, handling confirmed |
| `MAL-02` | Sample identification and hashing | Hashes, file type, size, source |
| `MAL-03` | **Sharing permission check (blocking)** — may this sample be submitted to third-party services? | Permission, granted by, scope of permission |
| `MAL-04` | Static analysis | Strings, imports, structure, findings |
| `MAL-05` | Dynamic analysis in an isolated environment | Environment described, behaviour observed |
| `MAL-06` | Memory analysis where applicable | Findings |
| `MAL-07` | Network behaviour and C2 identification | Infrastructure, protocols |
| `MAL-08` | Persistence mechanism identification | Mechanisms, locations |
| `MAL-09` | Obfuscation and anti-analysis assessment | Techniques, impact on analysis |
| `MAL-10` | Capability assessment and threat characterisation | Capabilities, likely purpose |
| `MAL-11` | IOC extraction and packaging | Host, network, registry, file indicators |
| `MAL-12` | Detection content production *(where in scope)* | Rules delivered, format, tested |

> **`MAL-03` is a disclosure control, not a formality.** Uploading a client's sample to a public
> multi-scanner makes it available to third parties — and, in a targeted-intrusion case, can alert
> the adversary that they have been discovered. The default must be **no sharing without explicit
> written permission**, recorded per sample.

### §3 Client information `[SERVICE]`
Sample provenance and how obtained · **safe transfer channel** · is it live in the environment right
now · affected systems · desired output *(IOCs / behaviour / attribution / decryption feasibility)* ·
**sharing permission (blocking)** · analysis depth required · urgency driver.

### §5 Authorisation
`[CORE]`, or **inherited from the parent engagement** where this is a child.

### §11 Stops `[SERVICE]`
⊗ The sample cannot be contained safely in the available environment.
⊗ Analysis indicates targeted intrusion tooling and sharing was assumed rather than authorised.
⊗ The sample proves to be, or contain, client personal data.

### §14 Deliverables
Analysis report with behavioural findings · **technical IOCs (hashes, network indicators, registry
artefacts)** · capability assessment and threat characterisation · detection and mitigation
recommendations *(`SITE-DERIVED`)*.

### §16 Closure `[SERVICE]`
Sample disposition — retained under a stated policy, or destroyed with certificate.
⊗ Analysis environment sanitised and confirmed.

**`[GAP]` BLOCKING — isolated analysis environment specification and network policy.**
Sleuth-specific infrastructure; getting it wrong risks Sleuth's own network.
