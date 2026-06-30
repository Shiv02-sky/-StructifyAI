import pytesseract
from PIL import Image

# Change this only if your path is different
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_image_text(uploaded_file):

    image = Image.open(uploaded_file)

    text = pytesseract.image_to_string(image)

    return text