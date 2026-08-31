# Iconography: Systems Survey & Selection

## The major systems (character survey — no artwork copying)

| System | Style | Weights | Best for | RTL |
|---|---|---|---|---|
| **Lucide** | 24px grid, 2px stroke, rounded | single (weight via stroke) | modern product UI, dev tools | mirror chevrons |
| **Material Symbols** | filled/outlined/sharp/round, variable weight+fill+optical axes | variable | dense UI needing weight matching | `rtl` variants exist |
| **Heroicons** | Tailwind-lineage, outline+solid+mini | 3 cuts | Tailwind products | mirror |
| **Phosphor** | 6 weights incl. duotone | thin→fill | expressive product UI | mirror |
| **Font Awesome** | glyph font + SVG | solid/brands | legacy enterprise, brand logos (OBSERVED 29% corpus: stc, Youm7, gov portals) | rotate classes |
| **Octicons** (GitHub) | 16px-precision glyphs | 2 | dense dev UI | mirror |
| **Tabler/Bootstrap Icons** | stroke sets, huge coverage | 1–2 | fast coverage | mirror |

## System selection rules

1. **One system per product** (the cardinal rule). Mixing Lucide nav +
   FA brands is acceptable ONLY for brand-logo glyphs
2. Match icon stroke weight to text weight ecosystem: 2px-stroke icons
   pair with 400/500 text; heavier UI (700 headlines) tolerates filled
3. Grid discipline: 16/20/24 sizes only; optical alignment beats
   mechanical (triangles/shapes get nudged)
4. Density: 16px icons in tables/rows, 20px in buttons, 24px nav,
   32–48px feature illustrations — size = meaning tier
5. Duotone/colored icons: reserved for marketing/empty states; UI icons
   single-color (currentColor) so states inherit

## Icon usage craft

- Icons + labels for navigation/actions (usability default); icon-only
  for universally-known actions (search, close, menu, cart) WITH
  aria-labels
- 8–16px gap icon↔label; align to text cap-height/x-height center
- Color: icons inherit text color; status icons may take semantic color
  (+ text label — never color alone)
- Don't re-illustrate: if a system lacks it, pick the closest semantic,
  don't commission a one-off style-breaker

## Directional icons & RTL (the real rules)

**Flip:** chevrons/arrows (next/prev, breadcrumbs, "learn more" arrows,
carousel controls), progress/stepper connectors, tooltips carets,
speech-bubble tails, list bullets with direction, share/send
**Never flip:** media controls (play/pause/rewind — timeline semantics),
clocks, logos/brand marks, charts/graph axes, checkmarks ✓, faces/bodies,
numbers, globes (usually), shopping/cart/bag (usually symmetric anyway)
**Mechanics:** CSS `[dir="rtl"] .icon-flip { transform: scaleX(-1); }`
class on directional icons; or logical icon slots (start/end) where
direction is implied by position; SVG `transform` attr for inline

## Icon implementation (performance+a11y)

- SVG inline for interactive/critical (stylable, currentColor)
- SVG sprite `<use>` for repeated sets (one request, cached)
- Icon fonts only in legacy systems (FA OBSERVED widely) — degrade: font
  not loaded = tofu boxes (real MENA enterprise risk OBSERVED: icon-font
  arrows extracted as "-->" text)
- `aria-hidden="true"` decorative; labeled when meaningful
  (`role="img" aria-label`)

## Anti-patterns

- Three icon styles on one page; icons as decoration next to obvious
  labels ("Home 🏠" fine in nav; "Home 🏠" in a sentence = noise)
- Unlabeled mystery icon buttons; emoji as UI icons (cross-platform
  rendering roulette — fine in content, not in buttons)
- 12px icons (below legibility); filled+outline same glyph mixed randomly
