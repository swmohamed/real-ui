#!/usr/bin/env python3
"""Aggregate cross-corpus findings from all fetched reports."""
import json, glob, re, collections

def load():
    sites = {}
    for f in sorted(glob.glob("reports/*.json")):
        for s in json.load(open(f, encoding="utf-8")):
            if s["status"] == "ok" and s.get("css"):
                sites[s["name"]] = s
    return sites

sites = load()
print(f"corpus: {len(sites)} sites with CSS evidence")

# 1. breakpoints
bp = collections.Counter()
for s in sites.values():
    for val, n in s["css"]["breakpoints"]:
        bp[int(val)] += n
std = [(k,v) for k,v in sorted(bp.items()) if v>=8]
print("\n== BREAKPOINT FREQUENCY (media-query width, count of sites using) ==")
for k,v in std: print(f"  {k:5d}px  {v}")

# 2. fonts
fam = collections.Counter()
gfonts = collections.Counter()
for s in sites.values():
    seen = set()
    for f, n in s["css"]["font_families"]:
        first = re.split(r",\s*", f)[0].strip("'\" ")
        if first and first.lower() not in ("inherit","var(--","monospace") and first not in seen:
            fam[first] += 1; seen.add(first)
    for g in s["html"].get("google_fonts", []):
        for m in re.findall(r"family=([\w+]+)", g): gfonts[m.replace("+"," ")] += 1
print("\n== PRIMARY FONT FAMILIES (sites) ==")
for k,v in fam.most_common(40): print(f"  {v:3d}  {k}")
print("\n== GOOGLE FONTS LOADED ==")
for k,v in gfonts.most_common(20): print(f"  {v:3d}  {k}")

# 3. radius
rad = collections.Counter()
for s in sites.values():
    for val, n in s["css"]["radii"]:
        v = val.strip()
        if re.match(r"^\d+(\.\d+)?px$", v): rad[v] += 1
print("\n== BORDER-RADIUS VALUES (px, sites) ==")
for k,v in rad.most_common(20): print(f"  {k:6s} {v}")

# 4. technique adoption rates
tot = len(sites)
def rate(key): return sum(1 for s in sites.values() if s["css"].get(key))
print("\n== TECHNIQUE ADOPTION (of %d sites w/ CSS) ==" % tot)
for k in ["container_queries","prefers_reduced_motion","prefers_color_scheme","focus_visible","backdrop_filter","position_sticky"]:
    print(f"  {k:24s} {rate(k):3d}  ({rate(k)*100//tot}%)")

# 5. frameworks
fw = collections.Counter()
for s in sites.values(): fw.update(s["html"].get("framework_hints", []))
print("\n== FRAMEWORK HINTS ==")
for k,v in fw.most_common(15): print(f"  {v:3d}  {k}")

# 6. Arabic vs global comparison
ar = {n:s for n,s in sites.items() if s["html"].get("dir")=="rtl"}
print(f"\n== ARABIC/RTL SITES: {len(ar)} ==")
arfonts = collections.Counter()
for s in ar.values():
    for f, n in s["css"]["font_families"]:
        first = re.split(r",\s*", f)[0].strip("'\" ")
        arfonts[first] += 1
for k,v in arfonts.most_common(18): print(f"  {v:2d}  {k}")
tech = collections.Counter()
for s in ar.values():
    c = s["css"]
    if c["dir_rtl_rules"]: tech["css :dir/[dir=rtl] rules"] += 1
    if c["lang_ar_rules"]: tech[":lang(ar) rules"] += 1
print("  RTL CSS techniques:", dict(tech))
arbp = collections.Counter()
for s in ar.values():
    for val, n in s["css"]["breakpoints"]: arbp[int(val)] += n
print("  RTL breakpoints:", sorted([(k,v) for k,v in arbp.items() if v>=5], key=lambda x:-x[1])[:10])

# 7. max-width conventions
mw = collections.Counter()
for s in sites.values():
    for val, n in s["css"]["max_widths"]:
        if re.match(r"^\d+px$", val.strip()) and 600 <= int(val[:-2]) <= 1800:
            mw[val.strip()] += 1
print("\n== MAX-WIDTH VALUES ==")
for k,v in mw.most_common(16): print(f"  {k:8s} {v}")

# 8. viewport meta variants
vp = collections.Counter()
for s in sites.values(): vp[s["html"].get("viewport","")[:60]] += 1
print("\n== VIEWPORT META ==")
for k,v in vp.most_common(8): print(f"  {v:3d}  {k}")

# 9. semantic usage rates
print("\n== SEMANTIC HTML (sites containing >=1) ==")
for tag in ["header","nav","main","footer","section","article","form","svg","table","dialog","details"]:
    n = sum(1 for s in sites.values() if s["html"].get(tag,0)>0)
    print(f"  {tag:10s} {n:3d} ({n*100//tot}%)")
avg_h1 = sum(s["html"].get("h1",0) for s in sites.values())/tot
print(f"  avg h1 per homepage: {avg_h1:.1f}")

# 10. font-size scale
fs = collections.Counter()
for s in sites.values():
    for val, n in s["css"]["font_sizes"]:
        v = val.strip()
        if re.match(r"^[\d.]+(px|rem)$", v): fs[v] += 1
print("\n== FONT-SIZE VALUES ==")
for k,v in fs.most_common(22): print(f"  {k:8s} {v}")
