#!/usr/bin/python3

import re

# создаем файл с ip и названиями машин
array = []
with open("openvpn-status.log", "r") as my_file:
    raw_data = my_file.readlines()

result = re.findall(r'10\.\d+\.\d+\.\d+\,\w+\-\w+\-\d+', str(raw_data))

for i in result:
    new_string = i.split(',')[1] + ',' + i.split(',')[0] + '\n'
    array.append(new_string)

array = sorted(array)

with open("net.csv", "w") as my_file:
    my_file.writelines(array)

with open("users.csv", "r") as my_users:
    raw_data = my_users.readlines()
print(raw_data)
result = re.findall(r'\w+\s\w+\s\w+\,\w+\,\w+\-\w+\-\d+', str(raw_data))
print(result)
array2 = []
for i in result:
    array2.append(i.lower())
array2 = sorted(array2)

array3 = []
for i in array2:
    for y in array:
        if y.split(',')[0] in i:
            x = i + ',' + y.split(',')[1] + '\n'
            array3.append(x)
with open("net_users.csv", "w") as my_file:
    my_file.writelines(array3)
