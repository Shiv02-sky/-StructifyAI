import json
import streamlit as st

from extractor import extract_pdf_text
from ocr import extract_image_text
from ai_processor import process_document
from database import initialize_database, save_document, get_documents

# ---------------- Page Config ---------------- #

st.set_page_config(
    page_title="Structify AI",
    page_icon="📄",
    layout="wide"
)

initialize_database()

# ---------------- Header ---------------- #

st.title("📄 Structify AI")
st.caption("Offline Intelligent Document Structuring System")

st.markdown("""
Transform **PDFs** and **Images** into structured JSON completely offline.

### Tech Stack
- 📄 PyMuPDF
- 🖼️ Tesseract OCR
- 🤖 Ollama (Local Small Language Model)
- 💾 SQLite
""")

st.divider()

# ---------------- File Upload ---------------- #

uploaded_file = st.file_uploader(
    "Upload a PDF or Image",
    type=["pdf", "png", "jpg", "jpeg"],
    accept_multiple_files=False
)

# ---------------- Main Flow ---------------- #

if uploaded_file is not None:
    st.success("File uploaded successfully!")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Filename", uploaded_file.name)

    with col2:
        st.metric("Type", uploaded_file.type)

    with col3:
        st.metric("Size (KB)", round(uploaded_file.size / 1024, 2))

    st.divider()

    if st.button("🚀 Extract Structured Data"):

        # -------- Step 1: Extract Text -------- #
        if uploaded_file.type == "application/pdf":
            with st.spinner("Extracting PDF text..."):
                extracted_text = extract_pdf_text(uploaded_file)
        else:
            with st.spinner("Running OCR on image..."):
                extracted_text = extract_image_text(uploaded_file)

        st.success("Text extraction completed!")

        st.subheader("📜 Extracted Text")
        st.text_area("Content", extracted_text, height=350)

        # -------- Step 2: Run Local AI -------- #
        with st.spinner("Running Local AI..."):
            result = process_document(extracted_text)

        # -------- Step 3: Show JSON -------- #
        st.subheader("📋 Structured JSON")
        st.json(result["json"])

        # -------- Step 4: Show Summary -------- #
        st.subheader("📝 Summary")
        st.success(result["summary"])

        # -------- Step 5: Save to SQLite -------- #
        save_document(
            uploaded_file.name,
            uploaded_file.type,
            extracted_text,
            json.dumps(result["json"]),
            result["summary"]
        )

        st.success("Saved to SQLite!")

        # -------- Step 6: Download JSON -------- #
        st.download_button(
            "⬇ Download JSON",
            data=json.dumps(result["json"], indent=4),
            file_name="structured_data.json",
            mime="application/json"
        )

        st.divider()
        st.info("Processing completed successfully.")

else:
    st.info("Upload a PDF or image to begin.")

# ---------------- Saved Documents History ---------------- #

st.divider()
st.subheader("📚 Saved Documents History")

documents = get_documents()

if documents:
    for doc in documents:
        st.write(f"**ID:** {doc[0]} | **File:** {doc[1]} | **Created At:** {doc[2]}")
else:
    st.info("No documents saved yet.")