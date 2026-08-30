# Pusula — Devir Yönergesi (Cursor için)

**Belge tarihi:** 30 Ağustos 2026 · **Devreden:** Claude Code oturumu · **Devralan:** Cursor
**Bu belgenin işi:** Projeyi hiç görmemiş birinin, kimseye soru sormadan devam edebilmesi.

---

## 0. Otuz saniyelik özet

Bu bir **yazılım ürünü değil**, bir **karar aracıdır**: tek kişilik bir girişimcinin (İsmail Karaca)
para, proje, aile ve sağlık kararlarını tek sayfada, kanıta bağlı biçimde görmesini sağlayan
statik bir web raporu. İki parçası vardır: **bugünün fotoğrafı** ve **kronolojik yol haritası**.

- **Canlı (güncel):** https://karacaismail.github.io/pusula/v3/
- **Canlı (donduruldu):** https://karacaismail.github.io/pusula/v2/
- **Canlı (eski arşiv, dokunulmaz):** https://karacaismail.github.io/pusula/
- **Depo:** https://github.com/karacaismail/pusula (public)
- **Yerel çalışma kopyası:** `/Users/karaca/DEV/pusula` ← Cursor bunu açacak
- **Teknoloji:** tek dosyalık HTML + DaisyUI 5 + Apache ECharts 5 + Phosphor Icons. Derleme: `python3 build.py`.

---

## 1. Bu proje nereden başladı, ne oldu (kronoloji)

