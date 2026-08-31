# Platform DNA: Jetpack Compose (Android, declarative)

Sources: developer.android.com fetched 2025-08 `[OBSERVED]` — adaptive
layouts, large screens, Material 3 in Compose pages.

## Adaptive scaffolds (official, use as design vocabulary) `[OBSERVED]`

- **NavigationSuiteScaffold** — "automatically switches between
  navigation bar and navigation rail depending on app window size class
  and device posture." This IS the adaptive-nav rule, as a component.
- **ListDetailPaneScaffold** — "implements the list-detail canonical
  layout. Adapts to the app window size" — list+detail on expanded
  windows, single pane + navigation on compact.
- Supporting-pane canonical layout = third pattern (content + support).

Design meaning: canonical layouts are named, solved problems — choose
one deliberately instead of inventing a layout the OS already has an
idiom for (responsive/adaptive-models.md).

## Material 3 in Compose `[OBSERVED]`

- `MaterialTheme(colorScheme=, typography=)` is the token root —
  same token discipline as design-systems/tokens.md.
- Dynamic color (wallpaper-derived palettes) + tonal elevation are
  platform features `[OBSERVED]`. Dynamic color personalizes — but a
  BRAND palette stays authored; offer dynamic as option, not default
  identity `[RECOMMENDED]`.
- M3 Expressive is the current visual direction (more motion/shape
  personality) `[OBSERVED - docs mention]` — know it, don't blindly
  chase it; match product DNA.

## Layout mechanics (implementation context)

- Column/Row/Box + ConstraintLayout; LazyColumn / LazyVerticalGrid
  (keys for stable identity — animation + scroll restoration).
- Scaffold = app chrome contract (topBar, bottomBar, fab, snackbar).
- Content padding from insets (edge-to-edge + WindowInsets APIs) —
  status/nav bars are layout input `[DESIGN PRINCIPLE]`.

## State-driven UI `[OBSERVED - Compose model]`

UI = f(state): hoist state, events flow up. Design consequence: every
screen must define its states (loading/empty/error/content/
offline — ux/mobile-states.md) BEFORE pixels; states are first-class,
not error-handling garnish.

## Window size classes `[OBSERVED - screens doc: sw ≥ 600dp; full class
cutoffs are the documented standard 600/840]`

compact (<600dp) medium (600–839) expanded (≥840) drive layout/nav
switching (responsive/adaptive-models.md) — reason from classes, not
device names.

## Android-specific UX rules

Back behavior: system back must work on every screen (gesture +
predictive back animations) `[PLATFORM RULE]`. Text scaling: sp units
honor user font size — test to 200% `[PLATFORM RULE]`. Foldables:
posture/fold as layout input (devices/foldable.md) `[OBSERVED - large-
screens docs section]`. Touch targets ≥48dp `[PLATFORM RULE - M3]`.

## Compose QA

[ ] window classes drive layout [ ] canonical layout chosen [ ] system
back works + predictive [ ] insets respected edge-to-edge [ ] sp text
scale tested [ ] 48dp targets [ ] LazyColumn keys set [ ] states all
designed [ ] brand tokens in MaterialTheme
