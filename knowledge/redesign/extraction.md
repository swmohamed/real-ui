# Product Extraction (separate the product from its presentation)

Two proven failure modes this file kills:
1. **Silent capability loss** — FULL REDESIGN replaces the XP bar and
   forgets the capability (progression) it served.
2. **Old-structure anchoring** — the new composition is built by
   improving old sections instead of re-deriving from the product.

Both stem from one omission: the old product was never decomposed into
layers. Extraction does that, ONCE, before re-derivation.

## The four layers (extract ALL before redesigning)

| Layer | Contains | In a FULL redesign |
|---|---|---|
| A. REQUIREMENTS | what the product does, people/context, business purpose, required content, channels, platform, technical constraints, SEO/a11y obligations, target outcomes | PRESERVE |
| B. CAPABILITIES | search · play · resume · progression/XP · points · streaks · personalization · filtering · ranking · account mgmt · history · saved state · notifications… | PRESERVE (re-present freely) |
| C. WORKFLOWS | discover→inspect→play · return→resume recent · check progress→continue | PRESERVE (re-path freely) |
| D. PRESENTATION | hero, split layouts, cards, sidebars, tabs, grids, progress bars, tickers, section order | FREELY RE-DERIVED — never an anchor |

**D is forbidden as an input to the new composition.** Allowed inputs:
A + B + C + constraints + the product model + industry conventions
(*as presentation options for existing capabilities* — never as
features, see scope gate below).

## Extraction procedure (code-first)

1. Walk every route/screen of the old product (HTML/DOM/components/
   data calls; screenshots as evidence).
2. For each visible surface ask: **which capability does this serve?**
   Write the capability, not the component ("progression", not "XP bar").
3. Hunt the subtle ones — they live only in presentation and die
   silently: personalization · progression · continuity/resume ·
   status/streak · filtering · history · saved state · user-specific
   content · recent activity · preferences. Also extract non-visual system
   contracts: actors/permissions · source/authorship/freshness · automation
   authority · approvals · shared-state/sync/conflict behavior · operation
   identity/state/history · partial outcomes · recovery and rollback.
4. Write layer A–D lists. Capabilities = the ledger input; presentation
   list exists only to be audited, never copied.

Also trace the current experience before changing it:

`trigger/entry → task/decision → handoff/wait → result → recovery/follow-up`

Record channels, deep links/notifications/files, backstage dependencies,
support/operations handoffs, accessibility and language needs, and current
success/failure evidence. A redesign can keep every feature and still break the
service by losing a handoff, entry route, continuity cue, or recovery step.

## Capability ≠ presentation (the core distinction)

| Capability | Valid presentations (choose by product model, not habit) |
|---|---|
| Game discovery | grid · carousel · search-first · category explorer · personalized feed · contextual recommendations |
| Player progression | XP bar · level ring · profile stat block · milestone path · header chip |
| Resume gameplay | continue-row · resume hero · dock/persistent control · home task-card |
| Personalization | named sections · adaptive home · "for you" rail · contextual inline |

The redesign may replace ANY representation. It may not remove the
capability unless: user explicitly requested removal · it is proven
unnecessary · requirements establish it no longer exists.

## Capability ledger (every row needs a disposition)

```
PRESERVE                  capability kept, representation may still change
TRANSFORM                 kept, fundamentally re-represented (XP bar → profile ring)
MERGE                     folded into another surface (personalized + discovery → adaptive home)
RELOCATE                  moved to where the model puts its task (continue → persistent dock)
REMOVE WITH JUSTIFICATION capability retired — quote the user/request/requirement
```

No meaningful capability disappears silently. Decorative widgets that
serve no capability are NOT ledger rows — remove freely.

## Coverage matrix (bidirectional — closes loss AND invention)

After the new structure exists, build the matrix:
- **Every ledger row → where it lives now** (surface named). Any row
  without a home = FAIL → restore/transform it.
- **Every new-structure element → which capability/requirement it
  serves.** Any element without a source = suspicious → scope gate.

## Scope fidelity gate (industry ≠ evidence)

Anything NEW in the product must classify as exactly one:

```
EXISTING PRODUCT FEATURE   (was extracted in layer B)
EXPLICIT USER REQUEST      (the request asked for it)
NECESSARY SUPPORTING UX    (enables an existing capability — e.g. the
                            empty/loading/error state OF an existing
                            feature; never a new feature itself)
```

Else: **DO NOT IMPLEMENT IT.** Optional ideas may be suggested in a
separate "not included — say the word" note; they must not enter the
delivered product.

> **Common industry behavior is not product evidence.**
> "Gaming sites often show ads" ≠ "this product should contain ads."
> "SaaS often has subscriptions" ≠ "invent a subscription system."

Invention traps (non-exhaustive): advertising · monetization · premium
tiers · subscriptions · social feeds · chat/messaging · marketplaces ·
accounts (when absent) · loyalty · leaderboards · achievements ·
notifications · recommendation engines · new business models.
Industry files describe these as GENRE OBSERVATIONS for recognition
and presentation — never as scope.

AI assistance, agent actions, real-time presence, comments, approvals,
version history, audit logs, background jobs, notifications, and collaboration
are capabilities—not modernizing decorations. Preserve them when extracted;
do not add them when unsupported. If present, re-derive their control and
recovery using `ux/ai-automation.md`, `ux/collaboration-concurrency.md`, and
`ux/operations-recovery.md`.

## Implementation behavior (codebase edits)

```
Business logic     ≠ component structure   (preserve the first)
Route preservation ≠ page-layout preservation (URLs live; shells change)
Data preservation  ≠ visual representation  (fields live; widgets change)
```

When editing an existing codebase in a genuine redesign you MAY:
restructure containers · rebuild section composition · replace
component types · reorganize page structure · create new composition
components · delete obsolete presentation components — while required
logic, routes, and data survive. "Preserve functionality" never means
"preserve the DOM."

For FULL, `full-redesign-execution.md` makes that permission operational:
the validated new shell is created before old presentation components are
considered for reuse. Logic/data imports are expected; wholesale reuse of the
old page subtree before the new structure exists is a PLAN/implementation
failure.

## Capability-loss test (before finalizing)

> Which capabilities existed before? For each: where is it now —
> preserved / transformed / merged / relocated / justifiably removed?
One line per capability. Any silent disappearance = FAIL (fix before
delivery — validation must be able to change the output).

Also ask: which person entered through which channel and how the journey
completed or recovered; which actor could do what; which changes were suggestions versus
committed; which sources and versions were visible; which shared/operation
states and recovery paths existed? A redesign that keeps the happy-path
button but loses these contracts still loses capability.

Connects: redesign/depth.md (depth classification + structural
validation) · foundations/product-modeling.md (re-derivation engine)
· redesign/workflow.md (stage 1.5 + 3.5 + 8) · industries/* (genre
possibilities — presentation only) · implementation/realism.md
(state completeness OF existing features = supporting UX).
