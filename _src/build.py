import sys, os, pathlib
sys.path.insert(0, os.path.dirname(__file__))
from jinja2 import Environment, FileSystemLoader
import content as C

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "src" / "templates"
OUT = ROOT / "site"

env = Environment(loader=FileSystemLoader(str(SRC)), autoescape=False, trim_blocks=True, lstrip_blocks=True)
env.globals.update({k: getattr(C, k) for k in dir(C) if k.isupper()})
env.globals["C"] = C.COMPANY
env.globals["P"] = {p["slug"]: p for p in C.PRODUCTS}

VARIANTS = sys.argv[1:] or ["v1", "v2", "v3"]
PAGES = ["index", "bewehrungsstahl", "karriere"]
BUILT = ",".join(p + ".html" for p in PAGES)

for v in VARIANTS:
    (OUT / v).mkdir(parents=True, exist_ok=True)
    for page in PAGES:
        tpl = env.get_template(f"{v}/{page}.html")
        html = tpl.render(page=page, built=BUILT, variant=v)
        (OUT / v / f"{page}.html").write_text(html, encoding="utf-8")
    print("built", v)
