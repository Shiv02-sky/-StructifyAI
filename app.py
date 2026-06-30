import json
import streamlit as st

from extractor import extract_pdf_text
from ocr import extract_image_text
from ai_processor import process_document
from database import (
    initialize_database,
    save_document,
    get_documents,
    get_document
)

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
- 🤖 Ollama (Phi-3 Mini)
- 💾 SQLite
""")

st.divider()

# ---------------- Upload ---------------- #

uploaded_file = st.file_uploader(
    "Upload a PDF or Image",
    type=["pdf", "png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    st.success("File uploaded successfully!")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Filename", uploaded_file.name)

    with col2:
        st.metric("Type", uploaded_file.type)

    with col3:
        st.metric(
            "Size (KB)",
            round(uploaded_file.size / 1024, 2)
        )

    st.divider()

    if st.button("🚀 Extract Structured Data"):

        # ---------------- Extract Text ---------------- #

        if uploaded_file.type == "application/pdf":

            with st.spinner("📄 Extracting PDF..."):
                extracted_text = extract_pdf_text(uploaded_file)

        else:

            with st.spinner("🖼️ Running OCR..."):
                extracted_text = extract_image_text(uploaded_file)

        st.success("Text extraction completed!")

        st.subheader("📜 Extracted Text")

        st.text_area(
            "Content",
            extracted_text,
            height=350
        )

        # ---------------- Local AI ---------------- #

        with st.spinner("🤖 Running Local AI..."):
            result = process_document(extracted_text)

        # ---------------- JSON ---------------- #

        st.subheader("📋 Structured JSON")

        st.json(result)

        # ---------------- Summary ---------------- #

        st.subheader("📝 Summary")

        if isinstance(result.get("summary"), list):

            for i, point in enumerate(result["summary"], start=1):
                st.success(f"{i}. {point}")

        else:

            st.success(result.get("summary", ""))

        # ---------------- Database ---------------- #

        save_document(
            uploaded_file.name,
            uploaded_file.type,
            extracted_text,
            json.dumps(result["json"], indent=4),
            result["summary"]
        )

        st.success("💾 Saved to SQLite!")

        # ---------------- Download ---------------- #

        st.download_button(
            label="⬇ Download JSON",
            data=json.dumps(result, indent=4),
            file_name="structured_data.json",
            mime="application/json"
        )

st.divider()

st.divider()

st.header("📚 Previously Processed Documents")

history = get_documents()

if history:

    for doc in history:

        with st.expander(f"{doc[1]}  |  {doc[2]}"):

            data = get_document(doc[0])

            st.subheader("Summary")

            st.write(data[5])

            st.subheader("Structured JSON")

            st.code(data[4], language="json")

else:

    st.info("No documents processed yet.")