# Industry: Fashion, Luxury, Beauty

## Characteristics
Brand-first commerce: the catalog sells, but the **worldview** converts.
Fashion spans utility (ASOS/Zara class) to aspiration (Ounass/Rolex class);
beauty adds education + shade/ingredient complexity. Imagery > words.

## User intents
1. Browse for inspiration (editorial loop)
2. Find specific item (search/filter by size/color/brand)
3. Evaluate fit/quality (size guides, reviews, materials)
4. Buy; return easily (returns anxiety is the conversion barrier)
5. Beauty: learn routines, match shade, check ingredients

## Business goals
Full-price sell-through, brand heat (drops, editorial), loyalty/app installs,
returns containment (fit info).

## Candidate information-architecture patterns (not a product sitemap)
- Fashion utility: Home (gender split entry) → categories → PLP (grid) → PDP
  (gallery, size selector, fit notes) → bag/checkout. Editorial lookbooks
  interleave shelves.
- Luxury: Home = campaign film/imagery → curated collections → very few,
  very large products. Lookbook/editorial pages; clienteling/appointment
  booking; no visible price on some jewelry (POA pattern).
- Beauty: routines/education hub + shade finder quizzes + PDP with ingredient
  accordions + UGC gallery.

## Navigation
- Fashion: top nav with mega-menu imagery; gender switcher persistent;
  utility row (search, account, wishlist, bag) right-aligned
- Luxury: minimal text nav (5–7 links), typography-led; hamburger tolerated
- Beauty: shop-by-concern/category + education nav

## Candidate components observed in the genre
- **Editorial hero** (full-bleed campaign, thin caption, single CTA or none)
- PLP: 3:4 imagery, dense hover-swap (alternate shot), quick-add sizes popover
- PDP gallery: stacked large images (luxury) or thumbnails+zoom (utility);
  size selector with availability states; fit/size guide modal
- Lookbook spreads, shop-the-look hotspots
- Beauty: shade swatch strips, before/after sliders, ingredient tables,
  routine builders
- If wishlist/recent-history capabilities exist, keep their controls and
  states consistent without visually repeating them indiscriminately

## Visual characteristics (OBSERVED + well-documented class knowledge)
- Utility fashion: sans (Helvetica Now on Nike OBSERVED), 0–8px radius, dense
  grids, promo strips
- Luxury: high-contrast minimalism — white or near-black canvas, serif display
  (Didone class) or spaced-out sans, letter-spacing 0.05–0.2em, hairline rules,
  radius 0–4px, zero to one accent. Photography is the interface.
- Beauty: soft warm neutrals, blush/skin-tone palettes, rounded geometry
  (Glossier 12–20px class), pastel semantic sets, illustration-friendly
- Motion: slow fades (0.5–0.8s) on luxury, none on the buy path

## Interaction patterns
- Hover image-swap (fashion PLP standard)
- Sticky size/CTA on mobile PDP
- Editorial → commerce: shoppable hotspots on lookbook images
- Beauty quizzes (shade finder) with progressive disclosure
- Wishlist + back-in-stock notifications (retention loop)

## Mobile patterns
- Fashion is 70%+ mobile: thumb grids, swipe galleries, sticky bag bar
- Luxury: video heroes muted-autoplay, tap-through editorial chapters

## Arabic/MENA considerations
- Gulf luxury (Ounass class): Arabic editorial voice, Ramadan/Eid gifting
  hubs, modest-fashion categories (عبايات، محرمات) as first-class IA
- Fashion Arabic IA: gender split "نسائي / رجالي / أطفال" mirrors EN
- Photography direction respects regional modesty norms on mass retail
- Luxury keeps brand-global identity + Arabic overlays (Ounass ar OBSERVED
  404 — verify with targeted live research when needed); Namshi (INFERRED) = regional fashion-first
  reference with bilingual UX
- Sizes stay Latin (XS/S/M) even in Arabic UI — sizing systems are global

## Conventions to evaluate (adopt only when model-supported)
Gender/category entry, hover-swap, size-selector with stock states, editorial
interleaving, wishlist, lookbook hotspots, delivery/returns reassurance near
price, price in local currency with correct formatting (AED/SAR/EGP).

## Overused/anti-patterns
- Auto-playing lookbook videos with sound
- Full-screen age-gate-style intros (luxury cliché that kills SEO + patience)
- Hiding price behind "add to bag" (only acceptable jewelry/watch POA)
- SaaS gradient buttons on luxury (instantly downgrades the brand)
- Dense promo badges on luxury PDPs

## Strong references
Nike, Zara (INFERRED), ASOS (INFERRED), Glossier, Sephora (INFERRED),
Ounass, Namshi, Mr Porter (INFERRED), Rolex (INFERRED — blocked), Chanel/LV
(class knowledge; verify with targeted current research), Arabic:
Ounass/Namshi class.

## Contextual decision prompts
Ask: utility or aspiration? Utility → density + speed + filters. Aspiration →
whitespace + serif display + restraint. Never blend: promo badges on luxury
or empty poetry on utility both fail.

## Corpus observations (v7.1 growth: 11+ products SOURCE-OBSERVED 2026-09-03)

Observed families: DTC beauty brands (glossier, fentybeauty, rarebeauty:
product-story led, quiz/personalization entries) - ingredient-science
registers (theordinary/deciem: clinical, typographic restraint) - luxury
multi-brand retail (mytheresa, farfetch, ssense: editorial + dense
catalog) - high-street global (zara: lookbook DNA, seasonal imagery) -
MENA fashion commerce (namshi, levelshoes: bilingual, occasion-led
categories) - founder-identity brands (hudabeauty) - ethics/transparent
(everlane) - scando-minimal (cos).
WHY: price-positioning + identity decide density and imagery (editorial
luxury vs clinical ingredient brands vs lookbook high-street). MENA adds
occasion-led IA (Ramadan/modest lines as first-class categories).
WHEN NOT: clinical restraint on trend-led brands reads cold; editorial
luxury on ingredient brands reads evasive.

## Strict-audit additions (v7.2, SOURCE-OBSERVED 2026-09-03)
- Modest-fashion commerce (modanisa observed): category-first nav (modest wear is the taxonomy, not a filter), model-imagery policies differ from western fast-fashion — evidence that imagery register is a product decision, not a style default.
- Beauty DTC (glossier, mac observed): tutorial/editorial content interleaved with SKUs (usage-first cards) vs. pure catalog grids; shade/variant selectors are the primary interaction after PDP entry.
- Resale luxury (vestiaire observed, see ecommerce): condition language ("very good/never worn") is a first-class taxonomy.
