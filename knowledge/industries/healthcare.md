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

## Information architecture
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

## Components that define the genre
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
- Click-to-call everywhere (anxious users phone more)
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

## Conventions (follow)
Plain-language content schema, search-first with A–Z fallback, appointment
wizards, real-staff photography, accessibility floor above commercial sites,
emergency exits everywhere, verified-badges on clinical claims.

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
(OBSERVED — pharmacy retail hybrid), Sehha/MOH portals (INFERRED — verify in
Deep Mode).

## Decision guidance
Calm blue/green system, humanist type, big readable body, structured
clinical schemas, search+A–Z, real photography, elevated a11y floor. Design
for the most anxious user in the room.
