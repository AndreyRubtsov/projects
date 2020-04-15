#!/usr/bin/python3
import re
import os

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

# считываем инфо о пользователях и сортируем их
with open("users.csv", "r") as my_users:
    raw_data = my_users.readlines()

result = re.findall(r'\w+\s\w+\s\w+\,\w+\,\w+\-\w+\-\d+', str(raw_data))

array2 = []
for i in result:
    array2.append(i.lower())
array2 = sorted(array2)

# сравниваем два массива, запись результата
array3 = []
for i in array2:
    for y in array:
        if y.split(',')[0] in i:
            x = i + ',' + y.split(',')[1] + '\n'
            array3.append(x)
with open("net_users.csv", "w") as my_file:
    my_file.writelines(array3)

# создаем реммина файлы
for i in array3:
    ping_string = 'ping -c 1 ' + i.rstrip().split(',')[3]
    ping_result = os.popen(ping_string).read()
    result = re.findall('ttl=\d{2}', str(ping_result))
    if result:
        file_name = '1/vpn_group_vnc_' + i.split(',')[1] + '.remmina'
        user_name = i.split(',')[0]
        comp_name = i.split(',')[3]
        remmina_data = "[remmina]\n" \
                       "shareparallel=0\n" \
                       "window_width=640\n" \
                       "disableclipboard=0\n" \
                       "serialpath=\n" \
                       "disable_fastpath=0\n" \
                       "disablepasswordstoring=0\n" \
                       "disableserverinput=0\n" \
                       "viewmode=4\n" \
                       "shareserial=0\n" \
                       "parallelname=\n" \
                       "password=.\n" \
                       "gwtransp=http\n" \
                       "sharesmartcard=0\n" \
                       "old-license=0\n" \
                       "shareprinter=0\n" \
                       "ssh_tunnel_loopback=0\n" \
                       "resolution_height=0\n" \
                       "ssh_auth=\n" \
                       "group=vpn\n" \
                       "enable-autostart=0\n" \
                       "smartcardname=\n" \
                       "ssh_tunnel_enabled=0\n" \
                       "domain=uts-spb\n" \
                       "serialname=\n" \
                       "ignore-tls-errors=1\n" \
                       "ssh_tunnel_auth=2\n" \
                       "loadbalanceinfo=\n" \
                       "last_success=20200130\n" \
                       "ssh_tunnel_server=\n" \
                       "clientname=\n" \
                       "sound=off\n" \
                       "ssh_server=\n" \
                       "resolution_mode=1\n" \
                       "security=\n" \
                       "protocol=VNC\n" \
                       "relax-order-checks=0\n" \
                       "gateway_username=\n" \
                       "name=" + user_name + "\nssh_privatekey=\n" \
                                             "window_maximize=1\n" \
                                             "showcursor=0\n" \
                                             "ssh_tunnel_password=\n" \
                                             "postcommand=\n" \
                                             "quality=9\n" \
                                             "username=\n" \
                                             "gateway_usage=0\n" \
                                             "window_height=480\n" \
                                             "resolution_width=0\n" \
                                             "ssh_tunnel_privatekey=\n" \
                                             "console=0\n" \
                                             "ssh_username=\n" \
                                             "gateway_server=\n" \
                                             "viewonly=0\n" \
                                             "microphone=0\n" \
                                             "proxy=\n" \
                                             "disableautoreconnect=0\n" \
                                             "keyboard_grab=0\n" \
                                             "ssh_tunnel_passphrase=\n" \
                                             "glyph-cache=0\n" \
                                             "ssh_tunnel_username=\n" \
                                             "serialpermissive=0\n" \
                                             "disableencryption=0\n" \
                                             "ssh_charset=\n" \
                                             "execpath=\n" \
                                             "cert_ignore=0\n" \
                                             "exec=\n" \
                                             "parallelpath=\n" \
                                             "keymap=\n" \
                                             "printer_overrides=\n" \
                                             "serialdriver=\n" \
                                             "precommand=\n" \
                                             "server=" + comp_name + "\nuseproxyenv=0\n" \
                                                                     "colordepth=32\n" \
                                                                     "gateway_domain=\n" \
                                                                     "ssh_loopback=\n" \
                                                                     "sharefolder="
        with open(file_name, "w") as my_file:
            my_file.writelines(remmina_data)
