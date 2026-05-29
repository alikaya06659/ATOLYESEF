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

## Uygulanan Özellikler
- **Kimlik Doğrulama**: Kullanıcı kayıt, giriş ve oturum yönetimi (Flask-Login).
- **Ekipman Yönetimi (CRUD)**: Ekipman ekleme, listeleme, güncelleme ve silme operasyonları (Yetkilendirmeli erişim).
  - SQLAlchemy 2.x `db.paginate` ile sunucu taraflı sayfalama (sayfa başı 10 kayıt).
  - SQLAlchemy `ilike` kullanımı ile ad, kod ve laboratuvar alanlarında esnek arama özelliği.
  - Silme işlemlerinde yanlışlıkla veri kaybını önlemek için CSRF korumalı form / modal onay mekanizması.
- **Ekipman Ödünç Alma ve İade Etme (Rezervasyon)**: Kullanıcıların "Mevcut" durumdaki ekipmanları ödünç alabilmesi ve sonrasında iade edebilmesi sağlandı.
  - İade işlemlerinde güvenlik odaklı sahiplik yetki kontrolü (`abort(403)`) uygulandı.
- **Profil ve Avatar Yönetimi**: Kullanıcılara ait bir profil sayfası oluşturularak form doğrulama süreçleri entegre edildi.
  - Yüklenen profil fotoğrafları `secure_filename` fonksiyonu ile güvenli olarak kaydedilir.
  - Kullanıcıların geçmiş ve aktif tüm rezervasyonları bu sayfa üzerinden yönetilebilmektedir.
- **Özel Hata Yönetimi**: 404 (Sayfa Bulunamadı) ve 500 (Sunucu Hatası) gibi hatalar özelleştirilmiş, Bootstrap 5 uyumlu ve kullanıcıyı ana sayfaya yönlendiren şablonlarla kaplandı.
- **RESTful API**: Harici servislerin ekipman listesine JSON formatında ulaşabilmesi için `GET /api/v1/equipments` ucu oluşturuldu (Türkçe karakter desteği sağlandı).

## Deploy
Uygulama, üretim (production) ortamında kesintisiz ve yüksek performanslı çalışabilmesi için **Docker** ile kapsüllenmiştir. `flask run` yerine, `run:app` üzerinden **Gunicorn** WSGI sunucusunu çalıştıran yapı kuruludur.

Docker imajını derlemek ve başlatmak için:
```bash
docker build -t atolyesef-app .
docker run -d -p 5000:5000 --env-file .env.example atolyesef-app
```
*(Üretim ortamı için `.env.example` baz alınarak gizli ortam değişkenleri sağlayan gerçek bir `.env` kullanılmalıdır ve yerel veritabanı harici bir MySQL/PostgreSQL sunucusuna bağlanmalıdır.)*
## Gelecek Geliştirmeler
- Front‑end için **React/Vue** entegrasyonu
- Ekipman durum takibi için **WebSocket** bildirimleri
- Rol‑tabanlı yetkilendirme (admin, kullanıcı)

---
*Bu rapor proje klasöründeki `docs/Proje_Raporu.md` dosyasında saklanmaktadır.*
