# Observed Findings — Real Web Corpus (2025)

Distilled from live code-first research: **156 websites fetched across ~45
industries and 5 regions; ~31 MB of production CSS parsed; 145 sites yielded
full CSS evidence.** Every number below is **SOURCE-OBSERVED** in the corpus
unless labeled otherwise: it describes fetched source, not verified rendering
or runtime behavior. Raw JSON evidence lives in `research/reports/`.

Corpus composition: global leaders (Stripe, Apple, GitHub, BBC, gov.uk,
Airbnb, Vercel, PayPal, ESPN, Toyota, MoMA…), conventional high-traffic sites,
and a dedicated MENA/Arabic track (31 RTL sites: youm7, SkyNewsArabia,
Jumia EG, Jarir, Emirates NBD, Al Rajhi, stc, Almosafer, HungerStation,
Property Finder, Shahid, Kooora, FilGoal, Salla, Zid, Edraak…).

## 1. Breakpoints — what the real web actually uses

Media-query width frequency across 145 sites (count = sites using that width):

- **Most prevalent:** 768px (91/145 sites, 63%) and 1024px (63/145, 43%).
- **Common:** 767 (54), 1200 (46), 1280 (41), 600 (34), 480/640/1440
  (32 each), 1023 (27), 992 (25), 991 (24), 320 (21), 1920 (20).
- **Situational:** 375 (13), 576 (19), 599 (10), 769 (11), 960 (12),
  1100 (8), 1199 (17), 1279 (13), 1536 (11), 1600 (14).

Interpretation (OBSERVED + INFERRED):
- Paired values (600/601, 767/768, 1023/1024, 1279/1280) show **two strategies
  coexisting**: desktop-first `max-width` (799, 1023, 1279, 1439) and
  mobile-first `min-width` (641, 769, 1025, 1281). Modern Tailwind-era sites
  skew mobile-first; legacy enterprise skews desktop-first.
- At least one width in a 640/768/1024/1280 candidate set appears in 104/145
  sites (72%); only 18 contain all four in the retained CSS evidence. This set
  is a useful research prompt, not a universal breakpoint system. Choose
  project breakpoints from content stress and platform needs.
- Only ~19% of sites use container queries yet (2025) — but adopters are the
  design-system leaders (Spotify 11 `@container` blocks, gov.uk 4, Coursera 8,
  Kooora 6, CrazyGames 6). Treat as progressive enhancement, not foundation.
- RTL/MENA source samples share several common candidates with the wider
  corpus (notably 768, 1200, 767, 1024, 992, 600, 1440, 1280). This does not
  authorize one grid: localized content and task stress still determine each
  product's breakpoints.

## 2. Typography — the real font stack of the web

**Latin (OBSERVED, by site count):**
- System stacks dominate: `sans-serif` alone (24), `-apple-system`/`ui-sans-serif`
  stacks (12+), Arial fallback (15).
- **Inter is the #1 custom typeface (17 sites)**, incl. variants Inter Display,
  Inter Tight. Then: Open Sans (5+), Roboto (5), Helvetica Neue (6), Georgia (5).
- Brand proprietary faces define identity tier: Söhne (Stripe), SF Pro (Apple),
  Airbnb Cereal VF, BBC Reith Sans/Serif, NYT Cheltenham + Franklin, MoMA Sans,
  UberMove, Porsche Next, GDS Transport (gov.uk), Torus (Poki), Roobert (Twitch).
- Monospace = product credibility signal: `ui-monospace`/`var(--font-mono)` in
  19+ sites (dev tools, crypto, fintech status pages).
- Google Fonts is NOT the default for top-tier sites — self-hosted/subset
  faces with `font-display` + fallback metrics are (INFERRED from woff2 preloads).

**Arabic (OBSERVED, 31 RTL sites):**
- Fonts seen: **Tajawal** (Jarir), **Almarai** (FilGoal; 4 Google Fonts loads
  corpus-wide), **Dubai** (Extra.com — the UAE government typeface),
  **Noto Kufi Arabic** (Almentor), **Noto Sans Arabic** (4 sites; Disney+,
  Almosafer fallback), **Noto Naskh Arabic** (2), **Readex Pro** (2),
  Arial as blunt fallback (7 RTL sites — legacy).
- Latin↔Arabic pairing observed: `Open Sans + NotoSansArabicUI` (Almosafer),
  `Inter + Noto Kufi Arabic` (Almentor), `Suisse/Codec Pro + Tajawal` (Zid),
  `Amazon Ember + local Ember Arabic` (Amazon.eg).
- Pattern: MENA leaders pair a geometric Latin sans with a geometric Arabic
  (Tajawal/Almarai match Inter/Open Sans energy). Naskh appears where trust and
  editorial reading matter; Kufi for headers/edgy brands.

