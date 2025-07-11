from file_organizer import downloads as fd
from pdf_manager import encrypter as ec
from pdf_manager import renamer as ren

print("Bienvenido a la demostración del asistente personal \n")
print("Seleccione la opción que desea probar: \n")
print("1. Organizar carpeta \n")
print("2. Encriptar pdf \n")
print("3. Renombrar pdf \n")

option = int(input())

if (option == 1):
    fd.organize_download_folder("/mnt/c/Users/estev/OneDrive - Universidad Nacional de Colombia/Universidad/02_Física/SemestreVII/IntroducciónCienciasDeLaComputación/Proyecto/test/")
    print("Carpeta de descargas organizada")

if (option == 2):
    ec.encrypt_pdf()
    print("PDF encriptado con éxito")

if (option == 3):
    ren.rename_pdf()
    print("El PDF ha sido renombrado")