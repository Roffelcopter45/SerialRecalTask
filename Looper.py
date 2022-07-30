import csv
from mimetypes import init
import random
from tkinter import *
import os

from initMenuPage import *


# from initMenuPage import initMenuPage

class Looper():

    def __init__(self) -> None:
        window = self.getWindow()
        menu = initMenuPage(window)
        menu.call()
        window.mainloop()

        menu.forget
        #change()



    def getWindow(self):
        window = Tk()
        window.title("Serial Recall Task.")
        window.configure(bg='black')
        # fenster.attributes('-fullscreen', True)  # hierbei keine menu bar sichtbar
        window.geometry("5000x900+0+0")           # leichte verschoben aber menubar vorhanden
        return window

    @staticmethod
    def change(str):
        print(str)



        
        
        



        # fenster.mainloop()


if __name__ == "__main__":
    Looper()