**Type scales (SOURCE-OBSERVED):**
- The most prevalent retained values by site are 16px (73), 14px (68), 12px
  (61), 1rem (55), and .875rem (42). Retention is limited to each site's top
  extracted values, so this is not a declaration-share measurement.
- 18–32px values are also common in source. Which elements use them and
  whether they are above the fold requires render/runtime inspection.
- rem scales mirror Tailwind's: 1, 1.125, 1.25, 1.5, 2, 2.25, 2.5, 3.
- **h1 discipline is real: average exactly 1.0 h1 per homepage across corpus.**
- Body line-height conventions: 1.5–1.7; UI labels 1.2–1.3.

## 3. Color & theming

- `theme-color` appears on 57/145 CSS-evidence sites (~39%); sampled values
  include:
  Stripe #635bff-family blue/purple, TED #EB0028 red, NHS blue family,
  Kooora green, Aqarmap #007dbe, Extra #0065A4, Shahid #0c9 (MBC green).
- Dark-mode via `prefers-color-scheme` in CSS: only 11% (manual toggles
  dominate via class strategy — INFERRED).
- Streaming/gaming/crypto default to dark canvases WITHOUT media queries
  (hard-coded dark identity, OBSERVED: Steam #171a21, Disney+ deep navy).
- Gradients appear in 100% of the six entertainment/streaming source samples,
  93% of 15 finance samples, and 84% of 25 SaaS samples. Presence does not
  prove visible prominence. Volume differs: Disney+ 230
  declarations vs Stripe 3. Gradient COUNT is a personality dial.

## 4. Radius — the real numbers

Top border-radius values across corpus (sites): **4px (62), 8px (35), 3px (34),
10px (32), 2px (31), 6px (29), 12px (26), 16px (24), 20px (22)**, pill
(9999/999/100/50px) appear in at least 34 sites in the retained top-value
evidence (one site counted once).
- **The real web is much less rounded than AI defaults.** 2–6px is the
  institutional/news norm; 8–12px is the product norm; 16–24px is reserved for
  media cards and playful/consumer brands (Airbnb 12/20/32; Poki 16;
  CrazyGames 16/30; Shahid 16+pills).
- Pills = action language (chips, tags, CTAs), not container language.
- Finance: 3–5px core + 10px cards (Monzo corner-radius tokens).
- Government/health: 0–4px (BBC literally `border-radius: 0`).

## 5. Component & layout facts

- Container max-widths (retained SOURCE-OBSERVED values): 1280 (12 sites),
  1200/1024 (10 each), and 640 (9) are most prevalent. The top-value sample
  cannot prove larger container values are absent.
- A viewport containing `width=device-width` appears on 130/145 sites (~90%);
  `viewport-fit=cover` (notch) on modern iOS-aware sites; **`maximum-scale=1`
  still appears — it's an accessibility violation to avoid.**
- Sticky positioning: 49% of sites (nav bars, filter bars, app CTAs).
  Travel/food sector leads (75%) — search sticks because search IS the product.
- backdrop-filter blur: 35% overall, but **83% of streaming** (poster scrims)
  and 47% of finance (frosted headers). Cost: GPU compositing on scroll.
- Shadows: 92% of SaaS, 100% of finance/auto, but light and tiered
  (2–3 elevation levels via tokens, e.g., `--corner-radius` + shadow pairs).
- Tables: only 2% of homepages ship `<table>` — comparison UIs are built as
  CSS grids/cards (OBSERVED) — but data-heavy internal pages still use tables.
- `<dialog>`: 6% native adoption; custom modal stacks persist.
- Semantic reality (homepages): header 68%, nav 72%, main **57%**, footer 51%,
  article 20%. "Main is missing on 4 of 10 real sites" — do better, not equal.

## 6. Interaction & motion signals

- `:focus-visible` styled in 55% of sites (up from historical ~0 — the
  focus-visible era is real). Leaders: gov, NHS, dev tools.
- `prefers-reduced-motion` respected by 40% — a baseline credibility marker.
- Transition declarations per site: tens to low hundreds; animation keyframes
  usually <30 per site except entertainment (Disney+ uses gradients+scrims more
  than keyframes; Youm7-style news sites run tickers/marquees via keyframes).
- Hover styles remain the #1 interaction affordance in CSS (`:hover` counts in
  hundreds per site).

## 7. RTL / Arabic implementation reality (31 RTL sites)

- **21 of 31 use explicit `[dir="rtl"]` / `:dir(rtl)` CSS rules**; only 2 use
  `:lang(ar)`. Most modern stack = logical properties + Tailwind `rtl:` variants
  (OBSERVED on Al Rajhi, Arabian Oud `rtl:group-hover:-translate-x-2`).
