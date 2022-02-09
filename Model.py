from tkinter import *
import random

class Grid():

    def __init__(self):
        
        self.grid = []
        for n in range(4):
            self.grid.append([None] * 4)
        
        self.add_number()
        self.add_number()

    def add_number(self):
        row = random.randint(0,3)
        col = random.randint(0,3)

        while self.grid[row][col] != None:
            row = random.randint(0,3)
            col = random.randint(0,3)
        
        self.grid[row][col] = 2
    
    def move_left(self):

        for r in range(4):
            prev_cell = None
            for cell in range(len(self.grid[r])):

                if self.grid[r][cell] != None:
                    if prev_cell == None:
                        prev_cell = cell
                    elif self.grid[r][cell] == self.grid[r][prev_cell]:
                        self.grid[r][prev_cell] **= 2
                        self.grid[r][cell] = None
                    else:
                        prev_cell = cell

            # for cell in self.grid[r]:

            #     if cell != None:
            #         if cell == prev_cell:
            #             prev_cell **= 2
            #             cell = None
            #         else:
            #             prev_cell = cell

    def move_right(self):
        
        pass

    def move_up(self):
        
        pass

    def move_down(self):
        
        pass