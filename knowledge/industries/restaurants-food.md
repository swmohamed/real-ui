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

## Information architecture
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

## Components that define the genre
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
- Payment: COD remains table stakes + cards + wallets (STC Pay, Fawry);
  delivery zones expressed by district names (حي النخيل) not postal codes
- Ramadan mode: iftar/suhoor timing sections, family bundles — seasonal IA
  (design token themes again)
- Dish descriptions in Arabic carry dialect warmth; formal MSA for allergen
  info (clarity over tone)
- Nutritional/allergen disclosure maturity rising (Saudi SFDA rules) —
  structured data ready

## Conventions (follow)
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

## Decision guidance
Brand: appetite-led photography, story sections, menu-as-content, reserve/
order CTAs persistent. Platform: utility density, option-group rigor,
tracking transparency. Both: speed, clarity, honest pricing, RTL-native for MENA.
