from tkinter import * 
from tkinter import ttk
from tkinter.ttk import Progressbar

class BaseScreen(Frame):
    def __init__(self, master, callback_to_battle):
        super(BaseScreen, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.callback_to_battle = callback_to_battle

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

        self.bar = Progressbar(self, length=350, style='health.Horizontal.TProgressbar')
        self.bar['value'] = 95
        self.bar.grid(column=0, row=0, padx = 10, pady=(10, 0), sticky=S)
        Label(self, text="Health", font="Ariel 10").grid(row=1, column=0, padx=6.5, sticky=W)
        
        
        self.bar2 = Progressbar(self, length=350, style='supplies.Horizontal.TProgressbar', mode="determinate")
        self.bar2['value'] = 100
        self.bar2.grid(column=0, row=2, padx = 10, sticky=W)
        Label(self, text="Supplies", font="Ariel 10").grid(row=3, column=0, padx=6.5, sticky=W)
        

        vspacing = Label(self, text=" ")
        vspacing.grid(row=4,column=2)

        stay = Button(self, text = "Stay", width = 20, height=2, command=self.lower_supplies)
        stay.grid(row=5,column=2,sticky=E)
        
        raid = Button(self, text = "Raid", width = 20, height=2)
        raid.grid(row=5,column=3)
        tempnext_button = Button(self, text="temporary Next", font = "Ariel 20", width=12, height=2, bg="#A0A0A0", command=self.base_to_battle)
        tempnext_button.grid(row=10, column=0)

        self.new()
        self.update()

    def lower_supplies(self):
        self.bar2['value'] -= 5
    def new(self):
        self.bar['value'] = 100
        self.bar2['value'] = 100

    def base_to_battle(self):
        self.base_to_battle()
