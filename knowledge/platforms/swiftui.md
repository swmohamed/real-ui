# Platform DNA: SwiftUI (Apple platforms)

Source labels: `APPLE OFFICIAL` (recovered 2026-08 via Apple's DocC
JSON docs API + WWDC transcripts — see research/reports/v2.1-
research-log.md Apple section) · `DESIGN PRINCIPLE` (stable conventions
without an official page). Never conflate the two.

## Apple DNA in one paragraph

Native controls over custom look-alikes; clarity of content over chrome;
deference (content is the hero); generous touch targets; Dynamic Type
and accessibility as first-class; navigation that feels like motion
through hierarchy (push/pop), not screen swaps.

## Navigation idioms

- `NavigationStack` — "displays a root view and enables you to present
  additional views over the root view" `[APPLE OFFICIAL - DocC]`;
  push/pop hierarchy; back = leading-edge swipe + chevron (design:
  titles that shrink into nav bar on scroll).
- `TabView` — "switches between multiple child views using interactive
  user interface elements" `[APPLE OFFICIAL - DocC]`; the 2–5 tab
  guidance itself is HIG convention `[DESIGN PRINCIPLE]` — tab = mode
  of the app, not a random page; badge dots for counts; no web-style
  mega-menus.
- `NavigationSplitView` — "presents views in two or three columns,
  where selections in leading columns control presentations in
  subsequent columns" `[APPLE OFFICIAL - DocC]` — the Apple
  large-screen answer (devices/tablet.md).
- `NavigationLink` — "a view that controls a navigation presentation"
  `[APPLE OFFICIAL - DocC]`.
- Modality ladder: sheet (focused task, drag-to-dismiss) →
  fullScreenCover (immersive, must offer explicit exit) → alert/
  confirmationDialog. Sheet-in-sheet is an anti-pattern. Height
  stopping points are detents — "the array of heights where a sheet
  can rest" `[APPLE OFFICIAL - DocC, UISheetPresentationController.detents]`.

## Content surfaces

- `List` — "a container that presents rows of data arranged in a single
  column, optionally providing the ability to select one or more
  members" `[APPLE OFFICIAL - DocC]`; `Form` — "a container for grouping
  controls used for data entry, such as in settings or inspectors"
  `[APPLE OFFICIAL - DocC]` — grouped inset style is the settings-native
  look; rows with chevrons carry semantics.
- `Grid`/LazyVGrid for media walls; text rows always List-style.
- Toolbar (leading/trailing/actions) — actions live in toolbars,
  not floating web-style button rows.

## Dynamic Type + accessibility `[APPLE OFFICIAL]`

- Dynamic Type: `dynamicTypeSize(_:)` "sets the Dynamic Type size
  within the view"; `accessibilityLabel(_:)` "adds a label to the view
  that describes its contents" `[APPLE OFFICIAL - DocC]`. WWDC23
  "Build accessible apps with SwiftUI and UIKit" (fetched transcript):
  VoiceOver + accessibility traits + actions are the official
  refinement vocabulary `[APPLE OFFICIAL]`.
- Support Dynamic Type scaling at least through accessibility sizes;
  never clamp text without reason (settings apps clamp with reflow plan).
- Built-in a11y: `.accessibilityLabel/Hint/Element/Children`, grouped
  elements, custom actions, sort priority; VoiceOver is the reference
  screen reader. Contrast ≥ 4.5:1 text — accessibility/mobile.md.

## Materials & motion

- Materials (blur/translucency) are Apple-native chrome vocabulary —
  use system materials, not fake glassmorphism (anti-patterns/ai-aesthetics).
- Motion: purposeful transitions (hero-ish navigation transitions via
  matchedGeometryEffect are fine); respect Reduce Motion.

## iPad / macOS / visionOS relevance

iPad: split views + multi-column + drag-and-drop between apps.
macOS: window resizing (min sizes!), menus + keyboard shortcuts,
denser lists acceptable. visionOS: depth + gaze/pointer hybrid — only
when briefed.

## SwiftUI QA

[ ] native navigation idioms [ ] Dynamic Type tested to large sizes
[ ] VoiceOver labels on custom elements [ ] sheets for tasks, alerts
for urgency [ ] tab bar stable [ ] Reduce Motion honored [ ] iPad gets
split layouts, not stretched phone
