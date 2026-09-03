# Long-Running Operations, Progress, and Recovery

A long-running action is not a spinner stretched over time. It is a durable
product object with identity, state, ownership, side effects, and recovery.
This applies to imports, exports, generation, research, uploads, payments,
deployments, builds, analyses, migrations, bulk edits, and agent tasks.

Knowledge class: **DESIGN PRINCIPLE + IMPLEMENTATION GUIDANCE**, grounded in
10-product **DOC-OBSERVED** comparison plus WCAG 4.1.3 status-message guidance;
see `research/reports/v6-evidence-driven-expansion.md`. WCAG semantics are a
**STANDARD REQUIREMENT** for applicable web content; product-state choices are
not.

## Model the operation

Create an operation record, whether or not it becomes a visible "job" entity:

`operation ID -> object/action -> initiator -> created/updated -> current state
-> measured progress -> result/partial result -> side effects -> log/evidence
-> cancelability -> retry/undo/rollback/resume -> permissions`

The user must be able to answer: What is running? On what? Who started it? Is
it safe to leave? What has already changed? What needs me? Where will the
result live? What can I do if it fails?

## State model

Use only states the product can distinguish, but do not collapse meaningful
differences into loading/success/error.

| State | User-facing contract |
|---|---|
| draft/configuring | inputs and scope are still editable; nothing committed |
| queued/scheduled | accepted but not started; position/time only when real |
| running | current stage or measurable work, start/update time, safe exit behavior |
| waiting for user/approval/permission | exact decision or missing requirement; work retained |
| waiting for dependency | identify dependency and retry/escalation path without blaming the user |
| partial | valid completed subset, missing/failed subset, and whether continuation is possible |
| succeeded | result, side effects, completion time, and next useful action |
| failed | failed stage/object, preserved work, safe retry or alternative |
| canceling/canceled | cancellation is requested vs confirmed; name retained side effects |
| superseded/rolled back | replacement/current version and audit link remain visible |

`canceling` matters when stop is asynchronous. A Cancel click is not proof that
work stopped.

## Progress honesty

- Show a percentage only when numerator and denominator are real and monotonic
  enough to help. Never animate a fake 0→99% timeline.
- When total work is unknown, show the current named stage, completed units,
  elapsed time, or indeterminate activity. Estimates need an evidence basis and
  an "updated" policy.
- For multiple items, show completed / failed / skipped / pending counts and
  preserve item-level outcomes. "Completed with 17 failures" is not success.
- Progressive results may be usable before completion. Label completeness and
  freshness, and avoid reordering the user's reading position as results arrive.
- Logs and technical detail belong behind disclosure unless the user is
  diagnosing the operation; do not hide the plain-language state inside logs.

## Cancel, retry, undo, and rollback are different

- **Cancel/interrupt** stops remaining work if the system can stop it. State
  what already happened and what cleanup continues.
- **Retry** creates another attempt. Reuse a safe operation identity or
  idempotency key so repeated clicks do not duplicate payments, imports, or
  messages. Offer failed-item-only retry when valid.
- **Undo** reverses a user-visible change within a bounded model. Do not promise
  it when downstream side effects cannot be reversed.
- **Rollback/restore** selects a known prior state/version. Show which related
  configuration/data is and is not included.
- **Resume** continues retained work after interruption; it is not a restart
  unless clearly labeled.

The interface must use the verb that matches the backend guarantee.

## Attention, backgrounding, and return

- Let users leave when the operation can run safely in background. Preserve a
  durable activity/operations location instead of requiring the original tab.
- Notify on completion, required action, or meaningful failure according to
  urgency and user preference. Deep-link to the operation/result, not home.
- Returning users see current state and changes since departure. Avoid replaying
  every transient message.
- On phone/native, respect platform background execution and notification
  limits. Do not promise progress the OS can suspend.
- For a queue, use list/table/chronological representation with filters by
  state, owner, object, and time when volume demands it; not a wall of cards.

## High-consequence and shared operations

- Before commit, summarize target, count/scope, irreversible effects,
  permissions, and notification/audience impact.
- Separate approval from execution state: approved does not mean completed;
  running does not mean approved by the right person.
- Shared operations record the initiating human, executing service/automation,
  approvals, and result. Connect to `ux/collaboration-concurrency.md`.
- Payments and other asynchronous transactions need domain state machines.
  "Submitted" or `processing` is not `succeeded`; fulfillment follows the
  authoritative completion state.

## Accessibility

- On web, status messages must be programmatically determinable without
  stealing focus when WCAG 4.1.3 applies. Use appropriate `status`, live-region,
  log, and progress semantics; a `progressbar` value alone may not announce
  updates.
- Announce meaningful milestones, required actions, failures, and completion;
  do not announce every token, row, or percentage tick.
- Every progress indicator has a visible/programmatic name. Indeterminate and
  determinate states are distinguishable without color or motion.
- Cancel/retry/open-result controls stay keyboard reachable, keep focus stable,
  and meet the relevant platform target guidance. Respect reduced motion.

## Anti-patterns

- Spinner with no operation identity, scope, exit behavior, or recovery.
- Fake percentage/ETA; success toast before authoritative completion.
- Disabling the whole product while independent work runs.
- Cancel that merely hides UI; retry that duplicates side effects.
- Failure that discards completed units, user input, or diagnostic reference.
- Notification flood for every stage; completion notification with no result
  link.
- Bulk success summary that conceals failed/skipped items.
- Logs as the only explanation; color as the only state signal.

## Finish gate

[ ] durable operation identity and actor [ ] truthful state machine [ ] progress
is measured or explicitly indeterminate [ ] safe-to-leave behavior stated [ ]
waiting/partial/canceling states covered [ ] cancel/retry/undo/rollback/resume
semantics match implementation [ ] side effects and partial results preserved
[ ] high-consequence approval/execution separated [ ] background return and
notifications designed [ ] accessible status announcements are useful, not
noisy [ ] mobile/offline/shared-state consequences specified
