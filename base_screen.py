from tkinter import * 
from tkinter import ttk
from tkinter.ttk import Progressbar
import random
class BaseScreen(Frame):
    def __init__(self, master):
        super(BaseScreen, self).__init__(master)
        self.grid()
        self.firsttime()
        self.create_base_widgets()
    
    def firsttime(self):
        self.firsttime = True

    def create_base_widgets(self):
        if self.firsttime == True:
            self.health=100
            self.supplies=100
            self.firsttime = False
        print(str(self.health))
        self.healthlb = Label(self, text=f"Health: {str(self.health)}", font="Ariel 18")
        self.healthlb.grid(row=0, column=0, sticky=W, padx=(5, 10), pady=(5, 0))
        
        self.supplieslb = Label(self, text=f"Supplies: {str(self.supplies)}", font="Ariel 18")
        self.supplieslb.grid(row=1, column=0, sticky=W, padx=(5, 10))
        

        self.vspacing = Label(self, text=" ")
        self.vspacing.grid(row=4,column=2)

        self.stay = Button(self, text = "Stay", width = 20, height=2, command=self.lower_supplies)
        self.stay.grid(row=5,column=2,sticky=E)
        
        self.raid = Button(self, text = "Raid", width = 20, height=2, command=self.to_battle)
        self.raid.grid(row=5,column=3)

        self.update()

    def lower_supplies(self):
        self.supplies -= 5
        self.supplieslb['text'] = "Supplies: " + str(self.supplies)

    def to_battle(self):
        self.destroy_base_widgets()
    
    def destroy_battle_widgets_nofight(self):
        self.fighttext.destroy()
        self.run.destroy()
        self.fight.destroy()
        self.create_base_widgets()

    def destroy_battle_widgets_afterfight(self):
        self.fighttext.destroy()
        self.run.destroy()
        self.fight.destroy()
        self.okay.destroy()
        self.fought.destroy()
        self.create_base_widgets
    
    # BATTLE SCREEN PAGE

    def destroy_base_widgets(self):
        self.healthlb.destroy()
        self.supplieslb.destroy()
        self.stay.destroy()
        self.raid.destroy()
        self.vspacing.destroy()
        self.create_battle_widgets()
    
    def create_battle_widgets(self):
        # self.columnconfigure(0,weight=2)
        self.fighttext = Label(self,text=f"You have a {self.health}% chance of winning. Do you want to fight or run?", font="Times 32")

        self.fighttext.grid(row=0, column=0, columnspan=2, sticky=N)

        print("test1")

        self.run = Button(self, text = "Run", font = "Times 30", width = 15, command = self.destroy_battle_widgets_nofight)
        self.run.grid(row=1,column=0)

        self.fight = Button(self, text = "Fight", font = "Times 30", width = 15, command = self.fight)
        self.fight.grid(row=1,column=1)
    
    def fight(self):
        healthlost=random.randint(1, self.health//8)
        self.fought=Label(self, text=f"You fought the zombie and lost {healthlost} health.")
        self.fought.grid(row=2,column=0)
        self.health -= healthlost

        okay=Button(self,text=f"Okay", command=self.destroy_battle_widgets_afterfight)
        okay.grid(row=3,column=0)
