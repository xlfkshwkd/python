import pymysql
import Adafruit_DHT
import time
import datetime

pin =4
sensor = Adafruit_DHT.DHT11

while True:
    db = pymysql.connect(host="localhost",
                        user='raspi_user',
                        password='1234',
                        db="raspi_db",
                        charset="utf8")

    cursor = db.cursor(pymysql.cursors.DictCursor)

    h, t = Adafruit_DHT.read_retry(sensor, pin)
    now = datetime.datetime.today()
    print(now)
    date_str = now.strftime("%Y-%m-%d %H:%M:%S")
    print(date_str)
    h = str(h)
    t = str(t)

    cursor.execute('use raspi_db;')
    cursor.execute('INSERT INTO collect_data (sensor,collect_time,value1,value2) VALUES("temp&hum",%s,%s,%s);',(date_str,h,t))

    cursor.execute('select * from collect_data;')
    value = cursor.fetchall()

    # print(value)
    # print(type(value))

    db.commit()
    db.close()

    time.sleep(5)