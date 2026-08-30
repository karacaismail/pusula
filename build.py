#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pusula build: src/ parcalarini tek dosyalik v2/index.html olarak birlestirir.

Kullanim:
    python3 build.py            # v2/index.html uret
    python3 build.py --check    # uret ama yazma; mevcut ciktiyla farki bildir

Kural: v2/index.html ELLE DUZENLENMEZ. Icerik degisikligi src/30-body.html,
grafik degisikligi src/50-charts.js, stil degisikligi src/20-style-sprite.html
dosyasinda yapilir. 10-daisyui.css ve 40-echarts.js vendor dosyalaridir; yalniz
surum yukseltmede degistirilir.
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "v2", "index.html")

ORDER = [
    "src/00-head.html",        # meta, title, font, favicon, <style> acilisi
    "src/10-daisyui.css",      # vendor: daisyUI 5.7.22
    "src/20-style-sprite.html",# ozel CSS + </style> + .wrap + Phosphor sprite
    "src/30-body.html",        # ICERIK
    "src/40-echarts.js",       # vendor: Apache ECharts 5 (<script> ile sarili)
    "src/50-charts.js",        # grafik baslatma
]

# Yayin oncesi zorunlu kontroller: (aciklama, kosul)
def checks(html: str):
    lower = html.lower()
    yield "charset var", '<meta charset="utf-8">' in lower
    yield "viewport var", 'name="viewport"' in lower
    yield "noindex var", "noindex" in lower
    yield "title var", "<title>" in lower
    yield "tek <style> blogu", html.count("</style>") == 1
    yield "3 <script> blogu", html.count("</script>") == 2
    yield "emoji yok (ikon)", "📊" not in html and "✅" not in html and "🚀" not in html
    yield "ucuncu kisi adi yok", "Üzeyir" not in html and "Ozan" not in html
    yield "kapsam disi proje yok", "Zabuno" not in html and "Cups" not in html
    yield "changelog anlatisi yok", "Bu turda kapananlar" not in html and "v2.2 —" not in html


def build() -> str:
    out = []
    for rel in ORDER:
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            sys.exit(f"EKSIK PARCA: {rel}")
        out.append(io.open(path, encoding="utf-8").read())
    return "".join(out)


def main():
    html = build()
    failed = [name for name, ok in checks(html) if not ok]
    for name, ok in checks(html):
        print(("  OK   " if ok else "  HATA ") + name)
    if failed:
        sys.exit("\nYayinlanmadi. Once su kontrolleri gecir: " + ", ".join(failed))

    if "--check" in sys.argv:
        cur = io.open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
        print("\nFark: " + ("YOK (cikti guncel)" if cur == html else "VAR (build gerekli)"))
        return

    io.open(OUT, "w", encoding="utf-8").write(html)
    print(f"\nYazildi: v2/index.html  ({len(html):,} bayt)")
    print("Sonraki adim: git add -A && git commit && git push  ->  ~1-2 dk sonra GitHub Pages guncellenir")


if __name__ == "__main__":
    main()
