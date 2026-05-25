# AtölyeŞef Proje Tasarım Belgesi & Uygulama Planı

Bu belge, **AtölyeŞef (Atölye ve Laboratuvar Ekipman Takip Sistemi)** projesinin Flask 3.x tabanlı, "Application Factory Pattern" ve Blueprint mimarisine uygun temiz iskelet yapısının tasarım detaylarını içerir.

---

## Proje Dizin Yapısı
```text
atölyeşef/
├── app/
│   ├── __init__.py          # Application Factory & Extension Initialization
│   ├── models.py            # Veritabanı Modelleri (Şablon)
│   ├── main/
│   │   ├── __init__.py      # Main Blueprint Tanımı
│   │   └── routes.py        # Main Route'ları
│   ├── auth/
│   │   ├── __init__.py      # Auth Blueprint Tanımı
│   │   ├── routes.py        # Auth Route'ları
│   │   └── forms.py         # Login/Kayıt Form Şablonları
│   ├── templates/
│   │   └── base.html        # Premium Arayüz Temel HTML Şablonu
│   └── static/              # Statik Dosyalar Klasörü (CSS, JS, Resimler)
├── migrations/              # Flask-Migrate Veritabanı Geçiş Dosyaları (Boş Klasör)
├── tests/                   # Birim Testleri Klasörü
│   ├── __init__.py
│   └── test_basics.py       # Temel Uygulama Testleri
├── config.py                # Uygulama Yapılandırma Sınıfı
├── requirements.txt         # Paket Bağımlılıkları Listesi
├── .env.example             # Örnek Çevre Değişkenleri Şablonu
├── .gitignore               # Git Tarafından Yoksayılacak Dosyalar
└── run.py                   # Uygulama Giriş Noktası
```

---

## Bileşen Detayları

### 1. Root Konfigürasyon Dosyaları
- **requirements.txt**: Yalnızca ders kapsamında talep edilen paketler (`flask>=3.0.0`, `flask-sqlalchemy`, `flask-migrate`, `flask-login`, `flask-wtf`, `python-dotenv`, `email-validator`) eklenmiştir.
- **.gitignore**: Güvenlik kuralları gereği `.env` dosyası, local veritabanı dosyaları (`*.db`) ve Python derleme klasörleri (`__pycache__/`, `venv/`) yoksayılmıştır.
- **config.py**: Ayarları `.env` dosyasından okuyacak şekilde `Config` sınıfı tanımlanmıştır.
- **run.py**: Uygulamayı factory desenine uygun şekilde başlatır.

### 2. Flask Uygulama Modülleri (`app/`)
- **app/__init__.py**: Eklentileri (`db`, `migrate`, `login_manager`) başlatır, `main` ve `auth` blueprint'lerini kaydeder. Modellerin Flask-Login tarafından yüklenebilmesi için `app/models.py` dosyasını içe aktarır.
- **app/models.py**: Temel `User` modeli ve `user_loader` fonksiyon iskeletini barındırır.
- **app/main/**: Anasayfa route'larını (`/`, `/index`) yönetir.
- **app/auth/**: Kullanıcı giriş/çıkış işlemlerini (`/login`, `/logout`) yönetir ve `LoginForm` şablonunu içerir.

### 3. Arayüz ve Tasarım (`templates/` & `static/`)
- **base.html**: Tüm sayfalarda kullanılacak premium HTML şablonudur. Sayfa başlıkları, dinamik bloklar, Flask flash mesajları ve WTForms alanları için gerekli taslak yapıları barındırır.
- **static/css/style.css**: Google Fonts 'Outfit' yazı tipini kullanan, modern koyu tema (dark mode), degrade geçişler, kart tasarımları ve mikro-animasyonlar barındıran premium CSS stil dosyasıdır.
