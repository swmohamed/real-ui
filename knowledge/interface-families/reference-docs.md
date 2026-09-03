# Interface Family: Reference / Documentation / Knowledge Base

The job is to find a topic and read or look up a fact. The durable
object is a TREE OF PAGES, not a story river and not a queue of work.

Apply `interface-families/README.md`. This catalog never invents
version switchers, search, accounts, or API playgrounds.

Label: REAL-WORLD OBSERVATION (SOURCE-OBSERVED 2026-09-03, wave 23)
plus prior corpus (JSTOR, Semantic Scholar, MedlinePlus, WebMD,
Cornell LII, legislation.gov.uk, arXiv). Distinct from
`pages/article.md` (journalism) and from science-utility query
engines (one box, results ARE the site).

## Distinct problem space

Users: practitioners, operators, citizens, students. Jobs: land on
the right page, see where they are in the tree, jump by search or
TOC, trust the version. Frequency is lookup. Consequence is wrong
action from stale or unsigned docs.

WHEN NOT article: there is no dek/byline/story river. WHEN NOT
queue: pages are not assigned. WHEN NOT dashboard: the home is a
tree or search, not live KPIs.

## Product families (never average)

| Family | Observed shape | WHY | WHEN | WHEN NOT | TRADEOFF |
|---|---|---|---|---|---|
| Encyclopedia / wiki (wikipedia portal language counts; wikipedia-en Main Page / Contents / Random; wikipedia-ar RTL الصفحة الرئيسة, 16 inputs / 6 tables; mediawiki) | search + language/size + topic portals | the corpus is a public encyclopedia | general reference | product handbooks or API refs | Stripe-product tiles on Wikipedia hide language/size; a news river on ar.wikipedia hides the tree |
| Language / platform reference (mdn Resources for Developers; python-docs "3.14.7 Documentation"; php-docs; npm-docs; go-docs Getting Started/References; rust book; kotlin-docs) | versioned reference tree, often a left TOC | the object is a language or API | official language docs | marketing blogs or ticket queues | a helpdesk home on MDN hides the reference; a Wikipedia portal on Python docs hides the version |
| Product / framework handbook (flutter-docs Guides/Learn/Reference; react-docs Learn/Reference; vue-docs Tutorial/API; django-docs; docusaurus Introduction; web.dev HTML/CSS/JS/a11y; stripe-docs Payments/Revenue/Developers; github-docs; gitlab-docs) | task guide + API reference as siblings | users switch between "how" and "what" | product docs | encyclopedias or legislation | an encyclopedia language-grid on Flutter hides Guides; a tutorial narrative on Stripe API hides the object |
| Official / legal text (prior lii-cornell, legislation.gov.uk, kenyalaw, moj-sa — see government-public) | search/browse an authoritative instrument | the page IS the law or filing | public legal corpora | vendor handbooks | Docusaurus tour chrome on legislation.gov.uk hides the Act |
| Help center / support KB (notion-help "Hi, how can we help you?" + popular topics; arxiv-help contents) | question-first search + topic cards | the visitor has a problem, not a syllabus | product help | language references | an MDN reference TOC on Notion Help hides the question |

ALTERNATIVES: language portal, versioned TOC, learn+reference split,
statute search, question-first help. Pick from whether the reader is
learning, looking up, or solving an incident.

Thin this wave: git-docs not HTML, apple-dev JS-only, android-docs
failed, aws-docs empty title, gitbook marketing ("knowledge layer
for AI"), mdn-ar served English. kubernetes-docs retained 692 inputs
— count the product, do not invent a form from the count.

## Decision conditions

- **Data shape**: hierarchical pages with stable IDs, maybe versions
  and languages. If pages have no tree or search, it may be an article.
- **Freshness**: version and last-updated matter when code or law
  changes. Undated docs are a trust defect.
- **Permissions**: public read vs signed-in vs internal. Do not put
  login walls on a public statute.
- **Representation**: tree + reading column is a candidate, not a
  law. Large APIs need search-first. Encyclopedias need language
  and size before a TOC.
- **RTL**: wikipedia-ar is SOURCE-OBSERVED RTL with a real tree.
  TOC on the end edge; code/API tokens stay LTR.
- **A11y**: skip-to-content, heading order, and in-page TOC are the
  product, not decoration (`accessibility/floor.md`).

## Don't

Newspaper section wells on MDN · helpdesk ticket chrome on Python
docs · inventing a playground because Stripe has one · treating
GitBook marketing as a docs tree · averaging Wikipedia, Stripe
Docs, and Notion Help into one "knowledge base layout" · treating
a Drive folder as a docs tree (`interface-families/asset-library.md`).
