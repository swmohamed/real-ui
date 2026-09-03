# REAL-UI V7 — Complete Design Intelligence Expansion

Audit date: 2026-09-01
Baseline: V6 evidence-driven expansion
Method: repository inspection → gap matrix → authoritative research → diverse
current-product documentary study → cross-product comparison → principle and
limit extraction → routing/knowledge repair → executable validation.

## Evidence boundary

- Existing V6 AI, automation, collaboration, concurrency, permission,
  long-running operation, recovery, authority, and provenance contracts were
  preserved.
- Official standards/platform/design-system pages below are DOC-OBSERVED.
- Current-product findings below are DOC-OBSERVED from public first-party
  product/help pages unless stated otherwise. They prove documented behavior
  and product intent, not that this audit executed the feature.
- The existing code-first corpus remains SOURCE-OBSERVED. Source presence does
  not prove rendering, visibility, or runtime success.
- A bounded Chromium render attempt was rejected: public HTTPS navigation
  timed out and blank captures were not admitted as RENDER-OBSERVED evidence.
- Product examples are evidence, not templates. No one product or industry
  determines a rule.

## V6 baseline preserved

V6 established durable contracts for:

- AI role, context/data scope, suggestion/draft/commit boundary, authority,
  provenance/freshness, review, interruption, and recovery;
- collaboration actors/permissions, attribution, presence limits,
  stale/conflict/offline states, durable vs ephemeral communication, history,
  and catch-up/restore;
- long-running work with durable identity/state, truthful progress, partial
  outcome, side effects, return, and distinct cancel/retry/resume/undo/rollback;
- scope authority, page/industry authority boundaries, evidence labels, and
  normal-vs-deep routing.

The V7 work extends those contracts; it does not replace them.

## Gap matrix

| Discipline | Baseline strength | Verified gap | Repair |
|---|---|---|---|
| Discovery/research | research-method rigor for the skill itself | no runtime module for users/context/current journey/research questions/outcomes | new `foundations/experience-evidence.md` + routing |
| Service/journey | product entities and lifecycles | weak entry/channel/handoff/backstage/result/recovery model | current-experience trace in evidence, product, and redesign modules |
| Task analysis | frequency × criticality | “task #1 one step/home” over-generalized; no entry-context model | multi-factor priority + entry/continuity/outcome fields |
| Interaction | states and long operations | no unified selection/range/bulk/drag/autosave/optimistic/latency contract | new `ux/interaction-control.md` |
| Visual design | hierarchy/layout/color and named DNA families | industry-to-style lookup and named-family blend created template gravity | independent visual job/axes, style-blind composition, lineage vocabulary only |
| Responsive | useful content-stress guidance mixed with fixed transforms | fixed spine, grid/card/sheet/footer/hero assumptions, unsupported regional traffic claim | content-derived thresholds and transformation ledger |
| Mobile/tablet | platform targets and state coverage | universal thumb/bottom-nav, tablet panes, columns, form thresholds | posture/window/task-dependent guidance |
| Desktop native | generic desktop-device page | Windows/macOS window, document, menu, command, resize, restore divergence missing | new `platforms/desktop-native.md` |
| Accessibility | strong WCAG 2.2 correction work | exactly one `h1`, never skip headings, fixed focus recipe, universal live region/AAA claims | standards/guidance/recipe distinctions corrected |
| Localization/RTL | good bidi and locale foundation | synthetic expansion heuristics too authoritative; chart/toast direction universal | actual target strings, domain conventions, semantic direction |
| Design systems | tokens/states/versioning | fixed variant matrix and shallow maturity/adoption governance | evidence, lifecycle, ownership, limitations, migration, escape-hatch health |
| Redesign | strong V6 extraction/full-redesign gates | current service journey/outcome and independent visual derivation not explicit | experience/outcome gate + visual axes in redesign pipeline |
| Anti-template | decorative + V6 structural AI failures | sidebar-dashboard, mobile card-stack/FAB, named-style roulette, identity=color/logo not explicit | new structural rejection signals |

## Authoritative sources

