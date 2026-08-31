# Industry Knowledge: Authority and Scope Contract

Industry modules are evidence catalogs, not product specifications. They
describe recurring terminology, trust expectations, risks, and candidate
patterns seen in a genre. They do **not** decide this product's features,
information architecture, page order, navigation model, or visual DNA.

Label: RECOMMENDED retrieval discipline. Individual claims retain their own
OBSERVED / INFERRED / RECOMMENDED labels.

## Load order (mandatory)

1. Model the product in `foundations/product-modeling.md`.
2. Write the scope ledger and content-priority model.
3. Read this contract.
4. Read the primary industry module; use secondary modules only for the
   overlapping risk, terminology, or workflow.
5. Accept a convention only when it supports a modeled task, entity, or known
   capability. Record the reason for each structural convention adopted.

## Authority boundary

Industry knowledge may inform:

- vocabulary, user expectations, trust and compliance pressure;
- domain-specific edge cases and evidence users need to decide;
- candidate interaction and presentation patterns;
- questions to ask when requirements are incomplete.

Industry knowledge may never invent:

- accounts, ads, payments, subscriptions, recommendations, chat, social
  features, notifications, tracking, reviews, maps, or personalization;
- a marketing homepage, dashboard, hero, sidebar, card grid, checkout, or
  other page merely because competitors commonly have one;
- a capability whose only evidence is an industry module.

## Scope gate

Every proposed capability must be classified before design:

| Status | Meaning | Action |
|---|---|---|
| KNOWN | exists in supplied product/code/data | preserve and support |
| REQUESTED | explicitly requested | design it |
| NECESSARY SUPPORT UX | required to complete a KNOWN/REQUESTED capability safely (for example, validation for a supplied form) | add narrowly and record why |
| HYPOTHESIS | plausible but not authorized | ask, label as a concept, or exclude |
| OUT OF SCOPE | unsupported or rejected | do not design |

If an industry module says “must,” “follow,” “standard,” or “default,” read
that as a domain expectation to evaluate unless it is explicitly labeled as
a legal, accessibility, security, or platform requirement.

## Exit test

- Can every proposed feature be traced to KNOWN, REQUESTED, or NECESSARY
  SUPPORT UX evidence?
- Can every major region in the layout be traced to a top task, content
  priority, or decision requirement?
- Would removing the industry name leave a structure that still makes sense
  for this product model?

Failure means return to product modeling; do not choose a genre template.
