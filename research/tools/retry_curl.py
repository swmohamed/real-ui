#!/usr/bin/env python3
"""Retry failed sites via curl subprocess, then analyze local files."""
import json, re, subprocess, sys, os, tempfile
sys.path.insert(0, os.path.dirname(__file__))
from fetch_analyze import analyze_html, analyze_css, get_css_links
from urllib.parse import urljoin

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"

def curl(url, out, extra=None):
    cmd = ["curl","-sL","-m","30","--compressed","-A",UA,
           "-H","Accept: text/html,application/xhtml+xml,*/*;q=0.8",
           "-H","Accept-Language: en;q=0.9,ar;q=0.8", "-o", out, "-w","%{http_code}"]
    if extra: cmd = cmd[:-1] + extra + [url] if False else cmd + [extra]
    cmd.append(url)
    r = subprocess.run(cmd, capture_output=True, text=True)
    return r.stdout.strip()

def process(site):
    name, url = site["name"], site["url"]
    rep = {"name":name,"url":url,"industry":site.get("industry",""),"region":site.get("region","global"),"lang_expected":site.get("lang","")}
    tmp = os.path.join(tempfile.gettempdir(), name+".html")
    code = curl(url, tmp)
    html = open(tmp, encoding="utf-8", errors="replace").read(400000) if os.path.exists(tmp) else None
    if not html or len(html) < 2000:
        rep["status"]="fetch_failed"; rep["error"]=f"HTTP {code}, len={len(html) if html else 0}"; return rep
    rep["status"]="ok"; rep["final_url"]=url; rep["html_bytes_capped"]=len(html)
    rep["html"]=analyze_html(html)
    css_texts=[]
    for u in get_css_links(html, url):
        t = os.path.join(tempfile.gettempdir(), name+"_"+re.sub(r'\W','',u[-30:])+".css")
        c = curl(u, t)
        if os.path.exists(t) and os.path.getsize(t)>500:
            css_texts.append(open(t,encoding="utf-8",errors="replace").read(200000))
    inline = "\n".join(re.findall(r"<style[^>]*>(.*?)</style>", html, re.S|re.I))
    if inline: css_texts.append(inline)
    all_css="\n".join(css_texts)
    rep["css_bytes_analyzed"]=len(all_css)
    rep["css"]=analyze_css(all_css) if len(all_css)>500 else None
    return rep

if __name__=="__main__":
    sites=json.load(open(sys.argv[1],encoding="utf-8"))
    out=[]
    for s in sites:
        print(" retry", s["name"], "...", flush=True)
        r=process(s); out.append(r)
        print("   ->", r.get("status"), "(css:", r.get("css_bytes_analyzed",0), ")", flush=True)
    json.dump(out, open(sys.argv[2],"w",encoding="utf-8"), indent=1, ensure_ascii=False)
    print("saved", len(out))
