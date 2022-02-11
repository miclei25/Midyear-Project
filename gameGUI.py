from tkinter import *
from Model import *
class Game_Screen(Frame):

    def __init__(self, master, callback_on_exit):
        super().__init__(master)

        self.callback_on_exit = callback_on_exit

        self.setup_grid()
        self.create_widgets()
        self.grid()
        self.display_grid()

    def setup_grid(self):
        self.grid1 = Grid()

    def display_grid(self):
        
        for row in range(4):
            rowtext = ""
            for col in range(4):
                if self.grid1.grid[row][col] == None:
                    rowtext += f"  {'x':4s}"
                else:
                    rowtext += f"  {str(self.grid1.grid[row][col]):4s}"

            self.rowtexts[row].set(rowtext)
       
    def create_widgets(self):
        
        Label(self, text = "2048", font = "Georgia 35 bold", fg = "Hot Pink").grid(row = 0, column = 1, columnspan = 3)

        Label(self, text = "Score:\n\n", font = "Georgia 15", fg = "Hot Pink"). grid (row = 1, column = 1)

        self.rowtexts = []
        for row in range(0,4):
            rowtext = StringVar()
            rowtext.set("")
            Label(self, textvariable = rowtext).grid(row = row + 2, column = 1)
            self.rowtexts.append(rowtext)

        Button(self, text = "UP", font = "Helvetica 10 bold", fg = "DeepPink", command = self.up
        ).grid(row = 8, column = 0, sticky = E)
        Button(self, text = "DOWN", font = "Helvetica 10 bold", fg = "DeepPink", command = self.down
        ).grid(row = 8, column = 1, sticky = W)
        Button(self, text = "LEFT", font = "Helvetica 10 bold", fg = "DeepPink", command = self.left
        ).grid(row = 9, column = 0, sticky = E)
        Button(self, text = "RIGHT", font = "Helvetica 10 bold", fg = "DeepPink", command = self.right
        ).grid(row = 9, column = 1, sticky = W)
        
        Button(self, text = "Exit", font = "Courier 12 bold", fg = "Maroon3", command = self.selected_exit
        ).grid(row = 10, column = 1)

    def up(self):
        self.grid1.move_up()
        self.display_grid()

    def down(self):
        self.grid1.move_down()
        self.display_grid()

    def left(self):
        self.grid1.move_left()
        self.display_grid()

    def right(self):
        self.grid1.move_right()
        self.display_grid()
        
    def selected_exit(self):
        self.callback_on_exit() 