# 📄 Structify AI

> Offline Intelligent Document Structuring System powered by Local AI

Structify AI is an offline-first AI application that transforms unstructured PDFs and images into structured JSON using OCR, a local Small Language Model (Phi-3 via Ollama), and SQLite.

Unlike cloud-based document processing systems, Structify AI performs **all processing locally** without sending any data to external APIs.

---

# 🚀 Features

- 📄 PDF Text Extraction (PyMuPDF)
- 🖼 Image OCR using Tesseract
- 🤖 Local AI inference using Ollama + Phi-3 Mini
- 📋 Automatic Structured JSON generation
- 📝 AI-powered document summarization
- 💾 Local SQLite database storage
- 📚 Document history
- ⬇ Download structured JSON
- 🔒 Fully Offline
- 💻 CPU Optimized

---

# 🛠 Tech Stack

- Python
- Streamlit
- PyMuPDF
- Tesseract OCR
- Pillow
- Ollama
- Phi-3 Mini
- SQLite

---

# 🏗 Architecture

```
PDF / Image
        │
        ▼
Text Extraction
(PyMuPDF / OCR)
        │
        ▼
Local AI
(Ollama + Phi-3)
        │
        ▼
Structured JSON
        │
        ▼
SQLite Storage
        │
        ▼
History & Download
```

---

# 📂 Project Structure

```
StructifyAI/
│
├── app.py
├── extractor.py
├── ocr.py
├── ai_processor.py
├── database.py
├── prompts.py
├── utils.py
│
├── database/
│
├── uploads/
│
├── assets/
│
├── screenshots/
│
├── requirements.txt
└── README.md
```

---

# ⚙ Installation

Clone the repository

```bash
git clone <repository-url>
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Install Ollama

Download:

https://ollama.com/download

Pull the model

```bash
ollama pull phi3:mini
```

---

# Install Tesseract OCR

Download Tesseract OCR.

Default installation path:

```
C:\Program Files\Tesseract-OCR\
```

---

# Run

```bash
streamlit run app.py
```

---

# Workflow

1. Upload PDF or Image
2. Extract text
3. OCR (for images)
4. Local AI processing
5. Generate structured JSON
6. Generate summary
7. Save into SQLite
8. Download JSON

---

# Sample Output

```json
{
  "document_type": "Internship Letter",
  "title": "Paid Internship Offer",
  "people": [
    "Pandhare Shivani"
  ],
  "organizations": [
    "DLRL",
    "DRDO"
  ],
  "dates": [
    "01-07-2026"
  ]
}
```

---

# Future Enhancements

- Multi-document analysis
- Table extraction
- Batch document processing
- Semantic search
- Local vector database
- Advanced document templates

---

# License

MIT License

---

# Author

**Pandhare Shivani**
