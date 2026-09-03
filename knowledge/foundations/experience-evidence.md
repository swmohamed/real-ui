# Experience Evidence (before product and interface decisions)

Use this module when the product, audience, current journey, or success
criteria are unclear; when designing a new service; or when a redesign may
change more than presentation. It does not require fresh research for every
ordinary task. Supplied requirements and known evidence can satisfy it, but
unknowns must stay visible.

Label: RECOMMENDED method synthesized from current GOV.UK Service Manual
guidance and cross-product study. It is not a claim that one research method
fits every team.

## Start with a decision, not a persona template

Write the decision the work must support, then the evidence needed to make it:

| Field | Record |
|---|---|
| Decision | What will change depending on what we learn? |
| People | Actual users, non-users, support/operations staff, and excluded or disabled users who affect the service |
| Context | Trigger, place, device/window, input, time pressure, connectivity, privacy, and social setting |
| Current behavior | What people do now, including workarounds and other channels |
| Desired outcome | What users can accomplish or understand—not which component they prefer |
| Evidence | Requirements, interviews, observation, analytics, support data, operations data, research, or documented product behavior |
| Confidence | KNOWN · SUPPORTED · ASSUMED · UNKNOWN · CONFLICTED |
| Risk if wrong | Scope, safety, inclusion, revenue, workload, trust, or reversibility consequence |

Personas, segments, and journey maps are optional representations. They do not
become evidence by being polished. Prefer specific behavior and context over
invented biographies, demographic stereotypes, or “busy professional” prose.

## Current-experience model

For each top outcome, trace the experience end to end:

`trigger → discover/enter → provide or retrieve information → decide/act → wait/track → result → recover/follow up`

For every stage record:

- user goal, questions, actions, decisions, and evidence available;
- frontstage touchpoint: web, app, phone, email, in-person, document, device;
- backstage dependency: staff, policy, data source, approval, inventory,
  scheduling, fulfillment, model, or external service;
- ownership and handoff, expected duration, failure/exception, and recovery;
- accessibility, language, identity, consent, and support needs;
- output state that lets the next stage start safely.

Do not force a linear “happy journey” when the work branches, repeats, pauses,
or changes channel. Use a state graph, service blueprint, or task tree when it
represents the work more truthfully.

## Task analysis

Break a task into trigger, prerequisite, information required, decisions,
actions, system response, completion evidence, and recovery. Rank tasks using
frequency, criticality, time sensitivity, consequence, and current friction.
No single number decides placement: a rare emergency action can outrank a
frequent low-value action, and a frequent task may enter through a deep link,
notification, OS command, or saved view rather than home.

## Evidence collection and triangulation

Match method to uncertainty:

| Uncertainty | Useful evidence |
|---|---|
| Who/why/context | observation, contextual interview, support and operations review |
| What happens/how often | analytics, logs, task inventory, search/support data |
| Whether people can use it | task-based usability study with representative users and assistive technology where relevant |
| Whether the service works end to end | journey walkthrough, service blueprint, operations and failure-case rehearsal |
| Which direction performs better | prototype comparison or experiment with a predeclared success measure |

One source can mislead. Triangulate behavioral, attitudinal, and operational
evidence where consequence warrants it. Preference is not task success;
click-through is not comprehension; a support ticket count is not the whole
experience.

## Research-to-design trace

Every material decision gets a short trace:

`evidence → interpretation → design decision → expected outcome → validation`

Record counterevidence and rejected alternatives. When evidence is absent,
label the decision RECOMMENDED or ASSUMED and choose a reversible path. Do not
launder a competitor pattern into a user need.

## Success and validation

Choose measures that fit the outcome: completion and error rate, time or
effort, comprehension, recovery success, accessibility barriers, support
burden, operation failure, abandonment, retention, trust calibration, or
business outcome. Include guardrails so improving one metric cannot silently
harm another group or stage.

## Finish gate

- [ ] decision, people, context, current behavior, and desired outcome are explicit
- [ ] top experience is traced through result and recovery, including channels and backstage dependencies where relevant
- [ ] assumptions and conflicts are not presented as facts
- [ ] task priority considers consequence and entry context, not frequency alone
- [ ] material design choices cite evidence or carry an assumption label
- [ ] success criteria and guardrails exist before claiming improvement

Connects: foundations/product-modeling.md · redesign/{extraction,workflow}.md ·
research/method.md · ux/states.md · ux/content-design.md.
