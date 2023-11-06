from PyPDF2 import PdfReader
from langchain.document_loaders import PyPDFLoader


def get_pdf_pages(file_obj):
    loader = PyPDFLoader(file_obj.upload_url)
    return loader.load_and_split()
