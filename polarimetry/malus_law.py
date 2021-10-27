
# This Program is assuming the following that the design is based on described as ...
# The program iterates the servo motor to each angle from 0 to 180 degrees and finds the intensity 
# using the Light Sensor. The program then plots the intensity vs angle. The Plot is compared to verify Malus Law 
# and the angle at which the intensity is maximum.

# Equipment that is going to be connected to the Arduino - 
# Micro Servo Motor 
# Light Sensor
# RGB Led
# Accelerometer / Inclinometer (Potentially)
# OLED Display (Potentially)

# Interfacing with the Arduino
import serial
import time
import numpy as np
import matplotlib.pyplot as plt

# Initializing the Arduino
arduino = serial.Serial(‘COM3’, 9600)

while True: # create loop

    command = str(input ("Servo position: ")) # query servo position
    pos = int(command)
    arduino.write(pos) # write position to serial port
    reachedPos = str(arduino.readline()) # read serial port for arduino echo