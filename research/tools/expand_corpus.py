#!/usr/bin/env python3
"""Detached corpus-expansion runner: processes wave manifests sequentially.

Fast first pass: HTML-only fetch (no CSS sub-fetches) with a tight timeout,
so a full wave completes in minutes instead of the full fetch_analyze path.
Structure evidence is extracted per site; CSS-token analysis can be re-run
later on any successful site via fetch_analyze.py if token detail is needed.
"""
import io, json, os, re, sys, time
from datetime import datetime, timezone
from urllib.request import Request, urlopen

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RAW = os.path.join(ROOT, "research", "raw")
OUT = os.path.join(ROOT, "research", "reports")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
CAP = 400_000

def fetch(url, timeout=14):
    req = Request(url, headers={
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
        "Accept-Language": "en;q=0.9,ar;q=0.8",
        "Accept-Encoding": "identity",
    })
    with urlopen(req, timeout=timeout) as r:
        ctype = r.headers.get("Content-Type", "")
        return r.read(CAP).decode("utf-8", "replace"), ctype, r.geturl()

def looks_like_html(html, ctype):
    if ctype and "html" not in ctype and "xml" not in ctype:
        return False
    if html is None or len(html) < 800:
        return False
    return "<html" in html.lower() or "<!doctype" in html.lower() or "<body" in html.lower()

def structure_evidence(html):
    title = re.search(r"<title[^>]*>(.*?)</title>", html, re.S | re.I)
    nav = re.search(r"<nav[^>]*>(.*?)</nav>", html, re.S | re.I)
    nav_links = []
    if nav:
        for h, t in re.findall(r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', nav.group(1), re.S)[:14]:
            txt = re.sub(r"<[^>]+>", "", t).strip()[:24]
            if txt: nav_links.append([txt, h[:70]])
    h1 = re.findall(r"<h1[^>]*>(.*?)</h1>", html, re.S | re.I)
    h2 = re.findall(r"<h2[^>]*>(.*?)</h2>", html, re.S | re.I)
    clean = lambda xs: [re.sub(r"<[^>]+>", "", x).strip()[:40] for x in xs[:10]]
    dir_attr = re.search(r'<html[^>]*\bdir="([^"]+)"', html, re.I)
    lang = re.search(r'<html[^>]*\blang="([^"]+)"', html, re.I)
    forms = len(re.findall(r"<form", html, re.I))
    inputs = len(re.findall(r"<input", html, re.I))
    tables = len(re.findall(r"<table", html, re.I))
    imgs = len(re.findall(r"<img", html, re.I))
    svgs = len(re.findall(r"<svg", html, re.I))
    buttons = len(re.findall(r"<button", html, re.I))
    grids = len(re.findall(r"grid-template", html))
    flex = len(re.findall(r"display:\s*flex", html))
    framework = []
    for probe, name in [("_next", "next.js"), ("__nuxt", "nuxt"), ("tailwind", "tailwind-class"),
                        ("wp-content", "wordpress"), ("cdn.shopify", "shopify"), ("react", "react-hint"),
                        ("wix", "wix"), ("squarespace", "squarespace"), ("framer", "framer")]:
        if probe in html: framework.append(name)
    jsonld = len(re.findall(r'application/ld\+json', html))
    return {
        "title": re.sub(r"\s+", " ", title.group(1)).strip()[:90] if title else None,
        "dir": dir_attr.group(1) if dir_attr else None,
        "lang": lang.group(1) if lang else None,
        "h1": clean(h1), "h2": clean(h2),
        "nav_sample": nav_links[:10],
        "counts": {"forms": forms, "inputs": inputs, "tables": tables,
                   "imgs": imgs, "svgs": svgs, "buttons": buttons,
                   "grid_templates": grids, "flex": flex, "jsonld": jsonld},
        "framework_hints": framework[:6],
    }

def main():
    waves = [f for f in sorted(os.listdir(RAW)) if f.startswith("w") and f.endswith(".json")]
    for w in waves:
        name = w.replace(".json", "")
        out_path = os.path.join(OUT, name + ".json")
        if os.path.exists(out_path):
            print(f"[skip] {name} already done", flush=True)
            continue
        sites = json.load(io.open(os.path.join(RAW, w), encoding="utf-8"))
        reports = []
        print(f"[wave] {name}: {len(sites)} sites, start {datetime.now().strftime('%H:%M:%S')}", flush=True)
        for s in sites:
            r = {"name": s["name"], "url": s["url"], "industry": s["industry"],
                 "region": s.get("region", "?"), "lang_expected": s.get("lang_expected", "en"),
                 "fetched": datetime.now(timezone.utc).isoformat()[:19]}
            try:
                html, ctype, final = fetch(s["url"])
                if not looks_like_html(html, ctype):
                    r.update(status="not_html", content_type=str(ctype)[:40])
                else:
                    r.update(status="ok", final_url=final[:150], html_bytes=len(html))
                    r["evidence"] = structure_evidence(html)
            except Exception as e:
                r.update(status="fetch_failed", error=str(e)[:110])
            reports.append(r)
            print(f"  {r['name']}: {r['status']}", flush=True)
        json.dump(reports, io.open(out_path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
        ok = sum(1 for r in reports if r["status"] == "ok")
        print(f"[wave] {name} DONE: {ok}/{len(reports)} ok, saved {out_path}", flush=True)
    print("[all-waves-complete]", flush=True)

if __name__ == "__main__":
    main()
