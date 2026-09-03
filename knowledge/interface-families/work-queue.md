# Interface Family: Work Queue / Inbox / Triage

Items arrive. A person (or agent) processes them and changes state.
This is not a dashboard (monitoring a system) and not a document
(reading or writing one artifact).

Apply `interface-families/README.md`. This catalog never invents
tickets, assignment, SLAs, chat, or AI agents.

Label: REAL-WORLD OBSERVATION (SOURCE-OBSERVED 2026-09-03, wave 22)
plus DOC-OBSERVED V6 collaboration set (Linear, Jira, GitHub, Slack,
Asana) and prior corpus (GitHub, GitLab, Linear, PagerDuty, Grafana,
Reddit). Most wave-22 public URLs are marketing shells — they prove
the product model, not in-app chrome. Do not invent a ticket list
from Zendesk's demo CTA.

## Distinct problem space

Users: operators, agents, reviewers, on-call, sellers. Jobs: see
what arrived, decide next, act, record outcome, move on. Frequency
is high. Consequence varies (a refund vs a production outage).
The object is an ITEM IN A QUEUE, not a page of metrics.

WHEN NOT dashboard: the job is not "how is the system." WHEN NOT
docs: the job is not "understand a topic." WHEN NOT calendar: the
item is not primarily an interval on a clock. WHEN NOT conversation:
the home object has assignee + status as the fields that matter, even
if the body is chat (`interface-families/conversation-space.md`).

## Product families (never average)

| Family | Observed shape | WHY | WHEN | WHEN NOT | TRADEOFF |
|---|---|---|---|---|---|
| Helpdesk / conversation inbox (zendesk / intercom / freshdesk / front / zammad / osticket / gorgias / kayako / zoho-desk AR marketing; prior Slack DOC) | conversation or ticket as the item; status + assignee + customer | the visitor or customer is waiting on a human | support / CX | error monitoring or a sales pipeline | KPI-card dashboards hide the next conversation; sales-pipeline stages on a support inbox fake a funnel |
| Error / incident queue (sentry Error Monitoring / Logs / Session Replay; datadog / newrelic observability marketing; statuspage "Build trust with every incident"; prior pagerduty / grafana) | event or incident as the item; severity + service + time | the job is restore or explain a failure | on-call / SRE | customer-email helpdesks | conversation chrome on Sentry hides stack context; status-page voice on an internal queue hides the next page |
| Sales pipeline / sales inbox (pipedrive Pipeline / Lead / Sales inbox; close-crm calling + email) | deal or lead as the item; stage + next action | the job is moving money through stages | outbound / CRM | support tickets or Git issues | a helpdesk satisfaction score on Pipedrive hides the stage; a board of issues on Close hides the call |
| Issue / work tracker (jira / shortcut / youtrack / redmine / clickup marketing; prior github / gitlab / linear / asana / trello / monday; Linear/Jira/GitHub DOC-OBSERVED) | work item as the item; status + owner + rank | the job is shipping a change | product/eng work | customer inboxes | CX chat on Linear hides rank and cycle; a marketing hero on Redmine is not the tracker |
| Feedback / request queue (canny / uservoice / productboard) | request as the item; votes + status | the job is deciding what to build | public feedback | confidential support | a private ticket inbox on Canny hides the vote; a roadmap board on a Sev-1 queue hides the incident |

ALTERNATIVES: conversation list, severity stream, stage board, ranked
backlog, public request board. Pick from who is waiting and what
"done" means. A board, a list, and a split inbox are representations,
not the family.

Thin / marketing this wave: Zendesk (demo nav only), Help Scout empty,
Jira/YouTrack title-only, Height failed. Count fetch-ok products;
do not invent agent-workspace IA.

## Decision conditions

- **Data shape**: incoming items with state, age, owner, and a next
  action. If there is no arriving set, this is not a queue.
- **Permissions**: who can see, claim, reassign, resolve, or escalate.
  Color-only identity is not enough (`ux/collaboration-concurrency.md`).
- **Decision speed**: interrupt-driven queues need the next item in
  reach; planned backlogs need rank and filters.
- **Risk**: destructive resolve, refund, or page needs confirmation
  and audit (`ux/interaction-control.md`, `ux/operations-recovery.md`).
- **Platform**: desktop split-view is common for volume; phone needs
  one item at a time, not a shrunk three-pane.
- **RTL**: Zoho Desk served Arabic marketing. Item lists flip; IDs,
  logs, and stack traces stay LTR.

## Don't

A 12-widget dashboard as the support home · averaging helpdesk,
Sentry, and Pipedrive into one "admin" · inventing AI agents because
the marketing page named one · treating Reddit/Discourse moderation
as a helpdesk clone (object = post/thread, not a paying customer).
