# Industry: Telecom (Consumer Connectivity)

V7.4 split from government-public.md (where `telecom` was mis-filed) and
from b2b-enterprise.md (where STC-class density was treated as a consulting
portal). A consumer telco sells plans, devices, and prepaid. A ministry
portal completes civic tasks. A group IR site talks to investors.

Apply `industries/README.md`. This catalog never invents coverage maps,
eSIM, M-PESA, TV bundles, or account login.

Label: REAL-WORLD OBSERVATION (SOURCE-OBSERVED 2026-09-03, waves 15+21)
plus DESIGN PRINCIPLE.

## Distinct problem space

Users: prepaid/postpaid subscribers and households buying broadband.
Jobs: pick a plan, buy/recharge a SIM, pair a device, manage a bill,
use a local wallet rail when the operator provides one. Trust is
coverage and bill honesty. Frequency is high (top-up, data). Visual
register is retail-offer density, not GDS sparseness.

WHEN NOT government: the visitor is not renewing a license. WHEN NOT
B2B consulting: the CTA is a plan card, not "Talk to us". WHEN NOT
finance: M-PESA on Safaricom is a wallet rail inside a telco, not a
neobank (see finance-banking.md).

## Product families (never average)

| Family | Observed shape | WHY | WHEN | WHEN NOT | TRADEOFF |
|---|---|---|---|---|---|
| Consumer shop (telstra Personal deals+nbn+devices; ee Phones/broadband/SIM; three-uk offers; free.fr fibre+mobile FR; movistar fibra+móvil+TV; kpn Combivoordeel NL; mintmobile $15/coverage; maxis Mobile/Home/Devices; claro-br Planos Internet/TV/Celular; tim-br Planos Controle, 182 inputs; jazz Prepaid/5G; dialog offers; mtn-ng Devices/Buy SIM; batelco plan+devices; ooredoo-qa Services; personal-ar Mi Personal; entel-cl Hogar y Móvil; inwi fibre; rain-za unlimited 5G; telkom-za device deal) | plans + devices + home internet as first-class nav | the object is a tariff the household will live on | consumer operators | group IR or civic portals | GDS task-grids on EE hide the phone deal; Salesforce mega-nav on Mint hides the prepaid price |
| Locale-first / RTL shops (mobily ar RTL باقات مفوتر/مسبق الدفع/أجهزة; te-egypt WE باقات/We Pay/الحماية الأبوية; telkomsel id Personal/Enterprise; docomo ja disaster board + 料金・割引) | in-language offer home, sometimes with disaster/utility extras | the legal market language is the product | in-market consumer brands | English group sites (vodafone.com, orange.com, eand.com) | Inter+purple on Mobily is unearned; English IR on WE مصر hides prepaid |
| Operator + payments (safaricom Voice/Tariffs/PrePay/PostPay + M-PESA sibling; te-egypt We Pay) | connectivity plus a cash/bill rail | high-frequency top-up expands into payments | MNO wallets | a standalone neobank or a remittance corridor | Paytm-class travel tabs on a SIM shop fake a super-app; hiding M-PESA on Safaricom hides the real job |
| Group IR (vodafone Everyone Connected; orange institutional; mtn Group Interim Results; eand strategy/governance; verizon/stc from prior corpus may be shop or hybrid) | stories, results, sustainability | the visitor is not buying a SIM | listed groups | consumer plan homes | IR on a prepaid page hides recharge; plan cards on IR hide filings |

ALTERNATIVES: plan+device shop, RTL offer home, operator-wallet, group IR.
Match the legal site the user will use. Do not copy STC's 612-link
enterprise tree onto a prepaid MVNO.

Thin this wave: att/airtel/singtel/vodacom/du/optus/spark/kt/giffgaff
empty or near-empty nav. Count them; do not invent a 5G shop IA.

## Arabic / RTL / a11y

Mobily and WE Egypt are SOURCE-OBSERVED RTL consumer shops. Offer
prices need tabular numerals and visible tax. Parental-control and
bill-cap copy is an a11y/plain-language job, not a decoration. Coverage
claims must not be color-only (accessibility/contrast-motion.md).

## Don't

gov.uk task grid on a phone shop · bank plan-matrix on prepaid ·
inventing a super-app because Grab exists · treating group.vodafone.com
as the consumer product.
