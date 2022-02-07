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
    
    def move_left(self, grid):

        if grid[0[3]] != None:
            if grid[0[2]] != None:
                if grid[0[1]] != None:
                    if grid[0[0]] != None:
                        pass
                    else:
                        grid[0[0]] = grid[0[1]]
                        grid[0[1]] = grid[0[2]]
                        grid[0[2]] = grid[0[3]]
                        grid[0[3]] = None
                else:
                    grid[0[1]] = grid[0[2]]
                    grid[0[2]] = grid[0[3]]
                    grid[0[3]] = None
            else:
                grid[0[2]] = grid[0[3]]
                grid[0[3]] = None
        else:
            pass

    def move_right(self, grid):
        pass

    def move_up(self, grid):
        pass

    def move_down(self, grid):
        pass