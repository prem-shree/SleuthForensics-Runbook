# 16 — Phased Implementation Plan

---

## 1. Two tracks, and which one is actually critical

```
TRACK A — PLATFORM        engineering
TRACK B — RUNBOOK CONTENT subject-matter authoring    ← THE CRITICAL PATH
```

**Track B is the constraint, not Track A.** A finished platform with three approved runbooks is unusable. A modest platform with twenty good runbooks changes how the firm works. Sixteen of the twenty-one services have no published methodology anywhere (research §2), so most of this is first-time authoring by senior people whose time is the scarcest resource in the firm.

Track B must start **before** Track A finishes Phase 0, and it must have named owners (Decision D8). Programme progress should be reported as *approved runbooks*, not *features shipped*.

---

## 2. Track A — platform phases

Durations are indicative and assume a small team. They are for sequencing, not commitment.

### Phase 0 — Foundations · ~4–6 weeks
Design system implemented from Sleuth's existing tokens (`12-visual-design-direction.md`). Authentication with mandatory MFA. RBAC with engagement-scoped membership. Hash-chained append-only audit log. Core entities: User, Client, ClientContact, Engagement. The engagement shell with the classification bar. Today queue skeleton. Synthetic data fixtures and the seeding guard.

*Exit:* a user can log in, see engagements they are a member of, and cannot see any they are not. Every action is audited.

**Why audit and RBAC come first:** both are close to impossible to retrofit honestly. An audit log added in Phase 4 has no record of Phases 0–3, and access control retrofitted into an application that never had it leaves gaps nobody finds until they matter.

### Phase 1 — Runbook engine + first vertical slice · ~6–8 weeks
The content plane: Runbook, Phase, Procedure, Task, ChecklistTemplate, GateDefinition — with versioning, status workflow and **pinning**. The execution plane counterparts. Questionnaire engine with conditional logic and context-module attachment. Gate evaluation with override workflow. The **Now** screen and procedure execution view. Authorisation Gate and Readiness Gate. Document template engine with variable resolution.

**Vertical slice: `SF-SEC-VAP-EXT` (VAPT — External Infrastructure)**, subject to Decision D9.

Chosen because A2 has the most externally-imposed structure — authorisation, scope, window, rules of engagement, findings, retest. Building it first exercises the machinery A1 and A3 both reuse. Building A1 first would produce a document-management tool that later has to be retrofitted with authorisation and evidence semantics, which is the expensive direction.

*Exit:* **a real engagement can be run end-to-end through Phase 4**, with gates enforced. This is the first point at which the platform is genuinely useful, and the first honest test of whether consultants prefer it to their current method.

### Phase 2 — Findings, reporting and QA · ~6–8 weeks
Findings register with severity, rationale and calibration. Evidence↔finding links with the ≥1 constraint enforced at the database. Report templates and composition. Report builder with generated and authored sections. Review workflow with itemised rejection. QA Gate. Release Gate with recipient verification. PDF generation. Acceptance recording. Remediation tracking and retest cycle. Findings Register Excel export (pulled forward — clients ask for it immediately).

*Exit:* **VAPT runs cradle-to-grave.** One archetype is complete. From here, the platform is delivering value on real work.

### Phase 3 — Evidence and custody core · ~6–8 weeks
Evidence register with the L0–L5 provenance ladder. Hashing and verification with immediate match feedback. Custody event stream with gap detection. Access history. Custody Gate. Evidence Integrity Gate. Disposition workflow with witness requirement and certificate generation. Mobile evidence-capture surface. Evidence Register and custody Excel exports.

Register-only, per Decision D1.

*Exit:* A3 work is possible. This is the subsystem that makes the platform specifically a *forensics* platform rather than a workflow tool.

### Phase 4 — Investigation archetype · ~6–8 weeks
A3 archetype module. Emergency authorisation path with ratification tracking. Decision tree engine with recorded traversal. Escalation workflow. Incident timeline construction. Child engagements. Runbooks: DFIR, Digital Forensics, Incident Response, Ransomware Investigation, Mobile Spyware, Malware Analysis, Compromise Assessment.

*Exit:* the Investigation pillar is live — six of the highest-stakes services.

### Phase 5 — Assessment & advisory archetype · ~4–6 weeks
A1 archetype module. Framework and control libraries. Maturity scoring with mandatory source citation. Evidence Sufficiency check. Interview and document-request tracking. Gap analysis and roadmap construction. Runbooks: Consulting, Audits, OT, SecOps, Compliance, and the A1 variants of Cloud, Identity, Endpoint and Network.

A1 is the largest bucket by engagement-type count and is deliberately later, because it is the *simplest* structurally and benefits most from reusing machinery proven in Phases 1–4.

### Phase 6 — Continuous & readiness archetype · ~4–6 weeks
A4 module with recurring cycles, cycle close and periodic re-authorisation. Delta analysis against the previous cycle. Alert ingestion and triage *(integration scope: Needs Confirmation)*. vCISO retainer periods and board reporting. Runbooks: Threat Intelligence monitoring, Periodic Threat Hunt, vCISO, Ransomware Readiness, Tabletop.

