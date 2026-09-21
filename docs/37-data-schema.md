# 37 — Data Schema

> **Status — `PROPOSED`, implementation-ready.** Supersedes `10-data-model.md` for field-level
> detail; `10` remains the conceptual overview. PostgreSQL-flavoured, per Decision D5.
>
> **Rule 7 still applies: this is a specification, not code.** No DDL is committed to this repository.

---

## 1. Conventions

| | |
|---|---|
| Primary keys | `uuid` internally. **Human identifiers are separate columns** (`ENG-2026-0141`) — unique, immutable, and what people actually type and say |
| Timestamps | `timestamptz` always. A naive timestamp in a forensic system is a defect |
| Timezone | Where an *observed* time matters (evidence acquisition, incident events), store both `occurred_at timestamptz` and `source_timezone text` — normalisation must be reversible |
| Enums | Postgres `enum` types for closed vocabularies; `text` + check constraint where Sleuth may extend |
| Soft delete | **None.** Records are closed, superseded or dispositioned. Nothing is deleted |
| Audit | Every mutating statement writes an `audit_event`. Enforced by trigger, not by application discipline |
| Money / time tracking | **Absent by design** *(Decision D4)* |
| Secrets | **No column anywhere is typed to hold one** *(Rule 4)* |
| Evidence content | **No column anywhere holds it** *(Rule 3)* |

---

## 2. Content plane

Versioned, approved, practice-wide. Written by Runbook Authors, validated by SMEs, approved by
Management.

### `service`
`id` · `code` · `display_name` *(site-exact)* · `short_name` · `pillar` enum(security, investigation, resilience) · `site_slug` · `summary` · `active` · `provenance` · `provenance_ref`

### `engagement_type`
`id` · `code` *(`SF-A2-IPT`)* · `name` · `archetype` enum(A1,A2,A3,A4) · `sold_as` enum(project, time_boxed, retainer, emergency) · `typical_duration_days` · `active`
`engagement_type_service` — many-to-many to `service` with `is_primary bool`

### `engagement_type_mode` · `domain_pack` · `incident_type_module`
Each: `id` · `engagement_type_id` · `code` · `name` · `description` · `default bool` · `sequence`

### `module` / `module_version`
The shared-module store (`20-shared-module-inheritance.md`).
`module`: `id` · `code` *(`core.evidence`, `arch.A2`, `service.ipt`, `ctx.production`)* · `kind` enum(core, archetype, service, context) · `owner_id`
`module_version`: `id` · `module_id` · `version` semver · `status` enum(draft, in_review, approved, deprecated) · `change_class` enum(editorial, substantive, breaking) · `change_summary` · `effective_from` · `effective_to` · `next_review_date` · `author_id` · `approver_id` · `approved_at`

### `runbook` / `runbook_version`
`runbook`: `id` · `code` · `engagement_type_id` · `archetype`
`runbook_version`: `id` · `runbook_id` · `version` · `status` · `owner_id` · `reviewer_id` · `approver_id` · `effective_from` · `effective_to` · `next_review_date` · `change_summary`
`composition_manifest` — `runbook_version_id` · `slot` · `module_version_id` · `sequence`
**The manifest is the runbook.** Content is never copied into it.

### `phase` · `procedure` · `task`
`phase`: `id` · `module_version_id` · `lifecycle_phase` smallint(0–10) · `sequence` · `entry_criteria[]` · `exit_criteria[]` · `gate_definition_id`
`procedure`: `id` · `phase_id` · `code` *(`EV-03`)* · `sequence` · `objective` · `rationale` · `preconditions[]` · `inputs[]` · `outputs[]` · `estimated_minutes` · `role` · `optional bool` · `approval_required` enum(none, reviewer, manager, management, client) · **`provenance`** · **`validation_status`** · `validated_by` · `validated_at` · `validation_note` · `revalidation_due`
`task`: `id` · `procedure_id` · `sequence` · `instruction` · `expected_result` · `estimated_minutes` · `parallel_ok bool`

