# Industry: Automotive ( OEM, Configurators, Luxury Auto, EV)

## Characteristics
Brand cinema + product utility. Configurators are the deepest interactive
product on the web (color/wheel/trim state machines). Showrooms moved
online; the emotional purchase (car as identity) meets heavy spec data.

## User intents
1. Fall in love (campaign films, design stories)
2. Configure & price a model (the core tool)
3. Compare models/specs (families of trims)
4. Find a dealer / book test drive (conversion)
5. Owners: service booking, manuals, recalls

## Business goals
Configurator completions, test-drive bookings, dealer leads, brand film
engagement, owner-retention (service).

## Candidate information-architecture patterns (not a product sitemap)
- Brand home: cinematic hero (current campaign) → model lineup strip →
  story sections → finder CTA
- Model hub: gallery (exterior/interior 360°s), specs, trims, configurator
  entry, compare, inventory/dealer search
- Configurator: stage view (large render) + option panels (model → engine →
  paint → wheels → interior → packages) + running price + summary/share/save
- Ownership: service booking, accessories shop, manuals, warranty
- EV-specific: range calculator, charging-map integrations, incentive guides

## Navigation
- Model-lineup mega-menu with imagery per model; persistent "Build" CTA
- Toyota OBSERVED: tcomMed/tcomLight proprietary weights, Vehicles/Shop/
  Support/Account trees, inventory-aware CTAs
- Porsche OBSERVED: Porsche Next type, model-grid menus, minimal chrome —
  luxury register

## Candidate components observed in the genre
- 360°/turntable viewer with hotspots
- Option swatches (paint chips with real finish names — GT Silver Metallic)
- Spec comparison tables (dimension/range/performance — legit tables!)
- Price totalizers that update live with option choices
- Dealer locators with inventory cross-links
- Test-drive booking wizards; service-booking flows
- Campaign video heroes with scroll cue (the genre's emotional openers)

## Visual characteristics (OBSERVED)
- Full-bleed cinematic photography/video; UI recedes to invisible over
  imagery (letterboxed captions, hairline buttons)
- Proprietary brand type (Porsche Next, Toyota tcom) — automotive invests
  in type like fashion does
- Radius 0–4px on chrome (precision/luxury) or 16–28px on card shelves
  (consumer family vans/SUV portals) — pick per brand tier
- Dark stages for configurators (renders pop); white for value trims
- Spec tables in condensed numerals

## Interaction patterns
- Configurator: instant render swaps (preloaded spins), share-build links,
  save/resume builds, price finance toggles (cash/lease/finance payments)
- Inventory search: model+trim+radius filters
- Compare tool: 2–3 models side-by-side spec diff highlighting
- Video: chaptered films, subtitles on (silent autoplay)

## Mobile patterns
- Configurator survives: swipe turntable, bottom-sheet options, sticky total
- Thumb galleries; tap-to-reveal specs accordions
- Maps/dealer click-to-call prominence

## Arabic/MENA considerations
- Gulf = flagship auto market: full AR sites with configurators (verify
  current OEM AR implementations with targeted research when needed — corpus
  blocked region OEMs)
- Spec tables RTL; numerals Western (units km); fuel/efficiency per GSO
  standards; heat-related options (ventilated seats) marketing emphasis
- Test-drive/dealer flows via WhatsApp common
- Finance: lease calc with local banks/BNPL integration display

## Conventions to evaluate (adopt only when model-supported)
Cinematic hero + lineup strip, spec-table honesty, configurator state
machine discipline, shareable builds, dealer locator always reachable,
chaptered video, condensed numeric tables.

## Overused/anti-patterns
- Configurators that require login before building
- Slow spin-viewers (preloading failure = product failure)
- Spec sheets as PDFs only
- Overwrought scroll-stories that bury the lineup
- Fake inventory urgency

## Strong references
Toyota (OBSERVED), Porsche (OBSERVED), BMW (INFERRED — blocked), Tesla
(INFERRED — blocked), Mercedes/Audi class (INFERRED), Lucid/Rivian EV class
(INFERRED).

## Contextual decision prompts
Luxury tier: cinema + precision chrome (0–4px, proprietary type).
Mainstream tier: family-friendly shelves (16px-class cards) + pragmatic
tools. Both: configurator excellence, spec honesty, dealer conversion.

## Corpus observations (v7.1 growth: 10+ products SOURCE-OBSERVED 2026-09-03)

Two deliberately opposite poles confirmed (plus marketplaces):

| Family (n) | Observed shape | Why it differs | When / when NOT |
|---|---|---|---|
| Luxury/performance OEMs (porsche, lamborghini, ferrari, maserati, koenigsegg) | cinematic full-bleed, 1–4px or 16–28px radius poles, proprietary type | desire sells; the car is the hero image | emotional brands; NOT volume brands |
| Volume/EV OEMs (polestar, byd, nio, hyundai, volvo) | configurator-led, planet/data-forward, cleaner grid systems | buyers compare specs + values | rational purchase journeys |
| Marketplaces (mobile.de, autoscout24, hatla2ee, contactcars, yallamotor) | search/filter-first dense classifieds; RTL for MENA | inventory scanning, price comparison | listings products; NEVER copy OEM cinematic onto them |

WHY: purchase emotion (desire vs comparison) decides media-vs-data. The
corpus radius bimodality is real and intentional. MENA marketplaces
(hatla2ee/contactcars RTL) run the same search-first DNA as European ones —
regional adaptation lives in language/RTL, not in different IA.