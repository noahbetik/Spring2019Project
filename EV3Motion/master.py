#!/usr/bin/env python3

from ev3dev2.motor import *
from time import sleep
from pixelPID import PID
from trigger import buttonBop
import socket

HOST = ''
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
targetState = False
offsetSpin, offsetLift = 0, 0   #prototyping code for now, will actually pull offset angle from vision tracking

sock =  socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

spinAction = PID(0.3, 0.25, 0, 0, 0, LargeMotor(OUTPUT_A))
liftAction = PID(0.3, 0.25, 0, 0, 0, LargeMotor(OUTPUT_B))

def receive():
    while True:
        data, addr = sock.recvfrom(1024)
        data = data.decode('utf-8')
        if data == "q":
                sock.close()
                break
        print (data) # one two testing
        offsetSpin, offsetLift = map(int, data.split())
        print (offsetSpin, "/n", offsetLift) # proto proto code


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
