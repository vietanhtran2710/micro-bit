from microbit import *
matrix = [
    '09090',
    '99999',
    '99999',
    '09990',
    '00900',
    '00000',
    '00000',
    '00000',
    '00000',
    '00000',
]

while True:
    display.show(Image(":".join(matrix[:5])))
    matrix = [matrix[-1]] + matrix[:-1]
    sleep(100)