# Device: Tablet

Tablets are dynamic touch-first windows that may also use keyboard, pointer,
stylus, multitasking, and desktop modes. Avoid both a stretched phone and an
automatic multi-pane shell.

## Pane opportunities, not a mandatory answer

- **List-detail**: list pane + detail pane side by side
  — Android's canonical layout `[OBSERVED - developer.android.com]`;
  iPadOS official equivalent: NavigationSplitView "presents views in
  two or three columns, where selections in leading columns control
  presentations in subsequent columns" `[APPLE OFFICIAL - DocC]`.
- **Supporting pane**: content + secondary panel (comments, filters,
  inspector).
- Use multiple panes only when simultaneous context improves the task and both
  panes retain useful minimums. Otherwise a focused single-pane flow can be
  more legible. Preserve selection and orientation when the model switches.

## Navigation on tablets

- Android: NavigationRail (labeled icon rail) between bottom nav
  (compact) and persistent nav (expanded) — NavigationSuiteScaffold
  automates the switch `[OBSERVED]`.
- iPadOS: sidebar + content (+detail) split; tab bar may remain;
  toolbar grows actions.
- Web tablets: expose useful navigation when labels and content fit; a drawer
  at a wide width is a smell only when it hides frequent destinations without
  a content/interaction reason.

## Density & layout

- Density ceiling rises: more info per viewport, larger tables/grids
  acceptable, multi-column content.
- Grid columns follow item/content minimums and available window width; tablet
  does not imply cards.
- Touch hit areas stay generous (Apple 44pt general guidance; Android 48dp
  recommendation); adding pointer support does not remove touch needs.
- Split/floating keyboards and handwriting can obscure unexpected regions.
  Multi-column forms are justified only when field relationships and reading
  order remain clear under resizing, text scaling, and virtual keyboards.

## Interaction upgrades

Hover appears on iPadOS/Android-tablet pointer cases — progressive
enhancement (hover reveals, but never required). Drag-and-drop between
panes/apps becomes real (iPad + Android desktop modes). Stylus input
plausible (input/stylus-voice.md).

## Tablet realism checks

[ ] layout earns tablet space without stretching [ ] nav adapts by hierarchy
[ ] pane selection/continuity when multi-pane [ ] density task-appropriate [ ] drag
parity where platform supports [ ] both orientations considered
[ ] targets still ≥44/48
