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
            
            empty_cell = None
            for cell in range(len(self.grid[r])):
                for c in range(len(self.grid[r])):
                    if self.grid[r][c] == None:
                        empty_cell = c
                        break
                
                if empty_cell != None:
                    for c in range(len(self.grid[r][empty_cell + 1:])):
                        if self.grid[r][empty_cell + 1 + c] != None:
                            self.grid[r][empty_cell] = self.grid[r][empty_cell + 1 + c]
                            self.grid[r][empty_cell + 1 + c] = None
                            move = True
                else:
                    break
        
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
            
            empty_cell = None
            for cell in range(len(self.grid[r])):
                for c in range(len(self.grid[r])):
                    if self.grid[r][3 - c] == None:
                        empty_cell = 3 - c
                        break
                
                if empty_cell != None:
                    for c in range(len(self.grid[r][:empty_cell + 1])):
                        if self.grid[r][c] != None:
                            self.grid[r][empty_cell] = self.grid[r][c]
                            self.grid[r][c] = None
                            move = True
                else:
                    break

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
            
            empty_cell = None
            for row in range(len(self.grid[c])):
                for r in range(len(self.grid[c])):
                    if self.grid[r][c] == None:
                        empty_cell = r
                        break
                
                if empty_cell != None:
                    for r in range(len(self.grid[:empty_cell + 1][c])):
                        if self.grid[empty_cell + 4 - r][c] != None:
                            self.grid[r][empty_cell] = self.grid[empty_cell + 4 - r][c]
                            self.grid[empty_cell + 4 - r][c] = None
                            move = True
                else:
                    break
        
        if move == True:
            self.add_number()
        else:
            pass

    def move_down(self):
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
            
            empty_cell = None
            for row in range(len(self.grid[c])):
                for r in range(len(self.grid[c])):
                    if self.grid[r][c] == None:
                        empty_cell = r
                        break
                
                if empty_cell != None:
                    for r in range(len(self.grid[:empty_cell + 1][c])):
                        if self.grid[empty_cell + 4 - r][c] != None:
                            self.grid[r][empty_cell] = self.grid[empty_cell + 4 - r][c]
                            self.grid[empty_cell + 4 - r][c] = None
                            move = True
                else:
                    break

        if move == True:
            self.add_number()