### `extension_point`
`id` · `procedure_id` · `slot_name` · `position` enum(before, after, replace_optional) · `description`
`extension_injection` — `extension_point_id` · `injecting_module_version_id` · `content_procedure_id`

### `delta`
Approved divergence from inherited content.
`id` · `module_version_id` *(the diverging module)* · `target_procedure_id` · `reason` · `author_id` · `approved_by_id` · `approved_at` · `review_by` · `active bool`
**Constraint:** `author_id <> approved_by_id`

### `gap`
Rule 2's alternative to invention.
`id` · `code` · `scope_type` enum(module, procedure, engagement_type, questionnaire, report_template) · `scope_id` · `description` · `consequence` · `blocking bool` · `blocking_reason` · `owner_id` · `opened_at` · `closed_at` · `closed_by_decision_ref`

### `capability` · `tool` · `tool_version` · `tool_validation`
`capability`: `id` · `code` *(`CAP-ACQ-01`)* · `category` · `name` · `max_intrusiveness_level` smallint null
`tool`: `id` · `name` · `vendor` · `purpose` · `license_type` · `license_ref` · `data_handling_notes` **not null**
`tool_version`: `id` · `tool_id` · `version` · `approval_status` enum(proposed, under_evaluation, approved, approved_with_conditions, restricted, prohibited, deprecated) · `approval_conditions` · `platforms[]` · `limitations[]` **not null** · `known_issues[]`
`tool_capability` — `tool_version_id` · `capability_id`
`tool_validation`: `id` · `tool_version_id` · `method` · `performed_by_id` · `performed_at` · `result` · `reference` · `next_due`

### Templates
`questionnaire_template` / `question_section` / `question`
`question`: `id` · `section_id` · `code` · `text` · `question_type` · `required bool` · **`blocking bool`** · **`must_be_verified bool`** · `condition_expr` · `triggers_context_module_id` · `help_text` · `why_we_ask` · `sequence`

`report_template` / `report_section`
`report_section`: `id` · `report_template_version_id` · `code` · `title` · `required bool` · `deletable bool` · `generated bool` · `source_query` · `condition_expr` · `sequence`

`document_template` / `document_template_version`
`document_template_version`: `id` · `template_id` · `version` · `variables[]` · `conditional_clauses[]` · **`legal_review_status`** enum(draft_not_reviewed, under_legal_review, counsel_approved, counsel_approved_expired) · `legal_reviewed_by` · `legal_reviewed_at`
**Constraint:** `legal_review_status = 'counsel_approved'` requires `legal_reviewed_by` and
`legal_reviewed_at` non-null. **No application path sets this** *(Rule 5)*.

`checklist_template` / `checklist_item_template` · `gate_definition` / `gate_condition` ·
`decision_tree` / `decision_node` / `decision_branch` · `evidence_requirement` · `knowledge_article`

`gate_condition`: `id` · `gate_definition_id` · `code` · `expression` · `evaluation_kind` enum(**fact**, attestation) · `failure_message` · `remediation_hint` · `applies_when` · `sequence`

---

## 3. Execution plane

### `client`
`id` · `code` *(`CLI-0087`)* · **`client_type`** enum(organisation, individual) · `legal_name` · `display_name` · `sector` · `regulated bool` · `regulators[]` · `size_band` · `locations[]` · `status` · `conflict_notes` · `default_classification`

### `client_contact`
`id` · `client_id` · `name` · `role` · `email` · `phone` · `is_authorised_signatory bool` · `authority_verified_by_id` · `authority_verified_at` · `is_emergency_contact bool` · `reachability_confirmed_at` · `receives_reports bool` · **`excluded_from_distribution bool`** · `exclusion_reason` · `is_sleuth_vciso bool`

