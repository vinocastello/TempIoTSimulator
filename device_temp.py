import mysql.connector
import argparse
import datetime
import random
from tabulate import tabulate
import time
import weather

SEND_INTERVAL = 3
# Location of UP AECH
LOCATION = (14.648900271585852, 121.06881775671476)

mydb = mysql.connector.connect(
    host = "localhost",
    user="root",
    password="cs198eth2",
    database="cs198trad"
)

mycursor = mydb.cursor()

# field_names = [i[0] for i in mycursor.description]
# field_names = mycursor.column_names
field_names = ["deviceID","timestamp","temperature"]

def get_random_float():
    start = random.randint(1,100)
    end = random.randint(1,100)

    if start == end:
        end += 1
    elif start > end:
        start,end = end,start

    return random.uniform(start,end)

def insert_random_data(deviceID):
    weather_reading = weather.get_weather(LOCATION)
    time = weather_reading.timestamp
    # str_time = time.strftime('%Y-%m-%d %H:%M:%S')
    sql = f"INSERT INTO devices_temp (deviceID, timestamp, temperature) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE timestamp = %s, temperature = %s;"
    val = (deviceID,time,weather_reading.random_temp,time,weather_reading.random_temp)
    sql2 = f"INSERT INTO all_temps (deviceID, timestamp, temperature) VALUES (%s, %s, %s);"
    val2 = (deviceID,time,weather_reading.random_temp)
    mycursor.execute(sql,val)
    mycursor.execute(sql2,val2)
    mydb.commit()
    table = [field_names,list(val2)]
    print(tabulate(table))
    print(mycursor.rowcount,"record inserted")

def read_latest(deviceID):
    # sql = '''SELECT * FROM gpsdata
    # ORDER BY timestamp DESC LIMIT 1;'''
    sql = f'''SELECT * FROM devices_temp
    WHERE deviceID = {deviceID};'''
    mycursor.execute(sql)
    result = mycursor.fetchone()
    if result == None:
        print("You do not have any data yet!")
    else:
        print("latest temp data:")
        table = [field_names,[result[0],result[1],result[2]]]
        print(tabulate(table))

def read_all():
    sql = '''SELECT * FROM all_temps
    ORDER BY timestamp DESC;'''
    mycursor.execute(sql)
    result = mycursor.fetchall()
    print(f"all temperature readings:")
    table = [field_names]
    for x in result:
        table.append([x[0],x[1],x[2]])
    print(tabulate(table))

def continous_send(deviceID):
    while True:
        insert_random_data(deviceID)
        time.sleep(SEND_INTERVAL)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', metavar='choice', type=str, required=True)
    parser.add_argument('-d',metavar='deviceID',type=int,required=True)
    args = parser.parse_args()
    choice = args.c.lower()
    deviceID = args.d
    if choice == "send" or choice == "1" or choice == "s":
        continous_send(deviceID)
    elif choice == "read_latest" or choice == "2" or choice == "l":
        read_latest(deviceID)
    elif choice == "read_all" or choice == "3" or choice == "a":
        read_all()
    else:
        print(f"Incorrect arguments!")

if __name__ == '__main__':
    main()
