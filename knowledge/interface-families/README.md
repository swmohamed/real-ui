# Interface Families: Authority and Scope Contract

Interface-family files are evidence catalogs for recurring WORKSPACE
shapes. They are not page templates, not industry modules, and not
product specifications.

An interface family is a different axis from industry:

`healthcare + work-queue + triage + desktop`
is not
`healthcare + patient-portal + appointment + mobile`

Label: RECOMMENDED retrieval discipline. Individual claims keep their
own SOURCE-OBSERVED / DOC-OBSERVED / INFERRED / RECOMMENDED labels.

## Load order (mandatory)

1. Model the product in `foundations/product-modeling.md`.
2. Write the scope ledger and content-priority model.
3. Read this contract.
4. Read only the family that matches THIS workspace job.
5. Reconcile with the industry module for domain risk and vocabulary.
6. Accept a convention only when it supports a modeled task, entity,
   permission, or known capability.

## What a family is allowed to inform

- how arriving work, reference text, time, spatial artifacts,
  named files, or conversations typically change IA, density, and
  representation;
- which sub-families must not be averaged;
- questions to ask when the workspace type is unclear.

A family may never invent:

- tickets, inboxes, calendars, canvases, maps, comments, presence,
  folders, channels, encryption, AI agents, or analytics because
  "this family usually has them";
- a left rail, KPI row, three-pane mail chrome, explorer tree, or
  infinite canvas because the file mentions those as candidates.

## Families in this catalog

Load only the one that matches THIS workspace job:

- `work-queue.md` — arriving items + state change
- `reference-docs.md` — topic tree + lookup
- `temporal-workspace.md` — time as the primary axis
- `spatial-canvas.md` — space as the object being made or watched
- `asset-library.md` — named files/assets kept, sent, or governed
- `conversation-space.md` — a DM, channel, thread, or mailbox

Roles that split into two products (`ux/roles-surfaces.md`) are not
an interface family. Comparison is a task (`foundations/product-modeling.md`),
not a seventh family.

## Family-split rule

Sub-families are DIFFERENCE evidence. A helpdesk inbox is not an
error queue. A docs tree is not a newspaper. A booking link is not
a team calendar. A live map is not a whiteboard. A brand DAM is not
a family Drive. Signal is not Slack. Never average them into one
"professional tool" layout.

## Exit test

- Can the workspace job be named without using the family label?
- Would removing the family name leave a structure that still fits
  the entities, volume, and consequence?
- Did industry + family together invent a capability?

Failure means return to product modeling.
