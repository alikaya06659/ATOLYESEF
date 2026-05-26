import multiprocessing
import threading
import time
import uvicorn
import webview
import os
import sys
from backend.main import app

def start_backend():
    # Backend'i başlat
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="error")

if __name__ == "__main__":
    # Windows'ta multiprocessing desteği için
    multiprocessing.freeze_support()

    # Backend'i ayrı bir thread'de başlat
    t = threading.Thread(target=start_backend, daemon=True)
    t.start()

    # Sunucunun başlaması için kısa bir bekleme
    time.sleep(2)

    # Webview penceresini oluştur
    print("Uygulama Başlatılıyor...")
    window = webview.create_window(
        'AI Detection System', 
        'http://127.0.0.1:8000',
        width=1000,
        height=800,
        resizable=True,
        background_color='#0f172a'
    )

    # Uygulamayı başlat
    webview.start()
