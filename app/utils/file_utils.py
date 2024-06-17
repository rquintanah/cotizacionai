# app/utils/file_utils.py

import fitz  # PyMuPDF

def extract_text_from_pdf(file_path):
    # Abrir el archivo PDF
    pdf_document = fitz.open(file_path)
    text = ""
    # Iterar a través de las páginas y extraer texto
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    return text
