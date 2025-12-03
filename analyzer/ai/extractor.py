# extractor.py
# This file is responsible ONLY for extracting text from uploaded resumes.
# It supports PDF and DOCX formats. We keep this simple and readable.

import PyPDF2
from docx import Document

def extract_text_from_pdf(file):
    """Extract all text from a PDF resume."""
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_text_from_docx(file):
    """Extract text from a DOCX resume."""
    doc = Document(file)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

def extract_resume_text(file):
    """Auto-detect file type and extract text accordingly."""
    filename = file.name.lower()

    if filename.endswith(".pdf"):
        return extract_text_from_pdf(file)

    elif filename.endswith(".docx"):
        return extract_text_from_docx(file)

    else:
        return "Unsupported file format"
