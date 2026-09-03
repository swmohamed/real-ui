# Classification Taxonomy (before retrieval)

Classify EVERY project before loading knowledge. Complex products combine
multiple axes — never force one label. This file drives retrieval combos.

## Axes

| Axis | Values (examples) |
|---|---|
| Primary industry | one of knowledge/industries/* — the business domain |
| Secondary industries | additional domains whose UX leaks in (e.g., sports + finance) |
| Experience evidence | supplied/observed/researched current behavior · assumption · unknown/conflicted; trigger · channel · handoff · outcome · success measure |
| Product type | marketing site · content site · web app · SaaS · dashboard · marketplace · ecommerce · mobile app · utility · social · media · entertainment · game · productivity · enterprise · consumer · internal tool · public service · AI-assisted/agentic · collaborative · hybrid |
| Audience | consumers · professionals · enterprises · developers · children · elderly · Arabic-first · bilingual |
| Business model | subscription · transactional · ad-funded · freemium · marketplace commission · licensed · nonprofit |
| Interaction model | browsing · searching · transactional · real-time · creation · monitoring · communication · review/approve · co-edit · select/bulk · direct manipulation · autosave/optimistic · automate/agentic · long-running/bulk |
| Service/channel model | self-service · assisted · staff-operated · web/app · phone/email · in-person · document/device · cross-channel handoff |
| Actor & authority | owner · editor · contributor · reviewer · approver · viewer · guest · support/admin · automation/agent; suggest · draft · commit · publish |
| Operational cadence | instantaneous · queued · long-running · scheduled · background · recurring · offline/deferred |
| Consequence & recovery | low/high consequence · reversible/irreversible · undo · retry · resume · cancel · rollback · restore |
| Data & provenance | first-party · connected source · generated · user-authored · regulated · live/delayed/versioned |
| Platform | web · iOS/iPadOS · Android · Windows · macOS · Flutter · React Native · SwiftUI · UIKit/AppKit · Jetpack Compose · native desktop · cross-platform |
| Device/window | phone · tablet · foldable · desktop · resizable/multi-window · large screen · TV · wearable |
| Region | global · MENA · GCC · Europe · Asia |
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
