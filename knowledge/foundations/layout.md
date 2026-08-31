# Layout Foundations — Grids, Containers, Space

Grounded in corpus measurements (see `research/observed-findings.md` §5).

## Container system (what real sites ship)

| Role | Observed range | Recommendation |
|---|---|---|
| Content container (marketing) | 1024–1280px candidates | choose from content measure, media needs, and viewport testing |
| Wide container (dashboards, catalogs) | up to 1440–1600 | 1440, cap inner density |
| Text measure (articles, forms) | 600–800px | 68–75ch max |
| Sidebar + content | 240–320px sidebar | 280px; collapses <1024 |
| Nav height desktop | 56–72px | 64px sticky |
| Nav height mobile | 48–56px | 52px + safe-area |

Real sites cap content at ≤1600 even on 4K walls (OBSERVED max-width census).
Gutters: 16–24px mobile, 24–40px desktop; section rhythm: 64–96px desktop,
48–64px mobile between major sections (INFERRED median from paddings corpus-wide).

## Grid selection rules

- **Card catalogs** (games, products, media rows): CSS Grid with
  `repeat(auto-fill, minmax(card-min, 1fr))`. Card minimums: 150–200px games,
  200–260px products, 220–300px editorial cards.
- **Asymmetric marketing** (hero + feature): 12-col grid, content spans 5–7,
  visual spans 5–7, deliberately unequal for hierarchy.
- **Editorial mixed** (news front): grid areas — lead story 2×2, secondary
  stack, sidebar rails (Guardian/NYT pattern family).
- **Dashboards**: 12-col with fixed left rail; content in 4/8 or 6/6 splits;
  never center a dashboard at 960px.
- **Full-bleed moments**: heroes, galleries, video. Bleed the media, not the
  text — keep captions inside the measure.

## The 4-breakpoint spine

```
<640 phone · 640–767 large phone · 768–1023 tablet · 1024–1279 laptop · ≥1280 desktop
```
Design at 390 (phone), 768 (tablet), 1280 (desktop) minimum; the spine covers
~90% of observed behavior. Add 1536+ only when the layout has a wide-desktop
payoff (multi-column dashboards, epic heroes).

## Responsive transformation rules (desktop → mobile)

Recompose, do not merely shrink. The following are candidate transformations;
their trigger widths come from content stress, not the numbers shown by a
framework:
- **Navigation**: keep the highest-frequency destinations/actions visible;
  move lower-priority hierarchy into a sheet/drawer only when the labels no
  longer fit. Search stays expanded when it is a top task.
- **Browse grids**: reduce columns as the minimum useful item width is
  breached; change media ratio only when the content still reads correctly.
- **Tables**: preserve tables when cross-row/column comparison matters, using
  column priority, horizontal scrolling, sticky identifiers, or disclosure.
  Transform to labeled rows/cards only when each record can be understood
  independently and comparison is secondary.
- **Filters**: sidebar → bottom sheet with "Show N results" CTA (e-commerce
  standard, OBSERVED on marketplace class).
- **Heroes**: split hero → stacked with media after text; sticky CTA bar
  appears at bottom on mobile conversion pages (travel/food 75% sticky rate).
- **Footers**: 4-col link farm → accordion sections.

## Space as a system

- Base unit 4px; common multipliers 8/12/16/24/32/48/64/96.
- Component-internal padding (button 12/20, card 16–24, input 12) vs
  section rhythm (64/96) — different scales, never mixed.
- Dense Arabic layouts tolerate tighter rhythm than Western equivalents
  (OBSERVED: MENA news/social run ~10–15% more items per viewport).

## Layering & elevation (z-index scale from real systems)

Standardize: 0 content / 10 sticky nav / 20 sticky sub-bar / 30 dropdown /
40 modal / 50 toast / 60 tooltip. Sticky nav + sticky filters stack at 768+,
merge into one bar on mobile. Elevation communicates layer: flat content →
hover-raised card (+shadow tier 1) → popover (tier 2) → modal (tier 3 + scrim).
Shadow tiers, not bespoke shadows: 2–3 box-shadow tokens site-wide.
