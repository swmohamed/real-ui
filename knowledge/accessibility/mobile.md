# Accessibility: Mobile & Screen Readers (VoiceOver, TalkBack, Dynamic Type)

Extends accessibility/floor.md (web floor) to native mobile + screen
readers. Labels: `APPLE OFFICIAL` (Apple DocC/WWDC recovered 2026-08) ·
`[OBSERVED - RN docs]` · `[PLATFORM RULE]` (OS requirement) ·
`[DESIGN PRINCIPLE]` (stable practice).

## Screen reader model (design consequence first)

Screen readers narrate a SEMANTIC TREE, not pixels. Your design job:
make the tree make sense.

- Every interactive element: label (+ role/value/state where custom).
  Icon buttons without labels = #1 violation. RN props:
  accessibilityLabel/Role/State/Value `[OBSERVED - RN docs]`.
- Group related elements (list row = one element with children hidden
  or summarized): iOS accessibilityElement(children:), Compose
  semantics(mergeDescendants) `[DESIGN PRINCIPLE]`.
- Order = logical reading order (usually visual order); custom sort
  only with reason.
- Announcements: changes announced deliberately
  (Android liveRegion/AndroidAnnouncement, UIAccessibility.post) —
  not chattily on every update.
- Custom actions on complex controls (rotors/actions) instead of
  burying actions inside gestures.
- Hints sparingly; labels never redundant with visible text.

## VoiceOver (iOS specifics) `[APPLE OFFICIAL anchors]`

Official vocabulary (WWDC23 "Build accessible apps with SwiftUI and
UIKit", transcript fetched 2026-08): VoiceOver interacts through
accessibility TRAITS and ACTIONS — refine with them `[APPLE OFFICIAL]`.
Rotor navigation (headings/links) — expose heading levels in custom
text; adjustable values (sliders) respond to swipe-up/down; container
labels for tab bars/regions; focus order follows accessibilityFrame
layout. Drag-and-drop needs accessible alternatives `[DESIGN PRINCIPLE]`.

## TalkBack (Android specifics)

- Content descriptions (contentDescription); decorative images
  null-marked; headings/paragraph semantics set.
- Touch exploration: user drags finger to HEAR what's under it —
  spacing between targets is auditory too; merged row semantics.
- Toasts announce (live region) — snackbar with action = good pattern.
- Labels tied to inputs (labelFor) `[PLATFORM RULE]`.

## Dynamic Type / text scaling `[APPLE OFFICIAL + PLATFORM RULE]`

- iOS official APIs: `dynamicTypeSize(_:)` "sets the Dynamic Type size
  within the view"; `UIFontMetrics` "obtaining custom fonts that scale
  to support Dynamic Type" `[APPLE OFFICIAL - DocC]`. Support Dynamic
  Type through accessibility sizes; test at XXL/accessibility sizes —
  truncation plan per text class (wrap/shrink-lineheight/not-clamp).
- Android: user font scale to 200% (sp units); display-size scaling;
  test reflow, not clipping.
- Web: text-scaling/zoom must not break layout (floor.md).
- NEVER disable system text scaling globally; per-surface clamps only
  with reflow alternative (Apple allows clamp + separate full view).

## Targets & motor (cross-ref)

Prefer generous hit regions: Apple HIG generally recommends 44×44pt (its
accessibility page distinguishes a 44×44pt default from 28×28pt minimum), and
Android recommends 48×48dp. WCAG 2.2 AA target-size is 24×24 CSS px on web or
an allowed exception; switch-access order stays logical
(input/stylus-voice.md).

## Mobile a11y QA

[ ] all icon-buttons labeled [ ] rows merged sanely [ ] order logical
[ ] Dynamic Type to max tested [ ] VoiceOver pass on key flows
[ ] TalkBack pass on key flows [ ] announcements deliberate
[ ] decorative images silent [ ] inputs with labels

Learning apps: expose captions/transcripts for lesson audio/video; do not
announce every XP tick; camera/mic features need labeled controls and a
non-camera path (`industries/education.md`).
