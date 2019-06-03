#!/usr/bin/env python3

from ev3dev2.motor import *
from time import sleep

class PID:

    def __init__ (self, KP, KD, KI, setPoint, errorAngle, m):
        self.KP = KP
        self.KD = KD
        self.KI = KI
        self.setPoint = setPoint
        self.previousError = 0
        self.errorSum = 0
        self.outputSpeed = 0
        self.errorAngle = errorAngle
        self.m = m


    def pos(self):
        #self.setPoint = int(input())   prototyping code
        encoderPos = self.m.position
        self.setPoint = encoderPos - self.errorAngle
        self.m.stop_action = 'coast'
        while (encoderPos != self.setPoint):
            encoderPos = self.m.position
            error = self.setPoint - encoderPos
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
        if (self.m.position >= 0):
            self.m.on(SpeedRPM(30))
        elif (self.m.position <= 360):
            self.m.on(SpeedRPM(-30))

    def worldHasEnded(self):
        self.m.on(SpeedRPM(175))
        print("THE WORLD HAS ENDED")

#yippity yee, get out of my tree
