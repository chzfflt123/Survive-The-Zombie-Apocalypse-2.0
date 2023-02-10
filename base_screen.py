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



        step()
        self.after(3000, change_dir)

        vspacing = Label(self, text=" ",height=30)
        vspacing.grid(row=4,column=2)

        stay = Button(self, text = "Stay", font = "Times 30", width = 20, height=2)
        stay.grid(row=5,column=2,sticky=E)
        # stay.place(x=300,y=300)

        raid = Button(self, text = "Raid", font = "Times 30", width = 20, height=2)
        raid.grid(row=5,column=3)
        tempnext_button = Button(self, text="temporary Next", font = "Ariel 20", width=12, height=2, bg="#A0A0A0", command=self.next)
        tempnext_button.grid(row=10, column=0)

    def next(self):
        self.callback_on_base()

    def quit_game(self):
        self.destroy()
