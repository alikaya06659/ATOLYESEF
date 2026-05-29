# 1. Resmi ve hafif Python 3.11 imajı
FROM python:3.11-slim

# 2. Konteyner içi çalışma dizini
WORKDIR /app

# 3. Python çalışma zamanı çevresel değişkenleri
# Python'un bytecode (.pyc) dosyaları oluşturmasını engeller
ENV PYTHONDONTWRITEBYTECODE=1
# Logların tamponlanmadan anında terminal/log akışına düşmesini sağlar
ENV PYTHONUNBUFFERED=1

# 4. Bağımlılıkların kopyalanması ve kurulumu
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Proje kodlarının kopyalanması
# .dockerignore dosyası sayesinde gereksiz/gizli dosyalar kopyalanmayacak
COPY . .

# 6. Uygulamanın çalışacağı port
EXPOSE 5000

# 7. Production WSGI sunucusu ile başlatma
# Projenizdeki run.py içerisindeki app = create_app() yapısını (run:app) kullanıyoruz
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "3", "run:app"]
