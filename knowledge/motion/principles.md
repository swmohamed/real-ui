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

## Duration and easing candidates (test, do not standardize globally)

| Interaction | Duration | Easing |
|---|---|---|
| Micro feedback (hover, press) | 100–150ms | ease-out |
| Small transitions (dropdown, tooltip) | 150–250ms | ease-out/quart |
| Large surfaces (drawer, modal, page) | 250–400ms | emphasize-decelerate (enter), accelerate (exit) |
| Deliberate/hero moments | 400–700ms | custom choreography |

- Duration follows distance, scale, complexity, continuity, input, platform,
  and urgency. Exits are often shorter than entrances, but interruption and
  comprehension can change that.
- Easing expresses physical/semantic behavior. Linear motion is appropriate
  for some continuous progress, timelines, or constant-rate movement; it is
  usually poor for entering/leaving surfaces.
- Stagger only when sequence communicates order and total delay does not block
  comprehension or action. Never animate a long list item-by-item by default.

## Scroll-linked motion (the modern layer)

- Scroll reveals require a content/identity reason and a static equivalent;
  “professional” is not a fade-and-rise recipe.
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

## Motion systems (illustrative token shape)

```
--motion-fast: 120ms; --motion-base: 200ms; --motion-slow: 350ms;
--motion-ease-out: cubic-bezier(0.2, 0, 0, 1);
--motion-ease-in: cubic-bezier(0.4, 0, 1, 1);
```
Keep a small semantic set with documented exceptions. Product identity and
state meaning—not a named visual family—decide where productive or expressive
motion earns cost.

## Reduced motion (mandatory accessibility)

Use `prefers-reduced-motion` and platform equivalents to remove or replace
vestibular/nonessential motion while preserving perceivable state changes.
A global near-zero-duration override can break functional events or context;
specify reduced behavior per motion role. Pause/stop controls follow applicable
accessibility requirements; decorative parallax and shimmer should not be
required for understanding.

## Performance rules

- Prefer compositor-friendly properties when they produce the intended effect,
  but profile the actual target. Layout animation is sometimes necessary for
  continuity; constrain scope, avoid layout thrash, and test low-end devices.
- `will-change` sparingly (hint, not paint-magic); contain: content on
  animated sections
- Long chains >700ms total = perceived slowness; kill the middle steps
- 60fps budget: 16ms/frame; test on budget Android (MENA reality)

## RTL motion

- Directional motion follows semantic relationship, platform navigation, and
  spatial origin. A sheet does not automatically enter from inline-start.
- Transform-based flips (scaleX) for directional icons — instant, not
  animated rotation
- Timeline scrub direction follows reading direction for narrative
  scrollers

## Anti-patterns

- Loader animations before content that's already loaded; spinners as
  decoration; confetti on every save; page-enter animations that delay
  first interaction (>300ms to interactive = dead); infinite marquees on
  text; parallax on body copy; motion that can't be skipped
