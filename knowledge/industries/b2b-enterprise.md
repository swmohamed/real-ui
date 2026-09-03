# Industry: B2B Enterprise, Consulting, Industrial, Logistics, Telecom, Energy

V2 depth: consumer shipment tracking/delivery UX → logistics-delivery.md.
V7.4: consumer telco shops → telecom.md. Agriculture OEM/IR stays here
(rejected as its own category).

## Characteristics
Long sales cycles, committee decisions, credibility-first. The website's job:
not to close, but to qualify and open conversations (leads, RFPs). Content
depth signals competence; case studies + whitepapers are the currency.

## User intents
1. Assess capability (can they actually do this?)
2. Evidence: clients, results, scale, certifications
3. Understand solutions by industry/function
4. Download research / register for events (lead capture)
5. Contact sales / find offices

## Business goals
Qualified leads (forms, gated content), brand authority, recruiting,
investor confidence (public companies).

## Candidate information-architecture patterns (not a product sitemap)
- Home: positioning statement + proof (clients/logos, numbers) + flagship
  insight (report/POV) + solutions overview + CTA (Talk to us)
- Solutions by industry × function matrices; services pages with depth
- Insights/Research hub (articles, reports, events)
- Case studies with metrics; About (leadership, history, values);
  Careers (heavy traffic section); Investors; Contact/office finder
- Telecom adds: consumer + enterprise split (stc OBSERVED: consumer shop +
  enterprise trees, 612 links — portal density)

## Navigation
- 2-tier: Industries / Services / Insights / About + persistent CTA
- Mega-menus with curated featured content (report promo inside menu)
- IBM OBSERVED: Carbon design system maturity — enterprise DS as brand
- Consulting OBSERVED (Deloitte): dense global/office/language switchers

## Candidate components observed in the genre
- Statement heroes (typographic, one POV, zero stock chaos)
- Logo walls + quantified proof bars ("$X B advised, 40 countries")
- Case study cards with client + metric + sector chips
- Gated content forms (email → PDF) with honest value exchange
- Leadership grids (portrait + credential); history timelines
- Office finders, RFP/contact forms with routing
- Telecom consumer side: plan cards, coverage maps, device shop (hybrid
  commerce patterns from ecommerce-marketplace.md apply)

## Visual characteristics (OBSERVED)
- Two viable registers: (a) corporate classic — navy/white, serif-or-clean
  sans, 0–8px radius, photography of real operations (Deloitte, GE, banks);
  (b) design-system modern — IBM Carbon gray-90/white/blue-60 tokens,
  mono accents, 0 radius brutalist precision
- Logistics/industrial: bold operational colors (Maersk blue, FedEx purple/
  orange), schedule-tables, tracking widgets = the utility moment
- Avoid: SaaS-playful illustration on heavy-industry trust surfaces
- Radius discipline tight (0–8px); shadows minimal; photography of real
  assets (ships, plants, people-at-work) over abstractions

## Interaction patterns
- Multi-step lead forms with progressive profiling (ask little, then more)
- Content gating with instant email verify + PDF streaming
- Tracking/quote tools embedded (logistics calculators)
- Events: agenda/registration flows; webinars gated
- Language/office localization (enterprise sites are country-matrixes)

## Mobile patterns
- Executives read on phones: insights typography must be excellent mobile
- Sticky "Contact" CTAs; click-to-call offices
- Forms split across steps (never 20 fields on one mobile screen)

## Arabic/MENA considerations (OBSERVED stc, Emirates NBD-class enterprise)
- stc OBSERVED: Arabic-first with full RTL, Font Awesome icon set (legacy
  enterprise pattern), section-link trees in headers, family-plan commerce
- B2B Arabic: bilingual capability decks, ISO/quality badges, royal/
  government client references where publishable
- Consulting/telecom mix Arabic marketing + English deliverables (documents
  often EN) — site should manage register shifts gracefully
- Government-tender visibility (procurement pages) — regional B2B channel

## Conventions to evaluate (adopt only when model-supported)
Statement typography, proof bars with real numbers, case studies with
metrics, gated research with fair exchange, office/global footers,
leadership pages, newsletter hubs, investor sections.

## Overused/anti-patterns
- Meaningless synergy sliders/carousels of stock handshakes
- "Solutions" pages that are feature lists without outcomes
- PDFs as the only content format (gate analytics + a11y)
- 7-field forms before any value delivered
- Copycat-IBM design without IBM's system discipline

## Strong references
IBM (Carbon OBSERVED class), Salesforce, HubSpot, Deloitte, Maersk, Shell,
GE, Verizon, FedEx, Uber (B2B side), stc (AR OBSERVED), Unifonic (AR OBSERVED).