Accessed 2026-09-01. The lesson column is a bounded synthesis, not a quotation.

| Authority | URL(s) | What was retained | Limit |
|---|---|---|---|
| GOV.UK Service Manual — user research | https://www.gov.uk/service-manual/user-research ; https://www.gov.uk/service-manual/user-research/how-user-research-improves-service-design ; https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs ; https://www.gov.uk/service-manual/user-research/plan-user-research-for-your-service ; https://www.gov.uk/service-manual/user-research/user-research-in-discovery ; https://www.gov.uk/service-manual/user-research/researching-user-experiences | research current behavior end to end and across channels; include disabled/support/operations perspectives; define questions and assumptions; combine qualitative, operational, and analytics evidence | government-service guidance informs a method, not every product’s staffing/process |
| GOV.UK Service Manual — service design | https://www.gov.uk/service-manual/design/introduction-designing-government-services | design the whole journey/front-to-back service, not isolated screens | public-service context does not prescribe commercial IA or visual style |
| WCAG 2.2 / WAI | https://www.w3.org/TR/WCAG22/ ; https://www.w3.org/WAI/WCAG22/Understanding/reflow.html ; https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/ ; https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html ; https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html ; https://www.w3.org/WAI/tutorials/page-structure/headings/ | 320 CSS px reflow with two-dimensional exceptions; 24×24 target-size criterion and exceptions; non-drag single-pointer path; headings represent structure and should avoid confusing gaps where possible | WCAG conformance criteria are distinct from preferred platform target sizes and component token recipes; exactly one `h1` is not required |
| W3C Internationalization | https://www.w3.org/International/articles/lang-bidi-use-cases/ | language/direction metadata and explicit bidi handling for mixed strings | bidi correctness does not decide chart/map/time semantics |
| Apple HIG | https://developer.apple.com/design/human-interface-guidelines/accessibility ; https://developer.apple.com/design/human-interface-guidelines/layout ; https://developer.apple.com/design/human-interface-guidelines/design-principles ; https://developer.apple.com/design/human-interface-guidelines/writing ; https://developer.apple.com/design/human-interface-guidelines/designing-for-macos/ ; https://developer.apple.com/design/human-interface-guidelines/keyboards | platform-specific control sizes; safe areas and context; flexible macOS windows, menu bar, precision input, standard shortcuts, keyboard-only work, and customization | Apple guidance is platform-specific; iOS/iPadOS/macOS sizes and behaviors are not CSS rules |
| Android Developers | https://developer.android.com/develop/ui/compose/build-adaptive-apps?hl=en ; https://developer.android.com/develop/adaptive-apps/guides/support-different-display-sizes ; https://developer.android.com/develop/ui/views/layout/canonical-layouts?hl=en ; https://developer.android.com/develop/adaptive-apps ; https://developer.android.com/develop/adaptive-apps/guides/get-started-with-adaptive-apps ; https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-2 | current window—not device label—drives adaptation; continuity across resize/rotation/multi-window/fold; canonical layouts are content/task candidates; support inputs beyond touch | Android window classes do not become web breakpoints or mandatory pane counts |
| Microsoft Learn | https://learn.microsoft.com/en-us/windows/apps/design/basics/navigation-basics ; https://learn.microsoft.com/en-us/windows/apps/design/basics/ ; https://learn.microsoft.com/en-us/windows/apps/develop/user-interface ; https://learn.microsoft.com/en-us/windows/apps/design/controls/navigationview ; https://learn.microsoft.com/en-us/windows/apps/design/basics/commanding-basics ; https://learn.microsoft.com/en-us/windows/apps/design/input/keyboard-interactions ; https://learn.microsoft.com/en-us/windows/apps/develop/ui/controls/collection-commanding | no single navigation shell; windows/layout/commands are separate concerns; frequent commands near content, secondary/context commands in suitable surfaces; feedback and cross-input paths; keyboard completeness | Windows control examples are not universal web/macOS component prescriptions |
| Carbon Design System | https://carbondesignsystem.com/elements/2x-grid/overview/ ; https://carbondesignsystem.com/elements/2x-grid/usage/ ; https://carbondesignsystem.com/elements/motion/overview/ | grids establish key lines/rhythm; fixed/fluid/hybrid behavior follows content; productive and expressive motion have distinct roles | one design system is a system-specific example, not a global grid/motion standard |
| GOV.UK Design System | https://design-system.service.gov.uk/community/contribution-criteria/ ; https://design-system.service.gov.uk/community/community-principles/ | shared components need a distinct evidenced need, representative testing including disabled users, consistency/versatility, ownership, support, versioning, and honest evidence | contribution governance does not mandate one lifecycle vocabulary |
| USWDS | https://designsystem.digital.gov/ ; https://designsystem.digital.gov/components/lifecycle/ | component maturity/confidence should be explicit from proposal through stable/caution/deprecation | public-sector lifecycle labels are examples, not required names |
| Atlassian Design System | https://atlassian.design/foundations ; https://atlassian.design/get-started/content-design ; https://atlassian.design/foundations/content/ ; https://atlassian.design/foundations/accessibility ; https://atlassian.design/foundations/typography/applying-typography ; https://atlassian.design/get-started/develop/composition | foundations/tokens and content are first-class; composition and primitives reduce inflexible god APIs; accessibility extends beyond a component | an enterprise system’s component API is evidence for governance principles, not an app architecture template |

