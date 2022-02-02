from tkinter import *
from OpeningGUI import Screen_Opening

class GameManager(object):

    def __init__(self):
<<<<<<< HEAD
        self.root = Tk()
    
    def setup_openingscreen(self):
        self.root.title ("2048")
        self.root.geometry ("555x500")
        self.current_screen = Screen_Opening (master = self.root, callback_on_play = self.onclose_openingscreen)

    def onclose_openingscreen(self):
        self.current_screen.destory()
        self.setup_gameGUI()

    def setup_gameGUI(self):
        self.root.title ("2048")
        self.root.geometry ("555x500")
        
=======
        self.root = tkinter.Tk()

    def opening_screen_stuff(self):

        self.root.title = "Welcome to 2048!"

    def game_screen(self):

        self.root.title = "2048"

def main():
    pass
    
>>>>>>> 9c4666f46bf5fe6dbd3ce2568200c8fd38692a1a
