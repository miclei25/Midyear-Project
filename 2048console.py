from tkinter import *
import random

def start_game():
    grid = []
    for n in range(4):
        grid.append([0] * 4)
    
    add_number(grid)
    add_number(grid)

def add_number(grid):
    row = random.randint(0,3)
    col = random.randint(0,3)

    while 0 not in grid[row]:
        row = random.randint(0,3)
        col = random.randint(0,3)
    
    grid[row[col]] = 2