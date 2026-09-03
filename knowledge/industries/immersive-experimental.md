# Industry: VR/AR, WebGL, Immersive & Experimental Web

## Characteristics
The web's frontier lab: scroll-driven 3D scenes, shader backgrounds, physics
toys, sound-reactive visuals. Used by: XR products, creative agencies,
portfolios, game marketing, music/album sites. Highest risk of performance
and accessibility failure; highest ceiling of memorability.

## User intents
1. Experience something novel (the point)
2. Evaluate the product (VR hardware/app — utility surfaces still needed)
3. Understand capability (agencies: "can they build this?")
4. Play (interactive toys)

## Business goals
Brand differentiation, virality/shares, awards (Awwwards OBSERVED class),
hardware/app conversions for XR products.

## Candidate information-architecture patterns (not a product sitemap)
- XR product sites: standard product IA (buy, specs, support) + immersive
  hero layer — do NOT sacrifice the conversion tree for the toy
- Agency/experimental: single-page narratives with scene chapters;
  contact/credits reachable without completing the experience
- Game marketing: trailer-first + platform store links + press-kit links

## Navigation
- Persistent minimal overlay nav (must survive over canvas; contrast over
  any scene)
- Progress/chapter indicators; skip-experience escape hatch (mandatory)
- Meta Quest OBSERVED: standard commerce IA under an immersive skin —
  discipline worth copying

## Candidate components observed in the genre
- Full-viewport canvas scenes (Three.js/WebGL/WebGPU) with DOM overlays
- Scroll progress → scene state binding (scrollytelling with 3D sets)
- Cursor/pointer feedback (custom cursors, magnetic buttons)
- Loading experiences (progress with brand narrative — make waiting fun)
- Audio toggles (off by default; on = permission)
- "View in AR" quick-look buttons (USDZ/GLB on supporting devices)

## Visual characteristics
- Type over 3D: massive display faces with strong contrast scrims; kinetic
  type (variable-font weight animation)
- Palette from shaders/materials; DOM UI stays monochrome over the scene
- Custom cursor + hover-reactive meshes; grain/scanline post-effects as
  identity
- Brutalist/mono labels as "technical HUD" accents (coordinates, version
  tags — the genre's trust-detail language)

## Interaction patterns
- Scroll velocity → camera; hover → focus targets; click → scene beats
- Device-orientation parallax (mobile) with permission prompts
- Performance tiers: detect GPU/mobile → reduce (lower DPR, fewer lights,
  disable post) — graceful degradation is the professional marker
- WebGL-fail fallback: static poster + full content access

## Mobile patterns
- Mobile = often a different experience: simplified scenes or video fallback
- Touch: pinch/drag mapped to camera; disable custom scroll physics on
  touch (native scroll wins)
- Battery respect: pause rAF when hidden (visibility API)

## Arabic/MENA considerations
- Immersive Arabic type experiments (kinetic Kufi) are an open frontier —
  Arabic display in 3D scenes needs font engineering (remap to mesh or
  SDF fonts with Arabic shaping support — most SDF pipelines break Arabic
  joining! Verify rendering approach before promising Arabic in-canvas)
- RTL scene choreography: scroll-narratives read right-to-left (sequence
  order flips), camera moves invert
- Regional agencies/festivals produce award-tier Arabic immersive work —
  establish current references with targeted research

## Conventions to evaluate (adopt only when model-supported)
Escape hatches, audio opt-in, loading narrative, perf-tier detection,
fallback content parity, credits/contact outside the canvas, reduced-motion
full-bypass to static.

## Overused/anti-patterns
- 3D for 3D's sake on conversion pages (configurator? yes; SaaS pricing?
  no)
- Scroll-jacking without native-scroll fallback
- 8MB shader heroes on mobile data
- Custom cursors that break touch
- WebGL-only contact info

## Strong references
Meta Quest (OBSERVED), Awwwards winners (OBSERVED index), active campaign
sites by Active Theory/Resn/Unit9 class (INFERRED — temporal by nature;
research current examples when needed), Igloo/Yugo Nakamura class
(historical canon).

## Contextual decision prompts
Budget immersion against task: brand film moment (high), product conversion
tree (standard UI), long-tail content (fast static). Never let the scene
hold information hostage.

## Corpus observations (v7.1 growth: 7+ products SOURCE-OBSERVED 2026-09-03)

Observed families: data-essay studios (pudding.cool, informationisbeautiful,
flowingdata: scroll-narrative + chart essays) - explorable explanations
(setosa, distill.pub: interactive widgets teaching one idea) - playful
toys (neal.fun: single-purpose experiences) - spatial toys (radio.garden,
window-swap: one canvas, one interaction) - viz platforms (observable:
notebook paradigm).
WHY: narrative duty (essay) vs single-idea exploration (widget) vs toy
(one mechanic). The unit of design is the EXPERIENCE, not the page.
WHEN NOT: nav/page-pattern thinking on toys breaks them (they need one
canvas); essay scrolltelling on a utility hides the tool. Load-time
honesty matters: these are heavy pages; state loading.

## Strict-audit additions (v7.2 knowledge integration, SOURCE-OBSERVED 2026-09-03)

| Family | Observed shape | WHY | WHEN | WHEN NOT | TRADEOFF |
|---|---|---|---|---|---|
| Studio portfolios (unit9: Films/Digital/Games/VR/AR/Experiential; activetheory title-only shell) | work-index, not a product UI | the artifact is the reel | production studios | tools or toys | page-pattern nav (Pricing, Blog, Login) on a studio kills the reel |
| Viz authoring (flourish: visualization / stories / examples / industries; rawgraphs About/News) | product + examples + use-cases | the job is making a graphic | authoring tools | one-off essays | essay scrolltelling on an authoring tool hides the editor |
| Live earth/weather canvas (earth.nullschool: one h1, 1 input, 1 table; ventusky: forecast/radar/wind, 1 form/1 input) | one canvas, almost no page nav | the map IS the product | live environmental viewers | marketing sites or essay studios | putting a hero+cards around the canvas breaks the instrument |

WHEN NOT: do not average studio / authoring / live-canvas / explorable-essay
(v7.1 pudding/setosa/neal.fun) into an immersive template. seeingtheory
returned a coming-soon shell - do not treat it as a live explorable.

## Corpus observations (v7.3 diversity, SOURCE-OBSERVED 2026-09-03)

| Family | Observed shape | WHY | WHEN | WHEN NOT | TRADEOFF |
|---|---|---|---|---|---|
| Public-data essays (ourworldindata Data / Latest; gapminder Resources / About, 10 h2) | chart + explanation, donate/resources chrome | the job is understanding a dataset, not making one | public-data education | Flourish authoring or unit9 reels | an editor chrome on OWID hides the essay; a reel index on Gapminder hides the chart |
| Story-map hosts (storymaps-esri ArcGIS StoryMaps) | narrative on a map | geography is the spine | place-based stories | live weather canvases | |
