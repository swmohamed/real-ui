# Industry: Entertainment, Streaming, Music, Video, TV

## Characteristics
Poster-led dark experiences where the **content imagery is the color palette**
and the UI recedes. Browse → watch loops, recommendation quality is the
product, and the first screen must sell the emotional promise instantly.

## User intents
1. Find something to watch/listen to now (decision fatigue is the enemy)
2. Continue watching (resume affordances)
3. Browse by mood/genre
4. Watch live (sports/news channels)
5. Subscribe/manage plan

## Business goals
Subscriptions (SVOD), ad-supported viewing time (FAST/AVOD), ticketing
(cinema/events variant), churn reduction (endless "new").

## Candidate information-architecture patterns (not a product sitemap)
- Home: hero banner (featured title, autoplaying muted) → "Continue
  watching" row → "Because you watched" → genre rows → top 10 with big
  numerals → coming soon
- Title detail page: key art, synopsis, cast, episodes (series), related,
  play/trailer CTAs
- Browse: genre grids, search with people/titles/moods
- Live: EPG (channel guide) or linear wall
- Music: home shelves, playlist/album pages, artist pages, player bar persistent

## Navigation
- Minimal top bar that transparent-over-hero → solid on scroll (Netflix
  pattern family; Disney+ OBSERVED same)
- 5–8 nav items max: Home, Series, Movies, Live, My List, Search
- Profile switcher (kids/profiles) on entry
- Arabic: Shahid OBSERVED with RTL nav + live TV section ("قنوات مباشرة")

## Candidate components observed in the genre
- Hero billboard with gradient scrim bottom→title stack→CTA row
  (Play + More info)
- Landscape poster rows (16:9 cards, 8–16px radius OBSERVED Shahid 16px)
  with hover-expand cards (Netflix hover preview class)
- Top-10 row with giant outline numerals
- Continue-watching row with progress bars
- Player chrome: centered controls, scrubber with thumbnails, skip-intro,
  next-episode countdown card
- Music: persistent player bar with queue drawer; mini/expandable player
- Live badges, "مباشر" RTL equivalents (OBSERVED Shahid/SkyNewsArabia)

## Visual characteristics (OBSERVED)
- Dark canvas is genre law: Disney+ deep navy gradients (230 gradient
  declarations — scrims), Steam-class near-black for game-adjacent
- UI chrome near-monochrome; accents minimal (Shahid MBC green #0c9 OBSERVED
  as theme-color — brand accent on dark)
- 83% of streaming corpus ships backdrop-blur scrims (OBSERVED) — blur is
  genre-appropriate here (behind text over art), unlike SaaS misuse
- Type: humanist/geometric sans (Inter OBSERVED on Disney+/Spotify stacks;
  Spotify `--encore-` token family; Roobert on Twitch)
- Radius: cards 4–16px; pills for tags; full-round buttons on dark

## Interaction patterns
- Hover-expand preview cards with delayed autoplay (desktop)
- Row scroll with peek of next card (affordance), arrows appear on hover
- Keyboard/remote navigation (TV-aware focus rings!) — streaming must be
  10-foot-UI literate
- Autoplay next episode countdown; skip-intro chapters
- Music: swipe to queue, like/dislike shaping radio

## Mobile patterns
- Tab bar: Home, Search, Downloads, Profile; player full-screens with gesture
  controls (swipe down to dismiss)
- Downloads/offline shelves above the fold for travelers
- Portrait mode shorts/promos (music/social-video hybrid)

## Arabic/MENA considerations (OBSERVED Shahid/OSN+/MBC)
- Full RTL rows with Arabic titles; bilingual titles common (Arabic + Latin
  series names on Shahid OBSERVED)
- Kids/profile switches with Arabic-first content trees
- Subscription pricing in local currency + mobile-operator billing (STC/
  Etisalat/Orange billing paths) — payment UX differs structurally
- Ramadan programming hub = seasonal IA event (massive traffic moment;
  design for themeable seasonal skins)
- OSN+/MBC OBSERVED: bilingual nav toggles ع/EN

## Conventions to evaluate (adopt only when model-supported)
Hero scrim, continue row first, genre rows with peeking cards, hover
previews, progress bars, kids profiles, skip-intro, search-by-mood chips,
minimal chrome.

## Overused/anti-patterns
- Light-mode streaming UI (breaks poster contrast law)
- Grid without hover/preview affordance (feels static-dead)
- Blocking play behind login before showing any catalog value
- 20-row homepages (choice paralysis; cap curated rows)
- Sound-on autoplay anywhere

## Strong references
Disney+, Twitch, Spotify, YouTube (dual-creator ecosystem), Shahid (AR),
OSN+ (AR/EN), Netflix (INFERRED — blocked), MBC.net, Crunchyroll class.

## Contextual decision prompts
Default: dark canvas, scrim-backed hero, 16:9 rows 8–16px radius, minimal
chrome, one brand accent, hover previews on desktop, TV-focusable controls.
Let artwork carry color; UI earns invisibility.
