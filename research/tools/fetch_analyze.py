#!/usr/bin/env python3
"""
real-ui research tool: code-first website analysis.
Fetches public HTML (+ primary CSS) and extracts observable design evidence:
structure, semantics, tokens, breakpoints, typography, colors, radii, shadows,
icons, frameworks, JSON-LD, RTL attributes. Saves a compact JSON report.
"""
import json, re, sys, os, hashlib
from urllib.parse import urljoin, urlparse
import urllib.request, gzip, io

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
HTML_CAP = 400_000
CSS_CAP_PER_FILE = 200_000
MAX_CSS_FILES = 3

def fetch(url, cap=HTML_CAP, timeout=20):
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": UA,
            "Accept": "text/html,application/xhtml+xml,application/css,*/*;q=0.8",
            "Accept-Language": "en;q=0.9,ar;q=0.8",
            "Accept-Encoding": "identity",
        })
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = r.read(cap)
            ctype = r.headers.get("Content-Type", "")
            final = r.geturl()
        return data.decode("utf-8", "replace"), ctype, final
    except Exception as e:
        return None, str(e), url

def top_counts(items, n=12):
    d = {}
    for i in items:
        if i: d[i] = d.get(i, 0) + 1
    return sorted(d.items(), key=lambda x: -x[1])[:n]

def analyze_html(html):
    h = {}
    for tag in ["header","nav","main","section","article","aside","footer","form","button","a","img","svg","table","figure","ul","ol","dialog","details","summary","canvas","iframe","video","picture"]:
        h[tag] = len(re.findall(r"<"+tag+r"[\s>]", html, re.I))
    for i in range(1,7):
        h[f"h{i}"] = len(re.findall(r"<h"+str(i)+r"[\s>]", html, re.I))
    m = re.search(r'<html[^>]*>', html, re.I)
    h["html_tag"] = m.group(0)[:300] if m else ""
    m = re.search(r'name="viewport"\s+content="([^"]*)"', html)
    h["viewport"] = m.group(1) if m else ""
    m = re.search(r'name="theme-color"\s+content="([^"]*)"', html, re.I)
    h["theme_color"] = m.group(1) if m else ""
    m = re.search(r"<title[^>]*>(.*?)</title>", html, re.S|re.I)
    h["title"] = (m.group(1).strip()[:200] if m else "")
    h["jsonld_types"] = sorted(set(re.findall(r'"@type"\s*:\s*"([^"]+)"', html)))[:12]
    h["lang"] = (re.search(r'<html[^>]*\blang="([^"]*)"', html, re.I) or [None,""])[1] if re.search(r'<html[^>]*\blang=', html, re.I) else ""
    h["dir"] = (re.search(r'<html[^>]*\bdir="([^"]*)"', html, re.I) or [None,""])[1] if re.search(r'<html[^>]*\bdir=', html, re.I) else ""
    # framework / library hints
    fw = []
    tests = {
        "next.js": r"__NEXT_DATA__|/_next/static",
        "react": r"data-reactroot|react[-_]dom|__REACT",
        "nuxt/vue": r"__NUXT__|data-v-[0-9a-f]{8}|vue",
        "tailwind": r'(?:class="[^"]*\b(?:flex|grid|text-\[|bg-\[|md:flex|lg:grid|hover:bg-)[^"]*")',
        "bootstrap": r'bootstrap(?:\.min)?\.(?:css|js)|class="[^"]*\bcol-md-',
        "font-awesome": r"font-?awesome|fa-solid|fa-",
        "material-icons": r"material-icons|material-symbols",
        "lucide": r"lucide",
        "heroicons": r"heroicons",
        "wp-block": r"wp-block-",
        "shopify": r"cdn\.shopify\.com",
        "gatsby": r"___gatsby",
        "astro": r"astro-",
        "svelte": r"svelte-[0-9a-z]",
        "webflow": r"webflow",
        "framer": r"framerusercontent|framer\.com",
        "wix": r"wixstatic|wix\.com",
        "squarespace": r"squarespace",
        "gtm": r"googletagmanager",
        "jquery": r"jquery",
    }
    for name, pat in tests.items():
        if re.search(pat, html, re.I): fw.append(name)
    h["framework_hints"] = fw
    # icon glyph usage
    h["icon_classes"] = top_counts(re.findall(r'class="([^"]*(?:material-icons|material-symbols|fa-|icon-|lucide-)[^"]*)"', html), 10)
    # svg sprite/use
    h["svg_use"] = len(re.findall(r"<use\s", html, re.I))
    # inline style custom props on html/body
    body = re.search(r"<body[^>]*>", html, re.I)
    h["body_tag"] = body.group(0)[:400] if body else ""
    # css vars declared inline (style blocks)
    inline_vars = re.findall(r"--[\w-]+\s*:\s*[^;}]+", html)
    h["inline_css_vars"] = top_counts(inline_vars, 25)
    # stylesheet + font links
    links = re.findall(r'<link[^>]+rel="stylesheet"[^>]*>', html, re.I)
    h["stylesheet_count"] = len(links)
    fonts = re.findall(r'<link[^>]*href="([^"]+\.woff2?[^"]*)"', html, re.I)
    h["preload_font_count"] = len(fonts)
    gfonts = re.findall(r'fonts\.googleapis\.com/css2?\?([^"]+)', html)
    h["google_fonts"] = gfonts[:4]
    # headings text sample
    h1s = re.findall(r"<h1[^>]*>(.*?)</h1>", html, re.S|re.I)
    h["h1_sample"] = [re.sub(r"<[^>]+>|\s+", " ", x).strip()[:120] for x in h1s[:3]]
    # buttons/cta words
    btns = re.findall(r"<(?:button|a[^>]+class=\"[^\"]*btn)[^>]*>(.*?)</(?:button|a)>", html, re.S|re.I)
    txt = [re.sub(r"<[^>]+>|\s+", " ", b).strip() for b in btns]
    h["cta_samples"] = [t for t in txt if t and len(t) < 40][:12]
    return h

