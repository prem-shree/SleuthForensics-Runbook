# 11 — UX Structure

> **Status — `PROPOSED`, awaiting approval.** Structural and design proposals, not confirmed
> Sleuth practice. See [`17-governing-constraints.md`](17-governing-constraints.md). Partly superseded on arrival of Sleuth's engagement-type list —
> [`19-engagement-type-specification.md`](19-engagement-type-specification.md) §5.


Every screen below is worked through the brief's six questions before any layout is proposed: **Message · User · Context · Priority · Risk · UI**.

---

## 1. The design problem, stated once

A consultant opens the platform in one of four states:

| State | Frequency | What they need |
|---|---|---|
| Resuming known work | Most common | The next action, immediately |
| Starting unfamiliar work | Common | The procedure, with enough detail to do it correctly |
| Something unexpected happened | Occasional, high stakes | Stop conditions, escalation, who decides |
| Checking someone else's work | Reviewer | Claim + evidence, side by side |

The interface is optimised for the first — because it is most of the time — without making the third dangerous. That tension is the whole design brief: **surface less by default, but never hide the things that prevent serious mistakes.**

---

## 2. Screen: Engagement → Now  *(the North Star)*

> **Message** — "This is the one thing to do next, here is what you need to do it, and here is what to do if it goes wrong."
> **User** — Analyst. Occasionally the Engagement Manager checking state.
> **Context** — Mid-engagement. Possibly on a client site, possibly at 3am, possibly having been interrupted twenty minutes ago. Cognitive load already high.
> **Priority** — Start or complete the current procedure. Everything else is secondary.
> **Risk** — Doing the *wrong* next thing. Doing the right thing without capturing evidence. Missing a stop condition that has already been met. Working past an expired authorisation window.
> **UI** — One action, presented large and unambiguously. Evidence capture inline, not a separate trip. Stop conditions promoted to the primary view, never behind a tab. Blockers stated with an owner and a next step. Everything else collapsed.

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│ CLIENT CONFIDENTIAL · ENG-2026-0141 · Meridian Logistics · VAPT — External        │
├──────────────────────────────────────────────────────────────────────────────────┤
│ Phase 4 Examine  ·  SF-SEC-VAP-EXT v1.2  ·  Window closes 26 Sep 18:00 (2d 4h)   │
│ ████████████░░░░░░░░░░░░  Procedure 7 of 14                    ● 1 gate open      │
├──────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│  NEXT                                                          ~45 min · Analyst │
│  ┌────────────────────────────────────────────────────────────────────────────┐  │
│  │  Manual validation of identified vulnerabilities                           │  │
│  │                                                                            │  │
│  │  Confirm exploitability of the 23 candidate findings from automated        │  │
│  │  discovery. Do not exploit beyond proof of access.                         │  │
│  │                                                                            │  │
│  │  NEEDS       23 candidate findings · approved toolset · test account TA-02 │  │
│  │  PRODUCES    Validated findings with proof-of-concept evidence             │  │
│  │                                                                            │  │
│  │  ┌──────────────┐  ┌────────────┐  ┌──────────────────┐                    │  │
│  │  │   START      │  │  I'M       │  │  NOT APPLICABLE  │                    │  │
│  │  └──────────────┘  │  BLOCKED   │  └──────────────────┘                    │  │
│  │                    └────────────┘             ▸ Full procedure detail      │  │
│  └────────────────────────────────────────────────────────────────────────────┘  │
│                                                                                  │
│  ⬛ STOP IF                                                                       │
│     · Evidence of a pre-existing compromise is found     → STOP · escalate now   │
│     · A production system becomes unstable               → STOP · call client    │
│     · Testing reaches an asset outside approved scope    → STOP · do not proceed │
│     Escalation: R. Mehta (EM) +91 ····· · Client: J. Fernandes +91 ·····         │
│                                                                                  │
│  ⚠ BLOCKING — 1 item                                                             │
│     Third-party authorisation outstanding for 2 AWS-hosted assets.               │
│     Those assets are excluded from testing until resolved.                       │
│     Owner: R. Mehta · raised 2 days ago                        [ View gate ]     │
│                                                                                  │
│  ▸ Also assigned to me in this engagement (3)                                    │
│  ▸ Completed in this phase (6)                                                   │
└──────────────────────────────────────────────────────────────────────────────────┘
```

**Design decisions and why**

- **One next action, not a task list.** A list re-poses the question the screen exists to answer. If several procedures are genuinely available in parallel, one is presented as next by runbook sequence and the others sit under "Also assigned to me".
- **STOP IF is above the fold, with phone numbers.** At the moment a stop condition is met, a consultant is surprised, possibly alarmed, and will not navigate to find the escalation path. It must already be on screen. This is the clearest case in the whole product where surfacing information *by default* outweighs the tidiness of progressive disclosure.
- **"I'm blocked" is a first-class button.** If reporting a blocker is harder than working around it, people work around it — and the workaround is invisible until it surfaces in QA, or in a client's question six months later.
- **The window countdown is in the header.** Testing outside the authorised window is an authorisation breach, and time pressure is precisely when it happens.
- **Evidence capture is inside Start, not a separate destination.** Evidence reconstructed afterwards is weaker evidence, and often simply absent.

---

## 3. Screen: Procedure execution

> **Message** — "Here is exactly how to do this, what to capture, and what to do if reality does not match the procedure."
> **User** — Analyst, actively working, switching between this screen and their tools.
> **Context** — This screen sits *beside* a terminal or a forensic tool. It is a reference, not a destination.
> **Priority** — Complete the steps. Capture the required evidence.
> **Risk** — Skipping a step silently. Capturing evidence that is incomplete or unverifiable. Losing work when interrupted.
> **UI** — Steps with individual completion state. Evidence capture attached to the step that requires it. Persistent notes. Autosave. Nothing that requires the window to be full-width.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ ‹ Back to Now      Manual validation of identified vulnerabilities          │
│                    Procedure 7 of 14 · Phase 4 · ~45 min                    │
├─────────────────────────────────────────────────────────────────────────────┤
│ OBJECTIVE  Confirm which candidate findings are genuinely exploitable, so   │
│            severity reflects real risk rather than scanner output.          │
│                                                                             │
│ TOOLS      Capability: web request manipulation                             │
│            Approved: [ ─ select from catalogue ─ ]        3 approved tools  │
│            ⓘ Selection is recorded against the evidence you capture.        │
│                                                                             │
│ STEPS                                                                       │
│  ☑ 1  Review the 23 candidate findings and group by asset and type          │
│  ☑ 2  Confirm each target asset is in the approved scope list               │
│  ☐ 3  Validate each candidate, stopping at proof of access                  │
│        ⓘ Do not pivot. Do not access client data. Do not persist.           │
│  ☐ 4  Capture request/response evidence for every confirmed finding         │
│  ☐ 5  Record non-exploitable candidates with the reason                     │
│                                                                             │
│ EVIDENCE REQUIRED                                        2 of 4 captured    │
│  ✓ Request/response pair per confirmed finding    ENG-2026-0141-E011        │
│  ✓ Screenshot of proof of access                  ENG-2026-0141-E012        │
│  ○ Tool session log                                       [ + Capture ]     │
│  ○ Validation summary (confirmed vs discounted)           [ + Capture ]     │
│                                                                             │
│ ⬛ STOP IF   pre-existing compromise · production instability · out of scope │
│ ▲ ESCALATE   R. Mehta (EM) · out of hours +91 ·····                         │
│ ▸ Rationale, standards references and prior examples                        │
│                                                                             │
│ NOTES  ┌─────────────────────────────────────────────────────────────────┐  │
│        │ 4 candidates on SRV-WEB-03 appear to be false positives from    │  │
│        │ the WAF returning 200 on blocked requests. Verifying.           │  │
│        └─────────────────────────────────────────────────────────────────┘  │
│                                                       saved 14:22           │
│  [ Complete procedure ]   [ Save and pause ]   [ Blocked ]   [ N/A ]        │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Design decisions**

- **"Complete procedure" is disabled while required evidence is missing**, with the reason stated. Not a warning on submit — a visible precondition, so the requirement is known before the work rather than after it.
- **Tool selection is a catalogue lookup, not free text.** It records what was actually used against the evidence, which is what makes the work reproducible (`07-tools-and-templates.md`).
- **Notes autosave.** People get interrupted constantly in this work; losing a half-written observation is a real cost.
- **"Record non-exploitable candidates with the reason" is an explicit step.** Negative results are findings too — the Compromise Assessment report structure has a whole section for them — and they only exist if someone is asked to record them.

---

## 4. Screen: Gate

> **Message** — "You cannot proceed, here is exactly why, and here is who resolves each item."
> **User** — Engagement Manager, mostly. Analysts read it to understand a block.
> **Context** — Usually under schedule pressure, often with a client waiting.
> **Priority** — Resolve the unmet conditions. Failing that, understand the override path.
> **Risk** — The override becoming routine. A gate passed on stale conditions. Pressure producing a workaround outside the system.
> **UI** — Binary, unmissable status. Per-condition detail with owner and age. Override present but visibly weighty.

```
┌────────────────────────────────────────────────────────────────────────────┐
│  AUTHORISATION GATE                                            ● BLOCKED   │
│  Blocks: all technical execution (Phase 4)                                 │
├────────────────────────────────────────────────────────────────────────────┤
│  ✓  NDA executed                     2026-09-02 · A. Rao (CFO)             │
│  ✓  SOW executed                     2026-09-09 · A. Rao (CFO)             │
│  ✓  Scope approved                   2026-09-11 · 14 assets · 2 excluded   │
│  ✓  Testing window agreed            22–26 Sep · 09:00–18:00 IST           │
│  ✓  Emergency contacts recorded      both sides                            │
│                                                                            │
│  ✕  Letter of Authorisation          NOT RECEIVED                          │
│     Issued 2026-09-12 · awaiting signature · 8 days                        │
│     Owner: R. Mehta            [ Resend ]  [ Record as received ]          │
│                                                                            │
│  ✕  Rules of Engagement approved     DRAFT                                 │
│     Awaiting client approval · 3 days                                      │
│     Owner: R. Mehta            [ View draft ]  [ Send for approval ]       │
│                                                                            │
│  ✕  Third-party authorisation        2 OF 14 ASSETS PENDING                │
│     api.meridian-log.in, portal.meridian-log.in — AWS-hosted               │
│     Owner: J. Fernandes (client)        [ View request ]                   │
├────────────────────────────────────────────────────────────────────────────┤
│  3 conditions unmet. Technical execution cannot begin.                     │
│                                                                            │
│  [ Request override ]   Requires Management approval, a written            │
│                         justification, an expiry date, and appears in      │
│                         the client's report under Limitations.             │
└────────────────────────────────────────────────────────────────────────────┘
```

**Design decisions**

- **Every unmet condition names an owner and an age.** "Blocked" without an owner is how items sit for three weeks.
- **The override button states its full cost before it is pressed** — two approvals, a written justification, an expiry, and visibility to the client. Describing consequences at the point of decision is more effective than a confirmation dialog after it.
- **Conditions that are *met* stay visible.** Progress is information, and the passing conditions are also the record of what was checked.

---

## 5. Screen: Evidence capture

> **Message** — "Capture this properly now, because it cannot be reconstructed later."
> **User** — Analyst, sometimes standing in a server room.
> **Context** — Interruptible, occasionally on a phone, often with the item physically in hand.
> **Priority** — Complete, verifiable capture with an intact custody record.
> **Risk** — Missing hash. Missing timezone. Wrong engagement. Handling a source without write protection. A custody gap opening on day one.
> **UI** — The minimum required fields, defaulted aggressively from context. Hash verification visible and immediate. The engagement name unmissable.

```
┌─────────────────────────────────────────────────────────────────────────┐
│  REGISTER EVIDENCE                          ENG-2026-0141 · Meridian    │
├─────────────────────────────────────────────────────────────────────────┤
│  LEVEL        ( ) L0 Source   (•) L1 Raw   ( ) L2 Working copy          │
│  DERIVED FROM  —                                                        │
│                                                                         │
│  SOURCE        [ Dell Latitude 5420 · S/N 7K2M9Q3                     ] │
│  TYPE          [ Host ▾ ]        LOCATION FOUND [ Finance, 3rd floor  ] │
│  DESCRIPTION   [ Workstation of subject A, seized 2026-09-14 16:10    ] │
│                                                                         │
│  ACQUIRED      [ 2026-09-14 ] [ 16:40 ] [ IST (UTC+05:30) ▾ ]          │
│  EXAMINER      P. Nair (you)                                            │
│  METHOD        [ Physical image ▾ ]                                     │
│  TOOL          [ ─ select from catalogue ─ ▾ ]  version auto-recorded   │
│  WRITE BLOCK   (•) Hardware   ( ) Verified software   ( ) None          │
│                 ⚠ "None" requires a justification and is reported.      │
│                                                                         │
│  HASH          [ SHA-256 ▾ ]                                            │
│  ACQUISITION   [ 4f2a9c1e…c81d                                        ] │
│  VERIFICATION  [ 4f2a9c1e…c81d                                        ] │
│                ● MATCH — integrity verified                             │
│                                                                         │
│  STORAGE       [ Evidence safe A-3 ▾ ]   MEDIUM [ WD-EVID-011        ] │
│  CLASSIFY      [ Client Confidential ▾ ]  ☑ contains personal data      │
│                                                                         │
│                        [ Register evidence ]   [ Cancel ]               │
│                                                                         │
│  On registration: custody chain opens · ACQUIRED event recorded ·       │
│  Custody Gate evaluated · ID assigned                                   │
└─────────────────────────────────────────────────────────────────────────┘
```

**Design decisions**

- **Timezone is an explicit field, never inferred from the browser.** Cross-source timeline work fails silently when times are ambiguous, and an examiner in Mumbai imaging a laptop that logged in UTC needs both facts recorded, not reconciled from a guess.
- **Hash match is shown the instant both values are present**, with an unmissable state. A mismatch here stops the workflow immediately rather than surfacing at the Evidence Integrity Gate days later.
- **"No write blocker" is selectable but costly** — justification required, and it appears in the report. Real situations occasionally demand it; the system's job is to record the fact, not to pretend it never happens.
- **The engagement name is in the header of the capture form.** Misfiled evidence is among the most damaging errors possible here and is almost always a two-tabs-open mistake.

---

## 6. Screen: Today

> **Message** — "Here is your work, in the order that matters."
> **User** — Analyst and Reviewer, at the start of a day or after an interruption.
> **Context** — Possibly several engagements; possibly one urgent one.
> **Priority** — Enter the right engagement and resume.
> **Risk** — Burying an urgent incident under routine work. Review queues silently growing.
> **UI** — Ordered by consequence, not by date. Urgent work is visually distinct, not merely sorted first.

```
┌──────────────────────────────────────────────────────────────────────────┐
│  TODAY                                            P. Nair · Analyst      │
├──────────────────────────────────────────────────────────────────────────┤
│  ▌ACTIVE INCIDENT                                                        │
│  ▌ENG-2026-0147 · Northgate Health · Ransomware Investigation            │
│  ▌Phase 4 Examine · Day 2 · Emergency authorisation expires in 6h        │
│  ▌NEXT  Acquire memory from SRV-DC-01 before any restart                 │
│  ▌                                                        [ Continue ]   │
│                                                                          │
│  IN PROGRESS                                                             │
│  ENG-2026-0141 · Meridian Logistics · VAPT External                      │
│  Phase 4 · window closes in 2d 4h                                        │
│  NEXT  Manual validation of identified vulnerabilities    [ Continue ]   │
│                                                                          │
│  ENG-2026-0138 · Calder & Vance · Digital Forensics                      │
│  Phase 5 Analyse                                                         │
│  NEXT  Construct timeline from processed artefacts        [ Continue ]   │
│                                                                          │
│  WAITING ON OTHERS (2)                                                   │
│  ENG-2026-0141  Third-party authorisation · R. Mehta · 2d                │
│  ENG-2026-0138  Reviewer feedback on 3 findings · S. Kulkarni · 1d       │
│                                                                          │
│  DUE SOON                                                                │
│  ENG-2026-0129  Evidence disposition — 4 items · due in 5d               │
└──────────────────────────────────────────────────────────────────────────┘
```

**Design decisions**

- **The active incident is visually separated, not just sorted first.** A left rule and a distinct treatment; it should be impossible to scan past.
- **"Waiting on others" is a section, not a filter.** It is where work quietly dies, and it belongs on the screen people open every morning.
- **Evidence disposition appears here before it is overdue.** Disposition is the most-skipped obligation in the lifecycle (`06-evidence-model.md` §5), and the fix is visibility while there is still time.

---

## 7. Screen: Review

> **Message** — "Is this claim supported by this evidence?"
> **User** — Reviewer.
> **Context** — Reviewing someone else's work, under time pressure, possibly across several engagements.
> **Priority** — Judge each finding accurately and quickly.
> **Risk** — Approving an unsupported claim. Inconsistent severity across the practice. Review becoming a rubber stamp because the interface makes real checking expensive.
> **UI** — Claim and evidence side by side, never sequentially. Calibration data present. Rejection produces a worklist, not a comment.

```
┌────────────────────────────────────────────────────────────────────────────┐
│  REVIEW · ENG-2026-0141-F012                          Finding 4 of 11      │
├──────────────────────────────────┬─────────────────────────────────────────┤
│  THE CLAIM                       │  THE EVIDENCE                           │
│                                  │                                         │
│  Authentication bypass via       │  E011  Request/response pair            │
│  parameter manipulation on the   │        captured 2026-09-24 11:14        │
│  partner portal                  │        ┌─────────────────────────────┐  │
│                                  │        │ POST /api/v2/session        │  │
│  SEVERITY   ● HIGH               │        │ role=partner&elevate=true   │  │
│                                  │        │ → 200 {"role":"admin"}      │  │
│  RATIONALE                       │        └─────────────────────────────┘  │
│  Unauthenticated escalation to   │                                         │
│  admin on an internet-facing     │  E012  Screenshot — admin panel         │
│  portal holding partner          │        captured 2026-09-24 11:16        │
│  commercial data. No             │        [ view ]                         │
│  compensating controls observed. │                                         │
│                                  │  ⓘ Both items: integrity verified       │
│  ASSET  portal.meridian-log.in   │                                         │
│         in approved scope ✓      │  CALIBRATION                            │
│                                  │  6 comparable findings in the last 12   │
│  AUTHOR  P. Nair                 │  months rated: High ×5 · Critical ×1    │
├──────────────────────────────────┴─────────────────────────────────────────┤
│  [ Approve ]   [ Change severity ▾ ]   [ Reject with reason ▾ ]            │
│                                          insufficient evidence ·           │
│                                          severity disputed ·               │
│                                          reproduction unclear ·            │
│                                          out of scope · other              │
└────────────────────────────────────────────────────────────────────────────┘
```

**Design decisions**

- **Side by side, always.** If verifying a claim requires navigating away and back, verification gets skipped under load — and a QA gate that is skipped is worse than no gate, because it produces false assurance.
- **Calibration data is shown at the moment of judgement.** It is the only intervention that reliably improves severity consistency across a practice, and it is free once findings are structured.
- **Rejection reasons are a fixed list.** They become the rework signal (`08-reporting-architecture.md` §5). Free text cannot be aggregated, and aggregate rework data is how runbook gaps get found.

---

## 8. Screen: Oversight

> **Message** — "Where is the practice exposed right now?"
> **User** — Management.
> **Context** — Weekly review, or responding to something.
> **Priority** — Find the exceptions.
> **Risk** — A vanity dashboard. Management drifting into engagement content they should not routinely read.
> **UI** — Obligations and exceptions first, volume metrics second. Metadata only; opening engagement content is a deliberate, logged act.

Content, in priority order: **Obligations** — overdue evidence disposition, expiring authorisations, active gate overrides and their expiry, runbooks past review date, tool validations lapsed. **Exceptions** — engagements blocked more than N days, reviews older than N days, emergency authorisations unratified, integrity failures. **Flow** — engagements by phase, review queue depth, time-in-phase against typical. **Quality** — rework rate by service, rejection reasons, retest pass rate. **Commercial** — pipeline by service and urgency, utilisation *(Needs Confirmation: whether Sleuth wants time tracking in this platform at all — it changes the product's character considerably)*.

Deliberately absent from the default view: client names on the obligations list beyond what is needed to act, and any evidence content whatsoever.

---

## 9. Cross-cutting UX rules

1. **One next action.** Every screen makes the primary action obvious.
2. **Blocked is never silent.** Every block carries a reason, an owner and a next step.
3. **Evidence is captured where work happens**, never as a separate administrative trip.
4. **Stop conditions and escalation contacts are never more than zero clicks away** during execution.
5. **Destructive and irreversible actions state their consequence before confirmation**, and name what cannot be undone.
6. **Nothing is lost to an interruption.** Autosave everywhere; pausing is a supported state, not an abandonment.
7. **The client and engagement are always on screen.** Misattribution is the expensive error.
8. **Dense views are scannable.** Tabular data, aligned columns, monospace identifiers, no decorative chrome between the reader and the data.
9. **Colour never carries meaning alone.** Every state has a label and a shape as well as a colour — for accessibility, for print, and for the greyscale PDF someone will inevitably read.
10. **Print and export are designed, not inherited.** Chain-of-custody forms and authorisation letters get carried on paper into rooms where the platform is not available.
