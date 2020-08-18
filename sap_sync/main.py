#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request,urllib.error
import os.path
from datetime import datetime, timedelta
import shutil
import fileinput


local_path = '/var/www/srv-spb-010/sap/10.1.0.228'
url = 'http://10.1.0.228/mirror'
period = 365

dirs = ('/kaz/', '/dir/', '/ukr/', '/rus/', '/bel/', '/sha/')
const_local_path = '/var/www/srv-spb-010/sap/'
const_files = ['http://10.1.0.228/mirror/Open_Orders_Reports/BEL_Open_Orders_New.xls',\
               'http://10.1.0.228/mirror/Open_Orders_Reports/DIR_Open_Orders_New.xls',\
               'http://10.1.0.228/mirror/Open_Orders_Reports/KAZ_Open_Orders_New.xls',\
               'http://10.1.0.228/mirror/Open_Orders_Reports/RUS_Open_Orders_New.xls',\
               'http://10.1.0.228/mirror/Open_Orders_Reports/UKR_KOU_Open_Orders_New.xls',\
               'http://10.1.0.228/mirror/Accounts_Receivable_Rosneft/E03-1.Accounts_Receivable_Rosneft.xls',\
               'http://10.1.0.228/mirror/Supplier_Payment_Terms_Report/010.Supplier_Payment_Terms.xls']

def download_file(path_from, path_to):

    global local_path
    global url

    path_to = path_to.replace('%20',' ').replace('%25','%')
    # create dir if absent
    if not os.path.isfile(path_to):
        os.makedirs(os.path.dirname(path_to), exist_ok=True)
    try:
      with urllib.request.urlopen(path_from) as response, open(path_to, 'wb') as file_download:
        shutil.copyfileobj(response, file_download)
        print('Success'.ljust(40, '.'), path_to)
    except IsADirectoryError:
        for file in files_links(path_from):
            download_file(url + file, local_path + file)
    except Exception as e:
        print('download_file:', e)
        print(path_to)

def folders_links(root_folder):

    folders = []
    with urllib.request.urlopen(root_folder) as root_content:
        links = BeautifulSoup(root_content, "lxml")

    for link in links.findAll('a')[1:]:
        folder = link.get('href')
        sub_folder = os.path.split(os.path.dirname(folder))[1]

        if folder.endswith('web.config'):
            continue
        folders.append(root_folder + sub_folder + '/')

    return folders

def files_links(folder):

    files = []
    global local_path
    global period

    old_date = datetime.today() - timedelta(days=period)
    try:
        with urllib.request.urlopen(folder) as folder_content:
            links = BeautifulSoup(folder_content, "lxml")
    except Exception as e:
        print('file_links:', e)
        print('folder:', folder)
        return

    for link in links.findAll('a')[1:]:
        file = link.get('href')
        if file.endswith(('.msg', '.log')):
            continue
        file = file.replace('/mirror', '')
        full_local_path = local_path + file.replace('%20', ' ').replace('%25', '%')
        date_file_str = link.previous[:10].strip()
        date_file = datetime.strptime(date_file_str, '%m/%d/%Y')
        # check file's date and Availability
        if old_date < date_file and not os.path.isfile(full_local_path):
            files.append(file)

    return files

# 3. download const files
print('____________ const files _____________')
for c_file in const_files:
    download_file(c_file, const_local_path + os.path.basename(c_file))



for dir in dirs:
    try:
        full_path = url + dir
        full_local_path = local_path + dir
        print('____________', dir, '_____________')
        # 1. download index.html
        download_file(full_path, full_local_path + 'index.html')
        # edit index.html (replace '/mirror')
        with fileinput.FileInput(full_local_path + 'index.html', inplace=True, backup='.bak') as index_file:
            for line in index_file:
                print(line.replace('/mirror', ''), end='')
        for folder in folders_links(full_path):
            for file in files_links(folder):
                # 2. download absent files
                download_file(url + file, local_path + file)

    except Exception as e:
        print(e)
        print('dir', dir)
