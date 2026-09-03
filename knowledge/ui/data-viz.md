# UI: Data Visualization & Charts (dashboards, live data, RTL numbers)

Complements ui/data-display.md (tables/stats — read first: number
alignment, tabular-nums, empty cells). This file covers CHARTS and
data-dense product surfaces (dashboards, trading, analytics, fitness,
logistics maps). Evidence: Apple Charts official DocC (mark vocabulary,
2026-08) `[APPLE OFFICIAL]` · web corpus dashboards `[OBSERVED]` ·
cross-source conventions `[DESIGN PRINCIPLE]`.

## Chart-type selection (start from the QUESTION, not the data)

| User question | Candidate representation | Notes |
|---|---|---|
| Trend over time? | line / area | time axis convention: LTR; RTL charts → rtl/cross-platform.md |
| Compare categories? | bar | sort by value (not alphabet) unless order is semantic |
| Part of whole? | bar, stacked bar, sector/donut, or direct values | choose by category count, precision, labels, and comparison; decorative 3D distorts judgment |
| Distribution? | histogram/rule marks | |
| Correlation? | point (scatter) | density > prettiness |
| Goal vs actual? | bar + rule (target line) | the classic combo |

Apple's official chart vocabulary maps cleanly: LineMark, BarMark,
AreaMark, PointMark, RectangleMark, RuleMark, SectorMark +
annotations `[APPLE OFFICIAL - Charts DocC]` — use these as the shared
vocabulary with Apple teams; web/Android equivalents exist under the
same concepts.

## Chart-first vs table-first (product decision)

Charts can reveal shape/velocity/relationship; tables or direct values support
exact comparison and audit. Pair or choose them from the decision and audience.
Even two points may need a slope/context visualization; do not decide from
count alone.

## Live & streaming data (crypto, logistics, ops)

- Update the VALUE in place (flash state), never re-layout.
- Throttle/coalesce visual updates to a cadence users can perceive and the
  task requires; high-frequency source data does not require high-frequency
  animation. Provide pause/freeze or aggregation when inspection needs it.
- Timestamp the data ("as of 14:02") — freshness is a trust signal;
  stale-indicator state when feed dies (ux/states.md).
- Pause/scrub affordance on hover/touch for inspection.

## Dashboard composition (pages/dashboard.md companion)

- Order metrics, exceptions, controls, and representations from the screen
  contract. A top KPI row and one dominant chart are candidates, not dashboard
  anatomy; coordinated monitoring may need several equal-status signals.
- Filters global-to-page with visible effect count; time-range
  control adjacent to charts it affects.
- Density is the point (devices/desktop.md) — but group: card ≈ one
  question, not one query.

## Accessibility (non-negotiable)

- Every chart has a text/table alternative or summary (screen-reader
  users get conclusions, not pixels) — accessible data table or
  description `[DESIGN PRINCIPLE; WCAG 1.1]`.
- Color never sole encoding: direct labels, patterns, shapes +
  color (contrast-motion.md).
- Minimum contrast for lines/bars against canvas; consider colorblind
  palettes for multi-series.
- Motion: transitions between data states respect reduced motion.

## RTL / Arabic specifics (rtl/cross-platform.md)

- Chart direction follows data meaning, domain convention, scale, platform,
  and target-user expectation. Horizontal categories, time, order, geography,
  and narrative can differ. Localize and bidi-isolate labels/values, document
  the policy, and test with Arabic users rather than applying blanket mirroring.
- Numbers on axes: Latin digits common in dashboards; Arabic-Indic
  variants per product policy — consistent everywhere.
- Currency/units localized (rtl/arabic-ux.md); percent sign placement.
- Arabic labels need width: charts tuned for short English labels
  overflow — test with real Arabic strings.

## Implementation implications

Web: SVG/canvas + a11y summary; tabular-nums for axes; virtualize
long series. Apple: Swift Charts (official marks). Android: Compose
charting via canonical libs or custom Canvas — design the STATES
(empty/error/loading for the chart widget itself) regardless of stack.
Every chart is a component with states: loading (skeleton), empty
("no data for range"), error (retry), partial (feed gap note).

## QA

[ ] chart answers ONE question [ ] table alternative exists
[ ] color + label encoding [ ] live-update flash not re-layout
[ ] freshness/staleness states [ ] RTL/Arabic label widths tested
[ ] chart widget has applicable states [ ] ordering/category count justified
