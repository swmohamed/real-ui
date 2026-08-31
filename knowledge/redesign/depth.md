# Redesign Depth (classify BEFORE the pipeline runs)

Observed failure mode this file kills: "redesign" requests producing
polish — old navbar → cleaner navbar, old grid → same grid with better
spacing. Root cause: evolution-by-default verdicts applied to whatever
already exists. Depth classification changes WHAT the defaults are.

## The four depths

| Depth | Preserves | Changes | Typical signals in the request |
|---|---|---|---|
| **POLISH** | structure, visual language, components | execution quality: spacing, contrast, states, alignment, consistency debt | "clean up", "tidy", "fix spacing/polish" |
| **REFRESH / RESTYLE** | structure (IA, nav, composition), components | visual language significantly: type/color/radius/motion system | "new/modern look", "restyle", "keep the layout" |
| **REDESIGN** | requirements, working UX value, brand constants | hierarchy, layout, navigation, composition, components, interaction, direction — WHERE the re-derived model + diagnosis justify it | "redesign", "improve the UX", scope beyond visuals |
| **FULL REDESIGN** | product requirements only (below) | the interface is re-derived from the product model; old composition is not an input to the new architecture | "complete/full redesign", "rethink from scratch", "rebuild the experience" |

Core rule (REDESIGN/FULL): **preserve product requirements, not
existing presentation.**

## What the old interface IS, per depth

- POLISH/REFRESH: the current composition is the base being executed
  better / reclothed.
- REDESIGN: the current composition is a CANDIDATE — each structural
  decision must be re-earned ("still correct" beats "it existed").
- FULL REDESIGN: the old interface is **evidence**, never architecture.
  Mine it for: functionality · content requirements · workflows ·
  routes/URLs worth keeping (SEO) · business logic · technical
  constraints · a11y obligations. Then derive the new interface from
  foundations/product-modeling.md (entities → tasks → priority → IA →
  interaction), reconciled with industry conventions and brand.

## Per-depth preservation defaults (supersedes "KEEP by default")

| Element | POLISH | REFRESH | REDESIGN | FULL |
|---|---|---|---|---|
| Composition/silhouette | locked | locked | re-assessed per verdict | re-derived |
| Section order | locked | locked | re-assessed | re-derived |
| Navigation structure | locked | locked | re-assessed (nav model is a dial) | re-derived |
| Components/containers | locked | locked | re-assessed (cards-vs-table etc.) | re-derived |
| Density/visual hierarchy | locked | adjustable | re-assessed | re-derived |
| Visual language | minor fixes | negotiable | follows new direction | follows new direction |
| Working flows/terminology/shortcuts | keep | keep | keep unless diagnosed harmful | keep unless re-derived model improves (state it) |
| Brand recognition assets | keep | keep | keep | keep unless rebrand briefed |
| Requirements (content, routes, a11y, constraints) | keep | keep | keep | KEEP — this is what survives a FULL redesign |

Ambiguity rule: request unclear + large product → state the assumed
depth in one line and proceed (or ask ONE question if it changes the
work fundamentally).

## Structural before/after validation (REDESIGN/FULL)

Style-blind diff — ignore colors, fonts, imagery, gradients, shadows,
radius, decorative styling. Compare ONLY:

information architecture · hierarchy · navigation · section order ·
page silhouette · content grouping · component types · primary
actions · interaction zones · density · responsive behavior.

**Insufficient-depth detection:** a FULL REDESIGN whose style-blind
diff shows nearly everything preserved, without strong product/UX
justification per item, is a restyle — reclassify honestly (deliver
it as REFRESH or go back to re-derivation).

**Acceptance tests (run both):**
1. **Reclothe test**: apply the OLD colors/typography/shadows to the
   NEW design — is the composition + hierarchy still clearly
   different? If not → restyle, not redesign.
2. **Existed-vs-correct audit**: for every preserved structural
   decision, one line: kept because still *correct* (say why) or kept
   because it *existed* (only valid in POLISH/REFRESH).

## Overcorrection guard (target: meaningful transformation)

Redesign depth ≠ maximum difference. Do NOT: destroy good UX, move
elements to appear different, violate familiar conventions without
reason, randomize layouts. If the re-derived model genuinely matches
the old structure (same tasks/volume/audience → same IA), a similar
result is CORRECT — document that via the existed-vs-correct audit
(originality.md "legitimate similarity" applies to redesigns too).
Every structural change traces to: a diagnosed problem, the product
model, or platform/industry convention. No orphan changes, no
randomness — the same rule as redesign/workflow.md stage 4, aimed at depth.

## Pipeline wiring

- redesign/workflow.md stage 0 = classify depth (this file) — before anything.
- REDESIGN/FULL: stage 3.5 re-derives the model BEFORE verdicts.
- Stage 8 QA includes this file's structural diff + acceptance tests.
- prioritization.md sequences whatever survives verdicts at any depth.
- POLISH/REFRESH skip 3.5 (no re-derivation) — evolution defaults
  (preservation.md) apply unchanged.

Connects: redesign/workflow.md (pipeline) · redesign/preservation.md (what identity
survives) · foundations/product-modeling.md (re-derivation engine) ·
redesign/originality.md (dials for the new composition) ·
diagnosis.md (justification for change).
