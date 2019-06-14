import serial
from time import sleep

port = "COM3" #fairly certain this is correct
ser = serial.Serial(port, 38400, timeout=0)

def fullSend():
    thingSent = input()
    ser.write(thingSent)
