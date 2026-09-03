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
  groups; offer structure groups lack (search, archive, threads).
  Dedicated messengers, team channels, and mailboxes are a different
  workspace (`interface-families/conversation-space.md`). A public feed
  is not Slack.
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

## Corpus observations (v7.1 growth: 8+ products SOURCE-OBSERVED 2026-09-03)

Observed families: microblogs/federated (mastodon.social, bsky, threads:
feed-first, timeline DNA) - interest communities (letterboxd, trakt,
last.fm, fandom: OBJECT-centered - the film/show/artist page is the social
object; community forms around artifacts) - reading communities (goodreads:
catalog+shelves) - messaging (signal, telegram: protocol-first marketing)
- event communities (meetup, eventbrite: discovery rails).
WHY: the social OBJECT decides structure. Feed products optimize the
stream; object-communities optimize the artifact page + personal
collection (letterboxd diary/shelves). WHEN NOT: feed DNA on an
object-community hides the collections; artifact-page density on a
microblog kills the stream.

## Strict-audit additions (v7.2 knowledge integration, SOURCE-OBSERVED 2026-09-03)

| Family | Observed shape | WHY | WHEN | WHEN NOT | TRADEOFF |
|---|---|---|---|---|---|
| Messenger / super-app marketing (line; wechat Chats/Calls/Life Services; viber Download/Features/Communities/Security/Business) | download + features; web is distribution | the product lives in the native app | chat super-apps | web-native communities (reddit-class) | putting a feed on a messenger homepage fakes a product that is not on the web |
| Live community (twitch: thin SPA shell) | web is a player/discovery app, often JS-empty to static fetch | live video + chat is the object | livestream platforms | text forums | static marketing chrome on a live product is a fetch artifact - do not over-read |
| Forum/feed (reddit: thin SPA, 1 form / 4 inputs) | the logged-out web is a teaser; the product is communities | object = thread + subreddit | link aggregators / forums | messenger download pages | SPA shells prove little about in-app IA |

HONESTY: several social fetches returned thin shells. Treat those as
distribution pages, not as proof of in-app IA. The v7.1 object-vs-feed split
still holds for web-native communities (letterboxd vs mastodon).

## Corpus observations (v7.3 diversity, SOURCE-OBSERVED 2026-09-03)

| Family | Observed shape | WHY | WHEN | WHEN NOT | TRADEOFF |
|---|---|---|---|---|---|
| Regional forums (nairaland Forum, 2 forms / 4 inputs / 3 tables) | thread list, dense tables | the object is the topic thread in a national conversation | text forums | messenger download pages | a LINE download page on Nairaland hides the threads |
| Platform-group marketing (kakao culture/group/history/AI/services, ko; naver-blog 41 inputs) | corp or blog-host chrome | web is identity + hosting; the social product is elsewhere | super-app vendors, blog hosts | web-native object-communities | |

## Corpus observations (v7.4 rejected dating category, SOURCE-OBSERVED 2026-09-03)

Dating was researched as a candidate category (wave 20: 15 fetch-ok, below
floor). Most pages are app-download shells. Store as a social family, not
a module. Matrimony is not Tinder.

| Family | Observed shape | WHY | WHEN | WHEN NOT | TRADEOFF |
|---|---|---|---|---|---|
| App-first dating (tinder empty nav; bumble Get the app; hinge designed to be deleted; happn/grindr/zoosk/pof shells) | download CTA is the page | the product lives in the native app | swipe/chat apps | web-native forums | putting a Reddit feed on Tinder fakes a web product |
| Matrimony / marriage intent (shaadi Choose Your Forever; muzz Where Muslims meet + privacy/selfie verification) | profile + intent + family/faith constraints | the job is a serious match, often with verification | marriage platforms | casual swipe shells | |

WHEN NOT: do not invent a swipe deck from a marketing homepage. Safety,
blocking, and reporting require scope evidence — never copy them in because
the category is "dating".
