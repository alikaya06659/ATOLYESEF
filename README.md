# 🛠️ AtölyeŞef: Atölye ve Laboratuvar Ekipman Takip Sistemi

![CI](https://github.com/alikaya06659/ATOLYESEF/actions/workflows/ci.yml/badge.svg)

**AtölyeŞef**, Flask 3.x ve SQLAlchemy 2.x ile geliştirilmiş, modern web standartlarına uygun bir ekipman/zimmet takibi uygulamasıdır.

## ✨ Öne Çıkan Özellikler
- Flask 3.x, Application Factory, Blueprint Mimarisi
- Premium UI – Google Fonts (Outfit), dark‑mode, Bootstrap 5
- **Kullanıcı Kimlik Doğrulama (Auth)**: Flask‑Login, Flask‑WTF, CSRF koruması, güvenli kayıt/giriş/çıkış akışı
- **Profil Sayfası**: `/auth/profile` – oturum açmış kullanıcılar için
- Güvenlik – parola hash’leme, benzersiz kullanıcı adı/e‑posta kontrolleri
- Kapsamlı test altyapısı ve AI geliştirme günlükleri

## 📄 Dokümantasyon
- **Uygulama Planı**: `docs/Uygulama_Plani.md`
- **Proje Raporu**: `docs/Proje_Raporu.md`
- **AI Geliştirme Günlüğü**: `docs/AI_Gunlugu.md`

*Bu proje İnternet Programcılığı dersi kapsamında geliştirilmiştir. © 2026*

**AtölyeŞef**, Meslek Yüksek Okulu İnternet Programcılığı dersi kapsamında modern web geliştirme standartlarına uygun olarak tasarlanmış, **Flask 3.x** tabanlı bir atölye ve laboratuvar ekipman/zimmet takip sistemidir.

---

## ✨ Öne Çıkan Özellikler

- 🌐 **Flask 3.x Standartları:** Modern Flask mimarisi ve bileşenleri.
- 📦 **Application Factory Pattern:** Modüler, kolay test edilebilir ve genişletilebilir uygulama yapısı.
- 🧩 **Blueprint Mimarisi:** Uygulamanın anasayfa (`main`) ve kimlik doğrulama (`auth`) bölümlerine temiz bir şekilde ayrılması.
- 🎨 **Premium Arayüz Deneyimi:** Google Fonts (Outfit) tabanlı, modern animasyonlu ve degrade geçişli estetik koyu tema (dark mode) tasarımı.
- 🛡️ **Güvenlik Politikası:** Çevre değişkenlerinin (`.env`) ve yerel veritabanlarının sürüm kontrol sisteminde (Git) güvenle yoksayılması.
- 🧪 **Kapsamlı Test Altyapısı:** Uygulama modülleri, konfigürasyonu ve temel route erişimlerini doğrulayan entegre birim testleri.
- 🔐 **Kullanıcı Kimlik Doğrulama (Auth):** Flask‑Login, Flask‑WTF ve CSRF korumalı formlarla tam güvenli kayıt, giriş ve çıkış akışı. Bootstrap 5 kartlarıyla şık ve ortalanmış tasarım.

---

## 🚀 Teknolojik Altyapı

Proje yalnızca ders gereksinimlerine uygun olarak en verimli kütüphaneler kullanılmıştır:

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
│   ├── models.py            # Veritabanı Modelleri (User vb.)
│   ├── main/
│   │   ├── __init__.py      # Main Blueprint Tanımı
│   │   └── routes.py        # Anasayfa ve Temel Route'lar
│   ├── auth/
│   │   ├── __init__.py      # Auth Blueprint Tanımı
│   │   ├── routes.py        # Giriş/Çıkış İşlemleri
│   │   └── forms.py         # Register ve Login Formları (Flask‑WTF)
│   ├── templates/          # Premium HTML Şablonları
│   │   └── base.html        # Temel Layout ve Stil
│   └── static/             # CSS & Görseller
│       └── css/
│           └── style.css    # Premium CSS Stil Dosyası
├── docs/                    # Geliştirme Raporları ve Planlar
│   ├── Uygulama_Plani.md    # Teknik Mimari Tasarım Planı
│   ├── Proje_Raporu.md      # Kurulum ve Test Doğrulama Raporu
│   └── AI_Gunlugu.md       # AI Geliştirme Günlüğü
├── tests/                   # Birim Testleri
│   ├── __init__.py
│   └── test_basics.py       # Temel Uygulama Testleri
├── config.py                # Dinamik Konfigürasyon
├── requirements.txt         # Paket Bağımlılıkları
├── .env.example             # Örnek Çevre Değişkenleri
├── .gitignore               # Sürüm Kontrolünde Yoksayılacak Dosyalar
└── run.py                   # Uygulama Giriş Noktası
```

---

## 🛠️ Kurulum ve Çalıştırma

Projenizi yerel bilgisayarınızda çalıştırmak için aşağıdaki adımları sırasıyla uygulayabilirsiniz:

1. **Sanal Ortamı Etkinleştirin**
   PowerShell veya Komut Satırı üzerinden proje dizinine girerek sanal ortamı aktif hale getirin:

   ```powershell
   # PowerShell için:
   .\venv\Scripts\Activate.ps1

   # Klasik CMD için:
   .\venv\Scripts\activate.bat
   ```

2. **Uygulamayı Başlatın**
   Uygulama sunucusunu çalıştırmak için:

   ```bash
   python run.py
   ```

   Sunucu başarıyla ayağa kalktığında tarayıcınızdan **`http://127.0.0.1:5000`** adresine giderek sistemi canlı olarak görebilirsiniz.

---

## 🧪 Testlerin Koşturulması

Projede yer alan temel birim testlerini (unittest) çalıştırmak için sanal ortamınız aktifken terminalde şu komutu yürütün:

```bash
python -m unittest tests/test_basics.py
```

---

## 📄 Proje Geliştirme Günlükleri ve AI Raporları

Projenin planlama, tasarım ve entegrasyon safhalarına ait tüm teknik belgelere `docs/` klasöründen erişebilirsiniz:

1. 📋 **[Uygulama Planı (docs/Uygulama_Plani.md)](docs/Uygulama_Plani.md):** Proje başlamadan önce hazırlanan teknik mimari planı.
2. 📊 **[Proje Raporu (docs/Proje_Raporu.md)](docs/Proje_Raporu.md):** Test doğrulama çıktıları ve yapılan işlerin özeti.
3. 📓 **[AI Geliştirme Günlüğü (docs/AI_Gunlugu.md)](docs/AI_Gunlugu.md):** Yapay Zeka ile birlikte gerçekleştirilen tüm debug, kurulum ve geliştirme süreçlerinin kronolojik kaydı.

---

*Bu proje İnternet Programcılığı Dersi için geliştirilmiştir. Tüm Hakları Saklıdır © 2026.*

**AtölyeŞef**, Meslek Yüksek Okulu İnternet Programcılığı dersi kapsamında modern web geliştirme standartlarına uygun olarak tasarlanmış, **Flask 3.x** tabanlı bir atölye ve laboratuvar ekipman/zimmet takip sistemidir.

---

## ✨ Öne Çıkan Özellikler

- 🌐 **Flask 3.x Standartları:** Modern Flask mimarisi ve bileşenleri.
- 📦 **Application Factory Pattern:** Modüler, kolay test edilebilir ve genişletilebilir uygulama yapısı.
- 🧩 **Blueprint Mimarisi:** Uygulamanın anasayfa (`main`) ve kimlik doğrulama (`auth`) bölümlerine temiz bir şekilde ayrılması.
- 🎨 **Premium Arayüz Deneyimi:** Google Fonts (Outfit) tabanlı, modern animasyonlu ve degrade geçişli estetik koyu tema (dark mode) tasarımı.
- 🛡️ **Güvenlik Politikası:** Çevre değişkenlerinin (`.env`) ve yerel veritabanlarının sürüm kontrol sisteminde (Git) güvenle yoksayılması.
- 🧪 **Kapsamlı Test Atyapısı:** Uygulama modülleri, konfigürasyonu ve temel route erişimlerini doğrulayan entegre birim testleri.

---

## 🚀 Teknolojik Altyapı

Proje yalnızca ders gereksinimlerine uygun olarak en verimli kütüphaneler kullanılmıştır:

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
│   ├── models.py            # Veritabanı Modelleri (User vb.)
│   ├── main/
│   │   ├── __init__.py      # Main Blueprint Tanımı
│   │   └── routes.py        # Anasayfa ve Temel Route'lar
│   ├── auth/
│   │   ├── __init__.py      # Auth Blueprint Tanımı
│   │   ├── routes.py        # Giriş/Çıkış İşlemleri
│   │   └── forms.py         # Login Form Sınıfı (Flask‑WTF)
│   ├── templates/          # Premium HTML Şablonları
│   │   └── base.html        # Temel Layout ve Stil
│   └── static/             # CSS & Görseller
│       └── css/
│           └── style.css    # Premium CSS Stil Dosyası
├── docs/                    # Geliştirme Raporları ve Planlar
│   ├── Uygulama_Plani.md    # Teknik Mimari Tasarım Planı
│   ├── Proje_Raporu.md      # Kurulum ve Test Doğrulama Raporu
│   └── AI_Gunlugu.md        # AI Geliştirme Günlüğü
├── tests/                   # Birim Testleri
│   ├── __init__.py
│   └── test_basics.py       # Temel Uygulama Testleri
├── config.py                # Dinamik Konfigürasyon
├── requirements.txt         # Paket Bağımlılıkları
├── .env.example             # Örnek Çevre Değişkenleri
├── .gitignore               # Sürüm Kontrolünde Yoksayılacak Dosyalar
└── run.py                   # Uygulama Giriş Noktası
```

---

## 🛠️ Kurulum ve Çalıştırma

Projenizi yerel bilgisayarınızda çalıştırmak için aşağıdaki adımları sırasıyla uygulayabilirsiniz:

1. **Sanal Ortamı Etkinleştirin**
   PowerShell veya Komut Satırı üzerinden proje dizinine girerek sanal ortamı aktif hale getirin:

   ```powershell
   # PowerShell için:
   .\venv\Scripts\Activate.ps1

   # Klasik CMD için:
   .\venv\Scripts\activate.bat
   ```

2. **Uygulamayı Başlatın**
   Uygulama sunucusunu çalıştırmak için:

   ```bash
   python run.py
   ```

   Sunucu başarıyla ayağa kalktığında tarayıcınızdan **`http://127.0.0.1:5000`** adresine giderek sistemi canlı olarak görebilirsiniz.

---

## 🧪 Testlerin Koşturulması

Projede yer alan temel birim testlerini (unittest) çalıştırmak için sanal ortamınız aktifken terminalde şu komutu yürütün:

```bash
python -m unittest tests/test_basics.py
```

---

## 📄 Proje Geliştirme Günlükleri ve AI Raporları

Projenin planlama, tasarım ve entegrasyon safhalarına ait tüm teknik belgelere `docs/` klasöründen erişebilirsiniz:

1. 📋 **[Uygulama Planı (docs/Uygulama_Plani.md)](docs/Uygulama_Plani.md):** Proje başlamadan önce hazırlanan teknik mimari planı.
2. 📊 **[Proje Raporu (docs/Proje_Raporu.md)](docs/Proje_Raporu.md):** Test doğrulama çıktıları ve yapılan işlerin özeti.
3. 📓 **[AI Geliştirme Günlüğü (docs/AI_Gunlugu.md)](docs/AI_Gunlugu.md):** Yapay Zeka ile birlikte gerçekleştirilen tüm debug, kurulum ve geliştirme süreçlerinin kronolojik kaydı.

---

*Bu proje İnternet Programcılığı Dersi için geliştirilmiştir. Tüm Hakları Saklıdır © 2026*

## 📦 Equipment CRUD Özellikleri

- **Listeleme**: `/equipments` rotası, ekipmanları tablo halinde gösterir (Bootstrap 5 ile biçimlendirildi).
- **Sayfalama**: Sayfa başına 10 kayıt, `?page=` parametresi (SQLAlchemy 2.x `db.paginate` kullanılarak).
- **Arama**: Üstteki arama çubuğu `?q=` ile `name`, `code`, `laboratory` alanlarında arama yapar (SQLAlchemy `ilike` kullanımı).
- **Ekleme**: `/equipment/new` (login_required) yeni ekipman ekleme formu (Flask-WTF).
- **Düzenleme**: `/equipment/<int:id>/edit` (login_required) mevcut ekipmanı güncelleme.
- **Silme**: `/equipment/<int:id>/delete` POST (login_required) ekipman silme, CSRF korumalı güvenli form yapısı.

---
< ! - -   D u m m y   c o m m i t   1   - - >  
 #   D u m m y   c o m m i t   1  
 