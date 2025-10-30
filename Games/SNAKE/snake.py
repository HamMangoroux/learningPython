from msvcrt import getch
import random as rd
import os
import time as t

start = t.time()
width, height  = 45, 20
grid = [["#" for _ in range(width)] for _ in range(height)]

for y in range(1, height-1):
    for x in range(1, width-1):
        grid[y][x] = " "

def print_grid():
    os.system('cls')
    for row in grid:
        print("".join(row))

def random_apple():
    apple_x = rd.randint(1, width-2)
    apple_y = rd.randint(1, height-2)
    grid[apple_y][apple_x] = "@"

def refresh():
    try:
        while True:
            elapsed = t.time() - start
            print_grid()
            t.sleep(1/120)

    except None:
        pass

def movement(): 
    x_head, y_head = 8, 18 
    grid[y_head][x_head] = "O"
    print_grid()
    while True:
        key = getch().decode("utf-8")
        grid[y_head][x_head] = " "
        if key == 'w':
            y_head -= 1
        elif key == 'a':
            x_head -= 1
        elif key == 's':
            y_head += 1
        elif key == 'd':
            x_head += 1
        elif key == 'q':
            break
        grid[y_head][x_head] = "O"

        print_grid()
    return

