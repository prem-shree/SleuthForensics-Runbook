# 32 — Operating Policies

> **Status:** §1, §2, §4, §6, §7, §8, §9, §10, §11 are **`SLEUTH-CONFIRMED`** (2026-09-21) and drafted
> here to the level the platform needs. §3 and §5 are **drafted for sign-off** — Sleuth confirmed the
> *principle*; the text below needs a named owner, and §3 additionally needs counsel review.
>
> These are firm policies, not technical procedures. They constrain runbooks; they do not replace the
> SME validation that runbook content still requires.

---

## 1. Intrusiveness ceiling `SLEUTH-CONFIRMED`

> **The gap this closes.** Every A2 procedure said "stop at proof of access". No analyst could follow
> that without a definition. This is that definition. It affects seven engagement types.

Three levels. **One is selected per engagement at scoping** and recorded in the Rules of Engagement.
It appears on the engagement header and on every procedure the analyst opens.

### Level 1 — IDENTIFY ONLY

*Confirm a weakness exists from observable evidence. Do not trigger it.*

| | |
|---|---|
| **Permitted** | Passive reconnaissance · service and version identification · configuration reading · authenticated configuration review · response-behaviour observation |
| **Prohibited** | Any payload · any authentication or authorisation bypass attempt · any write of any kind |
| **Stop point** | The observation that establishes the weakness exists |
| **Evidence** | The observation, with its source |
| **Default for** | `SF-A2-IPT` in VA mode · `SF-A1-TCR` · `SF-A1-OTA` passive observation · any asset flagged fragile or safety-critical |

### Level 2 — VALIDATE SAFELY  ← **firm default**

*Prove the weakness is real and reachable, without changing state and without taking more than the
minimum needed to prove it.*

| | |
|---|---|
| **Permitted** | Triggering the weakness with a benign, non-destructive proof — a timing or arithmetic proof for injection rather than data extraction; retrieving a single non-sensitive identifier; confirming a token or bypass is accepted; accessing one resource the tester should not be able to see |
| **Prohibited** | Writing, modifying or deleting client data · creating accounts · installing anything · bulk retrieval · persistence · pivoting beyond the asset proven |
| **Stop point** | **The first artefact that proves the weakness. Not a second.** |
| **Evidence** | Request/response pair plus a redacted screenshot |
| **Default for** | `SF-A2-IPT` external and internal · `SF-A2-WAT` · `SF-A2-MAT` · `SF-A2-CPT` · `SF-A2-ATP` |

### Level 3 — DEMONSTRATE IMPACT

*Show what an attacker could reach, to establish business consequence.*

| | |
|---|---|
| **Requires** | ✋ Explicit per-engagement authorisation in the Rules of Engagement, naming which assets and to what depth. Never a default |
| **Permitted** | Chaining · lateral movement within named scope · privilege escalation to a named ceiling · retrieving a small named sample sufficient to prove the *class* of data reachable |
| **Prohibited** | Bulk retrieval · any action outside the named scope |
| **Stop point** | The named ceiling, or the first proof of the named objective |
| **Evidence** | The full chain, with every step separately evidenced |
| **Default for** | `SF-A2-RED` *(mandatory — it is the point of the engagement)* · `SF-A2-ATP` path validation to domain admin *(separately authorised — proving the path means becoming domain admin)* |

### Absolute rules — every level, no exception, not overridable

1. Never destroy, degrade or deny availability.
2. Never modify production data.
3. Never exfiltrate data in bulk.
4. Never retain client data beyond the evidence needed to support the finding.
5. **Never access personal data beyond incidental exposure.** If encountered incidentally: stop, do
   not copy, record that it was encountered, notify the Engagement Manager.
6. Never leave persistence beyond the testing window.
7. **When unsure whether an action is within the ceiling, escalate rather than proceed.** The cost of
   a question is minutes; the cost of the alternative is an authorisation breach.

Rules 1–4 and 6 are also gate conditions at closure. Rule 5 is a stop condition.

