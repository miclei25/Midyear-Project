from tkinter import *
import random

class Grid():

    def __init__(self):
        
        self.grid = []
        for n in range(4):
            self.grid.append([None] * 4)
        
        self.add_number()
        self.add_number()

        self.score = 0

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

                        for c in range(prev_cell, 4):
                            if self.grid[r][c] == None:
                                prev_cell = c
                                break
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
                    for c in range(empty_cell, 4):
                        if self.grid[r][c] != None:
                            self.grid[r][empty_cell] = self.grid[r][c]
                            self.grid[r][c] = None
                            move = True
                            break
                else:
                    break
        
        if move == True:
            self.add_number()

    def move_right(self):
        move = False
        
        for r in range(4):
            prev_cell = None
            for cell in range(len(self.grid[r]) - 1, -1, -1):

                if self.grid[r][cell] != None:
                    
                    if prev_cell == None:
                        prev_cell = cell
                    
                    elif self.grid[r][cell] == self.grid[r][prev_cell]:
                        self.grid[r][prev_cell] *= 2
                        self.grid[r][cell] = None
                        self.score += self.grid[r][prev_cell]

                        for c in range(prev_cell, -1, -1):
                            if self.grid[r][c] == None:
                                prev_cell = c
                                break
                        move = True

                    else:
                        prev_cell = cell
            
            empty_cell = None
            for cell in range(len(self.grid[r]) - 1, -1, -1):
                for c in range(len(self.grid[r]) - 1, -1, -1):
                    if self.grid[r][c] == None:
                        empty_cell = c
                        break
                
                if empty_cell != None:
                    for c in range(empty_cell, -1, -1):
                        if self.grid[r][c] != None:
                            self.grid[r][empty_cell] = self.grid[r][c]
                            self.grid[r][c] = None
                            move = True
                            break
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
                        self.grid[prev_cell][c] *= 2
                        self.grid[r][c] = None
                        if self.grid[prev_cell][c] != None:
                            self.score += self.grid[prev_cell][c]

                        for row in range(prev_cell, 4):
                            if self.grid[row][c] == None:
                                prev_cell = row
                                break
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
                        for r in range(empty_cell, 4):
                            if self.grid[r][c] != None:
                                self.grid[empty_cell][c] = self.grid[r][c]
                                self.grid[r][c] = None
                                move = True
                                break
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
            for r in range(len(self.grid[c]) - 1, -1, -1):

                if self.grid[r][c] != None:

                    if prev_cell == None:
                        prev_cell = r
                    
                    elif self.grid[r][c] == self.grid[prev_cell][c]:
                        self.grid[r][c] *= 2
                        self.grid[prev_cell][c] = None
                        self.score += self.grid[prev_cell][c]

                        for row in range(prev_cell, -1, -1):
                            if self.grid[row][c] == None:
                                prev_cell = row
                                break
                        move = True
                    
                    else:
                        prev_cell = r
            
            empty_cell = None
            for row in range(len(self.grid[c]) - 1, -1, -1):
                for r in range(len(self.grid[c]) - 1, -1, -1):
                    if self.grid[r][c] == None:
                        empty_cell = r
                        break
                
                if empty_cell != None and empty_cell != 0:
                    for r in range(empty_cell, -1, -1):
                        if self.grid[r][c] != None:
                            self.grid[empty_cell][c] = self.grid[r][c]
                            self.grid[r][c] = None
                            move = True
                            break
                else:
                    break

        if move == True:
            self.add_number()