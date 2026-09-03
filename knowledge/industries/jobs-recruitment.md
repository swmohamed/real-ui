# Industry: Jobs & Recruitment (Job Boards, Hiring Platforms)

Evidence: v2 fetch 2025-08 `[OBSERVED]` — bayt.com (MENA leader),
wuzzuf.net (Egypt leader). Complements social-community.md (profiles/
communities) and saas-dev.md (ATS/enterprise tooling).

V7.4: booking a cleaner or tradesperson is local-services.md, not a job
board. Distinguish employment from a one-off local task.

Apply `industries/README.md`. Distinguish a public job board, candidate
tracker, employer ATS, recruitment agency site, and community product. Search,
profiles, alerts, easy-apply, employer tooling, subscriptions, and status
tracking all require scope evidence.

## Observed design languages

- Bayt: Roboto + **Vazirmatn** (Arabic-capable Latin font — bilingual
  stack in ONE family system) `[OBSERVED]`; minimal breakpoints
  (1023/1024) — simple two-state adaptive.
- Wuzzuf: Open Sans + **IBM Plex Sans Arabic** `[OBSERVED]`;
  Bootstrap-class breakpoint spread (575/576, 991/992, 1159/1160) —
  utility-first, dense mobile bp set.

## Conditional domain patterns and questions

1. **For broad public job boards**, keyword + location was prominent in both
   sampled products' source. Do not transfer a search-first homepage to an
   ATS, agency, or narrow campaign site without a matching top task.
2. Job card = structured data contract: title, company (logo),
   location, salary band if available, posted-date freshness, easy-
   apply/featured badges `[OBSERVED - bayt card anatomy]`. Salary
   display: MENA boards show bands more often than Western (trust +
   regulation-adjacent habit) `[INFERRED - corpus pattern]`.
3. Two-pane results on desktop (list ↔ detail), stacked + sheet/detail
   push on mobile (responsive/adaptive-models.md).
4. Where real data exposes them, filters may include experience level, career level, company, remote,
   salary, date-posted; filter chips visible + count badges; saved
   searches + alerts (email/push) are retention features, design them
   as first-class.
5. Application flow: short path wins (easy-apply 1–2 steps); CV-first
   UX (upload once, autofill forms); application status tracker
   (applied/viewed/rejected) — candidate anxiety is the design problem
   (honest silence > fake hope) `[DESIGN PRINCIPLE]`.
6. Profile completeness meter (bayt `[OBSERVED]`) — gamified CV
   completion; skills tests/certificates as profile signals.
7. Trust: verified-company badges, employer pages (culture/photos/
   reviews), scam-reporting affordance; MENA: company size + nationality
   hiring notes handled respectfully per market norms.

## Possible two-sided model (only when the product serves both)

Job-seeker side (above) + employer side (post job, applicant pipeline
= kanban-ish table, candidate search) — enterprise-density UI
(industries/b2b-enterprise.md) vs seeker side's friendly utility.

## MENA specifics

AR/EN full bilingual parity (bayt serves both fully `[OBSERVED]`);
CV language toggle and salary-period formatting follow supplied market data
and locale policy—do not assume monthly/annual defaults. Nationality or visa
fields are sensitive and appear only when necessary, lawful, and explicitly
required. Seasonal campaigns require actual content and business scope.

## Don't

Marketing-heavy home hiding search · fake "X jobs available" urgency ·
dark patterns in recurring subscription for seekers (pay-to-apply =
trust poison) · ghost-status black holes.

## Corpus observations (v7.1 growth: 11 products SOURCE-OBSERVED 2026-09-03)

| Family (n) | Observed shape | Why it differs | When / when NOT |
|---|---|---|---|
| Candidate marketplaces (otta, remoteok, weworkremotely) | search/filter-first or curated rails; otta = "Explore jobs" nav; remoteok near-bare list | users scan many listings fast | volume job discovery; NOT employer products |
| ATS boards (greenhouse, lever) | B2B SaaS register: Sign in/Demo/Pricing; the public board is a sub-surface of employer software | buyer = employer; candidates arrive by link | hiring-software contexts; never style candidate marketplaces like this |
| Regional/bilingual (wuzzuf EN, forasna RTL) | bilingual portals, CV-upload entry, career advice sections | MENA job seeking is CV+agency-flavored | regional; NOT global remote boards |
| Public-service (usajobs) | account-centric: profile, documents, saved searches, notifications | application lifecycle = the product | government hiring; NOT casual discovery |
| Career ecosystems (reed UK) | jobs + courses + advice in one nav | monetize the whole career journey, not placements | when the business model spans LTV |

WHY: who pays decides the surface (candidates pay with time → speed;
employers pay money → ATS features). WHEN NOT to copy any family onto
another: an ATS-styled consumer board reads corporate; a marketplace-styled
ATS undersells employer tools.

## Corpus observations (v7.3 diversity, SOURCE-OBSERVED 2026-09-03)

| Family | Observed shape | WHY | WHEN | WHEN NOT | TRADEOFF |
|---|---|---|---|---|---|
| Career + learning hybrids (jobberman Job Vacancies / AI Career Tool / My Learning; internshala Jobs + Hire Candidates) | jobs and courses/tools in one nav | the board monetizes the whole path, not only the listing | regional career ecosystems | ATS employer-login products | |
