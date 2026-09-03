# Industry: Ecommerce & Marketplaces (Mass, Electronics, Retail)

## Characteristics
Conversion machines. Users arrive to find/buy/compare. Speed and clarity beat
beauty at checkout; but category imagery drives the browse impulse. Every
extra step loses 5–20% of the funnel (industry-accepted heuristic).

## User intents
1. Find a known product (search-dominant)
2. Browse/category discovery (deals, new)
3. Evaluate (price, images, reviews, delivery, return policy)
4. Buy with minimal friction
5. Track orders / manage account

## Business goals
Conversion rate, AOV (cross-sell, bundles), repeat purchase (app install,
loyalty), marketplace take-rate.

## Candidate information-architecture patterns (not a product sitemap)
- Home: promo hero (deals/seasonal) + category tiles + deal shelves +
  personalized rows (logged-in) + trust strip (delivery/returns/payment)
- Category → filters sidebar/facets → sort → product grid → pagination or
  infinite scroll
- Product detail page (PDP): gallery, price, variants, buy box, delivery
  promise, reviews, Q&A, related
- Cart → checkout (address → payment → review) → confirmation
- Orders, wishlist, seller pages (marketplaces)

## Navigation
- Masthead: logo, **search bar center stage** (marketplaces put search at 50%+
  header width — Amazon pattern), account, cart with count badge
- Second row: category links or hamburger "All" mega-drawer (Amazon's
  hamburger+drawer OBSERVED on .eg/.sa variants)
- Breadcrumbs on category/PDP (SEO + orientation)

## Candidate components observed in the genre
- Product card: image (square 1:1 mass / 3:4 fashion), title 2-line clamp,
  price + strike-through original, rating stars + count, badges (SALE, NEW,
  best seller), quick-add on hover (desktop)
- Filter panel: facets (price range slider, brand checkboxes, rating, delivery
  promise), active-filter chips, result count, sort dropdown
- Buy box (sticky on mobile): price, variants, qty, add-to-cart CTA, delivery
  estimate, payment icons
- Carousel deal shelves with countdown timers (events)
- Reviews with photos, "verified purchase", rating distribution histogram

## Visual characteristics (OBSERVED)
- Mass market: system fonts or proprietary retail faces (Amazon Ember),
  4–8px radius, white canvas, dense grids 4–6 cols desktop / 2 cols mobile
  (Jumia EG: Ubuntu font, 4/6/8px radii, 2-col mobile grid OBSERVED)
- Electronics retail (Extra/Jarir): blue-family trust canvas, Dubai/Tajawal
  Arabic faces in MENA, promo-heavy shelves, banner sliders
- Deal-communication is the design: yellow/red price tags, strike-throughs,
  countdown chips — brighter than Western SaaS norms, globally consistent
- Imagery: pure product shots on white; lifestyle only in hero/promos

## Interaction patterns
- Search autocomplete with product thumbnails + corrections + recent searches
- Faceted filters that update results instantly (AJAX) with skeleton loaders
- Sticky add-to-cart on mobile PDP (ubiquitous)
- Cart drawer (side sheet) — keeps context vs full cart page
- Guest checkout + wallet buttons (Apple/Google Pay); COD in MENA markets

## Mobile patterns
- Search icon expands to full screen; voice/visual search on leaders
- Bottom nav (Home/Categories/Cart/Account) app-like standard
- On compact touch windows, filters/sort may use a sheet, overlay, compact bar,
  or dedicated result-refinement surface; choose by facet count, comparison,
  keyboard/accessibility behavior, and return-to-results continuity
- Image zoom gallery swipe; sticky buy bar

## Arabic/MENA considerations (heavily OBSERVED)
- Amazon.eg/-.sa serve path-segment Arabic (`/-/ar/`) with full RTL, Arabic
  Ember, localized checkout incl. COD; Jumia.eg/ar same pattern
- Extra.com uses the **Dubai typeface** (UAE gov identity font adopted by
  retail — local familiarity signal); Jarir uses Tajawal
- Trust = COD, mada/STCPay/Fawry logos, WhatsApp support, Arabic reviews,
  delivery-time promises (fast = #1 MENA conversion lever)
- Colors skew brighter for promos; national days (Saudi Founding Day, Ramadan)
  demand themeable identity — design tokens must support seasonal theming
- Numerals: Western digits in prices on mass sites (faster scanning);
  Arabic-Indic acceptable in editorial content

## Conventions to evaluate (adopt only when model-supported)
Search-first header, facet filters + sort, 2-col mobile grid, sticky buy box,
delivery-date prominence, payment-method logos near CTA, breadcrumbs, cart
drawer, review photos.

## Overused/anti-patterns
- Auto-adding to cart on hover/quick-view without feedback
- Countdown fake urgency on evergreen products (trust erosion)
- Gallery lightboxes that trap mobile back gesture
- Hidden total until last step (show shipping early — #1 cart abandonment cause)
- Generic SaaS-style hero on mass ecommerce (kills browse affordance)

## Strong references
Amazon.eg/.sa (AR), Jumia (AR/Africa), Noon (INFERRED — blocked; widely
documented), IKEA, LEGO, Argos (INFERRED), Walmart/Target class, Extra (AR),
Jarir (AR), Alibaba class (B2B variant: RFQ forms, supplier trust tiers).

## Contextual decision prompts
Default: white canvas, search-center header, deal shelves with honest
urgency, 1:1 product images, facet filters, sticky mobile buy bar, 4–8px
radius, bright but systematized promo colors. Luxury/fashion exceptions in
`fashion-luxury-beauty.md`.

## Strict-audit additions (v7.2, SOURCE-OBSERVED 2026-09-03)

| Family | Observed shape | WHY | WHEN | WHEN NOT | TRADEOFF |
|---|---|---|---|---|---|
| Authenticated resale (goat: Shop 315,299 + sneakers taxonomy; vestiaire: buy & sell designer) | condition / authenticity / last-sale as first-class card fields | the inventory is unique units, not SKUs | secondary markets where trust is the buy | new-goods retail (condition UI is noise) | verification above price slows browsing; price-above-condition hides fraud risk |
| Peer resale feeds (poshmark Feed; vinted sell-and-buy) | feed or sell-entry as home, not a brand lookbook | supply is user-generated; discovery is social or search | C2C clothing | authenticated sneaker/luxury vaults | feed DNA on a vault catalog hides size/condition filters |
| Regional retail marketplaces (jumia Nigeria; aliexpress AR locale) | search + category + local payment/COD gravity | local payment and language are conversion, not chrome | mass retail in-market | luxury editorial or B2B RFQ | COD/local-method prominence clutters US-card checkouts |
| B2B wholesale (alibaba: Manufacturers / Suppliers, not cart) | RFQ, MOQ, factory identity | the unit is a quote, not a cart line | wholesale | consumer cart-checkout | cart UI on RFQ products fakes a consumer journey |
| Country gateway (mercadolibre home = country picker) | choose-market before catalog | legal/catalog/payment stacks are per country | multi-country brands | single-market shops | a global catalog with one checkout lies about shipping/tax |

ALTERNATIVES: authenticated vault vs peer feed vs wholesale RFQ vs retail
search. Pick from the inventory model, not from "marketplace".
