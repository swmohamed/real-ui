# UI: Data Display — Tables, Lists, Stats, Timelines, Definition Sets

## Tables (legitimate where data is the product: finance, sports, specs,
dashboards)

- Header: sticky on scroll (and sticky first column for wide sets);
  sortable with direction indicator (↑↓ or RTL ⟷ semantics: still ↑↓ by
  value — direction icons flip only for sequence semantics)
- Columns: right-align numbers (tabular-nums), start-align text; units in
  header ("Price (SAR)") not repeated per cell
- Rows: 40–48px desktop, 32 compact; zebra OR row borders (pick one);
  hover highlights + reveals row actions (end-side)
- Cell content: wrap long text with title attr; empty = "—" (never blank);
  status cells = badge component
- Responsive: horizontal scroll container with shadow affordances;
  stacked cards transform for read-only tables; keep tables for comparison
  (finance/sports never fully card-stack)

## Key-value lists / definition sets

- Spec sheets, amenity lists, fact boxes: label muted start / value
  end-aligned (or 2-col grid); group with subheads; checkmark/dot lists
  for boolean amenities (✓ مسبح, ✗ موقف)
- Metadata rows (author/date/reading-time): inline with separators ·

## Stats & metrics

- Stat rows: value + label + period + delta (▲▼ with color + sign +
  accessible text "increased 12%")
- Big-number hero stats (impact pages): 32–56px tabular, captioned with
  date/source — undated stats erode credibility
- Count-up animation: once, 600–1000ms, reduced-motion off — subtle, not
  slot-machine

## Timelines

- Vertical (activity feeds, changelogs, match events): time/dot/start rail
  + content; grouping by date headers; newest-top (feeds) or oldest-top
  (narratives) — label which
- Horizontal (company history, roadmaps): year markers + scroll or fit
- Live timelines (live blogs/match): entries auto-prepend with new-count
  pill; anchor deep links per entry

## Progress & meters

- Determinate bars with accessible value (aria) + label; indeterminate
  only for unknown waits (rare, justify)
- Steps/steppers: numbered circles + labels, current highlighted, done
  checkmarked; RTL: flows start→end (right→left), connector direction
  flips, numbers keep Western digits
- Rating aggregates: stars + count + distribution bars histogram

## Trees & hierarchies

- Indent rails (1px line) + caret toggles; category trees with counts;
  keyboard expand/collapse (arrow keys); deep trees search-filterable

## RTL specifics

- Numbers/dates inside RTL text: wrap LTR spans; table numeric columns
  remain digit-formatted (Western or Arabic-Indic per market, consistent)
- Timeline rails flip to right side; carets flip; "newest" direction
  labels localize (الأحدث أولاً)

## Anti-patterns

- Borders everywhere (pick edges: rows OR columns OR zebra)
- Center-aligned mixed-content columns; numbers right-aligned via spaces
  (use text-align)
- Infinite columns requiring 4 swipes on mobile with no sticky anchor
- Sorting that loses current page/filter context
- Sparklines without axis context (no scale = no meaning)
