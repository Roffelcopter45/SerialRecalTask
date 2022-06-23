# TODO:
# probelauf könnte noch ausgebaut werden mit kommentaren

# klären mit buttons ob gerade ungerade VPn oder durch directory count, erstellung der kürzels
# wie definieren wir eine korrekte eingabe? 8 bel zeichen?!

# am ende des task die kss und likert ins csv appenden

# sound und licht einbindung module wird nochnicht richtig gefunden, wie kann ich das playsound richtig einbinden?

# fotos importieren/ tu logo
#from PIL import ImageTk,Image
#my_img = ImageTk.PhotoImage(Image.open("C:\Users\Rafael\Desktop\BA - Projekt\tu-berlin_logo.png"))

import csv
import random
from tkinter import *
import os
from playsound import playsound

small_counter = 0         # for sound and light
big_counter = 0             # for finishing the recall task
item_list = []
trefferquote = []
csv_file_data = []
kss_list = []
likert_list = []
file_count = 0
item_list_trial = []
trefferquote_trial = []

def start():
    # START Fenster Aufrufen mit Place
    change_button.place(x = 680, y = 680, width=150, height=50)
    exit_button.place(x = 920, y = 680, width=150, height=50)
    srt_text_label.place(x = 390, y = 80, width=720, height=500)
    trial_version_button.place(x = 450, y = 680, width=150, height=50)

# I.BEGIN: Serial Recall
def button_action():
    global kreuz_label
    change_button.destroy()
    exit_button.destroy()
    srt_text_label.destroy()
    trial_version_button.destroy()

    header = ['i1', 'i2', 'i3', 'i4', 'i5', 'i6', 'i7', 'i8']
    with open('srt_trefferquote.csv', 'w',newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)

    kss_scene()

def kss_scene():
    # rehearse_label.after(0, rehearse_label.place_forget)
    # Aufrufen des Eingabefensters karolinska sleeping skale
    eingabefeld.place(x = 1000, y = 390, width=300, height= 60)
    kss_button.place(x = 1000, y = 490, width=300, height= 60)
    kss_label.place(x = 230, y = 150,width=600, height= 550)
    nr_label.place(x = 840, y = 294, width=30, height= 400)

def kss_button():
    # nimmt kss_scene eingabe, append to kss_list, am ende der 120 Durchläufe put into csv
    eingabe_text = eingabefeld.get()
    eingabefeld.delete(0, 'end')
    kss_label.place_forget()
    nr_label.place_forget()
    eingabefeld.place_forget()
    kss_button.place_forget()

    if eingabe_text.isalpha():
        print("its alpha")
        try_again_kss_label.place(x=920, y=100, width=450, height=260)
        kss_scene()

    if int(eingabe_text) in range(1,11,1):
        kss_list.append(eingabe_text)
        try_again_kss_label.place_forget()
        likert_skala()

    if int(eingabe_text) not in range(1,11,1):
        try_again_kss_label.place(x=920, y=100, width=450, height=260)
        kss_scene()

def likert_skala():
    eingabefeld.place(x=1000, y=390, width=300, height=60)
    likert_label.place(x=230, y=190, width=600, height=550)
    likert_button.place(x=1000, y=490, width=300, height= 60)

def likert_button():
    eingabe_text = eingabefeld.get()
    eingabefeld.delete(0, 'end')
    eingabefeld.place_forget()
    likert_label.place_forget()
    likert_button.place_forget()

    if eingabe_text.isalpha():
        try_again_kss_label.place(x=920, y=100, width=450, height=260)
        likert_skala()

    if int(eingabe_text) in range(1,6,1):
        likert_list.append(eingabe_text)
        try_again_kss_label.place_forget()
        kreuz_label.place(x=550, y=300, width=450, height=260)
        kreuz_label.after(200, serial_recall)

    if int(eingabe_text) not in range(1,6,1):
        try_again_kss_label.place(x=920, y=100, width=450, height=260)
        likert_skala()

# On-time von 700-1000 ms und Off-time von 250-500 ms
def serial_recall():
    if (len(item_list) != 8):
        item = get_num()
        # Erscheinungsdauer der Zahlen hier modifizieren:
        kreuz_label.config(text = item, font=('Calibri', 150))
        kreuz_label.after(300, black_screen)

    if (len(item_list) == 8 ):
        # Rehearse Label und Zeit (10000)
        rehearse_label.place(x = 550, y = 300, width=450, height=260)
        rehearse_label.after(1000, input_gui)

def black_screen():
    kreuz_label.config(text="", font=('Calibri', 150))
    kreuz_label.after(250, serial_recall)