### Per-type summary

| Engagement type | Default | Escalatable to |
|---|---|---|
| `SF-A2-IPT` external / internal | L2 | L3 with RoE authorisation |
| `SF-A2-IPT` VA mode | L1 | — |
| `SF-A2-IPT` wireless | L2 | L3 with RoE authorisation |
| `SF-A2-WAT` · `SF-A2-MAT` | L2 | L3 with RoE authorisation |
| `SF-A2-CPT` | L2 | L3 for IAM path proof |
| `SF-A2-ATP` | L2 | **L3 mandatory for domain-admin path validation** |
| `SF-A2-RED` | **L3** | — |
| `SF-A2-SES` | §4 governs | — |
| `SF-A1-SOA` detection validation | L1/L2 equivalent — telemetry without real impact | — |
| `SF-A1-TCR` · `SF-A1-OTA` | L1 | — |

---

## 2. Severity model `SLEUTH-CONFIRMED`

> **Severity is a statement about consequence to *this* client, not about the technical flaw.**

| Severity | Consequence | Reachability |
|---|---|---|
| **Critical** | Severe and immediate: full environment compromise · unauthenticated access to bulk personal or regulated data · ability to halt a core business process · compromise of the identity system | Reachable now by a realistic attacker with no meaningful barrier |
| **High** | Serious, but requires a condition — authentication, a chained step, or a specific network position | Achievable by a capable attacker |
| **Medium** | Real, but bounded in scope, or meaningful barriers exist | Requires effort, access or an unlikely condition |
| **Low** | Limited. Contributes to risk rather than causing it | Requires substantial chaining |
| **Informational** | No direct consequence. Hygiene, hardening, or an observation worth recording | — |

**Anchor rules**

- **Two clients with the identical technical flaw may legitimately receive different severities.** The
  written rationale must say why — that is the rationale's purpose.
- CVSS is supplementary and optional. It never sets severity on its own.
- Severity never rises because a tool labelled it so, and **never falls because remediation is
  difficult or expensive.** Remediation effort is a separate field for exactly this reason.
- Reviewer moderation and calibration against comparable prior findings apply (`08` §1.1).

---

## 3. Safeguarding — individual clients `DRAFTED FOR SIGN-OFF`

> Sleuth confirmed the principle. **This text needs a named Sleuth owner and counsel review before
> `SF-A3-SPY` runs through the platform.** It is a duty-of-care commitment, not a procedure.

The website names domestic surveillance and stalkerware. In that context the examination itself can
place someone at greater risk — because the person monitoring them may notice.

### Standing position

1. **Safe channel first.** Establish a communication channel off the suspect device before any
   substantive discussion. Nothing else happens until this is done.
2. **Ask about context, neutrally.** Whether a domestic or intimate-partner situation may be involved
   is a standard question, asked without assumption, early.
3. **Where a safety concern is indicated:** no reports to a shared address · no voicemails · agree a
   safe contact window · assume the device may be monitored for the engagement's duration · restrict
   access to the engagement record inside Sleuth.
4. **Removal is not automatic, and not Sleuth's decision to take unilaterally.** Removing spyware can
   alert the observer and escalate risk. Present the options and their consequences: preserve and
   evidence · harden · replace the device · take no action yet. **The person decides.**
5. **Sleuth does not give legal or personal-safety advice. It refers.**
   `[GAP]` **Needs Sleuth:** a referral list of appropriate support organisations in India. I will not
   invent one — a wrong referral in this context is worse than none.
6. **Never contact the suspected observer**, under any circumstances, for any reason.
7. **If an examination would place the person at risk and no safe path exists: decline and refer.**
   Declining is a legitimate professional outcome and is recorded as one.
8. Safety considerations are recorded on the engagement and access to them is restricted.

### Why this sits above the technical method
An examination that finds spyware but gets the person hurt has failed. The ordering — safety, then
consent, then method — is deliberate and is reflected in the procedure order in `26` (`SPY-01` → `SPY-14`).

