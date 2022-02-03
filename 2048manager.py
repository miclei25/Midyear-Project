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
<<<<<<< HEAD
        
=======
        self.current_screen = Game_Screen()
>>>>>>> 83561cea40e2b13baa00d6ca5ac4ad984408cdca

def main():
    game = GameManager()
    game.setup_openingscreen()
<<<<<<< HEAD
    game.root.mainloop()
=======
    game.onclose_openingscreen()
    game.setup_gameGUI()

>>>>>>> 83561cea40e2b13baa00d6ca5ac4ad984408cdca
main()