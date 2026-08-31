# Industry: Jobs & Recruitment (Job Boards, Hiring Platforms)

Evidence: v2 fetch 2025-08 `[OBSERVED]` — bayt.com (MENA leader),
wuzzuf.net (Egypt leader). Complements social-community.md (profiles/
communities) and saas-dev.md (ATS/enterprise tooling).

## Observed design languages

- Bayt: Roboto + **Vazirmatn** (Arabic-capable Latin font — bilingual
  stack in ONE family system) `[OBSERVED]`; minimal breakpoints
  (1023/1024) — simple two-state adaptive.
- Wuzzuf: Open Sans + **IBM Plex Sans Arabic** `[OBSERVED]`;
  Bootstrap-class breakpoint spread (575/576, 991/992, 1159/1160) —
  utility-first, dense mobile bp set.

## DNA rules

1. **Search-first homepage**: keyword + location is THE hero (not
   marketing hero) `[OBSERVED - both leaders]`; browse-by-category/
   company tiles secondary; popular-search chips.
2. Job card = structured data contract: title, company (logo),
   location, salary band if available, posted-date freshness, easy-
   apply/featured badges `[OBSERVED - bayt card anatomy]`. Salary
   display: MENA boards show bands more often than Western (trust +
   regulation-adjacent habit) `[INFERRED - corpus pattern]`.
3. Two-pane results on desktop (list ↔ detail), stacked + sheet/detail
   push on mobile (responsive/adaptive-models.md).
4. Filters = facets: experience level, career level, company, remote,
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

## Two-sided reality

Job-seeker side (above) + employer side (post job, applicant pipeline
= kanban-ish table, candidate search) — enterprise-density UI
(industries/b2b-enterprise.md) vs seeker side's friendly utility.

## MENA specifics

AR/EN full bilingual parity (bayt serves both fully `[OBSERVED]`);
CV language toggle; currency+salary period (monthly is MENA default —
annual is Western default; respect it); GCC-specific: nationality/
visa status fields exist in some markets (design neutrally, only where
legally conventional); Ramadan hiring-season spikes (design for
seasonal campaigns).

## Don't

Marketing-heavy home hiding search · fake "X jobs available" urgency ·
dark patterns in recurring subscription for seekers (pay-to-apply =
trust poison) · ghost-status black holes.
