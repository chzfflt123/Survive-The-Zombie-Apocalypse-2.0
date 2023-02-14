from tkinter import *
from base_screen import HEALTH
class EventRaidBattle(Frame):
    def __init__(self, master, callback_on_battle_run):
        super().__init__(master)
        self.grid()
        self.create_widgets()
        self.callback_on_battle_run = self.callback_on_battle_run
        # self.callback_on_battle = callback_on_battle
    
    def create_widgets(self):
        health=HEALTH
        health+=1

        # self.columnconfigure(0,weight=2)
        label = Label(self,text=f"You have a {health}% chance of winning!")
        label.grid(row=0, column=0)

        mybutton1 = Button(self, text = "Run", font = "Times 30", width = 15, command = self.run)
        mybutton1.grid(row=1,column=0)

        mybutton1 = Button(self, text = "Fight", font = "Times 30", width = 15, command = self.start)
        mybutton1.grid(row=1,column=1)
    
    def run(self):
        self.callback_on_battle_run()

    def start(self):
        self.callback_on_start()