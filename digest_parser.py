from os import listdir
from os.path import join
from docx_to_txt import docx_to_txt, move_to_arch

path = 'Source'
topics = ['ЕКОНОМІКА', 'СОЦІАЛКА', 'ВНУТРІШНЯ ПОЛІТИКА', 'МІЖНАРОДНА БЕЗПЕКА',
                        'МІЖНАРОДНІ ЗВ\'ЯЗКИ (ЗОВНІШНЯ ПОЛІТИКА І ТОРГІВЛЯ)', 'ГУМАНІТАРНІ', 'УКРАЇНСЬКО-РОСІЙСЬКІ',
                        'ОКУПОВАНІ ТЕРИТОРІЇ']
file_list = [f for f in listdir(path) if f.endswith('.docx')]
if file_list:
    docx_to_txt(path)

file_list = [join(path, f) for f in listdir(path) if f.endswith('.txt')]
digest = {}
digest_key = None
for file in file_list:
    with open(file, 'r', encoding='UTF8') as f:
        for line in f:
            line = line.strip()
            if line in topics:
                if digest_key:
                    try:
                        digest[digest_key] = digest[digest_key] + digest_value
                    except KeyError:
                        digest[digest_key] = digest_value
                digest_key = line
                digest_value = []
            else:
                if line:
                    digest_value.append(line)
digest[digest_key] = digest[digest_key] + digest_value

move_to_arch(path)

data_out = []
for key in digest.keys():
    for line in digest[key]:
        data_out.append(line+'\n')
with open('Out/output.txt', 'w', encoding='UTF8') as f:
    f.writelines(data_out)