# Device: Desktop

Desktop can combine pointer, keyboard, touch/pen, resizable windows, multiple
displays, and long sessions. Audience and task—not the device label—decide
expertise, density, speed, guidance, and expressive character.

## Pointer economics

- Hover is free and expected (web.md) — tooltips, previews, inline
  reveals, affordance changes. Still never hover-ONLY.
- Precision → smaller targets acceptable (24px+), dense rows, tight
  tables, context menus (right-click), multi-select patterns.
- Cursor states + drag targets designed (not accidents).

## Keyboard-first workflows (the desktop differentiator)

- Everything operable by keyboard. Add standard and task-specific shortcuts
  for frequent actions when they improve real workflows; a command palette is
  optional and never the only path.
- Focus management: logical tab order, visible focus, focus traps in
  modals with release.
- Menus (menu bars in desktop apps; top nav + context menus on web).
- Enter/esc/arrow-key contracts per component (lists, dialogs, forms).

## Windows & space

- Resizable windows: define min-widths per layout; layouts reflow at
  window classes (responsive/adaptive-models.md) — a desktop app that
  breaks at 800px wide is a bug.
- Multi-column is native: sidebars, inspectors, palettes, canvases.
- Large desktop/ultrawide: content max-widths + secondary rails
  (corpus: 1120–1440 content bands), NOT stretched text lines; power
  surfaces may go full-bleed (editors, dashboards, editors' timelines).

## Density doctrine

Desktop permits higher information density when comparison, monitoring, or
expert throughput needs it. Row height, toolbar depth, and pane count must
survive content, target, text-scaling, platform, and accessibility tests.
Removing useful density is harmful; adding density to every desktop is too.

## Desktop-specific states

- Idle/long-ops (progress with cancel), unsaved-changes guards,
  offline indicators, background sync status, window-title reflects
  document/app state, close-confirmations only when truly destructive.

## Desktop QA

[ ] keyboard-only path complete [ ] justified shortcuts + command surfaces
[ ] hover designed (safe) [ ] context menus where habits expect them
[ ] window resize safe (min widths) [ ] density appropriate to product
[ ] focus visible/trapped correctly [ ] multi-column used honestly
