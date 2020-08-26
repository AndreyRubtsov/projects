import os
import requests
import sys
from bs4 import BeautifulSoup
import colorama
from colorama import Fore, Back, Style

colorama.init()

my_dir = str(sys.argv[1])
if not os.path.exists(my_dir):
    os.makedirs(my_dir)


def save_to_file(dir, data):
    file_name = dir.split('.')[0]
    with open(my_dir + '/' + file_name, 'w') as f:
        f.write(data)


my_stack = []
while True:
    url = input()

    if url == 'exit':
        break
    elif url == 'back':
        url = my_stack.pop()
        url = my_stack.pop()
    elif '.' not in url:
        print('Input error!')
        continue

    r = requests.get('http://' + url)
    # print(r.text)
    soup = BeautifulSoup(r.content, 'html.parser')
    print('*' * 150)
    # print(soup.prettify())
    text = soup.get_text()
    print(Fore.BLUE+text)

    save_to_file(url, data=text)
    my_stack.append(url)
