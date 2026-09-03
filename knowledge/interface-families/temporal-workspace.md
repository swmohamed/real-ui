# Interface Family: Temporal Workspace / Calendar / Schedule

Time is the primary axis. Items occupy intervals, availability, or
a day plan. This is not a salon marketplace (labor inventory) and
not a fare calendar (price by date).

Apply `interface-families/README.md`. This catalog never invents
calendars, booking links, reminders, or timezone logic.

Label: REAL-WORLD OBSERVATION (SOURCE-OBSERVED 2026-09-03, wave 24)
plus prior booking and season products (Fresha, Booksy, Treatwell,
Vagaro, Mindbody, NBA, Formula 1). Most consumer calendar apps
returned marketing or login shells (Google Calendar empty title;
iCloud title-only; Outlook failed). Do not invent a week-grid from
those shells.

## Distinct problem space

Users: people who place work or meetings in time, or who publish
availability. Jobs: see when something happens, find a free slot,
hold a resource, avoid collisions. Frequency is daily. Consequence
is a missed handoff or a double-book.

WHEN NOT queue: the item's first key is when, not "next unassigned."
WHEN NOT local-services marketplace: there is no catalog of trades.
WHEN NOT sports org: tickets/standings are not the clock.

## Product families (never average)

| Family | Observed shape | WHY | WHEN | WHEN NOT | TRADEOFF |
|---|---|---|---|---|---|
| Shared work calendar (teamup 12 views / 9 access levels; zoho-calendar AR "تقويم عبر الإنترنت") | people + resources on a shared grid | collisions are the product | teams/resources | public booking pages | a Calendly "pick a time" page on Teamup hides permissions; a week-grid on a one-off booking link is too much chrome |
| Booking / availability page (calendly meetings; cal.com; doodle Group Poll / Sign-up / 1:1; youcanbookme Customizable booking; acuity / setmore / simplybook / appointy / savvycal / tidycal) | the visitor picks a slot from published hours | the job is giving time away | 1:1 or service booking | internal team calendars or fare calendars | Taskrabbit "post a job" on Calendly hides hours; a 12-view team calendar on TidyCal hides Get booked |
| Meeting poll (when2meet 51 inputs / 1 table; doodle Group Poll) | a grid of candidate times, not a booked slot | the group has not chosen yet | find-a-time | confirmed bookings or clinic chairs | a confirmed-slot checkout on When2meet hides the poll |
| Personal planner / tasks-in-time (todoist Task/Project/Time; ticktick To-Do + Calendar; any-do Tasks + Calendar; fantastical Unify calendars; reclaim Habits/Tasks/Smart Meetings; motion AI Task Manager; cron "It's about time.") | tasks and events share a day | the job is planning a person, not selling a slot | individual/team planning | customer-facing booking or sports seasons | booking-page chrome on Todoist hides the list; a season ticket shop on Fantastical hides the day |
| Prior season / slot inventory (nba / formula1 calendars; fresha / booksy slot search — see sports-fitness and local-services) | season or chair-time as inventory | time is stock, not a personal plan | leagues and appointment marketplaces | work calendars | a Reclaim habit engine on Fresha hides the chair |

ALTERNATIVES: shared grid, public booking page, poll grid, task+day
list, season/inventory calendar. Pick from who owns the time and
whether the slot is already a commitment.

Thin / blocked: Google Calendar empty, Square Appointments empty,
Microsoft Bookings UA-block, Proton/Outlook/Letterboxd failed,
Amie title-only. Count fetch-ok; do not invent week-view IA.

## Decision conditions

- **Data shape**: intervals, all-day, recurrence, timezones, capacity.
  If time is only a filter on a table, this may still be a queue.
- **Permissions**: who can see busy/free vs title vs invite. Teamup's
  access levels are the product; do not copy them onto a personal list.
- **Decision speed**: booking pages optimize one decision; work
  calendars optimize scanning a week.
- **Platform**: week/day grids want width; phones collapse to agenda
  unless the task is placing a single slot.
- **RTL / locale**: Zoho Calendar served Arabic. Week-start and
  Hijri/Gregorian are locale contracts (`localization/i18n.md`),
  not decorations. Hours stay LTR numerals.
- **A11y**: do not encode availability by color alone. Keyboard
  movement between days is required if the grid is the product.

## Don't

Fresha slot chrome on a team ops calendar · Teamup 12-view chrome
on a single booking link · inventing AI scheduling because Reclaim
markets it · treating a to-do list as a calendar because it has
dates · a universal "calendar layout."
