# ✦ StudyMind

### AI Destekli Kişiselleştirilmiş Ders Çalışma Asistanı

StudyMind, öğrencilerin ders materyallerini daha kolay anlayıp çalışabilmesi için geliştirilmiş yapay zekâ destekli bir çalışma asistanıdır.

Öğrenci bir **PDF ders materyali** yükler. StudyMind bu materyali analiz ederek:

* 📖 Özet oluşturur
* 📝 Ders notları oluşturur
* ❓ Materyale özel çalışma soruları üretir

## 🚀 Nasıl Çalışır?

```text
PDF Yükle
    ↓
PDF'den Metin Çıkarma
    ↓
Metin Temizleme
    ↓
Yapay Zekâ Analizi
    ↓
┌─────────────┬──────────────┬───────────────┐
│    Özet     │  Ders Notu   │    Sorular    │
└─────────────┴──────────────┴───────────────┘
```

StudyMind, yüklenen materyalin içeriğini doğrudan analiz ederek çıktıları materyale göre oluşturur.

## 🧠 Özellikler

### 📄 PDF Analizi

Yüklenen PDF içerisindeki metin PyMuPDF kullanılarak çıkarılır ve AI işleminden önce temizlenir.

### 📖 Akıllı Özet

Ders materyalindeki ana fikirleri, önemli kavramları ve sınav açısından önemli noktaları öne çıkaran bir özet oluşturulur.

### 📝 Ders Notu

Materyal, öğrencinin çalışmasını kolaylaştıracak şekilde düzenlenmiş ders notlarına dönüştürülür.

### ❓ Soru Üretimi

Yüklenen materyalin içeriğine göre yapay zekâ tarafından çalışma soruları oluşturulur.

### 🎨 Öğrenci Dostu Arayüz

Çıktılar başlıklar, listeler, vurgular ve kod bloklarıyla daha okunabilir şekilde gösterilir.

## 🛠️ Kullanılan Teknolojiler

**Backend**

* Python
* FastAPI
* PyMuPDF

**Yapay Zekâ**

* Groq API
* OpenAI-compatible API
* `openai/gpt-oss-120b`

**Frontend**

* HTML
* CSS
* JavaScript

## 📁 Proje Yapısı

```text
StudyMind/
│
├── app/
│   ├── api/
│   │   └── pdf.py
│   │
│   ├── services/
│   │   ├── ai_service.py
│   │   ├── pdf_service.py
│   │   └── text_cleaner.py
│   │
│   └── static/
│       ├── index.html
│       ├── style.css
│       └── script.js
│
├── main.py
├── README.md
├── .gitignore
└── .env
```

## ⚙️ Kurulum

Projeyi klonladıktan sonra sanal ortam oluşturun:

```bash
python -m venv .venv
```

Sanal ortamı aktif edin:

### Windows

```bash
.venv\Scripts\activate
```

Gerekli paketleri yükleyin:

```bash
pip install fastapi uvicorn python-multipart pymupdf python-dotenv openai
```

Ardından proje klasöründe `.env` dosyası oluşturun:

```env
GROQ_API_KEY=your_api_key_here
```

Uygulamayı çalıştırın:

```bash
uvicorn main:app --reload
```

Tarayıcıdan:

```text
http://127.0.0.1:8000
```

adresine gidin.

## 🔐 Güvenlik

API anahtarı `.env` dosyasında tutulmaktadır ve `.gitignore` ile GitHub'a gönderilmemektedir.

## 🎯 Projenin Amacı

StudyMind'ın amacı, öğrencilerin uzun ve dağınık ders materyalleriyle çalışırken harcadıkları zamanı azaltmak ve tek bir materyal üzerinden farklı çalışma içerikleri oluşturabilmelerini sağlamaktır.

> **Upload your material. Understand it. Study smarter.**

---

### Hackathon Project

StudyMind, öğrenme deneyimini yapay zekâ ile desteklemek amacıyla geliştirilmiş bir hackathon projesidir.
