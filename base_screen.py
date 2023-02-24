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
        image_char = PhotoImage(file = "images/background.png")
        char_lbl=Label(self, image = image_char)
        char_lbl.x = image_char
        char_lbl.place(x=0, y=0)
        if self.firsttime == True:
            self.health=100
            self.supplies=100
            self.partymembers=1
            self.firsttime = False
        health = ttk.Style()
        health.theme_use('default')
        health.configure("health.Horizontal.TProgressbar", background='#00FF2B')

        supplies = ttk.Style()
        supplies.theme_use('default')
        supplies.configure("supplies.Horizontal.TProgressbar", background='blue')

        self.bar = Progressbar(self, length=300, style='health.Horizontal.TProgressbar')
        self.bar['value'] = self.health
        self.bar.grid(column=0, row=0, padx = 10, pady=(10, 0), sticky=S)
        self.healthlb = Label(self, text="Health: " + str(self.health), font="Ariel 10")
        self.healthlb.grid(row=1, column=0, padx=6.5, sticky=W)
        

        self.bar2 = Progressbar(self, length=300, style='supplies.Horizontal.TProgressbar', mode="determinate")
        self.bar2['value'] = 100
        self.bar2.grid(column=0, row=2, padx = 10, sticky=W)
        self.supplieslb = Label(self, text="Supplies: "+str(self.supplies), font="Ariel 10")
        self.supplieslb.grid(row=3, column=0, padx=6.5, sticky=W)

        self.partymemberslb = Label(self,text=f"Number of Party Members: {str(self.partymembers)}", font="Ariel 18")
        self.partymemberslb.grid(row=4,column=0,sticky=W,padx=(5,10),pady=(5,0))

        self.vspacing = Label(self, text=" ",height=28)
        self.vspacing.grid(row=5,column=2)

        self.stay = Button(self, text = "Stay", font="Ariel 24", width = 14, height=3, command=self.lower_supplies)
        self.stay.grid(row=6,column=2,sticky=N)
        
        self.raid = Button(self, text = "Raid", font="Ariel 24",width = 14, height=3, command=self.to_battle)
        self.raid.grid(row=6,column=3)

        self.adopt_btn = Button(self, text = "Adopt", font="Ariel 24",width = 14, height=3, command=self.to_adopt)
        self.adopt_btn.grid(row=6,column=4)

        self.update()

    def lower_supplies(self):
        self.supplies -= 5*self.partymembers
        if self.supplies<=0:
            self.die()
        self.supplieslb['text'] = "Supplies: " + str(self.supplies)
        self.health += 5
        if self.health>100:
            self.health = 100
        self.healthlb['text'] = "Health: " + str(self.health)
        self.bar['value'] = self.health
        self.bar2['value'] = self.supplies
        

    def to_battle(self):
        self.destroy_base_widgets_for_battle()

    def destroy_battle_widgets_for_base(self):
        self.destroy_battle_widgets()
        self.create_base_widgets()

    def destroy_battle_widgets(self):
        self.fighttext.destroy()
        self.run_btn.destroy()
        self.fight_btn.destroy()
    
    def destroy_okay(self):
        self.okay.destroy()
        self.fought.destroy()
        self.create_base_widgets()
    
    # BATTLE SCREEN PAGE

    def destroy_base_widgets(self):
        self.bar.destroy()
        self.bar2.destroy()
        self.healthlb.destroy()
        self.supplieslb.destroy()
        self.stay.destroy()
        self.raid.destroy()
        self.vspacing.destroy()
        self.adopt_btn.destroy()
        self.partymemberslb.destroy()     

    def destroy_base_widgets_for_battle(self):
        self.destroy_base_widgets()
        self.create_battle_widgets()
    
    def create_battle_widgets(self):
        # self.columnconfigure(0,weight=2)
        print(self.health)
        print(self.partymembers)
        self.percentage = self.health*(1+(self.partymembers-1)/self.partymembers)
        if self.percentage>100:
            self.percentage = 100
        self.fighttext = Label(self,text=f"You have a {self.percentage:.1f}% chance of winning. Do you want to fight or run?", font="Times 32")

        self.fighttext.grid(row=0, column=0, columnspan=2, sticky=N)

        self.run_btn = Button(self, text = "Run", font = "Times 30", width = 15, command = self.destroy_battle_widgets_for_base)
        self.run_btn.grid(row=1,column=0)

        self.fight_btn = Button(self, text = "Fight", font = "Times 30", width = 15, command = self.fight)
        self.fight_btn.grid(row=1,column=1)
    
    def fight(self):
        print("fight started")
        chance=random.randint(0,100)

        self.fought=Label(self,text="")
        self.fought.grid(row=0,column=0)

        self.percentage = self.health*(1+(self.partymembers-1)/self.partymembers)
        if self.percentage>100:
            self.percentage = 100

        if chance<=self.percentage:
            self.survive()
        else:
            self.die_battle()

    
    def survive(self):
        self.destroy_battle_widgets()
        healthlost=random.randint(1, self.health//8) #random way to calculate health lost when you survive; might change it ??
        self.health -= healthlost
        amount = random.randint(0,20)
        self.supplies += amount
        if self.supplies >= 100:
            self.supplies=100
        
        self.fought.config(text = f"You fought the zombie and lost {str(healthlost)} health.\n Your health is now at {str(self.health)}.\nYou received {amount} supplies. Your supplies is now at {str(self.supplies)}")

        self.okay=Button(self,text=f"Okay", command=self.destroy_okay)
        self.okay.grid(row=1,column=0)
    
    def die_base(self):
        self.destroy_base_widgets()
        self.died_base=Label(self,text="you died from low supplies lol")
        self.died_base.grid(row=0,column=0)

    def die_battle(self):
        self.destroy_battle_widgets()
        self.died_battle=Label(self,text = "you died in battle lol")
        self.died_battle.grid(row=0,column=0)

    def to_adopt(self):
        self.destroy_base_widgets_for_adopt()
    
    def destroy_base_widgets_for_adopt(self):
        self.destroy_base_widgets()
        self.create_adopt_widgets()
    
    def create_adopt_widgets(self):
        # self.columnconfigure(0,weight=2)
        self.partytext = Label(self,text=f"Do you want to adopt or leave? You currently have {self.partymembers} member(s) in your party.", font="Times 24")

        self.partytext.grid(row=0, column=0, columnspan=2, sticky=N)

        self.leave_btn = Button(self, text = "Leave", font = "Times 30", width = 15, command = self.destroy_adopt_widgets_noadopt_to_base)
        self.leave_btn.grid(row=1,column=0)

        self.adopt_btn = Button(self, text = "Adopt", font = "Times 30", width = 15, command = self.adopt)
        self.adopt_btn.grid(row=1,column=1)

    def destroy_adopt_widgets_noadopt(self):
        self.partytext.destroy()
        self.leave_btn.destroy()
        self.adopt_btn.destroy()
    def destroy_adopt_widgets_noadopt_to_base(self):
        self.destroy_adopt_widgets_noadopt()
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
        self.emptylabel.grid(row=0,column=0)
        self.destroy_adopt_widgets_noadopt()
        self.new_party_member()
        self.okay1=Button(self,text=f"Okay", command=self.destroy_adopt_widgets_afteradopt)
        self.okay1.grid(row=1,column=0)
    
    def new_party_member(self):
        self.partymembers +=1
        self.emptylabel.config(text = f"A new member joined your party! There are now {self.partymembers} members in your party.")

