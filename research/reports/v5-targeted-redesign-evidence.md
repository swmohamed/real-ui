# V5 targeted redesign evidence

## Failure traced

The real gaming failure was not a lack of redesign vocabulary. The source plan called the work a FULL REDESIGN while its decisions stayed at color, type, border, and component-skin level. The implementation then retained the existing home composition and component sequence: challenge hero, an inferred advertising band, continuation rail, catalog grid, category rail, and later a player panel. Saved before/after captures confirmed that the silhouette and information authority remained the same.

The causal chain was:

1. static guidance existed, but no artifact blocked implementation;
2. the plan could declare a redesign without separately modeling product and presentation;
3. old component boundaries became the default implementation plan;
4. industry-common advertising leaked into scope without a product requirement; and
5. validation was prose written after the change, so it did not force a new composition.

This is a process-level failure. The V5 repair therefore adds an executable PLAN checkpoint before presentation code and a RENDER checkpoint after real same-viewport captures.

## Research decision trace

| Source | Label | Supported decision | What it does not justify |
|---|---|---|---|
| [Xbox Accessibility Guideline 112](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/112) | PLATFORM RULE | Keep digital-input navigation and focus order logical and predictable across the play deck and library. | A particular hero, card grid, visual style, or game-business model. |
| [WCAG 2.2 reflow understanding](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) | PLATFORM RULE | Change the phone interaction model rather than squeezing desktop workspaces. | A universal bottom-navigation pattern. |
| [WCAG 2.2 target-size understanding](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) | PLATFORM RULE | Provide separated task tabs, facets, compare actions, and service controls. | Larger controls without task priority. |
| [Atlassian navigation system](https://atlassian.design/components/navigation-system/) | SOURCE-OBSERVED | Persistent context is reasonable for a real workspace/project hierarchy. | Copying Atlassian's shell or introducing absent entities. |
| [Atlassian drag-and-drop guidance](https://atlassian.design/components/pragmatic-drag-and-drop/design-guidelines) | DESIGN PRINCIPLE | Status movement needs visible outcomes and a non-drag path. | Making drag the primary or only workflow. |
| [GOV.UK task list](https://design-system.service.gov.uk/components/task-list/) | DESIGN PRINCIPLE | A task/status list can support choosing the next item when triage is the modeled job. | Replacing every dashboard with a task list. |
| [BBC GEL typography](https://bbc.github.io/gel/foundations/typography/) and [global navigation](https://bbc.github.io/gel/components/global-navigation/) | SOURCE-OBSERVED | Editorial hierarchy and section orientation need deliberate type and navigation behavior. | A newspaper-like composition for every content product. |
| [Baymard product-list research](https://baymard.com/research/ecommerce-product-lists) and [filtering benchmark](https://baymard.com/blog/current-state-product-list-and-filtering) | SOURCE-OBSERVED | Put real category-specific comparison fields, result context, and applied filters near the catalog decision. | Facets, reviews, recommendations, memberships, or marketplaces when the product lacks them. |

## Generalizable versus project-specific

The generalizable repair is stored in `knowledge/redesign/full-redesign-execution.md` and wired into the redesign workflow. It defines the product/presentation split, capability and scope ledgers, style-blind dimension check, composition reset, and executable PLAN/RENDER gates.

Gaming, SaaS, editorial, and ecommerce findings remain in their showcase case files. They are product evidence, not universal knowledge and not layout templates. The eight greenfield surfaces likewise demonstrate derivation from different tasks; they are explicitly excluded from retrieval as prescribed patterns.

## Honest boundary

The research is targeted rather than exhaustive. The browser fixtures prove that the repaired process can reject cosmetic-only redesigns and produce structurally different, scoped, responsive surfaces in four test domains. They do not prove that every future agent run will comply, nor that a static fixture covers production business logic or every browser and assistive-technology combination.