### `engagement`
`id` · `code` *(`ENG-2026-0141`)* · `client_id` · `engagement_type_id` · **`runbook_version_id`** · `parent_engagement_id` · `name` · `status` · `current_phase` · `classification` · `urgency` enum(general, planning, upcoming, urgent_active_incident) · `is_emergency bool` · `selected_mode_id` · `selected_incident_module_id` · **`intrusiveness_level`** smallint(1–3) · `manager_id` · `start_date` · `target_end_date` · `actual_end_date` · `authorisation_expires_at` · `legal_hold bool` · `is_pilot bool`
`engagement_domain_pack` · `engagement_context_module` · `engagement_member` *(user, role, from, to)*

### `scope_asset`
`id` · `engagement_id` · `identifier` · `asset_type` · `description` · **`environment`** enum(production, staging, development, unknown) · **`ownership`** enum(client, third_party, saas) · **`ownership_verified_by_id`** · `ownership_verified_at` · `third_party_authorised bool` · `in_scope bool` · `exclusion_reason` · `criticality` · `fragile bool` · `intrusiveness_override` smallint

### `scope_change`
`id` · `engagement_id` · `requested_by_id` · `requested_at` · `description` · `impact` · `approved_by_id` · `approved_at` · `document_instance_id`

### `access_grant` — Rule 4's mechanism
`id` · `engagement_id` · `reference` *(`TA-02`)* · `purpose` · `role_or_privilege` · `delivery_channel` enum(client_vault, secure_channel, in_person, client_managed) · `delivered_by` · `delivered_at` · `verified_working_by_id` · `verified_at` · `expires_at` · **`revocation_confirmed_by`** · `revocation_confirmed_at`
**There is no credential column.** A `CHECK` on free-text fields flags high-entropy strings; the
primary control is that no legitimate place exists.

### Execution records
`engagement_phase` · `task_instance` · `checklist_instance` / `checklist_item_instance` ·
`questionnaire_response` / `answer` · `gate_instance` / `gate_condition_result` ·
`decision_record` · `escalation`

`checklist_item_instance`: `id` · `checklist_instance_id` · `item_template_id` · `state` enum(not_started, completed, not_applicable, blocked, needs_review) · `evidence_item_id` · `note` · **`na_reason`** · **`blocked_reason`** · **`blocked_owner_id`** · `owner_id` · `completed_by_id` · `completed_at` · `attestation_basis`
**Constraints:** `state='not_applicable'` requires `na_reason`; `state='blocked'` requires
`blocked_reason` and `blocked_owner_id`.

`answer`: `id` · `questionnaire_response_id` · `question_id` · `value jsonb` · `respondent` · `answered_at` · **`source`** enum(client_stated, sleuth_observed, inferred, document) · **`confidence`** enum(high, medium, low, unverified) · `verified_by_id` · `verified_at` · `unavailable_reason`

`gate_instance`: `id` · `engagement_id` · `gate_definition_id` · `state` enum(blocked, ready, passed, overridden) · `passed_by_id` · `passed_at` · **`condition_snapshot jsonb`** · `override_requested_by_id` · `override_approved_by_id` · `override_justification` · `override_expires_at` · `override_remediation_task_id`
**Constraint:** override requires `requested_by <> approved_by`, an expiry, and a remediation task.
**Constraint:** `gate_definition.overridable = false` forbids any override column being set
*(Custody, Release)*.

`decision_record`: `id` · `engagement_id` · `decision_tree_id` · `node_path jsonb` · `outcome` · `decided_by_id` · `decided_at` · `rationale`

---

## 4. Evidence cluster — register only

> **No table in this cluster holds evidence content.** `storage_location` points outward.

### `evidence_item`
`id` · `code` *(`ENG-2026-0141-E007`)* · `engagement_id` · **`level`** enum(L0…L5) · **`parent_evidence_id`** · `source_description` · `source_type` · `client_asset_ref` · `description` · **`acquisition_at timestamptz`** · **`source_timezone`** · `acquisition_method` · `tool_version_id` · `examiner_id` · `write_blocker_used` enum(hardware, verified_software, none) · `write_blocker_justification` · **`hash_algorithm`** · **`acquisition_hash`** · `additional_hashes jsonb` · `verification_hash` · `verified_by_id` · `verified_at` · **`integrity_status`** enum(verified, pending, failed, not_applicable) · `size_bytes` · `file_count` · **`storage_location`** · `storage_medium_id` · `classification` · `contains_personal_data bool` · `legal_hold bool` · `retention_until` · `disposition_status`

