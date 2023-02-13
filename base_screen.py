from tkinter import * 
from tkinter import ttk
from tkinter.ttk import Progressbar

class BaseScreen(Frame):
    def __init__(self, master, base_to_battle):
        super(BaseScreen, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.base_to_battle = base_to_battle

    def create_widgets(self):
        self.health=100
        self.supplies=100

        self.healthlb = Label(self, text="Health: " + str(self.health), font="Ariel 18")
        self.healthlb.grid(row=0, column=0, sticky=W, padx=(5, 10), pady=(5, 0))
        
        self.supplieslb = Label(self, text="Supplies: " + str(self.supplies), font="Ariel 18")
        self.supplieslb.grid(row=1, column=0, sticky=W, padx=(5, 10))
        

        vspacing = Label(self, text=" ")
        vspacing.grid(row=4,column=2)

        stay = Button(self, text = "Stay", width = 20, height=2, command=self.lower_supplies)
        stay.grid(row=5,column=2,sticky=E)
        
        raid = Button(self, text = "Raid", width = 20, height=2)
        raid.grid(row=5,column=3)
        tempnext_button = Button(self, text="temporary Next", font = "Ariel 20", width=12, height=2, bg="#A0A0A0", command=self.base_to_battle)
        tempnext_button.grid(row=10, column=2)

        self.update()

    def lower_supplies(self):
        self.supplies -= 5
        self.supplieslb['text'] = "Supplies: " + str(self.supplies)

    def base_to_battle(self):
        self.base_to_battle()