Introduces background job infrastructure — deliberately deferred until now, because nothing before this needed it.

### Phase 7 — Export layer and oversight · ~3–4 weeks
Full Excel workbook suite (`14-excel-exports.md`). Oversight dashboard. Registers with cross-engagement filtering. Practice metrics, rework analysis, obligation tracking.

### Phase 8 — Client-facing seam *(optional, gated on D2/D3)* · ~3–4 weeks
Secure questionnaire links. Client remediation tracking. Delivery portal. **Only after an independent security review of the platform.**

### Continuous
Dark mode (Phase 4+). Accessibility audit each phase. Security assessment before real data, and annually. Performance work as volume dictates.

---

## 3. Track B — runbook authoring

| Wave | Content | Aligns with |
|---|---|---|
| **Wave 0** | Core spine (~35 procedures). Written once, used by all 41 types. | Phase 0–1 |
| **Wave 1** | A2 archetype module + External Infrastructure service module | Phase 1 |
| **Wave 2** | Remaining A2 service modules: Web/API, Mobile, Cloud Pen, Network Pen, Identity ATP, Endpoint Validation, Red Team | Phase 2 |
| **Wave 3** | A3 archetype module + all 9 investigation service modules | Phase 3–4 |
| **Wave 4** | A1 archetype module + all 20 assessment service modules | Phase 5 |
| **Wave 5** | A4 archetype module + 4 continuous service modules | Phase 6 |
| **Continuous** | Context modules · questionnaires · report templates · decision trees · tool catalogue · document templates · KB from lessons learned | Throughout |

**Sequencing rule:** a runbook must reach `Approved` before the platform phase that depends on it ships. A phase that ships without its content is a phase that shipped nothing.

**Authoring quality bar** (`04-runbook-architecture.md` §5): a procedure cannot be approved unless it answers all nine questions — where am I, what am I doing, why, what do I need, what evidence, what do I produce, what next, what if something unexpected, who reviews. The editor enforces this.

---

## 4. Timeline

```
        Q4 2026          Q1 2027          Q2 2027          Q3 2027
        ──────────────── ──────────────── ──────────────── ────────────────
TRACK A  P0──P1────────── P2────────P3──── P4──────── P5─── P6──── P7── [P8]
         found. runbook   report/   evid./ investig.  assess cont.  export
                engine+   QA        custody                 
                VAPT                                        

TRACK B  W0───W1───────── W2─────────────  W3──────────────  W4───── W5──
         spine  A2 ext     A2 remaining     A3 all            A1 all  A4

MILESTONE        ▲                  ▲              ▲             ▲
            first real         VAPT cradle    Investigation  All pillars
            engagement         to grave       pillar live    live
            runs in platform
```

### Milestones that matter

| # | Milestone | Why it is the right thing to measure |
|---|---|---|
| **M1** | A real VAPT engagement runs through Phase 4 in the platform, with gates enforced | First proof the model works against reality rather than against a document |
| **M2** | A VAPT report is delivered from the platform, through QA, to an accepting client | The full value chain works once |
| **M3** | A forensic engagement runs with full custody and disposition | The forensics-specific capability is real |
| **M4** | All three pillars live; ≥20 runbooks approved | The platform is the way Sleuth works |

**M1 is the decision point for the whole programme.** If an Analyst who has run engagements the old way finds the platform *better*, continue. If it feels like compliance overhead, stop and fix that before building six more phases on a foundation people avoid. That question is answerable in Phase 1, and it is much cheaper to answer then than in Phase 6.

---

## 5. What is deliberately not in this plan

| Excluded | Why |
|---|---|
| Forensic analysis capability | The platform records and governs; it does not replace the examiner's toolkit (`06-evidence-model.md` §7) |
| Time tracking and billing | Decision D4 — changes the product's character; integrate instead |
| Client portal | Decision D2 — a seam, not a Phase 1 feature |
| Evidence content storage | Decision D1 — register-first; revisit at Phase 5 |
| Automated scanning or tool orchestration | Different product. The catalogue references tools; it does not run them |
| AI assistance | Not ruled out, but not now. On a platform whose entire value is evidentiary defensibility, generated content needs a much clearer provenance story before it goes anywhere near a finding or a report |
| Multi-tenancy | Single firm. Do not build for a market that does not exist yet |

---

## 6. The first thing to do after this review

1. Answer **D9** — which engagement types Sleuth actually sells, and in what volume. It determines the Phase 1 slice, and everything sequences from there.
2. Answer **D1** (evidence storage) and **D6** (hosting/residency) — both constrain infrastructure and are expensive to change later.
3. Name **Runbook Authors** per pillar (D8) and start Wave 0. This can begin immediately and in parallel with everything else; it is the critical path.
4. Confirm the legal questions **NC-09 to NC-15** with qualified counsel. Several change the forensic report format, and it is far cheaper to know now.