| Aşama | Ne soruldu | Ne üretildi |
|---|---|---|
| 1 | "Projelerim neler? Ekonomik/gerçekleştirilebilirlik/yatırımcı bakımından karşılaştır" | Diskteki 63 depo + DEV klasörü tarandı; 7 girişim çıkarıldı; **Portföy Karnesi** raporu |
| 2 | "Hedeflerim için ne kadar para gerekli, nasıl kazanırım? Gap + unk-unks analizi yap, soru setleri hazırla" | Hedeflerin fiyat etiketi (≈5M $), üç motorlu gelir modeli, 19 soruluk gap formu → **Yaşam Planı Pusulası** |
| 3 | 19 sorunun cevapları geldi | Plan cevaplarla yeniden kuruldu; başlama takvimi + SMART karne eklendi |
| 4 | "GitHub Pages'te yayınla" | `karacaismail/pusula` deposu açıldı, Pages açıldı, `noindex` eklendi |
| 5 | Yeni gerçekler: borç kırılımı, USD kuralı, 5 yıl kuralı, arsam pivotu, AtonotA=MetaFramer | Rapor v3 → tüm ikonlar Phosphor'a çevrildi (emoji yasağı), ECharts grafikleri eklendi |
| 6 | "Şu ikinci raporu master ile birleştir" (Codex'in *Yaşam ve Ekonomik Özgürlük Raporu v3*) | İki rapor birleştirildi → `/v2/` yayına girdi; eski sayfa arşiv olarak korundu |
| 7 | "Eksik/çelişki/gap var mı? Soru setleri hazırla" | Denetim: 6 karar + 12 eksik veri → 18 cevap geldi → **nakit alarmı** bulgusu ortaya çıktı |
| 8 | Codex'in `problematic.md` teşhis raporu | 14 P0'dan 9'u bayat, 5'i işlendi, 1'i (mahremiyet) hâlâ karar bekliyor |
| 9 | "Sürekli tekrar eden veri var; sadece durum + gelecek planı olsun" | **Sayfa sıfırdan yeniden yazıldı**: changelog anlatısı silindi, 7 bölüm, her veri tek yerde |
| 10 | "Cursor'a devret" | Bu belge + `src/` kaynak yapısı + `build.py` |

**Kritik ders (tekrar etmeyin):** 9. aşamaya kadar her güncelleme "şu düzeltildi / bu karar verildi"
anlatısı olarak sayfaya eklendi. Sonuç: aynı veri 5–44 kez tekrarlandı (kohort 44×, kart yapılandırma 24×).
**Sayfa bir günlük değil, bir durum kaydıdır.** Değişiklik geçmişi yalnız git'te durur.

---

## 2. Amaç ve kapsam

### Amaç
Sahibinin şu üç soruyu her an tek yerden cevaplayabilmesi:
1. **Bugün neredeyim?** (nakit, borç, projeler, sağlık, eksik veriler)
2. **Nereye gidiyorum ve maliyeti ne?** (5 yılda ≈5M $ hedefi, hasat şartlı bahis, Plan B)
3. **Sırada ne var, hangi kapı açılmadan ne başlamaz?** (kronolojik yol haritası + SMART karne)

### Kapsamdaki girişimler (yalnız bunlar)
| Girişim | Rol | Bugünkü durum |
|---|---|---|
| **titanlar** | Nakit motoru | Kohort okulu modeli; ödeyen müşteri yok |
| **arsam** | Aktif ürün 2 | Yazılım ~%70; yayında değil; marka/domain kararsız (geçici arsam.net) |
| **DestekTeşvik** | Amiral ürün | Kod yok; MVP 60 günde dışarıya yaptırılacak |
| **MetaFramer / AtonotA + AEP** | İç kabiliyet | Ayrı girişim değil; haftada ≤2 saat |
| Shopify rakibi · Zoho+Odoo rakibi | Park fikir | Kapalı kapı |

### Kapsam DIŞI (sayfada adı bile geçmez)
- **İşveren (türksab) işleri:** segika, istoç, great doers, jobiers, hrms
- **Devredilen iş:** Zabuno (arkadaşının projesi, yardım için yapılıp devredildi)
- **İptal olan müşteri işi:** capclouds için 250 bin ₺'lik e-ticaret projesi
- **Başkalarının işleri:** cupsandclouds, tolgatradingbot
- **Yurtdışı yerleşim hedefi:** kullanıcı iptal etti; plan Türkiye/Çanakkale ekseninde

---

## 3. Değişmez kurallar (bunları bozan değişiklik geri alınır)

### İçerik kuralları
1. **Emoji yasak.** Tüm ikonlar Phosphor Icons (regular). Sayfada 18 SVG sembol gömülü.
1b. **Tipografi tabanı:** yazı tipi Roboto; hiçbir metin 1rem altına, hiçbir ağırlık 400 altına inmez. `build.py` bunu denetler.
2. **Her veri tek kanonik yerde.** Aynı sayıyı ikinci kez yazacaksan, yazma — o bölüme işaretçi ver
   ("tanımı Hedef bölümünde"). Yayın öncesi tekrar taraması: `python3 tools/dupscan.py` (bkz. §9).
3. **Changelog anlatısı yok.** "Şu düzeltildi", "bu karar verildi", "tur 2'de işlendi", "v2.2'de eklendi"
   cümleleri sayfaya girmez. Sayfa yalnız **mevcut durumu** ve **geleceği** anlatır.
4. **Üçüncü kişi adı yazılmaz.** (Eski arşiv sayfasında bir isim kaldı — anonimleştirme onayı bekliyor.)
5. **Para birimi USD esas**, ₺ girdiler parantezde. Kur: 1 $ ≈ 48,2 ₺ (29.08.2026). Kritik hesaplar
   45 / 48,2 / 55 ₺ ile üç kez okunmalı (kur stres bandı).
6. **Kanıt hiyerarşisi:** son kullanıcı beyanı > resmî kaynak > türetim > varsayım. Doğrulanmamış her sayı
   "tahmin" veya "öğrenilecek" etiketiyle görünür (ör. ev satışı 8M ₺).
7. **Tarih değil kapı.** Her adımın bir **açılış kapısı** ve gerekiyorsa bir **durdurma kuralı** vardır.
   "Neredeyse bitti" bir kapı durumu değildir.
8. **Scrum/Agile terimleri yasak.** sprint, backlog, story point, velocity, standup, retro, epic, kanban
   kullanılmaz. Yerine: **waterfall fazları + ara teslim (milestone) + kapı**. (§7'deki WBS sözlüğü.)
9. **Yasal sınır:** sayfa yatırım/hukuk/vergi/sağlık tavsiyesi değildir; her finansal iddianın yanında
   "lisanslı uzmandan yazılı teyit" şartı durur. Bu dil kaldırılmaz.

### Tasarım kuralları
10. **Mobile-first.** Önce 375px, sonra masaüstü. Yatay kaydırma yok; tablolar kendi `overflow-x` kutusunda.
11. **Üç tema durumu:** açık, koyu (`prefers-color-scheme`) ve `data-theme` damgası. Renkler yalnız
    token üzerinden; hiçbir renk sadece media/`[data-theme]` bloğu içinde tanımlanmaz.
12. **Tek dosya, harici bağımlılık yok.** DaisyUI ve ECharts sayfaya gömülüdür (CSP/çevrimdışı güvenliği).
    Tek istisna: Google Fonts (Archivo).
13. **`noindex, nofollow`** meta etiketi kalır (sayfa herkese açık ama arama motorlarında listelenmemeli).
14. **İzleme/analitik kodu yok.**

---

## 4. Kullanılan teknolojiler

| Katman | Seçim | Not |
|---|---|---|
| İşaretleme | Elle yazılmış HTML5, tek dosya | Framework yok, build step yalnız birleştirme |
| Bileşen/stil | **DaisyUI 5.7.22** (saf CSS dağıtımı, gömülü) | Tailwind derleyicisi YOK — `md:` gibi önekler çalışmaz; özel medya sorguları elle yazılır |
| Özel stil | `src/20-style-sprite.html` içinde katmansız CSS | daisyUI `@layer`'ını güvenle ezer |
| Grafik | **Apache ECharts 5** (gömülü) | 4 grafik: maliyet pastası, net varlık patikası, gelir köprüsü, saat bütçesi |
| İkon | **Phosphor Icons** (regular), 18 sembollük gömülü SVG sprite | `<svg class="ph"><use href="#ph-…"/></svg>` |
| Tipografi | Google Fonts **Roboto** (400–900 değişken) | **Kural: her metin ≥1rem, her ağırlık ≥400** — daisyUI'nin küçük bileşen boyutları (badge .625rem, tablo .6875rem, stat .75rem) özel katmanda eziliyor |
| Favicon | Phosphor "compass" ikonu, data-URI | |
| Yayın | **GitHub Pages** (`main` dalı, kök) | Push'tan ~1–2 dk sonra canlı |
| Derleme | `python3 build.py` | Bağımlılık yok, sadece Python 3 |

**Neden framework yok:** sayfa 10 yıl sonra da açılabilmeli, kullanıcı kod bilmiyor, tek dosya
indirilip çevrimdışı okunabilmeli, CSP kısıtlı ortamlarda (artifact) çalışmalı.

---

## 5. Codebase: nerede ne var

```
/Users/karaca/DEV/pusula/            ← Cursor bunu açar (git remote: karacaismail/pusula)
├─ HANDOFF.md                        ← bu belge
├─ build.py                          ← src/ → v2/index.html birleştirici + yayın öncesi kontroller
├─ index.html                        ← ESKİ ARŞİV (v3.1). Sürüm bandı var. DOKUNMA.
├─ v2/index.html                     ← DONDURULDU (30.08.2026). Referans sürüm; elleme.
├─ v3/index.html                     ← BUILD ÇIKTISI (güncel rapor). ELLE DÜZENLEME.
└─ src/
   ├─ 00-head.html        (751 B)    meta, title, font, favicon, <style> açılışı
   ├─ 10-daisyui.css      (1,1 MB)   VENDOR — sürüm yükseltme dışında dokunma
   ├─ 20-style-sprite.html (16 KB)   özel CSS tokenları + </style> + .wrap + Phosphor sprite
   ├─ 30-body.html        (39 KB)    ★ İÇERİK — işin %95'i burada
   ├─ 40-echarts.js       (1,0 MB)   VENDOR — dokunma
   └─ 50-charts.js        (6 KB)     grafik tanımları (tema duyarlı, yeniden çizim dahil)
```

### Düzenleme akışı
```bash
cd /Users/karaca/DEV/pusula
# 1. içeriği düzenle
$EDITOR src/30-body.html          # kural kutusu ekliyorsan: tools/add_rules.py
# 2. derle + kontrolleri geçir
python3 build.py
# 3. yerelde bak (mobil görünümde de)
python3 -m http.server 8080   # → http://localhost:8080/v3/
# 4. yayınla
git add -A && git commit -m "…" && git push
```

### Diğer kopyalar (senkron tutulacak veya emekliye ayrılacak)
- `/Users/karaca/Downloads/projelerim nelermis claude/pusula-v2-birlesik.html` — elle alınmış yedek,
  artık **eskimiş sayılır**; kanonik olan `v2/index.html`.
- Özel Claude artifact URL'i: `claude.ai/code/artifact/27fdb985-b03a-4bf2-be16-25b14d4206e0`
  (Cursor bunu güncelleyemez; ya emekliye ayır ya da "eski özel kopya" olarak bırak.)

---

## 6. Veriler nereden geldi (kaynak defteri)

### A. Kullanıcı beyanları (en yüksek otorite)
- 19 soruluk gap formu cevapları (29.08.2026)
- 18 maddelik denetim cevapları (29.08.2026 gecesi): borç kırılımı, eş geliri, konaklama, kohort modeli,
  DT outsource kararı, yurtdışı iptali, Zabuno'nun kendisine ait olmaması, AI abonelik gideri
- Yaşam vizyonu metni (Çanakkale, katamaran, miras, kimlik hedefi)

### B. Taranan yerel depolar (salt okunur; hiçbirine yazılmadı)
| Yol | Ne için |
|---|---|
| `/Users/karaca/DEV/destektesvik/` | DestekTeşvik planlama korpusu (184 doküman), MVP kapsamı, kill kriterleri |
| `/Users/karaca/DEV/destek tesvik eski yazilim/` | Arşiv teknik MVP (FastAPI, 260 test) — yapılabilirlik kanıtı |
| `/Users/karaca/DEV/mimari/metaframer-kernel/` | Kernel durum bayrakları, NO-GO kararı |
| `/Users/karaca/DEV/mimari/actionplan/` | WBS sözlüğü (§7), 617 düğüm, 148 satılabilir uygulama |
| `/Users/karaca/DEV/AI First EA (APE-EAP)/` | AEP tasarım sistemi durumu |
| `/Users/karaca/DEV/arsa birlestir/`, GitHub `finalarsa` | arsam metrikleri (99 kanonik metrik), sunum |
| `/Users/karaca/DEV/zabuno/` | *(taranmıştı, sonradan kapsam dışına alındı)* |

### C. Codex'in ürettiği iki belge (birleştirildi)
- `/Users/karaca/Documents/Codex/2026-08-29/projelerim-amac-kapsam-neler-ekonomik-olarak/outputs/yasam-ekonomik-ozgurluk-raporu.html`
  → içeriği v2'ye birleştirildi (kaynaklı kredi kuralları, başabaş, koruma maddeleri, kill gate'ler)
- `…/outputs/problematic.md` → 14 P0 teşhisi; 9'u bayat çıktı, 5'i işlendi, 1'i açık (mahremiyet)

### D. Resmî ve dış kaynaklar (sayfanın dipnotunda linkli)
- BDDK Kurul Kararı 11364 (29.01.2026) — kredi/değer oranı tablosu
- BDDK Basın Açıklaması (30.01.2026) — enerji sınıfı kuralı, kart yapılandırma penceresi
- Ziraat Bankası arsa kredisi (36 ay, ekspertizin %50'si, imar şartı) ve konut kredisi (azami 120 ay)
- KPMG Türkiye Startup Yatırımları 2025
- Kohort eğitim tamamlama oranları: teachable.com, disco.co, group.app
- Türkiye'de ücretsiz e-ticaret eğitimi: BTK Akademi, Ticimax, İSMEK, Tekdev

---

## 7. Sıradaki iş: yol haritasını "girişim başına akordeon + ara teslimler"e çevirmek

Kullanıcının talebi. Bugün yol haritası **kronolojik** (Bu hafta → Eylül → … → 2031). Eksik olan:
**her girişimin kendi derinliği** — akordeon içinde ara teslimler, waterfall fazları, uzun vadeli hedef.

### 7.1 WBS sözlüğü (kullanıcının kendi sistemi — actionplan deposundan; aynen kullan)
```
app (ada) → module (dağ) → archetype (kaya) → feature (taş)
          → component (kum) → work_unit (molekül) → micro_step (atom)
```
Raporda **kaya/taş** seviyesinden aşağı inilmez (rapor bir yönetim aracıdır, iş takip sistemi değil).

### 7.2 Waterfall faz modeli (Scrum/Agile YASAK)
Her ara teslim şu 7 fazdan birine etiketlenir:
`1 Başlatma · 2 Analiz/Gereksinim · 3 Tasarım · 4 İnşa · 5 Doğrulama/Test · 6 Geçiş/Yayın · 7 İşletme/Bakım`

### 7.3 İstenen bileşen (DaisyUI `collapse`)
Yol haritası bölümünün altına, kapsamdaki **4 girişim** için birer akordeon:

```html
<details class="collapse collapse-arrow">
  <summary class="collapse-title">DestekTeşvik — amiral ürün</summary>
  <div class="collapse-content">
    <!-- 1. Kimlik: ne, kime, hangi gelir modeli (tek paragraf) -->
    <!-- 2. Uzun vadeli hedef: 2031'de bu girişim ne olacak -->
    <!-- 3. Ara teslim tablosu (aşağıdaki sütunlar) -->
    <!-- 4. Durdurma kuralı (kill gate) -->
    <!-- 5. Kaynak: haftalık saat + para -->
  </div>
</details>
```

**Ara teslim tablosu sütunları (zorunlu):**
| # | Ara teslim | Faz (1–7) | WBS | Çıktı (kanıt) | Açılış kapısı | Kim | Tarih | Durum |
|---|---|---|---|---|---|---|---|---|

- **Çıktı:** ölçülebilir ve gösterilebilir olmalı (URL, imza, tapu, ekstre satırı, tahsilat kaydı).
- **Kim:** kurucu / dış yüklenici / mali müşavir / avukat / banka / eş — tek kişilik şirkette bile yazılır.
- **Durum:** yalnız üç değer — `bekliyor` · `yürüyor` · `bitti`. ("%80 bitti" yasak.)

### 7.4 Uzun vadeli hedefler (akordeonlarda yazılacak taslak — kullanıcı onaylamalı)
| Girişim | 2027 | 2028–29 | 2030–31 (uzun vade) |
|---|---|---|---|
| **titanlar** | 3 kohort tamamlandı, fiyat bir kez arttı | Kurumsal eğitim kanalı + kişisel marka | Bilinçli olarak ölçeklenmez; nakit + görünürlük hattı |
| **arsam** | Yayın + 20 ödeyen araç kullanıcısı + yatırımcı tanışma | Veri ürünü (değerleme veri seti), ikinci coğrafya | Dikey pazaryeri; hasat adaylarından biri |
| **DestekTeşvik** | MVP + 10 ödeyen | Ölçek, A.Ş., ilk tur ya da güçlü nakit akışı | **Ana değer taşıyıcısı** — hasat olayının birincil adayı |
| **MetaFramer/AEP** | DT veya arsam'ın bir ekranını hızlandırdı | Ölçülebilir zaman tasarrufu kanıtı | Ayrı yatırım yok; iç kaldıraç olarak kalır |
| **Ev/arazi** | İmar + emsal + banka ön onayları | Satış → arazi + daire; inşaat başlar | Çanakkale evi oturulabilir (31.12.2030) |

### 7.5 Kabul kriterleri (bu iş ne zaman bitti sayılır)
- [ ] 4 akordeon var; kapalı hâldeyken sayfa uzunluğu bugünkünden fazla artmıyor
- [ ] Hiçbir ara teslim, SMART karnedeki bir satırı **kelimesi kelimesine tekrar etmiyor**
      (karne = kurumsal hedef; akordeon = o hedefin içindeki adımlar; çakışan varsa karneye işaretçi ver)
- [ ] Scrum/Agile terimi yok (`tools/dupscan.py` bunu da kontrol eder)
- [ ] Mobilde tablolar yatay kaydırma kutusunda, sayfa gövdesi yatay kaymıyor
- [ ] `python3 build.py` tüm kontrolleri geçiyor
- [ ] Koyu ve açık temada okunabilir

---

## 8. Açık işler ve eksikler

### 8.1 Kullanıcıdan tek cevapla kapanacak kararlar
| # | Konu | Seçenekler |
|---|---|---|
| K1 | **Yayın mahremiyeti** (Codex P0-14, hâlâ açık) | (a) böyle kalsın (b) Pages kapansın, rapor özel kalsın (c) kamuya anonim özet + özel tam sürüm |
| K2 | Eski arşiv sayfasındaki **üçüncü kişi adı** | anonimleştir / dokunma |
| K3 | §7.4'teki uzun vadeli hedef taslağı | onayla / düzelt |

### 8.2 Belgeden/kurumdan gelecek eksik veriler (sayfada "Eksik veriler" kutusunda listeli)
konut kredisi faizi ve kalan vadesi · kart akdi faizi + banka taksitlendirme teklifi ·
"15 bin ₺ / 24 ay" yeni kredinin tanımı (aylık mı toplam mı) · devlet dönüşüm kredisinin vadesi/faizi/tapu şerhi ·
SGK sözleşmesinin kapsamı ve tutarı · DT outsource bütçesi ve yüklenici · arsam'ın yayına girecek kod tabanı ·
ev için 3 emsal fiyat + satış vergi/harç/komisyonu · Çardak arazisi imar durumu ve fiyat bandı ·
hane giderinin 30 günlük gerçek ortalaması

### 8.3 Üründe eksik olanlar (Cursor'ın backlog'u — öncelik sırasıyla)
1. **§7'deki akordeon + ara teslim yapısı** (asıl talep)
2. `tools/dupscan.py` — tekrar ve yasak terim tarayıcısı (bugün elle yapılıyor; §9'da tarif var)
3. **Yazdırma/PDF stili** — kullanıcı bunu bankaya/mali müşavire götürecek; bugün print CSS yok
4. **"Son güncelleme" tek damgası** — sayfada tarih birden fazla yerde geçiyor, tek yere indirilmeli
5. Eski `index.html` arşivi için karar: kalsın mı, yoksa `/v2/`'ye yönlendirme mi olsun
6. Grafik verilerinin `src/50-charts.js` içinde sabit kodlanmış olması — tek bir veri nesnesine çekilmeli
   ki içerik ile grafik çelişemesin

### 8.4 "Ne fazla?" (sadeleştirilecekler)
- Risk bölümü 16 kart — 8'i planı bugün gerçekten değiştiriyor, kalanı arka plan. Belki iki katman.
- Vendor dosyalar depoda 2,1 MB — kabul edilebilir ama `git` geçmişi şişiyor; ileride CDN+SRI tartışılabilir
  (dikkat: tek dosya/çevrimdışı kuralını bozar).

---

## 9. Yayın öncesi kontrol listesi

`build.py` şunları otomatik kontrol eder: charset/viewport/noindex/title, tek `<style>`, iki `<script>`,
emoji yok, üçüncü kişi adı yok, kapsam dışı proje adı yok, changelog anlatısı yok.

**Elle (veya yazılacak `tools/dupscan.py` ile):**
```bash
# tekrar taraması — bir anahtar ifade 3'ten fazla geçiyorsa gerekçesi olmalı
python3 - <<'EOF'
import re,html,io
t=io.open("src/30-body.html",encoding="utf-8").read()
t=html.unescape(re.sub(r'<[^>]+>',' ',t)).lower()
for k in ['kohort','yapılandır','outsource','hasat','5.000','sgk','emsal','plan b',
          'sprint','backlog','scrum','agile','story point','velocity','epic','kanban']:
    n=len(re.findall(k,t))
    if n: print(f"{n:3d}×  {k}")
EOF
```
Beklenen: agile terimleri **0**; içerik terimleri makul (bir kavram + karne satırı + grafik etiketi).

**Görsel kontrol:** 375px genişlikte aç, yatay kaydırma olmamalı; koyu ve açık temada oku;
dört grafiğin de çizildiğini gör (konsol hatası olmamalı).

---

## 10. Cursor'a verilecek ilk komut (kopyala-yapıştır)

> `/Users/karaca/DEV/pusula` deposunu aç ve önce `HANDOFF.md` dosyasını baştan sona oku.
> Bu bir karar destek raporudur; kurallar §3'te, teknoloji §4'te, dosya yapısı §5'tedir.
> **Yalnız `src/` altındaki dosyaları düzenle, sonra `python3 build.py` çalıştır** — `v2/index.html`
> elle düzenlenmez, `index.html` (eski arşiv) hiç değiştirilmez.
> İlk iş: §7'deki "girişim başına akordeon + ara teslim tablosu" yapısını `src/30-body.html` içine ekle.
> Waterfall fazları ve WBS sözlüğü §7.1–7.2'de; Scrum/Agile terimleri yasak. Kabul kriterleri §7.5'te.
> Bitirince §9'daki kontrol listesini çalıştır ve sonucu raporla. Yayın (`git push`) için onay iste.

---

## 11. Ne devredilir, ne devredilmez

**Devredilir:** `/Users/karaca/DEV/pusula` deposunun tamamı; içerik düzenleme; akordeon/ara teslim işi;
yazdırma stili; tekrar tarayıcı; grafik veri düzeni; yerelde önizleme.

**Devredilmez (kullanıcı kararı gerekir):**
- Yayın kararı ve mahremiyet (K1/K2) — `git push` yalnız kullanıcı onayıyla
- Girişimlerin kapsamı, öncelik sırası, tarihler ve hedef sayıları — bunlar kullanıcının beyanıdır,
  Cursor bunları "iyileştirmek" için değiştirmez
- Finans/hukuk/sağlık cümlelerinin yumuşatılması veya uzman şartının kaldırılması
- Eski arşiv sayfası (`index.html`)
- Kapsam dışı projelerin (işveren işleri, Zabuno, capclouds) geri eklenmesi

**Asla:** kullanıcının kişisel verisini yeni bir yere kopyalamak, üçüncü kişi adı eklemek,
`noindex` etiketini kaldırmak, izleme kodu eklemek.

---

## 12. Devir sonrası ilk hafta için önerilen sıra

1. `HANDOFF.md` okundu, depo açıldı, `python3 build.py --check` çalıştırıldı → "Fark: YOK" görülmeli
2. `tools/dupscan.py` yazıldı (§9'daki betiği dosyaya çevir) ve boş çıktı doğrulandı
3. §7 akordeon yapısı `src/30-body.html`'e eklendi → yerelde mobil + iki temada bakıldı
4. Kullanıcıya K1/K2/K3 kararları soruldu
5. Onay alındıktan sonra tek commit ile yayın

---

**Son not:** Bu rapor bir tabloyu değil, bir kişinin beş yılını taşıyor. Bir sayıyı değiştirmeden önce
kaynağını sor; bir cümleyi silmeden önce hangi kararı desteklediğini anla. Emin değilsen ekleme —
sayfanın en büyük düşmanı, bu projenin ilk dokuz turunda olduğu gibi, **tekrar ve gürültüdür**.
