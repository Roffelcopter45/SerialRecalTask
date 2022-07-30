import csv
import random
from tkinter import *
import os

trefferquote = []

class genderPage():

    # Members / attributes
    def __init__(self, window):

        self.soziodemo_label = Label(window, text="Socio Demographical Questionnaire\n\n Enter your gender:\n\n",
                                font=('Calibri', 20), bg='black', fg='#fff')
        self.male_button = Button(window, text="male", font=('Calibri', 25), height=3, width=15, command=male)
        self.female_button = Button(window, text="female", font=('Calibri', 25), height=3, width=15, command=female)
        self.diverse_button = Button(window, text="diverse", font=('Calibri', 25), height=3, width=15, command=diverse)

    # Methoden / functions
    def call(self):
        self.soziodemo_label.place(x=390, y=80, width=720, height=500)
        self.male_button.place(x=625, y=480, width=100, height=40)
        self.female_button.place(x=725, y=480, width=100, height=40)
        self.diverse_button.place(x=825, y=480, width=100, height=40)




def male():
    # enters male gender into csv and continues
    trefferquote.append("male")
    frage_1()

def female():
# enters male gender into csv and continues
    trefferquote.append("female")
    frage_1()

def diverse():
# enters male gender into csv and continues
    trefferquote.append("diverse")
    frage_1()

##########################################################################################################################


srt_text_label = Label(fenster,text = 'Welcome to the Serial Recall Task!\n 8 numbers will be shown to you,\n one after another.\n The goal: To memorize them\n in the right order.\n \n If you want to give it a try \n click on the button Trial.\n Or you feel ready, then you can click START.',
                       font=('Calibri', 30), bg = 'black', fg = '#fff')
exit_button = Button(fenster, text="EXIT", font=('Calibri', 20), height= 3, width=15, command=fenster.quit)
fragebogen_button = Button(fenster, text="Fragebögen", font=('Calibri', 20), height= 3, width=15, command=soziodemo)

continue_1_button = Button(fenster, text="continue", font=('Calibri', 20), height= 3, width=15, command= frage_1)

################################################ BEGIN ##############################################################################

main_menu()
fenster.mainloop()