def analyze_css(css):
    c = {}
    mq = re.findall(r"@media[^{]+", css)
    widths = []
    for m in mq:
        for w in re.findall(r"(?:min|max)-width\s*:\s*([\d.]+)(px|em|rem)", m):
            val = float(w[0])
            if w[1] == "em" or w[1] == "rem": val *= 16
            if 300 <= val <= 2000: widths.append(int(val))
    c["breakpoints"] = top_counts([str(w) for w in widths], 14)
    c["container_queries"] = len(re.findall(r"@container", css))
    c["font_families"] = top_counts(re.findall(r"font-family\s*:\s*([^;}]+)", css), 10)
    ff = re.findall(r'@font-face\s*{[^}]*}', css)
    faces = []
    for block in ff:
        fam = re.search(r"font-family\s*:\s*['\"]?([^;'\"}]+)", block)
        wgt = re.search(r"font-weight\s*:\s*([^;}]+)", block)
        faces.append(((fam.group(1).strip() if fam else "?"), (wgt.group(1).strip() if wgt else "?")))
    c["font_faces"] = top_counts([f"{a}|{b}" for a,b in faces], 16)
    c["font_sizes"] = top_counts(re.findall(r"font-size\s*:\s*([^;}]+)", css), 14)
    c["line_heights"] = top_counts(re.findall(r"line-height\s*:\s*([^;}]+)", css), 10)
    c["letter_spacings"] = top_counts(re.findall(r"letter-spacing\s*:\s*([^;}]+)", css), 8)
    c["colors"] = top_counts(re.findall(r"(?:#[0-9a-fA-F]{3,8}\b|rgba?\([^)]+\))", css), 16)
    c["css_vars"] = top_counts(re.findall(r"--[\w-]+\s*:", css), 20)
    c["radii"] = top_counts(re.findall(r"border-radius\s*:\s*([^;}]+)", css), 12)
    c["shadows"] = top_counts(re.findall(r"box-shadow\s*:\s*([^;}]+)", css), 8)
    c["transitions"] = top_counts(re.findall(r"transition\s*:[^;}]*(?:transition-property)?", css), 1)
    c["transition_count"] = len(re.findall(r"transition\s*:", css))
    c["animation_count"] = len(re.findall(r"@keyframes", css))
    c["transform_count"] = len(re.findall(r"transform\s*:", css))
    c["grid_count"] = len(re.findall(r"display\s*:\s*grid", css))
    c["flex_count"] = len(re.findall(r"display\s*:\s*flex", css))
    c["position_fixed"] = len(re.findall(r"position\s*:\s*fixed", css))
    c["position_sticky"] = len(re.findall(r"position\s*:\s*sticky", css))
    c["prefers_reduced_motion"] = len(re.findall(r"prefers-reduced-motion", css))
    c["prefers_color_scheme"] = len(re.findall(r"prefers-color-scheme", css))
    c["hover_count"] = len(re.findall(r":hover", css))
    c["focus_visible"] = len(re.findall(r":focus-visible", css))
    c["backdrop_filter"] = len(re.findall(r"backdrop-filter", css))
    c["filter_count"] = len(re.findall(r"filter\s*:", css))
    c["blur_values"] = top_counts(re.findall(r"blur\(([^)]+)\)", css), 6)
    c["gradient_count"] = len(re.findall(r"gradient\(", css))
    c["max_widths"] = top_counts(re.findall(r"max-width\s*:\s*([^;}]+)", css), 10)
    c["z_indexes"] = top_counts(re.findall(r"z-index\s*:\s*([^;}]+)", css), 10)
    c["dir_rtl_rules"] = len(re.findall(r"\bdir=rtl|:dir\(rtl\)|\[dir=['\"]?rtl", css))
    c["lang_ar_rules"] = len(re.findall(r":lang\(ar", css))
    return c

