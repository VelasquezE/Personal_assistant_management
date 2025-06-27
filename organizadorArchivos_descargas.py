import shutil
import os
import glob
import datetime
import time

extensions_type = {
    'documento': ['pdf', 'doc', 'docx', 'odt'],
    'texto': ['txt', 'md'],
    'hoja_calculo': ['xls', 'xlsx', 'ods', 'csv'],
    'presentacion': ['ppt', 'pptx', 'odp'],
    'imagen': ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'webp'],
    'vector': ['svg', 'eps'],
    'video': ['mp4', 'mov', 'avi', 'mkv', 'flv', 'webm'],
    'audio': ['mp3', 'wav', 'ogg', 'm4a'],
    'comprimido': ['zip', 'rar', '7z', 'tar', 'gz'],
    'codigo': ['py', 'ipynb', 'cpp', 'c', 'java', 'js', 'ts', 'html', 
               'css', 'json', 'xml', 'yml'],
    'instalador': ['exe', 'msi', 'apk', 'dmg', 'pkg'],
    'imagen_disco': ['iso', 'img'],
    'temporal': ['log', 'bak', 'tmp', 'part', 'crdownload']
}

def get_files_path_list(directory_path):
    file_paths_list  = [p for p in glob.glob(directory_path + "**", recursive = True) if os.path.isfile(p)]   
    return file_paths_list

def get_file_extension(file_path):
    return os.path.basename(file).split(".", 1)[1]

def get_document_type(file_path, extensions_type_dict):
    """
    Gets document type comparing the extension to a clasification
    given in a dictionary.
    """
    extension = get_file_extension(file_path)

    for type, extensions in extensions_type_dict.items():
        if extension in extensions:
            return type
        else:
            continue
    
    return extension
    
def is_file_old(file_path, maximum_days = 120):
    """
    Checks if the modification time is greater than 
    the maximum days.
    """
    last_modification = os.path.getmtime(file_path)
    actual_time = time.time()
    days_since_modification = (actual_time - last_modification) / 86400

    if (days_since_modification > maximum_days):
        return True
    else:
        return False

def give_modification_date(file_path):
    """
    Gives the modification date of a file (Year- month-day)
    Returns:
        modification_date_string (String)
    """
    modification_date = datetime.date.fromtimestamp(os.path.getmtime(file))
    modification_date_string = modification_date.strftime("%Y-%m-%d")

    return modification_date_string

def give_new_filename(file_type, file_path, n_image):
    """
    Creates new filename: 
        <type>_<description>_<YYYY-MM-DD>.ext
        For images:
        <type>_<YYYY-MM-DD>.ext
    Returns:
        new_filename (string)
    """
    modification_date = give_modification_date(file_path)

    current_filename = os.path.basename(file_path).split(".")[0]
    extension = get_file_extension(file_path)

    if file_type == "imagen":
        new_filename = f"{file_type}_0{n_image}_{modification_date}.{extension}"
    else:
        new_filename = f"{file_type}_{current_filename}_{modification_date}.{extension}"

    return new_filename

#base_path = "/mnt/c/Users/estev/OneDrive - Universidad Nacional de Colombia/Universidad/02_Física/SemestreVII/IntroducciónCienciasDeLaComputación/Proyecto/"
#origin_path = "Test_folder"

def is_file_for_delete(file_path, reference_name):
    """
    Checks if user wants to delete given file
    Returns:
        flag (Bool)
    """
    print(f"Desea eliminar el archivo {reference_name}")
    flag = int(input("Ingrese 0 para no y 1 para sí: "))
    
    return flag


# Main

base_path = "descargas/"

file_list = get_files_path_list(base_path)

image_counter = 0

for file in file_list:
    file_type = get_document_type(file, extensions_type)

    if file_type == "imagen":
        image_counter += 1

    new_filename = give_new_filename(file_type, file, image_counter)

    if (is_file_old(file)):
      if is_file_for_delete(file, new_filename):
          os.remove(file)
          continue
      else:
        destination_directory = base_path + "old_files" 
    else:
       destination_directory = base_path + file_type

    try:
       os.mkdir(destination_directory)
    except FileExistsError:
       pass   

    shutil.move(file, f"{destination_directory}/{new_filename}")

    try:
       os.rmdir(os.path.dirname(file))
    except OSError as e:
       pass



    
    