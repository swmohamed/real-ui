# UI: Cards — Anatomy, Variants, Behavior

The card is the web's universal content container. Its craft is in the
ratio, the internals hierarchy, and the interaction boundary.

## Card anatomy (universal)

```
[Media] → ratio per vertical (1:1 product, 4:3 editorial, 16:9 media/games,
         3:4 fashion, 2:1 wide promo)
[Content block]
  Primary line (title, 1–2 line clamp, weight 600)
  Meta line (kicker/category/price/rating — smaller, muted or accent)
  Support lines (description 2–3 lines clamp, specs icon-row)
[Action layer] whole-card link + optional explicit CTA / hover overlay
```

## The whole-card-link problem (do this right)

- One primary link covering title+media (stretched-link pattern);
  secondary links (author, tag) sit above it with their own targets
- Hover: elevation+1 or media scale 1.02 — pick ONE system
- Focus-visible on the card link must be visible (not clipped)

## Variants by vertical (observed canonical proportions)

- **Product**: 1:1 image, title 2 lines, price bold + compare-strike,
  rating row, badges corner; quick-add button hover (desktop)
- **Editorial/news**: 4:3 or 16:9, kicker (section color), headline 3-line
  clamp, timestamp; image optional for text-only "brief" cards
- **Game**: 16:9/4:3 thumb, title, tags, play-overlay on hover; 12–16px
  radius standard
- **Media/streaming**: 16:9 with progress bar (continue) or rank numeral
  (top-10); title below, 2-line
- **Real estate**: image carousel inside card, price + icon-facts row,
  location, agent logo chip
- **Profile/author**: avatar + name + role + meta actions
- **Stat/KPI card**: label (small caps/muted) + value (tabular, 24–32px) +
  delta chip + sparkline; title-attribute discipline: label the delta
  ("+12% vs last week")

## Card grid behavior

- Grid gap 16–24; card min-widths per vertical (see foundations/layout.md); auto-fill
  grids adapt without media queries
- Image-first cards keep equal heights via media ratio; text-first (news)
  use line-clamps for rhythm
- Horizontal scroll rails: card width 240–320 fixed, peek 16–24px of next,
  scroll-snap-type x mandatory, arrows + drag on desktop
- 2-col mobile minimum for browse verticals; 1-col for decision-heavy
  (hotels/real estate detail lists)

## Interaction states

- Static cards: no hover (feeds) except cursor pointer
- Interactive: hover elevation/subtle scale, active press (scale .99),
  selected state (border/ring) for pickers
- Hover-reveal actions (quick-add, save heart) must remain keyboard/touch
  reachable (actions visible on focus; on mobile, always visible)

## Density dials

Padding: 12–16 (dense feeds) / 16–24 (standard) / 24–40 (premium);
radius: 2–6 institutional / 8–12 product / 16–24 consumer-media;
shadow: none→hover-tier only, or border-only systems (modern preference)

## RTL

- Media right-aligned naturally by grid; text start-aligned; badges flip
  corners; carousels scroll RTL with snap; price blocks keep currency
  label adjacent (ر.س ١٢٩ or 129 ر.س — pick regional convention per
  market: SAR usually follows the number: 129 ر.س)

## Anti-patterns

- Nested-card chaos (cards inside cards) — use list rows inside cards
- Three different card systems on one page (unify by role, not by content)
- Clickable-looking cards that aren't links
- Auto-playing video inside every grid card (perf + annoyance)
- Equal-height stretch that centers 1-line titles in ghost space (align
  start, bottom-align meta)