def get_css_links(html, base):
    links = re.findall(r'<link[^>]+href="([^"]+\.css[^"]*)"', html, re.I)
    out = []
    for l in links:
        u = urljoin(base, l)
        if any(b in u for b in ["googletagmanager","google-analytics","facebook","twitter","cdn.jsdelivr.net/npm/"]): continue
        out.append(u)
    return out[:MAX_CSS_FILES]

def process(site):
    name, url = site["name"], site["url"]
    report = {"name": name, "url": url, "industry": site.get("industry",""), "region": site.get("region","global"), "lang_expected": site.get("lang","")}
    html, err, final = fetch(url)
    if html is None:
        # try http→https retry once or www alt
        alt = url.replace("://www.", "://") if "://www." in url else url.replace("://", "://www.")
        html, err2, final = fetch(alt)
    if html is None:
        report["status"] = "fetch_failed"
        report["error"] = f"{err[:120]} | {err2[:80] if 'err2' in dir() else ''}"
        return report
    report["status"] = "ok"
    report["final_url"] = final[:160]
    report["html_bytes_capped"] = len(html)
    report["html"] = analyze_html(html)
    css_texts = []
    for u in get_css_links(html, final):
        css, cerr, _ = fetch(u, cap=CSS_CAP_PER_FILE)
        if css and len(css) > 500 and "text/css" not in str(cerr)[:40] or (css and len(css) > 500):
            css_texts.append(css)
    # inline style blocks too
    inline = "\n".join(re.findall(r"<style[^>]*>(.*?)</style>", html, re.S|re.I))
    if inline: css_texts.append(inline)
    all_css = "\n".join(css_texts)
    report["css_bytes_analyzed"] = len(all_css)
    report["css"] = analyze_css(all_css) if len(all_css) > 500 else None
    # keep small evidence sample: first nav + first section opener
    nav = re.search(r"<nav[^>]*>.*?</nav>", html, re.S|re.I)
    report["nav_sample_hash"] = hashlib.md5((nav.group(0) if nav else "").encode()).hexdigest()[:8]
    return report

def run_batch(batchfile, outfile):
    sites = json.load(open(batchfile, encoding="utf-8"))
    reports = []
    for s in sites:
        print(f"  fetching {s['name']} ...", flush=True)
        r = process(s)
        reports.append(r)
        print(f"    -> {r.get('status')} (css: {r.get('css_bytes_analyzed',0)} bytes)", flush=True)
    json.dump(reports, open(outfile, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(f"saved {len(reports)} reports -> {outfile}")

if __name__ == "__main__":
    run_batch(sys.argv[1], sys.argv[2])
