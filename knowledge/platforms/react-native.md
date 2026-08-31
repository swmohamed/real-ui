# Platform DNA: React Native

Sources: react/react-native-website official docs source, fetched
2025-08 `[OBSERVED]` (accessibility.md, intro-react-native-components.md,
platform-specific-code.md, keyboard.md, keyboardavoidingview.md,
pressable.md, optimizing-flatlist-configuration.md).

## RN is a cross-platform IMPLEMENTATION model — not "React for mobile"

You write one product; Android and iOS still behave differently
(system back, gestures, sheets, haptics, status bars). Design for the
native behaviors, implement once where possible, diverge where the
platforms do.

## Core components ≠ web tags `[OBSERVED]`

`<View> <Text> <Image> <ScrollView> <TextInput>` — no divs/spans; Text
must wrap every string (nested Text for rich runs). Design consequence:
text styling is component-level, not document flow; think in boxes.

## Platform-specific divergence `[OBSERVED - platform-specific-code]`

- `Platform.OS` / `Platform.select({ios, android})` is the official
  pattern. LEGITIMATE divergences: back handling (Android hardware/
  gesture back must work `[PLATFORM RULE]`), translucent status bars,
  shadows (iOS shadow vs Android elevation), haptics, share sheets.
- Illegitimate: shipping two different visual languages "because
  platform file exists" — brand tokens stay shared
  (design-systems/cross-platform.md).

## Keyboard behavior `[OBSERVED - keyboard docs]`

- `softwareKeyboardLayout`/windowSoftInputMode differ per OS;
  KeyboardAvoidingView exists because each OS shifts layout differently
  (iOS pushes views, Android usually resizes window) `[OBSERVED]`.
- Design rules: inputs visible above keyboard; submit/dismiss reachable;
  keyboard won't cover the error state; test scroll-to-input.
  (devices/mobile.md keyboard states.)

## Pressable & touch `[OBSERVED - pressable docs]`

Pressable replaces Touchables; feedback states (pressed/hovered/
focused/disabled) are built-in — design all four, not just pressed.
Touch targets ≥44/48dp regardless of visual size (hitSlop extends).

## Lists & performance-aware UI `[OBSERVED - optimizing flatlist]`

FlatList props that shape UX: windowing (`windowSize`, `initialNumToRender`),
`getItemLayout` for instant scroll-to, stable keys, `keyExtractor`.
Design consequence: infinite lists must keep scroll position stable,
jump-to-section fast, and never flash placeholders on back-navigation.
Virtualization also limits exotic item layouts — design list items that
render cheap.

## Safe areas & notches

react-native-safe-area-context is the community standard for insets
`[DESIGN PRINCIPLE]`; safe-area padding is layout input everywhere
(devices/mobile.md).

## Accessibility `[OBSERVED - accessibility docs]`

Props: `accessibilityLabel`, `accessibilityRole`/`accessibilityValue`,
`accessibilityState`, `accessibilityHint`, `accessibilityLiveRegion`
(Android), groups/actions. Design rule: every icon-button has a label;
state changes announced deliberately, not chattily
(accessibility/mobile.md).

## RN QA

[ ] Android back works [ ] keyboard flows tested both OS [ ] press/
hover/focus/disabled states [ ] targets ≥44/48dp [ ] list perf props
set [ ] safe areas respected [ ] a11y props on interactive elements
[ ] one brand system, native behaviors per platform
