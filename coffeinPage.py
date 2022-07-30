from tkinter import *

trefferquote = []

class coffeinPage():

    # Members / attributes
    def __init__(self, window):
        self.kaffee_label = Label(window, text="How is your coffein consumption? \n\n Click accordingly:\n\n",font=('Calibri', 20), bg='black', fg='#fff')
        self.kaffee_never_button = Button(window, text="never", font=('Calibri', 20), height=3, width=15, command=never)
        self.kaffee_sometimes_button = Button(window, text="sometimes", font=('Calibri', 20), height=3, width=15,command=sometimes)
        self.kaffee_daily_button = Button(window, text="daily/regularly", font=('Calibri', 20), height=3, width=25,command=daily)

    # Methoden / functions
    def call(self):
        self.kaffee_label.place(x=390, y=80, width=720, height=500)
        self.kaffee_never_button.place(x=625, y=480, width=100, height=40)
        self.kaffee_sometimes_button.place(x=725, y=480, width=100, height=40)
        self.kaffee_daily_button.place(x=825, y=480, width=100, height=40)

# @ statische methoden braucht kein self arg,  weils keine instanz braucht
#  somitr als funktion immer und überall aufgerufen werden kann


######################################### Unfinished ###################################################################
def never():
    trefferquote.append("never")
    frage_2()

def sometimes():
    trefferquote.append("sometimes")
    frage_2()

def daily():
    trefferquote.append("daily")
    frage_2()
