# Industry: Sports & Fitness

## Characteristics
High-energy, results-first, tribal identity. Two modes: **media** (news,
highlights, analysis) and **utility** (scores, stats, tracking). Fitness
adds coaching/tracking products. Live-ness defines the experience class.

## User intents
1. Check scores/fixtures NOW (utility mode: speed over beauty)
2. Follow a team/league (personalized feeds)
3. Watch highlights (video hub)
4. Read analysis (editorial mode)
5. Fitness: log workout / follow a plan / track progress

## Business goals
Subscriptions (streaming rights, premium analysis), engagement/habits
(fitness apps), betting-adjacent traffic (regulated markets), merch/tickets.

## Candidate information-architecture patterns (not a product sitemap)
- Scores-first home: live strip (ticker) → today's fixtures by league →
  top news → video → tables/standings widgets
- League pages: fixtures/results/tables/stats tabs
- Match page: live score header, momentum events (timeline of goals/cards),
  lineups, stats bars, commentary feed, odds (where legal)
- Club pages, player pages (stat panels)
- Fitness: today's plan, history calendar, progress charts, library

## Navigation
- League/team selector (dropdown or rail) + section nav (Scores, News,
  Video, Watch, Standings)
- Personalization: star teams → custom "my teams" strip persists
- Arabic OBSERVED: Kooora (31M-pageview-class utility) ships a dedicated
  `fco-` design system with date-bar navigation (السبت 15 أغسطس OBSERVED as
  nav CTA) — date IS navigation in scores products

## Candidate components observed in the genre
- Live score cards/cards rows: crest + abbreviation + score + minute badge
  (red live dot)
- League tables (POS/TEAM/P/W/D/L/GD/PTS) — the rare legitimate `<table>`
- Stat comparison bars (possession, shots — mirrored bars)
- Match timeline (event icons on a minute axis)
- News cards with team-colored kickers; video highlight tiles with duration
- Fitness: rings/progress bars, streak flames, calendar heatmaps, PR badges

## Visual characteristics (OBSERVED)
- Team/league colors drive accents; base canvas white (media) or dark
  (streaming-adjacent, beIN OBSERVED dark with play-icon density)
- Condensed display type for scores/headlines (Roboto Condensed OBSERVED on
  NBA/ESPN class; heavy weights 700–900)
- Kooora OBSERVED: Tailwind-based `fco-` tokens, 190 gradient declarations
  (arena-light effects), dark hero utility hybrid
- Radius 4–10px + pills (beIN 0–11px OBSERVED); reds/blacks for live urgency
- Fitness: bright motivational gradients (Strava orange class), big numerals

## Interaction patterns
- Auto-updating score cells (websocket polling) with flash-on-change
- Ticker strips for breaking transfers
- Personalized team strip with reorder
- Fitness: streak mechanics, shareable result cards (social loop)

## Mobile patterns
- Score widgets/compact cards; match pages with tabbed sections
- Live match tracker = vertical event feed
- Fitness: bottom tab (Today/Plan/Progress/Social) + quick-log buttons

## Arabic/MENA considerations (heavily OBSERVED)
- Football dominates entirely (كورة = the category name); leagues: Saudi
  Pro League, Egyptian Premier League, European with Arabic commentary
- Kooora/FilGoal/Yallakora OBSERVED trio: FilGoal (Almarai font, Bootstrap+
  Tailwind), YallaKora (dense fixtures + standings), Kooora (token-system
  maturity + bilingual) — the regional canon
- beIN Arabic OBSERVED: bilingual toggle ع/EN + dark video-first
- RTL standings tables flip (PTS column reads right); match minute + score
  direction flips; crests never mirror
- Live commentary feeds right-to-left with minute chips
  (الدقيقة ٩٠+٢ → Western digits common)

## Conventions to evaluate (adopt only when model-supported)
Scores above the fold, live state visible (red dot + minute), league tables
as real tables, condensed numerals, team-colored kickers, personalization
strip, highlight tiles with duration badges.

## Overused/anti-patterns
- Giant hero banners before scores (users came for numbers)
- Hiding tables behind tabs with no deep links
- Countdown autoplay video with sound
- Fitness-shame copy patterns (motivate, don't guilt)
- Mixed betting UI in markets where it's illegal (compliance = UX)

## Strong references
ESPN, NBA (Roboto Condensed OBSERVED), BBC Sport, beIN (AR), Kooora (AR),
FilGoal (AR), YallaKora (AR), Strava, Olympics (INFERRED — blocked).

## Contextual decision prompts
Speed-first utility or media-first editorial — decide by audience. Utility:
dense, tabular, live-updating, team colors. Media: video tiles + editorial
cards + tribal color energy. Arabic football portals: date-bar navigation,
RTL tables, Kooora-class token maturity.

## Corpus observations (v7.1 growth: 10+ products SOURCE-OBSERVED 2026-09-03)

Observed families: live-scores terminals (sofascore, flashscore, fotmob:
dense tables, live tickers, minimal chrome - scanning machines) - media
brands (skysports, goal: news-led shelves) - training/companion apps
(myfitnesspal, peloton, whoop, garmin: habit+data products, dashboard DNA)
- equipment/retail crossover (decathlon) - Arabic fitness (ayhaga RTL).
WHY: live data changes everything - score terminals are closer to trading
terminals than to media sites (density, refresh, glanceability). Companion
apps are health dashboards (progress rings, plans). WHEN NOT: media-shelf
layouts on live-score products slow the glance task; marketing-polish on
training data products hides the metrics.

## Strict-audit additions (v7.2 knowledge integration, SOURCE-OBSERVED 2026-09-03)

Official league/org sites are neither score terminals nor sports media.

| Family | Observed shape | WHY | WHEN | WHEN NOT | TRADEOFF |
|---|---|---|---|---|---|
| League / sanctioning body (nba: Tickets / schedule / League Pass / key dates; formula1: Schedule / Results / Standings / Drivers / Teams; ufc: Events / Tickets / VIP / Road to UFC) | calendar + tickets + standings as first-class nav | the product is the season and access to it | official org sites | live-score apps or news brands | ticket/VIP chrome on a score terminal hides the live table; terminal density on an org site hides how to attend |

WHEN NOT: do not average sofascore-class scanners with NBA/F1/UFC org
sites. FIFA returned an empty title this wave — supporting mention only.
Olympics/ATP remained fetch-blocked.