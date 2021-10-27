import pyfirmata
import time

board = pyfirmata.Arduino('COM5')

servo = board.get_pin('d:7:o')

while True:
    servo.write(90)
    time.sleep(1)
    servo.write(0)
    time.sleep(1)