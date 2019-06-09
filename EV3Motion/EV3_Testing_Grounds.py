#!/usr/bin/env python3

from ev3dev2.motor import *
from time import sleep
m = LargeMotor(OUTPUT_A)
angle = 16 #example value, pulls actual angle offset from Pi vision
encoderPos, newPos, adjustment, previousError, errorSum = 0, 0, 0, 0, 0
KP, KD, KI = 0.2, 0.1, 0.05
m.stop_action = 'coast'
feedForward, outputSpeed = 0, 0
setPoint = int(input()) # setPoint will likely just be 0 (as offset angle = 0 means turret is aligned)

while True:
    encoderPos = m.position

    while (encoderPos != setPoint):
        encoderPos = m.position
        error = setPoint - encoderPos
        adjustment = (error * KP) + (previousError * KD) + (errorSum * KI)
        outputSpeed = feedForward + adjustment
        #outputSpeed = max(min(175, outputSpeed), 0)
        if (outputSpeed > 175):
            outputSpeed = 175
        if (outputSpeed < -175):
            outputSpeed = -175
        previousError = error
        errorSum += error
        m.on(SpeedRPM(outputSpeed))
        print(m.position)

    #outputSpeed = 0

