from tkinter import *

class Game_Screen(Frame):

    def __init__(self, master, callback_on_exit):
        super().__init__(master)

        self.callback_on_exit = callback_on_exit

        self.create_widgets()
        self.grid()

    def create_widgets(self):
        Label(self, text = "2048", font = "Georgia 25 bold", fg = "Hot Pink").grid(row = 0, column = 1)
        Label(self, text = "\n\n\n\n\n\n\n").grid(row = 1)

        Button(self, text = "Exit", font = "Courier 12 bold", fg = "Maroon3", command = self.callback_on_exit
        ).grid(row = 2, column = 1)

    def selected_exit(self):
        self.callback_on_exit()