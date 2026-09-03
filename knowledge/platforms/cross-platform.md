# Cross-Platform Products (shared meaning, native expression)

Aim for recognizable product continuity and platform-appropriate behavior,
not pixel identity or a fixed “web/iOS/Android” mapping table.

## Share the product contract

Keep entities, terminology, capability, permission, authority, provenance,
state meanings, outcome, and brand roles coherent. Task coverage should not
silently disappear, but priority, grouping, navigation, density, and command
placement may differ by device context and platform convention.

Token names and semantic roles can be shared. Literal typography metrics,
control dimensions, materials, shadows, motion, window chrome, and component
APIs may need platform mappings. “Card,” “sheet,” or “back” must not be assumed
to mean the same implementation everywhere.

## Derive each platform expression

For every major task/component record:

`shared meaning → web expression → iOS/iPadOS expression → Android expression → Windows/macOS expression → reason`

Evaluate:

- navigation hierarchy, browser/system back, deep links, tabs/windows/scenes;
- command frequency, selection, menus/toolbars/context, keyboard/hover/touch/pen;
- platform control behavior, safe/system areas, permissions, share/file flows;
- compact/expanded/resizable window adaptation and multi-window continuity;
- accessibility settings, screen readers, text scaling, contrast, motion, input;
- offline/sync/background/notification behavior and state restoration.

Use the applicable official platform file; platform components are candidates,
not mandatory branding. A bottom bar, rail, FAB, sheet, sidebar, or menu exists
only when hierarchy and native behavior support it.

## Continuity versus divergence

Continuity comes from product vocabulary, capabilities, data/status semantics,
content register, identity signals, and recovery—not identical coordinates.
Divergence is healthy when it follows native windowing, command, input, back,
permission, or accessibility behavior. Record any capability difference as
intentional product scope, not an unnoticed porting loss.

## Traveler test

A person switching platforms should recognize the product, find equivalent
outcomes, understand shared state, and trust status/source meanings. They
should not need to unlearn their operating system. Test real task paths rather
than comparing screenshots alone.

## Failure modes

- web squeezed into phone or desktop web relabeled as a native app;
- Android controls/back on Apple or Apple chrome on Android without a reason;
- identical navigation at incompatible window/input classes;
- shortcuts, hover, gestures, or context menus as the only capability path;
- tokens shared literally until text, targets, or native controls break;
- brand drift so large that status/action semantics feel like another product;
- scope loss hidden behind “platform simplification.”

Connects: platforms/{README,desktop-native}.md ·
design-systems/cross-platform.md · devices/* · accessibility/mobile.md.
