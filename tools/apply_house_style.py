"""Apply the Computing department's classroom-resources house style to every simulation.

Usage: python3 tools/apply_house_style.py [FONT_DIR]   (defaults to tools/fonts)

FONT_DIR holds the latin-subset woff2 files for Atkinson Hyperlegible Next,
Atkinson Hyperlegible Mono and Lexend (all SIL Open Font Licence). They are embedded
as base64 so each simulation stays a single file that works offline and behind
school web filters. Re-running the script replaces the previous house-style block.
"""
import base64
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SIMS = ['fde-cycle.html', 'binary-register.html', 'sort-search.html', 'trace-table.html', 'tcp-ip.html', 'sound-sampling.html', 'bitmap-builder.html']

FONTS = [  # (family, weight range, filename prefix)
    ('Atkinson Hyperlegible Next', '400 700', 'NaPNcYPdHfdVxJw0'),
    ('Atkinson Hyperlegible Mono', '400 700', 'tss4AoFBci4C4gvh'),
    ('Lexend', '500 700', 'wlpwgwvFAVdoq2'),
]

# Material Symbols paths (Apache 2.0), used as CSS masks so they take the text colour.
ICONS = {
    'pencil': 'M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04a1 1 0 0 0 0-1.41l-2.34-2.34a1 1 0 0 0-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z',
    'book': 'M21 5c-1.11-.35-2.33-.5-3.5-.5-1.95 0-4.05.4-5.5 1.5-1.45-1.1-3.55-1.5-5.5-1.5S2.45 4.9 1 6v14.65c0 .25.25.5.5.5.1 0 .15-.05.25-.05C3.1 20.45 5.05 20 6.5 20c1.95 0 4.05.4 5.5 1.5 1.35-.85 3.8-1.5 5.5-1.5 1.65 0 3.35.3 4.75 1.05.1.05.15.05.25.05.25 0 .5-.25.5-.5V6c-.6-.45-1.25-.75-2-1zm0 13.5c-1.1-.35-2.3-.5-3.5-.5-1.7 0-4.15.65-5.5 1.5V8c1.35-.85 3.8-1.5 5.5-1.5 1.2 0 2.4.15 3.5.5v11.5z',
    'help': 'M11 18h2v-2h-2v2zm1-16C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm0-14c-2.21 0-4 1.79-4 4h2c0-1.1.9-2 2-2s2 .9 2 2c0 2-3 1.75-3 5h2c0-2.25 3-2.5 3-5 0-2.21-1.79-4-4-4z',
    'star': 'M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z',
    'code': 'M9.4 16.6L4.8 12l4.6-4.6L8 6l-6 6 6 6 1.4-1.4zm5.2 0l4.6-4.6-4.6-4.6L16 6l6 6-6 6-1.4-1.4z',
    'warn': 'M1 21h22L12 2 1 21zm12-3h-2v-2h2v2zm0-4h-2v-4h2v4z',
}


def icon_url(name):
    svg = f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><path d='{ICONS[name]}'/></svg>"
    return 'url("data:image/svg+xml,' + svg.replace('<', '%3C').replace('>', '%3E') + '")'


def font_faces(font_dir):
    css = []
    for family, weights, prefix in FONTS:
        (path,) = [p for p in font_dir.glob('*.woff2') if p.name.startswith(prefix)]
        data = base64.b64encode(path.read_bytes()).decode()
        css.append(f'@font-face{{font-family:"{family}";font-style:normal;font-weight:{weights};font-display:swap;'
                   f'src:url(data:font/woff2;base64,{data}) format("woff2")}}')
    return '\n'.join(css)


