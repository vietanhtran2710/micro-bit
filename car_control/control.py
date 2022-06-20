from microbit import *

while True:
    matrix = [['0' for i in range(5)] for j in range(5)]
    x = accelerometer.get_x()
    if x <= -200:
        matrix[2][0] = '9'
    elif x >= 200:
        matrix[2][4] = '9'
    else:
        matrix[2][2] = '9'
    output = str(x)
    if button_a.is_pressed():
        matrix[0][2] = '9'
        output += " 1"
    else:
        output += " 0"
    if button_b.is_pressed():
        matrix[4][2] = '9'
        output += "1"
    else:
        output += "0"
    print(output)
    display.show(Image(":".join(["".join(row) for row in matrix])))