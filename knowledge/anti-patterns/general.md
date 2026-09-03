# Anti-Patterns: General UI/UX Failures (with why)

Each entry: pattern → why it fails → fix.

## Layout & hierarchy
- **Everything-centered pages** → kills scanning and pairing (label:value
  needs start-alignment) → center only heroes/closers
- **Two competing primary CTAs** → decision paralysis; one primary per
  view → demote second to secondary/ghost
- **Hero with no promise** (abstract tagline + "Learn more") → bounce →
  outcome-specific headline
- **Fixed-width layouts** (horizontal scroll on mobile) → responsive
  spine + fluid grids
- **Cards inside cards inside cards** → hierarchy inversion → one card
  level; lists inside cards

## Navigation
- **Hover-only dropdowns** → touch/keyboard lockout → click-open with
  hover-intent
- **Mystery icon-only nav** → comprehension collapse → icon+label
- **Nav that teleports between pages** (position/order changes) →
  reorientation cost → stable header system
- **Cookie+promo+chat+sticky-CTA stacking** → 40% viewport chrome
  (OBSERVED on several MENA portals) → one persistent + dismissibles

## Content
- **Lorem ipsum to production** → trust zero → real copy or honest
  placeholders marked TODO
- **Undated stats** ("1M+ users") → unverifiable → date + source
- **Feature lists without artifacts** → claims without proof →
  screenshot/demo/data per claim
- **Buried prices** → friction + distrust → pricing reachable ≤2 clicks

## Commerce & forms
- **Surprise shipping at final step** → #1 abandonment cause → show
  total early
- **Placeholder-as-label** → error amnesia on review → persistent labels
- **20-field single-screen forms** → abandonment → grouped multi-step
  with progress + save
- **Disabled CTA with no reason** → dead-end → explain requirement or
  enable with validation on submit

## Media
- **Autoplay sound** → instant tab-close → muted + opt-in
- **Carousel autoplay without pause** → accessibility + annoyance →
  controls + reduced-motion static
- **PDF menus/specs** → unusable on mobile + invisible to SEO → HTML
  first
- **Hero video >5MB mobile** → data + LCP death → poster + tap-to-play
  or skip on 3G

## Motion
- **Scroll-jacking** → disorientation + nausea → native scroll; choreograph
  within sections
- **Loader before ready content** → perceived slowness → progressive paint
- **Animation >500ms on UI feedback** → sluggish → 150–250ms micro
- **Parallax body text** → unreadable + jank → depth on media only

## Dark patterns (banned outright)
Fake countdowns; confirm-shaming; pre-checked paid add-ons; hidden
subscription terms; obstruction-to-cancel; disguised ads; fake activity
("32 people are viewing"); silent data sharing. Legal risk growing
(EU DSA, FTC, regional consumer law) and trust-destroying.

## Trust
- **Stock photos contradicting locale** (wrong driving side, wrong
  climate/dress for market) → subtle uncanny → localized imagery
- **Fake testimonials** → credibility collapse when detected (and
  detection is easy) → real names/roles/photos or none
- **No way to reach a human** → abandonment at problem moments →
  visible contact paths (WhatsApp for MENA)
- **Generic course UI as a default** (giant education hero, identical
  card grids, identical LMS dashboards, universal sidebar, purple/blue
  gradients, progress rings on every product, identical lesson players,
  identical mobile card stacks, unearned streaks) → reads as a template,
  not the current learning product → match family + platform in
  `industries/education.md`
- **One chrome for two jobs** (guest tools on a host home, rider map as
  the driver app, seller inventory on a shopper grid) → write two models
  or two apps (`ux/roles-surfaces.md`)
- **Inbox chrome on a file library or Drive chrome on a messenger** →
  match the primary object (`interface-families/` asset-library vs
  conversation-space vs work-queue)
