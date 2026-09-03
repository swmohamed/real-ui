# V6 Evidence-Driven Design Intelligence Expansion

Date: 2026-09-01

This audit improves the existing REAL-UI knowledge and routing system. It does
not rebuild the skill, create a showcase, modify showcase fixtures, or publish
the repository. Product-documentation findings are labeled **DOC-OBSERVED**:
they establish documented behavior as of the access date, not rendered
quality, runtime success, availability for every plan/region, or usability.

## 1. AREAS INSPECTED

- Skill orchestration: classification, product modeling, retrieval map,
  dimension activation, Normal versus Deep/Audit routing, finish gates, and
  evidence honesty.
- Product/scope modeling, taxonomy, representation selection, navigation,
  search/discovery, states, data display, implementation realism, anti-AI
  guidance, and redesign extraction/workflow.
- Research method, saturation/confidence ledger, prior V3–V5 audit reports,
  the 156-site source-derived corpus claims, and executable invariant tests.
- Coverage probes across all knowledge files for AI/automation, collaboration,
  concurrency, durable/background operations, provenance, recovery, and
  confidence language.
- Existing platform, accessibility, RTL/localization, industry, page, and FULL
  redesign coverage to determine whether research was genuinely missing or
  merely recently validated.

The repository was already broad. The inspection therefore prioritized
missing decision systems and brittle universal rules rather than adding more
industry catalogs or decorative pattern examples.

## 2. IMPORTANT KNOWLEDGE GAPS

| Gap | Evidence in the existing system | Risk |
|---|---|---|
| AI-assisted and agentic interaction | No substantive module or routing for model role, data scope, autonomy, review, provenance, or correction | Chat becomes the default UI; actions, uncertainty, sources, and consequences are hidden |
| Collaboration and concurrency | No dedicated treatment beyond scattered history/notification references | Avatar rows substitute for permissions, conflict handling, attribution, and recovery |
| Long-running operations and recovery | A few loading bullets, but no durable operation model | Spinners, fictional percentages, ambiguous cancel/retry, hidden partial outcomes, and unsafe backgrounding |
| Product-model dimensions | Entities/tasks/volume were strong; actors, authority, time, source, consequence, and shared state were absent | IA and state decisions missed who can act, what can be committed, and what happens when work overlaps or fails |
| Evidence classes | Source/runtime/render were separated; current first-party documented behavior was not | Help-center research could be overstated as exercised product behavior |
| Cross-product extraction protocol | General research steps existed, but not a method for comparing documented product behavior | One visible shell or famous product could become a template |
| Brittle presentation shortcuts | Navigation counts, three-click rule, fixed table density, title-attribute overflow, universal dash empties, timer-based progress | Context-free prescriptions override task, platform, content, accessibility, and implementation truth |

Recently audited official platform guidance, accessibility foundations,
Arabic/RTL, localization, the scope ledger, product-first IA, and FULL redesign
gates were not re-researched without a new gap signal. They were integrated
with the new dimensions where necessary.

## 3. AUTHORITATIVE RESEARCH

Accessed 2026-09-01. These sources informed principles; they were not copied as
interface templates.

