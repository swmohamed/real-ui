# Platform DNA: Android (native, View-system & conventions)

Android DNA independent of iOS (never port iOS idioms blindly).
Sources: developer.android.com adaptive apps, canonical layouts, and
accessibility docs checked 2026-08
`[OBSERVED]` + stable platform conventions `[DESIGN PRINCIPLE]`.

## The Android contract

1. **Back is a system-wide promise** `[PLATFORM RULE]` — every screen
   survives back (gesture bar / 3-button): predictable order, restores
   state, never traps flows. Predictive back shows a peek of
   destination — animations must cooperate.
2. **System navigation is gesture or button** — design for both: no
   critical UI at the bottom edge; edge-swipe gestures must not fight
   app gestures (horizontal paginators need care on edge pages).
3. **System bars are real estate** — edge-to-edge content + inset
   padding is the modern norm; status/nav bar styles are part of brand
   canvas (dark/light/canvas color).
4. **Material is the home dialect** — Android users read Material
   affordances instantly (FAB, chips, snackbar, bottom sheet, nav
   drawer). Custom systems are fine; Material semantics remain the
   shared language `[DESIGN PRINCIPLE]`.

## Large screens (official doctrine) `[OBSERVED]`

- Treat 600dp+ windows as a first-class target; current width classes are
  compact <600, medium 600–839, expanded 840–1199, large 1200–1599,
  extra-large ≥1600. Height class and posture are separate inputs
  (responsive/adaptive-models.md).
- Canonical layouts: list-detail, supporting pane — same doctrine as
  Compose (jetpack-compose.md) applies to Views.
- Foldables/cars/XR are listed as siblings of phones in current docs
  `[OBSERVED]` — posture-aware design is mainstream Android, not exotic
  (devices/foldable.md).

## Android-specific patterns

- Top app bar: title + icon actions (+ overflow ⋮); search as expandable
  bar. Tab layouts under bar for sibling content.
- Bottom navigation (3–5) for top destinations; nav drawer/rail for
  many; drawer hidden = hamburger (fine on Android).
- Bottom sheets are native vocabulary (drag handle, peek heights,
  expandable detents) for contextual secondary content/actions. Use dialogs
  for blocking decisions or focused modal tasks; neither is a universal
  replacement for the other.
  Official M3 definitions (material-components-android, fetched 2026-08
  `[PLATFORM RULE]`): bottom sheet = "slide up from the bottom of the
  screen to reveal more content"; banner = container for "important,
  concise messages" with actions (elevated surface); carousel = "a
  collection of items that can move into or out of view" (hero/
  multi-bucket layouts) — use M3 component names as the shared
  vocabulary with Android teams.
- Selection: long-press/contextual mode, checkboxes in lists for
  multi-select; snackbar (+ action) for undo — undo-over-confirm is
  the Android idiom `[DESIGN PRINCIPLE]`.
- FAB = single primary action of the screen; not decoration.

## RTL on Android `[PLATFORM RULE]`

- `android:supportsRtl="true"` + start/end (never left/right) padding
  → mirrors automatically. Icons that carry direction must flip;
  media/back icons don't (rtl/cross-platform.md).

## Text & scale

sp for text (user scaling respected), dp for layout; test 200% font
scale + display size; ellipsize rules per text class `[PLATFORM RULE]`.

## Android QA

[ ] back works everywhere [ ] gesture + button nav both fine [ ] insets
handled [ ] 48dp targets [ ] font scale 200% survivable [ ] sheet vs dialog
chosen by interaction need [ ] Material semantics kept [ ] all relevant
window classes designed (not stretched phone) [ ] RTL mirrors correctly
