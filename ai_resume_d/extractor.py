import os
import pdfplumber
import fitz  # PyMuPDF
import docx

def extract_text_from_pdf_pdfplumber(path):
    texts = []
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            texts.append(page.extract_text() or '')
    return '\n'.join(texts)

def extract_text_from_pdf_mupdf(path):
    doc = fitz.open(path)
    texts = []
    for page in doc:
        texts.append(page.get_text())
    return '\n'.join(texts)

def extract_text_from_docx(path):
    doc = docx.Document(path)
    texts = [p.text for p in doc.paragraphs]
    return '\n'.join(texts)

def extract_text_from_file(path):
    ext = os.path.splitext(path)[1].lower()
    if ext == '.pdf':
        try:
            return extract_text_from_pdf_pdfplumber(path)
        except Exception as e:
            # fallback
            return extract_text_from_pdf_mupdf(path)
    elif ext == '.docx':
        return extract_text_from_docx(path)
    else:
        return ''