- Real bugs OBSERVED (learn from them): Al Rajhi ships `lang="ar"` with **no
  `dir` attribute** on html; beIN serves `ar-mena` lang with **no dir**; Zid's
  Arabic homepage served `lang="en"`; several MENA portals hardcode Latin-only
  meta. Emirates NBD's Arabic CTA extracted as "-->" (icon font arrows in RTL).
- Bilingual conventions OBSERVED: language toggles as ع/EN pairs (beIN), hreflang
  alternates on leaders (Amazon.eg/-/ar/ vs /-/en/ path strategy), UAE gov
  portal at u.ae/ar with Bootstrap + Tailwind hybrid.
- Directional icon handling OBSERVED: rotating arrows with
  `rtl:[--rotate:180deg]` (PayPal global nav `rtl:[--glnv-after-icon-rotate:180deg]`),
  Arabian Oud flipping chevrons via `rtl:group-hover:-translate-x-2`;
  Kooora's `fco-` design system carries its own icon placeholder set.

## 8. Framework reality

- The legacy framework-hint report flagged Tailwind on 90/145 sites, but the
  original detector treated generic `flex`/`grid` class names as Tailwind and
  therefore cannot support an adoption-rate claim. The detector is now
  restricted to distinctive responsive/state variants or arbitrary-value
  grammar; corpus prevalence is **UNVERIFIED until reports are regenerated**.
  Utility-class implementation remains a project choice, not a corpus mandate.
- Next.js on 27% of sites; jQuery persists on 21% (33) — mostly MENA enterprise
  and legacy retail; Bootstrap on 17%; Font Awesome on 29% (46) — still the
  most common icon system on the real web (MENA: stc, Youm7, Emirates NBD).
- Design-token namespaces OBSERVED: `--hds-` (Stripe), `--cds-` (Coinbase,
  Coursera), `--fco-` (Kooora), `--glnv-` (PayPal global nav), `--sk-` (Apple),
  `--styleguide-` (Property Finder), `--sbsa-` (Zillow), `--encore-` (Spotify).
  Token prefixing is how real systems namespace intent.

## 9. Industry signal deltas (OBSERVED aggregates)

| Sector | Radius mode | Gradients | Blur | Sticky | Container-query | Signature |
|---|---|---|---|---|---|---|
| SaaS/dev | 3–8px, tight tokens | 84% (subtle) | 36% | 56% | **44%** | mono accents, `--token` systems |
| Ecommerce | 4–12px | 69% | 31% | 54% | 0% | proprietary display faces, pill CTAs |
| Travel/food | 4–16px mixed | 75% | 38% | **75%** | 0% | big search widgets, card grids |
| Finance/banking | 3–10px, 100px pills | 93% | 47% | 53% | 13% | trust blues, serif-or-none, shadow tiers |
| News/media | **2–6px, near-flat** | 69% (hero only) | 31% | 50% | 25% | editorial serifs, dense grids, reds |
| Entertainment | 2–16px + pills | **100%** | **83%** | 67% | 33% | dark canvases, poster scrims |
| Gaming | **12–16px** | 86% (loud) | 29% | 57% | 14% | saturated accents, Torus/Nunito |
| Gov/health | 0–4px | ~40% | ~12% | 25–29% | 12% | GDS patterns, blue links, zero chrome |
| Sports | 4–10px + pills | 80% | 20% | 40% | 20% | condensed display type, reds/blacks |
| Social/community | 2–16px | 75% | 50% | 50% | 0% | brand type, dense feeds |
| Creative/museum | 0–12px | 70% | 30% | 60% | 20% | custom faces, editorial layouts |
| Auto/luxury | 1–4px **or** 16–28px | 100% | 50% | 50% | 17% | cinematic full-bleed, proprietary type |

## 10. Geo-behavior (OBSERVED)

- PayPal.com served **`lang="ar-EG" dir="rtl"`** with Arabic CTAs ("بدء
  الاستخدام") to an Egyptian IP — global brands localize by geo+accept-language,
  including full RTL flip with `rtl:` utility variants.
- Porsche served its global EN page from Egypt; Amazon.eg serves Arabic-first
  with English at `/-/en/`; Amazon.sa mirrors. URL grammar (`/-/ar/`, `/ar/`,
  `?lang=`) is inconsistent across MENA — pick path-segment strategy.

## 11. Accessibility reality check

- 17 of 156 sites still ship `maximum-scale=1` (zoom blocking — including
  several majors: vercel, disneyplus, nba, spotify, toyota, almosafer-ar,
  emiratesnbd-ar, kooora, filgoal, almentor, hawaaworld...). Copy leaders,
  not the median.
- focus-visible 55%, reduced-motion 40%, semantic main 57%: the real web is
  mediocre on average. The Skill's floor must be ABOVE the observed median,
  matching the leaders (gov.uk, NHS, GitHub, Stripe), not the average.
