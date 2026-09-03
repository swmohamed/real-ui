# Industry: Government, Legal, Public Sector, Nonprofit

V7.4: consumer telecom shops → telecom.md. Legal research and donation
platforms remain families here; they did not earn separate categories.

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

## Candidate information-architecture patterns (not a product sitemap)
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

## Candidate components observed in the genre
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
  verticals with dedicated portals (verify the current landscape with targeted
  research when needed)

## Conventions to evaluate (adopt only when model-supported)
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

## Contextual decision prompts
Adopt GDS-class discipline: content design, task verbs, one-thing-per-page,
maximum contrast, bilingual/RTL parity. Add national identity through
controlled brand elements (emblem, one color), never through decoration.

## Corpus observations (v7.1 growth: 11 additional products SOURCE-OBSERVED 2026-09-03)

Government is NOT one pattern — four observed families:

| Family (n) | Observed shape | Why it differs | When / when NOT |
|---|---|---|---|
| Service portals (usa.gov, canada.ca, singapore.gov.sg, gov.ie) | task/topic-first: search + topic grids + "all services" entry (10 h2) | residents complete tasks; routing is the job | citizen service; NOT country branding |
| National portals (suomi.fi: 4-audience nav — citizen/business/authorities) | audience-split navigation | obligations differ by actor | multi-actor states |
| Country brands (germany.de, australia.gov.au) | editorial news/politics/life/culture; magazine rhythm | audience = world, not residents | soft-power communication; NOT service delivery |
| Service gateways (jordan.gov.jo RTL, hukoomi Qatar, bahrain.bh) | RTL service directories with deep transaction trees; heavy form entry points | digital-government transactions per ministry | MENA gateways; bilingual parity legally required |

WHY: the reader defines the surface (resident task vs international
audience vs transaction citizen). WHEN NOT: never apply country-brand
editorial rhythm to a service portal (routing degrades); never apply task
grid sparseness to a transaction gateway (users need entry density).
The GDS discipline in the corpus remains the service-portal reference;
national-brand sites legitimately break it.

## Strict-audit additions (v7.2 knowledge integration, SOURCE-OBSERVED 2026-09-03)

| Family | Observed shape | WHY | WHEN | WHEN NOT | TRADEOFF |
|---|---|---|---|---|---|
| Government communications / PR (gov-jp: media-by-channel nav — TV, radio, ads, audio CD, braille/large-print) | channel and format as IA, including accessible publications | the job is explaining policy to the public, not completing a transaction | gov publicity offices | service portals and tax gateways | task-grid sparseness on a comms site hides the campaign library; magazine country-brand chrome on a tax gateway hides the form |
| Service portals confirmed (govt.nz welcome; india.gov.in national portal, 10 h2 + table) | resident routing, high heading count | same family as usa.gov/canada.ca | citizen service | PR/media offices | |

ALTERNATIVES: if a government site both explains and transacts, keep
services as the persistent object and treat campaigns as a desk — do not
average into a lifestyle magazine. poland.gov remained fetch-failed.

## Corpus observations (v7.3 diversity, SOURCE-OBSERVED 2026-09-03)

| Family | Observed shape | WHY | WHEN | WHEN NOT | TRADEOFF |
|---|---|---|---|---|---|
| Citizen-engagement platforms (mygov.in Platform for Citizen Engagement, 10 h2 / 3 forms) | participate/consult, not pay-a-fine | the job is talking to government, not completing a statutory task | engagement portals | tax/license gateways | task-grid sparseness on MyGov hides campaigns; magazine country-brand on a fine-payment gateway hides the form |
| Multi-audience service homes (gov.za Residents / Business / Foreign Nationals / Online Services; gov.br skip-links to content/menu/search/map; gov.sg) | actor split + skip-link discipline | obligations differ by resident vs foreigner vs firm | national service portals | PR/media offices | |

## Corpus observations (v7.4 rejected-category families, SOURCE-OBSERVED 2026-09-03)

Legal and nonprofit were researched as candidate categories (waves 14, 18)
and rejected: they are not one design space. Store the splits here.
Consumer telco shops moved to `telecom.md`.

| Family | Observed shape | WHY | WHEN | WHEN NOT | TRADEOFF |
|---|---|---|---|---|---|
| Law as public text (lii-cornell Welcome to LII; legislation.gov.uk Search Legislation; kenyalaw Case Law / Laws of Kenya; moj-sa RTL e-services; adala-ma البوابة القانونية; uspto America's Innovation Agency; epo Patent knowledge; wipo; icj; courtlistener search) | search/browse statutes, cases, or filings | the object is an authoritative document, not a quote or a donate CTA | official/legal-info portals | law-firm SaaS or consumer LLC wizards | GDS task-grids on LII hide the corpus; LegalZoom chrome on legislation.gov.uk hides the Act |
| Humanitarian / donation orgs (unhcr Donate + language; oxfam campaigns; msf Where we work; save-the-children MATCH ALERT; islamic-relief / ksrelief / qcharity RTL zakat; gofundme / justgiving / donorschoose / globalgiving / givedirectly; amnesty / hrw; habitat; wfp; brac; human-appeal 133 inputs) | appeal + impact + give, sometimes crisis-first | the job is sending money or taking action, not completing a statutory form | charities and crowdfunding | license/tax gateways or consumer insurance | gov.uk one-thing-per-page on a crisis appeal hides urgency; a donate mega-CTA on a passport form is civic harm |
| Professional-body comms (lawsoc-uk Find a Solicitor / campaigns) | membership + public legal help | the visitor is a solicitor or a citizen finding one | bar/law societies | court-filing portals | |

ALTERNATIVES: civic task grid, statute search, donate/appeal, professional body.
Practice-management (MyCase/Smokeball/Filevine) and consumer legal docs
(LegalZoom/Rocket Lawyer) live in `saas-dev.md`. Do not create a "legal"
category that averages those with MOJ portals.
