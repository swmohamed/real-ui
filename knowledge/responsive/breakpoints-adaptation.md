# Responsive: Breakpoints & Real-World Adaptation

## Corpus candidates, not a breakpoint prescription

```
frequent retained widths: 768 (91/145) · 1024 (63/145) · 1200 (46/145)
other common candidates: 767 · 1280 · 600 · 480 · 640 · 1440
```
- Counts are per site where the width survived top-N source extraction. They
  do not prove the query is active on the sampled page.
- A 640/768/1024/1280 set has at least one member in 104/145 sites, but only 18
  retained all four. Never copy the set as a framework spine without content
  stress tests.
- Container-query syntax appears in 28/145 source samples (19%). Use it when a
  component truly adapts to container space; source presence does not prove
  runtime use.
- RTL samples share several candidates with the wider corpus, but localized
  strings and content priority still determine their actual boundaries.

## Per-element candidate adaptation map

Every item below is a choice to evaluate at the width where real content or
interaction fails—not a mandated transformation.

**Navigation**
- Visible links → condensed navigation when real labels/actions no longer fit;
  use a drawer/sheet or bottom destinations only when the hierarchy and
  platform support it (768 is a corpus candidate, not a universal trigger)
- Utility bar collapses into menu; language/currency stays accessible
  (≤2 taps)
- Search: expands to full-screen input on mobile (auto-focus)

**Layout regions**
- Sidebars: fixed → off-canvas drawer or stacked section when the main region
  breaches its useful width;
  sticky sidebars become inline blocks
- 3-col → 2-col → 1-col at natural density boundaries (see card
  minimums per vertical)
- Hero splits stack (text first, media after)

**Typography**
- Steps shift 1–2 levels; body stays 16; display clamps
- Meta/timestamp lines may hide on phone (only if duplicated elsewhere)

**Components**
- Tables → cards / horizontal-scroll (data keeps tables + sticky col)
- Filters sidebar → bottom sheet + apply CTA (marketplace standard)
- Modals → full-screen sheets on mobile
- Tooltips → inline hints / long-press
- Hover actions → always-visible actions (no hover on touch)

**Gestures & affordances**
- Swipe replaces arrows where native (carousels, galleries, tabs)
- Back gesture must exit overlays (history integration)

## Mobile-first RTL

- Direction set once on `<html dir>` — children inherit
- Prefer touch hit areas around 44×44 CSS px (48–56 for primary actions);
  WCAG 2.2 AA conformance floor remains 24×24 CSS px or an allowed exception
- Sticky elements respect safe-areas (env(safe-area-inset-*))
- Test at 320–360px (real budget Androids across MENA) not just 390

## Common failure modes

- Breakpoint-per-component chaos with no shared rationale — normalize to a
  small project set while reserving container queries for genuinely reusable
  component-level adaptations
- Hiding content at mobile that users need (contact info, filters)
- Desktop hover-only functionality with no touch equivalent
- Horizontal page scroll from fixed-width children (min-width leaks)
- Zoom-blocking viewport meta (`maximum-scale=1`) — still SOURCE-OBSERVED on
  17/145 CSS-evidence sites
