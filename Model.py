from tkinter import *
import random

class Grid():

    def __init__(self, score):
        self.score = score
        
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

        if self.grid[0][3] != None:
            if self.grid[0][2] != None:
                if self.grid[0][1] != None:
                    if self.grid[0][0] != None:
                        pass
                    else:
                        self.grid[0][0] = self.grid[0][1]
                        self.grid[0][1] = self.grid[0][2]
                        self.grid[0][2] = self.grid[0][3]
                        self.grid[0][3] = None
                else:
                    self.grid[0][1] = self.grid[0][2]
                    self.grid[0][2] = self.grid[0][3]
                    self.grid[0][3] = None
            else:
                self.grid[0][2] = self.grid[0][3]
                self.grid[0][3] = None
        else:
            pass
        if self.grid[1][3] != None:
            if self.grid[1][2] != None:
                if self.grid[1][1] != None:
                    if self.grid[1][0] != None:
                        pass
                    else:
                        self.grid[1][0] = self.grid[1][1]
                        self.grid[1][1] = self.grid[1][2]
                        self.grid[1][2] = self.grid[1][3]
                        self.grid[1][3] = None
                else:
                    self.grid[1][1] = self.grid[1][2]
                    self.grid[1][2] = self.grid[1][3]
                    self.grid[1][3] = None
            else:
                self.grid[1][2] = self.grid[1][3]
                self.grid[1][3] = None
        else:
            pass
        if self.grid[2][3] != None:
            if self.grid[2][2] != None:
                if self.grid[2][1] != None:
                    if self.grid[2][0] != None:
                        pass
                    else:
                        self.grid[2][0] = self.grid[2][1]
                        self.grid[2][1] = self.grid[2][2]
                        self.grid[2][2] = self.grid[2][3]
                        self.grid[2][3] = None
                else:
                    self.grid[2][1] = self.grid[2][2]
                    self.grid[2][2] = self.grid[2][3]
                    self.grid[2][3] = None
            else:
                self.grid[2][2] = self.grid[2][3]
                self.grid[2][3] = None
        else:
            pass
        if self.grid[3][3] != None:
            if self.grid[3][2] != None:
                if self.grid[3][1] != None:
                    if self.grid[3][0] != None:
                        pass
                    else:
                        self.grid[3][0] = self.grid[3][1]
                        self.grid[3][1] = self.grid[3][2]
                        self.grid[3][2] = self.grid[3][3]
                        self.grid[3][3] = None
                else:
                    self.grid[3][1] = self.grid[3][2]
                    self.grid[3][2] = self.grid[3][3]
                    self.grid[3][3] = None
            else:
                self.grid[3][2] = self.grid[3][3]
                self.grid[3][3] = None
        else:
            pass

    def move_right(self):
        
        if self.grid[0][3] != None:
            if self.grid[0][2] != None:
                if self.grid[0][1] != None:
                    if self.grid[0][0] != None:
                        pass
                    else:
                        self.grid[0][0] = self.grid[0][1]
                        self.grid[0][1] = self.grid[0][2]
                        self.grid[0][2] = self.grid[0][3]
                        self.grid[0][3] = None
                else:
                    self.grid[0][1] = self.grid[0][2]
                    self.grid[0][2] = self.grid[0][3]
                    self.grid[0][3] = None
            else:
                self.grid[0][2] = self.grid[0][3]
                self.grid[0][3] = None
        else:
            pass
        if self.grid[1][3] != None:
            if self.grid[1][2] != None:
                if self.grid[1][1] != None:
                    if self.grid[1][0] != None:
                        pass
                    else:
                        self.grid[1][0] = self.grid[1][1]
                        self.grid[1][1] = self.grid[1][2]
                        self.grid[1][2] = self.grid[1][3]
                        self.grid[1][3] = None
                else:
                    self.grid[1][1] = self.grid[1][2]
                    self.grid[1][2] = self.grid[1][3]
                    self.grid[1][3] = None
            else:
                self.grid[1][2] = self.grid[1][3]
                self.grid[1][3] = None
        else:
            pass
        if self.grid[2][3] != None:
            if self.grid[2][2] != None:
                if self.grid[2][1] != None:
                    if self.grid[2][0] != None:
                        pass
                    else:
                        self.grid[2][0] = self.grid[2][1]
                        self.grid[2][1] = self.grid[2][2]
                        self.grid[2][2] = self.grid[2][3]
                        self.grid[2][3] = None
                else:
                    self.grid[2][1] = self.grid[2][2]
                    self.grid[2][2] = self.grid[2][3]
                    self.grid[2][3] = None
            else:
                self.grid[2][2] = self.grid[2][3]
                self.grid[2][3] = None
        else:
            pass
        if self.grid[3][3] != None:
            if self.grid[3][2] != None:
                if self.grid[3][1] != None:
                    if self.grid[3][0] != None:
                        pass
                    else:
                        self.grid[3][0] = self.grid[3][1]
                        self.grid[3][1] = self.grid[3][2]
                        self.grid[3][2] = self.grid[3][3]
                        self.grid[3][3] = None
                else:
                    self.grid[3][1] = self.grid[3][2]
                    self.grid[3][2] = self.grid[3][3]
                    self.grid[3][3] = None
            else:
                self.grid[3][2] = self.grid[3][3]
                self.grid[3][3] = None
        else:
            pass

    def move_up(self):
        
        if self.grid[0][3] != None:
            if self.grid[0][2] != None:
                if self.grid[0][1] != None:
                    if self.grid[0][0] != None:
                        pass
                    else:
                        self.grid[0][0] = self.grid[0][1]
                        self.grid[0][1] = self.grid[0][2]
                        self.grid[0][2] = self.grid[0][3]
                        self.grid[0][3] = None
                else:
                    self.grid[0][1] = self.grid[0][2]
                    self.grid[0][2] = self.grid[0][3]
                    self.grid[0][3] = None
            else:
                self.grid[0][2] = self.grid[0][3]
                self.grid[0][3] = None
        else:
            pass
        if self.grid[1][3] != None:
            if self.grid[1][2] != None:
                if self.grid[1][1] != None:
                    if self.grid[1][0] != None:
                        pass
                    else:
                        self.grid[1][0] = self.grid[1][1]
                        self.grid[1][1] = self.grid[1][2]
                        self.grid[1][2] = self.grid[1][3]
                        self.grid[1][3] = None
                else:
                    self.grid[1][1] = self.grid[1][2]
                    self.grid[1][2] = self.grid[1][3]
                    self.grid[1][3] = None
            else:
                self.grid[1][2] = self.grid[1][3]
                self.grid[1][3] = None
        else:
            pass
        if self.grid[2][3] != None:
            if self.grid[2][2] != None:
                if self.grid[2][1] != None:
                    if self.grid[2][0] != None:
                        pass
                    else:
                        self.grid[2][0] = self.grid[2][1]
                        self.grid[2][1] = self.grid[2][2]
                        self.grid[2][2] = self.grid[2][3]
                        self.grid[2][3] = None
                else:
                    self.grid[2][1] = self.grid[2][2]
                    self.grid[2][2] = self.grid[2][3]
                    self.grid[2][3] = None
            else:
                self.grid[2][2] = self.grid[2][3]
                self.grid[2][3] = None
        else:
            pass
        if self.grid[3][3] != None:
            if self.grid[3][2] != None:
                if self.grid[3][1] != None:
                    if self.grid[3][0] != None:
                        pass
                    else:
                        self.grid[3][0] = self.grid[3][1]
                        self.grid[3][1] = self.grid[3][2]
                        self.grid[3][2] = self.grid[3][3]
                        self.grid[3][3] = None
                else:
                    self.grid[3][1] = self.grid[3][2]
                    self.grid[3][2] = self.grid[3][3]
                    self.grid[3][3] = None
            else:
                self.grid[3][2] = self.grid[3][3]
                self.grid[3][3] = None
        else:
            pass

    def move_down(self):
        
        if self.grid[0][3] != None:
            if self.grid[0][2] != None:
                if self.grid[0][1] != None:
                    if self.grid[0][0] != None:
                        pass
                    else:
                        self.grid[0][0] = self.grid[0][1]
                        self.grid[0][1] = self.grid[0][2]
                        self.grid[0][2] = self.grid[0][3]
                        self.grid[0][3] = None
                else:
                    self.grid[0][1] = self.grid[0][2]
                    self.grid[0][2] = self.grid[0][3]
                    self.grid[0][3] = None
            else:
                self.grid[0][2] = self.grid[0][3]
                self.grid[0][3] = None
        else:
            pass
        if self.grid[1][3] != None:
            if self.grid[1][2] != None:
                if self.grid[1][1] != None:
                    if self.grid[1][0] != None:
                        pass
                    else:
                        self.grid[1][0] = self.grid[1][1]
                        self.grid[1][1] = self.grid[1][2]
                        self.grid[1][2] = self.grid[1][3]
                        self.grid[1][3] = None
                else:
                    self.grid[1][1] = self.grid[1][2]
                    self.grid[1][2] = self.grid[1][3]
                    self.grid[1][3] = None
            else:
                self.grid[1][2] = self.grid[1][3]
                self.grid[1][3] = None
        else:
            pass
        if self.grid[2][3] != None:
            if self.grid[2][2] != None:
                if self.grid[2][1] != None:
                    if self.grid[2][0] != None:
                        pass
                    else:
                        self.grid[2][0] = self.grid[2][1]
                        self.grid[2][1] = self.grid[2][2]
                        self.grid[2][2] = self.grid[2][3]
                        self.grid[2][3] = None
                else:
                    self.grid[2][1] = self.grid[2][2]
                    self.grid[2][2] = self.grid[2][3]
                    self.grid[2][3] = None
            else:
                self.grid[2][2] = self.grid[2][3]
                self.grid[2][3] = None
        else:
            pass
        if self.grid[3][3] != None:
            if self.grid[3][2] != None:
                if self.grid[3][1] != None:
                    if self.grid[3][0] != None:
                        pass
                    else:
                        self.grid[3][0] = self.grid[3][1]
                        self.grid[3][1] = self.grid[3][2]
                        self.grid[3][2] = self.grid[3][3]
                        self.grid[3][3] = None
                else:
                    self.grid[3][1] = self.grid[3][2]
                    self.grid[3][2] = self.grid[3][3]
                    self.grid[3][3] = None
            else:
                self.grid[3][2] = self.grid[3][3]
                self.grid[3][3] = None
        else:
            pass