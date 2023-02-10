from tkinter import *
class EventRaidBattle(Frame):
    
    def __init__(self, master, callback_on_battle):
        super().__init__(master)
        self.grid()
        self.create_widgets()
        self.callback_on_battle = callback_on_battle
    
    def create_widgets(self):
        # self.columnconfigure(0,weight=2)

        mybutton1 = Button(self, text = "Run", font = "Times 30", width = 15, command = self.start)
        mybutton1.grid(row=1,column=0)

        mybutton1 = Button(self, text = "Fight", font = "Times 30", width = 15, command = self.start)
        mybutton1.grid(row=1,column=1)
    
    def start(self):
        self.callback_on_start()