import time
import sqlite3
import random
from datetime import datetime

from numpy import insert

def random_variables():
    temp = random.randint(0, 50)
    hum = random.randint(0, 100)
    dust = random.random()
    co2 = random.randint(0, 10000)
    return temp, hum, dust, co2


conn = sqlite3.connect(r'C:/db/IoT.db')
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS MEASUREMENTS")
c.execute("DROP TABLE IF EXISTS DEVICES")

devs = '''CREATE TABLE DEVICES(
    DEVICE INTEGER PRIMARY KEY,
    NAME TEXT NOT NULL
)'''


sql = '''CREATE TABLE MEASUREMENTS(
    DATE TEXT PRIMARY KEY,
    DEVICE_ID INT REFERENCES DEVICES(DEVICE),
    TEMPERATURE INT NOT NULL,
    HUMIDITY INT NOT NULL,
    DUST FLOAT NOT NULL,
    CO2 INT NOT NULL
)'''

# Only run once


print("Created table successfully........")
c.execute(devs)
c.execute(sql)

p1 = "Raspberry_Pi_1"
p2 = "Raspberry_Pi_2"

def new_device(device_name):
    c.execute('INSERT INTO DEVICES(NAME) VALUES (?)', (device_name,))
    print("Inserted device successfully........")

new_device(p1)
new_device(p2)

def create_date():
    date = datetime.now()
    date = date.strftime("%Y-%m-%d %H:%M:%S:%f")
    return date

def insert_data(device_name):
    current_date = create_date()
    device_id = c.execute("SELECT DEVICE FROM DEVICES WHERE NAME = ?", (device_name,)).fetchone()
    temp, hum, dust, co2 = random_variables()
    c.execute('''INSERT INTO MEASUREMENTS(DATE, DEVICE_ID, TEMPERATURE, HUMIDITY, DUST, CO2) 
            VALUES (?, ?, ?, ?, ?, ?)''',
        (current_date, device_id[0], temp, hum, dust, co2))
    print("Inserted data successfully........")

for i in range(1000):
    insert_data(p1)
    time.sleep(0.00001)
    insert_data(p2)
    time.sleep(0.00001)

c.execute("SELECT * FROM MEASUREMENTS")
data = c.fetchall()
print(data)
conn.commit()
conn.close()
