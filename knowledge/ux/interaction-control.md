# Interaction Control (selection, manipulation, saving, latency)

Use for high-volume work, multi-select or bulk actions, editors, reordering,
autosave, optimistic updates, slow commands, or any interaction where the
system can diverge from the user’s intent.

Label: RECOMMENDED synthesis from current Windows commanding guidance, WCAG
2.2 input requirements, and cross-product operational patterns. Platform
files decide native expression.

## Model the command before the control

For each command specify:

`target(s) → preconditions → effect → side effects → duration → authority → completion evidence → reversibility → failure/recovery`

Place frequently needed commands near the object or work surface when space
and clarity allow. Put secondary/contextual commands in a discoverable menu or
command surface. Hidden accelerators—hover, right-click, swipe, drag, shortcut,
voice—must have an input-agnostic path.

## Selection contract

- Distinguish focus, hover, active/pressed, current item, and selected state.
- Define single, toggle, contiguous range, and select-all semantics only when
  the collection and platform need them.
- Show selected count and the scope of “all”: visible page, filtered result,
  loaded items, or entire dataset. Never let “Select all” be ambiguous.
- Preserve or clear selection deliberately after filter, sort, pagination,
  refresh, permission change, and completed action; announce the result.
- Bulk actions operate only on eligible items. Explain skipped/ineligible
  items before commitment or in a precise partial-result summary.
- Keyboard and assistive-technology semantics must match the widget model;
  do not bolt checkbox visuals onto an incompatible interaction pattern.

## Direct manipulation and drag

Drag can make spatial relationships tangible, but it is not a complete
command channel. Provide a non-drag single-pointer alternative for WCAG 2.5.7
unless dragging is essential, plus a keyboard-accessible path under the
applicable keyboard requirements. Expose grab/move/drop state, valid targets,
autoscroll, cancel, and the final order or position. Avoid precision-only drop
zones; allow undo when reordering has consequence.

## Save and commit models

Choose and name one model per artifact or operation:

| Model | Required feedback |
|---|---|
| Explicit save | dirty state, save command, saving, saved/version, failed save, close/navigation behavior |
| Autosave | edited/saving/saved/failed/offline/conflict state, durable checkpoint, and what closes safely |
| Optimistic update | immediate local result, pending marker when consequential, server rejection restoration, and retry/undo |
| Draft then commit | private/draft scope, review boundary, authority, committed result, and history |

“Saved” means durably accepted by the responsible system, not merely rendered
locally. Never use both silent autosave and an unexplained Save button.

## Latency and feedback

- Immediate local response should acknowledge input without fabricating
  completion. If duration or outcome matters, expose pending/queued/running.
- Preserve context during refresh. Avoid replacing an entire usable surface
  with a skeleton for a small background update.
- Disable duplicate submission only for the command in flight; keep safe
  navigation and cancellation available when the operation supports them.
- State what finished, what did not, and what the user can do next. Route
  long-running and partial operations to `ux/operations-recovery.md`.
- Optimistic behavior is a risk decision. Prefer confirmed server state for
  irreversible, financial, permission, inventory, or scarce-resource changes.

## Destructive and consequential actions

Use friction proportional to consequence and reversibility: direct action +
undo for low-risk reversible change; confirmation for high-impact or broad
scope; typed/re-auth confirmation only when risk justifies the cost. The
confirmation names the object count, effect, and recovery reality. Never use
generic “Are you sure?” copy.

## Finish gate

- [ ] command target, scope, authority, side effects, and completion evidence are explicit
- [ ] focus/current/selected states cannot be confused
- [ ] bulk scope and partial eligibility are visible
- [ ] hidden accelerators have input-parity paths; drag has required alternatives
- [ ] save model and durability language are truthful
- [ ] pending, rejected, offline, conflict, retry, and undo/recovery states fit the consequence
- [ ] rapid repeat, stale data, filter/sort changes, and window/input switches do not corrupt intent

Connects: ux/{states,operations-recovery,collaboration-concurrency}.md ·
input/{touch,mouse-keyboard}.md · accessibility/{floor,mobile}.md ·
platforms/desktop-native.md.
