# 📚 StudyMind

**AI-powered study assistant that transforms PDF course materials into structured study content and practice questions.**

StudyMind is an educational AI application designed to help students study more efficiently. Users can upload their course materials as PDF files, and StudyMind analyzes the content to generate a concise summary, structured study notes, and exam-oriented questions.

---

## 🚀 Features

### 📄 PDF Upload

Upload any text-based PDF course material directly to the application.

### 🧠 AI-Powered Analysis

StudyMind uses an AI model to analyze the uploaded material and understand its content.

### 📖 Automatic Summarization

The application generates a structured summary containing:

* Main ideas
* Important definitions
* Exam-critical information
* Key concepts

### 📝 Study Notes

The uploaded material is transformed into organized study notes with sections such as:

* Concept explanation
* Important information
* Key concepts
* Examples
* Exam-critical points
* Commonly confused concepts

### ❓ Practice Question Generation

StudyMind can generate multiple-choice questions based directly on the uploaded material, helping students test their understanding.

### 🎨 Student-Friendly Interface

The web interface presents generated content in a clean, structured and easy-to-read format.

---

## 🛠️ Technologies

### Backend

* Python
* FastAPI
* PyMuPDF
* OpenAI Python SDK
* Groq API

### Frontend

* HTML
* CSS
* JavaScript

### AI

* Groq API
* `openai/gpt-oss-120b`

---

## 🔄 How It Works

```text
        PDF Upload
             │
             ▼
      PDF Text Extraction
             │
             ▼
        Text Cleaning
             │
             ▼
       AI Content Analysis
             │
       ┌─────┼─────┐
       ▼     ▼     ▼
    Summary Notes Questions
       │     │     │
       └─────┼─────┘
             ▼
      Student Study Material
```

---

## 💻 Project Structure

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
├── requirements.txt
└── .env
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/zgnrrs/StudyMind.git
cd StudyMind
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_api_key_here
```

### 6. Start the application

```bash
uvicorn main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

---

## 📚 Usage

1. Open StudyMind in your browser.
2. Select a PDF course material.
3. Upload the PDF.
4. Wait for the AI analysis to finish.
5. Review the generated summary and study notes.
6. Click **Generate Questions** to create practice questions.
7. Use the generated material to prepare for your exam.

---

## 🎯 Goal

The goal of StudyMind is to reduce the time students spend manually processing lecture materials and help them focus on actually learning the content.

Instead of reading through a large PDF and manually creating notes and questions, students can use StudyMind to transform their existing course materials into a personalized study resource.

---

## 🔮 Future Improvements

Possible future improvements include:

* Difficulty selection for generated questions
* Different question types
* Interactive quizzes
* Answer explanations
* Flashcard generation
* Personalized study plans
* Progress tracking
* User accounts
* Support for image-based/scanned PDFs
* Improved handling of tables and diagrams
* Multi-language support

---

## 🏆 Project

StudyMind was developed as an AI-powered educational project for a hackathon.

The project focuses on combining **generative AI, document processing, and web technologies** to create a practical study assistant for students.

---

## 👩‍💻 Team

**StudyMind Team**

Built with ❤️ and AI to make studying smarter.
