# Industry: Insurance (Quote, Cover, Claims, Takaful)

V7.4 split from finance-banking.md. Banks move money you hold. Insurers
price a contingent promise. Do not average a quote/compare home with a
neobank plan matrix or a hospital finder.

Apply `industries/README.md`. This catalog never invents quote engines,
claims, KYC, payments, or cover types.

Label: REAL-WORLD OBSERVATION (SOURCE-OBSERVED 2026-09-03, waves 13+21)
plus DESIGN PRINCIPLE. Thin IR shells count as products; they do not
authorize layout rules.

## Distinct problem space

Users: households and SMEs buying or servicing cover. Jobs: compare
eligible cover, get a quote, bind, renew, file a claim. Consequence is
high and delayed (the product is unused until a loss). Trust is
regulator + claims honesty, not deposit protection. Frequency is low
except claims and renewals.

WHEN NOT a bank: there is no daily balance. WHEN NOT healthcare: the
object is a policy, not a clinician. WHEN NOT comparison-shopping in
general ecommerce: the SKU is underwritten, not picked from a shelf.

## Product families (never average)

| Family | Observed shape | WHY | WHEN | WHEN NOT | TRADEOFF |
|---|---|---|---|---|---|
| Direct quote (geico Coverage That Grows / Get a quote; statefarm product explore + 3 forms; libertymutual bundle-to-save; nationwide Vehicle/Property; godigit 58 inputs; tataaig car/bike; bajaj resume-journey; outsurance start-your-quote; kingprice quote fields; adamjee 13 forms / 61 inputs) | quote CTA + cover lines as the page | conversion is a priced promise against a named risk | consumer P&C/health/motor | group IR or a bank dashboard | a Metal/Go plan tree hides the quote; a claims tracker on an unquoted home invents an account |
| Aggregators (policybazaar compare + calculators + claims/manage; confused.com car-insurance tree; comparethemarket app/previous quotes; coverfox retail+enterprise) | compare many carriers, then bind | the job is shopping the market, not loving one brand | price-led markets | exclusive direct writers | carrier chrome on an aggregator fakes loyalty; aggregator density on a takaful home hides Sharia terms |
| Takaful / Sharia cover (salama-takaful Auto/Health/Life; etiqa insurance and takaful; sukoon Personal/Business) | product lines plus faith/contract framing | the contract type is the differentiator | GCC/SEA takaful | conventional quote clones | Inter+blue on Salama is unearned; a UK aggregator on a takaful site hides wakala/mudaraba terms |
| Regional binders (porto-seguro pt-BR seguros+bank+saúde; gnp-mx Personas/Empresas; discovery-za Medical aid/Bank/Vitality; income-sg Protection/Wealth; great-eastern life stages; hdfc-ergo / starhealth / acko IN) | local-language cover catalog, sometimes bundled with bank or vitality | in-market regulation and language decide IA | national insurers | copying GEICO onto Porto or Discovery | vitality/bank tabs are earned only when those products exist |
| Group IR (aviva plc results; generali results; mapfre corporativa; oldmutual share price; sanlam investor centre; hollard thin; allstate "site update"; qic mixed products+IR; axa/prudential from prior corpus) | results, sustainability, investors | the public site serves capital markets | listed groups | consumer quote homes | IR chrome on a quote site hides the form; quote wizards on IR hide filings |

ALTERNATIVES: quote-first home, aggregator compare, takaful product tree,
regional bundle, IR. Pick from who underwrites and whether the visitor is
buying cover or reading results.

Thin this wave: aami empty nav, directline empty, allstate maintenance.
Count them; do not invent a quote IA from empty markup.

## Arabic / RTL / a11y

Tawuniya and GIG KSA were fetch-failed. Sukoon/Salama/QIC served EN.
Do not invent an Arabic quote wizard from those misses. When Arabic is
in scope: RTL forms, Western digits for sums, Hijri only if the product
shows it, claims copy in MSA. Contrast and focus on quote errors matter
more than illustration (accessibility/floor.md).

## Don't

Bank dashboard on an unquoted visitor · hidden excess/exclusions until
bind · fake countdown on a non-expiring quote · hospital-directory chrome
on motor cover · aggregating families into one "insurance layout".