---

## 4. Social engineering handling `SLEUTH-CONFIRMED`

| | |
|---|---|
| **Credentials** | **Never captured, never stored, never transmitted.** The platform records *that a submission occurred*, its timestamp and the target group. Nothing else. Any capture page is built to discard input at the point of receipt |
| **Individuals** | **Never named** in any deliverable, at any severity, for any client |
| **Reporting** | Aggregate only: click rate, submission rate, **report rate and time-to-first-report**, by group |
| **Reporting a phish is a positive finding** and is reported as prominently as failure rates |
| **Exclusions** | Honoured absolutely — individuals in sensitive circumstances, on leave, or in protected roles |
| **Distress** | If a target experiences genuine distress: stop that thread, notify HR, record it |
| **Client requests names** | A scoping conversation before the engagement, never a reporting decision after it. **Recommended answer: decline** |

> A simulation producing a list of people who failed is a disciplinary instrument, not a security
> assessment. It destroys the trust the exercise depends on, and next year's results become
> meaningless because people behave differently when they believe they are being scored.

---

## 5. Red team permitted techniques `DRAFTED FOR SIGN-OFF`

> Sleuth confirmed the principle of a written list. **This baseline needs sign-off by whoever carries
> the firm's risk.** Each engagement narrows it further in the Rules of Engagement; no engagement widens it.

**Permitted by default** — phishing with an approved pretext · credential submission simulation
*(never storing credentials — §4 applies)* · password spraying within agreed lockout-safe limits ·
living-off-the-land techniques · command and control over approved channels · lateral movement within
named scope · privilege escalation to a named ceiling · single-sample data access proof.

**Prohibited by default, at every engagement** — destructive actions of any kind · denial of service ·
modification of production data · **persistence surviving the engagement window** · disabling or
degrading security controls · physical damage · targeting personal devices or personal accounts ·
targeting individuals outside the agreed population · **exploiting a genuine third-party compromise
discovered during the engagement** *(stop and escalate — `25` `SF-A2-RED` §11)* · anything capable of
triggering a safety system.

**Requires explicit per-engagement approval** — physical entry · any technique against OT or ICS ·
any action against an asset flagged fragile · **deploying any persistence at all**.

**Always** — every persistence mechanism is inventoried at the moment of deployment, and each is
individually verified as removed at closure (`RED-10`, a Closure Gate condition). A forgotten red team
implant is a recurring industry failure and an avoidable one.

---

## 6. Ransomware — position on payment `SLEUTH-CONFIRMED`

**Sleuth supplies facts.** Is decryption technically feasible · is there evidence data was actually
taken, as distinct from could have been accessed · are backups viable and isolated · what variant and
what is known about it · what is the realistic recovery path and sequence.

**Sleuth does not** advise on whether to pay · negotiate · facilitate or handle payment · introduce
intermediaries.

Where the client raises payment, Sleuth refers them to their counsel and insurer and records that the
referral was made — not the content of the discussion.

> **Counsel matter (E-series):** payment may carry sanctions and legal exposure in several
> jurisdictions. Sleuth's position should be confirmed with counsel, not merely adopted.

---

## 7. vCISO independence `SLEUTH-CONFIRMED`

A Sleuth-supplied vCISO **may not be the client-side authoriser for Sleuth's own testing or assessment
engagements at that client.** An independent client-side signatory is required.

Enforced as a rule on the Authorisation Gate (`29` §4, invariant 13): the platform refuses a signatory
recorded as a Sleuth-supplied vCISO for that client.

Where Sleuth provides both vCISO and delivery services to one client, the overlap is declared in the
engagement charter (`VCI-01`) and visible on both engagements.

---

## 8. Takedowns `SLEUTH-CONFIRMED`

**Not offered.** `SF-A4-ASM` reports brand impersonation and phishing infrastructure, and advises on
the takedown route. It does not pursue takedowns on the client's behalf — that introduces third-party
interaction the platform does not model and the engagement does not cover.

