# FULL Redesign Execution Contract

Use this file only when the classified depth is **FULL REDESIGN**. It turns
the reasoning in `depth.md`, `extraction.md`, and `workflow.md` into two
checkpoints that can stop implementation. The known failure this prevents is
a plan that says "fully re-derived" while recording only colors, type,
spacing, borders, and replacement components.

Label: RECOMMENDED execution method plus deterministic repository verifier.

## The two checkpoints

### Checkpoint A — PLAN PASS (before editing presentation code)

Create a compact redesign contract, in JSON when the repository verifier is
available, or an equivalent structured artifact when it is not. It must
contain:

1. product extraction: purpose, users, intents, tasks, capabilities,
   workflows, entities/relationships, content/data, routes, business logic,
   technical constraints, SEO, accessibility, platform/device/locale;
2. presentation extraction: current navigation, hierarchy, zones/sequence,
   representations, interaction zones, density, responsive model, component
   tree, and visual system;
3. targeted evidence and the relevant REAL-UI knowledge used;
4. a decision brief: product/user priorities, IA/navigation/content/
   interaction/responsive direction, structures kept/changed with reasons,
   and out-of-scope features;
5. a closed capability ledger and bidirectional scope ledger;
6. the proposed style-blind structure plus structural decisions.

Run:

```bash
python scripts/validate_redesign.py path/to/case.json --phase plan
```

Do not start presentation implementation until this returns `PLAN PASS`.
When the verifier is unavailable, apply the same checks manually and label
the result REASONED rather than EXECUTABLE.

### Checkpoint B — RENDER PASS (before calling the redesign complete)

Render BEFORE and AFTER implementations at the same controlled desktop and
phone viewports. Capture screenshots and DOM structure snapshots. Then run:

```bash
python scripts/validate_redesign.py path/to/case.json --phase render
```

`RENDER PASS` requires real implementation files, correctly sized image
artifacts, DOM evidence, closed capabilities, scope fidelity, and a
style-blind structural change count appropriate to FULL. A screenshot alone
is visual evidence; the DOM snapshot is what makes the structure repeatable.

If browser tooling cannot run, do not block otherwise useful work, but report
RUNTIME/RENDER as UNVERIFIED. Never convert a reasoned inspection into a
render claim.

## Implementation reset

After PLAN PASS, create the new page shell and major regions from the proposed
structure. Import data, state, routes, business logic, and capability-level
helpers into that shell.

For FULL, do not begin by editing the old page component in place and do not
bulk-import its presentation subtree. An old presentation component may be
reused only after the new shell exists and its KEEP is recorded as
`still correct` in the contract. Reuse is an earned implementation decision,
not the starting point.

This is not a mandate to maximize code churn. Logic-only modules, data access,
content, routes, and well-scoped primitives can and should survive. The reset
boundary is composition authority.

## Research-to-decision trace

Each important decision records:

`DECISION -> EVIDENCE -> RELEVANT KNOWLEDGE -> PRODUCT REASON -> CONFIDENCE`

Evidence can authorize a pattern only when the product has the task and
conditions that make the pattern useful. Prevalence alone is not authority.
Project-specific evidence stays with the project. Promote a finding into the
permanent knowledge base only when it is well-supported, reusable, and
correctly scoped.

## Structural decisions and legitimate similarity

The verifier ignores color, typography, radius, shadows, gradients, imagery,
and token names. It compares navigation, hierarchy/zones, section sequence,
grouping, representations, primary interactions, density, responsive model,
and silhouette.

For a FULL result, at least five style-blind dimensions normally need to
change. This is a regression threshold, not a creativity quota. If fewer
changes are genuinely correct, record every preserved dimension in the
existed-vs-correct audit with product evidence; the result requires human
review and must not be auto-claimed as RENDER PASS.

Every structural change must cite a product task, diagnosed problem,
platform constraint, or supported research/knowledge decision. Random
difference fails even when the diff is large.

## Failure loop

```text
PLAN FAIL   -> repair model/brief -> re-run before coding
RENDER FAIL -> trace failing dimension/capability/scope -> re-derive ->
               rebuild -> re-render -> re-run
```

Do not lower thresholds, rewrite the contract after seeing the output, or
select an easier fixture. Advertising, subscriptions, accounts, social
features, recommendations, and other genre-common features remain excluded
unless their ledger classification authorizes implementation.

## Evidence boundaries

A fixture that clears both checkpoints may be called BEHAVIORALLY VERIFIED,
RUNTIME VERIFIED, and RENDER VERIFIED for that named fixture and harness run.
It does not prove that every future model invocation will comply.

Connects: `redesign/depth.md` (classification/style-blind test) ·
`redesign/extraction.md` (product/presentation and ledgers) ·
`redesign/workflow.md` (stage order) · `foundations/product-modeling.md`
(new IA) · `implementation/realism.md` (states and stack constraints).
