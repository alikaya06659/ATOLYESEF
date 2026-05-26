import customtkinter as ctk
import random # Şimdilik rastgelelik simülasyonu için

class AICheckerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Yapay Zeka Tespit Sistemi")
        self.geometry("500x450")

        self.label = ctk.CTkLabel(self, text="Analiz Edilecek Metni Girin", font=("Arial", 16))
        self.label.pack(pady=20)

        self.textbox = ctk.CTkTextbox(self, width=400, height=150)
        self.textbox.pack(pady=10)

        # Kullanıcı Ayarı (Hassaslık)
        self.detail_switch = ctk.CTkSwitch(self, text="Derin Analiz (Piksel/Dil Bilgisi Kontrolü)")
        self.detail_switch.pack(pady=10)

        self.analyze_button = ctk.CTkButton(self, text="Analiz Et", command=self.analyze_action)
        self.analyze_button.pack(pady=20)

        self.result_label = ctk.CTkLabel(self, text="Sonuç: -", font=("Arial", 14, "bold"))
        self.result_label.pack(pady=10)

    def analyze_action(self):
        # 1. Metni kutudan alıyoruz
        input_text = self.textbox.get("1.0", "end-1c").strip()
        
        if not input_text:
            self.result_label.configure(text="Hata: Lütfen bir içerik girin!", text_color="orange")
            return

        # 2. ANALİZ SİMÜLASYONU (Proje mantığına göre)
        # Gerçek bir sistemde burada dil bilgisi veya piksel kontrolü yapan kütüphaneler olur.
        if len(input_text) < 10:
            score = random.randint(10, 40) # Çok kısa metinler genelde düşük skor
        else:
            # Derin analiz açıksa skor daha hassas hesaplanır
            if self.detail_switch.get():
                score = random.randint(30, 95)
            else:
                score = random.randint(40, 60)

        # 3. MANTIKSAL TASARIM KARARLARI
        if score > 50:
            self.result_label.configure(text=f"Sonuç: %{score} Yapay Zeka Tespiti!", text_color="red")
        elif score == 50:
            self.result_label.configure(text=f"Sonuç: %{score} Belirsiz (Yapay Zeka Olabilir)", text_color="yellow")
        else:
            self.result_label.configure(text=f"Sonuç: %{score} İnsan Elinden Çıkma", text_color="green")

if __name__ == "__main__":
    app = AICheckerApp()
    app.mainloop()