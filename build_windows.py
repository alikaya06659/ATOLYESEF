import os
import subprocess
import sys

def build():
    print("Windows Uygulaması Paketleniyor...")
    
    # Gerekli kütüphane kontrolü
    try:
        import PyInstaller
    except ImportError:
        print("PyInstaller bulunamadı. Yükleniyor...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller", "pywebview"])

    # PyInstaller komutu
    # --onefile: Tek bir exe yapar
    # --windowed: Konsol penceresini gizler
    # --add-data: Frontend ve uploads klasörlerini dahil eder
    command = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--noconfirm",
        "--onefile",
        "--windowed",
        "--name=AIDetector",
        "--add-data=frontend;frontend",
        "--add-data=backend;backend",
        "--add-data=database;database",
        "--icon=NONE", # İsteğe bağlı ikon eklenebilir
        "desktop_app.py"
    ]

    print(f"Çalıştırılan komut: {' '.join(command)}")
    subprocess.run(command)

    print("\nİşlem Tamamlandı!")
    exe_path = os.path.abspath("dist/AIDetector.exe")
    print(f"Uygulamanız '{exe_path}' dizininde oluşturuldu.")

    # Masaüstüne kısayol ekle
    try:
        import winshell
        from win32com.client import Dispatch
    except ImportError:
        print("Kısayol oluşturmak için gerekli kütüphaneler yükleniyor...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "winshell", "pypiwin32"])
        import winshell
        from win32com.client import Dispatch

    desktop = winshell.desktop()
    path = os.path.join(desktop, "AI Detector.lnk")
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = exe_path
    shortcut.WorkingDirectory = os.path.dirname(exe_path)
    shortcut.IconLocation = exe_path
    shortcut.save()

    print(f"Masaüstüne kısayol eklendi: {path}")

if __name__ == "__main__":
    build()
