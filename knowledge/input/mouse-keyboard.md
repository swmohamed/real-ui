# Input: Mouse, Keyboard, Trackpad

Pointer+keyboard users: precise, fast, keyboard-loyal. Density and
shortcuts are respect, not clutter.

## Mouse

- Hover is an information channel (web.md): tooltips (with delay +
  dismiss/hover-safe), previews, secondary action reveal, inline edit
  hints. Critical actions stay visible without hover.
- Pointer precision permits smaller acquisition targets than touch in some
  contexts, but density still depends on platform guidance, accessibility,
  content, consequence, expertise, and mixed-input support. Tooltips do not
  rescue mystery controls or provide a touch path.
- Context menus (right-click) for object-level actions on power
  surfaces; cursor states per affordance (pointer, not-allowed, text,
  grab, col-resize, wait).
- Drag-and-drop: visible handles or whole-object draggable affordance,
  drop targets glow, escape cancels; always a non-drag alternative.

## Trackpad (laptop-first reality)

- Natural-scroll respect (system setting); momentum scroll smooth.
- Two-finger gestures count as pointer input (pinch zoom, back/forward
  swipes on web) — don't hijack without reason.
- Large invisible scroll-capture surfaces (maps, carousels) trap
  scrolling: provide escape (close/map collapse) — classic trap bug.

## Keyboard (the speed surface)

- Tab order = logical/visual order; focus-visible mandatory
  (accessibility/floor.md — corpus leaders style focus-visible).
- Respect standard platform/widget key behavior. Add discoverable shortcuts
  for frequent product actions without repurposing familiar combinations or
  making shortcuts/command palettes the only path.
- Focus traps in modals (with release); focus returns on close;
  skip-to-content on pages.
- Forms: label click focuses, enter submits, autocomplete attrs,
  error summary + per-field anchor `[PLATFORM RULE - WCAG-derived]`.

## Pointer+keyboard QA

[ ] hover designed + safe [ ] tab order sane [ ] focus visible [ ]
shortcuts for power actions [ ] esc/enter contracts [ ] context menus
on object surfaces [ ] drag has alternatives [ ] scroll traps none
