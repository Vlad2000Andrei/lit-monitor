import os
from sys import argv
import PyPDF2
def read_dir(path : str) -> list[str]:
    path = os.path.abspath(path)
    if not os.path.isdir(path):
        raise Exception("Argument should be path to a valid folder but is not.")

    try:
        files = [f for f in os.listdir(path)]
        file_paths = [os.path.join(path, f) for f in files]
        return file_paths
    except Exception as e:
        print(f"Could not get all files in folder {path}. An exception occurred:",  e, sep="\n")

def is_pdf(path : str) -> bool:
    if not os.path.isfile(path):
        raise Exception("Argument should be path to a valid file but is not.")

    return path.endswith(".pdf")

def get_pages(file : str) -> list[PyPDF2.PageObject]:
    if not is_pdf(file):
        raise Exception("Argument is not path to PDF file.")

    reader = PyPDF2.PdfReader(file)
    return reader.pages

