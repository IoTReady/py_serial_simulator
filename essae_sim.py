import sys
import serial
from time import sleep
from random import randint


def send_data(port='/dev/ttyUSB0', baudrate=9600, count=1, sleep_time=1):
    with serial.Serial() as ser:
        ser.baudrate = baudrate
        ser.port = port
        ser.open()
        for i in range(count): 
            weight = randint(0,6000)
            weight_kg = weight/1000.0
            data = f"{weight_kg} kg\n"
            print(data)
            ser.write(data.encode('utf-8'))
            sleep(sleep_time)


if __name__=='__main__':
    try:
        port = sys.argv[1]
    except:
        port = '/dev/ttyUSB0'
    try:
        baudrate = int(sys.argv[2])
    except:
        baudrate = 9600
    try:
        count = int(sys.argv[3])
    except:
        count = 10
    try:
        sleep_time = float(sys.argv[4])
    except:
        sleep_time = 1
    send_data(port,baudrate,count,sleep_time)
