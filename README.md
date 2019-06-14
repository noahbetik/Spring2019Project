# Spring 2019 Project
Independent engineering design project for spring 2019, with goal of creating a turret that has two degrees of freedom to acquire a target and launch a projectile. The main hardware used is a LEGO EV3 kit and a Raspberry Pi 3B, and the project is coded entirely in Python 3.

OpenCV is used to acquire the target, which is done by measuring the pixel offset between the centre of the target and the centre of the camera feed. At this point, a UDP connection sends a pixel offset value for the spin and lift values from the Pi to the EV3. A custom PID loop on the Pi takes continuous input from the UDP connection to modify the speed value of each motor in order to move the turret to position.  

Using the EV3 requires the EV3Dev2 library; more info can be found here: https://www.ev3dev.org
