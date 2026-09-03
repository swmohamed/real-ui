# Page Type: Dashboard / App Shell / Logged-in Product

The daily workspace: task speed + state clarity at the density its users and
content require. “Dashboard” does not automatically mean KPI cards, a left
rail, or instrument styling; derive the workspace from the product model.

## Candidate anatomy (select from the screen contract)

- **App shell** (when navigation depth requires it): product identity + only
  in-scope global actions + a navigation model chosen for task frequency and
  window class; a left rail is one option, not the default
- **First screen**: the user's live state (balance, today's tasks, live
  metrics), not a welcome hero
- Representations chosen per question: aligned lists/tables, timelines,
  charts with source data, or genuinely independent widgets; a 12-column
  card grid is optional
- Empty states designed as onboarding (first-use teaches)
- Global actions only when supported by scope and task frequency

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

## Navigation candidates

- Choose tabs, a rail, sidebar, search-first command surface, or shallow
  in-page navigation from task frequency, hierarchy depth, and window class
- Breadcrumbs in deep trees (settings > billing > invoices)
- Deep-linkable everything (URL = state: filters, tabs, selected rows)

## Mobile behavior

- Use bottom destinations only when 3–5 top-level modes dominate; otherwise
  choose a model suited to the hierarchy and platform
- Re-prioritize each region. Independent widgets may stack; tables retain
  comparison through column priority, horizontal scroll/sticky identifiers,
  disclosure, or a record-detail transition. Convert to cards only when
  records make sense independently
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
- Using this page as a work-queue, docs tree, calendar, or canvas
  template (v7.5). Those jobs load `interface-families/*`, not KPI chrome.
