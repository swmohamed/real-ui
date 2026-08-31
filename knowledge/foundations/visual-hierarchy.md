# Visual Hierarchy — How Real Sites Direct Attention

## The allocation model

A screen has a finite attention budget. Real sites spend it in this order:

1. **Primary signal** (1 per view): the hero headline, the product name, the
   search field, the checkout total. Biggest type or biggest surface.
2. **Action layer** (1–3): the CTAs. Distinct by fill, not just color.
3. **Scan layer**: section headings, card titles, prices. Built from weight
   and size steps, not new colors.
4. **Support layer**: metadata, timestamps, helper text. Muted color, smaller
   size, but never below readable minimums.
5. **Ambient layer**: backgrounds, textures, decoration. Must lose to everything.

## Size discipline (from corpus type scales)

- Real UI bodies live at 14–16px; support text 12–13px (61+68 sites declare
  14px and 12px). Below 12px is anti-pattern territory.
- Headline steps that read as "designed": ×1.25 ratio between adjacent levels
  (16 → 20 → 25 → 31 → 39 → 49). Editorial/display can go ×1.33+ for drama.
- One dramatic jump (h1 vs h2) beats five timid ones.

## Weight and color steps

- Weight: 400 body / 500–600 emphasis / 700 headlines covers 90% of real UIs.
  Reserve 800–900 for display marketing only (gaming, sports).
- Neutral ramp discipline: real systems run 8–12 steps from ink to paper.
  A hierarchy that needs a 13th gray is hiding a structural problem.
- Accent budget: **one** accent + semantic colors (success/warn/danger).
  News adds a single brand red for live/section identity (BBC, TED, Sky News
  Arabia all OBSERVED using exactly one identity red).

## Position and flow

- F-pattern for text-dense pages (news articles), Z-pattern for sparse
  marketing, grid-scan for card catalogs (games, products, streaming rows).
- RTL flips the F and Z **and** the implied "forward" of progress — a stepper
  moves right-to-left in Arabic (see `rtl/arabic-ux.md`).
- Above-the-fold is 1 message + 1 action on marketing pages; on tools it's
  the primary task surface (search field, dashboard first widget).

## Density as hierarchy

- Card padding is a signal: 12–16px = dense functional grid (news, games
  portal); 24–40px = premium browse (luxury, hotels).
- Row height carries meaning in data UIs: 40–48px interactive rows, 32px
  compact tables, 56px+ mobile touch rows.
- Whitespace volume maps to price positioning (OBSERVED: Ounass/luxury class
  vs Jumia density — same region, opposite whitespace).

## Common failure modes

- Two primary buttons on one view → demote one to secondary/ghost.
- Decorative layer competing with content (gradient hero behind gradient
  cards) → mute the ambient layer until it stops winning.
- Everything bold → nothing bold. Emphasis by promotion, not proliferation.
- Color used as the only differentiator (fails ~8% of males with color
  vision deficiency) → pair color with icon/text/shape.
