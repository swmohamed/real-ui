# Page Type: Dashboard / App Shell / Logged-in Product

The daily workspace: information density + speed + state clarity. Marketing
aesthetics are wrong here; instrument aesthetics are right.

## Anatomy

- **App shell** (persistent): top bar (product, search/⌘K, notifications,
  help, account) + left nav rail (sections, collapsible) + content region
- **First screen**: the user's live state (balance, today's tasks, live
  metrics), not a welcome hero
- Widgets/cards in a 12-col grid; density tiers per role (exec overview
  sparse, operator views dense)
- Empty states designed as onboarding (first-use teaches)
- Global: quick-create button, search-everything, keyboard shortcuts

## Widget/card rules

- One question per widget ("What needs action now?") with title, primary
  number, trend (sparkline/Δ with direction), and a link to the source list
- Time-window controls (7d/30d/90d) where meaningful; consistent across
  widgets
- Data freshness labels ("updated 2m ago") — trust in tools = freshness
  transparency
- Loading = skeletons matching layout; errors = widget-level with retry
  (never page-level blanks)

## Table/list views (the dashboard's muscle)

- Column sort + filters + saved views; bulk-select with action bar
- Row height 40–48px desktop; hover reveals row actions; detail drawer on
  row-click (keeps list context)
- Pagination for countable data; virtualization for streams
- Inline edit where safe; optimistic updates with undo toasts

## Forms inside apps

- Multi-column desktop layouts OK (2-col field groups), single-column mobile
- Draft autosave + "unsaved changes" guards
- Validation inline on blur; server errors mapped to fields

## Navigation model

- Left rail with grouped sections + icons + labels (icon-only with tooltips
  on collapse; persistence preference)
- Breadcrumbs in deep trees (settings > billing > invoices)
- Deep-linkable everything (URL = state: filters, tabs, selected rows)

## Mobile behavior

- Bottom tab navigation (4–5 max) + hamburger for the long tail
- Cards stack; tables become card lists or horizontal-scroll with sticky
  first column
- Quick actions as floating action button or bar
- Offline/slow states explicit (sync indicators)

## RTL/Arabic

- Full mirror: rail right, drawers slide from left… actually drawers slide
  from the start edge (logical properties)
- Charts: RTL axis flip is contested — numbers stay LTR inside charts on
  most regional products (Mubasher/Kooora class OBSERVED mix); pick LTR
  charts + RTL labels and be consistent
- Arabic-Indic vs Western digits: financial dashboards → Western
  (precision scanning); consumer apps may localize — consistency per product

## Anti-patterns

- Marketing gradients/glass inside the app (kills perceived performance)
- Welcome tours that block the first task (use contextual empty states)
- 20-widget walls without hierarchy (curate by role)
- Modal-per-action (prefer inline/drawer flows)
- Hiding loading/error states (the trust killer of tools)
- Auto-logout without draft save
