# Accessibility: Motion, Contrast, Color Independence

Extends floor.md (contrast minimums) with reduce-motion, forced
contrast, and color-independence rules.

## Reduced motion `[PLATFORM RULE]`

Users opt out of motion (vestibular disorders). Respect:
- Web: `prefers-reduced-motion: reduce` — collapse parallax, autoplay
  motion, large transitions to opacity/instant; keep state feedback.
- iOS: UIAccessibility.isReduceMotionEnabled — cross-fades replace
  slides/zooms.
- Android: animator duration scales to 0/user setting — animations
  must respect system animator scale.
- Never gate content behind motion; provide pause/stop on anything
  moving >5s (WCAG 2.2.2 `[PLATFORM RULE]`).

## High contrast / forced colors `[PLATFORM RULE]`

- Windows high-contrast / forced-colors mode: borders replace
  backgrounds; test that UI survives (system colors override yours —
  borders + text matter more than fills).
- Android: high-contrast text setting; ensure surfaces/text pairs
  remain legible when system boosts contrast.
- Dark mode is NOT high contrast — dark mode still needs its own
  contrast pairs (floor.md: never pure white on black).

## Color independence `[PLATFORM RULE - WCAG 2.x]`

Color never the ONLY signal (1.4.1): pairs with icon, text, shape,
or pattern. Cases: error vs success (icon+text), chart series
(patterns/labels/direct labeling), status dots (label/shape), map
legend, required fields (asterisk/label, not color alone).

## WCAG 2.2 criteria — official text recovered (W3C GitHub,
understanding/22, 2026-08) `[PLATFORM RULE]`

| Criterion / level | Rule (distilled from official Understanding docs) |
|---|---|
| 2.4.11 Focus Not Obscured (Minimum), AA | focused item stays at least partially visible under sticky headers/footers |
| 2.4.13 Focus Appearance, AAA | focus indicator meets the criterion's area and 3:1 change-of-contrast requirements; treat this as an enhanced target, not an AA claim |
| 2.5.7 Dragging Movements, AA | dragging actions need a non-drag alternative (single-click/tap path) unless dragging is essential |
| 2.5.8 Target Size (Minimum), AA | pointer targets ≥24×24 CSS px, or an allowed spacing/equivalent/inline/user-agent/essential exception; 2.5.5 Target Size (Enhanced), AAA uses 44×44 CSS px with exceptions |
| 3.2.6 Consistent Help, A | help access (human contact/FAQ…) appears in a consistent relative order when repeated across pages |
| 3.3.7 Redundant Entry, A | don't re-ask info already given in the same process unless an exception applies (autofill/persist) |
| 3.3.8 Accessible Authentication (Minimum), AA | authentication avoids cognitive-function tests unless an allowed assistance/alternative/object-recognition/personal-content exception applies |

## Beyond minimums (design quality floor)

- Body text contrast: aim 7:1 where feasible (AAA) — corpus leaders do
  `[OBSERVED - v1 research]`; minimums 4.5:1/3:1 are floors not goals.
- Focus indicators: ≥2px, 3:1 against adjacent — visible on every
  surface (never outline:none without replacement).
- Text on imagery: always a guaranteed layer (gradient scrim/solid
  panel), not hope.

## Cognitive load

Consistent nav, predictable patterns, chunked forms, clear language,
errors in human words, no time pressure without pause/extension
(WCAG timing rules) `[PLATFORM RULE]`.

## QA

[ ] reduce-motion respected everywhere [ ] contrast pairs checked in
both modes [ ] forced-colors/high-contrast survives [ ] no color-only
signals [ ] focus visible on all surfaces [ ] scrims under text-on-
image guaranteed [ ] timing adjustable