## Current-product sample

Eighteen product families across transport, travel, finance, public service,
commerce, delivery, media, sports/fitness, and education were studied. This
sample is deliberately heterogeneous; its value is comparison, not frequency
claims about the market.

| Product | Product/industry/platform spread | First-party URLs | DOC-OBSERVED decision evidence |
|---|---|---|---|
| Uber | transport; consumer mobile/web journey | https://www.uber.com/us/en/ride/how-it-works/ ; https://www.uber.com/us/en/ride/safety/tips/ | phased request/match/ride/result; map tracking, identity/safety verification, upfront price |
| Airbnb | travel marketplace; consumer web/mobile | https://www.airbnb.com/help/article/3043 ; https://www.airbnb.com/help/article/479 ; https://www.airbnb.com/help/article/252 ; https://www.airbnb.com/help/article/39 ; https://www.airbnb.com/help/article/149 | search depends on destination/dates/guests; facets/map-list; cancellation before/after booking; ranking and accessibility-filter documentation |
| Booking.com | travel marketplace; high-density consumer | https://www.booking.com/content/how_we_work.en-gb.html | filter/sort/ranking, personalization and commercial-ranking disclosure; criteria vary by product type |
| Emirates | airline; global transaction/service | https://www.emirates.com/us/english/manage-booking/online-check-in/ ; https://www.emirates.com/us/english/manage-booking/ ; https://www.emirates.com/us/english/book/about-booking-online/emirates-seat-selection/ | booking-reference entry, time/eligibility constraints, seat-map spatial choice, passenger/group rules, change/refund recovery |
| Wise | finance; cross-border consumer/business | https://wise.com/help/articles/2977959/how-do-i-send-money-with-wise ; https://wise.com/help/articles/2971625/how-do-i-cancel-my-transfer ; https://wise.com/help/articles/2522717/fees-for-sending-money/5pl8GO51vA.pdf ; https://wise.com/help/topics/5bVKT0uQdBrDp6T62keyfz/sending-money | recipient/amount/payment choice, fee and ETA evidence, review before commit, tracking, status-dependent cancellation |
| NHS App | health/public service; native/web support | https://digital.nhs.uk/services/nhs-app/nhs-app-features ; https://www.nhs.uk/nhs-app/ ; https://www.nhs.uk/nhs-app/about/nhs-app-release-notes/ ; https://digital.nhs.uk/services/nhs-app/roadmap ; https://design-system.nhsapp.service.nhs.uk/examples/hub-pages/your-health/ | current 2026 task grouping uses service evidence; prescriptions/appointments/results, profile/proxy access, screen-reader work, variable records/service availability |
| GOV.UK | cross-government public service; responsive web | authoritative GOV.UK URLs in the prior table | end-to-end service and current-channel research, plain-language/task focus, front/backstage dependencies |
| eBay | marketplace; browse/operate at scale | https://www.ebay.com/help/buying/finding-items-managing-purchases/watch-list?id=4046 ; https://www.ebay.com/help/buying ; https://www.ebay.com/help/default/default/default?id=4006 | retrieval/filter/sort, watch-list high-volume selection, ended-item lifecycle, saved search/history |
| IKEA | retail plus in-store/fulfillment service | https://www.ikea.com/us/en/customer-service/contact-us/ ; https://www.ikea.com/us/en/customer-service/track-manage-order/ ; https://www.ikea.com/us/en/customer-service/returns-claims/return-policy/ ; https://www.ikea.com/us/en/customer-service/shopping-at-ikea/ | online/in-store/click-collect/delivery journey; order state, partial deliveries, status-dependent cancellation, cross-channel recovery |
| Uber Eats | food delivery; mobile transaction/exception handling | https://help.uber.com/en/ubereats/restaurants/article/sustituciones?nodeId=56303d55-adf4-45dd-af28-2c9b6f228167 ; https://help.uber.com/ubereats/restaurants/article/my-order-had-missing-or-incorrect-items?nodeId=93fe8ec6-1f78-4279-a574-177d122fda26 ; https://help.uber.com/ubereats/stores/article/my-order-is-taking-longer-than-expected-?nodeId=383c2d40-e703-4ee0-a82c-8ff200432d8c | per-item substitution authority, approval/refund fallback, partial-order exceptions, delay tracking and status-dependent cancel/refund |
| Spotify | media; mobile/desktop/cross-device | https://support.spotify.com/uk/article/your-premium-benefits/ ; https://support.spotify.com/us/article/offline-backup/ ; https://support.spotify.com/us/ | online/offline state, library/search/queue, cross-device continuity, shared Jam queue |
| Netflix | media; TV/mobile/web | https://help.netflix.com/en/node/102377 ; https://help.netflix.com/en/node/65679 | profiles/parental control, browse/search/recommendations, cross-device continuity, platform-specific offline limits |
| YouTube | media; web/mobile/TV | https://support.google.com/youtube/answer/16089387?hl=en ; https://support.google.com/youtube/answer/6342839?hl=en | recommendation surfaces differ by context; user controls/history; search-first empty home when personalization is off |
| ESPN | sports/media; mobile/TV | https://plus.espn.com/app ; https://support.espn.com/hc/en-us/articles/360035075292-How-do-I-sign-up-for-Alerts | scores/stats/live video/highlights/alerts/favorites; TV multiview differs from mobile use |
| Strava | fitness/social/geospatial; mobile/web | https://support.strava.com/en-us/articles/15402012-edit-map-visibility?mobile_site=true ; https://support.strava.com/en-us/articles/15401776-strava-s-privacy-controls-faq ; https://support.strava.com/hc/en-us/articles/216919577-Ride-Activity-Pages | map/activity data representation, global versus per-activity privacy, downstream visibility consequences, density/disclosure and segment linkage |
| Khan Academy | education; web/mobile | https://support.khanacademy.org/hc/en-us/articles/115002552631-What-are-Course-and-Unit-Mastery | course/unit mastery hierarchy, progress, assessment, and next-learning relationship |
| Coursera | education; web/mobile | https://www.coursera.support/s/learner-help-center-quizzes-assignments?language=en_US | deadlines, grades, quizzes, peer review, and lab workflows vary; one course-card shell cannot represent all work |
| Duolingo | education; playful mobile/web | https://blog.duolingo.com/streak-milestone-design-animation/ ; https://blog.duolingo.com/product-lessons-friend-streak/ ; https://blog.duolingo.com/new-duolingo-home-screen-design/ ; https://blog.duolingo.com/duolingo-teaching-method/ | research/experiment-informed path, embedded practice, milestone motion, social accountability; first-party product-blog claims kept contextual |

