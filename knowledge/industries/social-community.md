# Industry: Social Platforms, Communities, Forums, Jobs, Directories

V2 depth: dedicated jobs/recruitment UX → jobs-recruitment.md.

## Characteristics
Identity + belonging + content velocity. Feeds are the canvas; the design
system must survive infinite user-generated chaos. Community products live
or die on norms surfaced in UI (voting, moderation states, roles).

## User intents
1. Check what's new (feed check-in loop)
2. Post/contribute (participation barrier = product design)
3. Find a community/topic (discovery)
4. Find people/answers (search)
5. Jobs: find roles; Directories: find entries

## Business goals
DAU/session loops, ad inventory (consumer social), subscriptions (creator
economy — Patreon OBSERVED), marketplace fees (jobs/directories), moderation
costs (community health).

## Candidate information-architecture patterns (not a product sitemap)
- Feed-first home + left rail (nav) + right rail (trending/suggested) — the
  Reddit/Discord-era three-column (collapses to tabs on mobile)
- Community/topic pages with rules panel, pinned posts, join states
- Post/detail threads (nested comments with voting/depth limits)
- Profiles (posts/karma/badges); notifications center; DMs
- Jobs: search (title+location) → filters (remote/salary/company) → listing
  → apply (WeWorkRemotely OBSERVED: no-login-apply simplicity)
- Directories: category browse + search + detail profiles

## Navigation
- Persistent left icon rail (desktop) / bottom tabs (mobile): Home, Search,
  Create, Notifications, Profile
- Community switchers; topic follows
- Discord OBSERVED: server rail + channel rail + chat — triple-rail pattern
  (densest nav in mainstream web)

## Candidate components observed in the genre
- Feed cards: author (avatar+name+meta), body, action bar (vote/comment/
  share/save), media states (all formats)
- Threaded comments with depth rails + collapse affordances
- Composer: low-friction posting (markdown/emoji/media) with drafts
- Trending rails, related communities, "who to follow"
- Badges/roles/flairs (trust systems made visible)
- Report/moderation states (removed/locked/NSFW shields)
- Job cards: role, company logo, location/remote chips, salary band,
  apply-CTA; saved-search alerts

## Visual characteristics (OBSERVED)
- Neutral dark canvases (Reddit, Discord) where UGC imagery supplies color;
  brand accent per community (Discord #161cbb-class saturated accents)
- Custom display faces for brand voice (Discord's ABC Ginto family OBSERVED)
  over utilitarian system stacks
- Density high: compact cards 12–16px padding, 8px radius, tight rows —
  feeds prioritize throughput over breathing room
- Forums (Hawaaworld OBSERVED): Tailwind-modernized classic forum DNA —
  avatars, postbit meta, quote trees — proof that forum conventions persist
  when modernized

## Interaction patterns
- Infinite scroll + "new posts" pill; pull-to-refresh mobile
- Optimistic UI (votes/likes instant, reconciled later)
- Keyboard shortcuts (j/k navigation, c comment — power-user retention)
- Notifications as a product surface (grouping, muting granularity)
- Onboarding: community picking → feed personalization loop

## Mobile patterns
- Bottom tab + floating create button; swipe between tabs (feed/subs)
- Media-first rendering; bottom sheets for share/actions
- Communities as tabs (horizontal scroll rails)

## Arabic/MENA considerations (OBSERVED Hawaaworld, hawaaworld-class forums)
- Hawaaworld OBSERVED: RTL Tailwind forum, `-apple-system` stacks — modern
  shell, classic forum soul; women's-community segment (كلاسيك عربي)
- Arabic feeds: RTL thread rails flip; mixed Latin content inside posts
  needs dir="auto" isolation to survive bidi
- Family/tribal community conventions: formal honorifics in UI copy,
  moderation transparency norms (Islamic etiquette rules surfaced in UI)
- WhatsApp/Telegram group culture — community web products compete with
  groups; offer structure groups lack (search, archive, threads)
- Jobs (regional): Wuzzuf/Bayt class (INFERRED) — CV-building funnels,
  WhatsApp apply paths, salary-bands normalization per market

## Conventions to evaluate (adopt only when model-supported)
Three-rail desktop/tabs mobile, vote+comment action bars, threaded collapse,
avatars+roles visible, trending rails, composer low-friction, moderation
states explicit; alerts appear at the point of action only when moderation
alerts are an in-scope capability.

## Overused/anti-patterns
- Chronological-only feeds without personalization controls (and vice versa:
  algorithmic-only without chronological escape)
- Dark patterns in notification emails (engagement-bait)
- Engagement-metric visibility that breeds toxicity (raw view counts on
  personal posts)
- Hamburger-only desktop navigation
- Forums with 2005 chrome (upgrade the shell, keep the conventions)

## Strong references
Reddit (OBSERVED), Discord (OBSERVED), Pinterest (OBSERVED), LinkedIn
(OBSERVED), Hawaaworld (AR OBSERVED), Patreon (OBSERVED), WeWorkRemotely
(OBSERVED), Eventbrite (events-directory hybrid OBSERVED), Quora (INFERRED —
blocked).

## Contextual decision prompts
Decide the loop (check-in? contribute? lurk?) and design the action bar +
notifications around it. Neutral canvas + community accents, density over
decoration, moderation UI as first-class, RTL-thread-native for Arabic.
