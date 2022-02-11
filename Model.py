from tkinter import *
import random

class Grid():

    def __init__(self):
        
        self.grid = []
        for n in range(4):
            self.grid.append([None] * 4)
        self.score = 0
        
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
        move = False

        for r in range(4):
            prev_cell = None
            for cell in range(len(self.grid[r])):

                if self.grid[r][cell] != None:
                    
                    if prev_cell == None:
                        prev_cell = cell
                    
                    elif self.grid[r][cell] == self.grid[r][prev_cell]:
                        self.grid[r][prev_cell] *= 2
                        self.grid[r][cell] = None
                        self.score += self.grid[r][prev_cell]
                        move = True

                    else:
                        prev_cell = cell
            
            prev_cell = None
            for cell in range(len(self.grid[r])):
                if prev_cell == None:
                    prev_cell = cell
                
                elif self.grid[r][cell] == None and self.grid[r][prev_cell] != None:
                    for c in range(len(self.grid[r])):
                        if self.grid[r][c] == None:
                            prev_cell = c
                            break

                elif self.grid[r][cell] != None and self.grid[r][prev_cell] == None:
                    self.grid[r][prev_cell] = self.grid[r][cell]
                    self.grid[r][cell] = None
                    move = True
        
        if move == True:
            self.add_number()

    def move_right(self):
        move = False
        
        for r in range(4):
            prev_cell = None
            for c in range(len(self.grid[r])):

                if self.grid[r][3 - c] != None:
                    
                    if prev_cell == None:
                        prev_cell = 3 - c
                    
                    elif self.grid[r][3 - c] == self.grid[r][prev_cell]:
                        self.grid[r][prev_cell] *= 2
                        self.grid[r][3 - c] = None
                        self.score += self.grid[r][prev_cell]
                        move = True

                    else:
                        prev_cell = 3 - c
            
            prev_cell = None
            for c in range(len(self.grid[r])):
                if prev_cell == None:
                    prev_cell = 3 - c
                
                elif self.grid[r][3 - c] == None and self.grid[r][prev_cell] != None:
                    for c in range(len(self.grid[r])):
                        if self.grid[r][3 - c] == None:
                            prev_cell = 3 - c
                            break

                elif self.grid[r][3 - c] != None and self.grid[r][prev_cell] == None:
                    self.grid[r][prev_cell] = self.grid[r][3 - c]
                    self.grid[r][3 - c] = None
                    move = True

        if move == True:
            self.add_number()

    def move_up(self):
        move = False

        for c in range(4):
            prev_cell = None
            for r in range(len(self.grid[c])):

                if self.grid[r][c] != None:
                    if prev_cell == None:
                        prev_cell = r
                    
                    elif self.grid[r][c] == self.grid[prev_cell][c]:
                        self.grid[r][c] *= 2
                        self.grid[prev_cell][c] = None
                        self.score += self.grid[r][c]
                        move = True
                    
                    else:
                        prev_cell = r
            
            prev_cell = None
            for r in range(len(self.grid[c])):
                if prev_cell == None:
                    prev_cell = r
                
                elif self.grid[r][c] == None and self.grid[prev_cell][c] != None:
                    for r in range(len(self.grid[c])):
                        if self.grid[r][c] == None:
                            prev_cell = r
                            break

                elif self.grid[r][c] != None and self.grid[prev_cell][c] == None:
                    self.grid[prev_cell][c] = self.grid[r][c]
                    self.grid[r][c] = None
                    move = True
        
        if move == True:
            self.add_number()
        else:
            pass

    def move_down(self):
        move = False
        
        # code

        if move == True:
            self.add_number()