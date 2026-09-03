# Collaboration, Concurrency, and Shared State

Collaboration is not an avatar row. It is a system of roles, shared artifacts,
authorship, change control, communication, recovery, and attention. Presence
may help orientation, but it does not resolve permissions or conflicting work.

Knowledge class: **DESIGN PRINCIPLE + RECOMMENDATION**, grounded in an
11-product **DOC-OBSERVED** comparison (Google Docs, Figma, Notion, Miro,
Airtable, Linear, Slack, Jira, GitHub, Microsoft Loop, and Asana) recorded in
`research/reports/v6-evidence-driven-expansion.md`.

## Model the collaboration contract

Record:

`artifact -> actors/roles -> edit granularity -> sync model -> consequence of
conflict -> source of truth -> review/approval -> history/restore -> attention`

Actor roles may include owner, administrator, editor, contributor, commenter,
reviewer, approver, viewer, external guest, service/integration, automation,
and AI. Do not collapse them into "user" when their authority differs.

For each shared entity, answer:

- Who can discover, view, comment, change structure, change values, approve,
  share, export, restore, delete, and automate it?
- Are edits live, autosaved, explicitly submitted, suggested, branched, or
  queued offline?
- What happens when two actors change the same field/object or an old client
  edits stale data?
- Where can a returning participant see the meaningful delta since their last
  visit?
- Which history is recoverable, and which log is merely informational?

## Choose the change-control model from risk

| Condition | Candidate model | Why |
|---|---|---|
| low-risk co-creation with mergeable changes | direct co-edit with presence and autosave | flow matters more than formal approval |
| feedback without edit authority | anchored comments or suggestions | preserves authorship and keeps source content stable |
| consequential artifact with an accountable owner | request changes / approve / reject | decision and responsibility are explicit |
| large or system-wide change | branch/copy, compare, conflict resolution, merge | isolates exploration from the source of truth |
| structured records with independent fields | field-level optimistic editing plus version checks | avoids locking the whole record unnecessarily |

These are alternatives, not maturity levels. A small team may need approval for
payments and direct editing for notes in the same product.

## Shared-state states

- **Presence**: who is viewing/editing and where, only when it helps
  coordination. Allow noise reduction on crowded canvases. Never encode identity
  by color alone.
- **Local/unsynced**: show that a draft or edit has not reached the source of
  truth. "Saved" must not mean "saved only on this device" without saying so.
- **Synced**: name the last confirmed state/freshness when users make decisions
  from changing data.
- **Stale**: the artifact changed since this view or edit began. Offer refresh,
  compare, or safe merge without discarding input.
- **Conflict**: show the affected object/field, both values/authors/times, and
  the consequence of each resolution. Preserve both when automatic merging is
  unsafe.
- **Locked/controlled**: state who or what controls the lock, why, and how to
  request access or continue read-only.
- **Restored**: restoring an old version creates a new current event; it should
  not erase the fact that later versions existed.

Last-write-wins is acceptable only when the content is low-risk, overwrite is
obvious, and history/recovery is sufficient. It is not a default concurrency
strategy.

## Communication and attention

- Anchor discussion to the smallest stable object that carries context: text
  range, record, layer, cell, issue, or change set. Also provide an artifact-
  level channel for cross-cutting decisions.
- Distinguish ephemeral coordination (live cursors, temporary cursor chat) from
  durable decisions (comments, review notes, activity/history). Do not use an
  ephemeral surface for accountable work.
- Resolve/archive discussions without making them undiscoverable. Reopen and
  filter unresolved/assigned-to-me/unread where volume warrants it.
- A mention routes attention; it does not grant access. If the recipient cannot
  open the target, state that before sending or provide an access-request path.
- Notifications deep-link to the exact object/change. Bundle low-urgency edits
  into catch-up summaries; do not emit one interruption per keystroke.
- "Since you left" should summarize decisions, ownership, conflicts, and
  required actions—not merely list every event.

## Permissions and sharing

Sharing controls must name the artifact, audience, access level, inheritance,
external status, and expiry/revocation when applicable. Surface effective
access, not only the setting being edited.

- Separate view, comment/suggest, edit values, edit structure, approve, share,
  export, administer, and automate when the product risk needs that granularity.
- Explain inherited or link-based access and downstream exposure before a
  sensitive share.
- Provide request-access and request-elevated-access paths without implying
  approval.
- Destructive shared actions name affected people/objects and whether recovery
  is possible. Use `ux/operations-recovery.md` for the actual operation.
- Automations and AI appear as actors in history when they create, edit, move,
  classify, or delete shared content. Record the human approval separately.

## Platform and accessibility adaptation

- Desktop/pointer surfaces can show collaborator location, side-by-side diffs,
  anchored discussion, and keyboard review. Hover-only authorship or actions
  still fail keyboard and touch users.
- Phone layouts should preserve the decision and response path even if rich
  presence, full diffs, or history comparison move to a focused view. Do not
  turn mobile into view-only unless the product role truly is view-only.
- Offline editing requires a visible queue, per-item sync outcome, and conflict
  recovery after reconnect.
- Screen readers need author, change type, state, and comment anchors in a
  predictable reading order. Rate-limit live collaboration announcements and
  provide an activity log instead of narrating every remote keystroke.
- RTL/mixed-script collaboration must isolate names, handles, code, IDs, dates,
  and changed text independently; spatial comment anchors mirror with the
  canvas, while chronological sequence remains chronological.

## Anti-patterns

- Decorative avatars with no usable presence, permissions, or identity text.
- "Saved" while remote sync failed; silent last-write-wins on consequential
  records.
- Comments detached after the underlying object moves or changes.
- Direct edit, suggestion, and approval rendered identically.
- A single Owner/Editor/Viewer model for products whose structure and data have
  different risk.
- Activity feeds with every event but no filter, delta, or next action.
- Restoring history destructively or hiding versions created after restore.
- AI/automation changes attributed to the nearest human collaborator.

## Finish gate

[ ] actors and permissions modeled [ ] source of truth and sync language clear
[ ] direct edit/suggest/approve/branch chosen by consequence [ ] stale/conflict/
offline states specified [ ] authorship and automation attribution preserved
[ ] durable vs ephemeral communication intentional [ ] mentions and access not
conflated [ ] history and restore behavior explicit [ ] catch-up/notification
load designed [ ] mobile/keyboard/screen-reader/RTL paths remain complete
