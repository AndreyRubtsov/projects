import os
import re

res = os.popen('ping -c 1 10.10.0.12').read()
result = re.findall('ttl3=64', str(res))
if result:
    print(result)

os.mkdir('1')
file_path = '1/test'
with open(file_path, "w") as my_file:
    my_file.writelines('dds')
