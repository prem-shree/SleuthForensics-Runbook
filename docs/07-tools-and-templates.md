# 07 — Tool Catalogue & Document Templates

> **Status — DRAFT / NEEDS SME VALIDATION.** Per Rule 1 of [`17-governing-constraints.md`](17-governing-constraints.md), nothing in this document is
> confirmed Sleuth practice. Procedures, tools, legal requirements and operational rules here are
> proposals for SME review, not internal SOP. Content drawn from the public website is
> `SITE-SUGGESTED` and carries no authority over internal method (Rule 6). Gaps are named rather
> than filled (Rule 2). Validation vocabulary: [`18-content-provenance-and-validation.md`](18-content-provenance-and-validation.md).
>
> **Rule 5 applies to Part B.** Every document template is a controlled draft. No workflow
> inside the platform can set `Counsel-approved`; that status is set only on recorded evidence
> of external legal review.


---

## PART A — Tool Catalogue

### 1. Why it is central rather than embedded

The brief is explicit: *"Runbooks should reference approved tools rather than hard-code tools everywhere. Do not assume one tool is universally required."*

Three reasons this matters operationally:

1. **Reproducibility.** A forensic report that says "imaged using standard tooling" is weak. One that names tool and version lets the work be reproduced — and lets Sleuth respond when a tool is later found to have a defect affecting a specific version.
2. **Defensibility.** "Was the tool validated?" is a fair question. Answering it requires a validation date and record, held somewhere other than an examiner's memory.
3. **Change cost.** Tools are replaced. If a tool name appears in 200 procedure texts, replacing it is a 200-edit project that will be done incompletely. If procedures reference a *capability* fulfilled by approved tools, it is one catalogue change.

### 2. Procedures reference capability, not product

```
PROCEDURE: Forensic acquisition of a powered-off workstation

  CAPABILITY REQUIRED:  Physical disk imaging with verification hashing
  APPROVED TOOLS:       [resolved from catalogue at execution time]
  SELECTED BY EXAMINER: <recorded on the evidence record>
  CONSTRAINT:           Write-blocking mandatory — hardware or verified software
```

The consultant sees the approved options for their platform and situation, picks one, and the choice is recorded against the evidence item. The runbook never has to be edited when the toolkit changes.

### 3. Tool record

| Field | Notes |
|---|---|
| `tool_id`, `name`, `vendor` | |
| `purpose` | One sentence |
| `capabilities[]` | What it fulfils — this is what procedures reference |
| `category` | Acquisition · Analysis · Scanning · Exploitation · Monitoring · Reporting · Utility |
| `services[]` / `archetypes[]` | Where it is applicable |
| `version` | Approval is **per version**, not per tool |
| `license_type` | Commercial · Open source · Internal · Client-provided |
| `license_ref`, `seat_count`, `expiry` | Renewal visibility |
| `approval_status` | `Approved` · `Approved with conditions` · `Under evaluation` · `Restricted` · `Prohibited` · `Deprecated` |
| `approval_conditions` | e.g. "lab use only", "not against production", "senior examiner only" |
| `platforms[]` | Windows · Linux · macOS · iOS · Android · Cloud · Appliance |
| `inputs[]`, `outputs[]` | Enables procedure input/output chaining |
| `limitations[]` | **Mandatory.** What it does *not* do, and where it is known to be unreliable |
| `validation_date`, `validated_by`, `validation_method`, `validation_ref` | The defensibility record |
| `next_validation_due` | Drives an Administration reminder |
| `alternatives[]` | Other tools with overlapping capability |
| `known_issues[]` | Version-specific defects and their impact |
| `data_handling_notes` | **Does this tool transmit data externally?** Critical for client-data tools |

`limitations` being mandatory is a deliberate authoring constraint. A catalogue entry that lists only what a tool can do is marketing; the operational value is in knowing where it will let you down.

`data_handling_notes` exists because of one recurring, serious mistake: uploading a client's suspected-malicious file to a public multi-scanner service is a disclosure of client data to third parties. The catalogue must make that visible at the point of use, and the Malware Analysis questionnaire makes sharing permission a blocking question (`05-questionnaire-architecture.md` §5).

### 4. Approval workflow

```
Proposed (Runbook Author)
   → Under evaluation        validation performed and recorded
   → Approved / Approved with conditions / Restricted / Prohibited   (Administrator)
   → Deprecated              superseded; existing engagements unaffected
```

The Readiness Gate checks that every tool planned for an engagement is currently Approved and within validation date. Using a non-approved tool is possible — reality demands it occasionally — but requires an exception with justification, which is recorded on the engagement and surfaces in the report's methodology section.

