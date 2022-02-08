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

        # for n in range(4):
        #     if self.grid[n][3] != None:
        #         if self.grid[n][2] != None:
        #             if self.grid[n][1] != None:
        #                 if self.grid[n][0] != None:
        #                     pass
        #                 else:
        #                     self.grid[n][0] = self.grid[n][1]
        #                     self.grid[n][1] = self.grid[n][2]
        #                     self.grid[n][2] = self.grid[n][3]
        #                     self.grid[n][3] = None
        #             else:
        #                 self.grid[n][1] = self.grid[n][2]
        #                 self.grid[n][2] = self.grid[n][3]
        #                 self.grid[n][3] = None
        #         else:
        #             self.grid[n][2] = self.grid[n][3]
        #             self.grid[n][3] = None
        #     else:
        #         pass
        #     self.add_number()

        for r in range(4):
            for cell in self.grid[r]:
                if cell == None:
                    pass

    def move_right(self):
        
        pass

    def move_up(self):
        
        pass

    def move_down(self):
        
        pass