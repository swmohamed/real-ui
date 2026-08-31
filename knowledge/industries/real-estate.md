# Industry: Real Estate & Property Portals

## Characteristics
High-value, low-frequency purchases. Users tolerate complexity (this is the
biggest purchase of their life) but reward clarity. The core UX duality:
**search/filter seriousness** + **emotional browsing** (dream homes).
Map-centric for rentals/sales; lead-gen for agents/agencies.

## User intents
1. Search by location/budget/type (filters: beds, baths, price, area, type)
2. Compare properties (shortlists)
3. Evaluate a property (photos, floor plans, location, price history)
4. Contact agent/developer (lead conversion)
5. Rent/manage (tenants: payments, maintenance — app side)

## Business goals
Qualified leads to agents (portal model: Bayut/PropertyFinder class),
listing packages (sellers), developer sales (new projects), iBuying/finance
attach (US model).

## Information architecture
- Home: search hero (location autocomplete + type + price) + quick links
  (Buy/Rent/New projects/Commercial) + popular areas + featured listings +
  agent finder
- Results: map + list split; filter bar (type, price range, beds, area sqm,
  amenities); sort (newest, price, area)
- Listing page: gallery, price + key facts bar (beds/baths/area/type),
  description, amenities checklist, floor plan, map with POIs, agent card
  with contact/WhatsApp, similar listings, payment plans (offplan)
- Project pages (developers): progress galleries, payment plans, brochures
- Area guides (SEO play: neighborhood content)

## Navigation
- Buy/Rent/New/Commercial/Agents/Find Agency primary nav; language EN/AR
  toggle prominent in MENA (PropertyFinder OBSERVED styleguide tokens
  `--styleguide-border-radius-m: 8px`)
- Aqarmap OBSERVED (Egypt): Tailwind+daisyUI tokens, valuation-CTA tools
  (احسب قيمة عقارك) — tool-led funnels for sellers

## Components that define the genre
- Search bar with location autocomplete (areas, compounds, metro stations)
- Listing card: photo carousel, price prominent, type chip, beds/baths/area
  icons row, location line, agency logo, "verified" badge
- Map cluster pins ↔ synced cards (hover linking standard)
- Key-facts icon bar (🛏 3 · 🛁 2 · 📐 165m²) — icon+number scan row
- Gallery lightbox w/ floor plan tab; mortgage calculator; price-per-m²
- Agent card: photo, rating, response-time, WhatsApp button (MENA standard)
- Shortlist hearts + search alerts (retention engine)
- Offplan payment-plan tables (10% down… installments…) — MENA signature

## Visual characteristics (OBSERVED)
- Portal utility: white canvas, blue-family or teal accents (Aqarmap #007dbe,
  PropertyFinder PF blue), 8–14px radius, dense cards
- Luxury development sites: dark cinematic, serif display, full-bleed
  renders, scroll-storytelling (Emaar/Aldar class)
- Photography: interiors/renders dominate; floor plans structured
- Type: Inter/system on portals; editorial pairing on developer sites

## Interaction patterns
- Save searches + alerts (email/WhatsApp notifications — MENA via WhatsApp)
- Gallery swipe + lightbox; virtual tour embeds (Matterport class)
- Draw-on-map search (advanced); commute search (by workplace)
- Lead forms with phone-first validation (+country code), call/WhatsApp CTAs
- Price negotiation hints, price-drop badges

## Mobile patterns
- Map-first toggle vs list-first; full-screen map with bottom sheet cards
- Sticky agent contact bar (call/WhatsApp/email) on listing pages
- Swipe galleries with key facts bar persistent

## Arabic/MENA considerations (heavily OBSERVED)
- Bilingual portals standard (Bayut EN/AR, PropertyFinder AR); Arabic
  listings search in Arabic areas; price in AED/SAR/EGP with correct formats
- **Offplan payment plans** = regional product signature (percent milestones
  tables); "چيك/تسليم" statuses with year timelines
- WhatsApp lead-gen replaces forms on many listings (response-speed culture)
- Compound/community pages (compounds are a MENA-specific property type)
- District names in Arabic with English secondary; sqm not sqft in EG/SA
  portals (regional units vary — verify per market)

## Conventions (follow)
Search-first hero, map+list duality, icon-fact bars, verified badges,
agent cards with fast-contact, alerts/shortlists, area guides, honest
price display (total vs per-m² both shown).

## Overused/anti-patterns
- Form-first UX before showing any listings (kills trust + SEO)
- Hiding location/area to force lead capture
- Fake urgency ("3 people viewing now") — legality varies; ethically out
- Static hero images on luxury without renders/galleries
- Map pin spam without clustering

## Strong references
Bayut (EN/AR), PropertyFinder (AR OBSERVED), Aqarmap (AR OBSERVED),
Zillow (OBSERVED `--sbsa-` tokens), Rightmove (INFERRED), Emaar/Aldar
(luxury dev class).

## Decision guidance
Portals: search-utility with map duality + trust badges + alerts. Developer
luxury: cinematic story + payment plans + register-interest funnels. MENA:
bilingual IA, WhatsApp CTAs, offplan tables, compound taxonomies.
