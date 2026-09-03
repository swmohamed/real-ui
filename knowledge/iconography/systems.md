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

1. Prefer a coherent icon language. Multiple sources can coexist when their
   optical weight, geometry, platform/brand role, license, and states are
   deliberately normalized; brand marks remain their own assets.
2. Match icon stroke weight to text weight ecosystem: 2px-stroke icons
   pair with 400/500 text; heavier UI (700 headlines) tolerates filled
3. Use a small size/grid system derived from font metrics, control targets,
   viewing distance, platform, and density; optical alignment beats mechanical.
4. Size and detail follow meaning, context, and target. Do not assign table,
   button, navigation, and illustration sizes from a universal pixel recipe.
5. Duotone/colored icons: reserved for marketing/empty states; UI icons
   single-color (currentColor) so states inherit

## Icon usage craft

- Prefer labels where recognition, consequence, audience, or localization
  needs them. Icon-only controls require a strong learned/platform convention,
  an accessible name, and discoverability; “cart” is not universal scope.
- Set icon/label gap and optical alignment from the selected icon/font/control
  metrics, then test across scripts and text scaling.
- Color: icons inherit text color; status icons may take semantic color
  (+ text label — never color alone)
- Don't re-illustrate: if a system lacks it, pick the closest semantic,
  don't commission a one-off style-breaker

## Directional icons & RTL (the real rules)

**Evaluate semantic direction:** navigation/order arrows and spatial carets
often flip; brand marks, numbers, and direction-neutral symbols usually do not.
Media, timelines, charts, maps, share/send, body/hand illustrations, and domain
symbols require product/platform/locale meaning—do not use one global list.
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
- icons too small/detailed for target conditions; filled+outline states mixed
  without semantic or optical rationale