## Cross-product comparisons

### 1. Entry and priority

NHS documents a reorganization around heavily used service areas; Emirates
and Wise use known-object/transaction entry; Uber begins a real-time request;
YouTube can become search-first when personalization is unavailable. Principle:
task priority must include launch context, identity/state, and consequence.
“Put task #1 on home in one step” was rejected.

### 2. Search and discovery

Airbnb, Booking.com, eBay, YouTube, Spotify, and course/media products all use
search/discovery, but the query dimensions, ranking explanations, saved state,
personalization controls, and result representations differ. Principle:
retrieval is derived from content relationships, user intent, and business
effects—not a universal search bar + filter chips template.

### 3. Transaction, commitment, and recovery

Wise, Emirates, Airbnb, IKEA, Uber Eats, and Uber expose different review,
timing, price, eligibility, cancellation, partial-outcome, and refund states.
Principle: friction and recovery follow consequence, authority, lifecycle, and
reversibility. A generic confirmation modal is insufficient.

### 4. State and continuity

Spotify/Netflix span offline and cross-device contexts; IKEA can split an
order into deliveries; Uber/food delivery depend on live/degraded tracking;
learning products preserve progression. Principle: continuity is a product
contract across sessions, devices, and channels—not a “recent activity” card.

### 5. Representation

