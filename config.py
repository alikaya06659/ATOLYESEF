import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """Uygulama yapılandırma sınıfı."""

    # Güvenlik anahtarı (geliştirme ortamı için örnek)
    SECRET_KEY = os.environ.get("SECRET_KEY", "cok-gizli-anahtar-degistir")

    # SQLAlchemy veritabanı URI; ortam değişkeni yoksa proje kök dizininde bir SQLite dosyası kullanılır
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQLALCHEMY_DATABASE_URI",
        f"sqlite:///{os.path.join(basedir, 'atelier.db')}"
    )

    # Track modifications kapalı (performans için)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
class TestConfig(Config):
    """Testing configuration – uses in‑memory SQLite DB and enables testing mode."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
