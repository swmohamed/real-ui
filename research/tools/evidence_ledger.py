#!/usr/bin/env python3
"""STRICT evidence ledger: counts only fetch-retained REAL PRODUCTION
PRODUCTS (v2 corpus batches + growth waves; each entry has a retained JSON
record with the fetched URL, final URL, and extracted structure evidence).

Non-product sources (module-observed names, V7 DOC studies, platform docs,
design systems) are SUPPORTING ONLY and never count toward the 20 floor.

Outputs research/reports/evidence-ledger.md with:
- per-category strict count + PASS/FAIL at 20 real products
- supporting non-product source counts (separate column)
- per-product traceability rows (name, url, final_url, observed summary)
"""
import glob, io, json, os, re
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REPORTS = os.path.join(ROOT, "research", "reports")

TAG2CAT = {
 'news':'news-media','news-print':'news-media','news-tv':'news-media','tech-media':'news-media','magazine':'news-media','finance-media':'news-media','tv-media':'news-media','events-media':'news-media',
 'gaming-media':'entertainment-streaming','streaming':'entertainment-streaming','streaming-live':'entertainment-streaming','music':'entertainment-streaming','video':'entertainment-streaming','edtech-video':'education',
 'banking':'finance-banking','fintech':'finance-banking','crypto':'crypto-web3','insurance':'finance-banking','investment':'finance-banking','neobank':'finance-banking','nonprofit-finance':'finance-banking',
 'dev-platform':'saas-dev','dev-tool':'saas-dev','dev-infra':'saas-dev','ai-product':'saas-dev','design-tool':'saas-dev','saas-payments':'saas-dev','saas-productivity':'saas-dev','productivity-saas':'saas-dev','marketing-saas':'saas-dev','productivity':'saas-dev','ecommerce-saas':'saas-dev','saas-b2b':'b2b-enterprise','enterprise-saas':'b2b-enterprise','enterprise-b2b':'b2b-enterprise','consulting':'b2b-enterprise','manufacturing':'b2b-enterprise',
 'edtech':'education','government':'government-public','telecom':'government-public','tourism-government':'government-public','energy':'science-utility','utility-weather':'science-utility','science':'science-utility','science-publishing':'science-utility','nonprofit':'government-public','nonprofit-global':'government-public','health-global':'healthcare','healthcare-public':'healthcare','pharmacy-retail':'healthcare',
 'real-estate':'real-estate','travel-booking':'travel-tourism','travel-marketplace':'travel-tourism','travel-search':'travel-tourism','budget-airline':'travel-tourism','transportation':'travel-tourism','restaurants':'restaurants-food','food-delivery':'restaurants-food','restaurants-discovery':'restaurants-food','logistics':'logistics-delivery',
 'browser-gaming':'gaming','indie-gaming':'gaming','gaming-store':'gaming',
 'marketplace':'ecommerce-marketplace','retail-electronics':'ecommerce-marketplace','ecommerce-tech':'ecommerce-marketplace','home-retail':'ecommerce-marketplace','toys-commerce':'ecommerce-marketplace','fashion-sport':'fashion-luxury-beauty','beauty':'fashion-luxury-beauty','fragrance-retail':'fashion-luxury-beauty',
 'sports-media':'sports-fitness','sports-scores':'sports-fitness','fitness':'sports-fitness','sports-league':'sports-fitness',
 'publishing':'creative-culture','photography':'creative-culture','art-museum':'creative-culture','creative-portfolio':'creative-culture','creative-community':'creative-culture','creator-economy':'creative-culture','portfolio-platform':'creative-culture','events':'creative-culture',
 'social-community':'social-community','community-forum':'social-community','professional-social':'social-community','social-discovery':'social-community',
 'automotive':'automotive','automotive-luxury':'automotive','jobs':'jobs-recruitment','vr':'immersive-experimental',
}
ORDER = ["news-media","ecommerce-marketplace","saas-dev","finance-banking","education","healthcare","government-public","entertainment-streaming","gaming","sports-fitness","travel-tourism","restaurants-food","fashion-luxury-beauty","real-estate","b2b-enterprise","social-community","creative-culture","science-utility","automotive","logistics-delivery","crypto-web3","jobs-recruitment","islamic-apps","immersive-experimental"]

def to_cat(tag):
    return TAG2CAT.get(tag, tag if tag in ORDER else None)

def norm(n):
    return re.sub(r'[^a-z0-9]', '', n.lower())

def obs_summary(it):
    ev = it.get('evidence') or it.get('html') or {}
    if not isinstance(ev, dict):
        return "structure evidence retained"
    c = ev.get('counts', {})
    bits = []
    if ev.get('title'): bits.append('title')
    if ev.get('nav_sample'): bits.append(f"nav({len(ev['nav_sample'])})")
    if ev.get('h1'): bits.append('h1')
    if isinstance(ev.get('h2'), int): bits.append(f"h2({ev['h2']})")
    elif ev.get('h2'): bits.append(f"h2({len(ev['h2'])})")
    if c.get('forms'): bits.append(f"forms({c['forms']})")
    if c.get('inputs'): bits.append(f"inputs({c['inputs']})")
    if c.get('tables'): bits.append('tables')
    if ev.get('dir') == 'rtl': bits.append('RTL')
    return ", ".join(bits) if bits else "html retained"

