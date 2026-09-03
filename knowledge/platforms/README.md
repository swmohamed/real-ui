# Platforms (index + ground rules)

Shared UI/UX knowledge lives in ui/, ux/, patterns/, foundations/ —
NOT duplicated here. Each platform file explains:

GENERAL DESIGN PRINCIPLE → PLATFORM-SPECIFIC ADAPTATION →
IMPLEMENTATION CONTEXT (widget/component names as context, not as the
goal — this skill is design-first, code-aware).

## File map

| File | Covers |
|---|---|
| web.md | browser DNA: pointer, hover, URLs, keyboard, density |
| flutter.md | Material 3 vs Cupertino vs custom, adaptive, tokens |
| react-native.md | RN as cross-platform model, native behavior diffs |
| swiftui.md | Apple platform conventions (declarative) |
| uikit.md | Apple platform conventions (imperative foundation) |
| jetpack-compose.md | Android declarative UI, canonical adaptive layouts |
| android.md | Android DNA: Material, back, system bars, large screens |
| desktop-native.md | Windows/macOS window, document, command, input, and platform-divergence contracts |
| cross-platform.md | shared product language + native experience |

## Source labels used in these files

- `[SOURCE-OBSERVED]` — present in fetched official docs or real product source
- `[RUNTIME-OBSERVED]` / `[RENDER-OBSERVED]` — exercised or visually
  inspected in a named state; absent unless explicitly recorded
- Legacy `[OBSERVED]` — SOURCE-OBSERVED unless a runtime/render state is named
- `[PLATFORM RULE]` — requirement supported by a cited current official source
- `[DESIGN PRINCIPLE]` — stable cross-source design knowledge
- `[RECOMMENDED]` — our synthesis for this skill

## Non-negotiables across ALL platforms

1. Never blindly copy WEB→MOBILE, ANDROID→iOS, iOS→ANDROID, MOBILE→DESKTOP.
   Same UX problem, different platform solution (see devices/, input/).
2. Platform DNA is not a costume: bottom sheets on web, hamburger on
   desktop, iOS switches in Android = each needs a reason.
3. Native window classes inform nav/layout where the platform defines them;
   web breakpoints come from content stress, not framework defaults
   (responsive/adaptive-models.md).
4. Accessibility is per-platform native (accessibility/mobile.md), never
   an afterthought port.
