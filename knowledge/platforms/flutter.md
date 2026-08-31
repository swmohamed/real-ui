# Platform DNA: Flutter (Dart)

Sources: docs.flutter.dev fetched 2025-08 `[OBSERVED]` — adaptive-
responsive, layout, material, web pages; plus DESIGN PRINCIPLE notes.

## Adaptive vs responsive — Flutter's own distinction `[OBSERVED]`

Docs warn these concepts "are often collapsed into a single term."
- Responsive: layout rearranges for available space (constraints).
- Adaptive: app changes STRUCTURE/NAVIGATION for device class.
Flutter's canonical adaptive question `[OBSERVED]`: "bottom navigation
or side-panel navigation?" — decide by window class, not habit.

## Design system choice — never "Material by default"

| Choice | When |
|---|---|
| Material 3 | Android-first, utility products, fastest to ship |
| Cupertino | iOS-only product that must feel Apple-native |
| Custom (ThemeData-driven) | brand-forward products, cross-platform consistency |
| Hybrid (M3 base + Cupertino on iOS) | platform-feel products (expensive — 2 skins, 1 system) |

Material 3 is the DEFAULT in current Flutter (`useMaterial3` on; M2
support is being deprecated — don't build new M2) `[OBSERVED]`. That is
a fact about the framework, NOT a design instruction — custom design
systems are fully legitimate (brands do it) via ThemeData.

## Tokens = ThemeData (single source)

- ColorScheme (seed-generated `fromSeed` is a START, not a brand —
  override brand roles deliberately) `[OBSERVED context]`.
- TextTheme: map to your type scale; respect user text scaling
  (MediaQuery.textScaleFactor; never disable globally) `[DESIGN PRINCIPLE]`.
- Component themes normalize radius/elevation — one system, no one-offs
  (same rule as design-systems/tokens.md).

## Layout mechanics (implementation context)

- Constraints go DOWN, sizes go UP (docs' core rule) `[OBSERVED]` —
  design consequence: outer context decides available space; components
  must be constraint-aware (LayoutBuilder) not size-assuming.
- MediaQuery = global env (size, padding, text scale, dark mode).
- SafeArea & MediaQuery listed by docs as the adaptive foundations
  `[OBSERVED]` — respect insets/notches/safe zones always.
- Slivers for scrolling complexity (pinned headers, collapsing bars);
  lists = builder-based (never unbounded children).

## Adaptive navigation `[OBSERVED → RECOMMENDED mapping]`

Docs' bottom-nav vs side-panel question maps to window classes
(responsive/adaptive-models.md): compact → NavigationBar · medium →
NavigationRail · expanded → persistent rail/Drawer/destinations in
header. Large screens & foldables are a first-class docs section
`[OBSERVED]` — foldable = treat hinge/posture as layout input
(devices/foldable.md).

## Sheets, dialogs, forms

Bottom sheets for mobile-context actions; dialogs for blocking, brief;
forms in sheets/pages with save in reach. Snackbars as non-blocking
feedback (with action). Match devices/mobile.md ergonomics.

## Accessibility

Semantics widgets expose structure to screen readers; label icons,
group list items, respect text scale, test talkback/voiceover builds
(accessibility/mobile.md) `[DESIGN PRINCIPLE]`.

## Flutter Web caveats `[OBSERVED - docs web page]`

Not a free desktop site: initial-load weight, text rendering
differences, no hover on touch. Use it for app-like surfaces; for
content/marketing sites prefer the web platform itself (web.md).
