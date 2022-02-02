from tkinter import *
import tkinter 

class GameManager(object):

    def __init__(self):
        self.root = tkinter.Tk()

    def opening_screen_stuff(self):

        self.root.title = "Welcome to 2048!"

    def game_screen(self):

        self.root.title = "2048"

def main():
    pass
    