metadata
title: Structify AI
emoji: 📄
colorFrom: blue
colorTo: indigo
sdk: docker
pinned: false
📄 Structify AI
Offline Intelligent Document Structuring System powered by Local AI.

Structify AI is an offline-first AI application that transforms unstructured PDFs and images into structured JSON using OCR, a local Small Language Model through Ollama, and SQLite.

Features
Upload PDF or image documents
Extract text from PDFs using PyMuPDF
Extract text from images using Tesseract OCR
Convert extracted text into structured JSON using a local LLM
Generate a short summary of the document
Save processed documents to SQLite
Download extracted structured JSON
Tech Stack
Streamlit
PyMuPDF
Tesseract OCR
Ollama
SQLite
Docker
Note
This Hugging Face Space runs the app using Docker and local inference setup.# 📄 Structify AI

Offline Intelligent Document Structuring System powered by Local AI

Structify AI is an offline-first AI application that transforms unstructured PDFs and images into structured JSON using OCR, a local Small Language Model (Phi-3 via Ollama), and SQLite.

Unlike cloud-based document processing systems, Structify AI performs all processing locally without sending any data to external APIs.

🚀 Features
📄 PDF Text Extraction (PyMuPDF)
🖼 Image OCR using Tesseract
🤖 Local AI inference using Ollama + Phi-3 Mini
📋 Automatic Structured JSON generation
📝 AI-powered document summarization
💾 Local SQLite database storage
📚 Document history
⬇ Download structured JSON
🔒 Fully Offline
💻 CPU Optimized
🛠 Tech Stack
Python
Streamlit
PyMuPDF
Tesseract OCR
Pillow
Ollama
Phi-3 Mini
SQLite
🏗 Architecture
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
📂 Project Structure
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
⚙ Installation
Clone the repository

git clone <repository-url>
Create virtual environment

python -m venv venv
Activate

Windows

venv\Scripts\activate
Install dependencies

pip install -r requirements.txt
Install Ollama
Download:

https://ollama.com/download

Pull the model

ollama pull phi3:mini
Install Tesseract OCR
Download Tesseract OCR.

Default installation path:

C:\Program Files\Tesseract-OCR\
Run
streamlit run app.py
Workflow
Upload PDF or Image
Extract text
OCR (for images)
Local AI processing
Generate structured JSON
Generate summary
Save into SQLite
Download JSON
Sample Output
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
Future Enhancements
Multi-document analysis
Table extraction
Batch document processing
Semantic search
Local vector database
Advanced document templates
License
MIT License

Author
Pandhare Shivani
M.Anila
Hakshith