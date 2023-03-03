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
            self.fight_count =0
            self.firsttime = False
        
        self.image_char = PhotoImage(file = "images/background_base.png")
        self.char_lbl=Label(self, image = self.image_char)
        self.char_lbl.x = self.image_char
        self.char_lbl.place(x=0, y=0)

        self.angryman = PhotoImage(file = "images/character_angryman.png")
        self.angryman_lbl=Label(self, image = self.angryman)
        self.angryman_lbl.x = self.angryman
        self.angryman_lbl.place(x=550, y=150)
        
        if self.partymembers>=2:
            self.baldie = PhotoImage(file = "images/character_baldie.png")
            self.baldie_lbl=Label(self, image = self.baldie)
            self.baldie_lbl.x = self.baldie
            self.baldie_lbl.place(x=220, y=175)
        
        if self.partymembers>=3:
            self.girl = PhotoImage(file = "images/character_girl.png")
            self.girl_lbl=Label(self, image = self.girl)
            self.girl_lbl.x = self.girl
            self.girl_lbl.place(x=775, y=115)

        if self.partymembers>=4:
            self.duck = PhotoImage(file = "images/character_duck.png")
            self.duck_lbl=Label(self, image = self.duck)
            self.duck_lbl.x = self.duck
            self.duck_lbl.place(x=425, y=100)

        if self.partymembers>=5:
            self.dog = PhotoImage(file = "images/character_dog.png")
            self.dog_lbl=Label(self, image = self.dog)
            self.dog_lbl.x = self.dog
            self.dog_lbl.place(x=710, y=450)

        health = ttk.Style()
        health.theme_use('default')
        health.configure("health.Horizontal.TProgressbar", background='#00FF2B')

        supplies = ttk.Style()
        supplies.theme_use('default')
        supplies.configure("supplies.Horizontal.TProgressbar", background='blue')

        self.bar = Progressbar(self, length=360, style='health.Horizontal.TProgressbar')
        self.bar['value'] = self.health
        self.bar.grid(column=0, row=0, padx = 10, pady=(10, 0), sticky=S)
        self.healthlb = Label(self, text="Health: " + str(self.health), font="Ariel 10")
        self.healthlb.grid(row=1, column=0, padx=6.5, sticky=W)
        

        self.bar2 = Progressbar(self, length=360, style='supplies.Horizontal.TProgressbar', mode="determinate")
        self.bar2['value'] = self.supplies
        self.bar2.grid(column=0, row=2, padx = 10, sticky=W)
        self.supplieslb = Label(self, text="Supplies: "+str(self.supplies), font="Ariel 10")
        self.supplieslb.grid(row=3, column=0, padx=6.5, sticky=W)

        self.partymemberslb = Label(self,text=f"Number of Party Members: {str(self.partymembers)}", font="Ariel 18")
        self.partymemberslb.grid(row=4,column=0,sticky=W,padx=(5,10),pady=(5,0))

        self.vspacing = Label(self, text="",height=28)
        self.vspacing.grid(row=5,column=2,sticky=E,columnspan=100)

        self.stay = Button(self, text = "Stay", font="Luminari 24", width = 10, height=2, command=self.lower_supplies)
        self.stay.grid(row=6,column=2,sticky=N)
        
        
        self.raid = Button(self, text = "Raid", font="Luminari 24",width = 10, height=2, command=self.to_battle)
        self.raid.grid(row=6,column=3)

        self.adopt_btn = Button(self, text = "People", font="Luminari 24",width = 10, height=2, command=self.to_adopt)
        self.adopt_btn.grid(row=6,column=4)

        self.hspacing = Label(self,text="",width=100)
        self.hspacing.grid(row=7,column=5,sticky=S,rowspan=100)

        self.spacing=Label(self, text="",height=100)
        self.spacing.grid(row=7,column=4,sticky=E,columnspan=100)

    def lower_supplies(self):
        self.supplies -= 5*self.partymembers
        if self.supplies<=0:
            self.die_base()
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
        self.battle_vspacing.destroy()
        self.battle_vspacing2.destroy()
    
    def destroy_okay(self):
        self.okay.destroy()
        self.fought.destroy()
        self.okay_vspacing.destroy()
        self.okay_spacing2.destroy()
        self.create_base_widgets()
    
    # BATTLE SCREEN PAGE

    def destroy_base_widgets(self):
        if self.partymembers>=1:
            self.angryman_lbl.destroy()
        if self.partymembers>=2:
            self.baldie_lbl.destroy()
        if self.partymembers>=3:
            self.girl_lbl.destroy()
        if self.partymembers>=4:
            self.duck_lbl.destroy()
        if self.partymembers>=5:
            self.dog_lbl.destroy()
        self.bar.destroy()
        self.bar2.destroy()
        self.healthlb.destroy()
        self.supplieslb.destroy()
        self.stay.destroy()
        self.raid.destroy()
        self.vspacing.destroy()
        self.adopt_btn.destroy()
        self.partymemberslb.destroy()
        self.char_lbl.destroy()
  

    def destroy_base_widgets_for_battle(self):
        self.destroy_base_widgets()
        self.create_battle_widgets()
    
    def create_battle_widgets(self):
        # self.columnconfigure(0,weight=2)
        self.image_char = PhotoImage(file = "images/background_battle.png")
        self.char_lbl=Label(self, image = self.image_char)
        self.char_lbl.x = self.image_char
        self.char_lbl.place(x=0, y=0)

        print(self.health)
        print(self.partymembers)
        self.percentage = self.health*(1+self.partymembers/(self.partymembers+15))
        if self.percentage>100:
            self.percentage = 100
        
        self.battle_vspacing=Label(self,text="",height=15)
        self.battle_vspacing.grid(row=0,column=0,sticky=E,columnspan=2)

        self.fighttext = Label(self,text=f"You have a {self.percentage:.1f}% chance of winning. Do you want to fight or run?", font="Luminari 32", width=67)
        self.fighttext.grid(row=1, column=0, columnspan=2, sticky=N)

        self.battle_vspacing2 = Label(self,text="",height=10)
        self.battle_vspacing2.grid(row=2,column=0,sticky=E,columnspan=2)

        self.run_btn = Button(self, text = "Run", font = "Luminari 30", width = 15, command = self.destroy_battle_widgets_for_base)
        self.run_btn.grid(row=2,column=0,sticky=E)

        self.fight_btn = Button(self, text = "Fight", font = "Luminari 30", width = 15, command = self.fight)
        self.fight_btn.grid(row=2,column=1,sticky=W)
    
    def fight(self):
        print("fight started")
        chance=random.randint(0,100)

        self.fought=Label(self,text="")
        self.fought.grid(row=1,column=0)

        self.percentage = self.health*(1+(self.partymembers-1)/self.partymembers)
        if self.percentage>100:
            self.percentage = 100

        if chance<=self.percentage:
            self.fight_count +=1
            if self.fight_count == 12:
                self.live()
            else:
                self.survive()
        else:
            self.die_battle()
    
    def live(self):

        self.image_char = PhotoImage(file = "images/background_live.png")
        self.char_lbl=Label(self, image = self.image_char)
        self.char_lbl.x = self.image_char
        self.char_lbl.place(x=0, y=0)

        self.destroy_battle_widgets()
        self.fought.config(text = f"You fought the zombie and killed all of them. Victory. Bye.")
    
    def survive(self):
        self.destroy_battle_widgets()
        healthlost=random.randint(1, self.health//8) #random way to calculate health lost when you survive; might change it ??
        self.health -= healthlost
        amount = random.randint(0,20)
        self.supplies += amount
        if self.supplies >= 100:
            self.supplies=100
        
        self.okay_vspacing=Label(self,text="",height=13)
        self.okay_vspacing.grid(row=0,column=0,sticky=E)

        self.fought.config(text = f"You fought the zombie and lost {str(healthlost)} health.\n Your health is now at {str(self.health)}.\n\nYou received {amount} supplies.\nYour supplies is now at {str(self.supplies)}",font="Luminari 30",width=70)

        self.okay_spacing2=Label(self, text="", height=2)
        self.okay_spacing2.grid(row=2, column=0, sticky=E)

        self.okay=Button(self,text="Okay", font="Luminari 30", command=self.destroy_okay,width=20,height=2)
        self.okay.grid(row=3,column=0)
    
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

        self.image_char = PhotoImage(file = "images/background_people.png")
        self.char_lbl=Label(self, image = self.image_char)
        self.char_lbl.x = self.image_char
        self.char_lbl.place(x=0, y=0)

        self.adopt_spacing1 = Label(self,text="",height=15)
        self.adopt_spacing1.grid(row=0,column=0,columnspan=2,sticky=E)

        self.partytext = Label(self,text=f"Do you want to adopt or leave? You currently have {self.partymembers} member(s) in your party.", font="Luminari 32",width=66)
        self.partytext.grid(row=1, column=0, columnspan=2, sticky=N)

        self.adopt_spacing2 = Label(self,text="",height=5)
        self.adopt_spacing2.grid(row=2,column=0,columnspan=2,sticky=E)

        self.leave_btn = Button(self, text = "Leave", font = "Luminari 30", width = 15, command = self.destroy_adopt_widgets_noadopt_to_base)
        self.leave_btn.grid(row=3,column=0)

        self.adopt_btn = Button(self, text = "Adopt", font = "Luminari 30", width = 15, command = self.adopt)
        self.adopt_btn.grid(row=3,column=1)

    def destroy_adopt_widgets_noadopt(self):
        self.partytext.destroy()
        self.leave_btn.destroy()
        self.adopt_btn.destroy()
        self.adopt_spacing1.destroy()
        self.adopt_spacing2.destroy()
    def destroy_adopt_widgets_noadopt_to_base(self):
        self.destroy_adopt_widgets_noadopt()
        self.create_base_widgets()
    
    def destroy_adopt_widgets_afteradopt(self):
        self.partytext.destroy()
        self.leave_btn.destroy()
        self.adopt_btn.destroy()
        self.emptylabel.destroy()
        self.okay1.destroy()
        self.adopt_spacing1.destroy()
        self.adopt_spacing2.destroy()
        self.adopt_spacing3.destroy()
        self.adopt_spacing4.destroy()
        self.create_base_widgets()
        print("destroy_adopt_widgets_afteradopt ended")

    def adopt(self):
        print("adopted")

        self.adopt_spacing3=Label(self,text="",height=15)
        self.adopt_spacing3.grid(row=0,column=0,sticky=E)

        self.emptylabel=Label(self,text="",font="Luminari 32",width=67)
        self.emptylabel.grid(row=1,column=0)

        self.adopt_spacing4=Label(self,text="",height=5)
        self.adopt_spacing4.grid(row=2,column=0,sticky=E)

        self.destroy_adopt_widgets_noadopt()
        self.new_party_member()
        self.okay1=Button(self,text=f"Okay", command=self.destroy_adopt_widgets_afteradopt,width=15,height=1,font="Luminari 30")
        self.okay1.grid(row=3,column=0)
    
    def new_party_member(self):
        self.partymembers +=1
        self.emptylabel.config(text = f"A new member joined your party! There are now {self.partymembers} members in your party.")

