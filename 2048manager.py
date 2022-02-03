from tkinter import *
from OpeningGUI import Screen_Opening
from gameGUI import Game_Screen

class GameManager(object):

    def __init__(self):
        self.root = Tk()
    
    def setup_openingscreen(self):
        self.root.title ("2048")
        self.root.geometry ("555x500")
        self.current_screen = Screen_Opening (master = self.root, callback_on_play = self.onclose_openingscreen)

    def onclose_openingscreen(self):
        self.current_screen.destroy()
        self.setup_gameGUI()

    def setup_gameGUI(self):
        self.root.title ("2048")
        self.root.geometry ("555x500")
        self.current_screen = Game_Screen()

def main():
    game = GameManager()
    game.setup_openingscreen()
    game.root.mainloop()
main()