#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>

extern "C" {
    // Basit bir analiz skoru hesaplayan C++ fonksiyonu
    // mode: 0 (Hızlı), 1 (Detaylı)
    // content_type: 0 (Metin), 1 (Görsel), 2 (Video)
    __declspec(dllexport) float calculate_ai_score(int mode, int content_type, const char* data) {
        float score = 0.0f;
        std::string content(data);
        
        if (content_type == 0) { // Metin Analizi
            // 1. Kelime Sayısı ve Ortalama Kelime Uzunluğu
            size_t word_count = 0;
            size_t char_count = content.length();
            bool in_word = false;
            for(char c : content) {
                if(isspace(c)) in_word = false;
                else if(!in_word) { word_count++; in_word = true; }
            }
            
            float avg_word_len = word_count > 0 ? (float)char_count / word_count : 0;
            
            // AI metinleri genellikle 5-6 karakter civarında ortalama kelime uzunluğuna sahiptir
            if (avg_word_len > 4.5 && avg_word_len < 6.5) score += 20.0f;

            // 2. Anahtar Kelime Analizi (Basit)
            const char* ai_patterns[] = {"furthermore", "moreover", "consequently", "conclusion", "additionally"};
            int patterns_found = 0;
            std::string content_lower = content;
            std::transform(content_lower.begin(), content_lower.end(), content_lower.begin(), ::tolower);
            
            for(const char* p : ai_patterns) {
                if(content_lower.find(p) != std::string::npos) patterns_found++;
            }
            score += patterns_found * 12.0f;

            // 3. Sterilite Kontrolü (Noktalama işareti sıklığı)
            int punct_count = 0;
            for(char c : content) if(ispunct(c)) punct_count++;
            float punct_ratio = word_count > 0 ? (float)punct_count / word_count : 0;
            
            if (punct_ratio > 0.1 && punct_ratio < 0.2) score += 15.0f;
            
        } else { // Görsel/Video
            score = 30.0f + (content.length() % 40);
        }

        if (mode == 1) score += 7.5f;

        if (score > 100.0f) score = 100.0f;
        if (score < 0.0f) score = 5.0f; // Tam 0 vermemek için (genellikle biraz şüphe olur)

        return score;
    }
}
