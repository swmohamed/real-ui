# Classification Taxonomy (before retrieval)

Classify EVERY project before loading knowledge. Complex products combine
multiple axes — never force one label. This file drives retrieval combos.

## Axes

| Axis | Values (examples) |
|---|---|
| Primary industry | one of knowledge/industries/* — the business domain |
| Secondary industries | additional domains whose UX leaks in (e.g., sports + finance) |
| Product type | marketing site · content site · web app · SaaS · dashboard · marketplace · ecommerce · mobile app · utility · social · media · entertainment · game · productivity · enterprise · consumer · internal tool · public service · hybrid |
| Audience | consumers · professionals · enterprises · developers · children · elderly · Arabic-first · bilingual |
| Business model | subscription · transactional · ad-funded · freemium · marketplace commission · licensed · nonprofit |
| Interaction model | browsing · searching · transactional · real-time · creation · monitoring · communication |
| Platform | web · iOS · Android · Flutter · React Native · SwiftUI · UIKit · Jetpack Compose · cross-platform |
| Device | phone · tablet · foldable · desktop · large screen · TV · wearable |
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

1. Model the product and write its scope/content-priority ledgers before
   retrieving genre or page patterns (`foundations/product-modeling.md`).
2. Load `industries/README.md`, then retrieve the PRIMARY industry file;
   skim secondaries for overlapping terminology, risk, or workflow only.
   Industry files do not create scope or architecture.
3. Platform + device axes decide platforms/* and devices/* files.
4. Arabic/RTL axis adds rtl/* files (see rtl/global-vs-arabic.md).
5. Product type may activate `pages/README.md` plus relevant page catalogs;
   it never selects a fixed page sequence.
6. Redesign tasks always add redesign/* (start at redesign/workflow.md).