## Contextual decision prompts
Pick register by audience age/sector: classic-corporate for legacy
industries, system-modern for tech-adjacent. Either way: proof density,
statement typography, disciplined forms, real photography. MENA adds
bilingual enterprise depth + telecom-style consumer portals.

## Corpus observations (v7.1 growth: 7+ products SOURCE-OBSERVED 2026-09-03)

Observed families: ops/observability (grafana, pagerduty: product-led,
docs+demo led) - data platforms (snowflake: solution/industry marketing
trees) - identity/security (okta: trust + compliance first) - work
management suites (smartsheet, workday, servicenow: suite breadth
marketing, mega-navs) - dev-collab (atlassian: product family hub).
WHY: enterprise purchase cycle surfaces = solution maps, compliance
proof, and demo gates - not consumer CTAs. Suite breadth produces
mega-navigation (observed across workday/servicenow) - legitimate when
the catalog genuinely spans functions. WHEN NOT: consumer-grade
single-CTA landing on a suite product hides the catalog; suite mega-navs
on a single-purpose tool fake breadth.

## Strict-audit additions (v7.2 knowledge integration, SOURCE-OBSERVED 2026-09-03)

Wave 9 added a GTM / product-analytics cluster that the v7.1 suite/observability
families do not cover. These are still B2B, but the buyer and the artifact differ.

| Family | Observed shape | WHY | WHEN | WHEN NOT | TRADEOFF |
|---|---|---|---|---|---|
| Revenue/sales engagement (gong Pricing/demo; outreach Why/vs-competition; apollo Outbound/Inbound/Data/AI; clay Product/Pricing/demo) | problem-tree nav + demo/pricing/login | buyer is a revenue team; the artifact is pipeline/calls/data | sales-ops tools | IT observability or HR suites | competitor-comparison pages are legitimate here; they read desperate on a data warehouse |
| Product analytics (amplitude Product Analytics + agents; mixpanel Pricing/Get Started Free; pendo Start for free / Get a Demo) | product-led free-start + demo | buyer is a product team; the artifact is event data | product intelligence | sales engagement (free-start on Gong-class can underplay enterprise procurement) | self-serve onboarding vs demo-gate: pick from sales motion, not aesthetics |
| Lifecycle CRM / forms (klaviyo email/SMS/CDP tree; activecampaign Marketing Automation; typeform Platform/AI/Flows) | channel or flow catalog | the product is a system of campaigns or forms | marketing ops | sales-call intelligence | mega-nav is earned when the catalog is real; fake breadth copies Workday poorly |

WHEN NOT to reuse v7.1 families: Workday/ServiceNow mega-navs on a single-purpose
analytics tool fake a suite; Grafana docs-led density on a sales-engagement
marketer landing hides ROI proof.

## Corpus observations (v7.3 diversity, SOURCE-OBSERVED 2026-09-03)

| Family | Observed shape | WHY | WHEN | WHEN NOT | TRADEOFF |
|---|---|---|---|---|---|
| Consumer-finance B2B edges (mercado-pago cuenta / pesos / dolares / tarjeta / linea de credito, es-AR) | wallet language on a payments company | LatAm payments sit between consumer wallet and merchant acquire | regional acquirers | Salesforce suite mega-nav | |
| Work platforms (monday.com AI Work Platform, 2 forms) | work OS marketing | the artifact is the board/workflow | work management | sales-engagement Gong-class | |

## Corpus observations (v7.4 rejected agriculture category, SOURCE-OBSERVED 2026-09-03)

Agriculture was researched as a candidate (wave 20: 10 fetch-ok). The set
splits OEM/IR, farm SaaS, and a government portal — not one industry module.
Consumer telco shops moved to `telecom.md`. Energy group IR stays adjacent.

| Family | Observed shape | WHY | WHEN | WHEN NOT | TRADEOFF |
|---|---|---|---|---|---|
| Ag OEM / group IR (deere empty shell; corteva Who We Are; syngenta Company/Agriculture; yara Crop nutrition; nutrien Potash/Nitrogen/Retail; mahindra Purpose Led conglomerate; agco Fendt/Massey/Valtra brands) | brand portfolio + investor/purpose | the public site sells equipment or the group | industrial OEM | Cropin-class farm SaaS or farmers.gov | a quote-engine on Deere IR hides dealers; Salesforce mega-nav on Yara hides crop nutrition |
| Farm software (cropin AI platform / Apps / Datahub; climate-fieldview data-driven insights) | product + pricing/demo | the buyer is a grower or agribusiness | agtech SaaS | tractor IR | |

farmers.gov is a civic task portal — see government-public.md. Do not
average it with John Deere.
