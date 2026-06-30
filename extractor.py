import fitz


def extract_pdf_text(pdf_file):
    """
    Extract text from a PDF using PyMuPDF.
    """

    document = fitz.open(
        stream=pdf_file.read(),
        filetype="pdf"
    )

    extracted_text = ""

    for page in document:
        extracted_text += page.get_text("text")
        extracted_text += "\n"

    document.close()

    if extracted_text.strip() == "":
        raise Exception(
            "No readable text found in the PDF."
        )

    return extracted_text