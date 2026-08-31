# Page Types: Account, Settings, Forms & Utility Pages

(Profile, Settings, Contact, About, Legal)

## Profile & account pages

- Identity block: avatar (upload with crop), name, role/status, meta
- Tabs/sections: Personal info, Security, Notifications, Billing, Connected
  apps, Sessions/devices, Danger zone (delete account — honest but
  protected)
- Show state, not just settings: active plan, last login, connected
  services with statuses

## Settings UX rules

- Save behavior: explicit Save per section (with dirty-state indicator) or
  instant-save with undo toasts — never both patterns mixed
- Search within settings (large products) — "find a setting" beats nav trees
- Toggle rows: label + description + switch + state feedback; destructive
  toggles require confirm
- Notification matrix (channel × event) over long checkbox lists

## Form craft (applies everywhere)

- One column beats two for comprehension; group related sets; logical tab
  order = visual order
- Labels above fields (not placeholders-as-labels); optional fields marked
  "(optional)", required unmarked (default assumption)
- Field types: correct keyboards (tel/email/number), autocomplete tokens
  (name, email, cc-number…), inputmode for numeric
- Validation: on blur first, on submit complete; success states too
  (green check on available username)
- Errors: summary for long forms (anchor links), field-level messages
  persistent until fixed, aria-live announcements
- Buttons: primary right/end-aligned; loading state disables + spinner +
  label ("Processing…"); double-submit prevention

## Contact page

- Route-first: purpose selector (support/sales/press) → tailored forms or
  direct info (email, phone with hours/timezone, WhatsApp in MENA)
- Real address + map + department routing; response-time expectation
  ("we reply within 1 business day")

## About page

- Story (short, human), team grid (real photos + roles), timeline,
  numbers-with-dates, press kit link, careers CTA
- Register: earnest beats clever for trust surfaces

## Legal pages (Privacy, Terms, Cookies)

- Readability floor: 16px body, generous measure, real headings hierarchy,
  TOC sidebar with scroll-spy for long docs
- Plain-language summaries at top (increasingly a legal expectation —
  GDPR/CCPA pattern), key tables (what data/why/retention)
- Version history + effective dates; print/PDF friendly

## RTL/Arabic

- Form direction: page RTL, but mixed-data fields (emails, card numbers,
  URLs) get dir="ltr" + text-align kept sensible
- Arabic labels with English terms inline (technical vocabulary often
  untranslated — البريد الإلكتروني fine; API keys stay Latin)
- Phone fields: country code selector + LTR number field; Saudi/EG/UAE
  formats (+966 5X XXX XXXX)
- Date inputs: Gregorian (default) or Hijri per product; dual display for
  official contexts

## Anti-patterns

- Placeholder-only labels; settings without dirty-state feedback
- Email-only contact walls (provide phone/chat where operationally true)
- Legal pages as scanned PDFs
- Captcha before any human contact
- Save buttons at page bottom only for 10-section forms (per-section save)
