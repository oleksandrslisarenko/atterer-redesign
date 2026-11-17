import sys, os, re, pathlib, html
sys.path.insert(0, os.path.dirname(__file__))
from jinja2 import Environment, FileSystemLoader
import content as C

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "src" / "templates"
OUT = ROOT / "site"


def md(text):
    """Tiny markdown for legal texts: ##/###/#### headings, '- ' lists, paragraphs, autolinks."""
    out, in_list = [], False
    link = lambda s: re.sub(r'(https?://[^\s<)]+[^\s<).,])', r'<a href="\1" target="_blank" rel="noopener">\1</a>', html.escape(s, quote=False))
    for line in text.strip().splitlines():
        line = line.rstrip()
        if not line:
            continue
        if line.startswith('- '):
            if not in_list:
                out.append('<ul>'); in_list = True
            out.append(f'<li>{link(line[2:])}</li>'); continue
        if in_list:
            out.append('</ul>'); in_list = False
        m = re.match(r'^(#{2,4}) (.*)', line)
        if m:
            lvl = len(m.group(1)); t = m.group(2)
            idn = re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')[:40]
            out.append(f'<h{lvl} id="{idn}">{html.escape(t)}</h{lvl}>')
        else:
            out.append(f'<p>{link(line)}</p>')
    if in_list:
        out.append('</ul>')
    return "\n".join(out)


def toc(text):
    return [(m.group(1), re.sub(r'[^a-z0-9]+', '-', m.group(1).lower()).strip('-')[:40]) for m in re.finditer(r'^## (.*)$', text, re.M)]


env = Environment(loader=FileSystemLoader(str(SRC)), autoescape=False, trim_blocks=True, lstrip_blocks=True)
env.globals.update({k: getattr(C, k) for k in dir(C) if k.isupper()})
env.globals["C"] = C.COMPANY
env.globals["P"] = {p["slug"]: p for p in C.PRODUCTS}

LEGAL = {}
for name in ["agb", "datenschutz"]:
    t = (ROOT / "src" / "legal" / f"{name}.md").read_text(encoding="utf-8")
    LEGAL[name] = {"html": md(t), "toc": toc(t)}


def pages():
    """(output file, template, context) for every page of a variant."""
    yield "index.html", "index", {}
    yield "firma.html", "firma", {}
    yield "qualitaetsmanagement.html", "qualitaetsmanagement", {}
    yield "produkte.html", "produkte", {}
    yield "bewehrungsstahl.html", "bewehrungsstahl", {}
    for slug, pp in C.PRODUCT_PAGES.items():
        yield f"{slug}.html", "produkt", {"slug": slug, "pp": pp, "prod": next(p for p in C.PRODUCTS if p["slug"] == slug)}
    yield "karriere.html", "karriere", {}
    for slug, jp in C.JOB_PAGES.items():
        yield f"{slug}.html", "job", {"slug": slug, "jp": jp}
    yield "ausbildung.html", "ausbildung", {}
    for slug, ap in C.AUSBILDUNG_PAGES.items():
        yield f"{slug}.html", "ausbildung-beruf", {"slug": slug, "ap": ap}
    yield "initiativbewerbung.html", "initiativbewerbung", {}
    yield "downloads.html", "downloads", {}
    yield "kontakt.html", "kontakt", {}
    yield "impressum.html", "legal", {"legal_title": "Impressum", "legal_kind": "impressum"}
    yield "datenschutz.html", "legal", {"legal_title": "Datenschutzerklärung", "legal_kind": "datenschutz", "legal": LEGAL["datenschutz"]}
    yield "agb.html", "legal", {"legal_title": "Allgemeine Geschäftsbedingungen", "legal_kind": "agb", "legal": LEGAL["agb"]}


def build(v):
    (OUT / v).mkdir(parents=True, exist_ok=True)
    allp = list(pages())
    built = []
    for out, tpl, ctx in allp:
        if (SRC / v / f"{tpl}.html").exists():
            built.append(out)
    n = 0
    for out, tpl, ctx in allp:
        if out not in built:
            continue
        html_ = env.get_template(f"{v}/{tpl}.html").render(page=out[:-5], built=",".join(built), variant=v, **ctx)
        (OUT / v / out).write_text(html_, encoding="utf-8")
        n += 1
    print(f"built {v}: {n} pages")


for v in (sys.argv[1:] or ["v1", "v2", "v3"]):
    build(v)
