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

def get_extension(file_path):
    return os.path.basename(file).split(".", 1)[1]

def get_document_type(file_path, extensions_type_dict):
    """
    Gets document type comparing the extension to a clasification
    given in a dictionary.
    """
    extension = get_extension(file_path)

    for type, extensions in extensions_type_dict.items():
        if extension in extensions:
            return type
        else:
            continue
    
    return extension
    

def is_file_old(file_path, maximum_days = 120):
    """
    Checks if the last modification time is greater than 
    the maximum days.
    """
    last_modification = os.path.getmtime(file_path)
    actual_time = time.time()
    days_since_modification = (actual_time - last_modification) / 86400

    if (days_since_modification > maximum_days):
        return True
    else:
        return False

def give_new_filename(file_type, file_path):
    """
    Creates new filename: 
        <type>_<description>_<YYYY-MM-DD>.ext
    Returns:
        new_filename (string)
    """
    creation_date = datetime.date.fromtimestamp(os.path.getctime(file))
    creation_date_string = creation_date.strftime("%Y-%m-%d")

    current_filename = os.path.basename(file_path).split(".")[0]
    extension = get_extension(file_path)

    if file_type == "imagen":
        new_filename = f"{file_type}_{creation_date_string}.{extension}"
        #TODO:definir un contador para imagenes del mismo día
    else:
        new_filename = f"{file_type}_{current_filename}_{creation_date_string}.{extension}"

    return new_filename

#base_path = "/mnt/c/Users/estev/OneDrive - Universidad Nacional de Colombia/Universidad/02_Física/SemestreVII/IntroducciónCienciasDeLaComputación/Proyecto/"
#origin_path = "Test_folder"

base_path = "Test_folder/"

file_list = [p for p in glob.glob(base_path + "**", recursive = True) if os.path.isfile(p)]

for file in file_list:
    file_type = get_document_type(file, extensions_type)

    if (is_file_old(file)):
      destination_directory = base_path + "old_files" 
    else:
       destination_directory = base_path + file_type
    
    try:
       os.mkdir(destination_directory)
    except FileExistsError:
       pass  
    
    new_filename = give_new_filename(file_type, file)

    shutil.move(file, f"{destination_directory}/{new_filename}")

    try:
       os.rmdir(os.path.dirname(file))
    except OSError as e:
       pass

    
    