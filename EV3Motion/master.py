#!/usr/bin/env python3

from ev3dev2.motor import *
from time import sleep
from pixelPID import PID
from trigger import buttonBop
import serial

targetState = False
offsetSpin, offsetLift = 0, 0   #prototyping code for now, will actually pull offset angle from vision tracking
port = "\\\\.\\CNCA0" #example port, update once found
ser = serial.Serial(port, 38400, timeout=0)

spinAction = PID(0.3, 0.25, 0, 0, 0, LargeMotor(OUTPUT_A))
liftAction = PID(0.3, 0.25, 0, 0, 0, LargeMotor(OUTPUT_B))

def receive():
    data = ser.read(9999)
    if len(data) > 0:
        offsetSpin, offsetLift = data.split()
        print (offsetSpin, offsetLift)
        targetState = True
    else:
        print ("no target received")

while True:

    if (targetState == False):
        spinAction.search()
        receive()

    elif (targetState == True):
        while targetState == True:
            receive()
            spinAction.pos(offsetSpin)
            liftAction.pos(offsetLift)
            receive()
            if offsetSpin == 0 and offsetLift == 0:
                buttonBop()
                targetState = False

    else:
        spinAction.worldHasEnded()
        ser.close
