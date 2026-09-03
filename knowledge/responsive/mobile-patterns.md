# Responsive Mobile Patterns (derive from task and window)

Mobile may be the primary context, a companion, or an occasional channel.
Use project analytics/research when available; do not assert regional traffic
shares or force phone-first solely from industry or geography.

## Phone constraints to model

- dynamic viewport and browser/app chrome (`svh`/`dvh` where appropriate);
- safe areas, cutouts, system gestures, and sticky-layer occlusion;
- virtual keyboard, autofill, password managers, voice input, and zoom/text scaling;
- reach, handedness, posture, motion, interruption, offline/poor network, and battery;
- touch plus relevant screen-reader, switch, keyboard, pointer, and stylus input.

Use WCAG 2.2 AA 24×24 CSS px target-size rules correctly for web, then prefer
larger platform/product targets for frequent touch actions. Apple and Android
guidance are not interchangeable CSS standards.

## Transform by job, not page genre

| Job | Questions before choosing a pattern |
|---|---|
| Browse | What item minimum, media evidence, grouping, position memory, and comparison must survive? Grid, list, rail, map, or search-first are candidates. |
| Search | Is search an entry mode, persistent command, or destination? How do suggestions, keyboard, history, filters, zero results, and privacy behave? |
| Decide | Which evidence must remain adjacent: price, source, status, option, risk, availability, or comparison? A sticky action is valid only if it does not occlude content/focus. |
| Convert | Which steps and fields are truly required? Support locale-aware input, autofill, wallets when in scope, error recovery, review, interruption, and return. |
| Navigate | Choose bottom destinations, visible header, drawer, tabs, search-first, or contextual back/orientation from hierarchy, label fit, and platform. |
| Consume | Set measure, type, media, source/caption, and chrome from content and script; preserve reading position and accessibility controls. |
| Operate | Preserve comparison, selection, bulk scope, status, commands, and recovery. Do not automatically convert tables to disconnected cards or add a FAB. |

## Sheets, gestures, and feedback

- Use a sheet when its modality, detents, background relationship, dismissal,
  focus, keyboard, and back behavior match the platform/task. A sheet is not a
  generic substitute for every secondary screen.
- Swipe, drag, pull-to-refresh, long-press, and edge gestures are accelerators.
  Provide visible/input-parity alternatives and avoid conflicts with system
  navigation and assistive technology.
- Place toast/snackbar/banner feedback where it stays associated with the
  result and does not cover navigation, focus, keyboard, or critical status.
- Keep focused fields and validation visible with the keyboard open; preserve
  the draft through interruption, orientation, and class changes.

## Performance and continuity

Use current project performance targets and field/lab measurement; do not
turn one web-vitals threshold into a universal native-mobile rule. Reserve
space for media/type, prioritize critical content, acknowledge input promptly,
and distinguish pending from complete. Re-entry from deep link, notification,
background, or offline state must restore orientation and durable work.

## RTL and localization

Direction comes from semantic flow and platform behavior, not blanket
mirroring. Test mixed Arabic/Latin identifiers, numbers, search, system back,
carousels, steppers, charts, maps, keyboard, sheets, long real strings, and
font metrics. Keep LTR data bidi-isolated where required.

## Finish gate

- [ ] mobile priority is evidence-backed; desktop/tablet needs are not erased
- [ ] transformations preserve task relationships, comparison, source, and state
- [ ] keyboard/safe-area/sticky layers do not obscure focus or actions
- [ ] gesture and hover accelerators have complete alternatives
- [ ] offline, interruption, deep-link, long-content, text-scale, and RTL states survive
- [ ] patterns are justified by task/platform, not a generic mobile recipe

Connects: devices/mobile.md · ux/{mobile-states,interaction-control}.md ·
responsive/{adaptive-models,breakpoints-adaptation}.md · accessibility/mobile.md.
