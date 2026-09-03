# V7 Complete-Intelligence Reasoning Scenarios

These are reasoned scenario specifications, not executable agent or render
tests. They evaluate routing, derivation, and rejection behavior. A future
harness may execute them; this document does not claim that it did.

Coverage: greenfield, REDESIGN/FULL redesign, web, mobile, tablet, desktop,
native, cross-platform, RTL, content-heavy, data-heavy, interaction-heavy,
same-industry/different-product, and same-product-type/different-industry work.

## S1 — same industry, opposite healthcare products

Input A: Arabic/English patient self-service app for appointments, results,
and proxy access. Input B: native Windows clinical operations workspace for
staff coordinating queues and urgent exceptions.

Required routing:

- both: experience-evidence + product-modeling + healthcare authority;
- A: mobile, accessibility/mobile, localization/RTL, consent/proxy source;
- B: desktop-native + desktop + mouse-keyboard + interaction-control +
  collaboration/operations where supplied.

Pass: derives different entry, density, representation, command, window, and
visual axes from people/tasks/consequence while keeping appropriate clinical
trust and terminology. Fail: both become “calm blue healthcare dashboards” or
the patient app inherits a staff sidebar.

## S2 — same product type, different industries

Input A: book a hotel. Input B: book a high-consequence specialist medical
appointment. Both include search, availability, selection, review, and change.

Pass: shared transaction principles remain, but eligibility, source,
availability semantics, consequence, recovery, identity/privacy, and content
register produce different flows and hierarchy. Fail: one universal booking
template with changed labels/photos.

## S3 — native desktop asset manager

Input: installed Windows/macOS creative asset manager with resizable windows,
files and cloud assets, multi-select/range/select-all, drag to collections,
bulk tagging, autosave metadata, import, conflicts, and keyboard workflows.

Pass: routes desktop-native, interaction-control, collaboration-concurrency,
operations-recovery, mouse-keyboard, and platform divergence. Specifies window/
document lifecycle, command target/scope, selection persistence, non-drag and
keyboard alternatives, durable save language, partial bulk results, restore,
and distinct Windows/macOS menus/shortcuts. Fail: a wide web dashboard with
hover-only controls or an unexplained Save button over silent autosave.

## S4 — Arabic mobile public service

Input: Arabic-first phone service for an eligibility application with mixed
Latin identifiers, uploaded evidence, save-and-return, staff handoff, status,
and appeal.

Pass: traces front/backstage journey through appeal; validates bidi strings,
real Arabic labels, keyboard/zoom/screen reader, save durability, source and
authority, interruption, and long-operation states. Fail: mirror-only RTL,
synthetic +25% strings presented as validation, or mobile = card stack/FAB.

## S5 — cross-platform live media

Input: one live-sports product across phone, responsive web, TV, and tablet;
scores, commentary, video, alerts, and favorites are in scope.

Pass: shared entity/status/terminology contract with platform-specific
navigation, focus, viewing distance, input, simultaneous content, notification,
and continuity. Fail: pixel-identical screenshots, a poster wall forced onto
scores, or phone bottom navigation copied to TV.

## S6 — FULL redesign with identity and journey preservation

Input: FULL redesign of a travel service whose old UI has known booking lookup,
seat choice, change/refund, disruption messages, and bilingual brand assets.

Pass: extracts requirements/capabilities/workflows/presentation; preserves
entry, handoff, result/recovery, authority and lifecycle; quarantines old
composition; derives new IA and visual axes; runs depth, capability, scope,
experience/outcome, control, accessibility, localization, and platform gates.
Fail: re-clothes the old shell, imports a cinematic airline preset, invents a
loyalty tier, or loses disruption/refund recovery.

## S7 — evidence integrity

Input: first-party help page documents a feature; Chromium rendering is blocked.

Pass: labels behavior DOC-OBSERVED, records access date/limit, makes no render
or runtime claim, compares with other products before integration, and rejects
blank captures. Fail: calls the page “tested,” infers usability, or turns one
documented product choice into a standard.

## Review rubric

Each scenario passes only if the reasoning exposes:

1. activated files and evidence confidence;
2. people/context/current experience and product/scope model;
3. representation and visual-axis decisions with alternatives rejected;
4. states, control, accessibility, localization, platform, and recovery;
5. no copied product shell, industry style lookup, invented capability, or
   universal device transformation;
6. a validation result that can force re-derivation.
