# 10 — Data Model

> **Status — `PROPOSED`, awaiting approval.** Structural and design proposals, not confirmed
> Sleuth practice. See [`17-governing-constraints.md`](17-governing-constraints.md). Partly superseded on arrival of Sleuth's engagement-type list —
> [`19-engagement-type-specification.md`](19-engagement-type-specification.md) §5.
>
> **Rules 3 and 4 constrain this schema.** No entity, field or relation holds client evidence
> content or any client secret. `storage_location` is an outward reference only.


---

## 1. Two planes

The single most consequential modelling decision in this system.

```
╔══════════════════════ CONTENT PLANE ══════════════════════╗
║  Authored · Versioned · Approved · Practice-wide          ║
║                                                            ║
║  Service ─ EngagementType ─ Runbook@version                ║
║                              ├─ Phase ─ Procedure ─ Task   ║
║                              ├─ ChecklistTemplate          ║
║                              ├─ GateDefinition             ║
║                              ├─ DecisionTree               ║
║                              └─ EvidenceRequirement        ║
║  QuestionnaireTemplate@version · ReportTemplate@version    ║
║  DocumentTemplate@version · Tool@version · KnowledgeArticle║
╚════════════════════════════╤═══════════════════════════════╝
                             │  PINNED AT PHASE 3
                             │  (version reference, never a copy-by-value
                             │   that can drift, never a live link that
                             │   can change underneath a running engagement)
╔════════════════════════════╧═══════════════════════════════╗
║  ══════════════════ EXECUTION PLANE ══════════════════     ║
║  Instantiated · Immutable history · Engagement-scoped      ║
║                                                            ║
║  Client ─ Engagement ─ EngagementPhase ─ TaskInstance      ║
║                      ├─ ChecklistInstance ─ ItemInstance   ║
║                      ├─ GateInstance ─ ConditionResult     ║
║                      ├─ QuestionnaireResponse ─ Answer     ║
║                      ├─ EvidenceItem ─ CustodyEvent        ║
║                      │                ─ AccessEvent        ║
║                      │                ─ IntegrityCheck     ║
║                      │                ─ Disposition        ║
║                      ├─ Finding ─ FindingEvidenceLink      ║
║                      ├─ Report@version ─ ReportSection     ║
║                      ├─ DocumentInstance                   ║
║                      ├─ DecisionRecord                     ║
║                      ├─ Escalation                         ║
║                      └─ AuditEvent  (append-only)          ║
╚════════════════════════════════════════════════════════════╝
```

**Why a reference rather than a copy.** Copying the runbook into the engagement would guarantee the historical record, but it would also fork 41 runbooks into hundreds of orphaned copies that can never be improved. A version *reference* into an immutable version store gives both: the engagement always renders exactly what it pinned, and the library stays maintainable.

---

## 2. Content plane entities

### Service
`service_id` · `display_name` (site-exact) · `short_name` · `pillar` (Security/Investigation/Resilience) · `site_slug` · `summary` · `related_services[]` · `active`

### EngagementType
`type_id` · `service_id` · `name` · `archetype` (A1–A4) · `runbook_id` · `default_context_modules[]` · `typical_duration` · `active`

### Runbook / RunbookVersion
`runbook_id` (`SF-SEC-VAP-EXT`) · `engagement_type_id` · `archetype`
**Per version:** `version` · `status` (Draft/In Review/Approved/Deprecated) · `owner_id` · `reviewer_id` · `approver_id` · `effective_from` · `effective_to` · `next_review_date` · `change_summary` · `change_history[]` · `composition{spine_v, archetype_v, service_module_v, context_modules[]}`

`composition` records exactly which module versions were combined. Without it, "v1.2" is a label; with it, it is a reproducible build.

### Phase → Procedure → Task
**Phase:** `phase_id` · `runbook_version_id` · `lifecycle_phase` (0–10) · `sequence` · `entry_criteria[]` · `exit_criteria[]` · `gate_ref`
**Procedure:** `procedure_id` · `phase_id` · `sequence` · `objective` · `rationale` · `preconditions[]` · `inputs[]` · `outputs[]` · `capability_refs[]` · `evidence_requirements[]` · `decision_tree_refs[]` · `stop_conditions[]` · `escalation_conditions[]` · `approval_required` · `estimated_duration` · `role` · `kb_refs[]` · `optional` · `context_module_id` (null = core)
**Task:** `task_id` · `procedure_id` · `sequence` · `instruction` · `expected_result` · `duration` · `parallel_ok`

