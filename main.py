import shutil
import sys
import scan
import normalize
from pathlib import Path
from files_generator import file_generator



def hande_file(path, root_folder, dist):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    path.replace(target_folder/normalize.normalize(path.name))


def handle_archive(path, root_folder, dist):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)

    new_name = normalize.normalize(path.name.replace(".zip", ''))

    archive_folder = root_folder / new_name
    archive_folder.mkdir(exist_ok=True)

    try:
        shutil.unpack_archive(str(path.resolve()), str(path.resolve()))
    except shutil.ReadError:
        archive_folder.rmdir()
        return
    except FileNotFoundError:
        archive_folder.rmdir()
        return
    path.unlink()


def remove_empty_folders(path):
    for item in path.iterdir():
        if item.is_dir():
            remove_empty_folders(item)
            try:
                item.rmdir()
            except OSError:
                pass


def get_folder_objects(root_path):
    for folder in root_path.iterdir():
        if folder.is_dir():
            remove_empty_folders(folder)
            try:
                folder.rmdir()
            except OSError:
                pass

def main(folder_path):
    scan.scan(folder_path)

    for file in scan.jpeg_files:
        hande_file(file, folder_path, "JPEG")

    for file in scan.jpg_files:
        hande_file(file, folder_path, "JPG")

    for file in scan.png_files:
        hande_file(file, folder_path, "PNG")

    for file in scan.svg_files:
        hande_file(file, folder_path, "SVG")

    for file in scan.avi_files:
        hande_file(file, folder_path, "AVI")    

    for file in scan.mp4_files:
        hande_file(file, folder_path, "MP4")

    for file in scan.mov_files:
        hande_file(file, folder_path, "MOV")

    for file in scan.mkv_files:
        hande_file(file, folder_path, "MKV")

    for file in scan.doc_files:
        hande_file(file, folder_path, "DOC")

    for file in scan.txt_files:
        hande_file(file, folder_path, "TXT")

    for file in scan.docx_files:
        hande_file(file, folder_path, "DOCX")
        
    for file in scan.xlsx_files:
        hande_file(file, folder_path, "XLSX")

    for file in scan.pdf_files:
        hande_file(file, folder_path, "PDF")

    for file in scan.pptx_files:
        hande_file(file, folder_path, "PPTX")

    for file in scan.mp3_files:
        hande_file(file, folder_path, "MP3")

    for file in scan.ogg_files:
        hande_file(file, folder_path, "OGG")
                
    for file in scan.wav_files:
        hande_file(file, folder_path, "WAV")
        
    for file in scan.amr_files:
        hande_file(file, folder_path, "AMR")
        
    for file in scan.others:
        hande_file(file, folder_path, "OTHERS")

    for file in scan.archives:
        handle_archive(file, folder_path, "ARCHIVE")

    get_folder_objects(folder_path)

if name == 'main':
    path = sys.argv[1]
    print(f"Start in {path}")

    arg = Path(path)
    file_generator(arg)
    main(arg.resolve())