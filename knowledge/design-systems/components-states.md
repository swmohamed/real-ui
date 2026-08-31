# Design Systems: Components, States, Variants & Composition

## Component API discipline

Every component = intent + variants + states + slots:
- **Intent**: what job (Button = action; Badge = status; Card = content
  unit grouping)
- **Variants**: by emphasis (primary/secondary/ghost), size (sm/md/lg),
  and media-orientation (leading-icon, icon-only) — NOT by page
- **States**: default, hover, active, focus-visible, disabled, selected,
  loading (interactive); empty, loading, error, partial (data)
- **Slots**: composed regions (card: media slot, content slot, action slot)

## Variant matrix method

Design the matrix, not instances: Button × {5 emphases} × {3 sizes} ×
{7 states} — specify at token level, document the corners. This is how
real design systems scale to 100s of components without bloat
(IBM Carbon/GitHub Primer lineage).

## State spec essentials (commonly missed)

- Focus-visible ring: 2px, offset 2px, uses brand or ink (never removed)
- Disabled: reduce to 40–50% ink + no pointer events + `aria-disabled`
  semantics preserved (button element, not div!)
- Loading: preserve layout (fixed width/height), label + spinner swap,
  block double submits
- Selected: distinct from hover (persistent), works with `aria-pressed`/
  `aria-selected`
- Skeleton states match final layout block-for-block

## Composition rules (page-level coherence)

- Components compose into sections; sections into templates; templates
  per page type (see pages/*). Define page **templates** in the system
  (marketing-2-col, dashboard-3-col, article-reading) — prevents
  per-page reinvention
- Density variants: comfortable (default) / compact (data tools) — a
  system-level dial, not per-component hacks
- RTL: variants must be direction-tested; directional icons variant
  (`icon-start` vs `icon-end`) handled by logical properties + flip token

## Versioning & governance (survival rules)

- Deprecation over breaking: new variant → migrate usage → remove old in
  major version; changelog public (design systems ARE products — leaders
  ship public changelogs, OBSERVED: gov.uk, IBM, GitHub docs)
- Contribution path: propose → token-check → a11y-check → document →
  adopt; undocumented components die as forks
- Adoption metric: % of pages using system components vs one-offs —
  the health KPI of real systems

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
