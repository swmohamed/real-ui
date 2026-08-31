#!/usr/bin/env python3
"""Render and audit the REAL-UI showcase with an isolated Chrome session."""

from __future__ import annotations

import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import uuid


ROOT = Path(__file__).resolve().parents[1]
SHOWCASE = ROOT / "showcase"
VIEWPORTS = {"desktop": (1440, 900), "mobile": (390, 844)}
AGENT_BROWSER = shutil.which("agent-browser") or "agent-browser"
SNAPSHOT_SCRIPT = r"""JSON.stringify((()=>{const box=(el)=>{const r=el.getBoundingClientRect();return{x:Math.round(r.x),y:Math.round(r.y),width:Math.round(r.width),height:Math.round(r.height)}};return{title:document.title,viewport:{width:innerWidth,height:innerHeight},h1_count:document.querySelectorAll('h1').length,landmarks:{header:document.querySelectorAll('header').length,nav:document.querySelectorAll('nav').length,main:document.querySelectorAll('main').length,footer:document.querySelectorAll('footer').length},zones:[...document.querySelectorAll('[data-zone]')].map(el=>({id:el.dataset.zone,box:box(el),visible:!!(el.offsetWidth||el.offsetHeight||el.getClientRects().length)})),horizontal_overflow:document.documentElement.scrollWidth>innerWidth+1,document_width:document.documentElement.scrollWidth,console_errors:[]}})())"""


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, _format: str, *_args: object) -> None:
        return


def run_cli(session: str, *args: str) -> dict:
    command = [AGENT_BROWSER, "--session", session, *args, "--json"]
    # The CLI may launch a persistent daemon. File-backed streams prevent that
    # grandchild from keeping Python's capture pipes open on Windows.
    with tempfile.TemporaryFile() as stdout_file, tempfile.TemporaryFile() as stderr_file:
        completed = subprocess.run(
            command,
            cwd=ROOT,
            check=False,
            stdout=stdout_file,
            stderr=stderr_file,
            timeout=45,
        )
        stdout_file.seek(0)
        stderr_file.seek(0)
        stdout = stdout_file.read().decode("utf-8", errors="replace")
        stderr = stderr_file.read().decode("utf-8", errors="replace")
    if completed.returncode:
        raise RuntimeError(f"agent-browser failed ({' '.join(args)}):\n{stdout}\n{stderr}")
    try:
        payload = json.loads(stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"invalid agent-browser JSON for {' '.join(args)}: {stdout}") from exc
    if not payload.get("success", False):
        raise RuntimeError(f"agent-browser reported failure for {' '.join(args)}: {payload}")
    return payload


def surfaces() -> list[dict]:
    items: list[dict] = []
    preferred = ("gaming", "saas", "editorial", "ecommerce")
    for domain in preferred:
        case_path = SHOWCASE / "redesign" / domain / "case.json"
        case = json.loads(case_path.read_text(encoding="utf-8"))
        for state in ("before", "after"):
            items.append(
                {
                    "id": f"redesign/{domain}/{state}",
                    "html": (case_path.parent / case["implementation"][state]).resolve(),
                    "root": case_path.parent,
                    "state": state,
                    "case": case,
                }
            )
    for domain_dir in sorted((SHOWCASE / "greenfield").iterdir()):
        html = domain_dir / "site" / "index.html"
        if html.is_file():
            items.append({"id": f"greenfield/{domain_dir.name}", "html": html.resolve(), "root": domain_dir})
    return items


def artifact_paths(item: dict, device: str) -> tuple[Path, Path, Path]:
    if "case" in item:
        case = item["case"]
        key = f"{item['state']}_{device}"
        root = item["root"]
        return (
            root / case["render"]["screenshots"][key],
            root / case["render"]["snapshots"][key],
            root / case["render"]["a11y"][key],
        )
    root = item["root"]
    return (
        root / f"{device}.png",
        root / "evidence" / f"{device}.json",
        root / "evidence" / f"{device}-a11y.json",
    )


def render_one(session: str, base_url: str, item: dict, device: str) -> dict:
    width, height = VIEWPORTS[device]
    relative = item["html"].relative_to(SHOWCASE).as_posix()
    url = f"{base_url}/{relative}"
    screenshot_path, snapshot_path, a11y_path = artifact_paths(item, device)
    for path in (screenshot_path, snapshot_path, a11y_path):
        path.parent.mkdir(parents=True, exist_ok=True)

    run_cli(session, "open", url)
    run_cli(session, "set", "viewport", str(width), str(height))
    run_cli(session, "errors", "--clear")
    run_cli(session, "reload")
    run_cli(session, "wait", "120")
    run_cli(session, "screenshot", str(screenshot_path))
    snapshot_payload = run_cli(session, "eval", SNAPSHOT_SCRIPT)
    errors_payload = run_cli(session, "errors")
    a11y_payload = run_cli(session, "a11y")

    snapshot = json.loads(snapshot_payload["data"]["result"])
    snapshot["console_errors"] = errors_payload.get("data", {}).get("errors", [])
    snapshot["surface"] = item["id"]
    snapshot["device"] = device
    snapshot_path.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    raw_a11y = a11y_payload.get("data", {})
    a11y_record = {
        "surface": item["id"],
        "device": device,
        "viewport": {"width": width, "height": height},
        "engine": "axe-core",
        "axe_version": raw_a11y.get("axeVersion"),
        "counts": raw_a11y.get("counts", {}),
        "violations": raw_a11y.get("violations", []),
        "incomplete": raw_a11y.get("incomplete", []),
    }
    a11y_path.write_text(json.dumps(a11y_record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    counts = a11y_record["counts"]
    violations = int(counts.get("violations", 0))
    incomplete = int(counts.get("incomplete", 0))
    if snapshot["viewport"] != {"width": width, "height": height}:
        raise RuntimeError(f"{item['id']} {device}: wrong viewport {snapshot['viewport']}")
    if snapshot["horizontal_overflow"]:
        raise RuntimeError(f"{item['id']} {device}: horizontal overflow ({snapshot['document_width']}px)")
    if snapshot["console_errors"]:
        raise RuntimeError(f"{item['id']} {device}: console errors {snapshot['console_errors']}")
    if violations:
        details = [entry.get("id") for entry in a11y_record["violations"]]
        raise RuntimeError(f"{item['id']} {device}: {violations} axe violations ({', '.join(details)})")
    return {
        "surface": item["id"],
        "device": device,
        "viewport": f"{width}x{height}",
        "screenshot": str(screenshot_path.relative_to(ROOT)),
        "zones": len(snapshot["zones"]),
        "axe_violations": violations,
        "axe_incomplete": incomplete,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--only", help="Render only surfaces whose id starts with this value")
    args = parser.parse_args()
    selected = [item for item in surfaces() if not args.only or item["id"].startswith(args.only)]
    if not selected:
        print("No matching showcase surfaces", file=sys.stderr)
        return 2

    server = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(SHOWCASE)))
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    session = f"real-ui-render-{uuid.uuid4().hex[:10]}"
    base_url = f"http://127.0.0.1:{server.server_port}"
    results: list[dict] = []
    try:
        for item in selected:
            for device in VIEWPORTS:
                print(f"RENDER {item['id']} {device}", flush=True)
                results.append(render_one(session, base_url, item, device))
    finally:
        try:
            run_cli(session, "close")
        except Exception:
            pass
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)

    report = {"generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "browser": "Chromium via agent-browser", "results": results}
    report_path = SHOWCASE / "render-report.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"PASS: {len(results)} viewport renders, report {report_path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