HOUSE_CSS = r"""
/* ===== House style: St David's College Computing classroom resources ===== */
:root{
  --navy:#001F5B; --gold:#85764d; --navy-soft:#e8ebf3;
  --accent:var(--navy); --accent-soft:var(--navy-soft);
  --ink:#000; --muted:#474747; --line:#c6c6c6; --bg:#f6f4ee; --surface2:#f2f2f2;
  --sans:"Atkinson Hyperlegible Next",Verdana,system-ui,sans-serif;
  --mono:"Atkinson Hyperlegible Mono",Consolas,"Cascadia Mono",monospace;
  --head:"Lexend",Verdana,system-ui,sans-serif;
}
html{font-size:16px}
body{line-height:1.5}
*{text-transform:none!important;letter-spacing:normal!important}
i,em,.cm{font-style:normal!important}
h1,h2,h3,.box-title,.tool-head h2,.brand h1,dialog h2,.pane h3{font-family:var(--head);font-weight:700;color:var(--navy)}
h3,.pane h3{font-weight:600}
.box-title small,.pane h3 .status{font-family:var(--sans)}
.btn.primary:hover{background:#00143d}
.bit.b1:hover:not(:disabled){background:#00143d}
.box,.stage{border-color:var(--navy)}
.seg button[aria-pressed="true"],.btn[aria-pressed="true"]{background:var(--navy);border-color:var(--navy);color:#fff}
.tabpanel{font-size:1rem}
.tabpanel p,.tabpanel li{max-width:70ch}

/* header bar: navy with a gold accent line */
.topbar{background:var(--navy);color:#fff;border-bottom:4px solid var(--gold)}
.topbar .brand h1{color:#fff}
.topbar .brand span,.topbar label.field{color:#d9ddea}
.topbar #speedLabel{color:#fff}
.topbar .btn{background:transparent;color:#fff;border-color:rgba(255,255,255,.55)}
.topbar .btn:hover{background:rgba(255,255,255,.14)}
.topbar .btn[aria-pressed="true"]{background:#fff;color:var(--navy);border-color:#fff}
.topbar .btn.primary{background:#fff;color:var(--navy);border:2px solid var(--gold)}
.topbar .btn.primary:hover{background:#e9ecf4}
.topbar .btn[disabled]{opacity:.45}
.topbar .seg{background:transparent;border-color:rgba(255,255,255,.55)}
.topbar .seg button{color:#fff;border-right-color:rgba(255,255,255,.35)}
.topbar .seg button[aria-pressed="true"]{background:#fff;color:var(--navy)}
.topbar select{background:#fff;color:#000}
.topbar input[type=range]{accent-color:var(--gold)}
.topbar .btn:focus-visible,.topbar .seg button:focus-visible{outline-color:#fff}

/* caption bar */
#dock{background:var(--navy);border-top:4px solid var(--gold)}
#dock .badge{background:transparent;border:2px solid var(--gold);color:#fff;font-family:var(--head);font-weight:600}
#dock .badge.predict,#dock .badge.ch{background:#ffd84d;border-color:#ffd84d;color:#000}
#dock .badge.done{background:#fff;border-color:#fff;color:var(--navy)}
#dock .badge.warn{background:#fff;border-color:#fff;color:#b42318}
.badge{font-family:var(--head);font-weight:600}
.tab{font-family:var(--head);font-weight:600}
.tab[aria-selected="true"]{color:var(--navy);border-bottom-color:var(--gold)}

/* explanation boxes: the guide's components, told apart by border and icon, not shade */
.tip{background:#fff;border:0;border-left:5px solid #000;border-radius:.3rem;padding:.6rem .85rem;--ic:ICON_PENCIL}
.tip-title{display:flex;align-items:center;gap:.4rem;font-family:var(--head);font-weight:600;font-size:.95rem;color:var(--navy);margin-bottom:.2rem}
.tip-title::before{content:"";flex:none;width:1.25em;height:1.25em;background:currentColor;-webkit-mask:var(--ic) center/contain no-repeat;mask:var(--ic) center/contain no-repeat}
.tip.key,.tip.now{background:#ebebeb;border:0;--ic:ICON_BOOK}
.tip.exam{background:#fff;border:1.5px dashed #3a3a3a;--ic:ICON_HELP}
.tip.chal{background:#fff;border:4px double #000;--ic:ICON_STAR}
.warn,.warnbox{position:relative}
.warn::before,.warnbox::before{content:"";display:inline-block;width:1.1em;height:1.1em;margin-right:.35em;vertical-align:-.18em;background:currentColor;-webkit-mask:ICON_WARN center/contain no-repeat;mask:ICON_WARN center/contain no-repeat}
.codebox .ch>span:first-child{display:inline-flex;align-items:center;gap:.35rem}
.codebox .ch>span:first-child::before{content:"";width:1.2em;height:1.2em;background:currentColor;-webkit-mask:ICON_CODE center/contain no-repeat;mask:ICON_CODE center/contain no-repeat}

/* states that must not depend on colour alone */
.bar.cmp{box-shadow:inset 0 0 0 3px #000;background-image:repeating-linear-gradient(45deg,transparent 0 6px,rgba(0,0,0,.12) 6px 9px)}
.bar.swap{box-shadow:inset 0 0 0 3px #000}
.card.chk .cv{border-width:3px;border-style:dashed}
.card.found .cv{box-shadow:0 0 0 3px var(--gold)}
"""


def tip_classes(html):
    html = re.sub(r'class="tip"><span class="tip-title">(Key point|What do the registers do\?|Two’s complement)', r'class="tip key"><span class="tip-title">\1', html)
    html = html.replace('class="tip exam"><span class="tip-title">Hex', 'class="tip key"><span class="tip-title">Hex')
    html = html.replace('class="tip"><span class="tip-title">Exam tip', 'class="tip exam"><span class="tip-title">Exam tip')
    html = html.replace('class="tip"><span class="tip-title">Challenge', 'class="tip chal"><span class="tip-title">Challenge')
    return html


def no_italics(html):
    html = html.replace('<i>Instruction or data?</i>', '“Instruction or data?”')
    # unwrap plain <i>…</i> pairs only, so other tags are never left unclosed
    return re.sub(r'<i>(.*?)</i>', r'\1', html, flags=re.S)


def apply(path, faces):
    html = path.read_text()
    html = re.sub(r'\n<style id="house-style">.*?</style>', '', html, flags=re.S)
    css = HOUSE_CSS
    for name in ICONS:
        css = css.replace('ICON_' + name.upper(), icon_url(name))
    block = f'\n<style id="house-style">\n{faces}\n{css}</style>'
    html = html.replace('</style>\n</head>', '</style>' + block + '\n</head>', 1)
    html = tip_classes(no_italics(html))
    path.write_text(html)


if __name__ == '__main__':
    faces = font_faces(pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'tools' / 'fonts')
    for name in SIMS:
        apply(ROOT / name, faces)
        print('styled', name)
