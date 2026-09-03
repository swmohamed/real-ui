# Industry: Gaming (Platforms, Stores, Browser Gaming, Gaming Media)

## Characteristics
High-arousal entertainment. Users arrive to **play, browse, or decide** — never
to read. Sessions are short and repeated. Visual identity leans saturated,
dark-friendly, kinetic. Discovery is thumbnail-led: the game tile IS the product.

## User intents
1. Play now (browser/mobile gaming — zero friction tolerated)
2. Browse what's new/hot (discovery loop)
3. Evaluate a specific game (price, rating, requirements, trailers)
4. Track friends/esports/community
5. Read news/reviews (gaming media)

## Business goals
Ad impressions + session time (free portals); premium sales + wishlist
funnel (stores); subscriptions (Game Pass class); engagement/retention.

## Candidate information-architecture patterns (not a product sitemap)
- Home = curated shelves (Featured, New, Popular, by-genre, by-tag)
- Game detail page (play/embed CTA or buy CTA, media, description, ratings,
  related)
- Category browse (/genre/, /tag/) — tags are a first-class IA axis in browser
  gaming (OBSERVED: CrazyGames ships tag chips on tiles; Poki runs
  interest-based rows)
- Search with instant results (portals) or full search page (stores)
- Community/profile optional; news section for media brands

## Navigation
- Portals: logo + 6–10 genre links + search field + language switcher.
  Everything reachable in one tap; no account required to play.
- Stores: product dropdowns (Browse/Store/Community/About) + persistent
  cart/install-client CTA (Steam: install CTA in global nav, OBSERVED).
- Media: section nav (News, Reviews, Guides, Videos) + trending rail.

## Candidate components observed in the genre
- **Game tile/card**: 16:9 or 4:3 thumb, title, (rating badge, tag chip,
  "NEW"/"HOT" corner flag, play overlay on hover). Radius 12–16px (OBSERVED:
  Poki 16px, CrazyGames 16px tiles).
- **Shelf/row** with scroll-snap and arrow controls; hover autoplay video
  preview is the modern premium touch (stores; expensive — gate it).
- **Hero carousel/banner**: single game promo with gradient scrim.
- **Tag chips + filter bar** (genre, .io, 2-player, mobile-friendly).
- **Play button overlay** on hover/touch — portal signature.
- Rating stars/thumbs, view counts, date badges.

## Visual characteristics
- Canvas: dark (#171a21 Steam, #212233 CrazyGames) for stores/streaming-adjacent;
  bright candy-white for kid/casual portals (Poki mint #83ffe7 accent on white).
- Color: one loud accent + saturated thumbnail sea. UI chrome recedes; thumbs carry color.
- Typography: friendly geometric sans (OBSERVED: Torus on Poki, Nunito on
  CrazyGames, Proxima Nova; Inter on itch.io's indie-utility variant).
  Chunky weights 700–800 for titles; playful is allowed — this is one of the
  few sectors where rounded display type fits.
- Imagery: game art only. No stock. Illustration OK for empty states/mascots.
- Radius 12–16px + pills for chips/CTAs; shadows light (thumbnails do the work).

## Interaction patterns
- Hover: scale 1.02–1.05 + play overlay (desktop portals) — must be instant.
- Infinite scroll or "load more" on category pages (portals); pagination on
  stores/search.
- No interstitials before play on leaders; ads surround, never block first play.
- Favorites/local-recent lists (localStorage) personalize without accounts.
- Video autoplay previews on hover (store class) — desktop only, lazy.

## Mobile patterns
- Thumb-first: 2-col grids, sticky bottom ad-safe zones, play fullscreen intent.
- Bottom tab bar (Home / Categories / Search) replaces side genres.
- "Add to home screen" prompts for PWA portals.

## Arabic/MENA considerations
- Huge browser-gaming audience; portal standard = full RTL flip with localized
  categories (سيارات، ألعاب ثنائية اللاعب…) and Arabic titles/descriptions.
- Poki ships a complete /ar RTL variant (OBSERVED) — genre rows localize
  ("ماذا ستلعب اليوم؟"), mint identity constant across locales.
- Latin game titles stay Latin; wrap mixed-direction lines with
  `dir="auto"` per title to prevent bidi mangling.
- Play buttons: use icon+word (العب) — directional arrows flip.
- Kids audience → larger touch targets (56px+), louder saturation, no dark
  default (parents' daylight contexts).

## Conventions to evaluate (adopt only when model-supported)
Thumb-first grids, one-tap play, tags as browse axis, hover preview, corner
badges, ratings on tiles, genre-colored accents.

## Overused/anti-patterns
- Fake "play" buttons that open ads (trust killer — leaders never do it)
- Autoplay sound anywhere before first interaction
- Cluttered sidebars with 50 genre links (use chips + 8 links + search)
- Generic SaaS hero + gradient on a gaming portal (kills genre credibility)
- Tables/data UI aesthetics — wrong energy entirely

## Strong references
Poki (+/ar), CrazyGames, itch.io (indie-utility counterpoint: 2–4px radius,
Lato, text-forward), Steam (store density), IGN/GameSpot (media), Roblox,
Epic Games Store (INFERRED — blocked from corpus; verify with targeted current
research when the reference matters).

## Contextual decision prompts
For a browser-gaming portal default: light candy canvas OR dark store canvas
(audience-dependent), 16px-radius tiles, 2-col mobile/6-col desktop grid,
hover-play overlay, tag chips, instant search, zero-friction play. Deviate
only with a stated audience reason (e.g., horror-games vertical → dark).

## Strict-audit additions (v7.2, SOURCE-OBSERVED 2026-09-03)
- Console/platform portals (playstation, nintendo, blizzard observed): hero = newest flagship game as full-bleed media; store nav (deals/new/genres) is secondary chrome; heavy motion-forward art direction by design (entertainment context) — contrast with browser-game portals (poki, crazygames, kongregate, gamejolt observed): instant-play grid, thumbnails-first, zero splash pages, because the product promise is "playing in 5 seconds".
- WHEN portal: platform has catalog gravity. WHEN instant-grid: time-to-play is the conversion metric. Both observed to coexist in category — never average them into one template.
