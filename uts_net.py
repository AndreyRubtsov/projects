#!/usr/bin/python3
import re

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
