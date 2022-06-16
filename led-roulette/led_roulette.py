from microbit import *

x, y = 0, 0
dir = ((0, 1), (1, 0), (0, -1), (-1, 0))
dir_index = 0
matrix = [['0' for i in range(5)] for j in range(5)]

while True:
    matrix[x][y] = '9'
    display_matrix = ':'.join([''.join(row) for row in matrix])
    print(display_matrix)
    display.show(Image(display_matrix))
    if not 0 <= x + dir[dir_index][0] < 5 or not 0 <= y + dir[dir_index][1] < 5:
        dir_index = (dir_index + 1) % 4
    matrix[x][y] = '0'
    x += dir[dir_index][0]
    y += dir[dir_index][1]
    sleep(20)