#!/usr/bin/env python3
"""Verify real-ui skill installation across all agent skill directories."""
import os, re, glob, hashlib, py_compile, sys

SRC = os.environ.get(
    'REAL_UI_SRC',
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
)

# Auto-detect every agent skills directory on this machine that already
# contains real-ui, plus the canonical 5 (kept explicit so a stray delete
# is detected rather than silently skipped).
HOME = os.path.expanduser('~')
_AGENT_SKILL_DIRS = [
    '.agents/skills', '.pi/agent/skills', '.claude/skills', '.codex/skills',
    '.cursor/skills', '.gemini/skills', '.opencode/skills', '.windsurf/skills',
    '.continue/skills', '.roo/skills', '.factory/skills', '.qoder/skills',
    '.trae/skills', '.kilocode/skills', '.codebuddy/skills', '.warp/skills',
    '.augment/skills', '.codewhale/skills',
]
def installed_destinations():
    destinations = {
        os.path.abspath(os.path.join(HOME, d, 'real-ui'))
        for d in _AGENT_SKILL_DIRS
        if os.path.isdir(os.path.join(HOME, d))
    }
    for entry in os.listdir(HOME):
        candidate = os.path.join(HOME, entry, 'skills', 'real-ui')
        if entry.startswith('.') and os.path.isdir(candidate):
            destinations.add(os.path.abspath(candidate))
    return [path.replace('\\', '/') for path in sorted(destinations)]


DESTS = installed_destinations()

def fingerprint(root):
    fp = {}
    for dirpath, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in ('__pycache__', '.git')]
        for f in sorted(files):
            p = os.path.join(dirpath, f)
            rel = os.path.relpath(p, root).replace(os.sep, '/')
            with open(p, 'rb') as handle:
                fp[rel] = hashlib.sha256(handle.read()).hexdigest()
    return fp

src_fp = fingerprint(SRC)
print(f"SOURCE: {len(src_fp)} files")
all_ok = True
for d in DESTS:
    if not os.path.isdir(d):
        print(f"FAIL  {d}  (directory missing)")
        all_ok = False
        continue
    fp = fingerprint(d)
    missing = set(src_fp) - set(fp)
    extra = set(fp) - set(src_fp)
    diff = [k for k in set(src_fp) & set(fp) if src_fp[k] != fp[k]]
    ok = not missing and not extra and not diff
    all_ok &= ok
    status = "IDENTICAL" if ok else f"missing={sorted(missing)[:4]} extra={sorted(extra)[:4]} diff={diff[:4]}"
    print(f"{'PASS' if ok else 'FAIL'}  {d}  ({len(fp)} files) {status}")

# knowledge cross-reference check
md_files = glob.glob(os.path.join(SRC, '**', '*.md'), recursive=True)
refs_missing = []
for md in md_files:
    content = open(md, encoding='utf-8').read()
    for ref in re.findall(r'knowledge/[A-Za-z0-9_/-]+\.md', content):
        if not os.path.exists(os.path.join(SRC, ref)):
            refs_missing.append((os.path.relpath(md, SRC), ref))
print("knowledge/* cross-references:", "PASS (all resolve)" if not refs_missing else f"FAIL {refs_missing[:6]}")

# python tools compile check
for t in sorted(glob.glob(os.path.join(SRC, 'research', 'tools', '*.py'))):
    try:
        py_compile.compile(t, doraise=True)
        print(f"compile PASS: {os.path.basename(t)}")
    except py_compile.PyCompileError as e:
        print(f"compile FAIL: {t}: {e}")
        all_ok = False

# retrieval-map completeness: every file the SKILL.md map promises exists
skill = open(os.path.join(SRC, 'SKILL.md'), encoding='utf-8').read()

def expand_braces(path):
    """Expand {a,b,c} at any position, combinatorially."""
    out = [path]
    while any('{' in p for p in out):
        nxt = []
        for p in out:
            m = re.search(r'\{([^}]+)\}', p)
            if m:
                pre, post = p[:m.start()], p[m.end():]
                for opt in m.group(1).split(','):
                    nxt.append(pre + opt.strip() + post)
            else:
                nxt.append(p)
        out = nxt
    return out

map_refs = []
for line in skill.splitlines():
    if line.strip().startswith('|') and '.md' in line:
        for raw in re.findall(r'([A-Za-z0-9_{}/,-]+\.md)', line):
            map_refs.extend(expand_braces(raw))
promised = set(map_refs)
actual = {os.path.relpath(p, os.path.join(SRC, 'knowledge')).replace(os.sep, '/') for p in glob.glob(os.path.join(SRC, 'knowledge', '**', '*.md'), recursive=True)}
ghost = promised - actual
orphan = actual - promised
print("retrieval map ghosts (promised but missing):", "none" if not ghost else f"FAIL {sorted(ghost)}")
print("knowledge files not in map:", sorted(orphan) if orphan else "none")

# frontmatter YAML safety: plain-scalar values must not contain colon-space
# (strict parsers like pi's `yaml` reject nested-mapping-looking values)
import subprocess
for md in [os.path.join(SRC, 'SKILL.md')] + glob.glob(os.path.join(SRC, 'knowledge', '**', '*.md'), recursive=True):
    text = open(md, encoding='utf-8').read()
    fm_m = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    if not fm_m:
        continue
    for i, line in enumerate(fm_m.group(1).splitlines(), 1):
        kv = re.match(r'^(\w[\w-]*):\s*(\S.*)$', line)
        if kv and not kv.group(2).startswith(('"', "'", '|', '>')):
            val = re.sub(r'\\.', '', kv.group(2))
            if ': ' in val or val.rstrip().endswith(':'):
                print(f"FRONTMATTER YAML HAZARD: {os.path.relpath(md, SRC)} line {i}: colon in plain scalar -> {line[:80]}")
                all_ok = False
print("frontmatter YAML safety check: done")

ok_final = all_ok and not refs_missing and not ghost
print()
print("FINAL:", "ALL CHECKS PASS" if ok_final else "ERRORS FOUND")
sys.exit(0 if ok_final else 1)