Emirates needs a seat map, Strava a geographic/activity representation,
eBay selection over homogeneous items, Khan Academy a mastery hierarchy,
ESPN simultaneous scores/media, and Coursera varied assignment workflows.
Principle: representation comes from relationships and decisions. Cards are
not a neutral default.

### 6. Authority, privacy, and provenance

Strava separates account defaults from per-activity visibility; YouTube
documents recommendation controls; Booking.com discloses ranking/commercial
influence; Uber Eats captures per-item substitution authority; NHS supports
proxy access. Principle: ownership, scope, source, and downstream consequence
must be visible at the decision boundary.

### 7. Visual/composition diversity

Institutional health/public service, premium airline operations, dense travel
marketplaces, playful learning, sports media, financial transfer, and
geospatial fitness can share accessibility and state principles while needing
opposite density, hierarchy, media, geometry, motion, and content registers.
Principle: set independent visual axes from the product; industry-to-style
lookup and competitor mimicry destroy this diversity.

### 8. Platform expression

Netflix/ESPN/YouTube change for TV; Spotify spans desktop/mobile/offline;
Strava and Uber are mobile/geospatial; NHS and commerce services bridge app,
web, staff, documents, and physical fulfillment. Principle: share product
meaning and lifecycle while adapting navigation, command, input, window, and
content expression. Pixel identity is not continuity.

## Integrated knowledge changes

### Genuinely new modules

1. `knowledge/foundations/experience-evidence.md`: decision-led research,
   people/context, current journey/service/channel, task analysis,
   triangulation, research-to-design trace, outcomes and guardrails.
2. `knowledge/ux/interaction-control.md`: command model, selection/range/
   select-all, bulk eligibility, drag alternatives, explicit/autosave/
   optimistic/draft commit models, latency, destructive-action friction.
3. `knowledge/platforms/desktop-native.md`: Windows/macOS windows,
   documents, menus/toolbars/context, keyboard/pointer/touch/pen, resize,
   multi-window/restoration, and platform divergence ledger.

### Corrected or expanded modules

- `SKILL.md` and `knowledge/taxonomy.md`: activation and finish gates for all
  three additions; visual derivation replaces named DNA selection.
- `foundations/{principles,product-modeling,layout,visual-hierarchy}.md`:
  coordinated-work hierarchy, entry-context task priority, content-derived
  regions/thresholds, and state-preserving transformation ledger.
- `visual-dna/*`: named families demoted to optional vocabulary; industry
  mapping, blend rules, and token recipes removed.
- `responsive/mobile-patterns.md` and device/platform files: removed traffic,
  fixed-count, fixed-pane, fixed-row, fixed-transform, and “all professionals”
  assumptions.
- `accessibility/*`: corrected headings, focus recipe, live-region, contrast,
  and standards-versus-guidance distinctions.
- `localization/i18n.md` and `rtl/implementation.md`: real strings and domain
  conventions outrank synthetic percentages; semantic direction outranks
  blanket chart/toast mirroring.
