# Accessibility: The Design Floor (non-negotiable)

V2 extensions: mobile/screen readers → accessibility/mobile.md ·
motion/contrast/color-independence → accessibility/contrast-motion.md
(now with official WCAG 2.2 criteria — recovered from W3C source repo).

Design a11y IN, not audits later. Corpus median is mediocre (main 57%,
focus-visible 55%) — match the leaders.

## Semantics (the free 80%)

- Landmarks every page: `<header> <nav> <main> <footer>` (+aside);
  ONE `<main>`; skip-link to it as first tab stop
- Headings communicate document structure and support in-page navigation.
  Use a clear top-level heading and nested ranks that reflect sections;
  avoid confusing upward gaps where possible, while recognizing that closing
  a subsection can legitimately return from a deeper rank. WCAG does not
  require exactly one `h1`; do not present a corpus tendency as conformance
- Native elements first: button (not div onClick), a with href (not
  JS-span), label+input pairs, fieldset/legend for groups, table for
  data
- Lists as lists (nav = ul of links); alt text per media rules (ui/media)

## Keyboard (the power-user contract)

- Tab order = visual/logical order; no positive tabindex
- Everything operable: focusable where the native control/widget pattern
  requires it, with a clearly visible `:focus-visible` indicator on every
  surface. A 2px ring may be a useful system token, but WCAG conformance is
  about visibility and the applicable criterion—not one prescribed style
- Skip links; Esc closes overlays; focus returns to trigger; modals trap
  focus; arrow-keys in menus/tabs/carousels; Enter/Space activate
- No keyboard traps (including cookie banners with hidden focuses)
- Custom widgets follow WAI-ARIA patterns (combobox, disclosure, tabs) —
  start from the applicable APG pattern, then verify its roles, states,
  keyboard behavior, focus movement, and fit for this context. APG examples
  are reference implementations, not text to copy blindly

## Forms

- Label EVERY field (visible, above); placeholder = example only
- Errors: text + icon near field, `aria-describedby`, and an error summary on
  submit when the flow benefits. Announce asynchronous changes with the least
  intrusive live-region behavior that makes them perceivable; do not put all
  changing content in `aria-live`
- Required marked in label/aria-required; instructions BEFORE fields
  (screen readers read ahead); timeouts warn + extendable

## Color & contrast

- Apply the relevant WCAG contrast criteria: 4.5:1 normal text, 3:1 large
  text, and 3:1 for the visual information required to identify UI components
  and states at AA. Enhanced contrast is a contextual target, not an AA rule
- Never color-only meaning (errors, statuses, links in text)
- Text over images: scrims + worst-frame verification; no text-in-image
  for content

## Pointer and touch targets

- Web WCAG 2.2 AA (2.5.8): target is at least 24×24 CSS px, or passes an
  allowed spacing/equivalent/inline/user-agent/essential exception. This is
  the conformance minimum, not the preferred product target
- Prefer approximately 44×44 CSS px for frequent touch controls; platform
  guidance may be stronger (Apple generally recommends a 44×44pt hit region;
  Android recommends 48×48dp). Visual bounds may be smaller when hit area and
  separation remain safe
- Zoom allowed (never maximum-scale=1 — OBSERVED violation on 17/156 corpus
  the anti-checklist)
- WCAG 2.2 AA that change structure (full table in contrast-motion.md):
  2.4.11 focused item not fully covered by sticky chrome; 2.5.7 drag needs a
  non-drag path; 3.2.6 help in a consistent order; 3.3.7 do not re-ask info
  already given; 3.3.8 auth without a cognitive puzzle when avoidable.

## Motion & vestibular

- prefers-reduced-motion honored (see motion/principles.md); no
  autoplaying motion text (marquees); parallax optional-off

## Screen-reader essentials (test with NVDA/VoiceOver)

- alt taxonomy (informative/decorative/functional); aria-label on
  icon-buttons; aria-expanded on disclosures; page title per route;
  language switches announce (lang attr changes); live regions for
  toasts/cart updates
- Tables: real th scope; charts: text alternatives (data table or
  summary); complex widgets: APG patterns

## PDFs & documents

- HTML-first; PDFs only for print-archive; tagged PDFs if shipped

## RTL/a11y intersection

- Focus ring + outline direction on RTL layouts (inline-start borders);
  skip-link text localized; screen readers announce Arabic properly with
  lang="ar" set; mixed-language content tagged (lang on spans) for
  correct voice synthesis
- Learning media: captions and transcripts when lessons are audio/video;
  keyboard-operable playback when a player exists; quiz status not
  color-only; progress has text/semantics, not only rings
  (`industries/education.md`). Mixed Arabic/English technical lessons
  (code, equations, course codes) keep Latin/math LTR inside RTL chrome.

## Testing ritual (ship gate)

1. Keyboard-only pass (tab/enter/esc/arrows)
2. VoiceOver or NVDA pass on key flows
3. Contrast audit (automated + manual on brand pairs)
4. Resize text to 200% (WCAG 1.4.4) without lost content/functionality
5. Reflow at a 320 CSS px viewport equivalent (commonly 1280px at 400%
   browser zoom): no two-dimensional scrolling except content that genuinely
   requires it, such as maps or data tables (WCAG 1.4.10)
6. Reduced-motion check
7. axe/Lighthouse — zero criticals, issues triaged not ignored
