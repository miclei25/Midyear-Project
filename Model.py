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
        
        if 32 in self.grid[0] or 32 in self.grid[1] or 32 in self.grid[2] or 32 in self.grid[3]:
            if_four = random.randint(0,10)
            if if_four <= 2:
                self.grid[row][col] = 4
            else:
                self.grid[row][col] = 2
        else:
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
            
            prev_cell = None
            for cell in range(len(self.grid[r])):
                if prev_cell == None:
                    prev_cell = cell
                elif self.grid[r][cell] == None and self.grid[r][prev_cell] != None:
                    prev_cell = cell

                    for c in range(len(self.grid[r])):
                        if self.grid[r][c] == None:
                            prev_cell = c
                            break

                elif self.grid[r][cell] != None:
                    self.grid[r][prev_cell] = self.grid[r][cell]
                    self.grid[r][cell] = None
                    
        self.add_number()

    def move_right(self):
        
        pass

    def move_up(self):
        
        pass

    def move_down(self):
        
        pass