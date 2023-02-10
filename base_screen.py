from tkinter import * 
from tkinter import ttk
from tkinter.ttk import * 
from tkinter.ttk import Progressbar
import time
  
class BaseScreen(Frame):
    def __init__(self, master, callback_on_base):
        super(BaseScreen, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.callback_on_base = callback_on_base
        """self.x = 1"""

    def create_widgets(self):
        def lower()
        
        Label(self, text="Health: ", font="Ariel 16").grid(row=1, column=0, sticky=W)
        self.health = Label(self, text="100", font="Ariel 16").grid(row=1, column=1, sticky=W)

        Label(self, text="Supplies: ", font="Ariel 16").grid(row=3, column=0, sticky=W)
        self.supplies = Label(self, text="100", font="Ariel 16").grid(row=3, column=1, sticky=W)



        tempnext_button = Button(self, text="temporary Next", font = "Ariel 20", width=12, height=2, bg="#A0A0A0", command=self.next)
        tempnext_button.grid(row=10, column=0)

    def next(self):
        self.callback_on_base()

    def quit_game(self):
        self.destroy()
