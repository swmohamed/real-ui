# Device: Tablet

Tablets are NOT big phones. Both platforms treat them as a distinct
window class with canonical multi-pane layouts.

## The tablet answer: panes, not stretching

- **List-detail** (master-detail): list pane + detail pane side by side
  — Android's canonical layout `[OBSERVED - developer.android.com]`;
  iPadOS official equivalent: NavigationSplitView "presents views in
  two or three columns, where selections in leading columns control
  presentations in subsequent columns" `[APPLE OFFICIAL - DocC]`.
- **Supporting pane**: content + secondary panel (comments, filters,
  inspector).
- Two-pane replaces phone's push-navigation for sibling contexts —
  selection happens in place, no screen swap.

## Navigation on tablets

- Android: NavigationRail (labeled icon rail) between bottom nav
  (compact) and persistent nav (expanded) — NavigationSuiteScaffold
  automates the switch `[OBSERVED]`.
- iPadOS: sidebar + content (+detail) split; tab bar may remain;
  toolbar grows actions.
- Web tablets: enough width for visible nav instead of hamburger
  (corpus: hamburger persistence on ≥1024px is a smell).

## Density & layout

- Density ceiling rises: more info per viewport, larger tables/grids
  acceptable, multi-column content.
- Grids: 2–4 columns of cards vs phone 1–2.
- Touch targets stay ≥44/48dp — pointer precision doesn't change.
- Split keyboard / floating input zones exist; forms can be two-column
  at ≥ 900 width.

## Interaction upgrades

Hover appears on iPadOS/Android-tablet pointer cases — progressive
enhancement (hover reveals, but never required). Drag-and-drop between
panes/apps becomes real (iPad + Android desktop modes). Stylus input
plausible (input/stylus-voice.md).

## Tablet realism checks

[ ] panes/canonical layouts (not stretched phone) [ ] rail/sidebar nav
[ ] selection-in-place for master-detail [ ] density upgraded [ ] drag
parity where platform supports [ ] both orientations considered
[ ] targets still ≥44/48