### 5. Seeding

**The catalogue ships empty.** The website names no tools (research §4.4), so populating it with an assumed stack would be inventing a capability claim. It is seeded by Sleuth during Phase 1 with what they actually own, license and have validated. The only pre-built content is the **capability taxonomy** — the vocabulary procedures reference — which is methodology-derived and vendor-neutral.

---

## PART B — Document Templates

### 6. Scope and a necessary caution

> These are **operational templates**. Every template in the library carries a permanent, non-dismissible banner:
>
> *"Operational template. Must be reviewed and approved by qualified legal counsel before use as a legal document. Template status: <Needs Legal Review | Counsel-Approved YYYY-MM-DD>."*
>
> The platform's contribution is **control and traceability** — which version was used, who approved it, what variables were filled, who signed, when — not legal drafting. No template reaches `Counsel-Approved` status through any workflow inside the platform; that status is set only on evidence of external legal review.

### 7. Template library

| Template | Phase | Applies to | Notes |
|---|---|---|---|
| Non-Disclosure Agreement | 1 | All | Mutual and one-way variants |
| Master Services Agreement | 1 | Repeat clients | Once per client, not per engagement |
| Statement of Work | 1 | All | Generated from scope + engagement type |
| Individual Engagement Agreement | 1 | `client_type = Individual` | Replaces MSA/SOW for spyware & personal matters |
| **Letter of Authorisation** | 2 | A2, A3 | **The single most important document in the system** |
| Rules of Engagement | 2 | A2 | Scope, windows, prohibited actions, deconfliction, emergency contacts |
| Third-Party Authorisation Request | 2 | A2 with hosted assets | For cloud/hosting providers and managed service providers |
| Scope Approval & Asset Schedule | 2 | All | The signed asset list — the reference for any later dispute |
| Emergency Authorisation Record | 0–2 | A3-E | Verbal authority captured, with a 24h ratification task |
| Consent & Device Ownership Declaration | 2 | Individual clients, spyware | Consent, ownership, employer-device disclosure |
| Evidence Handling Agreement | 2–4 | A3 | Handling standards, storage, access, retention |
| Chain of Custody Form | 4 | A3 | Generated from the custody event stream; printable for physical transfer |
| Evidence Receipt / Acknowledgement | 4 | A3 | Signed on physical handover |
| Change Request | Any | All | Scope changes — re-authorisation, not a note |
| Stop Notice | 4 | A2, A3 | Formal record of work halted, by whom, why |
| Retest Authorisation | 9 | A2 | Confirms the window and scope for verification |
| Report Acceptance | 7 | All | Closes delivery; starts the remediation clock |
| Evidence Return Acknowledgement | 10 | A3 | Signed by the receiving party |
| Certificate of Destruction | 10 | A3 | Method, performer, **witness**, date |
| Engagement Closure Summary | 10 | All | The formal end of the engagement |

### 8. Template mechanics

- **Variables, not find-and-replace.** Typed placeholders (`{{client.legal_name}}`, `{{engagement.scope.asset_count}}`, `{{authorisation.signatory.role}}`) resolved from engagement data. Fewer transcription errors, and it makes the scope in the SOW and the scope in the platform the same object rather than two things that drift.
- **Versioned and pinned.** A document instance records the template version used. Superseding a template never alters an executed document.
- **Execution record.** Signatories, their roles and how their authority was verified, dates, method (wet/e-sign/counter-signed), expiry where applicable, stored file reference and hash.
- **Gate integration.** The Authorisation Gate reads document instances directly. "NDA executed" is true because an executed NDA instance exists with a verified signatory — not because someone ticked a box.
- **Conditional clauses.** Context modules add clauses: OT engagements get safety clauses, individual clients get consent clauses, people-targeting engagements get staff-welfare clauses. Same composition principle as runbooks.

### 9. The Letter of Authorisation, specifically

It is worth stating why this one document is treated as the system's fulcrum. Authorised technical testing without documented authority is, at best, a serious professional failure and potentially far worse for the individual consultant who ran the command. The platform's position is unambiguous:

- The Authorisation Gate blocks **all** technical execution until an LoA instance exists.
- The LoA records the signatory, their **role**, and **how their authority to authorise was verified** — because a signature from someone without authority to give it provides no protection at all.
- It carries explicit validity dates. An expired LoA re-blocks the gate automatically.
- It enumerates the authorised scope and the prohibited actions.
- For A2, consultants can retrieve a copy on demand — including on a mobile device while on a client site, which is exactly where the question "who said you could do this?" gets asked.
