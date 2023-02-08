from tkinter import *
class EventRaid(Frame):
    
    def __init__(self, master, callback_on_raid):
        super(EventRaid, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.callback_on_raid = callback_on_raid
    
    def create_widgets(self):
        # self.columnconfigure(0,weight=2)

        mybutton1 = Button(self, text = "Stay", font = "Times 30", width = 15)
        mybutton1.grid(row=5,column=0)

        mybutton1 = Button(self, text = "Raid", font = "Times 30", width = 15)
        mybutton1.grid(row=5,column=1)
    
    # def start(self):
    #     self.callback_on_start()