- `design-systems/components-states.md`: meaningful state intersections,
  maturity/evidence/ownership/limitations/migration, and adoption quality.
- `typography/{latin-systems,responsive-pairing}.md`, `motion/principles.md`,
  `iconography/systems.md`, `ui/data-viz.md`, `input/{mouse-keyboard,touch}.md`,
  and `ux/states.md`: fixed family counts, pixel/type recipes, motion timings,
  global reduced-motion overrides, icon grids, command palettes, chart anatomy,
  gesture sets, skeletons, and empty-state illustrations demoted to contextual
  candidates with explicit decision conditions.
- `anti-patterns/ai-aesthetics.md`: professional-sidebar dashboard,
  named-style roulette, mobile card-stack/FAB, and identity-as-color/logo.
- `redesign/{extraction,workflow}.md`: current journey/channels/backstage and
  experience/outcome hard gate; independent visual axes for REDESIGN/FULL.
- `README.md`: obsolete showcase claims, tree entries, scripts, images, and
  commands removed; knowledge count updated.

## Rejected observations and limits

- BBC public-page access was blocked by robots; no BBC behavior claim was made.
- The browser render sample timed out on public HTTPS. Blank screenshots were
  rejected, not relabeled as render evidence.
- First-party help/blog documentation can describe intent and supported
  behavior, but not actual success, prevalence, or usability.
- One product’s feature, design-system component, or platform example cannot
  become a standard or product-scope default.
- Synthetic localization expansion percentages are stress inputs only; real
  target strings and translator/user review outrank them.
- “One `h1`,” “never skip heading levels,” “all desktop users are experts,”
  “tablet means two panes,” “mobile means bottom nav/cards/FAB/sheet,” and
  “task #1 must be one step from home” were rejected as universal rules.
- Current product pages are time-sensitive. URLs and access date are recorded;
  runtime guidance stores generalizable principles, not volatile screenshots
  or competitor-specific defaults.

## Validation record

This section is completed after integration. Required checks:

- **Executable repository invariants:** PASS — 29 tests; one expected Windows
  directory-symlink capability skip. Includes no-ghost/no-orphan routing,
  scope/template/accessibility/platform contracts, V6 AI/collaboration/
  operations preservation, three V7 module activations, showcase removal, and
  scenario-matrix coverage.
- **Skill-package quick validation:** PASS — official skill-creator validator
  under WSL (`Skill is valid!`). Windows Python lacked the validator’s external
  PyYAML dependency; the skill itself was not changed to work around that host
  dependency.
- **Python compile:** PASS — `research/tools` and `scripts`.
- **Patch hygiene:** PASS — `git diff --check` returned no errors (existing
  CRLF-to-LF notices are warnings on unrelated/previously modified files).
- **Knowledge integrity:** PASS — 126 knowledge files; retrieval-map ghosts
  none; orphans none; knowledge cross-references resolve; all 3 V6 target
  modules and all 3 V7 additions present.
- **Showcase/demo cleanup:** PASS — no active showcase path or render-showcase
  command remains; obsolete render scripts and V5 showcase reports are gone;
  the untracked pure-showcase tree was moved outside the repository to a
  recoverable temp archive. The outdated demo-like manual result trace was
  removed; reasoned scenario specifications remain.
- **Reasoning scenarios:** PASS at REASONED-SPEC/STRUCTURAL level — seven
  scenarios cover same-industry different products, same product type across
  industries, native desktop interaction, Arabic mobile public service,
  cross-platform live media, FULL redesign, and evidence integrity. Their
  activation/finish-gate consequences were reviewed; no BEHAVIORAL, RUNTIME,
  or RENDERED claim is made.
- **Rendered research:** REJECTED/NOT RUN — agent-browser public HTTPS
  navigation timed out; blank captures were discarded. Documentary evidence
  remains DOC-OBSERVED.
- **Installed-copy sync:** NOT PERFORMED — `verify_install.py` confirmed source
  cross-references/compile/routing/YAML checks but reported existing installed
  skill copies as stale. This audit did not overwrite installations or publish.
