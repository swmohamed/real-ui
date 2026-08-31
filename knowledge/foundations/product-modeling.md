# Product Modeling (before any IA decision)

An industry file describes the GENRE's conventions. It is a baseline to
reconcile with — never a substitute for modeling THIS product. The failure
mode this file prevents: `industry → familiar layout` (a clinic tool gets a
generic healthcare homepage because "healthcare sites look like that").

Label: RECOMMENDED method (design reasoning, not corpus observation).

## The model (write it down before IA)

| Element | Question | Design consequence |
|---|---|---|
| Entities | What nouns does the product manage? (patients, invoices, tracks, bookings) | Each entity needs surfaces: list, detail, create/edit, states |
| Top tasks | What will users do most? Rank 1–3 by frequency × criticality | Task #1 gets the shortest path (often = home screen) |
| Task verbs | browse · search · monitor · create · transact · review/approve · configure | Verb decides density + container (monitor→dense table; browse→cards) |
| Relationships | 1→n (clinic→appointments)? n→n (skills↔jobs)? owner? | 1→n = drill-down list; n→n = filters/facets/search-first; ownership = permissions surface |
| Entity lifecycle | What states does the main entity pass through? (draft→sent→paid) | Lifecycle = status column, filters, empty/error states, notifications |
| Volume | How many items typical? 10 or 10,000? | 10 = single screen; 10k = search + facets + pagination |
| Audience & register | Who + how expert? | Expert→density+shortcuts; consumer→guided+airy |

## Scope ledger (all design work, not only redesigns)

Before selecting pages or components, classify every proposed capability:

- **KNOWN** — present in supplied requirements, code, routes, data, or an
  existing product.
- **REQUESTED** — explicitly requested by the user.
- **NECESSARY SUPPORT UX** — the smallest interaction needed to make a
  KNOWN/REQUESTED capability complete, safe, or accessible.
- **HYPOTHESIS** — plausible but unconfirmed; ask, label as conceptual, or
  leave out.
- **OUT OF SCOPE** — unsupported or rejected; do not design it.

Industry and page-pattern files are not evidence of scope. Accounts, ads,
payments, subscriptions, recommendations, chat, social features, reviews,
maps, and notifications need their own scope evidence.

## Content model and information priority

Inventory real content before choosing its container. Mark assumptions.

| Content item/type | Source | Audience need | Decision/task supported | Frequency/urgency | Risk if missed | Constraints |
|---|---|---|---|---|---|---|

Rank major items with a small, explicit model rather than aesthetic instinct:

`priority = task importance + frequency + urgency + decision risk`

The exact arithmetic is unimportant; the relative order is. Content without
a traceable task, decision, legal need, or known product purpose does not earn
screen space.

## Deriving IA from the model

1. **Entity → surface map**: list the surfaces per entity (this IS the
   sitemap skeleton — not the industry file's sitemap).
2. **Task #1 → primary position**: home screen / first tab / hero action.
   If task #1 is "see today's schedule", the schedule IS the home — not a
   marketing hero, not a generic dashboard.
3. **Relationships → cross-links**: detail pages link across relations;
   n→n relationships demand search/filters as a first-class surface.
4. **Verb → density**: monitoring/review = dense tables, sticky columns;
   browsing/discovery = media-forward cards; creation = focused forms.
5. **Volume → retrieval**: >100 items = search-first IA + facets +
   sortable columns; <20 = curated single view, no search chrome.
6. **THEN reconcile with the industry file**: where the genre convention
   fits the model, use it (it carries user expectations); where it
   doesn't, deviate with a one-line reason. Write the reason down.

## Deriving representation and composition

Choose representations from content shape and task verb, not page genre:

| Need | Candidate representation |
|---|---|
| compare many entities across stable attributes | table/data grid |
| browse a small media-forward set | cards/shelves |
| scan simple homogeneous records | list rows |
| monitor time/state changes | timeline, queue, chart + source table |
| complete a focused sequence | form/step flow |
| understand a hierarchy or relationship | tree, grouped list, diagram |
| read a narrative | prose sections with restrained supporting media |

Write a screen contract before layout:

`screen job -> primary user -> top task -> required content/actions -> priority -> representation -> states`

Then use `pages/README.md` and individual page files as candidate-module
catalogs. Their listed order has no authority. Use `industries/README.md`
before any industry module.

## Product-fit test (finish gate input)

- Name the top task → is it reachable in one step from the entry screen?
- Which entity dominates the home screen, and why (task rank, not habit)?
- Can every entity's lifecycle be completed from the UI (create →
  progress → done/failed → resolved)?
- Would a user of THIS product recognize their job in the structure —
  or a generic version of the industry?
- Can every capability pass the scope ledger? Can every major region cite
  its task/content priority and explain why its representation fits?

## Worked micro-example

"Clinic operations tool" (healthcare + b2b axes). Model: entities =
patients, appointments, practitioners, invoices; top task = "see and run
today's schedule"; relationships = clinic 1→n appointments, appointment
n→1 patient; volume = 30–80 appointments/day; audience = staff (expert).
Derived IA: schedule-first home (timeline per practitioner), patient
drawer (not full page — task is quick context, not deep browsing),
billing as secondary tab, dense data tables, keyboard shortcuts for
check-in. Industry deviation: no marketing hero, no trust badges —
genre conventions that don't fit an internal expert tool. Reason logged.

Multi-industry products (taxonomy.md combos): model FIRST, then pull the
primary industry file fully + secondaries for overlap sections only.

Connects: taxonomy.md (classification) · pages/dashboard.md (app shells)
· redesign/workflow.md stage 1 (understand = model + diagnose current)
· implementation/realism.md (lifecycle states completeness).
