from tkinter import * 
from tkinter import ttk
from tkinter.ttk import * 
from tkinter.ttk import Progressbar
import time
  
class BaseScreen(Frame):
    def __init__(self, master, to_battle):
        super(BaseScreen, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.to_battle = to_battle
        self.x = 1

    def create_widgets(self):

        # Add image file
        bg = PhotoImage(file = "base_background.jpg")
        
        # Create Canvas
        canvas1 = Canvas(self, width = 1250,
                        height = 750)
        
        canvas1.pack(fill = "both", expand = True)
        
        # Display image
        canvas1.create_image( 0, 0, image = bg, 
                            anchor = "nw")

        def lower_supplies():
            bar2['value'] -= 5
        health = ttk.Style()
        health.theme_use('default')
        health.configure("health.Horizontal.TProgressbar", background='#00FF2B')
        
        supplies = ttk.Style()
        supplies.theme_use('default')
        supplies.configure("supplies.Horizontal.TProgressbar", background='blue')

        bar = Progressbar(self, length=300, style='health.Horizontal.TProgressbar')
        bar['value'] = 95
        Label(self, text="Health", font="Ariel 10").grid(row=1, column=0, padx=6.5, sticky=W)
        bar.grid(column=0, row=0, padx = 10, pady=(10, 0), sticky=S)
        
        bar2 = Progressbar(self, length=300, style='supplies.Horizontal.TProgressbar', mode="determinate")
        bar2['value'] = 100
        Label(self, text="Supplies", font="Ariel 10").grid(row=3, column=0, padx=6.5, sticky=W)
        bar2.grid(column=0, row=2, padx = 10, sticky=W)

        vspacing = Label(self, text=" ",height=30)
        vspacing.grid(row=4,column=2)

        stay = Button(self, text = "Stay", font = "Times 30", width = 20, height=2, command=lower_supplies)
        stay.grid(row=5,column=2,sticky=E)
        # stay.place(x=300,y=300)

        raid = Button(self, text = "Raid", font = "Times 30", width = 20, height=2, command=self.to_battle)
        raid.grid(row=5,column=3)

    def to_battle(self):
        self.base_to_battle()
