#!/usr/bin/env python3

from ev3dev2.motor import *
from ev3dev2.sound import *

bop = LargeMotor(OUTPUT_C)

def buttonBop():
    bop.position_sp = 180
    bop.run_to_abs_pos()
    bop.position_sp = 0
    bop.run_to_abs_pos()
    #Sound.play_file()   need to download a .wav file
    print("pew pew mofo")
