from tkinter import *
from Model import *
class Game_Screen(Frame):

    def __init__(self, master, callback_on_exit):
        super().__init__(master)

        self.callback_on_exit = callback_on_exit

        self.setup_grid()
        self.create_widgets()
        self.grid()

    def setup_grid(self):
        self.grid1 = Grid()

    def display_grid(self):
        row1text = ""
        for i in self.grid[0]:
            if i == None:
                row1text += "    "
            else:
                row1text += "   " + str(i)
            
        pass

    def create_widgets(self):
        
        Label(self, text = "2048", font = "Georgia 25 bold", fg = "Hot Pink").grid(row = 0, column = 1)
        Label(self, text = "\n\n\n\n\n\n\n").grid(row = 1)

        self.row1text = StringVar()
        self.row1text.set("")
        Label(self, textvariable = self.row1text).grid(row = 2, column = 1)

        self.row2text = StringVar()
        self.row2text.set("")
        Label(self, textvariable = self.row2text).grid(row = 2, column = 1)

        self.row3text = StringVar()
        self.row3text.set("")
        Label(self, textvariable = self.row3text).grid(row = 2, column = 1)

        self.row4text = StringVar()
        self.row4text.set("")
        Label(self, textvariable = self.row4text).grid(row = 2, column = 1)

        Button(self, text = "UP", font = "Helvetica 10 bold", fg = "firebrick1", command = self.up
        ).grid(row = 3, column = 0, sticky = E)
        Button(self, text = "DOWN", font = "Helvetica 10 bold", fg = "firebrick1", command = self.down
        ).grid(row = 3, column = 1, sticky = W)
        Button(self, text = "LEFT", font = "Helvetica 10 bold", fg = "firebrick1", command = self.left
        ).grid(row = 4, column = 0, sticky = E)
        Button(self, text = "RIGHT", font = "Helvetica 10 bold", fg = "firebrick1", command = self.right
        ).grid(row = 4, column = 1, sticky = W)
        
        Button(self, text = "Exit", font = "Courier 12 bold", fg = "Maroon3", command = self.selected_exit
        ).grid(row = 6, column = 1)

    def up(self):
        pass

    def down(self):
        pass

    def left(self):
        pass

    def right(self):
        pass
    
    def selected_exit(self):
        self.callback_on_exit()