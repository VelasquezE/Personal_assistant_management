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

pdf_path = "/mnt/c/Users/estev/OneDrive - Universidad Nacional de Colombia/Universidad/02_Física/SemestreVII/FundamentosDeÓptica/Libros/Francis Jenkins, Harvey White - Fundamentals of optics-McGraw-Hill Science_Engineering_Math (2001).pdf"
pdf = pypdf.PdfReader(pdf_path)

# TODO create function that gets path and name of a file, algo used in file organizer and encrypter

book_name = pdf.metadata.title
author = pdf.metadata.author

if not book_name and not author:
    draft_title = os.path.splitext(os.path.basename(pdf_path))[0]
    title = prepare_string(draft_title)
else:
    book_name = book_name.lower()
    draft_title = f"{book_name}_{author}"

new_title = prepare_string(draft_title)

# TODO rename file with shutil

