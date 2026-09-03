# Industry: Healthcare, Medical, Pharma Retail

## Characteristics
Anxiety-reducing design. Users seek reassurance + accuracy; clarity is care.
Medical trust = institutional calm, not marketing gloss. Accessibility
audiences skew older/disabled — design floor must rise.

## User intents
1. Check symptoms / condition info (health literacy mode)
2. Find a service/doctor/clinic (directories, appointment booking)
3. Access records/results (patient portals)
4. Buy pharmacy items (retail mode)
5. Trust the institution (donate, careers, about)

## Business goals
Appointments booked, patient acquisition (private), public health outcomes
(public), pharmacy conversion, donor/career pipelines.

## Candidate information-architecture patterns (not a product sitemap)
- Public: Home (services A–Z, urgent-care strip, search) → Condition/treatment
  content hub → Find-a-doctor/clinic directory → Appointment booking →
  Patient portal → About/insurance
- Content pages follow clinical structure: overview, symptoms, causes,
  diagnosis, treatment, when-to-see-doctor — consistent schema ( Mayo/
  NHS pattern family)
- Pharmacy retail: symptoms-based browse + product categories

## Navigation
- Big friendly search ("Search conditions/services"), A–Z indexes, services
  by body-system or specialty groups; NHS OBSERVED: GDS-adjacent patterns,
  blue system, Frutiger-class humanist, arrow-link list components
- Persistent urgent/emergency strip (111/999-style triage links)

## Candidate components observed in the genre
- Symptom/service search with plain-language synonyms (lay terms → clinical)
- A–Z directory lists (disease index pattern)
- Appointment wizards: specialty → doctor → slot grid → details → confirm
- Doctor cards: photo, specialty, languages, next-available slot
- Accordion clinical content (symptoms/causes/treatment sections)
- Trust strips: accreditations, stats (years, patients), insurer logos
- Medicine/product cards with dosage selector, pharmacist-verified badges

## Visual characteristics
- Calm institutional: NHS blues, whites, greens; zero gradient chrome;
  radius 2–8px; generous readable body (16–18px, 1.6 line-height)
- Humanist type (Frutiger W01 OBSERVED on NHS) beats geometric cold
- Photography: real staff/patients (consented), diverse, warm — never stock-
  smiley
- Wayfinding color coding for departments/hospitals (public institutions)

## Interaction patterns
- Triage flows with safety exits (if emergency, call… — prominent)
- Slot grids with timezone/session clarity; reschedule/cancel self-service
- Portal: results with plain-language explainers, secure messaging
- Pharmacy: refill tracking, substitution opt-ins (generic ↔ brand)

## Mobile patterns
- Keep an in-scope urgent phone/contact path easy to find; do not invent phone
  support or duplicate it indiscriminately
- Large touch targets (44–56px) — older audiences
- Content pages with text-size adjusters; dark-mode not a priority vs contrast

## Arabic/MENA considerations
- Ministry/insurance directories dominate (bilingual), hospital sites EN/AR
  with doctor-name Latin+Arabic
- Clinical content in MSA (formal register = trust); dialect for service
  warmth in marketing layers
- Gender considerations: doctor gender filters matter operationally in the
  region (patient preference is a real appointment criterion)
- Hijri/Gregorian scheduling; Ramadan clinic hours
- Insurance card (تأمين) verification UX — card scanning common

## Conventions to evaluate (adopt only when model-supported)
Plain-language content schema, search-first with A–Z fallback, appointment
wizards, real-staff photography, accessibility floor above commercial sites,
clear urgent-help exits where clinically relevant; clinical verification must
come from real governance/content evidence, never a fabricated badge.

## Overused/anti-patterns
- Marketing gloss/gradients on clinical surfaces (trust inversion)
- Tiny gray body text on health content (older readers!)
- Stock-photo stethoscope clichés; condition pages without "when to seek
  urgent help"
- Dark-mode-only patient portals
- Diagnosis chatbots without clinical disclaimers and exits

## Strong references
NHS (OBSERVED — pattern library public), Mayo Clinic (INFERRED — blocked),
WHO (OBSERVED), Cleveland/Johns Hopkins class (INFERRED), Walgreens
(OBSERVED — pharmacy retail hybrid), Sehha/MOH portals (INFERRED — verify with
targeted current research when the reference matters).

## Contextual decision prompts
Calm blue/green system, humanist type, big readable body, structured
clinical schemas, search+A–Z, real photography, elevated a11y floor. Design
for the most anxious user in the room.

## Strict-audit additions (v7.2, SOURCE-OBSERVED 2026-09-03)

Healthcare is multiple product families. A calm clinical homepage is not the
default.

| Family | Observed shape | WHY | WHEN | WHEN NOT | TRADEOFF |
|---|---|---|---|---|---|
| Visit-flow telehealth (teladoc, livi) | who / when / coverage before services prose; sparse h2 on livi, denser product tree on teladoc | the job is starting a visit, not browsing a hospital | booked or on-demand care | encyclopedia or pharmacy-price products | coverage honesty slows marketing copy; hiding it destroys trust |
| Symptom-checker (ada: Medical library + App, 2 h2) | one conversational entry, progressive disclosure, disclaimer from step one | users arrive with a question, not a department | self-triage utilities | replacing a clinician directory or visit booking | a checker without an exit to real care is a liability |
| Therapist/directory (psychologytoday: Find a Therapist / Psychiatrists / Treatment Centers; 4 forms) | search-first directory, filters as the product | matching a person is the conversion | find-a-provider | visit-flow telehealth (directory chrome hides booking) | editorial articles (psychologytoday) support trust but must not bury search |
| Drug-cost comparison (goodrx: Prescription savings + pharmacy search) | price-first cards per pharmacy, coupon CTA | payer-transparent cost is the trust object | cash-pay / coupon pharmacy | provider or insurer homepages | showing a coupon as "the price" without pharmacy name is a trust fail |
| Condition encyclopedia (verywellhealth A-Z, everydayhealth, drugs.com) | topic IA, body-copy first | reading is the job | editorial health publishers | transactional care products | dense medical prose needs larger type, not marketing cards |
| MENA care (seha hospitals: 5 forms/12 inputs; shezlong teletherapy shell) | appointment/contact-heavy hospital vs thin teletherapy marketing | regional products split clinical-ops vs app-distribution | match the actual job | importing US telehealth chrome onto a hospital locator | bilingual/RTL is a product decision, not a skin |

ALTERNATIVES: if the product is both encyclopedia AND booking, keep search as
the persistent object and treat articles as support — do not average into a
services-card grid.

## Corpus observations (v7.3 diversity, SOURCE-OBSERVED 2026-09-03)

| Family | Observed shape | WHY | WHEN | WHEN NOT | TRADEOFF |
|---|---|---|---|---|---|
| Care + pharmacy + lab bundles (apollo247 Online Doctor + Book Lab Tests; halodoc Beli Obat / Tanya Dokter / Cek Lab, ID) | three entry verbs on one home | users in these markets mix consult, meds, and diagnostics in one session | bundled care apps | a US encyclopedia or a coupon-price index | a GoodRx price grid on Halodoc hides the doctor; a hospital visit-flow on a pharmacy bundle hides SKUs |
| Public encyclopedia (medlineplus NLM; webmd condition A-Z nav) | topic IA, institution or publisher | reading and triage language, not booking | health publishers | transactional bundles | |
| Health conglomerate (cvshealth: Aetna / Caremark / Pharmacy / Investors) | brand-family nav | several legal entities share a group site | holding / IR + consumer entry | a single clinic | |

Netmeds returned a thin pharmacy shell — do not invent a catalogue from it.
