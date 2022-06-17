from microbit import *

while True:
    if button_a.is_pressed():
        x = accelerometer.get_x()
        y = accelerometer.get_y()
        z = accelerometer.get_z()
        print(x, y, z)