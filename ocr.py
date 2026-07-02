import os
import pytesseract
from PIL import Image

# Use custom path only if explicitly provided
TESSERACT_CMD = os.getenv("TESSERACT_CMD")
if TESSERACT_CMD:
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD


def extract_image_text(uploaded_file):
    image = Image.open(uploaded_file)
    text = pytesseract.image_to_string(image)
    return text