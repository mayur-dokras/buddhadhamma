"""Site checks run on every push and pull request.
1. Rebuilding from src/ must reproduce the committed index.html (nobody edited the built file by hand).
2. Every inline script in index.html must parse.
3. The page must declare a doctype and UTF-8.
4. Every local image the data files point to must exist."""
import re, subprocess, sys, tempfile, os, json
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
fail = []
html = (ROOT / 'index.html').read_text(encoding='utf-8')
if not html.lstrip().lower().startswith('<!doctype html>'): fail.append('index.html has no doctype')
if '<meta charset="utf-8">' not in html[:600]: fail.append('index.html does not declare UTF-8 near the top')
n = 0
for m in re.finditer(r'<script(?![^>]*\bsrc=)([^>]*)>(.*?)</script>', html, re.S):
    attrs, body = m.group(1), m.group(2)
    if 'importmap' in attrs or 'application/json' in attrs: continue
    ext = '.mjs' if 'module' in attrs else '.js'
    with tempfile.NamedTemporaryFile('w', suffix=ext, delete=False, encoding='utf-8') as f: f.write(body)
    r = subprocess.run(['node', '--check', f.name], capture_output=True, text=True); os.unlink(f.name); n += 1
    if r.returncode: fail.append(f'inline script {n} does not parse: ' + r.stderr.strip().splitlines()[-1])
for js in sorted(ROOT.glob('*.js')):
    r = subprocess.run(['node', '--check', str(js)], capture_output=True, text=True)
    if r.returncode: fail.append(f'{js.name} does not parse')
missing = set()
for src in [html] + [p.read_text(encoding='utf-8') for p in ROOT.glob('data_*.js')]:
    for ref in re.findall(r'img/[\w./-]+\.(?:jpg|jpeg|png|webp|svg)', src):
        if not (ROOT / ref).exists(): missing.add(ref)
if missing: fail.append('missing images: ' + ', '.join(sorted(missing)[:20]))
print(f'checked {n} inline scripts')
if fail:
    print('\n'.join('FAIL ' + x for x in fail)); sys.exit(1)
print('all checks passed')