**Constraints**
- `level IN ('L2','L3','L4') ⇒ parent_evidence_id IS NOT NULL`
- `integrity_status='failed'` is terminal — a trigger rejects any transition away from it
- `write_blocker_used='none' ⇒ write_blocker_justification IS NOT NULL`

### `custody_event` — append-only
`id` · `evidence_item_id` · `sequence` · `event_type` enum(acquired, verified, transferred, received, accessed, copy_derived, processed, stored, sealed, unsealed, hold_applied, hold_released, returned, destroyed) · `occurred_at` · `actor_id` · `counterparty` · `method` · `container_seal_ref` · `condition_notes` · `prev_hash` · `hash`
**No UPDATE, no DELETE.** Enforced by table privileges, not application code.

### `access_event`
`id` · `evidence_item_id` · `user_id` · `role` · `occurred_at` · `purpose` enum · `action` enum(view_metadata, open, export) · `ip` · `user_agent` · `bulk_operation_id`

### `integrity_check` · `disposition`
`disposition`: `id` · `evidence_item_id` · `instruction` enum(return, destroy, retain) · `authorised_by_id` · `authorised_at` · `scheduled_for` · `executed_at` · `method` · `performed_by_id` · **`witnessed_by_id`** · `certificate_ref` · `acknowledgement_ref`
**Constraint:** `instruction='destroy' AND executed_at IS NOT NULL ⇒ witnessed_by_id IS NOT NULL`
and `performed_by_id <> witnessed_by_id`

---

## 5. Findings & reports

### `finding`
`id` · `code` *(`ENG-2026-0141-F012`)* · `engagement_id` · **`finding_kind`** enum(vulnerability, control_gap, finding_of_fact) · `title` · `severity` enum(critical, high, medium, low, informational) · **`severity_rationale` not null** · `cvss_vector` · `category` · `description` · `impact` · `recommendation` · `remediation_effort` · `reproduction_steps` · `status` · **`author_id`** · **`reviewer_id`** · `reviewed_at`
*Kind-specific:* `control_ref` · `current_state` · `target_state` · **`source_citation`** *(control_gap)* · **`confidence`** enum · **`alternatives_considered`** · `answers_question_id` *(finding_of_fact)*
**Constraints:** `author_id <> reviewer_id` · `finding_kind='control_gap' ⇒ source_citation NOT NULL` · `finding_kind='finding_of_fact' ⇒ confidence AND alternatives_considered NOT NULL`

`finding_evidence` — `finding_id` · `evidence_item_id` · `role`
**Invariant enforced at report assembly:** a finding with zero rows here cannot enter a report.

`severity_change` — `finding_id` · `from_severity` · `to_severity` · `changed_by_id` · `changed_at` · `rationale`
`retest` — `finding_id` · `outcome` enum(resolved, partially_resolved, not_resolved, risk_accepted, unable_to_verify) · `tested_by_id` · `tested_at` · `notes` · `risk_accepted_owner` · `risk_accepted_until`

### `report` · `report_section_instance` · `document_instance`
`report`: `id` · `code` · `engagement_id` · `report_template_version_id` · `version` · `status` · `author_id` · `reviewer_id` · `qa_passed_at` · `released_at` · `released_by_id` · `recipients jsonb` · `file_ref` · **`file_hash`** · `frozen_at` · `accepted_at` · `accepted_by`
`document_instance`: `id` · `code` · `engagement_id` · `document_template_version_id` · `doc_type` · `status` · `variables_resolved jsonb` · `signatories jsonb` *(name, role, authority_verified_by, signed_at, method)* · `executed_at` · `valid_from` · `valid_until` · `file_ref` · `file_hash`

---

## 6. Audit — append-only, hash-chained

