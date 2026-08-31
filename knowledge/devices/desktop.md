# Device: Desktop

Desktop = pointer + keyboard + resizable windows + high density. Users
are professionals in flow: speed beats delight.

## Pointer economics

- Hover is free and expected (web.md) — tooltips, previews, inline
  reveals, affordance changes. Still never hover-ONLY.
- Precision → smaller targets acceptable (24px+), dense rows, tight
  tables, context menus (right-click), multi-select patterns.
- Cursor states + drag targets designed (not accidents).

## Keyboard-first workflows (the desktop differentiator)

- Everything reachable by keyboard; shortcuts for power actions
  (⌘K/ctrl-K command palettes are table stakes in 2020s SaaS —
  corpus-observed across saas/dev tools).
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

Desktop earns information density: data tables with 32–40px rows,
compact lists, toolbars. "Cleaning up" a desktop tool by removing
density = anti-pattern (industries/b2b-enterprise.md). Whitespace for
rhythm, not emptiness.

## Desktop-specific states

- Idle/long-ops (progress with cancel), unsaved-changes guards,
  offline indicators, background sync status, window-title reflects
  document/app state, close-confirmations only when truly destructive.

## Desktop QA

[ ] keyboard-only path complete [ ] shortcuts + command surface
[ ] hover designed (safe) [ ] context menus where habits expect them
[ ] window resize safe (min widths) [ ] density appropriate to product
[ ] focus visible/trapped correctly [ ] multi-column used honestly
