const API_URL = "http://localhost:8000";

const textInput = document.getElementById('text-input');
const fileInput = document.getElementById('file-input');
const fileNameDisplay = document.getElementById('file-name');
const analyzeBtn = document.getElementById('analyze-btn');
const resetBtn = document.getElementById('reset-btn');
const modeToggle = document.getElementById('mode-toggle');
const resultCard = document.getElementById('result-card');
const resultScore = document.getElementById('result-score');
const resultMsg = document.getElementById('result-msg');
const resultType = document.getElementById('result-type');
const historyList = document.getElementById('history-list');
const refreshHistoryBtn = document.getElementById('refresh-history');
const dropZone = document.getElementById('drop-zone');

// Drag and Drop Effects
dropZone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropZone.classList.add('dragover');
});

dropZone.addEventListener('dragleave', () => {
    dropZone.classList.remove('dragover');
});

dropZone.addEventListener('drop', (e) => {
    e.preventDefault();
    dropZone.classList.remove('dragover');
    if (e.dataTransfer.files.length > 0) {
        fileInput.files = e.dataTransfer.files;
        handleFileSelect(e.dataTransfer.files[0]);
    }
});

// Dosya seçimi gösterimi
fileInput.addEventListener('change', (e) => {
    if (e.target.files.length > 0) {
        handleFileSelect(e.target.files[0]);
    }
});

function handleFileSelect(file) {
    fileNameDisplay.textContent = `${file.name}`;
    textInput.placeholder = "Dosya seçildi. Metin girişi devre dışı.";
    textInput.disabled = true;
    textInput.value = "";
}

// Analiz butonu işlemi
analyzeBtn.addEventListener('click', async () => {
    const text = textInput.value;
    const file = fileInput.files[0];
    const mode = modeToggle.checked ? 1 : 0;

    if (!text && !file) {
        alert("Lütfen bir metin girin veya dosya seçin.");
        return;
    }

    analyzeBtn.disabled = true;
    const originalBtnText = analyzeBtn.textContent;
    analyzeBtn.textContent = "Analiz Ediliyor...";
    resultCard.style.display = 'none';

    const formData = new FormData();
    if (file) {
        formData.append('file', file);
    } else {
        formData.append('text', text);
    }
    formData.append('mode', mode);

    try {
        const response = await fetch(`${API_URL}/analyze`, {
            method: 'POST',
            body: formData
        });

        const data = await response.json();
        displayResult(data);
        loadHistory();
    } catch (error) {
        console.error("Hata:", error);
        alert("Sunucuya bağlanılamadı.");
    } finally {
        analyzeBtn.disabled = false;
        analyzeBtn.textContent = originalBtnText;
    }
});

function displayResult(data) {
    resultCard.style.display = 'block';
    
    // Animate percentage
    animateValue(resultScore, 0, data.score, 1000);
    
    resultMsg.textContent = data.message;
    resultType.textContent = `İçerik Türü: ${data.type}`;

    // Renk ayarla
    if (data.score < 50) {
        resultScore.style.background = 'linear-gradient(to bottom, #4ade80, #22c55e)';
        resultScore.style.webkitBackgroundClip = 'text';
    } else if (data.score === 50) {
        resultScore.style.background = 'linear-gradient(to bottom, #facc15, #eab308)';
        resultScore.style.webkitBackgroundClip = 'text';
    } else {
        resultScore.style.background = 'linear-gradient(to bottom, #f87171, #ef4444)';
        resultScore.style.webkitBackgroundClip = 'text';
    }
}

function animateValue(obj, start, end, duration) {
    let startTimestamp = null;
    const step = (timestamp) => {
        if (!startTimestamp) startTimestamp = timestamp;
        const progress = Math.min((timestamp - startTimestamp) / duration, 1);
        obj.innerHTML = `%${Math.floor(progress * (end - start) + start)}`;
        if (progress < 1) {
            window.requestAnimationFrame(step);
        }
    };
    window.requestAnimationFrame(step);
}

async function loadHistory() {
    try {
        const response = await fetch(`${API_URL}/history`);
        const data = await response.json();
        
        historyList.innerHTML = '';
        data.reverse().forEach(item => { // En yeni en üstte
            const div = document.createElement('div');
            div.className = 'history-item';
            const isAI = item.score >= 50;
            div.innerHTML = `
                <div>
                    <strong style="display: block; margin-bottom: 4px;">${item.filename}</strong>
                    <p style="font-size: 0.8rem; color: var(--text-muted);">${item.time}</p>
                </div>
                <div style="text-align: right;">
                    <span class="badge ${isAI ? 'ai' : 'human'}">${isAI ? 'Yapay Zeka' : 'İnsan'}</span>
                    <p style="font-size: 0.9rem; margin-top: 5px; font-weight: 600;">%${item.score}</p>
                </div>
            `;
            historyList.appendChild(div);
        });
    } catch (error) {
        console.log("Geçmiş yüklenemedi.");
    }
}

refreshHistoryBtn.addEventListener('click', loadHistory);

// Sıfırlama işlemi
resetBtn.addEventListener('click', () => {
    textInput.value = '';
    textInput.disabled = false;
    textInput.placeholder = "Analiz edilecek metni buraya yapıştırın veya bir dosya sürükleyip bırakın...";
    fileInput.value = '';
    fileNameDisplay.textContent = '';
    resultCard.style.display = 'none';
    modeToggle.checked = false;
});

// İlk açılışta geçmişi yükle
loadHistory();
