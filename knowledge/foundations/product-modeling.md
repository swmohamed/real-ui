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
| Top tasks | What outcomes matter? Rank tasks by frequency, criticality, time sensitivity, consequence, and context | Informs entry points, persistence, acceleration, and recovery without forcing a home-screen shortcut |
| Task verbs | browse · search · monitor · create · transact · review/approve · configure | Verb narrows representation and density candidates; content shape and consequence decide the container |
| Relationships | 1→n (clinic→appointments)? n→n (skills↔jobs)? owner? | 1→n = drill-down list; n→n = filters/facets/search-first; ownership = permissions surface |
| Entity lifecycle | What states does the main entity pass through? (draft→sent→paid) | Lifecycle = status column, filters, empty/error states, notifications |
| Volume | How many items are typical, and how do users find or act on them? | Informs retrieval, grouping, pagination/virtualization, selection, and density without a fixed numeric component rule |
| Audience & register | Who + how expert? | Expert→density+shortcuts; consumer→guided+airy |
| Actors & permissions | Who can view, edit, suggest, approve, publish, or administer—including automation? | Determines action visibility, attribution, approval, and audit surfaces |
| Time & freshness | Is data live, delayed, versioned, scheduled, or historical? | Requires timestamps, freshness language, refresh behavior, or temporal comparison |
| Shared state | Can actors edit concurrently or work from stale/offline copies? | Requires presence only when useful, plus sync, conflict, history, and recovery behavior |
| Automation & authority | Does the system suggest, draft, retrieve, recommend, or act? What can it commit? | Determines scope disclosure, review, confirmation, interruption, and rollback |
| Consequence & reversibility | What happens if this action is wrong, and can it be undone? | Sets friction, confirmation, approval, and recovery proportional to risk |
| Source & authorship | Where did content/data come from, who changed it, and under which version? | Requires provenance, citations, ownership, or audit history when decisions depend on it |
| Entry and continuity | How does work begin or resume: home, deep link, notification, file, OS command, saved view, handoff? | Determines launch, orientation, restoration, and cross-session continuity |
| Outcome and evidence | What result proves the task or service worked, for users and operations? | Defines completion state, success measures, guardrails, and validation |

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
2. **Task priority + entry context → access strategy**: choose home, first tab,
   persistent command, deep link, notification, saved view, file association,
   or resume surface based on how the task actually begins. If “see today’s
   schedule” dominates normal launches, the schedule may be home; prove that
   from the experience rather than making it a genre rule.
3. **Relationships → cross-links**: detail pages link across relations;
   n→n relationships demand search/filters as a first-class surface.
4. **Verb + content shape → representation**: monitoring/review may need
   dense comparison; browsing may need media-forward modules; creation may
   need a focused editor. The verb narrows candidates but does not pick a
   component by itself.
5. **Volume + findability need → retrieval**: high volume, repeated lookup,
   unstable ordering, or many attributes can justify search, facets, sorting,
   pagination, or virtualization. Low volume alone does not forbid search;
   known-item recall and accessibility may still require it.
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
| compare values or distributions | chart plus accessible source table |
| understand sequence, history, or time/state changes | timeline or event log |
| monitor staged work or ordered processing | board, queue, or operation list |
| complete a focused sequence | form/step flow |
| understand containment or hierarchy | tree or grouped outline |
| understand many-to-many relationships | graph or relationship explorer |
| understand geographic/spatial relationships | map plus non-map alternative |
| create or arrange freeform spatial material | canvas with inspectable structure |
| execute known expert commands | command surface plus discoverable alternatives |
| read a narrative | prose sections with restrained supporting media |

Cards are not a neutral default. Avoid them when the task depends on aligned
comparison, continuous reading, sequence, bulk selection, relationship or
spatial context, or scanning many homogeneous rows. Use them when a bounded
entity genuinely has heterogeneous, self-contained content and actions.

Write a screen contract before layout:

`screen job -> primary user -> top task -> required content/actions -> priority -> representation -> states`

Then use `pages/README.md` and individual page files as candidate-module
catalogs. Their listed order has no authority. Use `industries/README.md`
before any industry module.

## Product-fit test (finish gate input)

- Name the top outcomes → are their entry paths proportionate to frequency,
  urgency, consequence, and actual launch context?
- Which entity dominates the home screen, and why (task rank, not habit)?
- Can every entity's lifecycle be completed from the UI (create →
  progress → done/failed → resolved)?
- Would a user of THIS product recognize their job in the structure —
  or a generic version of the industry?
- Can every capability pass the scope ledger? Can every major region cite
  its task/content priority and explain why its representation fits?
- Are automation authority, shared-state behavior, operation recovery,
  source/authorship, and consequence modeled when the product contains them?

## Worked micro-example

"Clinic operations tool" (healthcare + b2b axes). Model: entities =
patients, appointments, practitioners, invoices; frequent high-consequence
work = run today’s schedule; relationships = clinic 1→n appointments,
appointment n→1 patient; audience = staff using resizable desktop windows.
If observation and launch data confirm that context, a schedule-first home
with quick patient context is a defensible candidate. Billing and command
density still depend on role, volume, input, permissions, and workflow
evidence. Industry marketing conventions do not enter the internal tool.

Multi-industry products (taxonomy.md combos): model FIRST, then pull the
primary industry file fully + secondaries for overlap sections only.

Connects: foundations/experience-evidence.md (people, journey, outcomes) ·
taxonomy.md (classification) · pages/dashboard.md (app shells)
· redesign/workflow.md stage 1 (understand = model + diagnose current)
· implementation/realism.md (lifecycle states completeness).
