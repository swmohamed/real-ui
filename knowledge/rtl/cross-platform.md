# RTL Cross-Platform (beyond web)

Extends rtl/implementation.md (web) to Flutter, Android, Compose,
React Native, iOS/SwiftUI. Web evidence is corpus-OBSERVED; platform
APIs below are `[PLATFORM RULE]` (official) with stable-docs caveat in
research/reports/v2-research-log.md.

## Core principle: directional vs semantic elements

Mirror DIRECTIONAL elements (layout order, chevrons/arrows of
progress, breadcrumbs, indentation, carousels' reading direction).
Do NOT mirror SEMANTIC elements:
- Media controls (⏮️▶️⏭️ stay LTR — playback direction is universal)
- Clocks, gauges, progress FILL direction can mirror but numeric
  meters usually stay
- Latin-script logos/wordmarks, phone numbers, code, Latin brand marks
- Charts: axes usually mirror (time flows right→left in RTL
  expectations vary) — FOLLOW REGIONAL CONVENTION, test with Arabic
  users; commonly: horizontal bar charts mirror, line charts' x-axis
  may stay LTR for time-series with Arabic labels
- Maps: geography doesn't mirror (qibla/compass apps prove direction
  correctness matters religiously-critically here)
- Numbers: Latin digits are common in UIs (Egypt/Levant default to
  Latin digits in products; Arabic-Indic ٤٥٦ in some Gulf contexts) —
  match product language, keep numerals consistent —
  rtl/arabic-ux.md + typography/arabic-typography.md.

## Platform APIs `[PLATFORM RULE]`

| Platform | Mechanism |
|---|---|
| Flutter | Directionality widget + Localizations/rtl; logical widgets (EdgeInsetsDirectional, Align(alignmentDirectional)); icons: use matchTextDirection where directional |
| Android Views | android:supportsRtl="true"; start/end instead of left/right (paddingStart, layout_marginEnd, layout_toStartOf) |
| Jetpack Compose | CompositionLocalProvider(LocalLayoutDirection) + LayoutDirection.Rtl; components mostly auto-mirror with correct direction setup |
| React Native | I18nManager.forceRTL/isRTL + community rtl libs; flexbox row direction flips with dir; transforms manual for icons |
| iOS UIKit | `semanticContentAttribute` — "a semantic description of the view's contents, used to determine whether the view should be flipped when switching between left-to-right and right-to-left layouts" `[APPLE OFFICIAL - DocC]`; `.playback` case = "a view representing the playback controls, such as Play, Rewind, or Fast Forward buttons or playhead scrubbers" `[APPLE OFFICIAL]` — the official mechanism for media controls NOT mirroring |
| SwiftUI | `LayoutDirection` — "a direction in which SwiftUI can lay out content" `[APPLE OFFICIAL - DocC]` (environment layoutDirection); flipsForRightToLeftLayoutDirection on views `[PLATFORM RULE - UIKit API]` |

## Mixed Arabic/English (the everyday MENA reality)

- Bidi text: embed English/numbers inside Arabic correctly (bidi
  isolate/markup — Unicode LRM/RLM; first-strong paragraph direction).
- Mixed UI: primary dir from product language; secondary-language
  content aligns within its own run (don't force-align English labels
  right-edge-glued inside RTL paragraphs).
- Search: Arabic normalization (alef variants, taa marbuta, diacritics)
  affects search/find UX `[DESIGN PRINCIPLE - MENA products]`.
- Dates: Hijri + Gregorian side by side (islamic-apps.md); currency:
  locale format (﷼, د.إ, EGP) with stable symbol placement per locale.

## Icons in RTL `[DESIGN PRINCIPLE]`

Mirror: back chevrons, forward/next, send (airplane→ may mirror),
indent, list-reorder handles, progress arrows, tutorial diagrams.
Never mirror: media playback, refresh/circular, brand marks, clocks,
volume/speaker glyphs (speaker + waves asymmetric — platform-stable),
thumbs-up/like (platform convention: usually NOT mirrored), shopping
cart (usually not), physical-world metaphors (globe, camera).

## Cross-platform RTL QA

[ ] direction set at root per platform API [ ] layout mirrors, content
logical [ ] directional vs semantic icons audited [ ] mixed bidi text
renders clean [ ] numbers/dates/currency per locale policy [ ] charts
follow regional convention [ ] maps/compass correct (qibla!)
[ ] LTR media controls stay [ ] deep-linked screens re-set direction
