# Industry: Science, Reference, Utilities (Weather, Maps, Tools)

## Characteristics
Task-pure products: answer-now interfaces. The best ones feel like
instruments — data density with hierarchy, zero decoration. Reference
products (encyclopedias, docs) prize skimming + citations.

## User intents
1. Get the answer/data NOW (weather at my location, launch schedule,
   fact lookup)
2. Scan a structured overview (tables, maps, timelines)
3. Verify/cite (sources, DOIs, revisions)
4. Go deeper (linked references)

## Business goals
Engagement/recency (weather apps), subscriptions (data products),
institutional authority (science orgs), public-good mandates.

## Information architecture
- Utility: location-first home → current conditions → hourly strip →
  daily grid → maps/radar tabs → alerts
- Science orgs: mission + missions/projects (NASA model: mission pages as
  narrative product pages), news/media hub, education branch, data portal
- Reference: article-first with infobox sidebars (the Wikipedia model —
  INFERRED for en-wiki from blocked fetch; structure is public knowledge),
  citations, interlanguage links
- Academic publishers (Nature OBSERVED): article pages with figure carousels,
  reference lists, metrics (citations/altmetric), subject trees

## Navigation
- Utility: search/location input prominent, unit toggles (°C/°F), map layers
- Science: mission/project trees, media types (images/videos/audio)
- Reference: search-first + category trees + interwiki/language links

## Components that define the genre
- Data tables with sortable headers + sticky first columns
- Map layers with legends (radar/satellite/temperature)
- Hourly/daily forecast strips (scroll-snap cards)
- Alert banners (severe weather = red system + icon, not color-only)
- Infobox tables (reference sidebars), citation lists with DOI links
- Figure viewers (scientific imagery with captions + licensing)
- Mission/event countdowns; orbit trackers

## Visual characteristics (OBSERVED)
- NASA OBSERVED: dark-space canvas, imagery-led, mission branding
- Weather OBSERVED: bright utility canvases, high-contrast data, brand
  accent for actions
- Nature OBSERVED: academic serif body (reading-grade), tight editorial
  grid, metrics chips
- Zero-radius or small-radius data chrome; tabular numerals mandatory
- Maps/visualizations supply the color; UI stays neutral

## Interaction patterns
- Location detection with graceful manual fallback
- Unit/format persistence (localStorage); deep-linkable states (map center,
  selected layer)
- Table sort/filter memory; export options (CSV where appropriate)
- Alerts: subscription flows (push/email per severity)

## Mobile patterns
- Widget-scale current-state cards; swipe hour strips
- Maps with native gestures, layer sheets
- Offline-tolerant basics (last-known data with timestamps)

## Arabic/MENA considerations
- Prayer-time utilities: institutional-grade Arabic utilities (Umm al-Qura
  calendar standard for KSA) — verify current references in Deep Mode
- Hijri/Gregorian dual calendars in all reference tools; Arabic month names
- Arabic reference products: RTL infoboxes, Arabic transliteration + Latin
  scientific names side by side, Quranic-text display rules (specialized
  typography — never default fonts)
- Units: metric standard regionally; °C, km, kg

## Conventions (follow)
Answer above the fold, sortable/sticky tables, alert systems with severity
hierarchy, deep-linkable states, citation/source prominence, tabular
numerals, dual calendars for MENA.

## Overused/anti-patterns
- Splashy hero animations before the data
- Infographics that decorate instead of inform (chart junk)
- Non-deep-linkable map states
- Light-gray data text
- PDF-only datasets

## Strong references
NASA (OBSERVED), Nature (OBSERVED), weather.com (OBSERVED), UN (OBSERVED),
Wikipedia (INFERRED — blocked; model is public knowledge).

## Decision guidance
Instrument discipline: neutral chrome, data as hero, interaction = state
control (sort/filter/layer), typography for scanning numbers. Decoration
budget near zero; memorability comes from data clarity and speed.
