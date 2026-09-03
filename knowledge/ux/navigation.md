# UX: Navigation Systems

## The navigation decision tree

1. Identify destinations from entities and top tasks; do not invent or merge
   them to fit a preferred component.
2. Evaluate task frequency, hierarchy depth, scope switching, label length,
   available width, platform convention, input method, and role/permission.
   Destination count is a constraint, not a component selector.
3. Choose among persistent bars/rails, tabs, drawers, menus, breadcrumbs,
   search, and in-context links by the jobs they serve. Test the chosen set
   with real labels, restricted roles, localization, text scaling, and window
   classes.
4. On adaptive products, preserve destination identity and user orientation
   when the container changes; a phone pattern is not a desktop rule shrunk.

## Header patterns (real-world canon)

- **Utility bar + main bar**: language/currency/support above; logo/nav/
   search/actions below (international/retail standard)
- **Logo left/start, actions right/end** (account, cart, search); search
  center when search-dominant (marketplaces)
- **Sticky behavior**: full sticky (SaaS 56% observed), sticky-on-scroll-up
  (content sites), transparent-over-hero → solid on scroll (entertainment)
- **Mega-menu discipline**: group by user-recognizable concepts, keep scanning
  load bounded, and include promotional material only when it does not obscure
  navigation. Opening and closing must work for pointer, keyboard, and touch;
  support Escape, focus return, and hover-intent where hover is additive.
- **Announcement bar** above header (promo/maintenance): dismissible,
  max-height one line, never stacks 3 banners (the enterprise-site disease)

## Mobile navigation canon

- Hamburger from left/start (drawer with sections + accordion sub-trees)
  OR bottom tabs — not both hiding the same links
- Bottom tab bar: use for a small, stable set of frequent peer destinations
  that fit with localized labels; icon+label, clear active state, safe-area
  inset, and platform-appropriate touch targets
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
- Primary tasks have short, predictable, and testable paths; evaluate task
  completion, disorientation, and recovery rather than enforcing a universal
  click count
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
- Navigation selected from destination count alone, without real labels,
  hierarchy, role, input, localization, or window-class testing
