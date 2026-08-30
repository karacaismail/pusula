#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pusula v4 HTML uretici.

KAYNAK: /Users/karaca/Documents/pusula/v4/*.md  — SALT OKUNUR, hicbiri degistirilmez.
CIKTI : <repo>/v4/index.html

Kullanim: python3 tools/build_v4.py
"""
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from md2html import convert  # noqa: E402

SRC_MD = "/Users/karaca/Documents/pusula/v4"
OUT = os.path.join(ROOT, "v4", "index.html")

# Kume dosyalari: (dosya, kisa ad, ikon)
CLUSTERS = [
    ("00-INDEX.md", "Küme haritası", "compass"),
    ("00b-atonota-holding.md", "AtonotA çatı şirket", "stack"),
    ("01-nakit-ve-borc.md", "Nakit ve borç", "wallet"),
    ("02-gelir-titanlar.md", "titanlar (kohort okulu)", "coins"),
    ("03-urun-destektesvik.md", "DestekTeşvik", "clipboard-text"),
    ("04-urun-arsam.md", "arsam", "clipboard-text"),
    ("05-ic-kabiliyet-metaframer-aep.md", "MetaFramer + AEP", "engine"),
    ("05b-atonota-ui-kit.md", "AtonotA UI Kit", "frame-corners"),
    ("06-gayrimenkul.md", "Gayrimenkul", "wallet"),
    ("07-hedef-servet-ve-hasat.md", "Hedef, servet, hasat", "coins"),
    ("08-zaman-ve-kapasite.md", "Zaman ve kapasite", "hourglass"),
    ("09-saglik-ve-koruma.md", "Sağlık ve koruma", "heartbeat"),
    ("10-aile-ve-yasam-vizyonu.md", "Aile ve yaşam vizyonu", "sailboat"),
    ("11-kimlik-ve-cevre.md", "Kimlik ve çevre", "user-focus"),
    ("12-riskler-ve-unk-unks.md", "Riskler ve unk-unks", "eye-slash"),
    ("13-karar-yontemi-ve-ritim.md", "Karar yöntemi ve ritim", "list-checks"),
    ("14-veri-defteri.md", "Veri defteri", "clipboard-text"),
    ("15-yayin-ve-mahremiyet.md", "Yayın ve mahremiyet", "eye-slash"),
    ("16-girisim-planlama-cercevesi.md", "Girişim planlama çerçevesi", "flag-checkered"),
]

RESEARCH = [
    ("bilimsel yaklaşım girişim.md", "Bilimsel yaklaşım — girişim", "question"),
    ("bilimsel yaklaşım girişim-2.md", "Bilimsel yaklaşım — değişmezler", "question"),
    ("bilimsel yaklaşım pazarlama.md", "Bilimsel yaklaşım — pazarlama", "question"),
    ("Girişim Başarısızlık önlemleri Analizi.md", "Başarısızlık önlemleri analizi", "warning-diamond"),
    ("AtonotA Marka Ouroboros.md", "AtonotA · Ouroboros", "compass"),
    ("marka/atonota/Atonota marka anlamlandırma araştırması.md", "AtonotA marka araştırması", "compass"),
]


def read(rel):
    p = os.path.join(SRC_MD, rel)
    if not os.path.exists(p):
        return None
    return io.open(p, encoding="utf-8").read()


def slug(name):
    s = re.sub(r'\.md$', '', os.path.basename(name)).lower()
    s = s.replace(" ", "-")
    return re.sub(r'[^a-z0-9-]', '', s.replace("ı", "i").replace("ş", "s").replace("ğ", "g")
                  .replace("ü", "u").replace("ö", "o").replace("ç", "c"))


def doc_section(rel, title, icon):
    md = read(rel)
    if md is None:
        return None, None
    body = convert(md)
    sid = slug(rel)
    html = (
        '<details class="docbox" id="%s">\n'
        '  <summary><svg class="ph" aria-hidden="true"><use href="#ph-%s"/></svg>'
        '<span>%s</span><span class="docmeta">%s</span></summary>\n'
        '  <div class="doccontent">%s</div>\n'
        '</details>' % (sid, icon, title, os.path.basename(rel), body)
    )
    return html, (sid, title)


def build():
    # --- tasarim parcalari (mevcut sistemden) ---
    head_css = io.open(os.path.join(ROOT, "src", "10-daisyui.css"), encoding="utf-8").read()
    style_sprite = io.open(os.path.join(ROOT, "src", "20-style-sprite.html"), encoding="utf-8").read()
    custom_css = style_sprite.split("</style>")[0]
    sprite = style_sprite[style_sprite.find('<svg xmlns'):]
    sprite = sprite[:sprite.rfind("</svg>") + len("</svg>")]

    synth = io.open(os.path.join(HERE, "v4-sentez.html"), encoding="utf-8").read()

    cluster_html, cluster_nav = [], []
    for rel, title, icon in CLUSTERS:
        h, nav = doc_section(rel, title, icon)
        if h:
            cluster_html.append(h)
            cluster_nav.append(nav)

    research_html, research_nav = [], []
    for rel, title, icon in RESEARCH:
        h, nav = doc_section(rel, title, icon)
        if h:
            research_html.append(h)
            research_nav.append(nav)

    v4css = """
.docbox { border: 1px solid var(--color-base-300); border-radius: var(--radius-box); background: var(--color-base-100); margin-bottom: 0.6rem; }
.docbox > summary { display: flex; align-items: center; gap: 0.55rem; padding: 0.9rem 1.05rem; cursor: pointer; font-weight: 700; }
.docbox > summary::-webkit-details-marker { display: none; }
.docbox > summary:hover { color: var(--color-primary); }
.docbox[open] > summary { border-bottom: 1px solid var(--color-base-300); color: var(--color-primary); }
.docmeta { margin-left: auto; font-weight: 400; font-size: 1rem; color: color-mix(in oklab, var(--color-base-content) 50%, transparent); }
.doccontent { padding: 1.1rem 1.15rem 1.4rem; }
.doccontent h1 { font-size: 1.5rem; margin: 0 0 0.6rem; }
.doccontent h2 { font-size: 1.3rem; margin: 1.6rem 0 0.5rem; }
.doccontent h3 { font-size: 1.12rem; margin: 1.2rem 0 0.4rem; }
.doccontent h4 { font-size: 1rem; margin: 1rem 0 0.35rem; }
.doccontent p { margin: 0.5rem 0; }
.doccontent ul, .doccontent ol { margin: 0.5rem 0 0.8rem; padding-left: 1.25rem; list-style: disc outside; }
.doccontent ol { list-style: decimal outside; }
.doccontent li { margin: 0.2rem 0; display: list-item; }
.doccontent ul.checklist { list-style: none; padding-left: 0.2rem; }
.doccontent blockquote { border-left: 3px solid var(--color-primary); background: var(--color-base-200); padding: 0.6rem 0.9rem; margin: 0.7rem 0; border-radius: 0 0.5rem 0.5rem 0; }
.doccontent blockquote p { margin: 0.25rem 0; }
.doccontent pre { background: var(--color-base-200); border: 1px solid var(--color-base-300); border-radius: 0.5rem; padding: 0.8rem 0.9rem; overflow-x: auto; margin: 0.6rem 0; }
.doccontent code { background: var(--color-base-200); padding: 0.1rem 0.32rem; border-radius: 0.3rem; }
.doccontent pre code { background: none; padding: 0; }
.doccontent hr { border: none; border-top: 1px solid var(--color-base-300); margin: 1.3rem 0; }
.doccontent input[type=checkbox] { margin-right: 0.4rem; }
.synth h2 { margin-top: 0; }
.pill { display: inline-block; border: 1px solid var(--color-base-300); background: var(--color-base-200); border-radius: 999px; padding: 0.15rem 0.7rem; margin: 0 0.3rem 0.35rem 0; font-size: 1rem; }
.stage { border-left: 3px solid var(--color-primary); padding-left: 0.8rem; margin: 0.7rem 0; }
.verdict-bad { border-left-color: var(--color-error); }
.verdict-ok { border-left-color: var(--color-success); }
.lead-note { border: 1px solid var(--color-base-300); border-left: 3px solid var(--color-warning); border-radius: 0.6rem; background: var(--color-base-200); padding: 0.9rem 1rem; margin: 1rem 0; }
"""

    parts = []
    parts.append('<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
                 '<meta name="robots" content="noindex, nofollow">\n'
                 '<title>AtonotA Pusula v4</title>\n'
                 '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@400..900&display=swap">\n'
                 '<style>\n')
    parts.append(head_css)
    parts.append(custom_css)
    parts.append(v4css)
    parts.append('</style>\n<div class="wrap">\n')
    parts.append(sprite)
    parts.append(synth)

    parts.append('<section id="kumeler"><div class="eyebrow">Kaynak belgeler · 19 küme</div>'
                 '<h2><svg class="ph" aria-hidden="true"><use href="#ph-list-checks"/></svg>v4 küme dosyaları</h2>'
                 '<p class="muted">Her küme: bilinen veri · soru kalıpları · araştırma sorguları · unk-unk taraması · '
                 'karar kapıları · kabul kriteri. Başlığa dokun, açılır.</p><div style="margin-top:1rem">')
    parts.extend(cluster_html)
    parts.append('</div></section>')

    parts.append('<section id="arastirma"><div class="eyebrow">Kaynak belgeler · yöntem araştırmaları</div>'
                 '<h2><svg class="ph" aria-hidden="true"><use href="#ph-question"/></svg>Bilimsel yaklaşım ve marka belgeleri</h2>'
                 '<p class="muted">Bu bölümdeki belgeler kullanıcının kendi araştırmalarıdır; yukarıdaki konumlandırma '
                 'bunlardan türetilmiştir.</p><div style="margin-top:1rem">')
    parts.extend(research_html)
    parts.append('</div></section>')

    parts.append("""
<footer class="footer-note">
  <p><strong>Kaynak ve biçim:</strong> Bu sayfa <code>/Users/karaca/Documents/pusula/v4/</code> altındaki Markdown
  kümelerinden üretilmiştir; kaynak dosyalar salt okunur olarak işlenir, değiştirilmez. Üretici:
  <code>tools/build_v4.py</code>. Kanonik çalışma alanı Markdown'dır; bu HTML yalnız okuma ve paylaşım içindir.</p>
  <p><strong>Sınır:</strong> Bu sayfa yatırım, hukuk, vergi veya sağlık tavsiyesi değildir. Kredi, sigorta, vergi,
  hukuk ve sağlık adımları için ilgili lisanslı uzmandan yazılı teyit alınır. Sayıların bir kısmı
  <code>[VARSAYIM]</code> ve <code>[EKSİK]</code> etiketlidir; karar girdisi değildir.</p>
  <p><strong>Mahremiyet:</strong> Sayfa <code>noindex</code> ile yayınlanır; bağlantıyı bilen herkes okuyabilir.
  Yayın kararı (kamuya açık / kapalı / anonim özet) hâlâ açıktır — küme 15.</p>
</footer>
</div>
""")

    html = "".join(parts)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    io.open(OUT, "w", encoding="utf-8").write(html)

    print("Kume dosyasi   : %d" % len(cluster_html))
    print("Arastirma belg.: %d" % len(research_html))
    print("Cikti          : v4/index.html  (%s bayt)" % format(len(html), ","))
    missing = [r for r, _, _ in CLUSTERS + RESEARCH if read(r) is None]
    if missing:
        print("UYARI okunamayan:", missing)


if __name__ == "__main__":
    build()
