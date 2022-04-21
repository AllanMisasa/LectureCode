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
   DEVICE_ID INTEGER PRIMARY KEY,
   TEMPERATURE INT NOT NULL,
   HUMIDITY INT NOT NULL,
    DUST FLOAT NOT NULL,
    CO2 INT NOT NULL
)'''

# c.execute(sql)
print("Created table successfully........")
# conn.commit()

for i in range(1000):
    temp, hum, dust, co2 = random_variables()
    c.execute('''INSERT INTO MEASUREMENTS(TEMPERATURE, HUMIDITY, DUST, CO2) 
            VALUES (?, ?, ?, ?)''',
         (temp, hum, dust, co2))
    print("Inserted data successfully........")

c.execute("SELECT * FROM MEASUREMENTS")
data = c.fetchall()
print(data)
conn.commit()