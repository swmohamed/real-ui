# Performance-Aware Design (value vs cost, per effect)

Design decisions ARE performance decisions. Every effect below has a
budget and a justification bar.

## Images (the #1 cost)

- Formats: AVIF > WebP > JPEG; SVG for icons/diagrams
- Sizes: serve per slot (card 400–600w, grid 800w, hero 1600–2400w);
  srcset+sizes; quality 70–80
- LCP image: `fetchpriority="high"` + preload + NO lazy; everything
  below fold: `loading="lazy" decoding="async"`
- CLS 0: width/height or aspect-ratio on every image; reserved space
  for fonts/media
- Card grids ×200 items: thumbnails 2x slot max, blur-up placeholders,
  content-visibility: auto on below-fold sections
- MENA reality: budget Androids + mixed networks — test at 4G/3G
  throttling, LCP <2.5s

## Video

- Muted autoplay loop (hero): ≤2MB total ideal, 5MB hard cap; poster
  first paint; preload=none below fold
- Lazy YouTube/Vimeo embeds (facade pattern: poster + play loads iframe)
- Duration badges; captions (a11y + sound-off norm)

## Fonts

- WOFF2 subsets: latin + arabic separate; 1–2 weights above fold;
  variable font if ≥3 weights
- font-display: swap + metric-tuned fallbacks (size-adjust) — kills
  both invisible-text and layout-shift failure modes
- Self-host or ONE font CDN origin; preconnect

## CSS/JS

- Critical CSS inline for above-fold; rest deferred; Tailwind: purge
  content (real-world shipped sizes prove it works)
- Third-party scripts: defer/async + audit quarterly (tag managers grow
  30%+ payloads unnoticed); chat widgets load on interaction/idle
- Hydration discipline (Next/Nuxt): islands for content-heavy pages

## Effects cost table (the value-vs-cost ledger)

| Effect | Value | Cost | Verdict |
|---|---|---|---|
| Gradient scrim behind hero text | readability | ~0 | always OK |
| backdrop-filter blur header | depth/clean | GPU per frame, low-end jank | OK ≤1 element, test Androids |
| backdrop blur on EVERY card (glass) | trend | multiplies cost + readability risk | avoid |
| Hover transform/scale | affordance | ~0 (compositor) | always OK |
| Box-shadow tiers | elevation language | cheap, avoid animating shadows | OK static |
| Parallax scroll | depth | scroll jank on low-end | opt-in, desktop |
| WebGL hero scene | wow/memorability | 2–8MB + GPU + battery | justify per project; tier+fallback |
| Scroll-reveal fades | rhythm | cheap w/ IO batch | OK; reduced-motion off |
| Lottie animations | brand delight | 50–500KB | size-budget, once |
| Custom cursor | identity | JS/frame + confusion cost | rare, justified |
| Marquee tickers | news energy | cheap CSS but distracting + a11y | optional, pauseable |

## Core Web Vitals (the targets)

- **LCP <2.5s**: hero image/font optimization story
- **CLS <0.1**: aspect-ratio + font fallbacks + no dynamic insertion above
  content (banners! cookie bars reserve space)
- **INP <200ms**: light JS, no long tasks; split handlers; virtualize
  huge lists

## Loading UX (perceived performance)

- Skeletons matching layout; optimistic UI; progressive image (blur-up);
  stale-while-revalidate data with freshness labels; instant nav
  transitions (View Transitions API where available)

## Anti-patterns

- Full-page preloader (the instant regret); carousels of 4MB images;
  font-loading 6 weights for 1 used; blur(40px) on scroll containers;
  animating layout properties; "please wait" spinners over blank pages
- Design review question ALWAYS: "what does this cost on a 150-dollar
  Android on 3G?" — if the answer is shame, cut it
