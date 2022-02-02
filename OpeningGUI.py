from tkinter import *

class Screen_Opening(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.create_widgets()
        self.grid()

    def create_widgets(self):

        Label(self, text = "2048", font = "Georgia 45 bold", fg = "Hot Pink").grid(row = 0, column = 1)
        Label(self, text = "").grid(row = 1)
        Label(self, text = "How to Play:\n\nUse buttons to move around the boxes within the grid.\nBoxes with the same number merge into one when they touch.\nTry to reach 2048.", font = "Helvetica 15 italic", fg = "Pink").grid(row = 2, column = 0, columnspan = 3)


root = Tk()
root.title("2048")
root.geometry("555x500")
app = Screen_Opening(root)
root.mainloop()