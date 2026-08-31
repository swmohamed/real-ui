# V4 Independent Audit, Repair, and Validation Log

Date: 2026-08-31. This log is the repository-side evidence record for the
independent audit. It preserves earlier V1–V3 reports as historical provenance
but does not inherit their PASS claims.

## Audit manifest

### Deeply inspected

- `SKILL.md`, `README.md`, taxonomy, retrieval/activation map, and runtime
  workflow.
- All 119 Markdown knowledge files across 25 directories, including every
  industry and page module, foundations, UX, redesign, platform, responsive,
  accessibility, localization/RTL, content, implementation, and research
  method/claims.
- All test Markdown, Python research tools, installer, verifier, repository
  history/diff, ignore rules, 18 initially installed copies, and the 19 final
  detected skill destinations (including LM Studio after synchronization).
- JSON report schema and aggregate behavior; corpus-wide values were recomputed
  from the report set with corrected site-prevalence logic.

### Partially inspected

- Large JSON/raw research artifacts were schema-checked, sampled, and processed
  by the aggregation tools; they were not manually read byte-for-byte.
- Historical reports were read for claims/provenance, not re-performed in full.

### Unverified

- Generated-agent behavior, browser/native runtime behavior, and rendered UI
  output: no isolated agent execution/render harness exists in the repository.
- Tailwind prevalence after detector repair: existing reports store outputs
  from the old overbroad heuristic and source HTML was not retained for an
  offline re-analysis.

## Initial issue registry and disposition

| ID | Severity | Issue / observed evidence | Root cause | Affected behavior | Repair and test | Status |
|---|---|---|---|---|---|---|
| C-01 | CRITICAL | Industry selector offered an “industry default” DNA; homepage/landing/PDP used universal or proven fixed sequences; dashboard assumed rail/KPIs/cards | page/industry catalogs had architectural authority before product/content modeling | industry→template, repeated silhouettes, generic dashboards | added page/industry authority contracts, model/screen-contract precedence, removed fixed headings/sequences; executable route/phrase tests | FIXED + STATICALLY VERIFIED |
| C-02 | CRITICAL | Scope firewall lived mainly in redesign while page/industry files freely named accounts, ads, subscriptions, reviews, chat, alerts, payments, etc. | genre knowledge doubled as requirements | silent feature/business-model invention | all-design KNOWN/REQUESTED/NECESSARY/HYPOTHESIS/OUT-OF-SCOPE ledger; catalog contracts; conditionalized high-risk page and four newer industry modules; scope finish gate | FIXED + STATICALLY VERIFIED; generated behavior UNVERIFIED |
| H-01 | HIGH | breakpoint “site count” summed declaration counts; impossible thousands were described as sites | aggregation mixed declaration frequency with site prevalence | false 90%/universal breakpoint spine | shared per-site prevalence helper, corrected 768=91/145 and 1024=63/145, rewrote responsive claims, executable fixture and report-consistency tests | FIXED + VERIFIED |
| H-02 | HIGH | Tailwind detector matched generic `flex`/`grid`; 90/145 became an adoption claim | low-specificity framework regex | misleading implementation recommendation | detector now requires distinctive variant/arbitrary grammar; removed adoption claim and marked prevalence UNVERIFIED; false-positive test | FIXED + VERIFIED; prevalence intentionally unresolved |
| H-03 | HIGH | legacy OBSERVED label implied source presence proved rendered behavior; research method claimed conversion priority/above-fold from source | evidence modes were collapsed | overconfident UI/behavior claims | SOURCE/RUNTIME/RENDER evidence modes, source-limit metadata, same-origin CSS source list, modern MQ syntax, HTML rejection | FIXED + STATICALLY VERIFIED |
| H-04 | HIGH | web target floor called 44×44 “WCAG 2.2”; 200% zoom was used as Reflow test; Focus Appearance level omitted; popovers/menus trapped focus | standards and platform guidance conflated | incorrect accessibility audits/implementations | corrected WCAG 2.5.8 AA, 1.4.10, 1.4.4, 2.4.13 AAA, APG focus behavior, Apple/Android guidance split; executable assertions | FIXED + VERIFIED AGAINST OFFICIAL SOURCES |
| H-05 | HIGH | Android exposed only three width classes; RN Pressable claimed four built-in style states; Apple HIG status/guidance stale | platform files froze earlier documentation | wrong adaptive thresholds/API designs | five Android width classes + height/dynamic semantics; RN `{pressed}` wording; Apple 44/28 distinction; Flutter current labels/TextScaler | FIXED + VERIFIED AGAINST OFFICIAL SOURCES |
| H-06 | HIGH | redesign workflow said POLISH/REFRESH skip extraction but stage 1.5 looked unconditional; ADD allowed an “industry gap” | later depth rules did not fully override earlier table wording | unnecessary churn and invented features during redesign | conditional stage 1.5, all-depth scope gate, content/screen-contract re-derivation; executable hard-gate test | FIXED + STATICALLY VERIFIED |
| H-07 | HIGH | Markdown “behavioral” suites recorded PASS without executing an agent/runtime/render | test taxonomy inflated evidence | false confidence in behavior | relabeled as reasoned specifications/historical traces; added 15 executable structural/research tests and V4 negative scenarios | FIXED + VERIFIED |
| H-08 | HIGH | responsive files prescribed a 640/768/1024/1280 spine and fixed stack/drawer/card transformations | corpus candidates became universal rules | desktop-narrower mobile and repeated layout behavior | content-stress breakpoints, representation-specific transformations, state/adaptation finish gate, current Android separation | FIXED + STATICALLY VERIFIED |
| M-01 | MEDIUM | cards called universal; static cards used pointer cursor; menus/popovers trapped focus; component system promoted page templates | component convenience outranked semantics | card/overlay/template overuse | representation matrix, card alternatives, corrected focus models, reusable regions instead of page templates | FIXED + STATICALLY VERIFIED |
| M-02 | MEDIUM | exact news red, MENA saturation, palette/ramp/default type and hero rules were stated as universal | observed examples were promoted to design law | cosmetic sameness and cultural stereotyping | demoted to sampled evidence/candidates; brand/content/contrast decide | FIXED + STATICALLY VERIFIED |
| M-03 | MEDIUM | expansion percentages read like translation facts; “same IA, never different structure” blocked cultural adaptation | heuristics and parity principle were overextended | brittle localization | synthetic-budget label, real-string precedence, same capability/task coverage with justified local grouping/order | FIXED + STATICALLY VERIFIED |
| M-04 | MEDIUM | pricing, checkout, settings, search, landing and detail catalogs invented common capabilities or delivery technology | page anatomy lacked scope boundary | plans/reviews/AJAX/account/support invention | page authority contract and conditional page-module language | FIXED + STATICALLY VERIFIED |
| M-05 | MEDIUM | installer deleted destination before copy; verifier used MD5 and fixed missing destinations | non-atomic installation and brittle integrity check | recoverability/sync risk | staged swap with rollback/path guard; SHA-256; verify only existing skill roots | FIXED + COMPILE/INSTALL VERIFIED |
| M-06 | MEDIUM | README counts stale; old reports/tests said complete/executed/current | growth outpaced documentation | misleading repository status | current counts, explicit historical disclaimers, test classification | FIXED + EXECUTABLE COUNT TEST |
| LOW-01 | LOW | skill-creator quick validator cannot import PyYAML in available runtimes | external validator dependency absent | one validation utility unavailable | used repository frontmatter/YAML hazard checks and executable invariants instead | UNRESOLVED — external PyYAML unavailable; equivalent checks passed |

