# UI: Media — Images, Video, Carousels, Galleries, Icons-in-media

## Images

- Ratios as system tokens (1:1, 4:3, 16:9, 3:4, 2:1, 21:9 hero) — never
  ad-hoc; aspect-ratio CSS boxes reserve space (CLS 0)
- srcset/sizes discipline: card thumbs 400–600w, grid images ~800w, heroes
  1600–2400w; AVIF/WebP with JPEG fallback; quality ~70–80
- Loading: hero eager+fetchpriority=high; grids lazy (first 1–2 rows
  eager); decoding=async
- Alt text taxonomy: decorative (alt="") vs informative (describe content)
  vs functional (describe action) — write real alt for informative
- Object-fit containment per ratio; focal-point (object-position) tokens
  for art-directed crops

## Video

- Muted-autoplay loop allowed (hero/scrim contexts) WITH reduced-motion
  bypass + pause control visible
- Posters mandatory; preload="none" for below-fold; duration badge on
  thumbnails; captions/subtitles provided (a11y + sound-off culture: 80%+
  social video watched muted)
- Player chrome: standard controls > custom (unless brand-critical);
  keyboard operable; focus-visible

## Carousels (the honest rules)

- Carousels underperform statically (well-documented: engagement decays
  after slide 1) — justify each use: true content-rotation need (hero
  promos with editorial ops, featured products) or spatial browsing
  (galleries)
- Requirements when used: visible pagination dots + arrows + swipe;
  auto-advance only with pause + 5–7s + reduced-motion off; height
  reserved (no CLS); aria-live polite off; deep-linkable slides (#slide-2)
- Scroll-snap rails > transform carousels (native gestures, a11y free)
  for card shelves

## Galleries & lightboxes

- Grid → lightbox: keyboard ← → Esc; swipe mobile; counter (3/12); captions
  persist; zoom (double-tap/pinch) where detail matters (products, art)
- Floor plans/360: tabbed media types inside PDP galleries
- EXIF/licensing info surfaces for photography products

## Hero media integration

- Scrim gradient (bottom → transparent) under text: 40–70% black gradient;
  text ≥4.5:1 over busiest image region — verify worst frame
- Poster-first video (paint image instantly, swap video when ready)

## RTL

- Galleries swipe RTL; arrow controls flip; counter order flips (٣/١٢
  with Western digits common)
- Overlays (badges, play buttons) mirror corners
- Infographic imagery does NOT auto-mirror (charts, logos stay as-is;
  directional photos may be re-art-directed per locale)

## Anti-patterns

- Background hero video >2MB total (mobile reality); autoplay with sound
- Lightbox that traps mobile back gesture; carousel that steals page scroll
- Lazy-loading the LCP image; placeholder-colored flash (LQIP/blur-up)
- Stock photos that contradict locale (wrong-side driving, wrong dress
  codes for MENA — cultural credibility detail)