def load_products():
    """name -> {cat, url, final, wave_or_v2, summary} for fetch-retained products only."""
    products = {}
    def add(it, src):
        cat = to_cat(it.get('industry',''))
        if not cat or it.get('status') != 'ok': return
        k = norm(it.get('name',''))
        if not k: return
        if k not in products:  # dedupe across v2/waves by name
            products[k] = {
                'name': it['name'], 'cat': cat, 'url': it.get('url',''),
                'final': it.get('final_url',''), 'src': src,
                'region': it.get('region','?'), 'lang': it.get('lang_expected','en'),
                'summary': obs_summary(it),
            }
    for f in sorted(glob.glob(os.path.join(REPORTS, '*.json'))):
        base = os.path.basename(f)
        if not (base.startswith('b') or base.startswith('m0') or base.startswith('m1') or base.startswith('retry')):
            continue
        try: d = json.load(io.open(f, encoding='utf-8'))
        except Exception: continue
        if not isinstance(d, list): continue
        for it in d: add(it, 'v2')
    for f in sorted(glob.glob(os.path.join(REPORTS, 'w*.json'))):
        try: d = json.load(io.open(f, encoding='utf-8'))
        except Exception: continue
        if not isinstance(d, list): continue
        for it in d: add(it, 'growth')
    return products

def supporting_counts():
    """Non-product supporting sources per category (never counted in the floor)."""
    sup = defaultdict(lambda: {'module_names': 0, 'doc_studies': 0})
    for f in glob.glob(os.path.join(ROOT, 'knowledge', 'industries', '*.md')):
        mod = os.path.basename(f).replace('.md','')
        if mod == 'README' or mod not in ORDER: continue
        body = io.open(f, encoding='utf-8').read()
        m = re.search(r"## Strong references(.*?)(?:\n## |$)", body, re.S)
        if m:
            tokens = set(re.findall(r"[A-Z][A-Za-z0-9.\-+&]+(?:\.[a-z]{2,4})?", m.group(1)))
            stop = {"OBSERVED","AR","MENA","UAE","KSA","MSA","GCC","The","AND","UN","Red","Kiva"}
            sup[mod]['module_names'] = len([t for t in tokens if len(t) > 2 and t not in stop])
    doc = {'Uber':'travel-tourism','Airbnb':'travel-tourism','Booking.com':'travel-tourism','Emirates':'travel-tourism','Wise':'finance-banking','NHS App':'healthcare','GOV.UK':'government-public','eBay':'ecommerce-marketplace','IKEA':'ecommerce-marketplace','Uber Eats':'restaurants-food','Spotify':'entertainment-streaming','Netflix':'entertainment-streaming','YouTube':'entertainment-streaming','ESPN':'sports-fitness','Strava':'sports-fitness','Khan Academy':'education','Coursera':'education','Duolingo':'education'}
    for c in doc.values(): sup[c]['doc_studies'] += 1
    return sup

def main():
    products = load_products()
    sup = supporting_counts()
    by_cat = defaultdict(list)
    for p in products.values(): by_cat[p['cat']].append(p)

    out = ["# Evidence Ledger — STRICT mode", ""]
    out.append("Counted: REAL PRODUCTION PRODUCTS only, each with a retained fetch record")
    out.append("(requested URL, final URL, extracted structure evidence). Module-observed")
    out.append("names, DOC studies, platform/standards/design-system sources are SUPPORTING")
    out.append("evidence only and never count toward the 20-product floor. Deduped by")
    out.append("normalized product name across all waves; one entry per product.")
    out.append("| Category | VERIFIED REAL PRODUCTS | supporting non-product sources | Floor |")
    out.append("|---|---|---|---|")
    total = 0
    short = []
    for c in ORDER:
        n = len(by_cat.get(c, []))
        total += n
        s = sup.get(c, {'module_names':0,'doc_studies':0})
        ok = "PASS" if n >= 20 else "**FAIL**"
        if n < 20: short.append((c, n))
        out.append(f"| {c} | **{n}** | {s['module_names']} module-names + {s['doc_studies']} doc-studies | {ok} |")
    out.append(f"| **TOTAL** | **{total}** | | |")
    out.append("")
    out.append("## Per-product traceability")
    out.append("")
    for c in ORDER:
        out.append(f"### {c} ({len(by_cat.get(c, []))} products)")
        out.append("")
        out.append("| Product | URL | Final URL | Region/Lang | Observed | Source |")
        out.append("|---|---|---|---|---|---|")
        for p in sorted(by_cat.get(c, []), key=lambda x: x['name']):
            out.append(f"| {p['name']} | {p['url'][:52]} | {p['final'][:44]} | {p['region']}/{p['lang']} | {p['summary']} | {p['src']} |")
        out.append("")
    io.open(os.path.join(REPORTS, 'evidence-ledger.md'), 'w', encoding='utf-8', newline='\n').write("\n".join(out) + "\n")
    print("\n".join(out[:30]))
    print("SHORT:", short)

if __name__ == '__main__':
    main()
