# Platform DNA: UIKit (Apple, imperative foundation)

Source labels: `APPLE OFFICIAL` (recovered 2026-08 via Apple's DocC
JSON docs API — quotes below) + `DESIGN PRINCIPLE` for conventions
without an official page. UIKit knowledge still matters: brownfield
apps, hybrid SwiftUI/UIKit screens, and understanding what SwiftUI
wraps.

## Core patterns that shape design (official anchors)

- **UINavigationController** — "a container view controller that
  defines a stack-based scheme for navigating hierarchical content"
  `[APPLE OFFICIAL - DocC]`. Large-title collapsing: `prefersLargeTitles`
  = "whether the title displays in a large format" `[APPLE OFFICIAL -
  DocC]` — the signature iOS pattern; right-bar-button = screen's
  primary action (Save/Add/Done).
- **UITabBarController** — "manages a multiselection interface, where
  the selection determines which child view controller to display"
  `[APPLE OFFICIAL - DocC]`; tab = mode of the app, not a random page;
  badge dots for counts; no web-style mega-menus.
- **Sheets**: UISheetPresentationController — "a presentation
  controller that manages the appearance and behavior of a sheet";
  its `detents` = "the array of heights where a sheet can rest"
  `[APPLE OFFICIAL - DocC]` — the native half-sheet vocabulary.
  Standard for compose/filter/detail tasks; full-screen only for
  immersive capture/editing.

## Safe areas & layout `[APPLE OFFICIAL]`

- `safeAreaLayoutGuide` — "the layout guide representing the portion of
  your view that is unobscured by bars and other content"
  `[APPLE OFFICIAL - DocC]`. Notches, home indicator, keyboard are
  layout facts — respect insets everywhere; keyboard avoidance built
  into scroll views (contentInset behavior) — design inputs with room
  to scroll above keyboard (devices/mobile.md).

## Dynamic Type & fonts `[APPLE OFFICIAL]`

- `UIFontMetrics` — "a utility object for obtaining custom fonts that
  scale to support Dynamic Type" `[APPLE OFFICIAL - DocC]`; system text
  styles auto-scale by default. Test layouts at largest sizes —
  truncation plans must exist per label class.

## Accessibility (UIKit native) `[APPLE OFFICIAL anchors]`

- `UIAccessibility.isReduceMotionEnabled` — "whether the Reduce Motion
  setting is in an enabled state" `[APPLE OFFICIAL - DocC]` — gate
  motion on it. accessibilityLabel/Value/Hint/Trait per element,
  grouping, UIAccessibility.post announcements, Dynamic Type +
  VoiceOver (accessibility/mobile.md; WWDC23 accessible-apps session
  `[APPLE OFFICIAL]`).

## Interaction vocabulary (native iOS patterns)

- Pull-to-refresh (UIRefreshControl) on list screens.
- Swipe actions on table rows (delete/archive) — the native row-level
  action pattern; don't invent hover menus on touch.
- System-matched transitions: navigation push, modal presentation,
  interactive pop gesture — custom transitions need a reason.

## When UIKit (vs SwiftUI) affects design

Same HIG DNA; implementation differs. For design work: assume Apple
conventions regardless of layer; flag hybrid stacks in delivery so
component mapping is honest (e.g., custom sheet vs UISheetPresentation
Controller detents — detents = the native half-sheet vocabulary).
