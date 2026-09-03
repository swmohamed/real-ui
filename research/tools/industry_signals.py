#!/usr/bin/env python3
"""Per-industry aggregated design signals + flagship site deep dives."""
import collections
import json
from pathlib import Path
import re

REPORTS_DIR = Path(__file__).resolve().parents[1] / "reports"

def load():
    sites = {}
    for f in sorted(REPORTS_DIR.glob("*.json")):
        with f.open(encoding="utf-8") as handle:
            report = json.load(handle)
        if not isinstance(report, list):
            continue
        for s in report:
            if s["status"] == "ok" and s.get("css"):
                sites[s["name"]] = s
    return sites

sites = load()
GROUPS = {
 "saas/dev": ["stripe","linear","vercel","openai","anthropic","github","tailwindcss","notion","framer","netlify","figma","supabase","gitlab","cloudflare","asana","trello","slack","dropbox","mailchimp","hubspot","salesforce","ibm","unifonic-ar","zid","salla"],
 "ecommerce/marketplace": ["apple","nike","sephora","glossier","ikea","lego","walgreens","amazon-eg-ar","jumia-eg-ar","amazon-sa-ar","jarir","extra-ar","arabianoud"],
 "travel/food": ["airbnb","booking","ryanair","starbucks","chipotle","elmenus","hungerstation-ar","almosafer-ar","wego-ar"],
 "finance/banking": ["paypal","wise","fawry","revolut","chase","hsbc","vanguard","coinbase","binance","monzo","emiratesnbd-ar","alrajhi","qnb","bankfab2","axa","prudential","mubasher"],
 "news/media": ["theguardian","nytimes","bbc","theverge","wired","natgeo","medium","substack","bbc-arabic","youm7","aawsat","cnn-arabic","skynews-arabia","almasryalyoum","rt-arabic","aitnews"],
 "entertainment/streaming": ["spotify","youtube","disneyplus","twitch","shahid","osnplus","mbc"],
 "gaming": ["steam","minecraft","ign","itchio","poki","crazygames","poki-ar"],
 "gov/institution": ["govuk","usagov","europa","uae-gov-ar","visitsaudi-ar","un","nasa","who"],
 "health/edu": ["nhs","coursera","khanacademy","duolingo","edx","edraak","almentor"],
 "sports": ["espn","nba","bein-ar","kooora","filgoal","yallakora"],
 "social/community": ["reddit","discord","pinterest","linkedin","hawaaworld","patreon","quora"],
 "creative/portfolio": ["behance","dribbble","flickr","moma","tate","eventbrite","ted","awwwards","cssdesignawards","cargo","500px"],
 "real-estate/auto": ["zillow","bayut-en","aqarmap","propertyfinder-ar","toyota","porsche","meta-quest"],
 "enterprise/industrial": ["deloitte","maersk","shell","ge","verizon","stc","fedex","uber"],
}

def signals(names):
    S = {}
    rad = collections.Counter(); shadow = 0; grad = 0; backdrop = 0; sticky = 0; cq = 0; dark = 0
    fonts = collections.Counter(); maxw = collections.Counter(); colors = collections.Counter()
    n = 0
    for nm in names:
        s = sites.get(nm)
        if not s: continue
        n += 1; c = s["css"]
        for v, cnt in c["radii"]:
            m = re.match(r"^(\d+)px$", v.strip())
            if m and int(m.group(1)) <= 100: rad[int(m.group(1))] += 1
        shadow += 1 if c["shadows"] else 0
        grad += 1 if c["gradient_count"] > 0 else 0
        backdrop += 1 if c["backdrop_filter"] else 0
        sticky += 1 if c["position_sticky"] else 0
        cq += 1 if c["container_queries"] else 0
        dark += 1 if c["prefers_color_scheme"] else 0
        for f, cnt in c["font_families"][:3]:
            first = re.split(r",\s*", f)[0].strip("'\" ")
            if first not in ("inherit","monospace","var(--font-mono","ui-monospace"): fonts[first] += 1
        for v, cnt in c["max_widths"]:
            if re.match(r"^\d+px$", v.strip()) and 900 <= int(v[:-2]) <= 1600: maxw[v.strip()] += 1
        for col, cnt in c["colors"][:6]: colors[col.lower()] += cnt
    S["n"] = n
    S["radius_top"] = rad.most_common(6)
    S["shadow_sites_%"] = round(shadow*100/max(n,1))
    S["gradient_sites_%"] = round(grad*100/max(n,1))
    S["backdrop_sites_%"] = round(backdrop*100/max(n,1))
    S["sticky_sites_%"] = round(sticky*100/max(n,1))
    S["cq_sites_%"] = round(cq*100/max(n,1))
    S["darkmq_sites_%"] = round(dark*100/max(n,1))
    S["fonts_top"] = fonts.most_common(8)
    S["maxw_top"] = maxw.most_common(5)
    return S

print("industry | n | radius-top(px) | shadows% | gradients% | backdrop% | sticky% | cq% | darkmq% | fonts | container")
for g, names in GROUPS.items():
    S = signals(names)
    print(f"{g:24s} | {S['n']:2d} | {S['radius_top']} | {S['shadow_sites_%']} | {S['gradient_sites_%']} | {S['backdrop_sites_%']} | {S['sticky_sites_%']} | {S['cq_sites_%']} | {S['darkmq_sites_%']} | {[f[0] for f in S['fonts_top'][:5]]} | {S['maxw_top']}")

# flagship deep dives
print("\n\n=== FLAGSHIP DEEP DIVES ===")
for nm in ["stripe","linear","openai","anthropic","github","apple","nike","sephora","airbnb","booking","paypal","monzo","coinbase","theguardian","nytimes","bbc","spotify","youtube","disneyplus","twitch","steam","itchio","poki","crazygames","govuk","uae-gov-ar","visitsaudi-ar","nhs","coursera","duolingo","espn","nba","reddit","discord","zillow","toyota","porsche","moma","ted","youm7","cnn-arabic","skynews-arabia","jarir","amazon-eg-ar","jumia-eg-ar","extra-ar","arabianoud","emiratesnbd-ar","alrajhi","stc","almosafer-ar","hungerstation-ar","bayut-en","propertyfinder-ar","aqarmap","shahid","bein-ar","kooora","filgoal","salla","zid","edraak","almentor","hawaaworld","poki-ar"]:
    s = sites.get(nm)
    if not s: continue
    h, c = s["html"], s["css"]
    fam = [f[0] for f in c["font_families"][:2]]
    bps = [b[0] for b, _ in c["breakpoints"][:4]]
    print(f"\n## {nm} ({h.get('lang','')}, dir={h.get('dir','')}) fw={','.join(h.get('framework_hints',[])[:4])}")
    print(f"   h1: {h.get('h1_sample',[])[:1]}")
    print(f"   nav/a/svg counts: nav={h.get('nav',0)} a={h.get('a',0)} svg={h.get('svg',0)} form={h.get('form',0)} img={h.get('img',0)} button={h.get('button',0)}")
    print(f"   fonts: {fam} | bps: {bps} | radius: {[r[0] for r in c['radii'][:3]]} | gradients:{c['gradient_count']} backdrop:{c['backdrop_filter']} sticky:{c['position_sticky']} cq:{c['container_queries']}")
    print(f"   theme-color: {h.get('theme_color','')} | cta: {h.get('cta_samples',[])[:4]}")
    print(f"   jsonld: {h.get('jsonld_types',[])[:6]}")
    tc = [t[0] for t in h.get("cta_samples",[]) if t]
    print(f"   icon classes: {h.get('icon_classes',[])[:3]}")
