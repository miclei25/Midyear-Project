from tkinter import *
from Model import *

bg_color = "black"
class Game_Screen(Frame):

    def __init__(self, master, callback_on_exit):
        super().__init__(master, bg = "black")

        self.callback_on_exit = callback_on_exit

        self.setup_grid()
        self.create_widgets()
        self.grid()
        self.display_grid()

        master.bind("<Left>", self.left)
        master.bind("<Right>", self.right)
        master.bind("<Up>", self.up)
        master.bind("<Down>", self.down)

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
        imageSmall = PhotoImage(file="images/2048title.gif")
        w = Label (self,
                        image = imageSmall, borderwidth=0
                         )
        w.photo = imageSmall
        w.grid (row = 0, column = 1, columnspan = 4)
        #Label(self, text = "2048", font = "Georgia 30 bold", fg = "Hot Pink", bg = bg_color
        #     ).grid(row = 0, column = 2, columnspan = 2)

        self.total_score = 0
        self.total_score = StringVar()
        self.total_score.set("0")
        Label(self, text = "  Score:", font = "Georgia 20", fg = "Hot Pink", bg = bg_color).grid(row = 1, column = 2, sticky = E)
        self.update_score = Label(self, textvariable = self.total_score, font = "Georgia 20", fg = "Hot Pink", bg = bg_color
        ).grid(row = 1, column = 3, sticky = W)
        Label(self,text = "", bg = bg_color).grid(row = 2, column = 1)
        
        self.imagelabels = []
        for row in range(4):
            for col in range(4):
                image = PhotoImage(file="images/image0.gif")
                piclabel = Label(self, image = image)
                self.imagelabels.append(piclabel)
                piclabel.photo = image
                piclabel.grid(row = row + 3, column = col + 1)
                
        Label(self, text = "", bg = bg_color).grid(row = 8)
        Button(self, text = "   UP ", font = "Helvetica 10 bold", fg = "DeepPink", command = self.up
        ).grid(row = 9, column = 2, sticky = E)
        Button(self, text = "DOWN", font = "Helvetica 10 bold", fg = "DeepPink", command = self.down
        ).grid(row = 9, column = 3, sticky = W)
        Button(self, text = " LEFT", font = "Helvetica 10 bold", fg = "DeepPink", command = self.left
        ).grid(row = 10, column = 2, sticky = E)
        Button(self, text = "RIGHT", font = "Helvetica 10 bold", fg = "DeepPink", command = self.right
        ).grid(row = 10, column = 3, sticky = W)
        
        Label(self, text = "\n", bg = bg_color).grid(row = 10)
        Button(self, text = "Exit", font = "Courier 12 bold", fg = "black", bg = "Hot Pink", command = self.selected_exit
        ).grid(row = 11, column = 1, columnspan = 4)
        Label(self, text = "", bg = bg_color).grid(row = 12)



    def display_score(self):
        self.total_score.set(str(self.grid1.score))

    def up(self, event = None):
        self.grid1.move_up = True
        self.grid1.move_vertical()
        self.grid1.move_up = False
        self.display_grid()
        self.display_score()
        self.losing_screen()
        # self.lose()

    def down(self, event = None):
        self.grid1.move_down = True
        self.grid1.move_vertical()
        self.grid1.move_down = False
        self.display_grid()
        self.display_score()
        self.losing_screen()
        # self.lose()

    def left(self, event = None):
        self.grid1.move_left = True
        self.grid1.move_horizontal()
        self.grid1.move_left = False
        self.display_grid()   
        self.display_score()
        self.losing_screen()
        # self.lose()

    def right(self, event = None):
        self.grid1.move_right = True
        self.grid1.move_horizontal()
        self.grid1.move_right = False
        self.display_grid()
        self.display_score()
        self.losing_screen()
        # self.lose()
        
    def selected_exit(self):
        self.callback_on_exit()

    def losing_screen(self):
        for row in range(4):
            for col in range(4):
                if self.grid1.grid[row][col] != None:
                    empty = False
                else:
                    empty = True
                    break
                    
        if self.grid1.can_move_horiz == False and self.grid1.can_move_vert == False and empty == False:
            image = PhotoImage(file="images/iwang.gif")
            piclabel = Label(self, image = image, bg = "Hot Pink", borderwidth = "50px")
            self.imagelabels.append(piclabel)
            piclabel.photo = image
            piclabel.grid(row = 3, column = 1, columnspan = 4, rowspan = 4)
            Label(self, text = "You Lose!", bg = "Hot Pink", font = "Georgia 24", fg = "white").grid(row = 6, column = 2, columnspan = 2)



    #for row in range(4):
        #for col in range(4):
            #if self.grid1.grid[row][col] == self.grid1.grid[row+1][col] or self.grid1.grid[row][col] == self.grid1.grid[row-1][]
    
    # def lose(self):
    #     if self.grid1.can_move_horiz == False and self.grid1.can_move_vert == False:
    #         # call the losing screen
    #         pass