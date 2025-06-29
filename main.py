from file_organizer import downloads as fd
from pdf_manager import encrypter as ec

#flag = int(input("¿Desea organizar la carpeta de descargas? "))

#if flag:
    #fd.organize_download_folder("/mnt/c/Users/estev/OneDrive - Universidad Nacional de Colombia/Universidad/02_Física/SemestreVII/IntroducciónCienciasDeLaComputación/Proyecto/Personal_assistant_management/test/")
    #print("Carpeta de descargas organizada")

flag = int(input("¿Desea encriptar un pdf?"))

if flag:
    ec.encrypt_pdf()
    print("PDF encriptado con éxito")


