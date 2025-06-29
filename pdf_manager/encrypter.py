import pypdf
import os

def get_pdf_path():
   pdf_path = input("Enter pdf: ")
   return pdf_path

def ask_password():
   password = input("Enter desired password: ")
   return password

def get_pdf_name_path(pdf_path):
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    pdf_base_path = os.path.dirname(pdf_path)

    return pdf_name, pdf_base_path

def is_replace_delete():
    """
    Checks if user wants to delete original pdf.
    Returns:
        flag (Bool)
    """
    print(f"Desea eliminar el pdf original y conservar solo el encriptado")
    flag = int(input("Ingrese 0 para no y 1 para sí: "))
    
    return flag

def encrypt_pdf(): 
    pdf_complete_path = get_pdf_path()
    password = ask_password()

    pdf_name, pdf_base_path = get_pdf_name_path(pdf_complete_path)

    original_pdf = pypdf.PdfReader(pdf_complete_path)

    new_encrypted_pdf = pypdf.PdfWriter(clone_from = original_pdf)
    new_encrypted_pdf.encrypt(password, algorithm = "AES-256-R5")

    new_name = pdf_name + "_encrypted"
    new_encrypted_pdf.write(f"{pdf_base_path}/{new_name}.pdf")

    if (is_replace_delete()):
        os.remove(pdf_complete_path)
