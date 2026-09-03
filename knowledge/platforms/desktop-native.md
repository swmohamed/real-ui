# Native Desktop: Windows and macOS

Use for installed Windows/macOS apps and desktop-class document, editor,
operations, utility, and media experiences. Combine with the relevant
framework file when one exists. A wide browser is not automatically a native
desktop app.

Labels: current Apple HIG and Microsoft Learn statements are PLATFORM
GUIDANCE; cross-platform conclusions are DESIGN PRINCIPLES.

## Model the window, document, and command system

Before drawing a shell, specify:

- window roles: primary, document, utility/inspector, modal, popover;
- single-window, multi-window, tabs, or document-based lifecycle;
- new/open/import/save/save-as/export/close/reopen/recovery behavior when
  files or durable artifacts exist;
- selection model and command targets;
- menus, toolbars/command bars, context menus, inspectors, status regions,
  and keyboard shortcuts by frequency and context;
- background/inactive behavior, notifications, system integration, and
  restoration after quit, update, crash, or device sleep.

Do not invent a document model because desktop apps often have one. If the
product is account/data based, model its actual durable objects and sync.

## Windows expression

- Design for a resizable app window and current window constraints; use
  platform navigation and layout options as candidates, not one shell.
- Integrate title-bar and system-window behavior deliberately. Preserve
  resize, maximize, snap, multi-monitor, text scaling, high contrast, and
  keyboard access.
- Place core frequent commands on or near the work surface; use command bars,
  menu bars, menus, or context menus for grouped and contextual commands.
- Expose commands across inputs. Right-click/hover, touch/pen, and keyboard
  accelerators supplement an input-agnostic command path.
- Use standard shortcuts and access keys where they exist; never repurpose a
  familiar shortcut for a different destructive action.

## macOS expression

- Support flexible windows: resize, move, show/hide appropriate regions,
  full screen, multiple displays, and restoration when the product needs it.
- Put the complete command vocabulary in the menu bar; toolbars and contextual
  controls accelerate frequent or selection-specific commands.
- Respect standard keyboard shortcuts and add discoverable app-specific
  shortcuts only for frequent actions. Support keyboard-only work and Full
  Keyboard Access.
- Treat precision pointer input, drag and drop, services/share, file
  management, and app activation/inactivation as platform capabilities—not
  automatic requirements for every app.
- Use system materials and control behavior in a way that survives appearance,
  accent, contrast, and accessibility settings; brand can shape expression
  without breaking platform behavior.

## Adaptive desktop behavior

Window size is live state. Define what happens at minimum, narrow, typical,
wide, and multi-monitor arrangements based on content stress:

- which pane remains primary; which inspector collapses, overlays, or moves;
- whether navigation changes representation;
- how selections and unsaved edits survive resize, tab detach, full screen,
  split view, display change, and relaunch;
- how keyboard focus and reading order move when panes recompose;
- how density changes without shrinking controls below platform/accessibility
  needs or stretching reading measures.

## Input and accessibility parity

Pointer precision can accelerate dense work, but hover and right-click are not
the only paths. Keyboard navigation, shortcuts, access keys where applicable,
screen-reader names/relationships, focus visibility, zoom/text scaling,
forced/high contrast, reduced motion, and touch/pen paths must survive.
Direct manipulation needs alternative commands; shortcut-only capability is a
failure.

## Platform divergence ledger

For a Windows + macOS product, record each difference as:

`shared product meaning → Windows expression → macOS expression → reason`

Share entities, terminology, capability, status semantics, provenance, and
brand roles. Allow window chrome, menu placement, command surfaces, shortcut
notation, system dialogs, typography metrics, materials, and navigation to be
native. “Pixel identical” is not a cross-platform success criterion.

## Finish gate

- [ ] window/document lifecycle and restoration are explicit
- [ ] command placement follows frequency, context, and selection—not a generic toolbar
- [ ] menus, contextual commands, and shortcuts use platform conventions without hiding capability
- [ ] minimum/narrow/wide/multi-window states preserve focus, selection, edits, and operation state
- [ ] mouse, keyboard, touch/pen where supported, and assistive technology have complete paths
- [ ] Windows/macOS differences are intentional and traced to native behavior

Connects: devices/desktop.md · input/mouse-keyboard.md ·
ux/{interaction-control,operations-recovery}.md · platforms/cross-platform.md ·
design-systems/cross-platform.md.
