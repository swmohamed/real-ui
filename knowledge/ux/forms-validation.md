# UX: Forms & Validation (the transaction's make-or-break)

Deep forms knowledge for flows (checkout, KYC, applications, settings).
Extends pages/account-settings-forms.md (page anatomy) and
input/touch.md (input modes). Evidence anchors: NN/g error-message
guidelines (fetched 2026-08 — OBSERVED secondary, high-quality) +
WCAG 2.2 criteria (official, recovered — PLATFORM RULE).

## Validation timing (the three-gate model)

1. **Inline (as-you-type)**: after field blur or completion — confirm
   formatting early (email/password strength/username availability).
2. **On-submit**: gate the flow; scroll to first error + anchor.
3. **Server-side**: async results shown AT the field (not a top banner
   hiding the problem); preserve ALL input on failure (NN/g: respect
   user effort — never wipe a form on error `[OBSERVED - nngroup]`).

Never: validate-on-keystroke before first completion (premature
errors), or validate only at the very end of a long form.

## Error message craft (NN/g evidence `[OBSERVED - nngroup.com/
articles/error-message-guidelines]`)

- **Highly visible**: adjacent to the field, high-contrast, not only
  red (color independence — accessibility/contrast-motion.md).
- **Constructive**: state the problem + HOW to fix it, in human words
  ("Enter a phone number like 01xx xxx xxxx") — plainspoken language.
- **Respect effort**: keep everything typed; place cursor in the
  offending field; never punish with full resets.
- **Severity-appropriate**: warning (can proceed) vs error (blocked)
  vs confirmation (destructive) — visually distinct classes.
- Apologize sparingly; specificity beats politeness.
- Announce errors to screen readers (aria-live / liveRegion
  `[PLATFORM RULE]`).

## Required vs optional discipline

Mark required (or optional when rare); never the ambiguous red-asterisk-
only pattern without a legend. Labels ABOVE inputs (fastest scanning —
stable cross-source convention `[DESIGN PRINCIPLE]`); placeholders are
NOT labels (they vanish on input).

## Field design rules

- Right keyboard/input-mode per field type (input/touch.md).
- Masks + live formatting (card numbers grouped, phone grouped per
  locale) — but accept paste in any format then normalize.
- Sensible defaults; auto-advance where safe (OTP digits); autofill
  attributes (name/email/one-time-code) `[PLATFORM RULE - HTML]`.
- Dropdowns only for short stable lists; long lists → searchable
  select (ux/search-discovery.md); country/city → typeahead with
  Arabic aliases (rtl/arabic-ux.md).
- Numeric: allow locale digits (Arabic-Indic input accepted, normalized
  or preserved per product policy — rtl/cross-platform.md).

## Multi-step forms (progress + trust)

Progress indicator with named steps (Booking → Payment → Review);
step-validation before advance; full review screen before submit
(money movement: crypto-web3.md preview rule); autosave drafts +
resume (interruption survival — mobile-states.md); back never loses
data.

## Recovery & edge flows

- Duplicate-submit protection (disabled-with-progress state).
- Timeout/re-auth mid-form (KYC, banking): re-auth RETURNS to the form
  intact (WCAG 3.3.8 accessible authentication: no cognitive test on
  re-entry where avoidable `[PLATFORM RULE]`).
- Redundant entry: don't re-ask known info (WCAG 3.3.7 `[PLATFORM
  RULE]`); auto-complete from account/session.
- Save-failure honesty: "saved locally, retry" beats silent loss.

## QA

[ ] three-gate validation [ ] errors visible+constructive [ ] input
survives every failure [ ] keyboard/mask/paste sane [ ] steps +
progress + review [ ] autosave/resume [ ] re-auth round-trip [ ]
screen-reader announced [ ] requiredness explicit [ ] RTL masks/align
correct
