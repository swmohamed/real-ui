# Design Systems: Components, States, Variants & Composition

## Component API discipline

Every component contract = intent + semantics + content + composition + states:
- **Intent**: what job (Button = action; Badge = status; Card = content
  unit grouping)
- **Variants**: only meaningful axes supported by repeated product needs;
  emphasis, size, density, or orientation are candidates—not mandatory sets
- **States**: default, hover, active, focus-visible, disabled, selected,
  loading (interactive); empty, loading, error, partial (data)
- **Slots**: composed regions (card: media slot, content slot, action slot)

## State-space method

Map supported properties and states, then test meaningful intersections:
content extremes, loading + disabled, selected + focus, error + read-only,
RTL + icon placement, compact + touch, and high/forced contrast. Do not create
a combinatorial variant API to appear systematic. Prefer composition,
semantic props, and shared primitives over page flags or a god component.

## State spec essentials (commonly missed)

- Focus-visible: clearly identifiable on every surface and in relevant
  contrast modes; use a system token tested against actual backgrounds
- Disabled: native/ARIA semantics match behavior; do not rely on opacity or
  `pointer-events` as the whole contract, and keep explanatory content legible
- Loading: prevent ambiguous duplicate effects, preserve enough layout and
  context for orientation, and state whether the command can be cancelled
- Selected: distinct from hover (persistent), works with `aria-pressed`/
  `aria-selected`
- Skeletons are optional and must not fabricate structure, loop indefinitely,
  or hide usable stale content during a background refresh

## Composition rules (page-level coherence)

- Components compose into reusable regions and layout primitives. Define
  constraints (content width, split ratios, density, media placement), not
  page-type section sequences. Assemble pages from their screen contracts and
  `pages/README.md`; recurring compositions may be promoted only after real
  repetition proves them
- Density variants: comfortable (default) / compact (data tools) — a
  system-level dial, not per-component hacks
- RTL: variants must be direction-tested; directional icons variant
  (`icon-start` vs `icon-end`) handled by logical properties + flip token

## Lifecycle, evidence, and governance

- Track maturity honestly: proposal/experimental → tested candidate → stable →
  caution/deprecated/retired. Names vary by system; confidence and support do not.
- Contribution evidence includes a distinct recurring need, representative
  usage, accessibility testing (including disabled users where relevant),
  content/localization stress, API review, ownership, documentation, and a
  maintenance/version plan. One product example rarely proves a shared component.
- Deprecate with replacement, migration guidance, telemetry/adoption evidence,
  version boundary, and removal policy. Publish known limitations.
- Measure adoption together with escape hatches, overrides, defect/accessibility
  rate, migration completion, and task fit. High adoption can still mean forced use.

## Documentation minimum per component

1. When to use / when NOT (the most valuable line)
2. Anatomy diagram + variants + states (all interactive states visible)
3. Content guidelines (label length, tone, icon rules)
4. A11y notes (roles, keys, contrast)
5. Code + design tokens used

## Anti-patterns

- God-components with 30 props (variant explosion); components without
  states shipped to prod; "design system" that's a sticker sheet (no
  tokens/API); per-page component forks; dark mode as an afterthought
  variant instead of token re-assignment