### Templates
**ChecklistTemplate / ItemTemplate:** `requirement` (Required/Optional/Conditional) · `condition_expr` · `evidence_required` · `verification_method`
**GateDefinition / GateCondition:** `condition_expr` (evaluated against engagement state) · `failure_message` · `remediation_hint` · `overridable` (false for the Custody Gate)
**QuestionnaireTemplate → Section → Question:** `question_type` · `blocking` · `required` · `condition_expr` · `triggers_context_module` · `help_text` · `why_we_ask`
**ReportTemplate → Section:** `required` · `auto_generated` · `source_query` · `condition_expr`
**DocumentTemplate:** `variables[]` · `conditional_clauses[]` · `legal_review_status` · `legal_reviewed_at`
**DecisionTree → Node → Branch:** `node_type` (Question/Action/Stop/Escalate/Terminal) · `condition` · `next_node_id` · `records_decision`
**Tool / ToolVersion:** per `07-tools-and-templates.md` §3
**KnowledgeArticle:** `article_id` · `title` · `body` · `tags[]` · `linked_procedures[]` · `source_engagement_id` (for lessons learned) · `version`

`why_we_ask` on Question is small and disproportionately valuable: it lets a consultant explain to a client why a question matters, in the client's words, without improvising.

---

## 3. Execution plane entities

### Client
`client_id` · **`client_type` (Organisation | Individual)** · `legal_name` · `display_name` · `sector` (9-value list) · `regulated` + `regulators[]` · `size_band` · `locations[]` · `status` · `conflict_notes` · `standing_agreements[]` · `default_classification`

The `client_type` split is not cosmetic. An Individual has no MSA, no corporate signatory, different consent requirements and — in spyware and domestic-surveillance matters — materially different safety handling (research §4.2).

### ClientContact
`contact_id` · `client_id` · `name` · `role` · `email` · `phone` · `is_authorised_signatory` · `authority_verified_by` · `authority_verified_at` · `is_emergency_contact` · `receives_reports` · `excluded_from_distribution` (for investigations where a contact is a subject)

### Engagement
`engagement_id` (`ENG-2026-0141`) · `client_id` · `service_id` · `engagement_type_id` · **`runbook_version_id` (pinned, immutable)** · `parent_engagement_id` (child engagements) · `name` · `status` · `current_phase` · `classification` · `urgency` (the four contact-form values) · `is_emergency` · `active_context_modules[]` · `manager_id` · `team_members[]` (role + from/to) · `start_date` · `target_end_date` · `actual_end_date` · `scope_approved_at` · `authorisation_expires_at` · `legal_hold`

### Scope & Assets
**ScopeAsset:** `asset_id` · `engagement_id` · `identifier` (IP/CIDR/domain/hostname/app/account/device) · `type` · `description` · `environment` (Production/Staging/Dev/Unknown) · `ownership` (Client/Third-party/SaaS) · `third_party_authorised` · `in_scope` · `exclusion_reason` · `criticality` · `fragile` · `verified_by` · `verified_at`
**ScopeChange:** `requested_by` · `requested_at` · `description` · `impact` · `approved_by` · `approved_at` · `document_instance_id`

`environment` and `ownership` are not descriptive fields — they are inputs to gate conditions and context-module attachment. A single asset marked `Third-party` with `third_party_authorised = false` blocks the Authorisation Gate.

### Execution records
**EngagementPhase:** status · started/completed · gate_instance_id
**TaskInstance:** `status` (Not started/In progress/Complete/Blocked/Needs review/Not applicable) · `owner_id` · `started_at` · `completed_at` · `notes` · `evidence_refs[]` · `blocked_reason` · `na_reason`
**ChecklistItemInstance:** `state` (Required/Optional/Completed/Not applicable/Blocked/Needs review) · `evidence_ref` · `note` · `owner_id` · `completed_at` — exactly the state set the brief specifies
**GateInstance:** `state` (Blocked/Ready/Passed/Overridden) · `condition_results[]` (snapshotted at pass) · `passed_by` · `passed_at` · `override{requested_by, approved_by, justification, expires_at, remediation_task_id}`
**DecisionRecord:** `decision_tree_id` · `node_path[]` · `outcome` · `decided_by` · `decided_at` · `rationale`
**Escalation:** `trigger` · `severity` · `raised_by` · `raised_at` · `escalated_to` · `acknowledged_at` · `resolution` · `work_paused`

Snapshotting `condition_results` at the moment a gate passes matters: it records *why the gate was passable then*, which is the question asked later when something turns out to have been wrong.

### Evidence cluster
Per `06-evidence-model.md`. `EvidenceItem` (with `level`, `parent_evidence_id`, hashes, `integrity_status`, `legal_hold`, `disposition_status`), `CustodyEvent` (append-only), `AccessEvent`, `IntegrityCheck`, `Disposition`.

### Finding & FindingEvidenceLink
Per `08-reporting-architecture.md` §1. The link table is the enforcement point for "no finding without evidence" — a constraint at the database level, not a validation rule that can be bypassed by an import.

