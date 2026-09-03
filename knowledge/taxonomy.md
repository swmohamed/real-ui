# Classification Taxonomy (before retrieval)

Classify EVERY project before loading knowledge. Complex products combine
multiple axes — never force one label. This file drives retrieval combos.

## Axes

| Axis | Values (examples) |
|---|---|
| Primary industry | one of knowledge/industries/* — the business domain |
| Secondary industries | additional domains whose UX leaks in (e.g., sports + finance) |
| Experience evidence | supplied/observed/researched current behavior · assumption · unknown/conflicted; trigger · channel · handoff · outcome · success measure |
| Product type | marketing site · content site · web app · SaaS · dashboard · marketplace · ecommerce · mobile app · utility · social · media · entertainment · game · productivity · enterprise · consumer · internal tool · public service · super-app · AI-assisted/agentic · collaborative · hybrid · work-queue · reference-docs · temporal-workspace · spatial-canvas · asset-library · conversation-space · dual-role · course-marketplace · academy · bootcamp · corporate-lms · exam-prep · tutoring-marketplace · cohort-school · instructor-platform · open-courseware · practice-workspace · language-habit · certification-path · classroom-lms |
| Interface family | none · work-queue/inbox/triage · reference-docs/knowledge-base · temporal-workspace/calendar · spatial-canvas/inspector · asset-library/files/DAM · conversation-space/chat/mail — a workspace shape, not an industry |
| Audience | consumers · professionals · enterprises · developers · children · elderly · Arabic-first · bilingual |
| Business model | subscription · transactional · ad-funded · freemium · marketplace commission · licensed · nonprofit |
| Interaction model | browsing · searching · transactional · real-time · creation · monitoring · communication · review/approve · co-edit · select/bulk · direct manipulation · autosave/optimistic · automate/agentic · long-running/bulk · triage · schedule · investigate · annotate |
| Service/channel model | self-service · assisted · staff-operated · web/app · phone/email · in-person · document/device · cross-channel handoff |
| Actor & authority | owner · editor · contributor · reviewer · approver · viewer · guest · support/admin · automation/agent; suggest · draft · commit · publish |
| Operational cadence | instantaneous · queued · long-running · scheduled · background · recurring · offline/deferred |
| Consequence & recovery | low/high consequence · reversible/irreversible · undo · retry · resume · cancel · rollback · restore |
| Data & provenance | first-party · connected source · generated · user-authored · regulated · live/delayed/versioned |
| Platform | web · iOS/iPadOS · Android · Windows · macOS · Flutter · React Native · SwiftUI · UIKit/AppKit · Jetpack Compose · native desktop · cross-platform |
| Device/window | phone · tablet · foldable · desktop · resizable/multi-window · large screen · TV · wearable |
| Region | global · MENA · GCC · Europe · Asia · Africa · LatAm · US |
| Language | English · Arabic (RTL) · bilingual Arabic+English · mixed-direction |

## Multi-category examples

- Sports betting/fantasy = sports + finance-banking + real-time data +
  transactional UX + mobile-first
- Food delivery = restaurants-food + logistics-delivery + maps +
  marketplace + transactions + mobile
- Crypto exchange (MENA) = crypto-web3 + finance-banking + real-time +
  bilingual Arabic/English + heavy trust/KYC
- Islamic super-app = islamic-apps + prayer/Quran core + utility +
  Arabic-first + mobile
- Job board = jobs-recruitment + search-discovery + social-community
  (profiles) + bilingual (MENA)
- Motor quote = insurance (not a bank dashboard; not a hospital finder)
- Prepaid telco = telecom (not a civic portal; not consulting IR)
- Home cleaning / salon slot = local-services (not a job board; not food delivery)
- Support inbox = saas-dev or b2b + work-queue (not a dashboard of KPI cards)
- Language docs = saas-dev or science-utility + reference-docs (not a newspaper)
- Team calendar = productivity + temporal-workspace (not Fresha chair inventory)
- Live flight map = science-utility + spatial-canvas (not a Miro whiteboard)
- Academy website = education + family (private academy / instructor-owned / MOOC) + web marketing or logged-in school — never a universal course template
- Exam-prep app = education + exam-prep + mobile + parent/student + test-date clock (not Duolingo streaks, not a corporate LMS)
- Corporate LMS = education + enterprise + licensed + classroom-lms or LXP (vendor marketing ≠ student app)
- Course marketplace = education + marketplace + transactional (not one school's catalog)
- Bootcamp = education + bootcamp + outcomes/application (not a 10k-card store)
- Tutoring product = education + tutoring-marketplace + people search (not a lesson player)
- Instructor-owned academy = education + instructor-platform + the creator's brand
- Certification platform = education + certification-path + verifiable proof
- Team Drive / DAM / send-link = industry + asset-library (not a canvas; not a wiki)
- Messenger / team chat / mailbox = industry + conversation-space (not a ticket queue; not a public feed)
- Host vs guest / driver vs rider = two product models + `ux/roles-surfaces.md` (not one dashboard with a role dropdown)
- Compare flights or specs = compare task + table/matrix (`product-modeling.md`); not a new interface family

## Rules

1. Establish people/context/current experience/outcome evidence when unclear
   (`foundations/experience-evidence.md`), then model the product and write its scope/content-priority ledgers before
   retrieving genre or page patterns (`foundations/product-modeling.md`).
2. Load `industries/README.md`, then retrieve the PRIMARY industry file;
   skim secondaries for overlapping terminology, risk, or workflow only.
   Industry files do not create scope or architecture.
3. Platform + device axes decide platforms/* and devices/* files.
4. Arabic/RTL axis adds rtl/* files (see rtl/global-vs-arabic.md).
5. Product type may activate `pages/README.md` plus relevant page catalogs;
   it never selects a fixed page sequence.
6. Redesign tasks always add redesign/* (start at redesign/workflow.md).
7. AI/automation activates `ux/ai-automation.md`; add
   `ux/operations-recovery.md` when work acts, queues, or runs in background.
8. Shared editing, review, presence, or multiple actors activates
   `ux/collaboration-concurrency.md`. Long-running, bulk, import/export,
   deployment, generation, or payment lifecycles activate
   `ux/operations-recovery.md`.
9. Selection, range/select-all, bulk commands, drag/reorder, autosave,
   optimistic updates, or slow commands activate `ux/interaction-control.md`.
10. Windows/macOS/native desktop/window/document work activates
    `platforms/desktop-native.md`, `devices/desktop.md`, and the relevant input
    module. Window size is live state, not a fixed device label.
11. Interface family (work-queue, reference-docs, temporal-workspace,
    spatial-canvas, asset-library, conversation-space) activates
    `interface-families/README.md` plus the matching family file. It never
    selects a layout. Industry and family stay separate axes.
12. Incompatible actor jobs (host/guest, driver/rider, seller/buyer,
    creator/audience) activate `ux/roles-surfaces.md`. Do not collapse them
    to hidden buttons.
