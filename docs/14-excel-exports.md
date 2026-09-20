# 14 — Excel Export Layer

> The brief: *"Excel is a future output layer, not the primary system. The web application should remain the source of structured information."*

---

## 1. Position

Excel is a **projection**, never a source. Data is never authored in a workbook and imported back. The workbook is a rendering of platform state at a moment in time, for people and processes that live in spreadsheets — clients, auditors, insurers, and colleagues working offline.

Every generated workbook therefore carries a provenance header on every sheet:

```
SLEUTH FORENSICS                                    CLIENT CONFIDENTIAL
Engagement    ENG-2026-0141  Meridian Logistics — VAPT External
Runbook       SF-SEC-VAP-EXT v1.2
Generated     2026-09-24 16:42 IST  by  P. Nair
Source        Sleuth Runbook Platform — this export is a point-in-time extract
Checksum      a91c…4d27
```

The checksum lets an emailed workbook be matched back to the platform state that produced it. Every export is an audit event, recording who exported what, when, and with which filters.

## 2. Workbooks

### 2.1 Engagement Checklist
Columns per the brief: Phase · Procedure · Task · Requirement · Status · Owner · Due date · Completion date · Notes · Evidence reference.
Plus: Runbook ID and version · Gate · Blocked reason · N/A reason.
Grouped by phase with subtotals. Status values use a fixed enumeration so filtering works. Conditional formatting kept minimal and greyscale-safe.

### 2.2 Evidence Register
Evidence ID · Level · Parent ID · Source · Description · Acquisition date/time and timezone · Examiner · Method · Tool and version · Hash algorithm · Hash · Integrity status · Storage location · Storage medium · Classification · Custody event count · Custody complete (Y/N) · Current holder · Legal hold · Disposition status · Disposition date.
**Second sheet:** the full custody event stream, one row per event, which is what makes this exportable register genuinely useful to counsel.

### 2.3 Findings Register
Finding ID · Title · Severity · CVSS (where used) · Asset · Category · Description · Impact · Recommendation · Remediation effort · Status · Owner · Evidence references · Author · Reviewer · Retest outcome · Retest date · Client response.
Sorted by severity then asset. **This is the sheet clients actually work in**, tracking their own remediation — so column order is chosen for that use, and the remediation columns are left deliberately editable on the client's copy.

### 2.4 Client Questionnaire
Section · Question · Why we ask · Answer · Respondent · Date · Source · Confidence · Verified by · Verified date · Outstanding (Y/N).
Two modes: **blank** (for a client to complete offline, with `why we ask` visible — genuinely useful for long asset inventories) and **completed** (the record of what was asked and answered).

### 2.5 Engagement Tracker
Cross-engagement, for Management. Engagement ID · Client · Service · Engagement type · Archetype · Status · Current phase · Manager · Team · Start · Target end · Actual end · Gate status · Days in phase · Blocked days · Report status · Acceptance · Retest · Disposition status.

### 2.6 Additional workbooks worth having
- **Remediation Tracker** — findings filtered to open items, with owner and target date, for client-side tracking between delivery and retest.
- **Evidence Disposition Schedule** — practice-wide, what is due and overdue. The operational answer to the obligation identified in `06-evidence-model.md` §5.
- **Maturity Scorecard** (A1) — domain, control, current level, target level, gap, evidence source, recommendation, priority.
- **Asset Schedule** (A2) — the approved scope as signed, which is the reference document in any scope dispute.

## 3. Formatting

Professional and plain, matching the platform's visual language: Inter-equivalent for text, monospace for identifiers and hashes, frozen header rows, defined print areas, page headers with classification, no decorative fills, no emoji, no colour-only meaning. Severity uses a text label plus a muted fill that survives greyscale.

Hashes are formatted as text with a fixed column width — Excel will otherwise mangle long hex strings into scientific notation, which silently corrupts exactly the field that must not be wrong.

## 4. Phasing

Excel arrives in **Phase 7**, after the registers it projects exist and have stabilised. Building exports before the underlying model settles produces workbooks that must be rewritten with every schema change.

One exception is worth pulling forward: a simple **Findings Register** export is likely to be requested as soon as the first real engagement is delivered, because clients ask for it. Building that one export in Phase 2 alongside the findings register itself is reasonable and low-cost.

PDF generation for reports and chain-of-custody forms is a separate concern and arrives earlier — it is part of the reporting engine in Phase 2, not part of this layer.
