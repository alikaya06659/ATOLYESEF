# Proje Raporu – AtölyeŞef

## Proje Tanımı
AtölyeŞef, **Flask 3.x** üzerine inşa edilmiş, **Atölye ve Laboratuvar Ekipman Takip Sistemi**dir. Kullanıcılar sisteme kayıt olur, ekipmanları görüntüler ve rezervasyon (ödünç alma) işlemleri yapabilir.

## Teknoloji Stack
- **Python 3.11+**
- **Flask 3.x** – Application Factory Pattern
- **Flask‑SQLAlchemy 3.x** (SQLAlchemy 2.x `Mapped`/`mapped_column` sözdizimi)
- **Flask‑Migrate** – Alembic tabanlı veritabanı göçleri
- **Flask‑Login** – Kullanıcı oturum yönetimi
- **Flask‑WTF** – Form ve CSRF koruması
- **SQLite** (development) – `SQLALCHEMY_DATABASE_URI` ortam değişkeni üzerinden yapılandırılabilir

## Mimari Tasarım
```
+-------------------+        +-------------------+
|   app/__init__.py | ---->  |   Flask app       |
+-------------------+        +-------------------+
        |                              |
        |                              |
        v                              v
+-------------------+        +-------------------+
|   app/models.py   | <----> |   SQLAlchemy ORM  |
+-------------------+        +-------------------+
        |
        |  One‑to‑Many
        v
+-------------------+        +-------------------+
|  app/main/       |        |   Blueprint      |
+-------------------+        +-------------------+
```
- **User** ↔ **Reservation** (1‑N)
- **Equipment** ↔ **Reservation** (1‑N)

## Kurulum
```powershell
# Proje klasörüne girin
cd C:\Users\LENOVA\Documents\netprog

# Sanal ortam oluşturup aktif edin
python -m venv venv
.\venv\Scripts\Activate.ps1  # Powershell

# Bağımlılıkları yükleyin
pip install -r requirements.txt

# Veritabanı göçlerini çalıştırın
flask db upgrade

# Sunucuyu başlatın
python run.py
```
Uygulama `http://127.0.0.1:5000` adresinde çalışır.

## Testler
```bash
python -m unittest discover -s tests
```
Temel route ve model import testleri içerir.

## Deploy
Uygulamayı bir WSGI sunucusuna (Gunicorn, uWSGI) veya **Docker** konteynerine yerleştirerek üretim ortamına aktarabilirsiniz. Çevre değişkenleri (`SECRET_KEY`, `SQLALCHEMY_DATABASE_URI`) güvenli bir şekilde yönetilmelidir.

## Gelecek Geliştirmeler
- RESTful API (CRUD endpoint’leri)
- Front‑end için **React/Vue** entegrasyonu
- Ekipman durum takibi için **WebSocket** bildirimleri
- Rol‑tabanlı yetkilendirme (admin, kullanıcı)

---
*Bu rapor proje klasöründeki `docs/Proje_Raporu.md` dosyasında saklanmaktadır.*
