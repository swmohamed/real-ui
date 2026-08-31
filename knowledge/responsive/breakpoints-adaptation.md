# Responsive: Breakpoints & Real-World Adaptation

## The evidence-based spine (from 2025 corpus, 145 sites)

```
sm 640 · md 768 · lg 1024 · xl 1280        (+ 2xl 1536 optional)
```
- 768px = the most-used breakpoint on the real web (dominant by far)
- Mobile-first `min-width` is the modern default (Tailwind-era); legacy
  desktop-first `max-width` persists in enterprise CSS
- Container queries: adopt where leaders do (component-level: cards,
  widgets, sidebars) — 19% corpus and rising; use alongside, not
  instead of, viewport breakpoints
- RTL sites use the same spine (OBSERVED) — grids are direction-agnostic

## Per-element adaptation map

**Navigation**
- Desktop links → ≤768: hamburger/sheet + bottom tabs (app-like)
- Utility bar collapses into menu; language/currency stays accessible
  (≤2 taps)
- Search: expands to full-screen input on mobile (auto-focus)

**Layout regions**
- Sidebars: fixed → off-canvas drawer (<1024) or stacked section;
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
- Touch targets ≥44×44 (56 for primary); spacing tokens mobile ≥8
- Sticky elements respect safe-areas (env(safe-area-inset-*))
- Test at 320–360px (real budget Androids across MENA) not just 390

## Common failure modes

- Breakpoint-per-component chaos (5 custom values per page) — normalize
  to the spine; component-specific adaptation belongs in container queries
- Hiding content at mobile that users need (contact info, filters)
- Desktop hover-only functionality with no touch equivalent
- Horizontal page scroll from fixed-width children (min-width leaks)
- Zoom-blocking viewport meta (maximum-scale=1 — accessibility violation
  still OBSERVED on 3 corpus sites)
