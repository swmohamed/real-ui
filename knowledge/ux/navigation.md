# UX: Navigation Systems

## The navigation decision tree

1. How many top-level destinations? **≤5** = tabs/pills; **6–9** = bar +
   More; **10+** = mega-menu or rail; **apps with sections** = left rail
2. Is content hierarchical trees (news, gov, retail) or flat tools (SaaS)?
   Trees → dropdowns/mega-menus; tools → persistent rails
3. Mobile-first? Bottom tabs (≤5) + hamburger for the long tail

## Header patterns (real-world canon)

- **Utility bar + main bar**: language/currency/support above; logo/nav/
   search/actions below (international/retail standard)
- **Logo left/start, actions right/end** (account, cart, search); search
  center when search-dominant (marketplaces)
- **Sticky behavior**: full sticky (SaaS 56% observed), sticky-on-scroll-up
  (content sites), transparent-over-hero → solid on scroll (entertainment)
- **Mega-menu discipline**: max 3 columns of grouped links + one featured
  promo with image; 20+ items per column = fail; open on click (not hover)
  with hover-intent bridging; full-width overlay with Esc/overlay close
- **Announcement bar** above header (promo/maintenance): dismissible,
  max-height one line, never stacks 3 banners (the enterprise-site disease)

## Mobile navigation canon

- Hamburger from left/start (drawer with sections + accordion sub-trees)
  OR bottom tabs — not both hiding the same links
- Bottom tab bar: 4–5 items, icon+label, active state clear, safe-area
  inset; the thumb zone owns it
- Section switchers as horizontal scroll chips (news sections, categories)
- "Back" must work: history-aware UIs, ←→ arrows in RTL

## Footer = the second navigation

- Real users scroll: contact, policies, sitemap links, language switch,
  newsletter, social; 4-col desktop → accordion mobile (standard)
- Trust furniture: certifications, payment methods, company info,
  copyright with year range

## Breadcrumbs, pagination, tabs

- Breadcrumbs: on hierarchical detail pages; first crumb linked, current
  not; schema.org markup
- Pagination: page numbers with current + neighbors, prev/next, count
  ("Page 2 of 34"); infinite-scroll hybrids keep footer reachable
- Tabs: same-page sibling content (not navigation to different pages);
  deep-linkable via hash/history; keyboard arrow navigation; lazy-load panels

## Wayfinding quality bar

- Current location always visible (active nav state, breadcrumbs, page h1)
- Maximum 3 clicks to any primary task (gov/retail standard)
- URLs readable by humans (/women/dresses/red, /ar/قسم/… transliterated
  or translated — pick translated for SEO)

## RTL navigation specifics

- Mirror everything EXCEPT: logos (usually), external-brand marks, media
  controls that imply time (play/rewind), number/graph axes
- Chevron/arrow direction flips (next = ← in RTL); use logical
  (start/end) icon semantics or CSS transforms via `[dir=rtl]`
- Hamburger opens from the right/start side; swipe-back gesture natural
  in RTL locales (system-level)

## Anti-patterns

- Hover-only menus (touch/kb lockout); unlabeled icon-only nav
- Mystery hamburger on desktop; carousel nav that fights scroll
- Nav that changes position between pages (cognitive reorientation cost)
- 3 stacked promo bars + cookie banner + chat bubble = death by chrome
  (common enterprise MENA portal failure — OBSERVED density on several)
