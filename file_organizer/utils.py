import glob
import os

def get_files_path_list(directory_path):
    """
    Gets list of files in a directory. Including subdirectories. 
    """
    file_paths_list  = [p for p in glob.glob(directory_path + "**", recursive = True) if os.path.isfile(p)]   
    return file_paths_list

def is_file_for_delete(reference_name):
    """
    Checks if user wants to delete given file
    Returns:
        flag (Bool)
    """
    print(f"Desea eliminar el archivo {reference_name}")
    flag = int(input("Ingrese 0 para no y 1 para sí: "))
    
    return flag

def get_file_name_path(file_path):
    """
    Gives file name and file path.
    Returns:
        file_name (String)
        base_path (Strin)
    """
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    file_base_path = os.path.dirname(file_path)

    return file_name, file_base_path