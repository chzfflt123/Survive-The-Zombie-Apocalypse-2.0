from tkinter import *
class EventRaid(Frame):
    
    def __init__(self, master, callback_on_raid):
        super().__init__(master)
        self.grid()
        self.create_widgets()
        self.callback_on_raid = callback_on_raid
    
    def create_widgets(self):
        # self.columnconfigure(0,weight=2)

        mybutton1 = Button(self, text = "Stay", font = "Times 30", width = 15, command = self.start)
        mybutton1.grid(row=1,column=0)

        mybutton1 = Button(self, text = "Raid", font = "Times 30", width = 15, command = self.start)
        mybutton1.grid(row=1,column=4)
    
    def start(self):
        self.callback_on_start()