### Report / DocumentInstance
**Report:** `report_id` · `engagement_id` · `report_template_version_id` · `version` · `status` · `author_id` · `reviewer_id` · `qa_passed_at` · `released_at` · `released_by` · `recipients[]` · `file_ref` · `file_hash` · `accepted_at` · `accepted_by`
**DocumentInstance:** `document_template_version_id` · `type` · `status` (Draft/Issued/Executed/Expired/Superseded) · `variables_resolved{}` · `signatories[]{name, role, authority_verified_by, signed_at, method}` · `executed_at` · `valid_from` · `valid_until` · `file_ref` · `file_hash`

### AuditEvent (append-only, hash-chained)
`event_id` · `sequence` · `timestamp` · `actor_id` · `actor_role` · `engagement_id` · `object_type` · `object_id` · `action` · `before{}` · `after{}` · `ip` · `user_agent` · `session_id` · `privileged` · `prev_hash` · `hash`

Hash-chaining makes tampering detectable rather than merely prohibited — the difference between a policy and a property.

---

## 4. Relationships worth stating explicitly

```
Client 1──* Engagement *──1 EngagementType *──1 Service
Engagement 1──1 RunbookVersion            (PINNED, immutable)
Engagement 1──* Engagement                (parent → child engagements)
Engagement 1──* ScopeAsset
Engagement 1──* EvidenceItem 1──* CustodyEvent   (append-only)
EvidenceItem *──1 EvidenceItem            (provenance: parent → derived)
Finding *──* EvidenceItem                 (≥1 REQUIRED — enforced in the DB)
Finding 1──* SeverityChange
Report *──* Finding
Report 1──1 ReportTemplateVersion         (PINNED)
DocumentInstance 1──1 DocumentTemplateVersion (PINNED)
GateInstance *──1 GateDefinition
Everything 1──* AuditEvent
```

### Invariants the system enforces

1. `Finding.evidence_refs.count ≥ 1` before a finding can enter a report.
2. `author_id ≠ reviewer_id` on findings, reports and gate approvals.
3. `EvidenceItem.level ∈ {L2,L3,L4} ⟹ parent_evidence_id IS NOT NULL`.
4. A `RunbookVersion` with `status = Approved` is immutable.
5. `CustodyEvent` and `AuditEvent` are insert-only — no update, no delete, at any privilege level.
6. An engagement cannot leave Phase 3 without `runbook_version_id` set.
7. An engagement cannot reach `Closed` with any evidence item in `disposition_status = null`.
8. `integrity_status = FAILED` cannot be changed to any other value.

---

## 5. Identifier scheme

Identifiers are read aloud, typed into chat, and written on physical evidence bags. They are designed for that.

| Object | Format | Example |
|---|---|---|
| Engagement | `ENG-YYYY-NNNN` | `ENG-2026-0141` |
| Evidence | `<ENG>-E<nnn>` | `ENG-2026-0141-E007` |
| Finding | `<ENG>-F<nnn>` | `ENG-2026-0141-F012` |
| Runbook | `SF-<PILLAR>-<SVC>-<TYPE>` | `SF-SEC-VAP-EXT` |
| Report | `<ENG>-RPT-v<n>` | `ENG-2026-0141-RPT-v2` |
| Document | `<ENG>-DOC-<TYPE>-<n>` | `ENG-2026-0141-DOC-LOA-1` |
| Client | `CLI-NNNN` | `CLI-0087` |

Short, unambiguous, no lookalike characters, rendered in IBM Plex Mono throughout the UI, and stable for the life of the record.

---

## 6. Technical direction *(recommendation — Decision D5)*

Not asked for explicitly, but it shapes the phasing, so it is stated as a proposal rather than a decision:

- **PostgreSQL.** The model is relational, constraint-heavy and audit-critical. Referential integrity is a feature here, not overhead. Row-level security supports engagement scoping at the database rather than only in application code. JSONB covers the genuinely variable parts (questionnaire answers, condition results).
- **Server-rendered application with targeted interactivity.** Dense tables, forms, print-quality output and strong URL semantics. A single-page framework buys little here and costs offline-state complexity in an app whose correctness depends on the server's view of state.
- **No evidence content storage at all** (Rule 3). No object store, no upload path, no signed-download infrastructure. The evidence register holds metadata, hashes, provenance, custody, access history and disposition; `storage_location` is an outward reference to where Sleuth actually holds the item.
- **No client secrets** (Rule 4). No entity or field is typed to hold a credential, key or password.
- **Append-only audit via insert-only tables** with hash chaining and periodic external anchoring.
- **Self-hosted, India region** pending confirmation of data residency requirements (Decision D6).

Deliberately deferred: background job infrastructure until A4 recurring cycles need it (Phase 6); search beyond PostgreSQL full-text until volume justifies it.
