# Patterns: Headers & Navigation Systems (section-level reference)

Quick-reference catalog. Component anatomy lives in `ui/components.md`;
page placement in `pages/*`. Format: Purpose / Use when / Anatomy /
Watch-outs.

## 1. Classic marketing header
- **Purpose**: persistent identity + top-level routing + CTA
- **Use**: SaaS, B2B, portfolios, docs (Stripe/Linear/Vercel class OBSERVED)
- **Anatomy**: logo start · links (Product/Solutions/Resources/Pricing) ·
  Sign in + primary CTA end · 64px sticky
- **Watch-outs**: >7 top items collapses into "More"; CTA always visible
  mobile (condensed bar + hamburger)

## 2. Utility + main double bar
- **Purpose**: international operations (language, currency, support)
- **Use**: travel, retail, banking, gov (Booking/Emirates NBD class)
- **Anatomy**: 32–40px utility bar (lang/currency/hours) + 64–72px main bar
- **Watch-outs**: utility links must work at 320px (collapse to menu);
  never hide language switching in footer

## 3. Mega-menu overlay
- **Purpose**: deep trees (100s of destinations) with context imagery
- **Use**: marketplaces, news, enterprises (GitHub/Amazon class)
- **Anatomy**: full-width panel, 2–4 grouped columns + featured card;
  click/hover-intent open, Esc + overlay close
- **Watch-outs**: keyboard nav through groups; images lazy; mobile becomes
  accordion drawer (never a shrunken mega-menu)

## 4. Center-search masthead
- **Purpose**: search-dominant products
- **Use**: marketplaces, real estate, jobs, reference
- **Anatomy**: logo · search 40–60% width · actions end; suggestions
  dropdown with grouped types
- **Watch-outs**: search focus ring visible; mobile: search icon expands
  full-screen sheet with instant focus

## 5. Transparent-over-hero header
- **Purpose**: cinematic first impressions
- **Use**: streaming, luxury, automotive, hotels
- **Anatomy**: absolute-positioned white text over hero; solidifies on
  scroll (class swap + scrim)
- **Watch-outs**: contrast at the transparent state (verify worst frame);
  logo variant switch light→dark

## 6. Bottom tab bar (mobile)
- 4–5 icon+label tabs, active state clear, safe-area padding; always pair
  with a "More" drawer for the long tail. Standard across app-like webs
  (commerce, delivery, social OBSERVED).

## 7. Section sub-nav / sticky tabs
- **Purpose**: sibling sections without page jumps (news sections,
  dashboard tabs)
- Horizontal chip rail, sticky under main header (headers stack ≤2),
  scroll-snap + active-section tracking (IntersectionObserver)

## 8. Breadcrumb bar
- Detail pages under trees; links + current page (not linked); ≤4 levels
  visible (ellipsis for deep); schema BreadcrumbList markup

## RTL header adaptations
- Mirror all positions; chevrons/carets flip; hamburger opens end-side
  drawer; search icon+input dir="auto"; logo commonly stays unmirrored
  (brand mark) but positions to the start (right) — follow brand system

## Cross-cutting rules
- One sticky system per page (header OR header+subnav stacking — max 2)
- Height budget: ≤120px desktop sticky, ≤104px mobile sticky (content
  wins); announcement bars dismissible and don't reappear per page
- Focus management: skip-to-content first tab stop; Esc closes any overlay
- Performance: headers render before anything else (inline critical CSS);
  no images above 30KB in headers
