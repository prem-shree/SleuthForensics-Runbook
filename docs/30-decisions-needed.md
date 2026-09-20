# 30 — Decisions Needed from Sleuth

> Plain English. Every item has my recommendation. **Nothing here blocks further design work** —
> it blocks *runbooks reaching Approved status*, which is what makes them safe to run engagements on.

**Current state: 20 engagement types specified · 0% SME-validated · 21 blocking gaps.**

---

## Part A — Policy decisions only Sleuth can make

These cannot be drafted from industry practice. They are risk-appetite and professional-conduct
choices that belong to the firm.

### A1. How far may a tester go before stopping?
Every test says "stop at proof of access". Nobody can follow that without knowing what proof of
access means. Is reading one file proof? Creating an account? Getting domain admin?

> **Recommend:** three levels, selected per engagement at scoping — *Identify only* (confirm the
> weakness exists), *Validate safely* (prove it works without changing anything), *Demonstrate impact*
> (show what an attacker could reach, stopping at the first proof). Default **Validate safely**.
> **This is the most important single gap in the design** — it affects seven engagement types.

### A2. What may a red team actually do?
Which techniques are permitted, and what persistence may be installed on a client's systems?

> **Recommend:** a written permitted-technique list with explicit prohibitions, agreed once as firm
> policy and narrowed further per engagement. Every persistence mechanism inventoried at the moment
> of use, for verified removal at closure.

### A3. Social engineering — do you capture credentials, and do you name individuals?
> **Recommend: no to both.** Record that a credential was submitted, never the credential. Report
> aggregate results only. A simulation producing a list of people who failed becomes a disciplinary
> instrument and destroys the trust the exercise depends on. If a client asks for names, that is a
> scoping conversation — and my recommendation is to decline.

### A4. What is Sleuth's position on ransom payment?
Not whether to pay — whether Sleuth advises on it at all, and whether the platform records it.

> **Recommend:** Sleuth provides *facts* (is decryption feasible, is data genuinely stolen, are
> backups viable) and does not advise on payment, which is a decision for the client with its counsel
> and insurer. Record the facts, not the payment discussion.

### A5. Do you produce expert reports, give testimony, or certify electronic records?
> **Recommend:** confirm with counsel before the first forensic engagement runs through the platform.
> If yes, the forensic report format and custody documentation both change materially — better known
> now than after twenty engagements are in the system.

### A6. What happens when a spyware client is in a domestic-abuse situation?
The website names domestic surveillance and stalkerware. An examination can itself put someone at
risk if the person monitoring them notices.

> **Recommend:** a written safeguarding position — what Sleuth does, what it will not do, and who it
> refers to. **I would settle this before running this service through the platform at all.** It is
> the one place in the catalogue where getting it wrong could hurt a person.

### A7. Can the vCISO authorise Sleuth's own testing at that client?
> **Recommend: no.** A Sleuth-supplied vCISO authorising Sleuth's own testing is self-authorisation.
> Require an independent client-side signatory. Built as a rule on the Authorisation Gate.

### A8. What makes a finding Critical rather than High?
> **Recommend:** define by *business consequence*, not technical severity — which matches how the
> site positions Sleuth's reporting. Without firm definitions, severity drifts between analysts and
> clients notice.

### A9. Does Sleuth perform takedowns?
> **Recommend:** no in the initial platform. It introduces third-party interaction the design does
> not model. Report and advise instead.

---

## Part B — Choices where a yes/no is enough

I have a recommendation for each; they just need confirming.

| # | Question | Recommendation |
|---|---|---|
| B1 | Which maturity scale for assessments? | A 5-level scale aligned to NIST CSF tiers. Must be one scale across all A1 types, or year-on-year comparison breaks |
| B2 | Which hardening benchmarks for configuration reviews? | **CIS Benchmarks** as the baseline, with vendor guidance where CIS has no coverage. Largest authoring item in A1 |
| B3 | Which mobile standard? The site says "industry mobile security standards" without naming one | **OWASP MASVS** |
| B4 | Which web/API testing standard and depth? | **OWASP WSTG** for coverage, **ASVS Level 2** as the default depth |
| B5 | Adopt the standards baseline in docs 22–23? *(NIST SP 800-115, NIST SP 800-61, ISO/IEC 27037 and 27041–27043, MITRE ATT&CK)* | **Yes.** All are mainstream and defensible. This is a policy confirmation, not a technical one |
| B6 | Is retest standard across all testing types, or only VAPT and Web/API where the site promises it? | **Standard across all A2 types.** Clients expect it and it is cheap once findings are structured |
| B7 | Does detection-validation testing belong in the SOC assessment? | **Yes** — otherwise you are assessing what a SOC *should* detect, not what it does. Note it adds a Letter of Authorisation requirement to an otherwise non-intrusive engagement |

---

## Part C — Facts only Sleuth has

Not decisions — information. Each unblocks work that is currently guessing.

| # | Needed | Why it matters |
|---|---|---|
| C1 | Which of the 20 engagement types are live today, and rough annual volume | Sets runbook authoring order. **The single most useful answer** |
| C2 | Who validates methodology, per pillar | Rule 1 does nothing without named people. This is the critical path |
| C3 | Where evidence is physically held today — lab storage, evidence safe, encrypted volumes | The register's vocabulary must match reality |
| C4 | Hosting and data residency preference | India assumed. Constrains infrastructure; expensive to change later |
| C5 | Existing identity provider, ticketing and document systems | Integration scope, and avoids duplicating what exists |

---

## Part D — The first build target

**My recommendation: `SF-A2-IPT` (Infrastructure Penetration Test), external mode.**

It carries the most externally-imposed structure — authorisation, scope, window, rules of engagement,
findings, retest — so building it first exercises machinery every other archetype reuses.

**But I am genuinely unsure, and it is worth a moment of Sleuth's attention.** The firm is called
Sleuth *Forensics* and leads with investigation, yet 10 of 21 public services are security testing
and assessment. If the real revenue is investigation work, the first build should be
`SF-A3-DFE` (Digital Forensic Examination) instead — which is a harder, slower start, because it
means building evidence custody before findings and reporting exist.

> **Question:** roughly what share of Sleuth's work is investigation versus security testing and
> assessment? A rough split is enough.

---

## Part E — For qualified counsel

Not for Sleuth to answer alone, and none of it should be assumed by me.

| # | Question |
|---|---|
| E1 | Data residency — must all client data, including evidence records, remain in India? |
| E2 | Which incident-reporting obligations bind Sleuth, and which bind its clients with Sleuth advising? |
| E3 | Obligations arising from holding forensic records containing third parties' personal data |
| E4 | Whether Sleuth issues certificates for electronic records, or gives expert testimony *(see A5)* |
| E5 | Retention minimums and maximums for evidence records, reports and audit logs |
| E6 | Cross-border transfer where evidence originates outside India |
| E7 | Review and approval of the document template library *(Rule 5 — no template is counsel-approved today)* |

---

## What I will do while these are open

Nothing here stops the architecture progressing. In priority order:

1. Author report templates for all 20 engagement types against the composition model.
2. Author the questionnaire instruments for all 20 types.
3. Specify the decision trees named across the ETS set.
4. Specify the tool capability taxonomy — vendor-neutral, so the catalogue can be seeded by Sleuth.
5. Produce the data schema in full, ready for implementation.

Gaps stay marked as gaps. Nothing gets invented to make a runbook look finished.
