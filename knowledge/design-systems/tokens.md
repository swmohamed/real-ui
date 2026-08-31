# Design Systems: Tokens (the contract layer)

Tokens turn arbitrary values into a design language. Observed namespaces in
the wild: Stripe `--hds-`, Coinbase/Coursera `--cds-`, Kooora `--fco-`,
Spotify `--encore-`, Apple `--sk-`, PayPal `--glnv-`, Property Finder
`--styleguide-`. The prefix = system ownership marker.

## Token architecture (3 tiers)

1. **Primitives** (raw): `--blue-600`, `--space-4`, `--radius-md`,
   `--font-display` — never used directly in components
2. **Semantic** (intent): `--color-action-primary`, `--color-surface-raised`,
   `--spacing-inline-section`, `--radius-card` — what components consume
3. **Component tokens** (optional): `--button-height-lg`,
   `--card-padding` — for systems with variant-heavy components

New product starting out? Two tiers (primitives + semantic) suffice.

## The minimal viable token set

```
Color:    canvas, canvas-raised, ink-primary/secondary/muted,
          brand, brand-strong, success, warning, danger, info (+ dark pairs)
Type:     font-sans, font-display, font-mono, font-arabic;
          sizes (12–48 scale), weights (400/500/600/700), leading (tight/normal/relaxed)
Space:    4px base → 4,8,12,16,24,32,48,64,96
Radius:   none, sm(4), md(8), lg(12), xl(16), full(pill)
Shadow:   none, sm, md, lg (+ optional dark-mode border alternative)
Z:        base, sticky(10), dropdown(30), modal(40), toast(50), tooltip(60)
Motion:   fast(120ms), base(200ms), slow(350ms) + standard easings
Break:    sm 640, md 768, lg 1024, xl 1280 (+2xl 1536 optional)
```

## Token discipline rules

- Every CSS value in shipped components traces to a token; exceptions
  require justification in review
- Naming = role, not value (`--color-danger` not `--red-500` at semantic
  layer); value-based names allowed at primitive layer only
- One source of truth file consumed by everything (CSS vars + JS theme
  object + design tool definitions generated from it)
- Dark mode = re-assign semantic tokens, never write dark-variant
  components (except shadows→borders swap)

## Multi-brand / theming (MENA seasonal reality)

Ramadan/Founding Day/national-day theming is expected: architecture with
**theme layers** (base tokens + brand theme overlay + seasonal overlay)
instead of duplicated stylesheets. Salla/Zid storefront platforms OBSERVED
theming per-merchant — token architecture is what makes 1000s of storefronts
coherent.

## RTL tokenization

- Direction-aware tokens: use logical properties (`padding-inline`,
  `margin-block`, `inset-inline-start`) so one token set serves both dirs
- Directional semantics need pairs: `--space-flow-start/end`,
  `--icon-flip: scaleX(-1)` utility token for mirrored directional icons

## Anti-patterns

- 400 tokens on day one (grow on demand); two systems living together
  (px literals + tokens mixed); tokens named after one component's mood
  (`--hero-glow`) — that's a component value, not a system token; theme
  forks per page
