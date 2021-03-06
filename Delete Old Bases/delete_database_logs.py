import re
import os
import shutil

PATH = 'C:\\Program Files\\1cv8\\srvinfo\\reg_1541'
os.chdir(PATH)

# считываем список
with open("1CV8Clst.lst", "r") as file_base_list:
    raw_data = file_base_list.readlines()
database_names = re.findall(r'\w{8}-\w{4}-\w{4}-\w{4}-\w{12}', str(raw_data))

# считываем директорию и удаляем лишнии папки
files_list = re.findall(r'\w{8}-\w{4}-\w{4}-\w{4}-\w{12}', str(os.listdir()))
for i in files_list:
    if i=='snccntxaa36abcb-4824-400c-9b73-bde43f1c83e3' or 'snccntx56b084d5-0467-429c-9830-227354e8f1f4':
        pass
    else:
        if i not in database_names:
            shutil.rmtree(i)
            print(i)