### `audit_event`
`id` · `sequence bigserial` · `occurred_at` · `actor_id` · `actor_role` · `engagement_id` · `object_type` · `object_id` · `action` · `before jsonb` · `after jsonb` · `ip` · `user_agent` · `session_id` · `privileged bool` · `break_glass bool` · **`prev_hash`** · **`hash`**

`hash = sha256(sequence ‖ occurred_at ‖ actor_id ‖ object_type ‖ object_id ‖ action ‖ before ‖ after ‖ prev_hash)`

Periodically anchored to external storage, so tampering is **detectable**, not merely prohibited.
No role holds UPDATE or DELETE on this table — Administrator included.

---

## 7. Enforced invariants

| # | Invariant | Mechanism |
|---|---|---|
| 1 | Finding needs ≥1 evidence link before entering a report | Assembly-time check + trigger |
| 2 | `author_id <> reviewer_id` on finding, report, gate pass | `CHECK` |
| 3 | L2–L4 evidence requires a parent | `CHECK` |
| 4 | Approved `runbook_version` / `module_version` immutable | Trigger rejects UPDATE |
| 5 | `custody_event`, `audit_event` insert-only | Table privileges |
| 6 | No engagement leaves Phase 3 without `runbook_version_id` | Trigger |
| 7 | No engagement closes with evidence lacking a disposition | Closure Gate condition + trigger |
| 8 | `integrity_status='failed'` is terminal | Trigger |
| 9 | No column holds a credential | Schema review + entropy check on free text |
| 10 | No column holds evidence content | Schema review |
| 11 | `runbook_version` cannot be `approved` while a composed procedure is `draft`/`in_review` | Trigger over the manifest |
| 12 | `delta` requires `author <> approver` and a `review_by` | `CHECK` |
| 13 | Authorisation Gate signatory must not be `is_sleuth_vciso` for that client | Gate condition |
| 14 | Destruction requires a witness distinct from the performer | `CHECK` |
| 15 | Non-overridable gates reject override columns | `CHECK` on `gate_definition.overridable` |

---

## 8. Row-level security

```
engagement-scoped tables
  USING ( engagement_id IN (
            SELECT engagement_id FROM engagement_member
            WHERE user_id = current_user_id()
              AND now() BETWEEN valid_from AND coalesce(valid_to,'infinity')
          )
          OR current_setting('app.break_glass', true) = 'on' )
```

Break-glass sets a session flag, writes an `audit_event` with `break_glass=true`, notifies the
Engagement Manager, and expires. **Defence in depth: the database refuses even when a `WHERE` clause
is forgotten.** Application-layer-only scoping fails open on the first mistake.

---

## 9. Indexes worth specifying now

`engagement(client_id, status)` · `engagement(runbook_version_id)` · `scope_asset(engagement_id, in_scope)` · `evidence_item(engagement_id, level)` · `evidence_item(acquisition_hash)` *(the "which engagements used this artefact?" query)* · `custody_event(evidence_item_id, sequence)` · `finding(engagement_id, severity)` · `audit_event(engagement_id, occurred_at)` · `audit_event(object_type, object_id)` · GIN on `answer.value` and `gate_instance.condition_snapshot`.

---

## 10. Placeholders

| Ref | Placeholder | Default applied |
|---|---|---|
| `‹PH-13›` | Retention periods per record class | Configurable; **no default hard-coded** *(counsel, E5)* |
| `‹PH-14›` | Identity provider integration | Local accounts + OIDC-ready; SSO on confirmation *(C5)* |
| `‹PH-15›` | `storage_location` vocabulary | Free text until Sleuth describes their actual storage *(C3)* |
| `‹PH-16›` | Classification vocabulary | `Client Confidential · Restricted · Privileged · Personal Data` |
| `‹PH-17›` | Sector list | The 9 from the industries page |

---

## 11. Counts

| | |
|---|---|
| Tables | **61** |
| Content plane / execution plane | 27 / 34 |
| Enforced invariants | 15 |
| Append-only tables | 2 |
| Tables holding evidence content | **0** |
| Columns typed to hold a secret | **0** |
