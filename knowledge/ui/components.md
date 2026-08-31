# UI Components: Atoms (Buttons, Inputs, Chips, Badges, Avatars, Feedback)

Component anatomy with real-world conventions. States first — an atom
without states is a mockup.

## Buttons

- Heights: 32 (sm) / 40 (md) / 48 (lg touch-recommended) / 56 (xl primary touch);
  padding symmetric 16–24px horizontal; radius follows system (pills for
  consumer/playful, 4–8px for professional)
- Hierarchy: **primary** (filled brand — 1 per view), **secondary**
  (outline/ghost), **tertiary** (text link), **destructive** (danger fill
  or outline+confirm). Icon buttons: prefer a 40–48px hit area with an
  accessible name; web WCAG 2.2 AA minimum is 24×24 CSS px or a documented
  exception/spacing path (accessibility/floor.md)
- States: default → hover (bg shift 8%) → active (shift 12%/scale .98) →
  focus-visible (2px ring offset) → loading (spinner, label stays, width
  locked) → disabled (40% opacity, no shadow, cursor not-allowed) →
  selected (for toggles)
- Content: verb + object ("Save changes", احفظ التغييرات); sentence case
  (Latin) / natural Arabic; icons optional lead/start position; never
  "Submit"/"OK"
- RTL: icon positions flip with direction; button text-align center always

## Inputs

- Height 40–48 (mobile/touch preferably ≥44); label always visible (above, 13–14px medium);
  helper text below (12–13px); placeholder = example not label
- Types: tel (country selector + LTR), email (ltr+lowercase hint), password
  (reveal toggle + caps-lock hint), number→ inputmode=decimal with units
  suffix, search (clear button + icon start)
- States: default → focus (ring + border) → filled → error (border red +
  message + icon) → success (check when verified) → disabled; readonly
  styled differently from disabled
- Prefix/suffix slots (currency ر.س, %, kg); textarea autosize with max
- Autocomplete tokens + name attributes — the free a11y/conversion win

## Chips, tags, badges

- Filter chips: toggleable, count optional, removable × when applied
- Status badges: dot + label + color (success/warn/error/info/neutral) —
  never color-only; consistent across every product surface
- Count badges: max "99+", positioned corner-end; cart/notifications
- NEW/HOT/SALE flags: corner ribbon or pill, restrained palette

## Avatars & identity

- Sizes 24/32/40/48; initials fallback (brand-derived colors), presence
  dot (online/busy) at corner-end; group avatars stacked +N

## Tooltips & popovers

- Tooltips: label clarification only (not actions), delay 300–500ms,
  dismiss on Esc/blur, never on touch-only (use long-press or inline hint)
- Popovers: keyboard reachable, dismissible with Esc, sensible initial focus,
  and focus returned to the trigger when dismissal would otherwise lose it;
  non-modal popovers do not trap focus
- Menus: focus enters the first/selected item, arrow keys move among items,
  Esc closes, and Tab leaves/closes according to the chosen APG pattern;
  positioning uses collision flipping (RTL-aware start/end)

## Toasts & snackbars

- Bottom-start (mobile bottom-center above tab bar); single-line + action;
  auto-dismiss 4–6s (errors persist); queue without stacking >2; undo
  pattern for destructive actions

## Modals & dialogs

- Rule: modal = interruption justified (confirm destruction, focused
  single task, required decision). Everything else = drawer/inline
- Sizes: sm 400 / md 560 / lg 720; focus trap + return; scrim click closes
  (unless dirty form); Esc; title + body + actions (primary end-aligned)
- Native `<dialog>` acceptable (6% and growing in corpus) with fallback

## Anti-patterns

- Ghost buttons on ghost backgrounds; 1px touch targets; hover-only
  affordances; spinners replacing labels (width jumps); tooltips holding
  critical info; modal-in-modal
