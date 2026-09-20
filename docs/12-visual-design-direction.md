# 12 — Visual Design Direction

> **Status — `PROPOSED`, awaiting approval.** Structural and design proposals, not confirmed
> Sleuth practice. See [`17-governing-constraints.md`](17-governing-constraints.md). Partly superseded on arrival of Sleuth's engagement-type list —
> [`19-engagement-type-specification.md`](19-engagement-type-specification.md) §5.


> The brief: *"cybersecurity consultancy + digital forensics laboratory + enterprise operations platform."*
> Sleuth's own stylesheet already says: *"Flat color palette. No gradients. Enterprise-grade."*
>
> The direction is therefore **not** to invent a look. It is to extend an existing, well-judged one into a dense operational context.

---

## 1. Inherit the brand, extend for operations

The public site's design system (research §5) is already close to what the brief asks for. The internal platform adopts it wholesale and adds only what an operational tool needs and a marketing site does not: a **status palette**, a **severity palette**, a **density scale**, and **print/export styling**.

### Inherited without change

```css
--navy:           #0f1b2d;   --navy-light:   #1a2b42;   --navy-mid:    #253d5b;
--blue-primary:   #2b5ea7;   --blue-accent:  #5b9bd5;   --blue-pale:   #e8f0fa;
--white:          #fdfbf7;   --gray-50:      #f5f2ec;   --gray-100:    #e8e4dd;
--gray-200:       #d4cfc7;   --gray-400:     #8a8278;   --gray-600:    #4d4640;
--text-primary:   #1d1c1a;   --text-secondary:#36322e;  --text-muted:  #6b6358;
--border:         #e2ded7;   --border-strong:#d4cfc7;

--font-sans: 'Inter';   --font-mono: 'IBM Plex Mono';
--radius: 4px / 6px / 8px only;
```

**The warm cream neutral base is the most valuable thing here and must be kept.** `#fdfbf7` and `#f5f2ec` rather than the cold greys every other security product uses reads as *paper, laboratory, document, record* — exactly the register this platform needs. It is also, incidentally, easier on the eyes across the long sessions this work involves.

---

## 2. What gets added

### 2.1 Status palette — engagement and task state

Distinct from severity, deliberately. Conflating "this task is blocked" with "this finding is critical" is the fastest way to make a dense interface unreadable.

| State | Colour | Marker | Notes |
|---|---|---|---|
| Not started | `--gray-300 #b0a99e` | `○` | Recessive |
| In progress | `--blue-primary #2b5ea7` | `◐` | Brand blue = active work |
| Complete | `--success #16a34a` | `●` | |
| Blocked | `--error #dc2626` | `⬛` | Square, not a circle — different shape, not only colour |
| Needs review | `--warning #d97706` | `◆` | Diamond |
| Not applicable | `--gray-300` | `⊘` | Present but muted; the record matters |
| Overridden | `--warning` + outline | `◆!` | Never looks like "passed" |

### 2.2 Severity palette — findings only

Deliberately a *different* hue family from status, so a table containing both remains legible.

| Severity | Colour | Marker |
|---|---|---|
| Critical | `#8b1a1a` deep red | `████` |
| High | `#dc2626` | `███` |
| Medium | `#d97706` | `██` |
| Low | `#b8a04a` muted gold | `█` |
| Informational | `--gray-400` | `▪` |

Severity uses a **bar of varying length**, not just a colour chip. Length is readable at a glance, survives greyscale printing, and does not depend on colour vision.

### 2.3 Integrity palette — evidence only

The smallest and most important palette. Three states, maximum contrast, no ambiguity:

| State | Treatment |
|---|---|
| Verified | `--success`, solid `●`, label "VERIFIED" |
| Pending | `--gray-400`, hollow `○`, label "VERIFICATION PENDING" |
| **Failed** | `--error` on a filled background, `✕`, label "INTEGRITY FAILED" — the only inverted badge in the entire system |

Reserving the one inverted treatment in the product for exactly this state means it can never be mistaken for anything else.

### 2.4 Density

One comfortable default for procedure and form views (16px base, 44px touch targets). One compact mode for registers and tables (14px, 32px rows, tighter leading). No third option — density settings proliferate into inconsistency, and the two genuine contexts here are *doing work* and *scanning records*.

---

## 3. Typography, with a functional rationale

**Inter** for all interface text. **IBM Plex Mono** for anything a human must compare character by character:

- Hashes — `4f2a9c1e…c81d`
- Identifiers — `ENG-2026-0141-E007`, `SF-SEC-VAP-EXT v1.2`
- IPs, CIDRs, hostnames, file paths, registry keys
- Timestamps in timeline views
- Command strings and request/response captures

This is not a stylistic gesture toward "technical". Proportional fonts make `1`/`l`, `0`/`O` and `rn`/`m` genuinely hard to distinguish, and a consultant verifying a hash against a physical label needs the distinction to be free. It also happens to give the interface its laboratory register honestly — the monospace appears where the work is precise, not as decoration.

