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
| cross-platform.md | shared product language + native experience |

## Source labels used in these files

- `[OBSERVED]` — fetched from official docs or real product CSS (v2 research)
- `[PLATFORM RULE]` — official platform requirement (docs known, page blocked from this network)
- `[DESIGN PRINCIPLE]` — stable cross-source design knowledge
- `[RECOMMENDED]` — our synthesis for this skill

## Non-negotiables across ALL platforms

1. Never blindly copy WEB→MOBILE, ANDROID→iOS, iOS→ANDROID, MOBILE→DESKTOP.
   Same UX problem, different platform solution (see devices/, input/).
2. Platform DNA is not a costume: bottom sheets on web, hamburger on
   desktop, iOS switches in Android = each needs a reason.
3. Nav and layout switch by WINDOW SIZE CLASS, not by framework default
   breakpoints (responsive/adaptive-models.md).
4. Accessibility is per-platform native (accessibility/mobile.md), never
   an afterthought port.
