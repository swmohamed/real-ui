# Responsive vs Adaptive (the fundamental distinction)

RESPONSIVE: the interface rearranges to fit available space.
ADAPTIVE: the interface changes layout, NAVIGATION, or INTERACTION
MODEL because device class or context changed.

Flutter docs explicitly warn the two concepts "are often collapsed
into a single term" — keep them separate `[OBSERVED - docs.flutter.dev]`.

## Window size classes (platform-specific rulers)

Do not merge web CSS breakpoints and Android window classes into one
standard. They are different inputs that may produce similar adaptations.

| Android width class (current official) | Width | Typical opportunities, not guarantees |
|---|---:|---|
| compact | <600dp | one pane; compact navigation |
| medium | 600–839dp | rail or two-pane where content fits |
| expanded | 840–1199dp | list-detail/supporting pane |
| large | 1200–1599dp | multi-pane with wider supporting regions |
| extra-large | ≥1600dp | desktop-scale multi-pane composition |

Android also classifies height separately. Classes are dynamic window
properties, not device labels; recalculate on resize, rotation, split-screen,
and fold changes `[PLATFORM RULE — developer.android.com, checked 2026-08]`.

Web breakpoint candidates come from content stress and project constraints.
The corpus commonly contains widths around 640/768/1024/1280, but presence in
CSS is not a platform rule and does not prove a query is active on a page
`[SOURCE-OBSERVED — corrected site-prevalence aggregation]`.

- Rule: classes are layout+nav INPUTS, decided by content needs —
  never "Tailwind gave me md:768 so I use 768" (foundations/layout.md).

## Navigation model switching (adaptive's signature move)

```
compact  → bottom navigation (3–5) / drawer
medium   → navigation RAIL (labeled icons)
expanded → persistent sidebar / header nav with sections
large / extra-large → persistent navigation plus additional content panes
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

For Android, test width-class boundaries 599/600, 839/840, 1199/1200,
1599/1600dp and relevant height classes. For web, test immediately on both
sides of each content-derived breakpoint. Across both, test empty · typical ·
extreme (long localized strings, 200% text) · loading. Foldables add mid-use
class switches (devices/foldable.md).

## QA

[ ] nav model changes by class [ ] layout changes by class [ ]
interaction model adapts (hover/keys/gestures) [ ] boundaries tested
[ ] state survives class switches [ ] breakpoints reasoned from
content, not framework defaults
