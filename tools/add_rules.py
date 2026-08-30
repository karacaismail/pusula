#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kural kutularina iki icon-only buton (Neden? / Uymazsam ne olur?) ekler.
Kural: her hukum icin hem 'cunku' gerekcesi hem 'eger' sonucu bulunur;
iki balon ayni seyi tekrar etmez (birincisi sebep, ikincisi sonuc)."""
import io
import sys

SRC = "src/30-body.html"

IDX = [0]

def _wrap(why_html, risk_html):
    IDX[0] += 1
    i = IDX[0]
    return (
        '\n      <div class="rules">\n'
        '        <div class="rule-btns">\n'
        f'          <button type="button" class="rule-btn rule-btn-why" aria-expanded="false" aria-controls="why{i}" aria-label="Neden?" title="Neden?"><svg class="ph" aria-hidden="true"><use href="#ph-question"/></svg></button>\n'
        f'          <button type="button" class="rule-btn rule-btn-risk" aria-expanded="false" aria-controls="risk{i}" aria-label="Uymazsam ne olur?" title="Uymazsam ne olur?"><svg class="ph" aria-hidden="true"><use href="#ph-warning-diamond"/></svg></button>\n'
        '        </div>\n'
        f'        <div class="rule-pop-body rule-pop-why" id="why{i}" hidden><h4>Neden?</h4>{why_html}</div>\n'
        f'        <div class="rule-pop-body rule-pop-risk" id="risk{i}" hidden><h4>Uymazsam ne olur?</h4>{risk_html}</div>\n'
        '      </div>'
    )


def block(why_lead, whys, risk_lead, risks):
    def ul(items):
        return "".join(f"<li>{x}</li>" for x in items)
    return _wrap(f"<p>{why_lead}</p><ul>{ul(whys)}</ul>", f"<p>{risk_lead}</p><ul>{ul(risks)}</ul>")


def multi(pairs_why, pairs_risk):
    """Cok maddeli kutu: her kural icin ayri 'cunku' ve 'eger' bloklari."""
    def sect(items):
        out = ""
        for lead, bullets in items:
            out += f"<p>{lead}</p><ul>" + "".join(f"<li>{b}</li>" for b in bullets) + "</ul>"
        return out
    return _wrap(sect(pairs_why), sect(pairs_risk))


# (essiz capa metni, eklenecek blok)
INSERTS = [
    # 1 — Bu hafta
    ("<em>Kapı: başvurular yapıldı + sayfa canlı.</em></p>",
     block(
        "Kart yükü bu hafta indirilecek ve gider kısılacak, çünkü:",
        ["Kredi kartı, portföydeki en pahalı borç türüdür; bakiyesi en küçük, aylık maliyeti en büyüktür.",
         "92 bin ₺'lik asgari ödeme, aylık açığın tek başına yarısından fazlasını üretiyor.",
         "Gelir artışı ay alır; gider ve borç servisi bugün değiştirilebilen tek kalemdir.",
         "Ön kayıt sayfası, gelir merdiveninin ilk basamağı — açılmadan hiçbir tahsilat başlayamaz."],
        "Eğer başvuru bu hafta yapılmaz ve gider kısılmazsa:",
        ["Birikim Ekim içinde tükenir; açık kart limitinden döndürülmeye başlar.",
         "Aynı borcun kapanma tarihi 2027 sonundan öteye kayar.",
         "Ekim'deki fon kapısı karşılıksız kalır; outsource ödemesi başlatılamaz.",
         "Takvimin tamamı bir çeyrek geriye kayar ve kanıt penceresi daralır."])),

    # 2 — Eylül
    ("outsource şartnamesi (Durum tablosundaki MVP tanımı) + 3 yükleniciden teklif · arsam kutusu: haftada sabit 8 saat.</p>",
     multi(
        [("arsam'a haftada sabit 8 saat ayrılacak, çünkü:",
          ["Kutu tanımlanmazsa \"paralelde vakit harcamadan\" cümlesi kendini yalanlar.",
           "arsam, kohort ve DestekTeşvik aynı haftadan besleniyor; sabit kutu üçünü de öngörülebilir kılar.",
           "Aralık yayını, değişken değil sabit bir hızla planlanabilir."]),
         ("Marka kararı 30 Eylül'e kadar verilecek, çünkü:",
          ["İsim estetik değil operasyon meselesidir; yanlış yazılan isim her tanıtımda maliyet üretir.",
           "Ölçüt yazılmadığı için karar aylardır sürünüyor; telefon testi bu işi bir saate indirir.",
           "Domain alımı ve outsource şartnamesi bu karara bağlı."]),
         ("Sağlık ücretsiz yoldan başlatılacak, çünkü:",
          ["Aile hekimi ve KETEM taramaları maliyet engelini ortadan kaldırıyor.",
           "40'lı yaşlarda erken bulgu, sonraki yirmi yılın çalışma kapasitesini belirler.",
           "Planın tamamı tek kişinin çalışabilmesine bağlı; bu, en ucuz sigortadır."])],
        [("Eğer arsam kutusu aşılırsa:",
          ["DestekTeşvik hazırlığı ve kohort saatleri erir.",
           "Aralık yayını yine kaçar; iki iş birden gecikir."]),
         ("Eğer marka kararı Eylül'ü geçerse:",
          ["Şartname ve domain bekler; 60 günlük inşa penceresi Aralık'a sığmaz.",
           "Yüklenici sözleşmesi ekim ayında imzalanamaz."]),
         ("Eğer sağlık adımı ertelenirse:",
          ["Hiçbir sinyal ölçülmez; en ucuz erken uyarı kaçırılır.",
           "Ertelenen randevu pratikte yılı devirir."])])),

    # 3 — Ekim
    ("SGK sözleşme görüşmesi: kapsam + karşılık + fikri mülkiyet yazılı — 30 Kasım'a kadar imza ya da yazılı vazgeçme.</p>",
     multi(
        [("Kohort ≥12 ödeme olmadan başlatılmayacak, çünkü:",
          ["Ön ödeme, ilginin gerçek olduğunun tek kanıtıdır; niyet beyanı gelir üretmez.",
           "12 kişinin altında hem dönem geliri hem grup dinamiği kurulamaz.",
           "Hazırlık saati katılımcı sayısından bağımsızdır; düşük doluluk saat başına geliri düşürür."]),
         ("Birebir yol haritası oturumu kohort başına 6 kişiyle sınırlı, çünkü:",
          ["Yirmi kişiye verilen taahhüt otuz saatlik bedava danışmanlık demektir.",
           "Bu oturum, satılabilir danışmanlığın ücretsiz sürümüdür; sınırsız verilirse ürünü değersizleştirir.",
           "Kurucunun ürün geliştirmeye ayırdığı zaman kontrolsüz biçimde tükenir."]),
         ("Outsource ödemesi fon kapısından önce başlamayacak, çünkü:",
          ["Dış geliştirme sabit maliyet, kohort geliri ise henüz belirsizdir.",
           "Kart yapılandırması sonuçlanmadan aylık taksit yükü bilinemez.",
           "Ödeme kaynağı yazılmadan verilen sipariş, nakit açığını büyütür."])],
        [("Eğer kohort 12 dolmadan başlatılırsa:",
          ["Dönem geliri hedefin yarısında kalır; hazırlık yükü aynı kalır.",
           "Model yanlış görünür ve doğru olan fiyat düşürülerek bozulur."]),
         ("Eğer birebir taahhüt sınırsız verilirse:",
          ["Takvim dış taleplerle dolar; DestekTeşvik kabul testleri ve arsam kutusu ezilir.",
           "Hizmet ölçeklenemez hale gelir; ikinci kohort açılamaz."]),
         ("Eğer fon kapısı atlanır ve ödeme erken başlarsa:",
          ["Birikim yüklenici avansına gider; ay ortasında nakit biter.",
           "Sözleşme yarıda kalırsa hem ödenen para hem 60 günlük pencere kaybedilir."])])),

    # 4 — Kasım–Aralık
    ("Aralık sonu gelir ara hedefi: ≥3.500 $.</p>",
     multi(
        [("arsam kapsamı yayına kadar donuk kalacak, çünkü:",
          ["Kalan iş yeni özellik değil, yayına çıkarma işidir (kayıt, ilan, arama, moderasyon, hukuki metinler).",
           "Her yeni özellik yayın tarihini belirsiz süre öteler.",
           "Donuk kapsam, hem yüklenici hem kendinle yapılan sözleşmenin tek ölçüsüdür."]),
         ("Kasım ortasında hazır değilse kapsam daralır, tarih kaymaz, çünkü:",
          ["Kapsam daraltmak takvim kaydırmaktan her zaman ucuzdur.",
           "Tek ilde doygunluk, ülke genelinde yüzde birlik kapsamadan güçlüdür.",
           "Yayın tarihi kayarsa 2027'deki kanıt penceresi de kayar."]),
         ("DestekTeşvik kabul testi haftalık yapılacak, çünkü:",
          ["Dışarıya yaptırılan işte kalite ancak düzenli kabulle tutulur.",
           "Altmışıncı günde ilk kez bakmak, hatayı en pahalı anda bulmaktır."])],
        [("Eğer kapsama yeni özellik eklenirse:",
          ["Aralık yayını kaçar ve kohort teslimiyle çakışır.",
           "Üç iş birden yarım kalır; hiçbirinde kapı geçilmez."]),
         ("Eğer kill gate uygulanmaz ve tarih kaydırılırsa:",
          ["arsam'ın ilk kullanıcı verisi 2027'ye kayar.",
           "Yatırımcı tanışması bir yıl öteler; kanıt paketi kurulamaz."]),
         ("Eğer kabul testleri atlanırsa:",
          ["Teslim edilen MVP kabul kriterlerini karşılamayabilir.",
           "Düzeltme maliyeti ve gecikme yükleniciye değil sana kalır."])])),

    # 5 — Ocak–Haziran 2027
    ("İkinci çocuk bu yıl — tempo planı buna göre.</p>",
     multi(
        [("Dokuz ayda ödeyen çıkmazsa müşteri tarafı değişecek, çünkü:",
          ["Sınırsız deneme, yanlış müşteri segmentinde yılları tüketir.",
           "Danışman tarafı bu işi bugün zaten ücret karşılığı yapıyor; ödeme alışkanlığı orada kurulu.",
           "Kural önceden yazılmazsa, karar anında duygusal olarak ertelenir."]),
         ("On ödeme kapı sayısıdır, PMF hükmü değildir, çünkü:",
          ["Ödeme ilk temasın kanıtıdır; değerin kanıtı tekrar kullanımdır.",
           "Kayıp oranı görülmeden yapılan ölçek yatırımı yanlış yere gider."]),
         ("Gelir eşiği üç ay üst üste ölçülecek, çünkü:",
          ["Tek iyi ay mevsimsel ya da tek müşteriye bağlı olabilir.",
           "Maaştan bağımsızlaşmanın eşiği süreklilik, zirve değildir."])],
        [("Eğer dokuz ay dolar ve pivot yapılmazsa:",
          ["2028 ev olayı fonsuz karşılanır.",
           "Ürün hem zaman hem kendine olan güven kaybeder; sonraki karar daha da gecikir."]),
         ("Eğer on ödeme PMF sayılır ve ölçeğe geçilirse:",
          ["Kayıp oranı ölçülmemiş bir ürüne pazarlama harcaması yapılır.",
           "Harcanan para geri gelmez; asıl sorun geç fark edilir."]),
         ("Eğer eşik tutmadan bir sonraki basamak açılırsa:",
          ["Aile bütçesi ürün riskini taşımaya başlar.",
           "İlk kötü ayda duracak olan proje değil hanedir."])])),

    # 6 — 2027 H2 → Şubat 2028
    ("para yetmezse önce arazi, daire ertelenir</em>.</p>",
     multi(
        [("Yazılı banka ön onayı olmadan alım taahhüdüne girilmeyecek, çünkü:",
          ["Kredi tutarı satış fiyatına değil, ekspertiz değerine ve enerji sınıfına bağlı hesaplanır.",
           "Sözlü \"olur\" hiçbir bankada bağlayıcı değildir.",
           "Eski binada ekspertiz, fiyatın belirgin altında çıkabilir."]),
         ("Para yetmezse önce arazi alınacak, çünkü:",
          ["Arazi, Çanakkale evinin ön koşulu — yani yaşam planının parçası; daire ise ertelenebilir bir yatırımdır.",
           "Arsa kredisi kısa vadeli ve düşük oranlıdır; öz kaynak ihtiyacı daha katıdır.",
           "Hanede konut sahipliği doğduğunda sonraki konut kredisinin oranı düşer."])],
        [("Eğer ön onaysız kapora verilirse:",
          ["Kredi çıkmazsa kapora kaybedilir.",
           "Satıştan kalan tutar planlanandan az kalır; iki varlık birden alınamaz."]),
         ("Eğer sıra bozulup önce daire alınırsa:",
          ["Arazi bütçesi erir ve ev projesi başlayamaz.",
           "Mevcut konut sahipliği yüzünden arazi tarafında kredi koşulları sertleşir."])])),

    # 7 — 2028–2029
    ("<em>kapı: 4. yılda dağıtılabilir kâr yoksa hedef hisse satışından nakit akışına döner</em>.</p>",
     multi(
        [("İnşaat gelirin üzerine binerse kaba inşaatta durulacak, çünkü:",
          ["Yarım ev korunabilir bir varlıktır; borçlu ev aylık nakdi rehin alır.",
           "İnşaat maliyeti enflasyonla oynar, gelir aynı hızda artmayabilir.",
           "Kaba inşaat, ileride kaldığı yerden sürdürülebilir."]),
         ("Dördüncü yılda dağıtılabilir kâr yoksa hedef nakit akışına dönecek, çünkü:",
          ["Hisse değeri kâğıt üstündedir; hane harcaması için kullanılabilir nakit değildir.",
           "Dört yılda kâr üretmeyen şirket, satılabilir şirket varsayımını da doğrulamaz.",
           "Hedefi zamanında revize etmek, beşinci yılda çakılmaktan ucuzdur."])],
        [("Eğer inşaat durdurulmaz ve sürdürülürse:",
          ["Kredi taksiti, inşaat ödemesi ve hane gideri üst üste gelir.",
           "Ev bitmeden nakit biter; yarım ev bu kez borçla birlikte kalır."]),
         ("Eğer kâr yokken hedef revize edilmezse:",
          ["2031'de gelmeyecek bir hasat beklenir.",
           "Plan B geç devreye girer; ev, miras ve tekne planı topluca kayar."])])),

    # 8 — 2030–2031
    ("sağlık ve aile bedel ödüyorsa finansal hedef gecikir — bu ikisi gecikmez.</em></p>",
     multi(
        [("Hasat gelmezse Plan B uygulanacak, çünkü:",
          ["Bahsin bilinen riski önceden yazılmazsa, başarısızlık hissi doğru kararın önüne geçer.",
           "Ufku uzatmak, aceleyle satmaktan veya borçlanmaktan daha az kayıp verir.",
           "Elde kalan varlıklar (ev, arazi, iki gelirli ürün) korunmaya değer bir sonuçtur."]),
         ("Sağlık ve aile hiçbir koşulda geciktirilmeyecek, çünkü:",
          ["Bu iki kalemdeki kayıp geri alınamaz; finansal hedef ertelenebilir.",
           "Çocukların büyüme dönemi ve kendi fiziksel kapasiten tek seferliktir."])],
        [("Eğer hasat gelmez ve Plan B uygulanmazsa:",
          ["Hedefe yetişmek için risk alınır: acele satış, ek borç, aşırı tempo.",
           "Elde olan varlıklar da tehlikeye girer."]),
         ("Eğer takvim sağlık ve aile pahasına korunursa:",
          ["Kazanılan yıl, sağlık ve ilişki maliyetiyle geri ödenir.",
           "Planın taşıyıcısı yıpranır; hiçbir hedef sahipsiz yürümez."])])),

    # 9 — Yapılmayacaklar
    ("gece çalışmak (uyku, iyi kararların hammaddesi) · haftada bir ekransız eş saatini atlamak.</p>",
     multi(
        [("DestekTeşvik'e kendin kod yazmayacaksın, çünkü:",
          ["Rolün kapsamı belirlemek ve kabul etmek; inşa yetkilendirilmiş yüklenicidedir.",
           "Kendi yazdığın işi kendin kabul edemezsin; bağımsız doğrulama kaybolur.",
           "Aynı saat, gelir üreten kohort ve arsam yayınından çalınır."]),
         ("arsam kutusunu aşmayacaksın, çünkü:",
          ["Kutu, üç işi aynı haftaya sığdıran tek mekanizmadır."]),
         ("Birebir oturum taahhüdünü sınırsız vermeyeceksin, çünkü:",
          ["Ücretsiz verilen danışmanlık, satılan danışmanlığın fiyatını düşürür."]),
         ("Kanıt paketi olmadan yatırımcıyla tur konuşmayacaksın, çünkü:",
          ["Erken açılan görüşme, kanıt geldiğinde ikinci kez açmayı zorlaştırır."]),
         ("Maaşı bırakmayacaksın, çünkü:",
          ["Esnek ve uzaktan maaş bugün planın taşıyıcısı; riski karşılayan tek sabit gelirdir."]),
         ("Devlet kredisini erken kapatmayacaksın, çünkü:",
          ["Portföydeki en ucuz ve en uzun vadeli borçtur; erken kapatmak pahalı fırsatı kaçırmaktır."]),
         ("2027 ikinci çeyreğinden önce yeni fikir veya depo açmayacaksın, çünkü:",
          ["Altmıştan fazla depo, dağılmanın maliyetinin zaten ödendiğini gösteriyor."]),
         ("Gece çalışmayacaksın, çünkü:",
          ["Uyku, karar kalitesinin hammaddesidir.",
           "Gece çalışması ertesi günün dikkatini ve üretkenliğini düşürür.",
           "Düzenli uyku, uzun vadeli çalışma kapasitesini korur."]),
         ("Haftalık ekransız eş saatini atlamayacaksın, çünkü:",
          ["Girişim, iki bebek ve inşaat aynı beş yıla sıkışıyor; ortak karar bu saatte kuruluyor."])],
        [("Eğer kendin kod yazarsan:",
          ["Üretilen iş bağımsız kabulden geçmiş sayılamaz.",
           "Kohort ve arsam teslimleri gecikir; 60 günlük pencere ikinci kez kurulamaz."]),
         ("Eğer arsam kutusunu aşarsan:",
          ["DestekTeşvik hazırlığı durur; iki teslim birden kayar."]),
         ("Eğer sınırsız birebir taahhüt verirsen:",
          ["Takvim dış taleple dolar; ikinci kohort açılamaz ve gelir tavan yapar."]),
         ("Eğer kanıtsız yatırımcı görüşmesi açarsan:",
          ["\"Erken ve hazırlıksız\" izlenimi kalır; sonraki görüşmede aynı kapı daha zor açılır."]),
         ("Eğer maaşı bırakırsan:",
          ["Hane, ürün riskini doğrudan taşımaya başlar; ilk kötü ayda plan durur."]),
         ("Eğer devlet kredisini erken kapatırsan:",
          ["Arazi ve daire için gereken öz kaynak azalır; ucuz borç yerine pahalı fırsat kaybedilir."]),
         ("Eğer yeni fikir veya depo açarsan:",
          ["Üç aktif iş dörde çıkar; dördü de yavaşlar ve hiçbirinde kapı geçilmez."]),
         ("Eğer gece çalışırsan:",
          ["Ertesi gün karar kaliten düşer; hata ve yanlış önceliklendirme ihtimali artar.",
           "Kazanılan birkaç saat, sonraki günün verim kaybıyla geri alınır.",
           "Tekrarlanırsa sürdürülebilir çalışma düzeni bozulur."]),
         ("Eğer eş saatini atlarsan:",
          ["Kararlar tek başına alınmaya başlar; en pahalı senaryo sessizce büyür."])])),

    # 10 — Ritim
    ("risk kartlarında sinyal taraması.</p>",
     multi(
        [("Üç randevu takvime yazılacak, çünkü:",
          ["Ne zaman güncelleneceği yazılı olmayan plan altı ay içinde ölür.",
           "Haftalık ritim işi küçük tutar, aylık ritim sayıyı denetler, çeyreklik ritim yönü sorgular."]),
         ("Haftaya en fazla üç madde yazılacak, çünkü:",
          ["Dördüncü madde diğer üçünü de yarım bırakır.",
           "Haftalık kapasite 58 saat tavanında ve ikinci çocukla azalacak."]),
         ("Büyük kararlar eşle birlikte alınacak, çünkü:",
          ["Taşınma, tekne ve miras iki kişinin hayatını aynı anda değiştirir."])],
        [("Eğer randevular takvime yazılmazsa:",
          ["Rapor okunmaz hale gelir; aynı tartışma birkaç ay sonra tekrar açılır.",
           "İlerleme ölçülemez; kapılar kendiliğinden geçilmiş sayılır."]),
         ("Eğer haftaya üçten fazla madde yazılırsa:",
          ["Hiçbirinde kapı geçilmez; ilerleme hissi üretilir ama kanıt üretilmez."]),
         ("Eğer kararlar tek başına alınırsa:",
          ["Ortak sahiplenme kaybolur; uygulama aşamasında direnç ve gecikme çıkar."])])),

    # 11 — Ev hesabi sinir kurali (%40)
    ("aşarsa daire ertelenir, arazi önceliklidir.</p>",
     block(
        "Taksitler ve kira toplamı aylık gelirin %40'ını aşmayacak, çünkü:",
        ["Gelir henüz hedefte değil; bugünkü seviye 2.730 dolar ve dalgalı.",
         "Sabit yükün payı büyüdükçe tek kötü ay hane bütçesini kilitler.",
         "Bankalar da başvuruda benzer bir orana bakar; aşan dosya zaten reddedilir.",
         "İki ayrı kredi (arazi ve daire) aynı anda taşınacaksa tampon şart."],
        "Eğer %40 sınırı aşılırsa:",
        ["Gelir dalgalandığında taksit ödenemez; gecikme kredi notunu düşürür.",
         "Sonraki kredi pahalanır veya hiç verilmez; Çanakkale ev projesi finanse edilemez.",
         "Acil fon taksite gider; koruma katmanı sıfırlanır.",
         "Sıra bozulur: ertelenmesi gereken daire alınmış, arazi bütçesiz kalmış olur."])),
]


def main():
    h = io.open(SRC, encoding="utf-8").read()
    missing = []
    for anchor, blk in INSERTS:
        if h.count(anchor) != 1:
            missing.append(f"{h.count(anchor)}× {anchor[:60]}")
            continue
        h = h.replace(anchor, anchor + blk, 1)
    if missing:
        print("BULUNAMADI / COKLU:")
        for m in missing:
            print("  -", m)
        sys.exit(1)
    io.open(SRC, "w", encoding="utf-8").write(h)
    print(f"OK — {len(INSERTS)} kural kutusuna iki ikon eklendi")


if __name__ == "__main__":
    main()
