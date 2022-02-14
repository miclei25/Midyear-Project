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
            for col in range(4):
                w = self.imagelabels[row*4 + col]
                if self.grid1.grid[row][col] == None:
                    image = PhotoImage(file="images/image0.gif")
                else:
                    image = PhotoImage(file="images/image" + str(self.grid1.grid[row][col]) + "num.gif")
                w.configure(image = image)
                w.image = image
       
    def create_widgets(self):
        
        Label(self, text = "2048\n", font = "Georgia 30 bold", fg = "Hot Pink").grid(row = 0, column = 1, columnspan = 3)

        Label(self, text = "Score:\n\n", font = "Georgia 15", fg = "Hot Pink"). grid (row = 1, column = 1)

        self.imagelabels = []
        for row in range(0,4):
            for col in range(0,4):
                image = PhotoImage(file="images/image0.gif")
                piclabel = Label(self, image = image)
                self.imagelabels.append(piclabel)
                piclabel.photo = image # saving the image as a property is required for "saving" the image. It's odd.
                piclabel.grid(row = row + 2, column = col + 1)
                
        Label(self, text = "").grid(row = 8)
        Button(self, text = "UP", font = "Helvetica 10 bold", fg = "DeepPink", command = self.up
        ).grid(row = 9, column = 0, sticky = E, columnspan = 4)
        Button(self, text = "DOWN", font = "Helvetica 10 bold", fg = "DeepPink", command = self.down
        ).grid(row = 9, column = 2, sticky = W, columnspan = 4)
        Button(self, text = "LEFT", font = "Helvetica 10 bold", fg = "DeepPink", command = self.left
        ).grid(row = 10, column = 0, sticky = E, columnspan = 4)
        Button(self, text = "RIGHT", font = "Helvetica 10 bold", fg = "DeepPink", command = self.right
        ).grid(row = 10, column = 2, sticky = W, columnspan = 4)
        
        Label(self, text = "").grid(row = 10)
        Button(self, text = "Exit", font = "Courier 12 bold", fg = "Maroon3", command = self.selected_exit
        ).grid(row = 11, column = 1, columnspan = 4)

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