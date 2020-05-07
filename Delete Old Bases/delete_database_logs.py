import re
import os
import shutil
print('sd')
# считываем список
with open("1CV8Clst.lst", "r") as file_base_list:
    raw_data = file_base_list.readlines()
print(raw_data)
database_names = re.findall(r'\w{8}-\w{4}-\w{4}-\w{4}-\w{12}', str(raw_data))
sorted(database_names)
for database_name in database_names:
    print(database_name)

# считываем директорию
files_list = re.findall(r'\w{8}-\w{4}-\w{4}-\w{4}-\w{12}', str(os.listdir()))
for i in files_list:
    if i not in database_names:
        shutil.rmtree(i)
