#!/usr/bin/env python3

import serial
from time import sleep

port = "/dev/ttyUSB0" #example port, update once found
ser = serial.Serial(port, 38400, timeout=0)

def receive():
    data = ser.read(9999)
    if len(data) > 0:
        offsetSpin, offsetLift = data.split()
        print (offsetSpin, offsetLift)
        #targetState = True
    else:
        print ("no target received")

ser.close()

while True:
    receive()
