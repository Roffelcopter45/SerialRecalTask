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


