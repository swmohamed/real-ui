# Industry: Creative, Culture, Portfolios, Art, Museums, Events, Photography

## Characteristics
Expression-forward: the design IS the portfolio. Conventions exist to be
mastered then bent. But the best creative sites still obey usability floor —
expressive ≠ unusable. Distinctive typography and layout risk are the tools.

## User intents
1. Judge skill/taste (recruiters, clients, curators — fast, skeptical)
2. Consume work (browse galleries, read essays, view exhibitions)
3. Plan a visit (museums: hours, tickets, exhibitions calendar)
4. Attend (events: lineup, tickets, logistics)
5. Hire/contact the creator

## Business goals
Commissions/jobs (portfolios), ticket sales (museums/events), memberships/
patronage, cultural authority, community engagement (creative platforms).

## Candidate information-architecture patterns (not a product sitemap)
- Portfolio: Home = work samples immediately → selected works → about/bio →
  contact; resume/press secondary. The portfolio rule: work above the fold,
  no "loading intros."
- Museum: Visit (plan) / Exhibitions (now+upcoming) / Collection (search) /
  Learn / Shop / Membership / Donate — MoMA OBSERVED: MoMA Sans custom type,
  Nuxt-powered, editorial grids
- Events: lineup/speakers grid → schedule → venue/travel → tickets tiers →
  sponsors
- Photography platforms: feed/masonry + curated collections + licensing flows
  (500px OBSERVED: dense masonry, minimal chrome)

## Navigation
- Portfolio: minimal (Work / About / Contact) — often experimental hover
  states, but always discoverable
- Museum: institutional nav + ticket CTA persistent; exhibition hero as
  temporal skin (the site re-skins per show — design for themability)
- Event: countdown + ticket CTA sticky from first pixel

## Candidate components observed in the genre
- Full-bleed case-study heroes; project galleries with captions
- Exhibition cards (image + dates + status: Now/Upcoming/Past)
- Collection search + filters (artist, medium, era, on-view)
- Lineup grids (speaker/artist cards with roles)
- Schedule tables/timelines; venue maps; sponsor tiers
- Masonry/packery feeds (photography); lightboxes with EXIF/licensing info
- Artist statement typography pages (editorial essays)

## Visual characteristics (OBSERVED)
- Museum class: custom or rare typefaces (MoMA Sans, Tate regular OBSERVED
  families), generous whitespace, editorial grid discipline, near-zero
  radius, system-quality contrast despite avant styling
- Portfolio platforms: canvas exposes work (Cargo OBSERVED: template system
  with designer fonts — restraint as platform)
- Award-scene sites (Awwwards/CSSDA OBSERVED): experimental hero typography,
  asymmetric layouts, WebGL accents — treat as inspiration upper-bound, not
  default for client work
- Events: bold poster-heritage type, bright duotones, ticket urgency honest
- Photography: chrome recedes to near-invisible (black/white UI, images rule)

## Interaction patterns
- Hover-expressive states (scale/parallax/cursor) on covers — desktop only,
  always with reduced-motion off-switch
- Scroll-storytelling sequences (museum exhibitions, case studies)
- Lightbox flows with keyboard navigation (← → Esc)
- Ticket tier selection with countdown + group options
- Collection filters with faceted search (medium/era/on-view)

## Mobile patterns
- Galleries: swipe-native, captions persistent; avoid hover-only affordances
- Events: schedule personalization (my lineup) + add-to-calendar
- Portfolios: degrade gracefully — kinetic covers become static, speed first

## Arabic/MENA considerations
- Arabic calligraphy + Kufi display as authentic identity (not "exotic"
  accent for Western brands) — work with type designers for custom Arabic
- Cultural institutions: bilingual AR/EN with equal design quality in both
  (Sharjah Art Foundation / Ithra class — INFERRED; verify with current
  targeted research when the reference matters)
- Galleries/events: Hijri+Gregorian dates side by side; RTL editorial layouts
  with Arabic-first typographic hierarchy
- Dialect vs MSA: statements in MSA, marketing voice may carry dialect warmth

## Conventions to evaluate (adopt only when model-supported)
Work-first portfolios, exhibition themability, visit-info clarity, honest
tickets, lightbox keyboard support, custom type as identity, restrained
chrome for image-first products.

## Overused/anti-patterns
- Intro animations before content (recruiters leave)
- Mystery navigation (icon-only unlabeled) — expression that costs task clarity
- Parallax-everything (motion sickness + perf)
- Fake-3D clutter on editorial museum content
- Scroll-jacking hijacks (fine line between narrative and trap)

## Strong references
MoMA (OBSERVED), Tate (OBSERVED), Awwwards (OBSERVED), CSSDA (OBSERVED),
Cargo (OBSERVED), 500px (OBSERVED), Flickr (OBSERVED), Behance/Dribbble
(OBSERVED platforms), TED (OBSERVED events hybrid), Eventbrite (OBSERVED).

## Contextual decision prompts
Define the expression budget: institution (10% risk), event (30%),
portfolio (50%), art piece (70%+). Spend it on typography + layout, keep
the usability floor intact. Never spend the whole budget on motion.

## Corpus observations (v7.1 growth: 10+ products SOURCE-OBSERVED 2026-09-03)

Observed families: stock/photo marketplaces (unsplash, pexels: search+grid,
license-first) - artist portfolio communities (artstation, deviantart:
artwork grids + profile surfaces) - museums (tate, moma: exhibition and
editorial DNA, visit-info hierarchy) - art market (artsy: gallery/listing
hybrid) - lyrics/knowledge (genius: annotation UI) - events discovery
(songkick, bandsintown: artist-tracking tools).
WHY: license model vs exhibition model vs market model. Museums answer
"visit + what is on"; marketplaces answer "find + license"; communities
answer "show my work". WHEN NOT: e-commerce grid density on museums
flattens editorial hierarchy; museum whitespace on stock grids wastes
scan throughput.