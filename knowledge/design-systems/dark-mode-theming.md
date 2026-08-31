# Design Systems: Dark Mode & Theming

Systematic theming across light/dark/high-contrast. Consolidates
scattered dark-mode notes (color.md, tokens.md, contrast-motion.md)
into retrieval-ready knowledge. Evidence: MDN official (Baseline:
`prefers-color-scheme` media feature, `color-scheme` property —
fetched 2026-08) `[PLATFORM RULE - web]` · crypto-dark corpus
`[OBSERVED]` · platform APIs `[PLATFORM RULE / APPLE OFFICIAL where
marked]`.

## What theming IS (decision, not feature)

Theme = semantic color ROLES + their values per scheme. Tokens.md
roles (canvas/surface/text/accent/action) get N value sets — not N
token sets. Users may prefer dark for: OLED battery, low-light,
eye conditions, or taste. OS-level preference exists → products
follow it AND allow manual override in settings.

## Mechanics (official)

- Web: `prefers-color-scheme` media feature (user preference) +
  `color-scheme` property (tells the browser to adapt UA chrome —
  form controls, scrollbars) `[PLATFORM RULE - MDN Baseline]`. Set
  BOTH: custom tokens via media query, `color-scheme: light dark` on
  :root for native pieces.
- iOS: system scheme + asset catalogs (light/dark appearances);
  `preferredColorScheme` in SwiftUI. Android: dark theme system-wide;
  `DayNight`/Compose dark ColorScheme `[PLATFORM RULE]`.
- Manual override: persist choice; respect OS until user overrides.

## Dark mode design rules (not "invert")

1. **Don't reuse light colors inverted**: build a dark value set —
   dark surfaces need LESS saturated accents, softer whites (pure
   #FFF on #000 vibrates; corpus dark leaders use off-white text
   `[OBSERVED]`).
2. **Elevation by surface lightness** (lighter-surface-up), NOT
   heavy shadows (shadows are nearly invisible on dark; Material
   does tonal elevation `[PLATFORM RULE - M3]`).
3. **Contrast pairs re-checked per scheme** (floor.md minimums hold
   in dark too; "dark mode ≠ high contrast" — contrast-motion.md).
4. **Images/media**: dark-canvas-safe (scrims, borders), or content
   images keep white backgrounds deliberately (product screenshots
   on dark = framed cards, common pattern `[OBSERVED]`).
5. **Semantic colors retuned**: error/success/warning hues shift
   for dark legibility; state colors are scheme-relative.
6. **Forced-dark avoidance**: UA auto-darkening of light-only sites
   = broken brand; ship real tokens or opt out honestly.
7. **Brand colors**: primary may need a dark-variant (accessibility
   or vibrancy) — brand system defines the mapping, not per-page.

## Theming beyond light/dark

High contrast/forced-colors (contrast-motion.md) · brand skins/white-
label (marketplace/enterprise): theme via token layer only, never
per-component forks · seasonal modes (Ramadan theming is a real MENA
pattern — islamic-apps.md) — same token layer.

## Architecture (tokens.md extension)

```
--canvas / --surface / --text-primary / --accent ...
  :root { light values }
  [data-theme="dark"], (prefers-color-scheme: dark) { dark values }
```
Component styles NEVER reference raw colors — only roles. QA: flip
scheme, no unreadable pair survives. Cross-platform: same roles,
platform-native dark implementations (design-systems/cross-platform.md).

## When NOT to build dark mode

Single-session utility pages · print-first · strict brand-light
products (luxury white) — offer it only with real demand signals;
half-shipped dark (some pages dark) is worse than none.

## QA

[ ] role tokens only (no raw hex in components) [ ] dark set designed
(not inverted) [ ] UA chrome adapts (color-scheme set) [ ] contrast
pairs pass both schemes [ ] images safe on dark [ ] state colors
retuned [ ] manual override persists [ ] forced-colors survives
