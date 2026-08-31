# Patterns: Hero Sections (the catalog — pick by intent, not by trend)

Every hero = promise + proof-of-promise + next step. Format: Purpose /
Anatomy / Use when / Avoid when.

## 1. Statement hero (typographic)
Text promise (h1) + subline + CTA pair + product visual below/side
- **Use**: SaaS/B2B positioning pages (Linear/Stripe lineage)
- **Anatomy**: 56–72px display type desktop / 28–36 mobile, 2-line max,
  one accent word or none; ghost secondary CTA
- **Avoid when**: brand has no strong verbal promise (use media hero)

## 2. Product-shot hero
The actual interface (screenshot/video/browser-chrome frame) as hero,
often tilted/floating with depth shadows
- **Use**: tools with visual products (dashboards, editors)
- **Watch-outs**: real data in shots (lorem = credibility death); aspect
  boxes for CLS; video poster first paint

## 3. Search hero
Embedded search widget as THE hero (travel/marketplace/jobs/real estate)
- **Anatomy**: tab strip (product switchers) + grouped fields + CTA;
  below: trust strip or popular destinations
- **Use when**: >60% of traffic arrives with intent (paid/direct searchers)

## 4. Cinematic media hero
Full-bleed image/video with scrim + minimal caption + one CTA (or none)
- **Use**: luxury, hotels, automotive, entertainment, destinations
- **Rules**: LCP image ≤200KB effective; poster-first video; text contrast
  verified on busiest frame; height 70–100vh desktop / 60–80svh mobile
  (svh units — mobile URL-bar reality)

## 5. Poster/shelf hero (discovery)
Featured content carousel with autoplay rotation + manual controls
- **Use**: streaming, gaming portals, media front pages
- **Rules**: slide 1 must carry alone (assume 80% never see slide 2);
  height fits 1 row of content visible; pause control + reduced-motion
  static

## 6. Split hero (text + visual side-by-side)
Statement + media panel (illustration/product/UGC collage)
- **Use**: consumer apps, fintech onboarding pages (Monzo/Revolut class)
- **Watch-outs**: 5/7–7/5 asymmetric split beats 50/50; stacks mobile with
  media AFTER text (promise first)

## 7. Interactive/demo hero
Working product in the hero (playground, configurator, live calculator)
- **Use**: dev tools (try the API), calculators (fintech), configurators
- **Watch-outs**: works without login; degrades to GIF if heavy; ≤2s to
  first interaction

## 8. Editorial hero (content sites)
Lead story treatment: big headline + standfirst + image (news front pages)
- **Use**: publications, blogs, magazine fronts
- **Anatomy**: kicker + 32–44px headline + dek + byline/time + hero image
  with caption/credit

## 9. Hero-less routing (the honest non-hero)
Task grid / links-first above the fold (gov portals, utilities, intranets)
- **Use when**: efficiency IS the brand promise (GDS insight)

## Hero quality constraints (when a hero is justified)
- Keep one clear page h1; place it in the hero when that region carries the
  page's main subject. Use only actions supported by the page job; a routing
  or product-surface page may need several task links or no promotional CTA
- Avoid trapping the next required content below an oversized viewport-height
  composition; verify at short as well as tall viewports
- Text sizes clamp() responsive (no media-query jumps)
- RTL: split heroes mirror; scrims stay bottom; CTA icon flips
- Performance budget: hero LCP ≤2.5s on 4G mid-tier device or simplify

## Anti-pattern catalog
Giant gradient blobs + glass card + floating 3D + glow (AI-slop combo —
see anti-patterns); carousel of abstract stock; video walls on mobile
data; hero forms with 6+ fields; "Scroll to discover" mystery pages
