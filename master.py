#!/usr/bin/env python3

from ev3dev2.motor import *
from time import sleep
from PID import PID
from trigger import buttonBop

targetState = True
#errorAngle = int(input())   prototyping code for now, will actually pull offset angle from vision tracking

spinAction = PID(0.3, 0.25, 0, 0, 0, LargeMotor(OUTPUT_A))
liftAction = PID(0.3, 0.25, 0, 0, 0, LargeMotor(OUTPUT_B))

while True:

    if (targetState == False):
        spinAction.search()

    elif (targetState == True):
        spinAction.pos()
        liftAction.pos()
        if errorAngle == 0:
            buttonBop()
            targetState = False

    else:
        spinAction.worldHasEnded()




# need some vision/motion integration to change targetState
# also need to provide spinAction and liftAction with setPoint values
# setPoint may need to be calculated from an angle offset given by vision
# thread-splitting to run spinAction and liftAction at the same time???

#yippity yote, get off of my goat



