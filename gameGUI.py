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
        #for row in range(0):
        row = 0
        for row in range(0,4):
            rowonetext = ""
            for col in range(0,4):
                if self.grid1.grid[row][col] == None:
                    rowonetext += "  x  "
                else:
                    rowonetext += "   " + str(self.grid1.grid[row][col])

            self.rowtexts[row].set(rowonetext)

            
        pass

    def create_widgets(self):
        
        Label(self, text = "2048", font = "Georgia 25 bold", fg = "Hot Pink").grid(row = 0, column = 1)
        Label(self, text = "\n\n\n\n\n\n\n").grid(row = 1)

<<<<<<< HEAD
        Label(self, text = "Score:", font = "Georgia 15", fg = "Hot Pink"). grid (row = 0, column = 2)

        self.rowtexts = []
        for row in range(0,4):
            rowtext = StringVar()
            rowtext.set("")
            Label(self, textvariable = rowtext).grid(row = row + 2, column = 1)
            self.rowtexts.append(rowtext)
=======
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
>>>>>>> b2293464c76fa511d2a79fce135b021f81481b49

        Button(self, text = "Up", font = "Symbol 10", fg = "firebrick1").grid(row = 3, column = 0)
        Button(self, text = "Left", font = "Symbol 10", fg = "firebrick1").grid(row = 4, column = 0)
        Button(self, text = "Right", font = "Symbol 10", fg = "firebrick1").grid(row = 4, column = 1)
        Button(self, text = "Down", font = "Symbol 10", fg = "firebrick1").grid(row = 5, column = 0)
        
        Button(self, text = "Exit", font = "Courier 12 bold", fg = "Maroon3", command = self.callback_on_exit
        ).grid(row = 6, column = 1)
<<<<<<< HEAD





=======
>>>>>>> b2293464c76fa511d2a79fce135b021f81481b49

    def selected_exit(self):
        self.callback_on_exit()