---

## 9. Standards baseline `SLEUTH-CONFIRMED`

| Area | Adopted |
|---|---|
| Technical testing | **NIST SP 800-115** · PTES as supporting method |
| Web and API | **OWASP WSTG** for coverage · **OWASP ASVS Level 2** as default depth |
| Mobile | **OWASP MASVS** |
| Adversary behaviour | **MITRE ATT&CK** — detection coverage mapping and threat profiles |
| Incident handling | **NIST SP 800-61** |
| Digital evidence | **ISO/IEC 27037** · **ISO/IEC 27041–27043** for assurance, analysis and investigation principles |
| Tool validation | SWGDE and NIST CFTT as reference |
| Hardening benchmarks | **CIS Benchmarks**; vendor guidance where CIS has no coverage |
| OT / ICS | **IEC 62443** · **NIST SP 800-82** *(both named on the website)* |
| Governance frameworks | ISO/IEC 27001 · SOC 2 · NIST CSF 2.0 *(all three named on the website)* |

**Maturity scale — one scale, all A1 engagement types:**

| Level | Name | Meaning |
|---|---|---|
| 1 | Initial | Ad hoc, undocumented, dependent on individuals |
| 2 | Developing | Documented, inconsistently applied |
| 3 | Defined | Documented, consistently applied, owned |
| 4 | Managed | Measured and reviewed, with evidence of effectiveness |
| 5 | Optimising | Continuously improved, informing strategy |

Every rating cites its source (`A1-06`). Target state is set per control with the client, not assumed
to be 5 — most controls do not need to be, and a roadmap that implies otherwise is not credible.

---

## 10. Retest `SLEUTH-CONFIRMED`

**Standard across all A2 engagement types**, included in the original scope.

- Window: **90 days** from report acceptance.
- Only **remediated** findings are retested. The client declares which.
- Outcomes: `Resolved` · `Partially resolved` · `Not resolved` · `Risk accepted` · `Unable to verify`.
- New findings discovered during retest are reported, and **flagged as outside the original scope** —
  they are not silently folded into the original engagement.
- A retest addendum is issued; the original report is never edited.
- Beyond 90 days, a retest is a new engagement.

---

## 11. Operating thresholds `SLEUTH-CONFIRMED` *(recommended defaults, adopted)*

| Threshold | Value |
|---|---|
| Blocked checklist item escalates | **3 business days** |
| Gate override maximum duration | **14 days**, then the gate re-blocks |
| Emergency authorisation ratification | **24 hours** |
| Methodology revalidation | **Annually**, or on a material tooling change |
| Document template legal review | **Annually**, or on a material legal change |
| `SF-A4-ASM` discovery | Continuous |
| `SF-A4-ASM` delta analysis | **Weekly** |
| `SF-A4-ASM` client report | **Monthly** |
| `SF-A4-ASM` coverage review | **Quarterly** |
| `SF-A4-ASM` alert response | Critical — notify immediately · High — within 24h · Medium/Low — in the cycle report |
| `SF-A4-VCI` reporting | **Monthly** operational · **Quarterly** board |
| Standing authorisation re-confirmation (A4) | **Per reporting period** |

All are configurable per client where a contract requires it — but these are the defaults, and a
deviation is recorded on the engagement.

---

## 12. How these policies reach the analyst

None of this is a document anyone is expected to remember.

- The **intrusiveness level** appears on the engagement header and on every procedure.
- **Absolute rules** (§1) render as stop conditions on the Now screen, always visible.
- **Severity definitions** appear inline in the finding editor, beside the severity selector.
- **Safeguarding steps** are the first procedures in `SF-A3-SPY`, not a policy to consult.
- **Permitted techniques** are rendered as the RoE is constructed, with prohibited items shown.
- **Thresholds** drive automatic escalation and gate re-blocking without anyone tracking dates.

A policy that lives only in a document is a policy that gets missed at 2am. Each of these is placed
where the decision is actually made.
