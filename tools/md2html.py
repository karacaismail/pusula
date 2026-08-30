#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kucuk Markdown -> HTML donusturucu (bagimliliksiz).

Kapsam: baslik, paragraf, liste (ic ice yok), numarali liste, onay kutusu,
tablo, kod blogu, alinti, yatay cizgi, kalin/italik/kod/link.
Amac: Pusula v4 .md kumelerini tek sayfalik HTML'e cevirmek.
KAYNAK DOSYALAR SALT OKUNUR — bu betik hicbir .md dosyasini degistirmez.
"""
import html
import re


def _inline(t: str) -> str:
    t = html.escape(t, quote=False)
    # kod
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    # link
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', t)
    # kalin
    t = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', t)
    # italik (tek yildiz, kalin sonrasi)
    t = re.sub(r'(?<!\*)\*([^*\n]+)\*(?!\*)', r'<em>\1</em>', t)
    return t


def _cells(line: str):
    line = line.strip()
    if line.startswith('|'):
        line = line[1:]
    if line.endswith('|'):
        line = line[:-1]
    return [c.strip() for c in line.split('|')]


def convert(md: str) -> str:
    lines = md.split('\n')
    out = []
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]
        s = line.strip()

        # kod blogu
        if s.startswith('```'):
            lang = s[3:].strip()
            i += 1
            buf = []
            while i < n and not lines[i].strip().startswith('```'):
                buf.append(html.escape(lines[i]))
                i += 1
            i += 1
            cls = ' class="lang-' + re.sub(r'[^a-z0-9-]', '', lang.lower()) + '"' if lang else ''
            out.append('<pre><code%s>%s</code></pre>' % (cls, '\n'.join(buf)))
            continue

        # yatay cizgi
        if re.fullmatch(r'-{3,}', s):
            out.append('<hr/>')
            i += 1
            continue

        # baslik
        m = re.match(r'^(#{1,6})\s+(.*)$', s)
        if m:
            lvl = len(m.group(1))
            out.append('<h%d>%s</h%d>' % (lvl, _inline(m.group(2)), lvl))
            i += 1
            continue

        # tablo
        if s.startswith('|') and i + 1 < n and re.match(r'^\|[\s:|-]+\|?$', lines[i + 1].strip()):
            head = _cells(s)
            i += 2
            rows = []
            while i < n and lines[i].strip().startswith('|'):
                rows.append(_cells(lines[i]))
                i += 1
            th = ''.join('<th>%s</th>' % _inline(c) for c in head)
            tb = ''
            for r in rows:
                tb += '<tr>' + ''.join('<td>%s</td>' % _inline(c) for c in r) + '</tr>'
            out.append('<div class="tablebox"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (th, tb))
            continue

        # alinti
        if s.startswith('>'):
            buf = []
            while i < n and lines[i].strip().startswith('>'):
                buf.append(lines[i].strip()[1:].strip())
                i += 1
            inner = convert('\n'.join(buf))
            out.append('<blockquote>%s</blockquote>' % inner)
            continue

        # liste (onay kutusu dahil)
        if re.match(r'^[-*]\s+', s):
            items = []
            while i < n and re.match(r'^[-*]\s+', lines[i].strip()):
                txt = re.sub(r'^[-*]\s+', '', lines[i].strip())
                cb = ''
                m2 = re.match(r'^\[( |x|X)\]\s*(.*)$', txt)
                if m2:
                    checked = ' checked' if m2.group(1).lower() == 'x' else ''
                    cb = '<input type="checkbox" disabled%s/> ' % checked
                    txt = m2.group(2)
                items.append('<li>%s%s</li>' % (cb, _inline(txt)))
                i += 1
            cls = ' class="checklist"' if 'type="checkbox"' in ''.join(items) else ''
            out.append('<ul%s>%s</ul>' % (cls, ''.join(items)))
            continue

        # numarali liste
        if re.match(r'^\d+[.)]\s+', s):
            items = []
            while i < n and re.match(r'^\d+[.)]\s+', lines[i].strip()):
                txt = re.sub(r'^\d+[.)]\s+', '', lines[i].strip())
                items.append('<li>%s</li>' % _inline(txt))
                i += 1
            out.append('<ol>%s</ol>' % ''.join(items))
            continue

        # bos satir
        if not s:
            i += 1
            continue

        # paragraf
        buf = []
        while i < n and lines[i].strip() and not re.match(r'^(#{1,6}\s|[-*]\s|\d+[.)]\s|>|\||```|-{3,}$)', lines[i].strip()):
            buf.append(lines[i].strip())
            i += 1
        if buf:
            out.append('<p>%s</p>' % _inline(' '.join(buf)))

    return '\n'.join(out)
