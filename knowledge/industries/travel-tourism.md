# Industry: Travel, Tourism, Hotels

V2.1 extension: airline/flights UX below (evidence: flynas.com
fetched 2026-08 `[OBSERVED]` — custom branded typeface `flynas-Bold`,
Font Awesome icon stack, bp 912/992 — brand-through-type on a
low-cost carrier). Emirates bot-blocked (research log v2.1).

## Flights / airline UX (v2.1)

- **Search is the home**: origin/destination/date/passengers widget =
  hero (same DNA as jobs-recruitment.md) `[DESIGN PRINCIPLE + flynas
  OBSERVED layout]`; promo fare cards as secondary.
- Fare-calendar + cheapest-day strip (LCC DNA: price-first discovery).
- Booking flow: search → results (sortable list, duration/stops/
  baggage chips, price prominence) → passenger forms (forms-
  validation.md — passport fields, Arabic/Latin name-as-in-passport
  warnings) → seats/ancillaries (upsell ladder honesty) → payment →
  PNR receipt (shareable booking ref = the real success state).
- Seat map = data-grid interaction (touch targets + legend + price
  overlay); ancillary cart pattern (add-ons accumulate in sticky
  summary).
- Manage-booking surfaces: check-in window logic, boarding-pass
  wallet states, disruption UX (delay/cancel → rebook first, explain
  second — logistics-delivery.md exception rule applies).
- MENA: bilingual AR/EN parity, Hijri-aware date pickers alongside
  Gregorian (islamic-apps.md), prayer-time breaks in support hours,
  umrah-travel packages as distinct content class.
