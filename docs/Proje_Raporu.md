# AtölyeŞef Kurulum Sonrası Proje Raporu

Bu rapor, **AtölyeŞef (Atölye ve Laboratuvar Ekipman Takip Sistemi)** projesinin iskelet kurulumunun ve yapılan testlerin sonuçlarını içerir.

---

## Gerçekleştirilen İşlemler
1. **Dizin ve Dosya Yapısı:** Belirtilen iskelet yapısı birebir oluşturuldu.
2. **Sanal Ortam ve Bağımlılıklar:**
   - Python sanal ortamı (`venv`) kuruldu.
   - Sadece ders için istenen kütüphaneler `requirements.txt` üzerinden sanal ortama yüklendi.
3. **Güvenlik Önlemleri:** `.env` dosyası oluşturuldu ve `.gitignore` dosyası aracılığıyla sürüm kontrol sisteminden (Git) başarıyla gizlendi.
4. **Veritabanı ve Konfigürasyon:** SQLite veritabanı bağlantısı `config.py` içinde `.env`'den beslenecek şekilde dinamik hale getirildi.
5. **Modern Tasarım Entegrasyonu:** `app/static/css/style.css` ve `app/templates/base.html` dosyalarıyla modern koyu tema tasarımı yapıldı.

---

## Test Doğrulama Raporu

Projenin hatasız çalıştığını doğrulamak amacıyla `tests/test_basics.py` modülü altında birim testleri koşturulmuştur.

### Koşturulan Komut
```bash
python -m unittest tests/test_basics.py
```

### Test Sonuçları
```text
....
----------------------------------------------------------------------
Ran 4 tests in 0.144s

OK
```

### Doğrulanan Test Durumları:
- **test_app_exists**: Flask uygulama nesnesinin başarıyla oluşturulduğunu doğrular.
- **test_app_is_testing**: Test modunda uygulamanın doğru konfigürasyonla çalıştığını doğrular.
- **test_index_page**: Anasayfaya yapılan isteğin `200 OK` döndürdüğünü ve modern arayüz başlığının (AtölyeŞef) sayfada yer aldığını doğrular.
- **test_login_page**: Giriş yap sayfasına yapılan isteğin `200 OK` döndürdüğünü ve giriş formunun başarıyla render edildiğini doğrular.
