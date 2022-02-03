from tkinter import *

class Game_Screen(Frame):

    def __init__(self):
        pass

    def create_widgets(self):
        Label(self, text = "2048", font = "Georgia 25 bold", fg = "Hot Pink").grid(row = 3, column = 1)
        Label(self, text = "").grid(row = 4)
