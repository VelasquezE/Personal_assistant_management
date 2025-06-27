from file_organizer import downloads as fd

flag = int(input("¿Desea organizar la carpeta de descargas? "))

if flag:
    fd.organize_download_folder("/mnt/c/Users/estev/OneDrive - Universidad Nacional de Colombia/Universidad/02_Física/SemestreVII/IntroducciónCienciasDeLaComputación/Proyecto/Personal_assistant_management/test/")
    print("Carpeta de descargas organizada")