- LCC vs full-service visual registers differ (flynas type-led value
  vs Emirates' luxury-media register `[INFERRED - blocked site,
  fashion-luxury-beauty.md register applies]`).

## Characteristics
Dream + plan + book. High-stakes purchases (money + anticipation), long
consideration windows, comparison-heavy. Search IS the interface; everything
else supports the search → results → detail → book funnel.

## User intents
1. Discover destinations (inspiration mode)
2. Search availability (flights/hotels) with flexible dates
3. Compare options (price × reviews × photos × location)
4. Book with confidence (cancellation clarity!)
5. Manage trip (bookings, check-in, itineraries)

## Business goals
Bookings/commission, upsells (insurance, rooms), loyalty programs,
cross-sell (flights+hotel+car bundles).

## Candidate information-architecture patterns (not a product sitemap)
- Home: hero search widget (destination, dates, occupancy) + inspiration
  shelves (destinations, deals, "popular now")
- Results page: map+list split (hotels) or matrix (flights) with filters
  (price, stars, amenities, cancellation, neighborhood)
- Detail page: gallery, amenities, map with POIs, room/rate selector with
  cancellation policies per rate, reviews with sub-scores, FAQ
- Checkout: traveler details, add-ons, payment with price breakdown
  (taxes/fees transparency = trust)
- Trip pages: itinerary, vouchers, manage/cancel

## Navigation
- Simple top nav: product tabs (Stays/Flights/Cars/Packages) above the
  search widget (Booking OBSERVED), account, language/currency switcher
  prominent (international by nature)
- Almosafer (AR OBSERVED): Open Sans + NotoSansArabicUI, bilingual, FAQ
  schema, national-currency pricing

## Candidate components observed in the genre
- **Search widget**: tabbed product switch + grouped fields + date-range
  picker + guest selector + big CTA (ابحث OBSERVED)
- Results card: image strip, name+stars, location chip, sub-scores
  (location/staff/cleanliness), price block with total-for-nights,
  "free cancellation" green badge (the #1 trust chip)
- Interactive map with clustered pins ↔ synced list
- Price calendar (flexible dates heat)
- Reviews: verified badges, trip type (family/solo), response from property
- Sticky booking summary on detail/checkout (price breakdown line items)

## Visual characteristics (OBSERVED)
- Photography-led: destination imagery is the hero; UI clean and quiet
- Booking class: blue-family trust + dense utility; Airbnb class: warm
  gray/coral, 12–32px radius OBSERVED (12/20/32 = card/img/action scale),
  Cereal VF type
- Ryanair class budget: yellow/orange urgency, upsell-dense (regulated
  honesty still required)
- Radius mixed: inputs 8–12px, media 12–16px, buttons pill on consumer side
- Sticky elements in 75% of travel corpus (OBSERVED — search + filters + CTA)

## Interaction patterns
- Autocomplete destinations with airports/regions grouping + recent searches
- Calendar with price coloring, flexible-month view
- Map-list sync with hover pin↔card linking
- Filters as chips + drawer on mobile; sort persistence
- Price-watch saved searches (retention loop)

## Mobile patterns
- Search-first full-screen; bottom sticky "View deals"/price CTA on detail
- Horizontal-scroll image galleries (swipe native)
- Map full-screen takeover with sheet-dragged list
- App-install prompts post-booking (itinerary utility)

## Arabic/MENA considerations (OBSERVED)
- Almosafer/Wego class: bilingual by default, SAR/AED/EGP pricing, installments
  (تقسيط via Tabby/Tamara class BNPL — regional conversion standard)
- Hajj/Umrah travel = unique MENA vertical (package IA: visa, hotel distance
  to Haram, shuttle details) — design affordances differ structurally
- Destination names bilingual (مكة/دبي with Latin secondary)
- Hijri-aware event pricing (Ramadan/Hajj seasons); family-room occupancy
  conventions (larger default groups)
- Cancellation clarity in Arabic with green/red badges mirrored RTL

## Conventions to evaluate (adopt only when model-supported)
Search widget above all, map+list duality, free-cancellation badges, review
sub-scores, total-price honesty, sticky summaries, destination inspiration
shelves, currency/language switchers.

## Overused/anti-patterns
- Fake "only 1 room left" pressure (regulatory + trust risk in EU)
- Hidden resort fees until checkout
- Carousel heroes with no search (inspiration ≠ conversion for intent traffic)
- 12-field search forms (group logically, progressive disclosure)
- Price per night shown as total-for-stay later (bait feeling)

## Strong references
Booking, Airbnb, Ryanair, Marriott (INFERRED), Expedia (INFERRED),
Almosafer (AR), Wego (AR/EN), Qatar Airways/Emirates class (INFERRED),
VisitSaudi (AR gov-tourism OBSERVED).

## Contextual decision prompts
Intent traffic (ads/direct): search-first, dense results, trust chips.
Inspiration traffic (social/brand): destination shelves + editorial. Both
share: photography warmth, price honesty, cancellation clarity. MENA adds
BNPL, bilingual IA, and religious-travel verticals.

## Corpus observations (v7.1 growth: 9+ products SOURCE-OBSERVED 2026-09-03)

Observed families: OTAs/search (wego, cleartrip, almosafer:
search-widget-first, bilingual MENA variants) - rail/multimodal
(thetrainline, omio: origin-destination + times, journey-results DNA) -
accommodation niche (hostelworld: budget-social register) - inspiration
(lonelyplanet: editorial destination content, guides-as-content) - route
planning (rome2rio: A-to-B query machine).
WHY: the query shape defines the surface (dates+place vs A-to-B time vs
browse-inspiration). Editorial travel content follows magazine DNA, not
booking DNA. WHEN NOT: inspiration imagery walls on a rail-search product
hide the timetable; booking widgets on editorial guides interrupt reading.
MENA OTAs prove search-first survives bilingual + RTL.

## Strict-audit additions (v7.2 knowledge integration, SOURCE-OBSERVED 2026-09-03)

V7.1 grouped OTAs and search together. Wave 9 splits them by whether the
product books or only compares.

| Family | Observed shape | WHY | WHEN | WHEN NOT | TRADEOFF |
|---|---|---|---|---|---|
| Metasearch (momondo cheap-flights compare, 3 inputs; kayak Search Flights / Hotels / Car Hire, skip-to-content, en-ae locale) | query widget is the page; skip-link into the form | conversion is a comparison, then an exit to a booker | compare products | owned-inventory OTAs | package-holiday chrome on metasearch fakes inventory the product does not hold |
| OTA / packager (opodo cheap flights + hotels + packages; edreams flights / hotels / vacation packages / cars; trip.com deals; ixigo flights / trains / hotels / buses, 10 h2 + 3 tables) | multi-modal bookable catalog | the product takes the booking (and often trains/buses, not only flights) | inventory-holding bookers | pure compare or editorial guides | compare-only honesty on an OTA undersells checkout; inspiration walls still hide the widget |

WHEN NOT: do not average kayak-class compare with ixigo-class book. expedia /
rehlat / goibibo remained fetch-failed this wave.