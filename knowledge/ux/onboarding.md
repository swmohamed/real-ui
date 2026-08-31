# UX: Onboarding & Activation

Onboarding = the path from arrival to first value ("aha"). Activation
metric defined first; UI second.

## The three onboarding schools

1. **Zero-onboarding** (consumer utilities): value before signup; account
   created opportunistically (save-progress prompts). Poki/browser-games
   class: play first, nothing asked.
2. **Guided setup** (tools/SaaS): 3–5 steps max — goal selection →
   template/import → invite (skippable) → done. Skippable at every step;
   progress preserved.
3. **Compliance onboarding** (fintech/health): KYC/regulatory steps that
   cannot be skipped — make them fast and honest: step indicator, document
   previews, in-progress save, resume links, clear failure states with
   rephoto/redo guidance.

## Rules

- Show the product doing something real in step ≤2 (template with their
  data, sample dashboard, preview generation)
- Ask for data when needed, not upfront (progressive profiling); every
  field justified by the value it unlocks
- Empty states continue onboarding (first-task CTAs)
- Activation checklist widget (advanced tools): 4–6 setup tasks with
   progress (Notion/Intercom-class pattern — effective and honest)
- Skip everything: "skip tour" on tours; tooltips max 3, dismissible,
   never modal-locked
- Welcome email = onboarding step 1 of the product (task link deep into
  first value)

## Mobile onboarding

- 2–3 permission asks max, each with pre-permission rationale screen
  (camera → "scan your ID"), never on splash
- Carousels of value props: max 3 slides, skippable, no fake dots-only
  progress
- Biometric/pin setup deferred until value established

## Arabic/MENA onboarding

- Language selection as first-citizen step (default from locale, changeable
  — never lock to GPS default silently)
- Phone-first signups (+966/+971/+20 selectors), OTP via SMS/WhatsApp
- Dual-script names (legal Arabic name + preferred Latin display name)
- Family/group account patterns in some products (shared plans)

## Activation measurement (the design loop)

Define: X did Y within Z days. Instrument the funnel; onboarding changes
ship as experiments. UI patterns that can't be measured can't claim to
"improve activation."

## Anti-patterns

- 12-step wizards for a to-do app
- Product tours before the product appears
- Blocking value behind profile completion percentage
- Email verification walls before first use (verify async, allow preview)
- Asking for payment during trial signup without clear trial terms
