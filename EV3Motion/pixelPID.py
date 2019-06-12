#!/usr/bin/env python3

from ev3dev2.motor import *
from time import sleep
import serial

class PID:

    def __init__ (self, KP, KD, KI, setPoint, offset, m):
        self.KP = KP
        self.KD = KD
        self.KI = KI
        self.setPoint = setPoint
        self.previousError = 0
        self.errorSum = 0
        self.outputSpeed = 0
        self.offset = offset
        self.m = m

    def pos(self, offset):
        #self.setPoint = int(input())   prototyping code
        encoderPos = self.m.position
        self.setPoint = offset
        self.m.stop_action = 'coast'
        if self.setPoint != 0:
            error = self.setPoint
            self.outputSpeed = (error * self.KP) + (self.previousError * self.KD) + (self.errorSum * self.KI)
            if (self.outputSpeed > 175):
                self.outputSpeed = 175
            if (self.outputSpeed < -175):
                self.outputSpeed = -175
            self.previousError = error
            self.errorSum += error
            self.m.on(SpeedRPM(self.outputSpeed))
            print(self.m.position)

    def search(self):
        if (0 <= self.m.position <= 360):
            self.m.on(SpeedRPM(30))
        elif (self.m.position <= 360):
            self.m.on(SpeedRPM(-30))

    def worldHasEnded(self):
        self.m.on(SpeedRPM(175))
        print("THE WORLD HAS ENDED")

#yippity yee, get out of my tree
