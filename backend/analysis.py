import ctypes
import os
import random

# C++ Motoru (DLL) yolu
DLL_PATH = os.path.join(os.path.dirname(__file__), '..', 'engine', 'detector.dll')

class AIAnalyzer:
    def __init__(self):
        self.engine = None
        if os.path.exists(DLL_PATH):
            try:
                self.engine = ctypes.CDLL(DLL_PATH)
                self.engine.calculate_ai_score.restype = ctypes.c_float
                self.engine.calculate_ai_score.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_char_p]
            except Exception as e:
                print(f"C++ Motoru yüklenemedi: {e}")

    def analyze(self, data: str, mode: int = 0, content_type: int = 0) -> float:
        """
        data: İçerik (Metin içeriği veya dosya adı)
        mode: 0 (Hızlı), 1 (Detaylı)
        content_type: 0 (Metin), 1 (Görsel), 2 (Video)
        """
        if self.engine:
            try:
                # C++ motorunu çağır
                score = self.engine.calculate_ai_score(mode, content_type, data.encode('utf-8'))
                return float(score)
            except Exception as e:
                print(f"C++ analizi sırasında hata: {e}")
        
        # Gelişmiş Heuristik Analiz (C++ motoru yoksa veya yedek olarak)
        if content_type == 0: # Metin Analizi
            score = self._analyze_text_heuristics(data)
        else: # Görsel/Video (Simülasyon)
            score = 45.0 + random.uniform(-10, 10)
            
        if mode == 1:
            score += random.uniform(2, 5)
            
        return min(max(score, 0.0), 100.0)

    def _analyze_text_heuristics(self, text: str) -> float:
        text = text.strip()
        if len(text) < 15:
            return 5.0 # Çok kısa metinler genellikle insan
            
        # 1. Cümle Yapısı Analizi
        sentences = [s.strip() for s in text.split('.') if len(s.strip()) > 5]
        if not sentences:
            return 15.0

        # Cümle uzunluğu varyansı (İnsanlar daha kaotik yazar)
        word_counts = [len(s.split()) for s in sentences]
        avg_len = sum(word_counts) / len(word_counts)
        variance = sum((l - avg_len) ** 2 for l in word_counts) / len(word_counts) if len(word_counts) > 1 else 0
        
        # Varyans düşükse (0-10 arası) AI olma ihtimali artar
        # Varyans yüksekse (30+) İnsan olma ihtimali çok yüksektir
        variance_score = max(0, 40 - variance)

        # 2. Kelime Dağarcığı ve Tekrar
        words = text.lower().split()
        if not words: return 0.0
        unique_words = set(words)
        lexical_richness = len(unique_words) / len(words)
        
        # Düşük kelime zenginliği (tekrarlı metin) AI belirtisi olabilir
        richness_score = max(0, (0.7 - lexical_richness) * 100)

        # 3. AI Kalıpları (Transition words)
        # Sadece bu kelimelerin olması AI demez, ama sıklığı önemli
        ai_patterns = ["furthermore", "moreover", "consequently", "additionally", "in conclusion", "to sum up", "it is important to note", "notably", "specifically"]
        pattern_count = 0
        for pattern in ai_patterns:
            if pattern in text.lower():
                pattern_count += 1
        
        pattern_score = min(pattern_count * 10, 50)

        # 4. Karakter Analizi (AI metinleri çok "temiz"dir)
        # Özel karakter ve noktalama işareti kullanımı
        special_chars = sum(1 for c in text if not c.isalnum() and not c.isspace())
        char_ratio = (special_chars / len(text)) * 100
        # Çok düşük veya çok standart noktalama AI işareti olabilir
        punct_score = 15 if (1.5 < char_ratio < 3.0) else 0

        # Ağırlıklı Hesaplama (Daha dengeli)
        # İnsanları suçlamamak için baz skoru düşük tutuyoruz
        final_score = (variance_score * 0.35) + (richness_score * 0.20) + (pattern_score * 0.35) + (punct_score * 0.10)
        
        # Rastgelelik ekleyerek sistemin "tahmin edilemez" ama tutarlı olmasını sağla
        final_score += random.uniform(-2, 2)
        
        # Sonuç normalizasyonu: İnsan yazısını kolay kolay 50+ yapma
        if final_score > 40 and final_score < 60:
            # Gri bölgeyi biraz daha aşağı çek (False positive'i azaltmak için)
            final_score -= 10
            
        return min(max(final_score, 5.0), 98.0)

analyzer = AIAnalyzer()
