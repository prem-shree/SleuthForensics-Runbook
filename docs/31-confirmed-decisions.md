# 31 — Confirmed Decisions Register

**Confirmed by Sleuth: 2026-09-21** — "yes to all" against the recommendations in
`30-decisions-needed.md`.

> **This is the first content in the repository with provenance `SLEUTH-SUPPLIED`.** Everything else
> remains `PROPOSED` / `INDUSTRY-PRACTICE` / `SITE-DERIVED` and **Draft / Needs SME Validation**.
>
> A new validation value is introduced: **`SLEUTH-CONFIRMED`** — a *policy* decision accepted by
> Sleuth. It is distinct from `SME-VALIDATED`, which concerns whether a *technical procedure* is how
> Sleuth actually works. A confirmed policy can still sit above an unvalidated procedure.

---

## 1. What is now confirmed

| Ref | Decision | Confirmed position | Specified in |
|---|---|---|---|
| **A1** | Intrusiveness ceiling | Three levels — *Identify only* · *Validate safely* · *Demonstrate impact*. Default **Validate safely** | `32` §1 |
| **A2** | Red team permitted techniques | A written firm-level permitted list with explicit prohibitions, narrowed further per engagement. Every persistence mechanism inventoried at deployment | `32` §5 |
| **A3** | Social engineering handling | **No credential capture. No naming of individuals.** Aggregate reporting only | `32` §4 |
| **A4** | Ransom payment | Sleuth supplies facts. It does not advise on payment, negotiate, or facilitate | `32` §6 |
| **A5** | Expert reports / testimony / certificates | **Confirm with counsel before the first forensic engagement runs.** *(Accepting the recommendation means agreeing to obtain that advice — it does not itself answer the question)* | remains open — §3 |
| **A6** | Safeguarding for individual clients | A written position is adopted. **Drafted here; requires a named Sleuth owner and counsel review** | `32` §3 |
| **A7** | vCISO independence | A Sleuth-supplied vCISO may **not** authorise Sleuth's own testing at that client | `32` §7 |
| **A8** | Severity definitions | By **business consequence**, not technical severity | `32` §2 |
| **A9** | Takedowns | **Not offered** in the initial platform. Report and advise instead | `32` §8 |
| **B1** | Maturity scale | Five levels, NIST CSF-tier aligned. One scale across all A1 types | `32` §9 |
| **B2** | Hardening benchmarks | **CIS Benchmarks** baseline; vendor guidance where CIS has no coverage | `32` §9 |
| **B3** | Mobile standard | **OWASP MASVS** | `32` §9 |
| **B4** | Web/API standard and depth | **OWASP WSTG** coverage, **ASVS Level 2** default depth | `32` §9 |
| **B5** | Standards baseline | Adopted: NIST SP 800-115 · NIST SP 800-61 · ISO/IEC 27037 · ISO/IEC 27041–27043 · MITRE ATT&CK · OWASP · CIS · IEC 62443 / NIST SP 800-82 | `32` §9 |
| **B6** | Retest | **Standard across all A2 engagement types**, in scope, 90-day window | `32` §10 |
| **B7** | Detection-validation in SOC assessment | **In scope.** Carries a Letter of Authorisation requirement into an otherwise non-intrusive engagement | `24` `SF-A1-SOA` |
| **D** | First build target | **`SF-A2-IPT`, external mode** | `16` / `29` §8 |

---

## 2. Gaps closed

**21 blocking gaps → 7.**

| Closed | By |
|---|---|
| `A2-09` intrusiveness ceiling — *was the largest gap in the design, affecting 7 engagement types* | A1 |
| `SF-A2-IPT` intrusiveness *(inherited)* | A1 |
| `SF-A2-ATP` path validation depth | A1 — validation to domain admin is Level 3 and separately authorised |
| `SF-A2-RED` permitted TTPs and persistence | A2 |
| `SF-A2-SES` credential capture and individual naming | A3 |
| `SF-A3-IRE` ransom-payment position | A4 |
| `SF-A4-VCI` independence policy | A7 |
| Severity definitions *(`29` §1)* | A8 |
| `SF-A4-ASM` takedowns | A9 |
| `A1-06` maturity scale | B1 |
| `SF-A1-SPA` maturity scale *(inherited)* | B1 |
| `SF-A1-TCR` benchmark source *(per pack)* | B2 — **the pack content is now authoring work, not a decision** |
| `SF-A2-MAT` mobile standard | B3 |
| `SF-A2-WAT` testing standard and depth | B4 |
| Retest scope across A2 | B6 |
| `SF-A1-SOA` detection-validation applicability | B7 |
| `A4-02` collection cadence · `SF-A4-ASM` cadence and alert severity | Recommended defaults adopted — `32` §11 |
| Gate thresholds — blocked-item ageing, override duration | Recommended defaults adopted — `32` §11 |

