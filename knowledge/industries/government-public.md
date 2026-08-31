# Industry: Government, Legal, Public Sector, Nonprofit

## Characteristics
Service delivery, not persuasion. Users are captive (they MUST complete
tasks: renew, pay, apply) so design debt becomes civic harm. The reference
standard is GDS (gov.uk): content design + task-first forms + zero chrome.

## User intents
1. Complete a task (renew license, pay fine, book appointment, register)
2. Find authoritative information (rules, benefits, hours, forms)
3. Verify authenticity (is this official?)
4. Contact the right department
5. Nonprofit: donate / volunteer / verify impact

## Business goals
Task completion rates (measured publicly on GOV.UK), reduced call-center
load, digital-adoption targets, transparency mandates, donation conversion.

## Information architecture
- Topic/task-based IA (not department mirrors!): "Renew a passport", not
  "Directorate of Travel Documents" — GDS's core insight
- Home: search-first + popular tasks grid + alerts/notices strip
- Step-by-step guides (one page per task with steps, eligibility, time,
  cost boxes)
- A–Z of services; department directories secondary
- UAE portal OBSERVED (u.ae/ar): Bootstrap+Tailwind hybrid, 183+ links,
  mega-service trees, bilingual

## Navigation
- Search-first header + task links; language toggle AR/EN top-right
  (MENA standard)
- Breadcrumb-heavy deep trees; footer with legal/privacy/accessibility
  statements (legally required in many jurisdictions)

## Components that define the genre
- Task cards/grid (icon + verb-first label: "Renew", "Apply", "Pay")
- Step-by-step content pages with "What you'll need" boxes, time/cost facts
- Forms: one-thing-per-page pattern (GDS), inline validation, save-progress
- Notice/alert banners (emergency, maintenance) with explicit dismiss rules
- Facts/statistics blocks (nonprofit impact: numbers with sources + dates)
- Document downloads with format/size metadata (PDF accessibility honesty)
- Consultation/legal comment flows (published responses = transparency)

## Visual characteristics (OBSERVED)
- gov.uk: GDS Transport type, #1d70b8 link blue, black text on white, focus
  yellow — the highest-legibility convention set; radius 0–4px
- Institutional MENA: national flag palettes (UAE portal greens/golds,
  Saudi portals green), formal serifs or Naskh Arabic, emblem/logo lockups
- Zero decorative gradients/glass/3D — decoration reads as unserious
- Dense link lists are LEGITIMATE here (users scan for their task words)

## Interaction patterns
- Session-save + resume on long forms; reference numbers on completion
- Status trackers for applications (submitted → processing → decision)
- Multilingual parity: every task exists in all official languages
  (Arabic-first in MENA — Arabic is the legal reference language)
- Accessibility toolbars (text-size, contrast) on public-sector sites —
  common and expected
- Payment integrations (government gateways) with receipt PDFs

## Mobile patterns
- Task-first single columns; SMS/OTP verification flows
- Government app deep-links (Absher/Tawakkalna class — app-first ecosystem
  in KSA; web = entry + info)
- Click-to-call department finders

## Arabic/MENA considerations (OBSERVED u.ae/ar, visitsaudi/ar)
- Arabic-first with complete EN parity; legal language in MSA; RTL forms
  with correct input direction mixing (English names LTR fields inside RTL
  pages — `dir="ltr"` on specific fields!)
- National identity: emblems, flag colors, rulers' imagery conventions
  (respect formal protocol)
- Service counters: branch locator + queue booking (EIDA/class services)
- Umrah/Hajj, zakat calculators, labor-law services = region-specific task
  verticals with dedicated portals (verify current landscape in Deep Mode)

## Conventions (follow)
Verb-first task IA, one-thing-per-page forms, search-first, bilingual
parity, notice banners, reference numbers, print-friendly pages (government
users print!), accessibility statements, zero marketing gloss.

## Overused/anti-patterns
- PDF-only services (the classic government failure)
- Department-structure mirrors instead of task structure
- Stock-photo politicians/handshakes on every page
- Chatbots that block human contact paths
- Dark patterns in fine payments (obfuscated appeal rights)

## Strong references
gov.uk (OBSERVED — the global canon), USAGov, canada.ca, europa.eu
(OBSERVED), u.ae (AR OBSERVED), VisitSaudi (AR OBSERVED), UN, Red Cross,
Kiva (nonprofit donation UX OBSERVED).

## Decision guidance
Adopt GDS-class discipline: content design, task verbs, one-thing-per-page,
maximum contrast, bilingual/RTL parity. Add national identity through
controlled brand elements (emblem, one color), never through decoration.