def get_num():
    global rehearse_label
    # get random nr in range 0 to 9
    num = random.randrange(1, 10)

    # if there exists this number already in the list search a new one, until its new
    while num in item_list:
        num = random.randrange(1, 10)

    if len(item_list) <= 7:
        item_list.append(num)

    print(item_list)
    return num

def input_gui():
    rehearse_label.after(0, rehearse_label.place_forget)

    insert_label.place(x = 460, y = 250)
    eingabefeld.place(x = 625, y = 400, width=300, height= 60)
    eingabe_button.place(x = 625, y = 470, width=300, height= 60)

def eingabe_button():
    global csv_file_data
    global trefferquote
    global small_counter
    global big_counter

    eingabe_text = eingabefeld.get()
    eingabefeld.delete(0, 'end')
    insert_label.place_forget()
    eingabefeld.place_forget()
    eingabe_button.place_forget()
    kreuz_label.place_forget()
    rehearse_label.place_forget()

    # wie sollen die eingaben sein ?
    # string muss 8 zeichen haben, ohne zeichen aneinander gekettet
    # falls man nicht weiß welches item kommt, kann ein beliebiges zeichen zahl buchstabe gewählt werden

    # Falls korrekte Eingabe, VErGleichE
    if (len(eingabe_text) == 8 ):
        for i in range(0, 8):
            if int(eingabe_text[i]) == item_list[i]:
                trefferquote.append(1)
            else: trefferquote.append(0)

    # print trefferquote to csv
    if (len(eingabe_text) == 8):
        with open('srt_trefferquote.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(trefferquote)

        item_list.clear()
        trefferquote.clear()

        small_counter = small_counter + 1

        if small_counter == 2:
            print("switch my sound")
            # pip install sound package  zum abspielen
            big_counter = big_counter + small_counter

            kss_scene()

            # if big_counter == 30:
            #     #switch light
            # if big_counter == 60:
            #     #switch light
            # if big_counter ==90:
            #
            # if big_counter == 4:
            #     kss_scene()

            #if big_counter == 6:
                # kreuz_label.config(text="THANKS", font=('Calibri', 50), bg='black', fg='#fff')
                # kreuz_label.after(3000, fenster.quit)

            # reset small_counter
            small_counter = 0

        try_again_label.place_forget()

        kreuz_label.place(x=550, y=300, width=450, height=260)
        kreuz_label.after(300, serial_recall)

    # Exception label, falls eingabe unpassend
    if len(eingabe_text) != 8:
        try_again_label.place(x=370, y=500, width=800, height=260)
        input_gui()

################################################### Trial version im 2. Fenster ##################################################################
# ------------------------------------------------------------------------------------------------------------------------------------------------
##################################################################################################################################################

def trial_version():
    global fenster2
    global trial_label
    global insert_label_trial
    global eingabefeld_trial
    global eingabe_button_trial
    global rehearse_label_trial

    fenster2 = Toplevel()
    fenster2.title("Serial Recall Task - Trial.")
    fenster2.configure(bg='black')
    fenster2.geometry("5000x900+0+0")

    # Return to Menu
    return_to_menu_button = Button(fenster2, text="Return", font=('Calibri', 20), height=3, width=15,command=return_button)
    return_to_menu_button.place(x=720, y=680, width=150, height=50)

    # REHEARSE
    trial_label = Label(fenster2, text="+", font=('Calibri', 50), bg = 'black', fg = '#fff')
    rehearse_label_trial = Label(fenster2, text="REHEARSE", font=('Calibri', 50), bg='black', fg='#fff')

    # EINGABE FENSTER -------------------------------
    insert_label_trial = Label(fenster2, text="Enter the whole number series: ", font=('Calibri', 50), bg='black', fg='#fff')
    eingabefeld_trial = Entry(fenster2, font=("Calibri", 25), bd=5, width=30)
    eingabe_button_trial = Button(fenster2, text="ENTER", font=('Calibri', 20), height=3, width=15, command = eingabe_trial)

    # Start trial
    trial_label.place(x = 550, y = 300, width=450, height=260)
    trial_label.after(1000, serial_recall_trial)

def serial_recall_trial():
    if (len(item_list_trial) != 8):
        item = get_num_trial()
        # Erscheinungsdauer der Zahlen hier modifiezieren:
        trial_label.config(text = item, font=('Calibri', 150))
        trial_label.after(700, black_screen_trial)

    if (len(item_list_trial) == 8 ):
        # Rehearse Label und Zeit (10000)
        rehearse_label_trial.place(x = 550, y = 300, width=450, height=260)
        rehearse_label_trial.after(5000, input_gui_trial)

def input_gui_trial():
    rehearse_label_trial.after(0, rehearse_label_trial.place_forget)
    # Aufrufen des Eingabefensters
    insert_label_trial.place(x=460, y=150)
    eingabefeld_trial.place(x=625, y=300, width=300, height=60)
    eingabe_button_trial.place(x=625, y=370, width=300, height=60)

def black_screen_trial():
    trial_label.config(text="", font=('Calibri', 150))
    trial_label.after(300, serial_recall_trial)

def get_num_trial():
    global rehearse_label_trial
    # get random nr in range 0 to 9
    num = random.randrange(1, 10)

    # if there exists this number already in the list search a new one, until its new
    while num in item_list_trial:
        num = random.randrange(1, 10)

    if len(item_list_trial) <= 7:
        item_list_trial.append(num)

    print(item_list_trial)
    return num

def eingabe_trial():
    global trefferquote_trial

    eingabe_text_trial = eingabefeld_trial.get()
    eingabefeld_trial.delete(0, 'end')
    insert_label_trial.place_forget()
    eingabefeld_trial.place_forget()
    eingabe_button_trial.place_forget()

    print(eingabe_text_trial)
    if (eingabe_text_trial == ""):
        item_list.clear()
        trefferquote.clear()

    # Falls korrekte Eingabe, VErGleichE
    if (len(eingabe_text_trial) == 8):

        for i in range(0, 8):
            if int(eingabe_text_trial[i]) == item_list_trial[i]:
                trefferquote_trial.append(1)
            else:
                trefferquote_trial.append(0)

    item_list_trial.clear()
    trefferquote_trial.clear()

    # Transition zum recall task
    trial_label.config(text="", font=('Calibri', 50), bg='black', fg='#fff')
    trial_label.after(500, serial_recall_trial)

def return_button():

    fenster2.destroy()

#-------------FENSTER; LABEL; BUTTONS-------------------------------------------------------------------------------------

# Hauptfenster & title erstellen
fenster = Tk()
fenster.title("Serial Recall Task.")
fenster.configure(bg='black')
#fenster.attributes('-fullscreen', True)  # hierbei keine menu bar sichtbar
fenster.geometry("5000x900+0+0")          # leichte verschoben aber menubar vorhanden

# Label und Buttons erstellen.
change_button = Button(fenster, text="START",font=('Calibri', 20), height= 3, width=15, command=button_action)
exit_button = Button(fenster, text="EXIT", font=('Calibri', 20), height= 3, width=15, command=fenster.quit)
trial_version_button = Button(fenster, text="Trial", font=('Calibri', 20), height= 3, width=15, command=trial_version)

kss_label = Label(fenster,text="Karolinska Sleepiness Skale\n Please enter the number that fits the most,\n according the description:\n \nExtremely alert\n Very alert\n Alert\n Rather alert\nNeither alert nor sleepy\n Some signs of sleepiness\n Sleepy, but no effort to keep awake\nSleepy but some effort to keep awake\n Very sleepy, great effort to keep awake, fighting sleep\nExtremely sleepy, can't keep awake",font = ('Calibri', 20),bg = 'black',fg = '#fff')
nr_label = Label(fenster,text="1\n 2\n 3\n 4\n 5\n 6\n 7\n 8\n 9\n 10 ",font=('Calibri', 20),bg='black',fg='#fff')

kreuz_label = Label(fenster, text="+", font=('Calibri', 50), bg = 'black', fg = '#fff')
rehearse_label = Label(fenster, text="REHEARSE", font=('Calibri', 50),bg = 'black', fg = '#fff')
black_screen_label = Label(fenster, text  ="",bg = 'white', fg = '#fff')
srt_text_label = Label(fenster,text = 'Welcome to the Serial Recall Task!\n 8 numbers will be shown to you,\n one after another.\n The goal: To memorize them\n in the right order.\n \n If you want to give it a try \n click on the button Trial.\n Or you feel ready, then you can click START.',
                       font=('Calibri', 30), bg = 'black', fg = '#fff')
try_again_label = Label(fenster, text=" Try again please,\n the input should consist of 8 characters!", font=('Calibri', 30), bg = 'black', fg = '#fff')
try_again_kss_label = Label(fenster, text=" Try again please,\n the input should consist \nof only one number\n in the given range!", font=('Calibri', 20), bg = 'black', fg = '#fff')
likert_label = Label(fenster, text =" Likert Scale:\n Please enter the number that fits the most,\n according the description:\n\n I feel pleasent and good!\n\n Strongly disagree   1\n Disagree                  2\n Undecided                3 \n Agree                       4\n Strongly Agree        5\n", font = ('Calibri', 20), bg = 'black', fg = '#fff')

# EINGABE FENSTER -------------------------------
insert_label = Label(fenster, text="Enter the number series: ",font=('Calibri', 50),bg = 'black', fg = '#fff')
eingabefeld = Entry(fenster,font=("Calibri", 25), bd=5, width=30)
eingabe_button = Button(fenster, text="Enter", font=('Calibri', 20), height= 3, width=15, command= eingabe_button)
kss_button = Button(fenster, text="Enter", font=('Calibri', 20), height= 3, width=15, command= kss_button)
likert_button = Button(fenster, text="Enter", font=('Calibri', 20), height= 3, width=15, command= likert_button)
################################### BEGIN ##############################################################################



dir_path = r'C:\Users\Rafael\Desktop\BA - Projekt\srt_results'
for path in os.scandir(dir_path):
    if path.is_file():
        file_count += 1

# file_count um zu determinieren ob gerade oder ungerade vpn
print('file count:', file_count)
print(dir_path, "swag")

# get current working dir path
cwd = os.getcwd()

# join current working dir with folder
targetPath = os.path.join(cwd, 'srt_results')

while not os.path.exists(targetPath):
    os.mkdir(targetPath)
print(targetPath)

# funktioniert nicht r + path
# dir_path = r'%s'%targetPath
# print(dir_path)
# for path in os.scandir(dir_path):
#     if path.is_file():
#         file_count += 1

# file_count um zu determinieren ob gerade oder ungerade vpn
print('file count 2:', file_count)

# hier kommt der neue name je nach dem kürzel rein
kürzel = 'blabli'
endung = '.csv'

kürzel = kürzel + endung

targetFile = os.path.join(targetPath, kürzel)
testFile = open(targetFile, "w")
testFile.write("test")
testFile.close()


start()
#playsound('C:/Users/Rafael/Desktop/Audio_Musik/Arctic Monkeys - Riot Van Acoustic.mp3')
fenster.mainloop()
########################################################################################################################





















# # START Fenster Aufrufen mit Place
# #anweisungs_label.place(x = 800, y = 50, width=450, height=260)
# change_button.place(x = 680, y = 680, width=150, height=50)
# #info_label.place(x = 800, y = 400, width=450, height=170)
# exit_button.place(x = 920, y = 680, width=150, height=50)
# srt_text_label.place(x = 390, y = 80, width=720, height=500)
# trial_version_button.place(x = 450, y = 680, width=150, height=50)

# anweisungs_label.place(x = 800, y = 50, width=450, height=260)
# change_button.place(x = 950, y = 330, width=150, height=80)
# info_label.place(x = 800, y = 400, width=450, height=160)
# exit_button.place(x = 950, y = 580, width=140, height=80)
# srt_text_label.place(x = 30, y = 180, width=720, height=500)



# Komponenten, Fenster in gewünschter Reihenfolge
# anweisungs_label.pack(fill=BOTH, expand=True)
# change_button.pack()
# info_label.pack(fill=BOTH, expand=True)
# exit_button.pack()

# 3,2,1 counter
# def print_3():
#     kreuz_label.config(text="3", font=('Calibri', 50))
#     kreuz_label.after(1000, print_2)
#
# def print_2():
#     kreuz_label.config(text="2", font=('Calibri', 50))
#     kreuz_label.after(1000, print_1)
#
# def print_1():
#     kreuz_label.config(text="1", font=('Calibri', 50))
#     kreuz_label.after(1000, serial_recall)


#I had a similar problem with PyCharm, where the dependencies I installed using pip would work for the editor windows
# (i.e., there were no error reports about imports), but the project would complain about the dependencies when I tried to run it.
# Turns out, I set up a virtual environment for that project after I created the tasks that ran my project and tests.
# I had to go to the window where you set up the tasks and make sure that all of them used the correct venv. Hope this is useful.


# def trefferquote_to_csv():
#     # überschreibt die alte csv
#     # evtl noch markieren im header ob es gerade oder ungerade VPn ist
#     global csv_file_data
#
#     data = csv_file_data
#
#     #differentiation der VPn gera oder ungerade
#     # if gerade  : header[gerade, bla blub]
#     # if ungerade : header[ungerade, ...]
#
#     header = ['i_1','i_2','i_3','i_4','i_5','i_6','i_7','i_8']
#
#     with open('srt_trefferquote.csv', 'w') as file:
#         writer = csv.writer(file)
#         writer.writerow(header)
#         writer.writerows(data)
#
#     return
