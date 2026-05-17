# İlaç Veri Setleri Arasında Kayıt Eşleştirme

Bu projede TİTCK ve ATC veri setleri arasında benzerlik tabanlı kayıt eşleştirme işlemi gerçekleştirilmiştir.

Veri setlerinde ortak bir ID alanı bulunmadığı için eşleştirme işlemleri ilaç adı, etkin madde ve firma bilgileri kullanılarak yapılmıştır.

Proje kapsamında veri temizleme, metin normalizasyonu ve fuzzy matching yöntemleri kullanılmıştır.

---

## Kullanılan Teknolojiler

- Python
- Pandas
- RapidFuzz
- Unidecode

---

## Veri Ön İşleme

Eşleştirme işlemi öncesinde veri temizleme uygulanmıştır.

Yapılan işlemler:

- Küçük harfe dönüştürme
- Türkçe karakter normalizasyonu
- Özel karakter temizleme
- Fazla boşlukları kaldırma
- Eksik veri kontrolü

Bu işlemler veri setleri arasındaki yazım farklılıklarının etkisini azaltmak için uygulanmıştır.

---

## Eşleştirme Yöntemi

Kayıt eşleştirme işlemi fuzzy matching yaklaşımı ile gerçekleştirilmiştir.

Karşılaştırma sırasında:

- İlaç adı
- Etkin madde
- Firma bilgisi

alanları birlikte değerlendirilmiştir.

Benzerlik hesaplaması için RapidFuzz kütüphanesindeki aşağıdaki yöntem kullanılmıştır:

```python
fuzz.token_sort_ratio
```

Her kayıt için ATC veri setindeki en uygun eşleşme bulunmuş ve benzerlik puanı hesaplanmıştır.

---

## Çıktı

Program çalıştırıldığında `eslesmis_ilaclar.csv` dosyası oluşturulur.

Çıktı dosyasında aşağıdaki alanlar bulunmaktadır:

- TITCK_ID
- TITCK_Ilac_Adi
- ATC_Barkod
- ATC_Kodu
- ATC_Durumu
- Match_Score
