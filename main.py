from tkinter import *
from tkinter import ttk
import time


class digitalwatch(Tk):
    def __init__(self):
        super().__init__()

        self.title('Python Guides')
        self.resizable(0, 0)
        self.geometry('300x80')
        self['bg'] = 'white'

        self.style = ttk.Style(self)
        self.style.configure(
            'TLabel',
            background='white',
            foreground='black')

        self.label1 = Label(
            self,
            text=self.time_string(),
            font=('Digital-7', 40))

        self.label1.pack(expand=True)

        self.label1.after(1000, self.update)

    def time_string(self):
        return time.strftime('%H:%M:%S')

    def update(self):
        """ update the label every 1 second """

        self.label1.configure(text=self.time_string())

        self.label1.after(1000, self.update)


if __name__ == "__main__":
    ws = digitalwatch()
    ws.mainloop()














# # This is a sample Python script.
#
# # Press Umschalt+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print('Hi, Raphael')  # Press Strg+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
#
# # Serial recall

