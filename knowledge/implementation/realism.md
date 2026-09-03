# Implementation Realism (the anti-"pretty screenshot" bridge)

The guard that designs stay implementable and state-aware across
stacks. Design-first, code-aware (SKILL.md hierarchy: USER → UX → UI
→ SYSTEM → PRODUCT → PLATFORM → IMPLEMENTATION — never reversed).
No new research here: synthesis of corpus perf evidence `[OBSERVED]`
+ platform QA blocks + conventions `[DESIGN PRINCIPLE]`.

## Static-screenshot smells (design-time check)

A design that only works as a picture fails. Hunt:
- No loading/empty/error state for any dynamic region (ux/states.md,
  mobile-states.md — every data region × every state).
- One "hero" content length: test title/paragraph/list at 1×, 3×,
  extreme (long Arabic strings, 200% text, 10-item vs 0-item lists).
- Fixed-pixel assumptions (designs that can't reflow at window-class
  boundaries — adaptive-models.md).
- Decorative complexity with no data path (blobs over content),
  animations without cancellation (motion/principles.md).
- Hover-only affordances on touch; press/focus/disabled missing.
- Fonts/sizes that can't scale with Dynamic Type/user font scale.

## Per-stack realism ledger

| Stack | Reality that bites | Design accommodation |
|---|---|---|
| HTML/CSS/JS | CLS from fonts/media; a11y via semantics only | system-font fallback metrics, aspect-ratio boxes, landmarks/focus-visible (web.md) |
| React | render-driven states; lists need keys | states as data, stable list identity |
| Flutter | constraints down/sizes up; text scale | constraint-aware components, no fixed heights with text (flutter.md) |
| React Native | OS keyboard/back differences; virtualized lists | keyboard flows per OS, cheap list items (react-native.md) |
| SwiftUI | Dynamic Type reflow; navigation idioms | flexible stacks, truncation policy (swiftui.md) |
| UIKit | safe areas + auto-layout priorities | inset-aware layouts (uikit.md) |
| Jetpack Compose | window classes + state hoisting | states-first design, canonical layouts (jetpack-compose.md) |
| Android Views | RTL mirrors automatically with start/end | logical-direction layouts (android.md) |

## State completeness contract (per dynamic component)

For EVERY region that loads data: loading (skeleton mirrors layout) ·
empty (first-action affordance) · error (retry + input preserved) ·
partial (gap honesty) · success (data) · offline variant where mobile
(mobile-states.md matrix — fill the cells BEFORE polish).

For durable work, also model queued · running · waiting for input · canceling ·
partial success · failed · canceled · superseded, with real operation identity
and implemented recovery (`ux/operations-recovery.md`). For shared artifacts,
model syncing · stale · conflict · permission change · offline edits · history
(`ux/collaboration-concurrency.md`). For AI-assisted changes, keep source/data
scope and suggestion/draft/committed state explicit (`ux/ai-automation.md`).

## Performance-aware design budget (performance-aware-design.md)

- Effects ledger: every blur/shadow/animation pays frames — prefer
  transform/opacity animations; cap blur radius; no backdrop-filter
  stacks on low-end.
- Media: aspect-ratio reserved space (no CLS), responsive sources,
  lazy below fold; hero media budgeted.
- Lists: virtualization-friendly item designs (uniform heights ok,
  avoid per-item heavy decoration).

## Accessibility implementation floor

Semantics before visuals per stack: HTML landmarks/aria only where
semantic HTML can't; RN a11y props; SwiftUI/UIKit traits; Compose
semantics. Focus order = DOM/tree order — design order accordingly.
Test name: "what does the screen reader HEAR here?" per surface.

## Handoff contract (what a complete design delivers)

direction → tokens → structure → per-state specs (the matrix) →
responsive/adaptive behavior (breakpoints + nav switching) → a11y
annotations (labels, order, contrast) → implementation notes (the
ledger rows for the chosen stack) → QA checklist. If any row is
"figure it out during build", the design isn't done.

## QA

[ ] every dynamic region has applicable states (not only happy path)
[ ] durable/shared/AI state contracts applied where present [ ] extreme-content tests
[ ] window-class boundaries [ ] per-stack ledger acknowledged
[ ] effects budgeted [ ] a11y semantics named [ ] handoff rows filled
