# AI-Assisted and Agentic Interaction

AI is a product capability, not a page type or visual style. A chat window,
sparkle icon, side panel, or gradient does not become appropriate merely
because a model is involved. Derive the interaction from the user's task, the
system's authority, the consequence of error, and the artifact being changed.

Knowledge class: **DESIGN PRINCIPLE + RECOMMENDATION**, grounded in
**OFFICIAL GUIDANCE** (Microsoft HAX, Google PAIR, NIST AI RMF) and a
12-product **DOC-OBSERVED** comparison recorded in
`research/reports/v6-evidence-driven-expansion.md`. Product documentation
establishes documented behavior, not rendered or runtime quality.

## Model the AI role before choosing a surface

Record these fields in the product model:

`role -> input/context -> output/artifact -> authority -> stakes ->
reversibility -> source/provenance need -> human decision -> failure path`

| AI role | Useful interaction class | Commit boundary |
|---|---|---|
| Suggest or complete | inline proposal, ranked alternatives | remains distinct until accepted or ignored |
| Generate or transform | editable draft/artifact, targeted changes, comparison | preview/apply; preserve the prior version |
| Retrieve or synthesize | answer/report plus source scope and freshness | user verifies before relying where stakes matter |
| Classify or recommend | rationale, alternatives, missing-context cue | human decision when consequence or uncertainty is material |
| Act across tools | plan/queue, action trace, approvals, checkpoints | approval and permission scale with external impact |

These are representation classes, not prescribed layouts. A conversational
surface is useful for ambiguous exploration. Sustained writing, code, media,
data, or workflow work usually needs the domain artifact itself: editor, diff,
canvas, table, timeline, queue, or review surface.

## The control contract

Before design, answer all nine:

1. **Capability** — what can the system do, and what can it not do here?
2. **Context** — which files, records, people, sites, or sensors can it use?
3. **Intent** — what outcome and boundaries did the user authorize?
4. **Proposal vs execution** — is output a suggestion, a draft, or a committed
   change?
5. **Progress** — what is happening now; can the user steer, pause, or cancel?
6. **Review** — what changed, what evidence supports it, and what needs human
   judgment?
7. **Commit** — which exact action changes external or shared state?
8. **Recovery** — can the user undo, restore, retry, or continue manually?
9. **Audit** — who/what acted, when, on which objects, with which result?

If the product cannot answer these, an agentic UI is not ready for polish.
Use `ux/operations-recovery.md` for durable operation states and
`ux/collaboration-concurrency.md` when shared artifacts or approvals are
involved.

## Risk-scaled autonomy

Autonomy is a spectrum, not an on/off setting.

| Consequence and recoverability | Default control |
|---|---|
| local, low-stakes, easily reversible | act with visible result and nearby undo |
| bounded but meaningful change | preview or diff; granular accept/reject |
| shared-state or externally visible change | name target/audience/consequence before commit |
| financial, legal, health, safety, destructive, or hard-to-reverse action | explicit human decision at the last responsible moment; retain an audit path |
| repeated automation | global policy plus per-run exceptions, pause/disable, and review thresholds |

Approvals are not permission boundaries. The system still needs least-privilege
access and must not imply that a review affordance technically prevents an
otherwise-authorized action.

## Authorship, sources, and explanations

- Distinguish human-authored, AI-suggested, AI-generated, retrieved, and
  committed content when that distinction changes trust, responsibility, or
  review. Do not paint the entire product as "AI" when only one field is.
- Expose source scope and freshness for retrieval/synthesis. Link claims to
  sources where verification is part of the task; a source list with no claim
  relationship is weak provenance.
- Explain the decision-relevant part: inputs used, missing context, why an
  action was suggested, or which rule triggered it. Do not expose fabricated
  chain-of-thought or use explanation as decorative reassurance.
- Persistent exported media may need durable provenance metadata. In-product
  labels and exported credentials solve different problems.
- A universal AI badge is not required. IBM Carbon's AI label is one
  first-party system solution, not a cross-product layout rule. Choose wording,
  placement, and persistence from user risk and the host design system.

## Uncertainty and confidence

The objective is calibrated reliance, not maximum trust.

- Prefer actionable uncertainty: name missing data, limits, alternatives, and
  what the user should verify.
- Do not show raw model confidence as a percentage unless it is calibrated,
  understandable to this audience, and changes a real decision. False
  precision can increase over-reliance.
- Categorical confidence is also a product policy, not decoration. Define what
  each band changes: auto-apply, hold for review, or decline to act.
- High-stakes output needs domain evidence, a responsible human role, and a
  contest/review path. A disclaimer alone is not oversight.
- When uncertain about intent, narrow scope, ask, or degrade to a suggestion;
  do not silently guess and execute.

## Editing, versioning, and recovery

Real products converge on reversible work, not one visual shell:

- Keep generated changes distinguishable until applied where selective review
  is useful.
- Support targeted edits to the existing artifact instead of forcing complete
  regeneration.
- Preserve checkpoints or version history for material transformations.
- Show a diff or changed-region summary when the user must assess consequences.
- Keep partial useful output when a long-running task stops, if the data is
  valid and clearly labeled.
- Separate **interrupt** (stop current work), **reject** (do not apply a
  proposal), **undo/restore** (reverse applied work), and **retry** (new
  attempt). They are not interchangeable.

## States and platform adaptation

Agentic work may be planning, waiting for input, queued, working, using a tool,
blocked by permission, awaiting review, partially complete, complete, failed,
canceled, or superseded. Use the operation state model rather than a permanent
typing indicator.

- Web/desktop: diffs, logs, queues, keyboard review, and side-by-side artifacts
  can use available space; do not force every task into a narrow chat rail.
- Phone: prioritize current state, consequence, next decision, and safe
  interruption; move detailed traces behind disclosure without hiding the
  action boundary.
- Native/cross-platform: use platform permission, background-task,
  notification, and destructive-action conventions. Brand consistency does
  not justify identical control geometry.
- Accessibility: announce meaningful status changes without streaming every
  token to a live region; retain keyboard focus; label source/generated
  distinctions in text/semantics, not color alone; respect reduced motion.
- Localization/RTL: localize AI terminology only when users need it; isolate
  mixed-script prompts, citations, IDs, code, and model/tool names; keep source
  ordering and directional controls semantically correct.

## Anti-patterns

- Chat as the default IA for unrelated domain tasks.
- One "Generate" button with hidden input scope and undefined side effects.
- Auto-applying high-impact changes because the model sounds confident.
- Sources that cannot be connected to claims; explanations that are just
  fluent restatements of the output.
- A thumbs-up/down control that does not say what feedback changes or when.
- Regeneration as the only correction path; no direct edit, alternatives, or
  restore.
- Persistent animated "thinking" with no durable state, progress, or exit.
- AI-authored changes indistinguishable from human-approved state in shared or
  regulated work.

## Finish gate

[ ] AI role and artifact modeled [ ] context/data scope visible where needed
[ ] suggestion/draft/commit boundary explicit [ ] autonomy matches stakes and
reversibility [ ] sources/authorship/freshness traceable [ ] uncertainty is
actionable, not decorative [ ] edit/reject/interrupt/undo/retry are correctly
separated [ ] all operation states covered [ ] permissions and approvals are
not conflated [ ] keyboard/screen-reader/RTL behavior specified [ ] the design
would still fit the product if all sparkle/AI styling were removed
