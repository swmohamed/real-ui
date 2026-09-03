# Industry: News, Media, Publishing, Tech Media

## Characteristics
Volume + velocity + trust. Users scan first, read second. The design must
handle 100s of updates daily, breaking-news modes, and mixed media. Ad
realities shape layout (leaderboards, in-read). Observed density is the
highest of any sector.

## User intents
1. Scan latest headlines (front page = river)
2. Follow a story (topic pages, live blogs)
3. Read an article (the core experience)
4. Search/verify (archives, fact-check)
5. Subscribe (the business conversion)

## Business goals
Subscriptions/membership (quality press), ad impressions (volume press),
syndication, app installs.

## Candidate information-architecture patterns (not a product sitemap)
- Front page: masthead + edition/date/weather strip → lead story cluster
  (1 big + 4–6 secondary) → section rivers (World, Business, Sport…) →
  opinion → video → most-read rail
- Section fronts (mirror the home at section level)
- Article page: headline, standfirst, byline, timestamp, hero media, body,
  embeds, related, comments/none
- Topic/author pages, live blogs (timestamped updates, newest-top),
  newsletters hub, paywall gates

## Navigation
- Masthead with brand wordmark centered or left + sections in one or two
  rows; BBC OBSERVED: Reith Sans, zero radius, chunky section bar
- "More" overflow drawer; persistent search; live indicator ("مباشر"
  OBSERVED on Sky News Arabia)
- Arabic portals OBSERVED: dense header link farms (Emirates NBD-style
  density applies: Youm7 460 links, stc 612) + top utility strips

## Candidate components observed in the genre
- Story cards: thumb + kicker (section label) + headline + timestamp; tight
  radius (2–6px OBSERVED across Guardian/NYT/BBC/Al-Masry Al-Youm)
- **Live blog** module (entries with time chips)
- Most-read/watched numbered list rail
- Breaking banner (top strip, single red)
- Topic tag chips; author bios; "first published / updated" dual timestamps
- Paywall gates with article-count meters (quality press)
- Video hubs with playlist rails

## Visual characteristics (OBSERVED)
- Editorial type: serif headlines + sans body is the quality-press signature
  (NYT Cheltenham+Franklin OBSERVED in CSS; Guardian Egyptian; BBC Reith
  Serif for features). Popular/mass press: all-sans (Sky News Arabia
  HelveticaNeueBold OBSERVED).
- Radius near-flat (0–6px); shadows minimal; dividers do the work
- One signal red for breaking/live/brand (BBC, CNN Arabic #000 + red accents,
  Sky News Arabia light-blue breaking canvas #E9EEFF OBSERVED)
- Dark canvases rare; reading surfaces stay light
- Arabic news: Naskh for long-form body (OBSERVED Noto Naskh loads), sans
  for headlines (Almarai/Tajawal/Roboto Arabic variants)

## Interaction patterns
- Infinite or "load more" rivers on section pages; pagination on search
- Sticky section sub-nav; progress bars on articles
- Text-size controls on article pages (accessibility maturity marker)
- Live auto-refresh with new-content pill ("3 new stories")
- Save/bookmark lists + newsletter interstitials

## Mobile patterns
- River-first single column; chunky cards; sticky top bar with section
  hamburger; AMP-heritage minimalism on article bodies
- Bottom "top stories" notifications opt-ins
- Live blogs render as cards with anchors

## Arabic/MENA considerations (heavily OBSERVED)
- RTL rivers, Arabic datelines (relative time "منذ ساعتين" standard),
  Arabic-Indic or Western digits — mass portals mix: Western digits for
  timestamps, Arabic words for units
- Prayer times + Hijri date strips in headers (utility, OBSERVED on portals)
- Video-first tilt: MENA news skews heavier video/social embeds than Western
  print-heritage sites
- Facebook/WhatsApp/X share rows dominate; X formerly primary — comment
  systems often delegated to social embeds
- Trust markers: state vs independent branding matters visually (logos,
  "official" language) — reflect the outlet's positioning honestly

## Conventions to evaluate (adopt only when model-supported)
Kicker+headline+time cards, serif/sans editorial pairing, most-read rails,
live blogs with time chips, dual timestamps, section color labels, reading
progress, related-by-topic not random.

## Overused/anti-patterns
- Infinite autoplay video with sound
- Popover interstitials on first visit
- 4px-gray-on-gray timestamps (illegible)
- Hero-portal gradients/glass cards (breaks genre trust completely)
- Burying the timestamp (verification readers need it)

## Strong references
BBC, The Guardian, NYT, The Verge, Wired, NatGeo, Medium, Substack,
BBC Arabic, CNN Arabic, Sky News Arabia, Al-Masry Al-Youm, Youm7, RT Arabic
(hybrid), Aitnews (tech niche AR OBSERVED).

## Contextual decision prompts
Default: light canvas, serif-headline system for quality positioning or
all-sans for mass/speed positioning, 2–6px radius, dense but rhythm-ed
river, live capability, honest timestamps. Differentiate via typography and
grid rhythm, not decoration.

## Corpus observations (v7.2 knowledge integration, SOURCE-OBSERVED 2026-09-03)

| Family | Observed shape | WHY | WHEN | WHEN NOT | TRADEOFF |
|---|---|---|---|---|---|
| Wire/hub (apnews: World + conflict hubs + Espanol; geography as IA) | hub nav, sparse heading shell | the product is a feed of dispatches | wire services | magazine features or GCC lifestyle | feature-well chrome on a wire slows scanning |
| Mass Arabic dailies (youm7 RTL: home / breaking / politics / incidents; ahram Arabic title) | section-first RTL IA | local readers navigate by desk | mass dailies | English GCC papers or wires | Latin-first chrome on youm7-class products is a register error |
| GCC English (thenational: News/UAE/Gulf/MENA/US/UK/Europe/Asia, 21 inputs) | geography + search weight | audience is bilingual professional | regional English papers | mass Arabic section desks | lifestyle chrome on a news spine hides desks |
| Video-broadcaster (euronews: skip-links to nav/main/search/footer, VOD framing) | a11y skip + video-on-demand | the object is video packages | TV-origin outlets | print rivers | skip-link discipline is earned; it is not a visual style |

HONESTY: dw returned an empty title/shell this wave - supporting mention only,
not a counted template. Do not invent a Deutsche-Welle layout from a failed
extract.
