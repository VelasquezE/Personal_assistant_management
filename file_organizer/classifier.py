import os

EXTENSIONS_TYPE = {
    'documento': ['pdf', 'doc', 'docx', 'odt', 'djvu'],
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

def get_file_extension(file_path):
    #TODO manage names with multiple points 
    return os.path.basename(file_path).split(".", 1)[1]

def get_document_type(file_path):
    """
    Gets document type comparing the extension to a clasification
    given in a dictionary.
    """
    extension = get_file_extension(file_path)

    for type, extensions in EXTENSIONS_TYPE.items():
        if extension in extensions:
            return type
        else:
            continue
    
    return extension