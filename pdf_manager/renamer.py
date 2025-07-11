import pypdf
import os
import re
import shutil

def prepare_string(text):
    """
    Fix string format.
    """
    text = text.strip()
    text = re.sub(r"-", "_", text)
    text = re.sub(r"\s+", "_", text)
    text = re.sub(r"[^\w\d\-_()]", "", text)
    text = re.sub(r"_+", "_", text)

    return text.strip("_")

def is_a_book(pdf_path):
    """
    Identifies if a pdf is a book based on 
    the number of pages o the document.
    Returns: 
        (Bool) 
    """
    pdf = pypdf.PdfReader(pdf_path)
    n_pages = len(pdf.pages)
    if (n_pages > 100):
        return True
    else:
        return False

def give_new_book_name(book_path):
    pdf = pypdf.PdfReader(book_path)

    book_name = pdf.metadata.title
    author = pdf.metadata.author

    if not book_name and not author:
        draft_title = os.path.splitext(os.path.basename(book_path))[0]
        title = prepare_string(draft_title)
    else:
        book_name = book_name.lower()
        draft_title = f"{book_name}_{author}"

    new_title = prepare_string(draft_title)

    return new_title