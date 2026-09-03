# Interface Family: Conversation Space

The primary object is a CONVERSATION: a DM, group, channel, thread,
or mailbox. People take turns. Unread, presence, and reply matter.
This is not a public feed, not a ticket queue, and not a document.

Apply `interface-families/README.md`. This catalog never invents
channels, huddles, encryption, or agents because "chat products
usually have them."

Label: REAL-WORLD OBSERVATION (SOURCE-OBSERVED 2026-09-03, waves
32 and 36) plus prior social-community Discord observation and V6
DOC-OBSERVED Slack. Public URLs are mostly marketing. They prove
positioning. They do not authorize invented message lists. Play
listings prove claimed messaging/call/encryption capabilities, not
bubble chrome.

V7.5 rejected email/messaging this wave because Gmail/Outlook/Proton
failed or were app-gated, and Slack/Discord already lived under
social/collaboration. Wave 32 retained **28/32** fetch-ok products
across consumer messengers, team channels, and mailboxes. The
dedicated family is justified because those jobs cross industries
and are not decided by `social-community.md` (feeds) or
`work-queue.md` (tickets). Slack still collaborates; Discord still
is a community product. The workspace shape is conversation.

## Distinct problem space

Users: people talking to people (or to a named channel). Jobs: reach
someone, keep a thread findable, know what is unread, sometimes call.
Frequency is high. Consequence ranges from a joke to a classified
ops channel.

WHEN NOT work-queue: Intercom/Zendesk/Front already in work-queue —
the home object is a ticket/customer waiting, even when the body is
chat. WHEN NOT social feed: Reddit/Twitter posts are broadcast
objects. WHEN NOT docs: a wiki page is not a thread. WHEN NOT
calendar: Fastmail sells email+calendar; the mail family is still a
mailbox, not Teamup.

## Product families (never average)

| Family | Observed shape | WHY | WHEN | WHEN NOT | TRADEOFF |
|---|---|---|---|---|---|
| Consumer messenger (signal "Speak Freely"; telegram Messenger; line-me "always at your side"; wechat Chats · Calls · Life Services; viber Free and secure calls and messages; threema Highly Secure Communication; session-app "Send Messages, Not Metadata"; wire Secure Messenger; whatsapp Play listing) | 1:1 and small groups; calls often first-class | the job is reach a person privately | personal/mobile messaging | a company helpdesk or a public feed | Ticket stages on Signal hide the person; a Reddit-style feed on LINE hides the thread |
| Community / group chat (discord "Group Chat That’s All Fun & Games"; revolt fetch now **Stoat** "open-source group chat") | servers/communities + channels | the job is belong and talk in a place | communities, games, fandom | 1:1 encrypted messengers or email | Drive-style folder trees on Discord hide the channel; email folders on a Discord server hide presence |
| Team channels (slack Channels / Messaging / Huddles / Slack Connect; google-chat AI-powered chat for teams; zulip "Organized chat for distributed teams" / async; twist "Work communication that won’t distract you"; mattermost / rocket-chat mission-critical comms; element Matrix collaboration; pumble / flock / ryver team hubs; matrix-org open network) | named channels + threads + (maybe) async | the job is work conversation that must be found later | internal teams | consumer IM or CX tickets | A support SLA board on Zulip hides topics; Discord playfulness on Mattermost hides sovereignty claims |
| Email mailbox (fastmail Email and calendar; hey-email "fresh take on email + calendar"; tuta / mailfence secure email; zoho-mail **Arabic locale** `lang=ar` business mail) | messages + folders/filters/search | the job is asynchronous addressed mail | email as the product | live chat or a ticket queue | Channel unread dots on Fastmail hide folders; a Slack huddle on HEY hides the inbox. Proton Mail timed out this wave — do not invent its three-pane chrome |

ALTERNATIVES: person-first IM, community servers, topic/channel chat,
async threads, mailbox. Pick from who is addressed, whether presence
matters, and what "done" means (read vs resolved).

Skip / thin: ms-teams UA-block (same Microsoft interstitial as
OneDrive); whatsapp.com HTTP 400 (Android listing exists); messenger
not_html; proton-mail timeout; guilded not_html. Revolt redirected to
Stoat — same product, new name; do not treat as two products.

Customer-messaging vendors (Intercom, Front, Zendesk) stay in
`work-queue.md`. They are not this family just because bubbles appear
in marketing.

## Decision conditions

- **Data shape**: turns in a thread, unread, participants, time.
  If the item has assignee + status as the home fields, it is a queue.
- **Permissions**: who can join, history-share, export, or admin a
  space. Encryption claims are positioning until runtime-observed.
- **Decision speed**: live messengers optimize the next reply; Zulip
  and Twist optimize later reading; mail optimizes search and
  folders.
- **Platform**: consumer messengers are mobile-native (Play listings).
  Team chat marketing is desktop-class. Do not stack a three-pane
  mail client onto a phone.
- **A11y**: live regions for new messages without stealing focus;
  transcripts for calls; don't rely on color-only unread.
- **RTL**: Zoho Mail served Arabic marketing this wave. Chrome flips;
  addresses, Message-IDs, and code stay LTR.

## Don't

A KPI dashboard as Slack home · averaging Signal, Discord, Zulip, and
Fastmail into one "chat UI" · inventing huddles because Slack named
them · treating WhatsApp as a helpdesk · copying Discord's server rail
onto Threema · using email three-pane chrome as the universal
professional layout.
