#### IMPORTANT
# is there a way to make it so that if you clicked a button already you cant click it again or smth
# like in battle, if you click fight, you can click fight again and again and like it doesn't seem to work


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
            self.partymembers=1
            self.firsttime = False
        self.healthlb = Label(self, text=f"Health: {str(self.health)}", font="Ariel 18")
        self.healthlb.grid(row=0, column=0, sticky=W, padx=(5, 10), pady=(5, 0))

        self.supplieslb = Label(self, text=f"Supplies: {str(self.supplies)}", font="Ariel 18")
        self.supplieslb.grid(row=1, column=0, sticky=W, padx=(5, 10))

        self.partymemberslb = Label(self,text=f"Number of Party Members: {str(self.partymembers)}", font="Ariel 18")
        self.partymemberslb.grid(row=2,column=0,sticky=W,padx=(5,10),pady=(5,0))

        self.vspacing = Label(self, text=" ")
        self.vspacing.grid(row=5,column=2)

        self.stay = Button(self, text = "Stay", width = 20, height=2, command=self.lower_supplies)
        self.stay.grid(row=6,column=2,sticky=E)
        
        self.raid = Button(self, text = "Raid", width = 20, height=2, command=self.to_battle)
        self.raid.grid(row=6,column=3)

        self.adopt_btn = Button(self, text = "Adopt", width = 20, height=2, command=self.to_adopt)
        self.adopt_btn.grid(row=6,column=4)

        self.update()

    def lower_supplies(self):
        self.supplies -= 5*self.partymembers
        if self.supplies<0:
            self.supplies = 0
        self.supplieslb['text'] = "Supplies: " + str(self.supplies)
        self.health += 5
        if self.health>100:
            self.health = 100
        self.healthlb['text'] = "Health: " + str(self.health) + ", Number of Party Members: " + str(self.partymembers)
        

    def to_battle(self):
        self.destroy_base_widgets_for_battle()

    def destroy_battle_widgets(self):
        self.fighttext.destroy()
        self.run_btn.destroy()
        self.fight_btn.destroy()
        print("destroy_battle_widgets ended")
    
    def okay_function_after_battle(self):
        self.create_base_widgets()
        self.okay.destroy()
        self.fought.destroy()
    
    # BATTLE SCREEN PAGE

    def destroy_base_widgets_for_battle(self):
        self.healthlb.destroy()
        self.supplieslb.destroy()
        self.stay.destroy()
        self.raid.destroy()
        self.vspacing.destroy()
        self.adopt_btn.destroy()
        self.create_battle_widgets()
    
    def create_battle_widgets(self):
        # self.columnconfigure(0,weight=2)
        self.percentage = self.health*(1+(self.partymembers-1)/self.partymembers)
        if self.percentage>100:
            self.percentage = 100
        self.fighttext = Label(self,text=f"You have a {self.percentage:.1}% chance of winning. Do you want to fight or run?", font="Times 32")

        self.fighttext.grid(row=0, column=0, columnspan=2, sticky=N)

        self.run_btn = Button(self, text = "Run", font = "Times 30", width = 15, command = self.destroy_battle_widgets)
        self.run_btn.grid(row=1,column=0)

        self.fight_btn = Button(self, text = "Fight", font = "Times 30", width = 15, command = self.fight)
        self.fight_btn.grid(row=1,column=1)
    
    def fight(self):
        print("fight started")
        chance=random.randint(0,100)

        self.fought=Label(self,text="")
        self.fought.grid(row=2,column=0)

        self.percentage = self.health*(1+(self.partymembers-1)/self.partymembers)
        if self.percentage>100:
            self.percentage = 100

        if chance<=self.percentage:
            self.survive()
        else:
            self.die()

    
    def survive(self):
        healthlost=random.randint(1, self.health//8) #random way to calculate health lost when you survive; might change it ??
        self.health -= healthlost
        self.destroy_battle_widgets()
        self.fought.config(text = f"You fought the zombie and lost {str(healthlost)} health.\n Your health is now at {str(self.health)}.")
        amount = random.randint(0,50)
        if amount == 50:
            self.supplies = 100
        else:
            self.supplies += amount
        self.okay=Button(self,text=f"Okay", command=self.okay_function_after_battle)
        self.okay.grid(row=3,column=0)
        self.supplies -= 5*self.partymembers
        if self.supplies <0:
            self.supplies = 0
        if self.supplies == 0:
            self.die()
    
    def die(self):
        self.destroy_battle_widgets()
        self.fought.config(text = "you died lol") # placeholder for ending scene
    
    def to_adopt(self):
        self.destroy_base_widgets_for_adopt()
    
    def destroy_base_widgets_for_adopt(self):
        self.healthlb.destroy()
        self.supplieslb.destroy()
        self.stay.destroy()
        self.raid.destroy()
        self.vspacing.destroy()
        self.adopt_btn.destroy()
        self.create_adopt_widgets()
    
    def create_adopt_widgets(self):
        # self.columnconfigure(0,weight=2)
        self.partytext = Label(self,text=f"Do you want to adopt or leave?", font="Times 32")

        self.partytext.grid(row=0, column=0, columnspan=2, sticky=N)

        self.leave_btn = Button(self, text = "Leave", font = "Times 30", width = 15, command = self.destroy_adopt_widgets_noadopt)
        self.leave_btn.grid(row=1,column=0)

        self.adopt_btn = Button(self, text = "Adopt", font = "Times 30", width = 15, command = self.adopt)
        self.adopt_btn.grid(row=1,column=1)

    def destroy_adopt_widgets_noadopt(self):
        self.partytext.destroy()
        self.leave_btn.destroy()
        self.adopt_btn.destroy()
        self.create_base_widgets()
    
    def destroy_adopt_widgets_afteradopt(self):
        self.partytext.destroy()
        self.leave_btn.destroy()
        self.adopt_btn.destroy()
        self.emptylabel.destroy()
        self.okay1.destroy()
        self.create_base_widgets()
        print
        ("destroy_adopt_widgets_afteradopt ended")

    def adopt(self):
        print("adopted")
        self.emptylabel=Label(self,text="")
        self.emptylabel.grid(row=2,column=0)

        self.new_party_member()

        self.okay1=Button(self,text=f"Okay", command=self.destroy_adopt_widgets_afteradopt)
        self.okay1.grid(row=3,column=0)
    
    def new_party_member(self):
        self.partymembers +=1
        self.emptylabel.config(text = f"You adopted a new party member!")

