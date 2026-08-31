# Product Modeling (before any IA decision)

An industry file describes the GENRE's conventions. It is a baseline to
reconcile with — never a substitute for modeling THIS product. The failure
mode this file prevents: `industry → familiar layout` (a clinic tool gets a
generic healthcare homepage because "healthcare sites look like that").

Label: RECOMMENDED method (design reasoning, not corpus observation).

## The model (write it down before IA — 5–10 lines is enough)

| Element | Question | Design consequence |
|---|---|---|
| Entities | What nouns does the product manage? (patients, invoices, tracks, bookings) | Each entity needs surfaces: list, detail, create/edit, states |
| Top tasks | What will users do most? Rank 1–3 by frequency × criticality | Task #1 gets the shortest path (often = home screen) |
| Task verbs | browse · search · monitor · create · transact · review/approve · configure | Verb decides density + container (monitor→dense table; browse→cards) |
| Relationships | 1→n (clinic→appointments)? n→n (skills↔jobs)? owner? | 1→n = drill-down list; n→n = filters/facets/search-first; ownership = permissions surface |
| Entity lifecycle | What states does the main entity pass through? (draft→sent→paid) | Lifecycle = status column, filters, empty/error states, notifications |
| Volume | How many items typical? 10 or 10,000? | 10 = single screen; 10k = search + facets + pagination |
| Audience & register | Who + how expert? | Expert→density+shortcuts; consumer→guided+airy |

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

## Product-fit test (finish gate input)

- Name the top task → is it reachable in one step from the entry screen?
- Which entity dominates the home screen, and why (task rank, not habit)?
- Can every entity's lifecycle be completed from the UI (create →
  progress → done/failed → resolved)?
- Would a user of THIS product recognize their job in the structure —
  or a generic version of the industry?

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