## Research claim ledger

| Claim repaired | Authoritative source | Source type / freshness | What it supports | Where used | Status |
|---|---|---|---|---|---|
| WCAG 2.5.8 is Level AA, 24×24 CSS px or named exceptions | https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html | W3C official, updated 2026-05-11 | level, size, five exceptions | accessibility/floor, contrast-motion, touch/mobile/component guidance | VERIFIED |
| Reflow tests 320 CSS px equivalent; 1280 at 400%; 2D exceptions | https://www.w3.org/WAI/WCAG22/Understanding/reflow.html | W3C official, checked 2026-08-31 | width/height equivalents and exceptions | accessibility/floor | VERIFIED |
| Focus Appearance 2.4.13 is AAA | https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html | W3C official, checked 2026-08-31 | level and enhanced focus target | accessibility/contrast-motion | VERIFIED |
| modal dialogs trap focus; menus use item/arrow-key focus patterns | https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/ and https://www.w3.org/WAI/ARIA/apg/patterns/menubar/ | W3C APG official, checked 2026-08-31 | distinct focus models | accessibility/floor, ui/components | VERIFIED |
| Android has compact/medium/expanded/large/extra-large width classes; width/height are dynamic | https://developer.android.com/develop/adaptive-apps/guides/use-window-size-classes | Android official, checked 2026-08-31 | current cutoffs and runtime semantics | responsive/adaptive-models, android, jetpack-compose | VERIFIED |
| RN Pressable style callback receives `{pressed}`; hover callbacks and hitSlop exist | https://reactnative.dev/docs/pressable | React Native official, checked 2026-08-31 | current API surface | platforms/react-native, input/touch | VERIFIED |
| Flutter Material 3 default is true; M2 opt-out is transitional | https://docs.flutter.dev/release/breaking-changes/material-3-default | Flutter official, checked 2026-08-31 | framework default, not design mandate | platforms/flutter | VERIFIED |
| Apple button hit region general rule 44×44pt; accessibility table distinguishes 44 default / 28 minimum for iOS/iPadOS | https://developer.apple.com/design/human-interface-guidelines/buttons and https://developer.apple.com/design/human-interface-guidelines/accessibility | Apple HIG official, checked 2026-08-31 | general target and platform table | mobile/accessibility/touch/SwiftUI source notes | VERIFIED |