---

## 3. What "yes to all" did **not** resolve

Stated plainly, because treating these as settled would be the single easiest way to get this wrong.

### 3.1 Three of the items were requests for facts, not decisions

| Ref | Still needed | Why a "yes" cannot supply it |
|---|---|---|
| **C1** | Which of the 20 engagement types are live, and annual volume | Sets runbook authoring order |
| **C2** | **Who validates methodology, per pillar** | Rule 1 is inert without named people. **This is the critical path, and it is now the single most important outstanding item** |
| **C3** | Where evidence is physically held today | The register's `storage_location` vocabulary must match reality |
| **C4** | Hosting and data residency preference | India assumed; constrains infrastructure |
| **C5** | Existing identity provider, ticketing, document systems | Integration scope |
| **D** | The investigation vs security-testing revenue split | I asked a question, not for a yes. **Proceeding on my recommendation (`SF-A2-IPT` first) as a recorded assumption** — reversible at low cost until Phase 1 begins |

### 3.2 Counsel matters are not resolved by client acceptance

**Rule 5 is binding and a "yes" does not override it.** No document template is counsel-approved; no
workflow inside the platform can make one so. Outstanding, unchanged:

E1 data residency · E2 incident-reporting obligations · E3 third-party personal data in forensic
records · **E4 expert reports, testimony and electronic-record certificates** · E5 retention periods ·
E6 cross-border transfer · E7 review of the template library.

E4 remains the one that changes a deliverable's structure. Until it is answered, `SF-A3-DFE` can be
built but should not be run for any matter heading toward proceedings.

### 3.3 Two confirmed policies still need a named owner at Sleuth

Accepting a recommendation is not the same as owning the resulting commitment.

- **A6 safeguarding** (`32` §3) is a duty-of-care position. It needs a named Sleuth owner, counsel
  review, and — specifically — **a referral list of appropriate support organisations in India**,
  which I will not invent.
- **A2 red team permitted techniques** (`32` §5) is a firm risk-appetite statement. The baseline is
  drafted; it needs sign-off by whoever carries that risk.

### 3.4 Four technical gaps remain, and they are genuinely Sleuth's

These cannot be drafted from industry practice because they depend on Sleuth's own tooling,
infrastructure and responders' judgement:

| Gap | Engagement type | Why only Sleuth can supply it |
|---|---|---|
| Triage collection scope and order | `SF-A3-IRE` | Depends on Sleuth's tooling and what its responders collect first. **Most operationally important remaining gap** |
| Hunt hypothesis library and standard sweep set | `SF-A3-CTH` | Depends on Sleuth's telemetry access and intelligence sources |
| Isolated analysis environment specification | `SF-A3-MAL` | Sleuth's own infrastructure; getting it wrong risks Sleuth's network |
| Passive observation method and safety approval | `SF-A1-OTA` | Site- and vendor-specific. **Must not be drafted from general practice** |

Plus two currency-dependent items: spyware indicator sources (`SF-A3-SPY`) and per-provider cloud
testing policies (`SF-A2-CPT`) — both better maintained as living references than as runbook text.

---

## 4. Readiness after this confirmation

| | Before | After |
|---|---|---|
| Blocking gaps | 21 | **7** |
| Engagement types with no blocking gap | 6 of 20 | **14 of 20** |
| Policy decisions outstanding | 9 | **0** *(2 need a named owner)* |
| Standards baseline | undecided | **adopted** |
| `SLEUTH-CONFIRMED` content | none | 17 decisions |
| `SME-VALIDATED` content | **0%** | **0%** — unchanged, and this is the real constraint |

> The honest read: **policy is now largely settled, and technical validation has not started.** The
> six engagement types still carrying blocking gaps are all in A3 and A1-OT — the areas where Sleuth's
> own expertise is irreplaceable. Nothing I can write closes them.
