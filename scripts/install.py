#!/usr/bin/env python3
"""
real-ui installer — copies the skill into every AI-agent skills directory
it detects on this machine, then verifies all copies are identical.

Usage:
    python scripts/install.py            # install everywhere detected
    python scripts/install.py --verify   # verify only (no copying)

Source of truth = this repository folder. Re-run after any edit.
"""
import argparse, os, shutil, subprocess, sys

HOME = os.path.expanduser("~")
SRC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL_NAME = "real-ui"

# Known agent skills directories (relative to home). The installer also
# scans for any other ~/.something/skills folder that already exists.
KNOWN = [
    ".agents/skills", ".pi/agent/skills", ".claude/skills", ".codex/skills",
    ".cursor/skills", ".gemini/skills", ".opencode/skills", ".windsurf/skills",
    ".continue/skills", ".roo/skills", ".factory/skills", ".qoder/skills",
    ".trae/skills", ".kilocode/skills", ".codebuddy/skills", ".warp/skills",
    ".augment/skills", ".codewhale/skills", ".vscode/skills",
]

def normalized_relative(path):
    return os.path.normpath(path).replace("\\", "/")


def remove_path(path):
    """Remove one validated staging/backup path without traversing junctions."""
    if os.path.islink(path):
        os.unlink(path)
    elif hasattr(os.path, "isjunction") and os.path.isjunction(path):
        os.rmdir(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)
    elif os.path.exists(path):
        os.remove(path)


def detect():
    found = [normalized_relative(d) for d in KNOWN if os.path.isdir(os.path.join(HOME, d))]
    # opportunistic scan for other agents following the same convention
    for entry in os.listdir(HOME):
        cand = os.path.join(HOME, entry, "skills")
        if entry.startswith(".") and os.path.isdir(cand) and cand not in [
            os.path.join(HOME, d) for d in KNOWN
        ]:
            found.append(normalized_relative(os.path.relpath(cand, HOME)))
    return sorted(set(found))


def install(targets):
    ok = []
    for rel in targets:
        dest = os.path.abspath(os.path.join(HOME, rel, SKILL_NAME))
        skills_root = os.path.abspath(os.path.join(HOME, rel))
        if os.path.commonpath([dest, skills_root]) != skills_root or os.path.basename(dest) != SKILL_NAME:
            print(f"FAIL       ~/{rel}/{SKILL_NAME}: unsafe destination")
            continue
        stage = dest + ".installing"
        backup = dest + ".previous"
        try:
            for stale in (stage, backup):
                remove_path(stale)
            shutil.copytree(SRC, stage,
                             ignore=shutil.ignore_patterns("__pycache__", ".git", "nul", "NUL"))
            if os.path.isdir(dest):
                os.replace(dest, backup)
            try:
                os.replace(stage, dest)
            except Exception:
                if os.path.isdir(backup) and not os.path.exists(dest):
                    os.replace(backup, dest)
                raise
            remove_path(backup)
            ok.append(rel)
            print(f"INSTALLED  ~/{rel}/{SKILL_NAME}")
        except Exception as e:
            remove_path(stage)
            print(f"FAIL       ~/{rel}/{SKILL_NAME}: {e}")
    return ok


def verify():
    script = os.path.join(SRC, "research", "tools", "verify_install.py")
    env = dict(os.environ, REAL_UI_SRC=SRC, PYTHONIOENCODING="utf-8")
    r = subprocess.run([sys.executable, script], env=env)
    return r.returncode == 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--verify", action="store_true", help="verify only, do not install")
    args = ap.parse_args()

    if not os.path.isfile(os.path.join(SRC, "SKILL.md")):
        sys.exit("Run this from inside the real-ui repository (SKILL.md not found).")

    targets = detect()
    print(f"Detected {len(targets)} agent skills directories:")
    for t in targets:
        print(f"  ~/{t}")

    if args.verify:
        sys.exit(0 if verify() else 1)

    installed = install(targets)
    print(f"\nInstalled to {len(installed)} locations. Verifying...")
    all_installed = len(installed) == len(targets)
    sys.exit(0 if all_installed and verify() else 1)
