import sys
from pathlib import Path


jpeg_files = list()
png_files = list()
jpg_files = list()
svg_files = list()
avi_files = list()
mp4_files = list()
mov_files = list()
mkv_files = list()
doc_files = list()
docx_files = list()
txt_files = list()
pdf_files = list()
xlsx_files = list()
pptx_files = list()
mp3_files = list()
ogg_files = list()
wav_files = list()
amr_files = list()
folders = list()
archives = list()
others = list()
unknown = set()
extensions = set()

registered_extensions = {
    "JPEG": jpeg_files,
    "PNG": png_files,
    "JPG": jpg_files,
    "SVG": svg_files,
    "AVI": avi_files,
    "MP4": mp4_files,
    "MOV": mov_files,
    "MKV": mkv_files,
    "DOC": doc_files,
    "DOCX": docx_files,
    "TXT": txt_files,
    "PDF": pdf_files,
    "XLSX": xlsx_files,
    "PPTX": pptx_files,
    "MP3": mp3_files,
    "OGG": ogg_files,
    "WAV": wav_files,
    "AMR": amr_files,
    "ZIP": archives,
    "GZ": archives,
    "TAR": archives
}


def get_extensions(file_name):
    return Path(file_name).suffix[1:].upper()


def scan(folder):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ("JPEG", "PNG", "JPG", "SVG", "AVI", "MP4", "MOV", "MKV", "DOC", "DOCX", "TXT", "PDF", "XLSX", "PPTX", "MP3", "OGG", "WAV", "AMR", "ZIP", "GZ", "TAR", "OTHER", "ARCHIVE"):
                folders.append(item)
                scan(item)
            continue

        extension = get_extensions(file_name=item.name)
        new_name = folder/item.name
        if not extension:
            others.append(new_name)
        else:
            try:
                container = registered_extensions[extension]
                extensions.add(extension)
                container.append(new_name)
            except KeyError:
                unknown.add(extension)
                others.append(new_name)


if __name__ == 'main':
    path = sys.argv[1]
    print(f"Start in {path}")

    arg = Path(path)
    scan(arg)

    print(f"jpeg: {jpeg_files}\n")
    print(f"png: {png_files}\n")
    print(f"jpg: {jpg_files}\n")
    print(f"svg: {svg_files}\n")
    print(f"avi: {avi_files}\n")
    print(f"mp4: {mp4_files}\n")
    print(f"mov: {mov_files}\n")
    print(f"mkv: {mkv_files}\n")
    print(f"doc: {doc_files}\n")
    print(f"docx: {docx_files}\n")
    print(f"txt: {txt_files}\n")
    print(f"pdf: {pdf_files}\n")
    print(f"xlsx: {xlsx_files}\n")
    print(f"pptx: {pptx_files}\n")
    print(f"mp3: {mp3_files}\n")
    print(f"ogg: {ogg_files}\n")
    print(f"wav: {wav_files}\n")
    print(f"amr: {amr_files}\n")
    print(f"archive: {archives}\n")
    print(f"unknown: {others}\n")
    print(f"All extensions: {extensions}\n")
    print(f"Unknown extensions: {unknown}\n")