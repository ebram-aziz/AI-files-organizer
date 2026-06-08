import pytesseract
from pdf2image import convert_from_path

def ocr_pdf(path):

    pages = convert_from_path(path)

    text = ""

    for page in pages:
        text += pytesseract.image_to_string(page)

    return text