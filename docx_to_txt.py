from os import listdir, rename
from os.path import join, split
from extractdocx import get_docx_text

path = 'Source'

def docx_to_txt(path):
    file_list = [join(path, f) for f in listdir(path) if f.endswith('.docx')]

    for file in file_list:
        out_to_txt = get_docx_text(file)
        with open(file.replace('.docx', '.txt'), 'w', encoding='UTF-8') as f:
            f.write(out_to_txt)
    move_to_arch(path, mask=('.docx', ))

def move_to_arch(path, mask=('.docx', '.txt')):
    file_list = [join(path, f) for f in listdir(path) if f.endswith(mask)]
    for file in file_list:
        rename(file, 'Arch\\'+split(file)[1])


if __name__ == "__main__":
    docx_to_txt(path)