| Role | Treatment |
|---|---|
| Screen title | Inter 600, 24px, `-0.02em` |
| Section heading | Inter 600, 16px |
| Label / eyebrow | Inter 600, 11px, uppercase, `0.08em`, `--text-muted` |
| Body | Inter 400, 16px, 1.6 |
| Table cell | Inter 400, 14px |
| Identifier | **IBM Plex Mono 500, 13px** |
| Hash | **IBM Plex Mono 400, 12px**, wrapping at a fixed column |

---

## 4. Layout and structural language

### Borders, not shadows
The public site uses subtle shadows for marketing cards. The application should use **1px borders and surface tints** instead. Shadows imply floating and depth; an operational record should read as ruled and filed. Shadows are reserved for genuinely overlaid elements — modals and dropdowns — where the depth cue is accurate.

### The record header
Every record — evidence, finding, engagement, document — opens with a consistent metadata strip: identifier in mono, type, state badge, and the two or three facts that matter most for that type. Once learned, it is readable everywhere.

```
ENG-2026-0141-E007   L1 RAW   ● VERIFIED   SHA-256 4f2a9c1e…c81d
custody: 6 events · complete · holder: S. Kulkarni · evidence safe A-3
```

### Rules and tables
Horizontal rules between rows, no zebra striping, no vertical grid lines. Right-aligned numerics, left-aligned text, monospace identifiers. Column headers in the label style. The result reads like a laboratory register, which is precisely what it is.

### The classification bar
A persistent navy bar across the top of every engagement screen carrying classification, engagement ID and client name. It cannot be dismissed. It appears on print and export. It is the first thing on screen and the last defence against misattribution.

---

## 5. Iconography

Thin-line geometric, 1.5px stroke, 20px grid, drawn from a single consistent set. Icons appear **only where they carry meaning**: state markers, evidence type, document type, escalation, stop. Never decorative, never alongside a label that already says the same thing.

**Explicitly excluded**, per the brief and by judgement: emoji anywhere in the product; illustration of any kind; shields, padlocks, bug-with-magnifier, fingerprints, hooded figures, terminal-green, matrix rain, circuit-board motifs, radar sweeps, glowing edges. These are the visual vocabulary of security *marketing*, and their presence in an operational tool undermines exactly the seriousness the product depends on.

The strongest visual statement this product can make is that it is entirely undecorated.

---

## 6. Motion

- 150ms for state changes, 250ms for panel expansion. Nothing longer.
- No entrance animation, no skeleton shimmer, no attention-seeking motion.
- Motion is used only to preserve continuity — an expanding procedure, a panel sliding in — so that the eye does not lose its place.
- **Exception: nothing animates on an incident screen.** During an active incident, movement on screen is noise at the exact moment attention is most expensive.
- Full respect for `prefers-reduced-motion`.

---

## 7. Dark mode

Genuinely useful here — forensic work happens at night, and lab environments are often dimly lit. But it is a **Phase 4+ addition**, not a Phase 1 feature.

What Phase 1 must do is make it possible later: define every colour as a semantic token (`--surface`, `--surface-raised`, `--text-primary`, `--state-blocked`) rather than a literal, and never hard-code a hex value in a component. A dark theme then becomes a token file, not a rewrite.

When it arrives, the navy family becomes the surface family and the warm creams become the text family — the palette is already structured for the inversion.

---

## 8. Print and export

The most-overlooked surface, and here it genuinely matters: chain-of-custody forms get signed on paper, authorisation letters get carried to client sites, and reports get printed for board meetings and legal review.

- Dedicated print stylesheet. Navigation and controls removed entirely.
- Classification header and footer on every page, with page `n of m`.
- Every printed artefact carries its identifier, version, generation timestamp and the name of the person who generated it.
- Severity bars and state markers must survive greyscale — which they do, because they use shape and length as well as colour.
- Chain-of-custody forms print in a signature-ready layout with ruled transfer rows.

---

## 9. Accessibility

- WCAG 2.2 AA minimum; AAA for body text where the palette allows. The warm cream base makes this easier than a white ground.
- **No meaning carried by colour alone**, anywhere — enforced by the shape and label conventions above.
- Full keyboard operation, visible focus rings (2px, `--blue-primary`, 2px offset).
- Semantic HTML with correct landmarks and live regions for state changes.
- Minimum 44px touch targets for the mobile evidence-capture surface, which is used one-handed while holding a device in the other.

---

## 10. Design principles, in one place

1. **Undecorated is the statement.** Every element earns its place by carrying information.
2. **Density with clarity.** Dense is fine; cluttered is not. Rules, alignment and whitespace do the separating.
3. **Shape and label before colour.** Colour is reinforcement, never the sole carrier.
4. **Monospace signals precision**, and appears only where precision is required.
5. **Inherit the brand.** The internal tool should feel like the same firm as the website, because it is.
6. **Calm under pressure.** The screen a consultant sees at 3am during a ransomware incident should be the calmest in the product, not the loudest.
