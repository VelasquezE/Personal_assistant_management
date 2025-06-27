import os
import shutil
from . import filedate
from . import classifier
from . import utils

# Renaming files function for download folder (generic organization)

def give_new_filename(file_type, file_path, n_image):
    """
    Creates new filename: 
        <type>_<description>_<YYYY-MM-DD>.ext
        For images:
        <type>_<YYYY-MM-DD>.ext
    Returns:
        new_filename (string)
    """
    modification_date = filedate.give_modification_date(file_path)

    current_filename = os.path.basename(file_path).split(".")[0]
    extension = classifier.get_file_extension(file_path)

    if file_type == "imagen":
        new_filename = f"{file_type}_0{n_image}_{modification_date}.{extension}"
    else:
        new_filename = f"{file_type}_{current_filename}_{modification_date}.{extension}"

    return new_filename

# Downloads folder organizer

def organize_download_folder(download_folder_path):
    file_list = utils.get_files_path_list(download_folder_path)

    image_counter = 0

    for file in file_list:
        file_type = classifier.get_document_type(file)

        if file_type == "imagen":
            image_counter += 1

        new_filename = give_new_filename(file_type, file, image_counter)

        if (filedate.is_file_old(file)):
          if utils.is_file_for_delete(file, new_filename):
              os.remove(file)
              continue
          else:
            destination_directory = download_folder_path + "old_files" 
        else:
           destination_directory = download_folder_path + file_type

        try:
           os.mkdir(destination_directory)
        except FileExistsError:
           pass   

        shutil.move(file, f"{destination_directory}/{new_filename}")

        try:
           os.rmdir(os.path.dirname(file))
        except OSError as e:
           pass
