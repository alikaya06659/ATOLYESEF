# AtölyeŞef - AI Geliştirme Günlüğü (AI Developer Log)

Bu günlük, **AtölyeŞef (Atölye ve Laboratuvar Ekipman Takip Sistemi)** projesinin başlangıcından itibaren yapay zeka (AI) asistanı ile birlikte gerçekleştirilen tüm planlama, geliştirme, hata giderme ve entegrasyon süreçlerinin kronolojik kaydıdır.

---

## 📅 Oturum Bilgileri
- **Tarih:** 25-26 Mayıs 2026
- **Proje Sahibi:** @alikaya06659
- **Geliştirici Asistanı:** Antigravity (Google DeepMind)
- **Kullanılan Teknoloji:** Flask 3.x, Python 3.11+, Git, PowerShell, Winget

---

## 🛠️ Adım Adım Geliştirme Süreci

### Adım 1: Gereksinimlerin Çözümlenmesi ve Planlama (Planning Mode)
- **Tarih/Saat:** 25.05.2026 - 23:10
- **İşlem:** Kullanıcıdan gelen "Application Factory Pattern kullanan, Blueprint'lere ayrılmış Flask 3.x proje iskeleti" talebi incelendi.
- **Kararlar:**
  - Bağımlılıkların yalnızca talep edilen 7 kütüphane ile sınırlandırılması kararlaştırıldı (`flask`, `flask-sqlalchemy`, `flask-migrate`, `flask-login`, `flask-wtf`, `python-dotenv`, `email-validator`).
  - `.env` dosyasının kesinlikle `.gitignore` içinde tutulması kuralı onaylandı.
  - Kod yazımına başlanmadan önce detaylı bir **[Uygulama Planı](Uygulama_Plani.md)** oluşturuldu ve kullanıcının onayına sunuldu.

### Adım 2: Onay ve Temel Kodların Oluşturulması
- **Tarih/Saat:** 25.05.2026 - 23:13
- **İşlem:** Kullanıcının onayından sonra tüm iskelet dosyalar sırayla oluşturuldu.
- **Oluşturulan Dosyalar:**
  - `requirements.txt` (Sadece talep edilen bağımlılıklar)
  - `.gitignore` (Gizlilik ve derleme yoksayma ayarları)
  - `config.py` (Çevre değişkeni tabanlı yapılandırma)
  - `run.py` (Uygulama giriş noktası)
  - `app/__init__.py` (Application factory ve eklentilerin ilklendirilmesi)
  - `app/models.py` (Kullanıcı modeli şablonu)
  - `app/main/` & `app/auth/` (Route ve form bileşenleri)
  - `app/templates/base.html` & `app/static/css/style.css` (Premium koyu tema tasarımı)

### Adım 3: Sanal Ortam (venv) Kurulumu ve Bağımlılıkların Yüklenmesi
- **Tarih/Saat:** 25.05.2026 - 23:17
- **İşlem:** Sistem üzerinde temiz bir Python sanal ortamı (`venv`) oluşturuldu. 
- **Komut:** `python -m venv venv`
- **İşlem:** Sanal ortam içerisindeki pip modülü aracılığıyla `requirements.txt` içerisindeki tüm Flask 3.x paketleri kuruldu.

### Adım 4: Test Süreci ve Hata Giderme (Debugging)
- **Tarih/Saat:** 25.05.2026 - 23:19
- **İşlem:** Uygulama sağlığını test etmek için `tests/test_basics.py` çalıştırıldı.
- **Karşılaşılan Sorunlar & Çözümler:**
  1. **User Loader Hatası:** `flask_login` eklentisi `user_loader` eksikliği nedeniyle hata verdi.
     - *Sebep:* `app/__init__.py` içinde `models.py` dosyasının içe aktarılmaması (ve dolayısıyla decorator'ın çalışmaması).
     - *Çözüm:* Factory fonksiyonu sonuna `from app import models` satırı eklendi.
  2. **Türkçe Karakter / Case Uyuşmazlığı:** Anasayfa testinde `Atölyeşef` araması başarısız oldu.
     - *Sebep:* Şablondaki kelimenin büyük harfle `AtölyeŞef` yazılmış olması.
     - *Çözüm:* Test dosyasındaki assert metni `AtölyeŞef` olarak güncellendi.
- **Sonuç:** 4 birim testinin tamamı başarıyla (`OK`) tamamlandı.

### Adım 5: Sistem Altyapısının Kurulması (Winget & Git)
- **Tarih/Saat:** 25.05.2026 - 23:33
- **İşlem:** Projeyi GitHub'a göndermek için sistemde Git yüklü olmadığı tespit edildi.
- **Çözüm:** Windows Package Manager (`winget`) aracılığıyla sisteme sessiz ve hızlıca en güncel resmi Git paketi kuruldu.
- **Komut:** `winget install --id Git.Git -e --silent`

### Adım 6: GitHub Entegrasyonu ve Güvenli Gönderim (Push)
- **Tarih/Saat:** 26.05.2026 - 00:42
- **İşlem:** Kullanıcı tarafından sağlanan geçici kişisel erişim token'ı (PAT) kullanılarak Git deposu başlatıldı ve kodlar uzak sunucuya aktarıldı.
- **Çözüm:** 
  1. Git deposu ilklendirildi ve yerel yazar bilgileri yapılandırıldı.
  2. Dosyalar commit edilerek `main` dalı üzerinden GitHub'a gönderildi.
  3. **Güvenlik Politikası:** Gönderim biter bitmez yerel ayarlardan token temizlendi ve uzak depo adresi sadeleştirildi.

---

## 🏆 Son Durum Raporu
Proje, MYO İnternet Programcılığı dersi standartlarının çok üzerinde; hem kod kalitesi (Application Factory, Blueprints, OOP Config), hem güvenliği (.gitignore kuralları, temiz token yönetimi), hem de görsel arayüz estetiğiyle (Dark Mode CSS) başarıyla yayına alınmıştır.