## Test classification and results

- **STATIC/STRUCTURAL executable:** `python -m unittest discover -s tests
  -p "test_*.py" -v` — 17 tests discovered: 16 passed; one synthetic
  directory-symlink unit skipped because the test environment cannot create
  one. The real legacy Pi junction cleanup path was exercised successfully by
  the subsequent installation run.
- **Tool syntax:** `python -m compileall -q research/tools scripts` — passed.
- **Research aggregation:** corrected aggregate ran over 145 CSS-evidence sites;
  report facts matched executable recomputation.
- **Repository integrity:** retrieval map has no ghosts/orphans; local
  knowledge references resolve; frontmatter hazard check passes.
- **REASONED-SPEC:** V4 14-scenario matrix plus preserved historical suites;
  clearly non-executable.
- **BEHAVIORAL/RUNTIME/RENDER:** UNVERIFIED — no repository harness.

## Failures encountered and repair loop

1. New executable suite initially failed because V2.2 Markdown was still named
   behavioral without a reasoned/non-executable disclosure. It was relabeled;
   retest passed.
2. Pre-sync install verification failed across all 18 destinations, correctly
   detecting missing/new/different files. The installer was made recoverable,
   copies were synchronized only after content validation, and verification
   was rerun.
3. Skill-creator `quick_validate.py` failed to start because PyYAML is absent
   in both available Python runtimes. No repository mutation can repair that
   external dependency; equivalent YAML/frontmatter checks passed.
4. The first synchronization exposed Windows path aliases being detected twice
   and a moved Pi junction backup that `rmtree` could not remove. Destination
   content was already intact, but the installer was repaired to normalize
   paths, unlink junctions without traversal, report partial installs as
   failure, and dynamically verify every detected root. Retest: 19/19
   destinations, 277/277 files each, SHA-256 identical.

## Final limitations

- Static contracts materially reduce known failure paths but cannot guarantee
  compliance by every future model invocation.
- Source-only corpus evidence cannot establish rendered hierarchy, active CSS,
  interaction quality, or performance.
- The corpus remains a dated sample; current competitor-specific or
  fast-changing facts require targeted research. Deep/Audit is reserved for
  explicitly broader investigation and repository/evidence-wide work.
- Tailwind adoption has no current percentage until the corpus is re-fetched
  with the repaired detector. No decision in the skill depends on that number.

## Post-audit finalization addendum

Date: 2026-08-31.

- Re-verified the report-backed scope, template, redesign, responsive,
  accessibility, platform, evidence, and installer contracts against the
  current master; no repaired CRITICAL or HIGH issue regressed.
- Corrected the remaining mode-router defect: Normal mode now includes every
  redesign depth and the full relevant design/validation workflow. Deep/Audit
  is limited to REAL-UI/repository/evidence-wide investigation or explicitly
  deep research. The five release prompts are covered by executable static
  assertions and reasoned traces.
- Removed the install verifier's machine-specific source fallback; it now
  derives the repository root from its own location. A regression assertion
  rejects user-home absolute paths.
- Ran the skill-creator quick validator successfully using PyYAML from an
  isolated temporary dependency directory; no dependency was added to this
  repository or its release package.
- Exact public-package validation exposed and repaired one test dependency:
  breakpoint consistency now recomputes from raw corpus JSON when it exists
  and otherwise verifies the published aggregate summary that ships publicly.
- That fallback then exposed a stale generated public artifact:
  `aggregate-summary.txt` still contained pre-repair declaration-frequency
  counts (for example 768px=2641). It was regenerated from the repaired
  per-site aggregator and now records 768px=91/145 and 1024px=63/145.
- Final executable repository result at this stage: 19 tests discovered,
  18 passed, and one synthetic directory-symlink test skipped because this
  Windows environment cannot create it. The real legacy junction path remains
  verified by the prior successful 19-destination installation run.
- BEHAVIORAL/RUNTIME/RENDER remain **UNVERIFIED** because the repository has no
  isolated agent/browser/native/render harness. The routing scenarios are
  STATIC/STRUCTURAL plus REASONED-SPEC evidence, not generated-output proof.