| Source | Evidence/class | Reusable contribution |
|---|---|---|
| [Microsoft HAX Toolkit](https://www.microsoft.com/en-us/haxtoolkit/library/) | DOC-OBSERVED · OFFICIAL GUIDANCE | Communicate capability/limits; support invoke, dismiss, correction, scope, explanation, feedback, and change control |
| [Google PAIR: Explainability + Trust](https://pair.withgoogle.com/guidebook-v2/chapter/explainability-trust/) | DOC-OBSERVED · OFFICIAL GUIDANCE | Calibrated trust, source/data scope, explanation timing, and stakes-dependent transparency |
| [Google PAIR: Feedback + Control](https://pair.withgoogle.com/guidebook-v2/chapter/feedback-controls/) | DOC-OBSERVED · OFFICIAL GUIDANCE | Balance automation and control; make feedback valuable and provide reset/opt-out where applicable |
| [Google PAIR: Errors + Graceful Failure](https://pair.withgoogle.com/guidebook-v2/chapter/errors-failing/) | DOC-OBSERVED · OFFICIAL GUIDANCE | Separate context, system, and input failures; provide risk-appropriate paths forward |
| [NIST AI RMF, Appendix C](https://airc.nist.gov/airmf-resources/airmf/appendices/app-c-ai-risk-management-and-human-ai-interaction/) | DOC-OBSERVED · OFFICIAL GUIDANCE | Model human roles, responsibility, oversight, opacity, bias, and ability to challenge or overrule |
| [WCAG 2.1 Understanding 4.1.3 Status Messages](https://www.w3.org/WAI/WCAG21/Understanding/status-messages) | DOC-OBSERVED · STANDARD REQUIREMENT explanation | Applicable status, progress, and error messages must be programmatically determinable without unnecessarily moving focus |
| [WAI ARIA25](https://www.w3.org/WAI/WCAG21/Techniques/aria/ARIA25) | DOC-OBSERVED · IMPLEMENTATION GUIDANCE | A progressbar's values do not by themselves guarantee useful progress announcements; live-status behavior needs design |
| [WAI-ARIA APG Grid Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/grid/) | DOC-OBSERVED · IMPLEMENTATION GUIDANCE | Interactive grids require a deliberate focus/keyboard model; a visual table does not automatically justify `grid` semantics |
| [IBM Carbon AI label](https://carbondesignsystem.com/components/ai-label/usage/) and [Carbon for AI](https://carbondesignsystem.com/guidelines/carbon-for-ai/) | DOC-OBSERVED · REAL-WORLD OBSERVATION | One design system's approach to AI indication and explanation; retained as a system-specific example, not a universal badge |

## 4. REAL PRODUCTS STUDIED + SAMPLE SIZE

Samples are purposive and decision-oriented, not prevalence studies. Counts
overlap; they are not 33 unique products.

### AI-assisted and agentic control — 12 core product families

| Product family | First-party documentation inspected | Compared behavior |
|---|---|---|
| OpenAI ChatGPT | [Deep research](https://help.openai.com/en/articles/10500283-deep-research-faq/), [agent](https://help.openai.com/en/articles/11752874-agent), [Canvas](https://help.openai.com/en/articles/9930697-what-is-the-canvas-feature-in-chatgpt-and-how-do-i-use-it) | source scope, plan/progress, interruption, high-impact confirmation, editable artifacts, versions |
| Anthropic Claude | [Artifacts](https://support.anthropic.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them), [web search](https://support.anthropic.com/en/articles/10684626-enabling-and-using-web-search) | editable artifact, targeted/full revision, versions, search indication and citations |
| Google Gemini | [Sources](https://support.google.com/gemini/answer/14143489?hl=en), [Gemini in Docs](https://support.google.com/docs/answer/14206696?hl=en) | source inspection, insert/retry/feedback, review/accept/reject in an existing artifact |
| GitHub Copilot | [Inline suggestions](https://docs.github.com/en/copilot/responsible-use/inline-suggestions), [automation rationale and approvals](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automation-rationale-and-approvals) | granular accept/dismiss, human review, rationale, thresholds, approvals and their security limits |
| Notion | [Enterprise Search](https://www.notion.com/help/enterprise-search) | selectable source context, citations, connected-app permissions |
| Perplexity | [How Perplexity works](https://www.perplexity.ai/help-center/en/articles/10352895-how-does-perplexity-work) | source citations and transparency |
| Figma | [AI tools in Figma Design](https://help.figma.com/hc/en-us/articles/23870272542231-Use-AI-tools-in-Figma-Design) | local/action-based generation, editable output, AI-output indication/caveat |
| Canva | [Magic Design](https://www.canva.com/help/use-magic-design/) | multiple generated proposals followed by user choice and editing |
| Adobe Firefly | [Content Credentials overview](https://helpx.adobe.com/ca/firefly/web/get-started/learn-the-basics/content-credentials-overview.html) | durable exported-media provenance differs from transient in-product labeling |
| Microsoft Copilot | [Copilot Pages](https://support.microsoft.com/en-us/microsoft-copilot/using-copilot-pages) | generated response becomes an editable artifact; proposed revisions can be applied or rejected |
| Cursor | [Agent overview](https://cursor.com/docs/agent/overview), [Review changes](https://docs.cursor.com/en/agent/review) | plans/tools, queue/steer, checkpoints, and diff review |
| IBM Carbon for AI | [AI label usage](https://carbondesignsystem.com/components/ai-label/usage/) | a system-level indication/explanation pattern, treated as an example rather than a rule |

### Collaboration and concurrency — 11 core product families

| Product | First-party documentation inspected | Compared behavior |
|---|---|---|
| Google Docs | [Version history](https://support.google.com/docs/answer/190843?hl=en_) | attributed versions, names, restore/copy |
| Figma | [Branching](https://help.figma.com/hc/en-us/articles/360063144053-Guide-to-branching), [version history](https://help.figma.com/hc/en-us/articles/360038006754-View-a-file-s-version-history), [comments](https://help.figma.com/hc/en-us/articles/360039825314), [cursor chat](https://help.figma.com/hc/en-us/articles/1500004414842-Send-messages-with-cursor-chat) | branch/merge review, versions, anchored durable comments, explicitly ephemeral cursor chat |
| Notion | [Workspace collaboration](https://www.notion.com/en-gb/help/collaborate-within-a-workspace), [restore content](https://www.notion.com/help/duplicate-delete-and-restore-content), [audit log](https://www.notion.com/help/audit-log?id=988097) | permissions, shared editing, restore, administrative event history |
| Miro | [Board history and versions](https://help.miro.com/hc/en-us/articles/360021668819-Board-history-versions) | version recovery in a shared spatial artifact |
| Airtable | [Record-level revision history](https://support.airtable.com/articles/3516802427-record-level-revision-history-in-airtable) | field/record change attribution and recovery context |
| Linear | [Issue comments](https://linear.app/docs/comment-on-issues), [documents](https://linear.app/docs/documents) | durable issue discussion, document collaboration/history, automation attribution |
| Slack | [Canvases](https://slack.com/help/articles/203950418-Use-a-canvas-in-Slack), [canvas settings](https://slack.com/help/articles/33536064287891-Manage-canvas-settings-in-Slack) | shared artifacts embedded in communication, comments/history/access control |
| Jira | [Issue activity](https://support.atlassian.com/jira-software-cloud/docs/what-are-the-different-types-of-activity-on-an-issue/) | comments, work logs, history, and activity as distinct records |
| GitHub | [Managing and standardizing pull requests](https://docs.github.com/en/pull-requests/reference/managing-and-standardizing-pull-requests) | review, protected integration, checks, and explicit merge control |
| Microsoft Loop | [Loop components](https://support.microsoft.com/en-us/loop/get-to-know-loop-components) | portable synchronized collaborative components |
| Asana | [Approvals](https://help.asana.com/s/article/approvals) | explicit approve/request-changes/reject decision state |

### Long-running and recoverable operations — 10 product systems

The bounded sample compared ChatGPT deep research, Cursor Agent, GitHub
Actions, Vercel deployments, Stripe PaymentIntents, Shopify bulk operations,
Figma versions, Notion restore/history, Miro board versions, and GitHub Copilot
agent approvals. Additional first-party sources included [GitHub workflow-run
management](https://docs.github.com/en/actions/how-tos/manage-workflow-runs),
[workflow logs](https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs),
[Vercel deployment rollback](https://vercel.com/docs/deployments/rollback-production-deployment),
[Vercel deployment management](https://vercel.com/docs/deployments/managing-deployments),
[Stripe PaymentIntent lifecycle](https://docs.stripe.com/payments/paymentintents/lifecycle),
and [Shopify bulk queries](https://shopify.dev/docs/api/usage/bulk-operations/queries).

## 5. CROSS-PRODUCT COMPARISONS

| Decision | Common mechanism | Meaningful variation | Transfer condition |
|---|---|---|---|
| AI invocation | User can request or trigger bounded assistance | inline suggestion, side panel, artifact editor, research plan, autonomous task | Choose from task/artifact/authority; do not default to chat or a side panel |
| Proposal versus commitment | Human can inspect or influence output | accept token/line, insert draft, apply/reject revision, approve action, direct execution | Friction rises with scope, consequence, irreversibility, and permission |
| Sources and provenance | Origin becomes visible when it affects trust | citations, source panels, connected-source scope, screenshots, content credentials | Persistent media provenance and in-product answer citations solve different problems |
| Uncertainty | Products expose limits or invite verification | explanations, caveats, sources, alternatives, edit/retry; raw probability is uncommon | Make uncertainty actionable; do not fabricate confidence meters |
| Collaboration control | Changes have actors and history | direct co-edit, suggestion, branch/merge, approval, protected integration | Consequence and ownership determine the appropriate control model |
| Communication | Work is discussed near its artifact | anchored comments, issue threads, canvas comments, ephemeral cursor chat | Durability should match whether the conversation must support decisions/audit |
| Presence | Current collaborators may be visible | cursors, avatars, editing indicators, portable shared components | Presence aids orientation; it does not solve permissions, conflict, or history |
| Long-running work | Work has status beyond a spinner | plan/stages, queue, logs, durable IDs, notifications, partial results | Percentage only when measured; background return depends on durable operation state |
| Recovery | Systems provide ways to continue or reverse | retry, resume, cancel, restore version, rollback deployment, rerun workflow | These verbs have different side effects and must match implementation |

## 6. WHAT REAL-UI LEARNED WITHOUT COPYING

- AI is a role in a domain workflow—retrieve, classify, suggest, draft,
  recommend, generate, or act—not a page type or visual identity.
- The transferable AI pattern is a control contract: visible context/data
  scope, proposal-versus-commit boundary, risk-scaled authority, review,
  provenance, interruption, correction, and recovery.
- Editable artifacts, targeted changes, diffs, checkpoints, and history often
  fit creation work better than a transcript-shaped interface.
- Collaboration is a contract among actors, permissions, shared artifacts,
  attribution, communication, concurrency, history, and recovery. Presence is
  only one optional orientation mechanism.
- Direct editing, suggestion, branching, approval, and protected integration
  are not maturity levels of one pattern. They answer different ownership and
  consequence conditions.
- A long-running action is a durable product object with identity, owner,
  state, timestamps, side effects, logs/links, partial outcomes, and recovery.
- Cancel, retry, resume, undo, restore, and rollback cannot be interchanged.
- Representation should follow content relationships and task: comparison,
  sequence, space, hierarchy, relationship, bulk work, narrative, and freeform
  creation should not all collapse into cards.

## 7. NEW KNOWLEDGE ADDED

- `knowledge/ux/ai-automation.md`: role/artifact model, context contract,
  risk-scaled autonomy, provenance, uncertainty, editing/versioning,
  operation states, platform/a11y behavior, anti-patterns, and finish gate.
- `knowledge/ux/collaboration-concurrency.md`: actors/permissions, change
  control, sync/conflict/offline states, attention, history, automation as an
  actor, platform/a11y behavior, anti-patterns, and finish gate.
- `knowledge/ux/operations-recovery.md`: durable operation record and state
  machine, truthful progress, partial outcomes, side-effect-aware recovery,
  background return, high-consequence controls, accessibility, and finish gate.
- DOC-OBSERVED evidence mode and orthogonal knowledge classes.
- A cross-product comparison protocol with a template-gravity rejection gate.
- A 2026 confidence ledger for the three targeted documentary samples.

## 8. EXISTING KNOWLEDGE IMPROVED/CORRECTED

- Product modeling now includes actors/permissions, time/freshness, shared
  state, automation/authority, consequence/reversibility, and
  source/authorship.
- Representation selection now distinguishes comparison, distribution,
  sequence, staged work, hierarchy, relationship, geography, freeform spatial
  creation, commands, and narrative; it states when cards are a poor fit.
- Navigation no longer selects components from destination count alone or
  enforces a universal three-click rule.
- Search now begins with corpus/scope, permission, freshness, ranking,
  retrieval-versus-synthesis, grounding, and recovery. Voice/visual input no
  longer appears as an automatic mobile/vertical feature.
- State guidance no longer assigns progress behavior by a fixed wait duration;
  it distinguishes truthful progress from the full operation lifecycle.
- Data-display guidance removes universal row heights, `title` as overflow
  disclosure, dash-for-every-empty, fixed count-up timing, and automatic
  mobile card conversion.
- Implementation realism now includes durable work, shared-state conflicts,
  and AI proposal/commit states.

## 9. ANTI-TEMPLATE / ANTI-AI IMPROVEMENTS

The anti-pattern system now rejects structural generation habits, not only
purple gradients and glass cards: chat-as-everything, the universal assistant
side panel, prompt/prose replacing domain IA, repeated card shells, AI as
sparkle branding, fake confidence/progress, hidden provenance, irreversible
automation, and identical responsive stacking.

The research method rejects any “lesson” that can be copied as a layout
without knowing target entities, tasks, actors, authority, consequence, and
content shape. One product's AI label, side panel, review UI, or avatar system
cannot become a cross-product default.

## 10. REDESIGN / FULL REDESIGN IMPROVEMENTS

REDESIGN/FULL extraction now preserves non-visual contracts that are easy to
lose while changing composition: permissions, authorship/source/freshness,
automation authority, approvals, sync/conflict behavior, durable operation
state/history, partial outcomes, and recovery. Stage 3.5 re-derives the new IA
using those dimensions. Stage 8 adds an applicable hard gate for control,
shared state, and operations. A redesign that retains a happy-path button but
loses authority, provenance, conflict, or recovery now fails.

The scope boundary remains unchanged: AI, comments, presence, approvals,
history, notifications, or background work are not “modernization” features.
They must be existing, requested, or necessary support UX.

## 11. ROUTING / INTEGRATION CHANGES

- Taxonomy adds AI-assisted/agentic and collaborative products; review,
  co-edit, automation, and long-running interaction; actor/authority,
  operational cadence, consequence/recovery, and provenance axes.
- The retrieval map has explicit rows for all three new modules.
- Dimension activation connects AI actions to operation recovery, shared work
  to collaboration/notifications, and queued/background/bulk/import/export/
  deployment/generation/migration/payment work to operations and states.
- The runtime MODEL stage and finish gate now require the applicable control,
  collaboration, and operation contracts.
- README coverage and knowledge-file count are updated from 120 to 123.

## 12. VALIDATION RESULTS

Initial post-integration executable result:

```text
python -B -m unittest discover -s tests -p "test_*.py" -v
25 tests discovered; 24 passed; 1 environment-dependent Windows
directory-symlink case skipped.
```

New executable invariants verify that the three modules exist and are routed,
their critical contracts remain present, DOC-OBSERVED remains separate from
knowledge class, the removed shortcuts do not return, and README's knowledge
count matches disk. Existing scope, authority, platform, accessibility,
research aggregation, FULL redesign, installer, and routing contracts remain
green. Compile, isolated skill validation, and fresh reasoning scenarios are
recorded after the final run in the validation addendum below.

## 13. REJECTED KNOWLEDGE / OBSERVATIONS AND WHY

- A universal AI badge or IBM Carbon component: one system's documented
  solution, not a cross-product requirement.
- “AI products use chat” or “agents use side panels”: visible shells ignore
  task, artifact, authority, and platform.
- Raw confidence meters as a universal trust mechanism: calibration and user
  interpretation vary; sources, limits, alternatives, and review are often
  more actionable.
- Approval as a security boundary: GitHub's own documentation distinguishes
  workflow convenience from complete security protection.
- Presence/avatars as collaboration completeness: does not establish
  permission, sync, conflict, attribution, history, or restore.
- Ephemeral cursor chat as a durable decision record: its documented lack of
  history makes it unsuitable where accountability or later context matters.
- Fixed navigation destination counts, maximum click counts, table row sizes,
  automatic card stacking, wait-time thresholds, and fake percentages:
  context-free rules that fail across platform, content, input, and risk.
- Features mentioned only in a comparator: product observation is not scope
  evidence for a future design.
- Blocked, plan-gated, region-gated, stale, or third-party summaries were not
  promoted when the named first-party evidence could not establish the claim.

## 14. REMAINING WEAK AREAS

- The new product samples are documentation-observed and concentrated in
  global technology products with English documentation. They do not measure
  regional prevalence, actual accessibility, latency, usability, or runtime
  failure behavior.
- Native mobile and Arabic-first examples of AI/collaboration/long operations
  are underrepresented in this targeted sample; current platform and RTL rules
  reduce risk but do not replace future product observation.
- Complex spatial/relationship representations, multimodal accessibility,
  enterprise policy administration, and offline merge semantics would benefit
  from future bounded runtime/render studies when a concrete product requires
  them.
- Confidence in pattern existence is HIGH for the sampled families; transfer
  remains MEDIUM and must be re-earned from the target product model.

## 15. FINAL ASSESSMENT

REAL-UI is materially stronger in three previously thin, high-impact areas:
AI/agentic control, collaboration/concurrency, and durable operations/recovery.
The improvement is integrated into product modeling, taxonomy, search,
navigation, states, data display, implementation, anti-template guidance,
redesign extraction, routing, evidence classification, and executable tests.

The expansion does not turn current product examples into layouts. It adds
decision variables and failure gates that force future designs to derive their
structure from the product's actors, tasks, artifacts, authority, consequence,
sources, shared state, and operation lifecycle. No showcase was created or
changed for this task, and no remote publication was performed.

### Validation addendum

Final local results:

| Check | Result | What it proves / does not prove |
|---|---|---|
| `python -B -m unittest discover -s tests -p "test_*.py" -v` | PASS: 25 discovered, 24 passed, 1 Windows symlink skip | Executable repository contracts pass; not UI/runtime usability |
| `python -B -m compileall -q research/tools scripts` | PASS | Python sources compile |
| Skill-creator `quick_validate.py` under WSL PyYAML 6.0.3 | PASS: `Skill is valid!` | Frontmatter and skill structure meet validator rules; no dependency added to the repository |
| `research/tools/verify_install.py` with isolated HOME and this repo as source | PASS: 694 source files; all knowledge cross-references resolve; no retrieval ghosts/orphans; YAML safety and tool compilation pass | Source integrity; installed user copies were intentionally not synchronized or compared |
| Scoped `git diff --check` | PASS | No whitespace-error diagnostics in current-task files |

Fresh ephemeral Codex sessions used only the current REAL-UI skill, a
read-only empty workspace, no browsing, no implementation, and the scenario
specification in `tests/v6-reasoning-scenarios.md`:

| Scenario | Observed reasoning outcome |
|---|---|
| S1 Arabic banking agent | PASS: proposal-only AI authority; preparer/approver/execution separated; fraud-review and fee-reservation partial state durable; list/timeline chosen over chat/cards; RTL phone/tablet adaptation |
| S2 collaborative spatial board | PASS: canvas remains primary artifact; anchored comments/history durable; presence ephemeral; stale/conflict/offline merge and automation attribution explicit |
| S3 bilingual bulk inventory import | PASS: desktop grid and focused rugged-mobile flows differ; measured progress only; canceling/canceled/partial distinct; retry/undo/rollback not invented |
| S4 Arabic education tutor | PASS: lesson-first reading workspace; exact bounded sources; editable proposals; grading/open web/records/gamification rejected |
| S5 shared clinical care plan | PASS: no AI invented; proposal is not committed plan; senior approval, stale base version, durable audit, and restore-as-new-version explicit |
| S6 FULL deployment-console redesign | PLAN PASS and final-completion FAIL, as required: capabilities extracted and re-homed in an operations-first queue/inspector, but the run refused to claim completed redesign or render validation without source inspection/implementation |

S1 exposed a routing ambiguity: the retrieval map did not explicitly state
that its paths are relative to `knowledge/`. The skill found the files after a
directory scan, but that is avoidable. `SKILL.md` was repaired before S2–S6 to
state the path base explicitly; the invariant suite now locks this rule.

No browser, native-app, visual, accessibility-runtime, or usability claim is
made: this task intentionally created no interface/showcase artifact. No
GitHub or other remote publication occurred.
