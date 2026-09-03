# Modern Craft: Execution Quality from Evidence

What makes an interface read as contemporary and production-ready is not a
style. It is the discipline of small decisions executed coherently. This
file turns corpus evidence (knowledge/research/observed-findings.md, 156-site
corpus + growth waves) into decision logic for craft-level choices. It
never selects a look; product axes (visual-dna/dna-selector.md) do that.

Label: DESIGN PRINCIPLE + REAL-WORLD OBSERVATION, per item as noted.

## Typography discipline (the largest "modern" lever)

Observed: leader-class products are typographically conservative and
ruthlessly consistent (Stripe/Inter-era systems, Linear near-mono
discipline, gov.uk single-family). "Modern" reads as SCALE DISCIPLINE, not
big fonts.

- **Limit role count**: 3–4 roles (display, body, UI label, mono/data).
  Each additional face must justify itself against content shape. WHEN NOT:
  two-role products (documents) need fewer; four is not a target.
- **Scale by ratio, not vibes**: pick a step ratio (1.2–1.25 product UI,
  1.25–1.333 editorial) and stay on it. Off-scale sizes are the #1 tell of
  hand-built pages. TRADEOFF: tighter ratios compress hierarchy; widen only
  when scanning distance grows (TV/poster-class surfaces).
- **Weight carries hierarchy before size does**: 600-vs-400 at the same
  size reads cleaner than +8px. Reserve 700+ for one level (page statement
  or data emphasis). WHEN NOT: low-res/elderly audiences may need size
  hierarchy over weight.
- **Line-height from content class**: prose 1.5–1.7, UI labels 1.2–1.3,
  Arabic 1.7–2.0 (arabic-typography.md). Mismatched leading is instantly
  "amateur". Measure 45–75ch; data tables may exceed via tabular scan.
- **Line-height as fraction of scale**: tighten display leading as size
  grows (1.1–1.25 at display sizes); body keeps 1.5+. Display text at 1.5
  looks like a template default.
- **Numerals**: tabular-nums for any changing data (prices, counts, times);
  proportional elsewhere. Mixed numerals in a data column are a
  production-readiness defect.

## Spacing and rhythm

Observed: mature systems run 2–3 spacing steps at page level (section
rhythm) and a fine scale inside components (4/8-based). Everything-on-8
with no large jumps reads mechanical; three paragraph-sized gaps (e.g.
4/16/64-class) with proportional multiples reads intentional.

- Choose **one rhythm unit** (4 or 8) for inside components; derive section
  spacing as 3–4 jumps (component → group → section → act). WHEN NOT:
  dense operational tools may compress to 2 jumps; editorial luxury may
  expand to 5 for air.
- **Grouping is spacing's job**: related items sit closer to each other
  than to the next group (proximity) — if borders are doing grouping work
  spacing should have done, the layout is over-boxed.
- **Optical over mathematical**: icons and caps need less top padding than
  lowercase; equalize by eye at final sizes. QA in a screenshot, not in CSS.

## Geometry (radius discipline)

Observed sector modes: gov/health 0–4px; SaaS/dev 3–8px; finance 3–10px
(+100px pills for actions); news 2–6px near-flat; gaming 12–16px; auto 1–4
OR 16–28px (two deliberate poles). Radius is REGISTER, not taste.

- Pick a **radius register** with the product's geometry axis and hold TWO
  values max at component level (e.g., 4/10, 12/20) + pill for actions.
  Three-plus unrelated radii is craft drift. WHY: consistent curvature is
  subconsciously read as system quality.
- **Radius follows control size**: large containers may share or exceed
  control radius; never a 16px control inside a 4px card without intent.
- WHEN NOT to round: institutional/legal trust surfaces (0–2px reads
  official); data-dense tables (square cells scan better).

## Color execution

Observed: leaders run 1 identity hue + neutrals + semantic states; a
second hue only for a real system (category coding, brand pair). Trust
blues in finance, reds in news/sports are conventions to reconcile with,
not obey.

- **Neutrals carry the interface; the accent spends itself** on primary
  actions and key state only. If accent covers >10–15% of pixels it stops
  emphasizing. TRADEOFF: entertainment/gaming products legitimately spend
  more color; verify with the register, not a rule.
- **Semantic colors are never decorative** and never the sole encoding.
- **Dark surfaces** (justified by context: media, monitoring, enthusiast,
  night-shift): elevate with lighter steps of the surface, not bigger
  shadows; borders at 8–12% white; NEVER pure #000 or full-sat accents on
  dark. Contrast floor applies (accessibility/floor.md).

## Surfaces and depth

Observed: mature systems use 2–3 elevation levels MAX (token'd), flat
separation first (spacing/borders), elevation only where things actually
float (menus, sheets, toasts).

- **Separation hierarchy**: spacing → border/tint → shadow, in that order.
  A page where every card has a shadow is noise; where nothing does,
  floating elements get lost.
- **Shadow character**: small y-offset + tight blur for controls; larger
  softer for overlays. Uniform big-blur shadows on static cards are the
  classic "template polish" tell. WHEN NOT: flat-by-doctrine products
  (GDS-class) need none.
- **Background layering**: 1 canvas + at most 2 panel tints. Every
  additional tint must encode meaning (zone, state, selection).

## Imagery role (choose deliberately)

dominant (media/luxury: imagery IS the content) · editorial (one strong
image per act, article-class) · supportive (product/context photos in
cards) · functional (screenshots, maps, data viz) · ambient (texture,
never required for meaning) · absent (civic/utility/data products where
imagery would be decoration).

- Stock that could belong to any product is decoration; if no real imagery
  exists for the product, ABSENT is the professional choice. WHEN imagery
  is dominant: build contrast/scrims so type survives (entertainment
  corpus: 100% use scrims on posters).

## Motion budget

Observed: production products move little and meaningfully; expressiveness
lives in one or two signature moments, not everywhere.

- Allowed jobs: feedback (press/hover state), continuity (element
  origin/destination), state change (appear/settle), causality (my tap
  caused this), spatial hint (drawer direction). Everything else is
  decoration.
- Duration classes: micro 100–200ms, transition 200–400ms; nothing
  idles/loops unless it is the product's single expressive moment.
  prefers-reduced-motion always respected (accessibility/floor.md).
- WHEN NOT: institutional/legal/ops contexts — near-static is correct.

## The "production-ready" checklist (craft gate)

- [ ] Type: ≤4 roles, on-scale, correct leading per class, tabular numerals
- [ ] Spacing: one rhythm, 3–4 section jumps, proximity grouping
- [ ] Geometry: ≤2 radii + action pill, register-consistent
- [ ] Color: neutrals carry, accent scarce, semantics separate
- [ ] Surfaces: separation order respected, ≤3 elevations
- [ ] Imagery role chosen and justified; no stock filler
- [ ] Motion budgeted by job, reduced-motion honored
- [ ] No banned default aesthetics without written justification
      (anti-patterns/ai-aesthetics.md — includes the generic-polish list)

Connects: visual-dna/dna-selector.md (axes first — this file executes
them) · foundations/{layout,visual-hierarchy,color}.md ·
typography/{latin-systems,arabic-typography}.md ·
design-systems/tokens.md · accessibility/floor.md ·
implementation/realism.md (states completeness).
