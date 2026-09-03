# UI: Data Display — Tables, Lists, Stats, Timelines, Definition Sets

## Tables (legitimate where data is the product: finance, sports, specs,
dashboards)

- Header: sticky on scroll (and sticky first column for wide sets);
  sortable with direction indicator (↑↓ or RTL ⟷ semantics: still ↑↓ by
  value — direction icons flip only for sequence semantics)
- Columns: right-align numbers (tabular-nums), start-align text; units in
  header ("Price (SAR)") not repeated per cell
- Rows: derive height and density from content, text scaling, input target,
  scanning need, and platform. Hover may supplement but never own row actions.
- Cell content: define wrap/truncate/expand behavior and expose the full value
  through a keyboard-, touch-, and screen-reader-accessible path. Distinguish
  missing, zero, not applicable, withheld, and unknown values; a dash is not a
  universal substitute. Status may use text, icon, tone, or a badge according
  to prominence and density—not badge decoration by default.
- Responsive: horizontal scroll container with shadow affordances;
  prioritize/pin columns or provide a focused detail view. Preserve aligned
  comparison when that is the task; do not automatically transform every row
  into a card or assume every table must remain visually unchanged.
- Selection and batch actions keep counts, scope, permission, partial success,
  and recovery visible. Route queued/bulk work to
  `ux/operations-recovery.md`.

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
- Count-up animation is optional and must not delay comprehension; respect
  reduced motion and expose the final value immediately to assistive tech

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
- Card-stacking every mobile row until comparison, selection, and column
  relationships disappear
