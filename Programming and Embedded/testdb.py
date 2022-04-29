import sqlite3
import random

temp = 20
hum = 50
dust = 0.1
co2 = 10

def random_variables():
    temp = random.randint(0, 50)
    hum = random.randint(0, 100)
    dust = random.random()
    co2 = random.randint(0, 10000)
    return temp, hum, dust, co2


conn = sqlite3.connect(r'C:/db/tttest.db')
c = conn.cursor()

sql = '''CREATE TABLE MEASUREMENTS(
   TEMPERATURE INT NOT NULL,
   HUMIDITY INT NOT NULL,
    DUST FLOAT NOT NULL,
    CO2 INT NOT NULL
)'''

c.execute(sql)
print("Created table successfully........")
# conn.commit()

sql2 = '''CREATE TABLE DEVICES(
    DEVICE_ID INTEGER PRIMARY KEY
'''

add_keys = '''ALTER TABLE MEASUREMENTS ADD FOREIGN KEY (DEVICE_ID) INTEGER REFERENCES DEVICES(DEVICE_ID)'''

c.execute(sql2)

c.execute()

def device1data():
    dev1_id = 1
    for i in range(1000):
        temp, hum, dust, co2 = random_variables()
        c.execute('''INSERT INTO MEASUREMENTS(DEVICE_ID, TEMPERATURE, HUMIDITY, DUST, CO2) 
                VALUES (?, ?, ?, ?, ?)''',
            (dev1_id, temp, hum, dust, co2))
        print("Inserted data successfully........")
    conn.commit()

def device2data():
    dev2_id = 2
    for i in range(1000):
        temp, hum, dust, co2 = random_variables()
        c.execute('''INSERT INTO MEASUREMENTS(DEVICE_ID, TEMPERATURE, HUMIDITY, DUST, CO2) 
                VALUES (?, ?, ?, ?, ?)''',
            (dev2_id, temp, hum, dust, co2))
        print("Inserted data successfully........")
    conn.commit()

device1data()
device2data()

c.execute("SELECT * FROM MEASUREMENTS")
data = c.fetchall()
print(data)
conn.commit()