# Industry: Islamic Apps (Prayer, Quran, Ramadan, Hijri)

A PRIMARY MENA industry, not a niche. Evidence: v2 fetch 2025-08
`[OBSERVED]` — quran.com (gold standard), islamicfinder.org,
muslimpro.com.

Apply `industries/README.md`. First identify the subtype: Quran reader,
prayer-time utility, Hijri calendar, learning product, mosque service, or a
known combination. Patterns below are conditional and do not authorize extra
religious content, sensors, audio, accounts, notifications, or location use.

## Observed design languages

- Quran.com: **dedicated mushaf typography** — UthmanicHafs script for
  Quranic text + Kitab + Newsreader (serif reading) + Figtree (UI);
  768/1024 breakpoints `[OBSERVED]`. Role-split fonts = the whole
  design lesson: scripture ≠ UI text.
- IslamicFinder: Red Hat Display + Roboto + Noto Naskh Arabic fallback
  `[OBSERVED]` — utility-first scheduling face.
- MuslimPro: conventional utility app framing, WordPress-era site
  `[OBSERVED]`.

## Conditional domain patterns and questions

1. **When Quranic text is supplied**, treat it as a distinct sacred content class: dedicated script
   (Uthmanic/Amiri/Noto Naskh/Mushaf fonts), generous line-height,
   justify per mushaf tradition, ayah-end markers, surah headers as
   ornaments. NEVER generic sans for Quranic text.
2. **For a prayer-time utility where “next prayer” is the top task**, a
   prayer-times widget may become the primary surface
   content (next prayer countdown, not a dashboard) `[OBSERVED - all
   three leaders]`; location-first UX; times in BOTH Arabic-Indic and
   Latin digits option.
3. When the product uses dates, define its Hijri/Gregorian policy. A Ramadan
   mode or seasonal IA shift requires real seasonal capabilities/content.
4. If Qibla is in scope, treat it as a sensor experience with calibration
   states (device flat提示, magnetic interference warning), map fallback.
5. If recitation is in scope: player behavior may include a reciter picker, per-ayah repeat
   (learning loop), background play + lock-screen controls (mobile
   states — ux/mobile-states.md).
6. Calm, respectful motion; adhkar/dhikr counters (tap haptics);
   content accuracy trust (Quran text verified, translations credited
   — source attribution visible `[OBSERVED - quran.com credits]`).

## Candidate flows by subtype (scope required)

- Home = prayer card + next-prayer progress ring + hijri date + verse-
  of-day + quick tiles (quran/qibla/adhkar).
- Quran reader: surah list → reading view (mushaf page mode vs list
  mode `[OBSERVED - both exist on quran.com]`), tajweed coloring
  toggle, translation side-by-side, bookmark/last-read resume (state
  survival — mobile lifecycle).
- Prayer details: calculation method + juristic setting (these change
  times! — expose honestly), notifications per prayer (silent vs
  adhan modes), location management (travel mode).

## MENA/global notes

Arabic-first with English UI may serve a global ummah; Tajik/Urdu/French/
Indonesian translations are content, not just locale. Mosque finding and
dua/adhkar collections are separate capabilities, not genre defaults.
Establish imagery/ornament policy with the specific community,
scholarly/brand guidance, and audience research; do not impose one religious
interpretation as a universal UI rule.
