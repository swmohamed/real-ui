# Platform DNA: Web

Browser conventions are the platform. Web strengths: pointer precision,
hover as an information channel, URLs, keyboard workflows, unlimited
back (history), tabs, text selection, printing, deep-linking everything.

## Pointer-first design `[DESIGN PRINCIPLE]`

- Hover is a LEGAL state with a job: reveal affordances, previews,
  secondary actions, tooltips. Design hover for every interactive
  element — but NEVER put critical info or actions hover-only
  (touch devices exist; WCAG: content on hover must be dismissible/
  hoverable/persistent `[PLATFORM RULE - WCAG 2.x]`).
- Pointer precision → density is cheap: smaller targets (24px+),
  tighter lists, multi-column layouts, right-click context menus,
  drag-and-drop workflows.
- Cursor states matter (pointer/not-allowed/text/col-resize).

## URL thinking

- Every meaningful state deserves a URL (shareable, bookmarkable,
  SEO — seo/seo-aware-design.md). Modals that orphan content from
  URLs are desktop-app cosplay.
- Back button = platform navigation. Flows must survive back/refresh.

## Keyboard workflows

- Tab order = visual order; focus-visible is mandatory
  (accessibility/floor.md — corpus leaders ship focus-visible styles).
- Shortcuts for power surfaces (cmd+k search, j/k lists, esc closes).
- Forms: enter submits, labels clickable, autocomplete attributes.

## Layout & density norms (corpus-observed)

- Content max-width bands: 1120–1440px; wider = secondary rails.
- Breakpoint spine (v1 corpus OBSERVED): 640 / 768 / 1024 / 1280 —
  derive from layout needs, not framework defaults
  (responsive/breakpoints-adaptation.md).
- Desktop pages earn MORE information per viewport than mobile —
  squeezing mobile layouts up to desktop (giant touch cards) is a
  platform mismatch (redesign/diagnosis.md).
- Learning web vs mobile: comparison, packets, applications, and L&D
  admin earn desktop density; continue/download/live/scan earn the
  phone. Do not stack a catalog homepage and call it the app
  (`industries/education.md` mobile vs web).

## Web-specific states

- Loading: skeletons over spinners for content areas (ux/states.md).
- Empty/error states are real pages, not console text.
- Scroll-driven affordances (sticky headers, scroll-to-top, lazy media).

## Implementation context (semantics-first)

Semantic HTML landmarks (header/nav/main/footer), buttons-as-buttons,
CSS logical properties for RTL readiness (rtl/implementation.md —
corpus: modern leaders use logical props + `rtl:` variants), container
queries for component-level adaptation `[OBSERVED - corpus]`.

## Web QA

[ ] hover states designed + safe [ ] keyboard path works [ ] URL per
state [ ] back/refresh safe [ ] density right for pointer [ ] focus
visible [ ] semantic landmarks [ ] logical properties for RTL
