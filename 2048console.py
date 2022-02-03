from tkinter import *
import random

class Grid():

    def __init__(self):
        grid = []
        for n in range(4):
            grid.append([None] * 4)
        
        Grid.add_number(grid)
        Grid.add_number(grid)

    def add_number(self, grid):
        row = random.randint(0,3)
        col = random.randint(0,3)

        while grid[row[col]] != 0:
            row = random.randint(0,3)
            col = random.randint(0,3)
        
        grid[row[col]] = 2