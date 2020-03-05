import psycopg2, random

con = psycopg2.connect(
  database="fusionpbx",
  user="fusionpbx",
  password="mzLZqOwcUjA67vUHdwArjYpomc",
  host="192.168.122.11",
  port="5432"
)
print("Database opened successfully")

cur = con.cursor()

conf_pin =random.randint(1000, 9999)

cur.execute(f'update v_conferences set conference_pin_number={conf_pin};')
con.commit()
print("Record inserted successfully")
con.close()

with open("/tmp/pin_number","w") as my_file:
    my_file.write(str(conf_pin))


