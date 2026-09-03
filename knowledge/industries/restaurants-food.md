# Industry: Restaurants & Food Delivery

## Characteristics
Appetite is visual; convenience is structural. Two modes: **brand sites**
(single restaurant/chain: menu + story + reservations) and **delivery/
discovery platforms** (multi-restaurant marketplaces). Food imagery triggers
craving — it must dominate.

## User intents
1. See the menu (the #1 job — often within maps/social contexts)
2. Order now (delivery/pickup)
3. Reserve a table / find hours & location
4. Choose a restaurant (platform mode: cuisine, rating, ETA, fees)
5. Track order (live status)

## Business goals
Direct orders (chains dodge platform fees), platform commission volume,
reservation covers, loyalty/repeat rate.

## Candidate information-architecture patterns (not a product sitemap)
- Brand site: Home (hero dish imagery + reserve/order CTAs) → Menu
  (categories with prices/photos) → Locations/Hours → About/Story →
  Reservations → Gift cards/Contact
- Platform: Home (address-entry hero → cuisine rail → carousels: "Fast
  delivery", "New", "Offers") → Restaurant page (menu sections, item
  dialogs) → Cart → checkout → live tracking
- Item dialog (platform signature): photo, description, options/groups
  (size, extras, spice), quantity, notes, add-to-cart

## Navigation
- Brand: logo + Menu/Locations/About + Order/Reserve primary CTA sticky
- Platform: top search + address + cuisines rail; bottom tabs mobile
  (Home/Search/Orders/Account)
- Elmenus OBSERVED (discovery mode): menus-as-content browsing, photos-first

## Candidate components observed in the genre
- Menu lists with dotted-leader or clean rows: name, description, price,
  dietary chips (vegan/spicy 🔥), photo thumbnails optional
- Restaurant cards: logo, cuisine tags, rating, ETA badge, delivery-fee
  badge, promo ribbon
- Cuisine rail (pizza 🍕 sushi 🍣 icons + labels — iconography carries scan speed)
- Item option groups (radio: size; checkbox: extras; quantity steppers)
- Order tracker (confirmed → preparing → on the way → delivered) with
  courier map
- Hours/open-now state, "closed — preorder tomorrow" pattern
- Hero dish photography; story sections (chef, sourcing) for brand sites

## Visual characteristics
- Brand sites: dark-or-warm editorial, big type, generous photography,
  0–12px radius (fine dining near 0; casual larger), serif display common
- Platforms: white utility canvas, bright brand accents (HungerStation gold
  #ffd700 OBSERVED), dense cards, 8–16px radius
- Dietary/allergen chips color-coded + icon (never color-only)
- Delivery apps lean on illustration/photography mix for empty/loading states

## Interaction patterns
- Address-first entry (postal/GPS) → personalizes everything after
- Item option validation (required groups blocked until chosen — with clear
  inline errors)
- Cart drawer with upsell ("Add fries?"), scheduling, group ordering
- Live tracking maps + status pings; reorder from history in one tap

## Mobile patterns
- Platform = app-pattern web: sticky item bar, bottom nav, full-screen
  item dialogs
- Brand sites: click-to-call, maps deep-links, menu as accordions (long
  menus), reserve widget embedded
- PWA ordering (HungerStation AR OBSERVED: app-download-first hero with
  web fallback)

## Arabic/MENA considerations (OBSERVED)
- Talabat/HungerStation class: full RTL, Arabic dish names + English
  secondary (or bilingual menus), cuisine icons localized
- When payment is in scope, verify current market/user evidence for COD, cards,
  wallets, fees, and refund expectations rather than treating one mix as fixed;
  delivery zones expressed by district names (حي النخيل) not postal codes
- Ramadan mode: iftar/suhoor timing sections, family bundles — seasonal IA
  (design token themes again)
- Dish descriptions in Arabic carry dialect warmth; formal MSA for allergen
  info (clarity over tone)
- Nutritional/allergen disclosure maturity rising (Saudi SFDA rules) —
  structured data ready

## Conventions to evaluate (adopt only when model-supported)
Menu above all (hours + location adjacent), open/closed states, item dialogs
with option groups, ETA/fee clarity, live tracking, reorder, dietary chips,
click-to-call on brand sites.

## Overused/anti-patterns
- PDF menus (usability + SEO failure; also no RTL dignity in PDFs)
- Autoplay video with sound (even food)
- Buried hours/phone behind "Contact"
- Delivery platforms hiding fees until checkout
- Trendy dark + neon on family restaurants (audience mismatch)

## Strong references
Starbucks, Chipotle, Elmenus (AR/EN), HungerStation (AR), Talabat
(INFERRED — blocked), McDonald's (INFERRED), OpenTable (INFERRED).

## Contextual decision prompts
Brand: appetite-led photography, story sections, menu-as-content, reserve/
order CTAs persistent. Platform: utility density, option-group rigor,
tracking transparency. Both: speed, clarity, honest pricing, RTL-native for MENA.

## Corpus observations (v7.1 growth: 8+ products SOURCE-OBSERVED 2026-09-03)

Observed families: delivery marketplaces (careem food, talabat-class:
address-first + cuisine rails) - meal-kit subscriptions (hellofresh,
gousto: plan-choice funnels, recipe-as-content) - brand chains (kfc,
starbucks, dunkin, pizzahut, papajohns: menu-brand sites with store
locators + app CTAs) - local fine-dining (dishoom: story-led single-site
register) - food-waste mission (toogoodtogo: purpose-first, map-led) -
Egyptian discovery (elmenus) + Saudi delivery (jahez RTL).
WHY: who cooks and who chooses splits the surface (marketplace = discovery
+ logistics; chains = brand + nearest store; kits = plan commitment).
WHEN NOT: chain-brand chrome (promo tiles, app gates) on fine dining is
register damage; kit-plan funnels on a marketplace break discovery.

## Strict-audit additions (v7.2, SOURCE-OBSERVED 2026-09-03)
- Delivery-discovery platforms (talabat GCC, openrice Asia, swiggy/zomato India observed): search+geo is the hero; cuisine filters before offers; restaurant cards carry ETA + rating + fee lines (decision trio). MENA/Asia variants add Arabic/RTL and COD prominence. Discovery-table surfaces (openrice) add editorial reviews the pure-delivery ones omit.

WHY the delivery decision-trio (ETA + rating + fee) sits on the card: the
choice is which kitchen arrives, at what cost, how fast - not brand story.
WHEN: marketplace discovery. WHEN NOT: a single restaurant site (trio is
platform chrome; the menu and hours are the objects). TRADEOFF: fee honesty
on the card reduces checkout shock and can make a kitchen look expensive
early - that is the correct trust move. Editorial-review tables (openrice-class)
are an alternative when the job is choosing a place to go, not a courier.

## Corpus observations (v7.3 diversity, SOURCE-OBSERVED 2026-09-03)

| Family | Observed shape | WHY | WHEN | WHEN NOT | TRADEOFF |
|---|---|---|---|---|---|
| Super-app food rails (gofood 24h Gojek; grab consumer food as one job among many) | food is a tab, not a restaurant brand site | the user already opened the app for a ride or a pay | bundled super-apps | a single kitchen's menu site | decision-trio cards still belong on the food tab; they do not belong as the whole super-app home |
| Grocery + restaurant hybrids (rappi Mexico food + super; mr-d-food Restaurants / Pick n Pay / Shops; foodpanda Food & Grocery SG) | two inventories, one address | the same drop-off serves meals and SKUs | markets where courier density supports both | fine-dining reservation products | grocery aisle IA on a chef-led restaurant is register damage |
| Courier marketplace (uber-eats: restaurant / deliver / ride / business account) | multi-sided CTAs on the public page | three actors share the same brand | platform marketplaces | owned-fleet restaurant chains | |

WHEN NOT: do not average a super-app food tab with Dishoom-class story dining.

V7.4: booking a cleaner, tradesperson, or salon slot is `local-services.md`,
not a restaurant marketplace. There is no menu; the inventory is labor.
