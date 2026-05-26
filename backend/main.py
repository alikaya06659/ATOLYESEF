from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
import shutil
from .analysis import analyzer
from .database import save_analysis, get_history, init_db

app = FastAPI(title="AI Detection System API")

# CORS ayarları (Frontend ile iletişim için)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Klasörleri oluştur
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)
init_db()

@app.post("/analyze")
async def analyze_content(
    file: UploadFile = File(None),
    text: str = Form(None),
    mode: int = Form(0), # 0: Hızlı, 1: Detaylı
):
    content_data = ""
    content_type_idx = 0 # 0: Metin, 1: Görsel, 2: Video
    filename = "text_input"

    if file:
        filename = file.filename
        file_path = os.path.join(UPLOAD_DIR, filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Dosya uzantısına göre tip belirle
        ext = filename.split(".")[-1].lower()
        if ext in ["jpg", "jpeg", "png"]:
            content_type_idx = 1
        elif ext in ["mp4", "avi", "mov"]:
            content_type_idx = 2
        content_data = filename # C++ tarafında dosya adı üzerinden işlem yapılabilir
    elif text:
        content_data = text
        content_type_idx = 0
    else:
        return {"error": "İçerik sağlanmadı."}

    # Analiz Yap
    score = analyzer.analyze(content_data, mode, content_type_idx)
    
    # Mesaj Belirle
    if score < 50:
        message = "İnsan yapımı gibi görünüyor."
    elif score == 50:
        message = "Şüpheli/Yapay zeka olabilir."
    else:
        message = "Yapay zeka tarafından üretilmiş olma ihtimali yüksek!"

    # Veritabanına kaydet
    content_type_str = ["Metin", "Görsel", "Video"][content_type_idx]
    save_analysis(filename, content_type_str, score, message)

    return {
        "score": round(score, 2),
        "message": message,
        "type": content_type_str
    }

@app.get("/history")
async def fetch_history():
    history = get_history()
    return [{"id": r[0], "filename": r[1], "type": r[2], "score": r[3], "message": r[4], "time": r[5]} for r in history]

# Frontend statik dosyalarını servis et
import sys
if hasattr(sys, '_MEIPASS'):
    # PyInstaller bundle path
    BASE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.join(os.path.dirname(__file__), "..")

FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")
app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
