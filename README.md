# 🛠️ AtölyeŞef: Atölye ve Laboratuvar Ekipman Takip Sistemi

![CI](https://github.com/alikaya06659/ATOLYESEF/actions/workflows/ci.yml/badge.svg)

**AtölyeŞef**, Meslek Yüksek Okulu İnternet Programcılığı dersi kapsamında modern web geliştirme standartlarına uygun olarak tasarlanmış, **Flask 3.x** tabanlı bir atölye ve laboratuvar ekipman/zimmet takip sistemidir.

---

## ✨ Öne Çıkan Özellikler

- 🌐 **Flask 3.x Standartları:** Modern Flask mimarisi ve bileşenleri.
- 📦 **Application Factory Pattern:** Modüler, kolay test edilebilir ve genişletilebilir uygulama yapısı.
- 🧩 **Blueprint Mimarisi:** Uygulamanın anasayfa (`main`) ve kimlik doğrulama (`auth`) bölümlerine temiz bir şekilde ayrılması.
- 🎨 **Premium Arayüz Deneyimi:** Google Fonts (Outfit) tabanlı, modern animasyonlu ve degrade geçişli estetik koyu tema (dark mode) tasarımı, Bootstrap 5 bileşenleri.
- 🔐 **Kullanıcı Kimlik Doğrulama (Auth):** Flask‑Login, Flask‑WTF ve CSRF korumalı formlarla tam güvenli kayıt, giriş ve çıkış akışı.
- 👤 **Profil ve Avatar Yönetimi:** Kullanıcıların bilgilerini güncelleyebileceği, güvenli (secure_filename) avatar yükleme destekli kişisel profil sayfası.
- 📦 **Rezervasyon Takibi:** Ekipmanların "Ödünç Al" ve "İade Et" işlemleriyle takip edildiği, geçmiş işlemleri barındıran yetki kontrollü rezervasyon akışı.
- 🚨 **Özel Hata Yönetimi:** Bootstrap 5 tasarımlı 404 (Sayfa Bulunamadı) ve 500 (Sunucu Hatası) sayfalarıyla kullanıcı dostu hata yönlendirmesi.
- 🔌 **RESTful API Desteği:** Dış sistemlerin veritabanındaki ekipmanlara JSON formatında erişebilmesi için oluşturulmuş özel API katmanı.
- 🛡️ **Güvenlik Politikası:** Çevre değişkenlerinin (`.env`) ve yerel veritabanlarının sürüm kontrol sisteminde (Git) güvenle yoksayılması, parola hash'leme.
- 🧪 **Kapsamlı Test Altyapısı:** Uygulama modülleri, konfigürasyonu ve temel route erişimlerini doğrulayan entegre birim testleri.

---

## 📦 Ekipman ve Rezervasyon Özellikleri

- **Listeleme**: `/equipments` rotası, ekipmanları Bootstrap 5 tablosu ile listeler.
- **Sayfalama**: Sayfa başına 10 kayıt gösterimi (SQLAlchemy 2.x `db.paginate` kullanılarak).
- **Arama**: Üst kısımdaki arama çubuğu ile `name`, `code` ve `laboratory` alanlarında filtreleme (SQLAlchemy `ilike` kullanımı).
- **Ekleme/Düzenleme/Silme**: Flask-WTF tabanlı formlar ve CSRF korumalı silme işlemleri.
- **Ödünç Alma**: "Mevcut" durumdaki ekipmanlar için `POST /equipment/<int:id>/borrow` kullanılarak otomatik rezervasyon kaydı oluşturulur.
- **İade Etme**: Sadece işlemi yapan kullanıcı tarafından, profil ekranı üzerinden `POST /reservation/<int:id>/return` ile gerçekleştirilen ve ekipmanı tekrar "Mevcut" duruma çeken yetki kontrollü işleyiş.

---

## 🔌 API Kullanımı

Sistemdeki güncel ekipman durumlarını dışarıdan çekmek için aşağıdaki uç noktayı (endpoint) kullanabilirsiniz:

- **Endpoint:** `GET /api/v1/equipments`
- **Yanıt Tipi:** `application/json`
- **Açıklama:** Veritabanında kayıtlı tüm ekipmanların id, name, code, laboratory ve status bilgilerini içeren serileştirilmiş bir JSON dizisi döndürür. Türkçe karakter desteği (UTF-8) mevcuttur.

---

## 🚀 Teknolojik Altyapı

Projede yalnızca modern standartlara uygun kütüphaneler kullanılmıştır:

- **Core:** Python 3.11+ & Flask 3.x
- **Veritabanı ve ORM:** Flask‑SQLAlchemy (SQLAlchemy 2.x stili)
- **Veritabanı Göçleri:** Flask‑Migrate (Alembic tabanlı)
- **Kullanıcı Yönetimi:** Flask‑Login
- **Form Yönetimi:** Flask‑WTF (CSRF korumalı formlar)
- **Doğrulamalar:** email-validator
- **Çevre Değişkenleri:** python-dotenv

---

## 📁 Proje Dizin Yapısı

```text
atölyeşef/
├── app/
│   ├── __init__.py          # Application Factory & Extension Başlatıcı
│   ├── models.py            # Veritabanı Modelleri (User, Equipment vb.)
│   ├── main/
│   │   ├── __init__.py      # Main Blueprint Tanımı
│   │   ├── routes.py        # Anasayfa ve Ekipman CRUD Route'ları
│   │   └── forms.py         # Ekipman Formu
│   ├── auth/
│   │   ├── __init__.py      # Auth Blueprint Tanımı
│   │   ├── routes.py        # Giriş/Çıkış ve Profil İşlemleri
│   │   └── forms.py         # Register ve Login Formları
│   ├── templates/           # Premium HTML Şablonları (Bootstrap 5)
│   │   ├── auth/            # Giriş, Kayıt, Profil şablonları
│   │   ├── base.html        # Temel Layout ve Navbar
│   │   └── equipment_*.html # Ekipman listesi ve formları
│   └── static/              # CSS & Görseller
├── docs/                    # Geliştirme Raporları ve Planlar
│   ├── Uygulama_Plani.md    # Teknik Mimari Tasarım Planı
│   ├── Proje_Raporu.md      # Rapor ve Özellik Özeti
│   └── AI_Gunlugu.md        # AI Geliştirme Günlüğü
├── tests/                   # Birim Testleri
│   └── test_basics.py       # Temel Uygulama Testleri
├── config.py                # Dinamik Konfigürasyon
├── requirements.txt         # Paket Bağımlılıkları
├── .env.example             # Örnek Çevre Değişkenleri
├── .gitignore               # Sürüm Kontrolünde Yoksayılacak Dosyalar
└── run.py                   # Uygulama Giriş Noktası
```

---

## 🛠️ Kurulum ve Çalıştırma

Projenizi yerel bilgisayarınızda çalıştırmak için aşağıdaki adımları uygulayın:

1. **Sanal Ortamı Etkinleştirin**
   ```powershell
   # PowerShell için:
   .\venv\Scripts\Activate.ps1
   # Klasik CMD için:
   .\venv\Scripts\activate.bat
   ```

2. **Bağımlılıkları Yükleyin**
   ```bash
   pip install -r requirements.txt
   ```

3. **Veritabanını Hazırlayın**
   ```bash
   flask db upgrade
   ```

4. **Uygulamayı Başlatın**
   ```bash
   python run.py
   ```
   Tarayıcınızdan **`http://127.0.0.1:5000`** adresine giderek sistemi görebilirsiniz.

---

## 🧪 Testlerin Koşturulması

Birim testlerini çalıştırmak için sanal ortamınız aktifken terminalde şu komutu yürütün:
```bash
python -m unittest discover -s tests
```

---

## 📄 Proje Geliştirme Günlükleri ve AI Raporları

Projenin planlama, tasarım ve entegrasyon safhalarına ait teknik belgelere `docs/` klasöründen erişebilirsiniz:

1. 📋 **[Uygulama Planı](docs/Uygulama_Plani.md):** Teknik mimari planı.
2. 📊 **[Proje Raporu](docs/Proje_Raporu.md):** Test doğrulama çıktıları ve iş özeti.
3. 📓 **[AI Geliştirme Günlüğü](docs/AI_Gunlugu.md):** Yapay Zeka ile gerçekleştirilen geliştirme süreçlerinin kaydı.

---

*Bu proje İnternet Programcılığı Dersi için geliştirilmiştir. Tüm Hakları Saklıdır © 2026.*