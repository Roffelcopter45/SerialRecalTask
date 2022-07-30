import csv
import random
from tkinter import *
import os

from Looper import *

class initMenuPage():


    def __init__(self, window) -> None:
        self.srt_text_label = Label(window,text = 'Welcome to the Serial Recall Task!\n 8 numbers will be shown to you,\n one after another.\n The goal: To memorize them\n in the right order.\n \n If you want to give it a try \n click on the button Trial.\n Or you feel ready, then you can click START.',
                        font=('Calibri', 30), bg = 'black', fg = '#fff')
        self.exit_button = Button(window, text="EXIT", font=('Calibri', 20), height= 3, width=15, command=window.quit)
        self.fragebogen_button = Button(window, text="Fragebögen", font=('Calibri', 20), height= 3, width=15, command=Looper.change("soziodemo"))

        self.elementList = [self.srt_text_label, self.exit_button, self.fragebogen_button]

    def call(self):
        self.srt_text_label.place(x=390, y=80, width=720, height=500)
        self.exit_button.place(x=920, y=680, width=150, height=50)
        self.fragebogen_button.place(x = 680, y = 680, width=150, height=50)

    def forget(self):
        self.srt_text_label.place_forget()
        self.exit_button.place_forget()
        self.fragebogen_button.place_forget()