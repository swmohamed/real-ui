# Input: Stylus, Voice, Assistive

## Stylus (pen)

- Precision input: smaller targets become feasible BUT keep ≥44dp too
  (mixed finger+pen usage).
- Pressure/tilt matter for creation tools: line weight, shading —
  design brush/ink affordances honestly (creation products).
- Palm rejection expectation: full-canvas drawing areas are safe;
  resting hand never triggers UI.
- Handwriting surfaces: generous input boxes (line guides), recognition
  preview, corrections UX (tap-suggestion).
- Annotation layers (PDFs, screenshots): pen colors, highlighter mode,
  eraser + undo; gestures with pen-button variants.
- iPadOS + Android tablets + desktop pens: hover-preview (cursor shows
  pen tip preview) — progressive nicety.

## Voice

- Input mode (dictation): punctuation/formatting UX, correction flow,
  no-voice-emoji honesty; works in ANY text field, not just "voice
  features."
- Voice COMMANDS (assistants, in-app): command surface must be
  documented/discoverable; confirm-before-destructive; error recovery
  ("did you mean...?").
- Feedback: state visible (listening/thinking/speaking), cancelable,
  barge-in allowed (interrupt playback).
- Voice output (screen readers, assistants): content structured so it
  reads sanely — labels before values, groups announced together
  (accessibility/mobile.md).

## Assistive input technologies

- Switch access (single/multi-switch scanning): linear navigation
  order matters; scan groups; adjustable timing — design logical
  focus order (accessibility/floor.md + mobile.md).
- Keyboard-only (motor): everything reachable, no pointer-only traps —
  mouse-keyboard.md.
- Screen readers (VoiceOver/TalkBack/NVDA): semantics first
  (accessibility/mobile.md).
- Reduce motion / high contrast: accessibility/contrast-motion.md.

## Rule

Input modes are additive lenses, not separate products: one design
that works across touch/pointer/keyboard/voice with progressive
enhancement, never modal lockout ("voice-only setup steps" etc.).
