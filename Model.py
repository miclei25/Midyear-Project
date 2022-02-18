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
    
    def move_horizontal(self):
        self.move = False
        self.can_move_horiz = False

        for r in range(4):
            prev_cell = None
            if self.move_left == True:
                self.x = range(len(self.grid[r]))
            elif self.move_right == True:
                self.x = range(len(self.grid[r]) - 1, -1, -1)
            
            for cell in self.x:

                if self.grid[r][cell] != None:
                    if prev_cell == None:
                        prev_cell = cell
                    
                    elif self.grid[r][cell] == self.grid[r][prev_cell]:
                        self.grid[r][prev_cell] *= 2
                        self.grid[r][cell] = None
                        if self.grid[r][prev_cell] != None:
                            self.score += self.grid[r][prev_cell]

                        if self.move_left == True:
                            self.y = range(prev_cell, 4)
                        elif self.move_right == True:
                            self.y = range(prev_cell, -1, -1)

                        for c in self.y:
                            if self.grid[r][c] == None:
                                prev_cell = c
                                break
                        self.move = True

                    else:
                        prev_cell = cell
            
            empty_cell = None
            for cell in self.x:
                for c in self.x:
                    if self.grid[r][c] == None:
                        empty_cell = c
                        break
                
                if empty_cell != None:
                    if self.move_left == True:
                        self.z = range(empty_cell, 4)
                    elif self.move_right == True:
                        self.z = range(empty_cell, -1, -1)
                    
                    for c in self.z:
                        if self.grid[r][c] != None:
                            self.grid[r][empty_cell] = self.grid[r][c]
                            self.grid[r][c] = None
                            self.move = True
                            break
                else:
                    break
        
        if self.move == True:
            self.add_number()
            self.can_move_horiz = True
    
    # def horizontal_shifting(self, r, cell, prev_cell):
    #     if self.grid[r][cell] != None:
    #                 if prev_cell == None:
    #                     prev_cell = cell
                    
    #                 elif self.grid[r][cell] == self.grid[r][prev_cell]:
    #                     self.grid[r][prev_cell] *= 2
    #                     self.grid[r][cell] = None
    #                     if self.grid[r][prev_cell] != None:
    #                         self.score += self.grid[r][prev_cell]

    #                     if self.move_left == True:
    #                         self.y = range(prev_cell, 4)
    #                     elif self.move_right == True:
    #                         self.y = range(prev_cell, -1, -1)

    #                     for c in self.y:
    #                         if self.grid[r][c] == None:
    #                             prev_cell = c
    #                             break
    #                     self.move = True

    #                 else:
    #                     prev_cell = cell

    # def horizontal_merging(self, r, cell, empty_cell):
    #     for c in self.x:
    #         if self.grid[r][c] == None:
    #             empty_cell = c
    #             break
                
    #     if empty_cell != None:
    #         if self.move_left == True:
    #             self.z = range(empty_cell, 4)
    #         elif self.move_right == True:
    #                     self.z = range(empty_cell, -1, -1)
                    
    #         for c in self.z:
    #             if self.grid[r][c] != None:
    #                 self.grid[r][empty_cell] = self.grid[r][c]
    #                 self.grid[r][c] = None
    #                 self.move = True
    #                 break
    #     else:
    #         return
    
    def move_vertical(self):
        self.move = False
        self.can_move_vert = False

        for c in range(4):
            prev_cell = None
            if self.move_up == True:
                self.x = range(len(self.grid[c]))
            elif self.move_down == True:
                self.x = range(len(self.grid[c]) - 1, -1, -1)

            for r in self.x:

                if self.grid[r][c] != None:
                    if prev_cell == None:
                        prev_cell = r
                    
                    elif self.grid[r][c] == self.grid[prev_cell][c]:
                        self.grid[prev_cell][c] *= 2
                        self.grid[r][c] = None
                        if self.grid[prev_cell][c] != None:
                            self.score += self.grid[prev_cell][c]

                        if self.move_up == True:
                            self.y = range(prev_cell, 4)
                        elif self.move_down == True:
                            self.y = range(prev_cell, -1, -1)

                        for row in range(prev_cell, 4):
                            if self.grid[row][c] == None:
                                prev_cell = row
                                break
                        self.move = True
                    
                    else:
                        prev_cell = r
            
            empty_cell = None
            for row in self.x:
                for r in self.x:
                    if self.grid[r][c] == None:
                        empty_cell = r
                        break
                
                if empty_cell != None:
                    if self.move_up == True:
                        self.z = range(empty_cell, 4)
                    elif self.move_down == True:
                        self.z = range(empty_cell, -1, -1)
                        
                    for r in self.z:
                        if self.grid[r][c] != None:
                            self.grid[empty_cell][c] = self.grid[r][c]
                            self.grid[r][c] = None
                            self.move = True
                            break
                else:
                    break
        
        if self.move == True:
            self.add_number()
            self.can_move_vert = True