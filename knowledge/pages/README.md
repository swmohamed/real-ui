# Page Patterns: Candidate Modules, Not Templates

The files in this directory are pattern inventories for common page jobs.
They are not canonical templates and do not authorize a page to exist.
Product entities, top tasks, content priority, and known capabilities decide
the page set and composition first.

Label: RECOMMENDED composition discipline.

## Selection procedure

1. Name the page job in one sentence (“compare eligible plans,” “run today's
   schedule,” “understand this article”).
2. List the content and actions required to complete that job.
3. Rank them by user value, decision risk, frequency, and urgency using
   `foundations/product-modeling.md`.
4. Choose only the page-file modules that represent those requirements well.
5. Order and group modules by the ranked information model—not by the order
   in a page file or a competitor screenshot.
6. Define empty, loading, error, partial, permission, and extreme-content
   states before calling the composition complete.

## Structural rationale requirement

For each major region, record:

`region -> required content/action -> user task or decision -> chosen representation`

Examples:

- `appointment timeline -> today's bookings -> run the clinic -> dense time grid`
- `delivery promise -> arrival date -> decide whether to buy -> text beside price`
- `related items -> none in scope -> no region`

If the rationale starts with “this industry usually has…” or “this page type
normally uses…”, it has not passed the gate.

## Responsive rule

Adaptation preserves task and information priority, not desktop geometry.
At each relevant width/input class, state what remains, moves, condenses,
changes representation, or is removed. “Stack everything” is not a plan.

## Originality rule

Files here supply modules and failure modes. They must not supply a complete
section sequence. Two products with different tasks, content, volume, or
brand should not converge merely because both use the same page type.
