"""Typography clean-up for visible text: no em dashes, no colons inside prose.
   ' — ' becomes ', ' ; a colon after a short heading becomes ' · ', a colon inside a sentence becomes ', '.
   Works on HTML pages (text nodes, readable attributes, JS string literals) and on JS/JSON data files.
   Idempotent: running it twice changes nothing more."""
import re, sys

CSS = set('display position margin padding font flex grid text background color border gap align justify width height top left right bottom overflow transform transition opacity cursor white-space z-index box-shadow content line-height letter-spacing object-fit fill stroke min-width max-width min-height max-height inset outline place-items vertical-align'.split())
COLON = re.compile(r'(?<=[\w’”\)\]])[ ]?: (?=[\w“‘(\[])')
STOP = set('.!?>\n·;"`|(')

def _prefix_words(s, i):
    j = i - 1
    while j >= 0 and s[j] not in STOP:
        j -= 1
    return s[j + 1:i].strip()

def clean(s):
    if not s or ('—' not in s and ': ' not in s):
        return s
    s = s.replace(' — ', ', ').replace(' —', ',').replace('— ', ', ').replace('—', '–')
    out, last = [], 0
    for m in COLON.finditer(s):
        pre = _prefix_words(s, m.start())
        word = (pre.split() or [''])[-1].lower()
        if word in CSS or pre.endswith(('http', 'https')) or re.fullmatch(r'[\d\s.,–-]*', pre):
            continue
        rep = ' · ' if len(pre.split()) <= 2 else ', '
        out.append(s[last:m.start()]); out.append(rep); last = m.end()
    out.append(s[last:])
    return ''.join(out)

def _scan(code):
    o, i, n = [], 0, len(code)
    while i < n:
        c = code[i]
        if c == '/' and i + 1 < n and code[i + 1] == '/':
            j = code.find('\n', i); j = n if j < 0 else j
            o.append(code[i:j]); i = j; continue
        if c == '/' and i + 1 < n and code[i + 1] == '*':
            j = code.find('*/', i + 2); j = n if j < 0 else j + 2
            o.append(code[i:j]); i = j; continue
        if c in '\'"`':
            j, piece = _string(code, i, c)
            o.append(piece); i = j; continue
        o.append(c); i += 1
    return ''.join(o)

def _string(code, i, q):
    n = len(code); j = i + 1; out = [q]; buf = []
    while j < n:
        c = code[j]
        if c == '\\':
            buf.append(code[j:j + 2]); j += 2; continue
        if c == q:
            out.append(clean(''.join(buf))); out.append(q); return j + 1, ''.join(out)
        if c == '\n' and q != '`':
            break
        if q == '`' and c == '$' and j + 1 < n and code[j + 1] == '{':
            out.append(clean(''.join(buf))); buf = []
            k = j + 2; depth = 1; expr = ['${']
            while k < n and depth:
                ch = code[k]
                if ch in '\'"`':
                    k2, piece = _string(code, k, ch); expr.append(piece); k = k2; continue
                if ch == '{': depth += 1
                elif ch == '}': depth -= 1
                expr.append(ch); k += 1
            out.append(''.join(expr)); j = k
            if code.startswith(': ', j):
                out.append(' · '); j += 2
            continue
        buf.append(c); j += 1
    out.append(''.join(buf)); return j, ''.join(out)

TAGS = re.compile(r'(<script\b[^>]*>)(.*?)(</script>)|(<style\b[^>]*>.*?</style>)|(<[^>]+>)', re.S)
ATTR = re.compile(r'\b(title|aria-label|alt|placeholder)="([^"]*)"')

def clean_html(html, max_script=300_000):
    out, last = [], 0
    for m in TAGS.finditer(html):
        out.append(clean(html[last:m.start()]))
        if m.group(1):
            body = m.group(2)
            out.append(m.group(1) + (body if len(body) > max_script else _scan(body)) + m.group(3))
        elif m.group(4):
            out.append(m.group(4))
        else:
            out.append(ATTR.sub(lambda a: f'{a.group(1)}="{clean(a.group(2))}"', m.group(5)))
        last = m.end()
    out.append(clean(html[last:]))
    return ''.join(out)

if __name__ == '__main__':
    for f in sys.argv[1:]:
        s = open(f, encoding='utf-8').read()
        t = clean_html(s) if f.endswith('.html') else _scan(s)
        if t != s:
            open(f, 'w', encoding='utf-8').write(t)
            print('cleaned', f)
