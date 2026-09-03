# UX: States — Loading, Empty, Error, Success, Offline

V2.1: deep error craft + validation timing → ux/forms-validation.md;
notification surfaces → ux/notifications.md; durable/background work →
ux/operations-recovery.md.

States are where amateurs ship blanks and professionals ship confidence.

## Loading

- Use stale content, reserved space, skeleton, progress, or activity indicator
  according to what is known and whether useful content already exists.
  Skeletons must not fabricate structure or loop indefinitely; a page-level
  indicator may be appropriate for a genuinely bounded transition.
- **Inline activity indicators** for bounded local actions when progress is
  unknown (buttons keep width and preserve an accessible label)
- **Progressive loading**: render text instantly, media streams in with
  aspect-ratio placeholders (CLS = 0)
- Long or background-safe work: expose a meaningful stage and durable status;
  show percentage only when measured against real work. Offer cancel only when
  cancellation is implemented and its side effects are clear.
- Optimistic UI is a consequence/reversibility decision, not a feature-class
  recipe; expose pending/rejection and restore or recover truthfully.

Loading is not the whole operation lifecycle. Queued, waiting-for-input,
partial, canceling, superseded, resumable, and rollback states belong in the
operation model when applicable. Keep cancel, retry, undo, resume, restore,
and rollback distinct; see `operations-recovery.md`.

## Empty states (the onboarding moment)

Every empty state answers: what is this? why is it empty? what do I do now?
- Use only the explanation, action, sample, guidance, or illustration the empty
  cause and next step need. Do not force an illustration, one-action hierarchy,
  or “first item” onboarding into filtered, permission, or completed empties.
- Contextual empties beat generic: empty search ≠ empty project ≠ first-run
- Seed-content options where honest (sample project, demo data toggle)

## Errors

- **Field-level**: persistent message adjacent to field, icon + text,
  aria-describedby link; error summary on top for long forms with anchors
- **Page-level**: what happened (plain), why (if known), what to do
  (retry/alternative), who to contact (with reference ID)
- **Never**: raw stack traces, "Error 500" alone, blame copy ("You entered
  an invalid…" → "That email looks incomplete — mind checking it?")
- Network errors: auto-retry with backoff + manual retry; queue offline
  actions where the product expects connectivity gaps (MENA mobile
  networks included)

## Success

- Confirm what happened + what happens next + timeline ("Receipt sent to
  your email; delivery Tue–Thu")
- Reference numbers copyable (order #, ticket ID)
- Continue-to-value CTA (track order / go to dashboard), not dead ends
- Celebrate sparingly: confetti for milestones ( Duolingo-class products
  only), not for saving settings

## Offline & degradation

- Offline banner with queued-actions count; cached views labeled with
  freshness ("prices as of 10:42")
- Feature degradation > full failure (chat down ≠ site down)
- Service-status transparency for tools (status page link in-app)

## RTL/Arabic

- All state copy localized properly (error messages are UX copy, not
  developer strings); Arabic politeness register without excessive
  formality
- Numbers/codes inside Arabic error text: wrap LTR spans so order IDs
  don't scramble
- Skeleton layouts mirror RTL

## Anti-patterns

- Spinners for everything; skeletons that don't match layout (shift)
- Empty states with no action; errors with no next step
- Alert() dialogs for system errors
- Silent failures (user believes action succeeded)
- Success pages that auto-redirect before reading
- Invented percentages, fake stages, or a cancel control that only hides work
