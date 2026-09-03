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

## Candidate information-architecture patterns (not a product sitemap)
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

## Candidate components observed in the genre
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
  calendar standard for KSA) — verify current references with targeted research
- Hijri/Gregorian dual calendars in all reference tools; Arabic month names
- Arabic reference products: RTL infoboxes, Arabic transliteration + Latin
  scientific names side by side, Quranic-text display rules (specialized
  typography — never default fonts)
- Units: metric standard regionally; °C, km, kg

## Conventions to evaluate (adopt only when model-supported)
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

## Contextual decision prompts
Instrument discipline: neutral chrome, data as hero, interaction = state
control (sort/filter/layer), typography for scanning numbers. Decoration
budget near zero; memorability comes from data clarity and speed.

## Corpus observations (v7.1 growth: 11 products SOURCE-OBSERVED 2026-09-03)

| Family (n) | Observed shape | Why it differs | When / when NOT |
|---|---|---|---|
| Query engines (arxiv, pubmed) | one search box + advanced filters; results ARE the site | expert exact-lookup behavior | scholarly search; NOT consumer tools |
| Calculator/utility grids (calculator.net, rapidtables, symbolab) | tool-first, near-zero chrome, dense link grids, ad-supported plainness | user wants the tool instantly; speed+SEO beat polish | utilitarian tools; do NOT "modernize" into hero sections |
| Computational engine (wolframalpha) | THE single query input as the entire page | one job, one box | compute products |
| Map-canvas (windy) | full-viewport interactive canvas, controls overlay | spatial data IS the interface | geo products |
| Agencies (nasa, esa, noaa, usgs) | mission news + data portals; heavy content + topic trees | public communication + data duty | agencies; NOT pure tools |
| Open data/APIs (open-meteo) | docs + pricing + playground | developer buyers | API products |

WHY: intent span. Utility users have 10-second jobs; researchers run long
query sessions; agencies publish. A hero section on calculator.net would be
active harm; a bare box on NOAA would hide the mission. Plainness is a
legitimate professional register here (generic-polish list applies).

## Corpus observations (v7.3 diversity, SOURCE-OBSERVED 2026-09-03)

| Family | Observed shape | WHY | WHEN | WHEN NOT | TRADEOFF |
|---|---|---|---|---|---|
| National search (yandex Images/Video/Maps/Translate/Weather/Mail; baidu) | multi-service query home | the homepage is infrastructure | portal markets | a calculator or a journal | Wolfram-style query chrome on Baidu is the wrong density story — these are OS-like portals |
| Research indexes (jstor; semanticscholar AI-Powered Research Tool) | search + paper identity | the object is a paper | scholarly search | public weather canvases | |

V7.5: a live weather/flight map is a spatial-canvas job
(`interface-families/spatial-canvas.md`). A language or product handbook
is `interface-families/reference-docs.md`. Neither is a NASA mission tree.

## Corpus observations (v7.4 rejected energy category, SOURCE-OBSERVED 2026-09-03)

Retail energy was researched as a candidate category (waves 16+21). After
stripping group IR, honest product-true count sat near the floor but the
jobs split: switch/quote vs outage/account vs listed-group IR. Energy is
not a new industry module. Keep retail utility here; group IR belongs in
b2b-enterprise.

| Family | Observed shape | WHY | WHEN | WHEN NOT | TRADEOFF |
|---|---|---|---|---|---|
| Retail switch / tariff (octopus-energy cheaper/green tariffs; edf Lock in your energy prices; britishgas Flash Sale + quote; ovoenergy Get a quote; eonnext tariffs; origin-energy electricity/gas/internet; simplyenergy / mercury-nz / genesis-nz) | quote or tariff as the home | the household is switching supplier | contestable retail markets | weather instruments or Enel-class IR | a NASA mission tree on Octopus hides the tariff; IR chrome on a quote hides unit rates |
| Account / outage utilities (coned Pay Bill / Outages / Start-Stop; pge Climate Credit + languages; kplc Customer service / Report Crime; cemig SERVIÇOS; enel-br Esta sem energia) | bill + outage + move-in as first jobs | the visitor already has supply | incumbent utilities | green-tariff challengers or weather maps | |
| Group energy IR (enel Group; engie transition; eskom Holdings; tata-power Investor hub; tokyo-gas personal/corporate split) | results, transition, investors | public site serves capital markets / policy | listed groups | household switch | |

Hydro-Quebec returned a geo-block page; octopus-us was an empty shell.
Retail/account fetch-ok products are filed here; group IR is filed under
b2b-enterprise; geo-blocked or empty shells stay uncounted. Do not invent
a smart-meter dashboard from any of them.
