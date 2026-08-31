# Motion Design: Principles & Real-World Practice

## Why motion exists (the only valid reasons)

1. **Continuity**: object persists between states (drawer opens from
   button, card expands to page — shared-element)
2. **Feedback**: action registered (press, toggle, add-to-cart)
3. **Orientation**: where did this come from / where does it go
   (list reorder, tab underline slide)
4. **Attention** (budgeted): one thing matters now (new message, form
   error location)
Decoration is not a reason. If deleting the motion changes no
understanding, delete the motion.

## Duration & easing standards (industry convergence)

| Interaction | Duration | Easing |
|---|---|---|
| Micro feedback (hover, press) | 100–150ms | ease-out |
| Small transitions (dropdown, tooltip) | 150–250ms | ease-out/quart |
| Large surfaces (drawer, modal, page) | 250–400ms | emphasize-decelerate (enter), accelerate (exit) |
| Deliberate/hero moments | 400–700ms | custom choreography |

- Enter faster than exit feels responsive; exits 50–75% of enter
- Standard easings: `cubic-bezier(0.2, 0, 0, 1)` (material-emphasized),
  ease-out for entrances; NEVER linear for UI (feels dead)
- Staggered lists: 20–40ms per item, cap total ≤500ms

## Scroll-linked motion (the modern layer)

- IntersectionObserver reveals: fade + 8–16px rise, once, 200–300ms —
  the SaaS-corp standard (restraint reads professional)
- Parallax: depth accents only; disable on touch + reduced-motion
- Scroll-driven animations (CSS scroll-timeline, 2024+): progress bars,
  reading indicators — native + cheap; progressive enhancement
- Sticky-scene storytelling (museum/auto class): choreograph sections;
  every scene readable statically (JS-off fallback)

## Micro-interaction catalog (the vocabulary)

Press states (scale .97–.98), toggle switches (thumb travel 200ms),
heart/like bursts (one playful scale-pop per product, not per pixel),
cart badge bump (300ms), toast slide+fade, skeleton→content crossfade
(150ms), tab indicator slide, list add/remove (layout animation FLIP),
number counters (600ms once), focus rings (no animation — instant).

## Motion systems (tokens)

```
--motion-fast: 120ms; --motion-base: 200ms; --motion-slow: 350ms;
--motion-ease-out: cubic-bezier(0.2, 0, 0, 1);
--motion-ease-in: cubic-bezier(0.4, 0, 1, 1);
```
Keep ≤4 tokens + documented exceptions. Motion personality per DNA
(calm utility = 2 tokens used sparsely; playful consumer = choreographed
moments at key flows only).

## Reduced motion (mandatory accessibility)

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```
Plus: pause autoplay video/carousels, disable parallax, replace
skeleton-shimmer with static. 40% of major sites ship this (OBSERVED) —
the floor, not the ceiling.

## Performance rules

- Animate ONLY transform + opacity (compositor); layout properties
  (top/left/width/height) = jank
- `will-change` sparingly (hint, not paint-magic); contain: content on
  animated sections
- Long chains >700ms total = perceived slowness; kill the middle steps
- 60fps budget: 16ms/frame; test on budget Android (MENA reality)

## RTL motion

- Slides/sheets from start edge; tab indicators travel start→end
- Transform-based flips (scaleX) for directional icons — instant, not
  animated rotation
- Timeline scrub direction follows reading direction for narrative
  scrollers

## Anti-patterns

- Loader animations before content that's already loaded; spinners as
  decoration; confetti on every save; page-enter animations that delay
  first interaction (>300ms to interactive = dead); infinite marquees on
  text; parallax on body copy; motion that can't be skipped
