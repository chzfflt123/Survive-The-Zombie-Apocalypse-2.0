from tkinter import * 
from tkinter import ttk
from tkinter.ttk import Progressbar

class BaseScreen(Frame):
    def __init__(self, master, callback_on_base):
        super(BaseScreen, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.callback_on_base = callback_on_base

    def create_widgets(self):
        # bg = PhotoImage(file = "base_background.jpg")
        
        # # Create Canvas
        # canvas1 = Canvas(self, width = 1250,
        #                 height = 750)
        
        # canvas1.pack(fill = "both", expand = True)
        
        # # Display image
        # canvas1.create_image( 0, 0, image = bg, 
        #                     anchor = "nw")
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
        
        raid = Button(self, text = "Raid", width = 20, height=2, command=self.to_battle)
        raid.grid(row=5,column=3)

        self.update()

    def lower_supplies(self):
        self.supplies -= 5
        self.supplieslb['text'] = "Supplies: " + str(self.supplies)

    def to_battle(self):
        self.callback_on_base()
