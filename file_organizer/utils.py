import glob
import os

def get_files_path_list(directory_path):
    file_paths_list  = [p for p in glob.glob(directory_path + "**", recursive = True) if os.path.isfile(p)]   
    return file_paths_list

def is_file_for_delete(file_path, reference_name):
    """
    Checks if user wants to delete given file
    Returns:
        flag (Bool)
    """
    print(f"Desea eliminar el archivo {reference_name}")
    flag = int(input("Ingrese 0 para no y 1 para sí: "))
    
    return flag