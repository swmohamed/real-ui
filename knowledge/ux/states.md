# UX: States — Loading, Empty, Error, Success, Offline

V2.1: deep error craft + validation timing → ux/forms-validation.md;
notification surfaces → ux/notifications.md.

States are where amateurs ship blanks and professionals ship confidence.

## Loading

- **Skeletons** that match final layout (same blocks, shimmer subtle) —
  perceived speed + no layout shift; never spinners for page-level loads
- **Inline spinners** only for actions <1s (buttons keep width — label +
  spinner swap)
- **Progressive loading**: render text instantly, media streams in with
  aspect-ratio placeholders (CLS = 0)
- Long waits (>3s): percentage or steps ("Fetching rates…"), cancel affordance
- Optimistic UI for likes/votes/cart — instant with rollback on failure

## Empty states (the onboarding moment)

Every empty state answers: what is this? why is it empty? what do I do now?
- Illustration/photo (on-brand, not clip-art), one-line explanation, one
  primary action ("Add your first invoice" / أضف أول فاتورة), secondary
  link (import/learn)
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
