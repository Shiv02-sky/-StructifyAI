---
title: Structify AI
emoji: 📄
colorFrom: blue
colorTo: indigo
sdk: docker
pinned: false
---

# 📄 Structify AI

Offline Intelligent Document Structuring System powered by Local AI.

Structify AI is an offline-first AI application that transforms unstructured PDFs and images into structured JSON using OCR, a local Small Language Model through Ollama, and SQLite.

## 🚀 Features

- Upload PDF or image documents
- Extract text from PDFs using PyMuPDF
- Extract text from images using Tesseract OCR
- Convert extracted text into structured JSON using a local LLM
- Generate a short summary of the document
- Save processed documents to SQLite
- Download extracted structured JSON

## 🛠️ Tech Stack

- Python
- Streamlit
- PyMuPDF
- Tesseract OCR
- Ollama
- SQLite
- Docker

## 📌 Note

This Hugging Face Space runs the app using Docker and local inference setup.

## 📂 Project Structure

```bash
StructifyAI/
│── app.py
│── ai_processor.py
│── extractor.py
│── ocr.py
│── database.py
│── requirements.txt
│── Dockerfile
│── start.sh
│── README.md
```

## ▶️ How it works

1. User uploads a PDF or image.
2. Text is extracted using PyMuPDF or Tesseract OCR.
3. Extracted text is sent to the local LLM through Ollama.
4. The model returns structured JSON and a summary.
5. The results are displayed and saved locally in SQLite.

## 🌍 Use Cases

- Resume parsing
- Invoice/document extraction
- Offline record digitization
- Structured conversion of government or academic documents
- Low-connectivity document intelligence workflows

## 🔒 Offline-first Advantage

Unlike cloud-based document processing systems, Structify AI performs all processing locally without sending any data to external APIs.

## 👩‍💻 Author

Pandhare Shivani
