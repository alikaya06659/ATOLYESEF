# Uygulama Planı

## Proje Özeti
AtölyeŞef, Flask 3.x ve SQLAlchemy 2.x kullanarak atölye ve laboratuvar ekipman takibi sağlayan bir web uygulamasıdır.

## Mimari
- **Application Factory** (`app/__init__.py`)
- **Blueprints**: `main` ve `auth`
- **Modeller**: `User`, `Equipment`, `Reservation`
- **Formlar**: Flask‑WTF ile CSRF korumalı `RegisterForm` ve `LoginForm`
- **Şablonlar**: Bootstrap 5 ile responsive kartlar

## Kimlik Doğrulama Akışı
1. `/auth/register` – yeni kullanıcı oluşturulur, benzersizlik kontrolü ve şifre hash'leme.
2. `/auth/login` – kullanıcı e‑posta ve şifre ile doğrulanır, `login_user` çağrılır.
3. `/auth/logout` – oturum sonlandırılır.

## Güvenlik
- CSRF koruması (`{{ form.hidden_tag() }}`)
- Parola hash'leme (`werkzeug.security.generate_password_hash`)
- Flask‑Login `LoginManager` ile kullanıcı yükleme (`user_loader`).

## Test Stratejisi
- Birim testler `tests/` içinde.
- Manuel UI testleri: kayıt, giriş, çıkış ve yetkisiz yönlendirmeler.

## Geliştirme Süreci
- AI asistanı ile adım adım kod üretimi ve dökümantasyon.
