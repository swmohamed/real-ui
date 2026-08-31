# Responsive vs Adaptive (the fundamental distinction)

RESPONSIVE: the interface rearranges to fit available space.
ADAPTIVE: the interface changes layout, NAVIGATION, or INTERACTION
MODEL because device class or context changed.

Flutter docs explicitly warn the two concepts "are often collapsed
into a single term" — keep them separate `[OBSERVED - docs.flutter.dev]`.

## Window size classes (the cross-platform ruler)

| Class | Web (corpus-approx) | Android/M3 dp | Behavior |
|---|---|---|---|
| compact | <640 | <600 | phone: single column, bottom nav |
| medium | 640–1023 | 600–839 | tablet portrait/foldable: rail/2-pane |
| expanded | 1024–1279 | ≥840 | tablet/desktop: sidebar, list-detail |
| large | ≥1280 | — | desktop+: rails+panels, full density |

- Android/M3 official classes: 600 / 840 cutoffs, compact/medium/
  expanded `[OBSERVED - developer.android.com; m3 cutoffs are the
  documented standard]`.
- Web spine from v1 corpus: 640/768/1024/1280 `[OBSERVED - 156-site
  census]` — close enough to the mobile classes to unify reasoning.
- Rule: classes are layout+nav INPUTS, decided by content needs —
  never "Tailwind gave me md:768 so I use 768" (foundations/layout.md).

## Navigation model switching (adaptive's signature move)

```
compact  → bottom navigation (3–5) / drawer
medium   → navigation RAIL (labeled icons)
expanded → persistent sidebar / header nav with sections
```
Android's NavigationSuiteScaffold implements exactly this switch
`[OBSERVED]`; Flutter's canonical adaptive question is "bottom
navigation or side-panel?" `[OBSERVED]`. Web equivalents: hamburger →
visible nav; sidebar collapse at expanded (patterns/header-navigation.md).

## Layout model switching (canonical layouts)

list-detail (master-detail) · supporting pane · feed+panel —
Android canonizes these `[OBSERVED]`; iPadOS NavigationSplitView
mirrors the doctrine `[DESIGN PRINCIPLE]`. On web: two-pane at ≥1024,
push-navigation below.

## Interaction model switching (often forgotten)

- Hover affordances appear only with pointer class.
- Keyboard shortcuts matter at desktop class.
- Gesture-first (swipe actions) at touch class; visible twins always.
- Density scales up per class (devices/desktop.md).

## Testing adaptation honestly

Test at class BOUNDARIES (599/600, 839/840, 1023/1024, 1279/1280) and
across the four content conditions: empty · typical · extreme (long
Arabic strings, 200% text) · loading. Foldable adds mid-use class
switches (devices/foldable.md).

## QA

[ ] nav model changes by class [ ] layout changes by class [ ]
interaction model adapts (hover/keys/gestures) [ ] boundaries tested
[ ] state survives class switches [ ] breakpoints reasoned from
content, not framework defaults
