#!/usr/bin/python3
import psycopg2, random, subprocess

con = psycopg2.connect(
    database="fusionpbx",
    user="fusionpbx",
    password="otOhLFpCU0ggzRuehRexwG3cY",
    host="10.0.3.32",
    port="5432"
)

cur = con.cursor()

conf_pin = random.randint(1000, 9999)

cur.execute('update v_conferences set conference_pin_number=' + str(conf_pin) + ';')

con.commit()
con.close()

with open("pin_number", "w") as my_file:
    my_file.write(str(conf_pin))

subprocess.call("scp pin_number root@10.0.0.110:/var/www/srv-spb-010/", shell=True, stdout=None)
