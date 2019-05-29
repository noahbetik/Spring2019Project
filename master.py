from ev3dev2.motor import *
from time import sleep
from PID import PID

targetState = False


spinAction = PID(0.3, 0.25, 0, 0, LargeMotor(OUTPUT_A))
liftAction = PID(0.3, 0.25, 0, 0, LargeMotor(OUTPUT_B))

while True:

    while (targetState == False):
        spinAction.search()

    if (targetState == True):
        liftAction.pos()
        spinAction.pos()


# need some vision/motion integration to change targetState
# also need to provide spinAction and liftAction with setPoint values
# setPoint may need to be calculated from an angle offset given by vision
# thread-splitting to run spinAction and liftAction at the same time???

#yippity yote, get off of my goat



