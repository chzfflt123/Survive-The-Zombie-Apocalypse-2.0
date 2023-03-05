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
        self.bar.grid(column=0, row=0, padx = 10, pady=(10, 0), sticky=W)
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
        self.vspacing.grid(row=5,column=2,sticky=E,columnspan=2)

        self.wspacing = Label(self, text="", width=50)
        self.wspacing.grid(row=10, column=0)

        self.stay = Button(self, text = "Stay", font="Luminari 24", width = 7, height=2, command=self.lower_supplies)
        self.stay.grid(row=6,column=0,sticky=E)

        self.raid = Button(self, text = "Fight", font="Luminari 24",width = 7, height=2, command=self.to_battle)
        self.raid.grid(row=6,column=1, sticky=W)

        self.adopt_btn = Button(self, text = "People", font="Luminari 24",width = 7, height=2, command=self.to_adopt)
        self.adopt_btn.grid(row=6,column=2, sticky=W)

        self.kill_btn = Button(self, text="Kill", font="Luminari 24", width=7, height=2, command=self.kill)
        self.kill_btn.grid(row=6, column=3, sticky=W)

        self.lucky_btn = Button(self, text = "Lucky???", font="Luminari 24", width = 7, height = 2, command=self.destroy_base_widgets_for_luck)
        self.lucky_btn.grid(row=6, column=4)

        self.hspacing = Label(self,text="",width=100)
        self.hspacing.grid(row=7,column=6,sticky=S,rowspan=100)

        self.spacing=Label(self, text="",height=100)
        self.spacing.grid(row=7,column=5,sticky=E,columnspan=100)

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
        self.kill_btn.destroy()
        self.wspacing.destroy()
  
    def destroy_okay(self):
        self.okay.destroy()
        self.fought.destroy()
        self.okay_vspacing.destroy()
        self.okay_spacing2.destroy()
        self.create_base_widgets()

    def destroy_base_widgets_for_battle(self):
        self.destroy_base_widgets()
        self.create_battle_widgets()
    
    def create_battle_widgets(self):
        # self.columnconfigure(0,weight=2)
        self.image_char2 = PhotoImage(file = "images/background_battle.png")
        self.char_lbl2=Label(self, image = self.image_char2)
        self.char_lbl2.x = self.image_char2
        self.char_lbl2.place(x=0, y=0)

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
    
    def kill(self):
        self.destroy_base_widgets()
        self.image_char = PhotoImage(file = "images/background_people.png")
        self.char_lbl=Label(self, image = self.image_char)
        self.char_lbl.x = self.image_char
        self.char_lbl.place(x=0, y=0)

        self.kill_vspacing=Label(self,text="",height=18)
        self.kill_vspacing.grid(row=0,column=0,sticky=E,columnspan=2)

        self.percentage = (self.health*((self.partymembers-1)/self.partymembers) + 100) /2
        if self.percentage>100:
            self.percentage = 100

        if self.partymembers > 1:
            self.kill_text = f"You have a {self.percentage:.1f}% chance of survival. Would you like to kill a party member?"
        else:
            self.kill_text = "You have no party members to kill"

        self.aspacing=Label(self, text="", height=2)
        self.aspacing.grid(row=2, column=100)
        
        self.kill_text_lb = Label(self, text=self.kill_text, font="Luminari 32", width=67)
        self.kill_text_lb.grid(row=1, column=0, columnspan=2)

        self.kill_yes = Button(self, text="Yes", font="Luminari 30", width=15, command=self.member_killed)
        self.kill_no = Button(self, text="No", font="Luminari 30", width=15, command=self.kill_to_base)

        self.kill_back = Button(self, text="Back to Base", font="Luminari 30", width=15, command=self.kill_to_base)

        if self.partymembers > 1:
            self.kill_yes.grid(row=3, column=0)
            self.kill_no.grid(row=3, column=1)
        else:
            self.kill_back.grid(row=3, column=0, columnspan=2)

    def member_killed(self):
        chance=random.randint(0,100)

        self.percentage = (self.health*((self.partymembers-1)/self.partymembers) + 100)/2
        if self.percentage>100:
            self.percentage = 100

        if chance<=self.percentage:
            print("you killed a party member")
            self.partymembers -= 1
            self.kill_to_base()
        else:
            self.die_kill()

    def destroy_kill_widgets(self):
        self.kill_yes.destroy()
        self.kill_no.destroy()
        self.kill_back.destroy()
        self.kill_text_lb.destroy()
        self.aspacing.destroy()
        self.kill_vspacing.destroy()
    
    def die_kill(self):
        self.destroy_kill_widgets()
        self.image_char = PhotoImage(file = "images/deadlol.png")
        self.char_lbl=Label(self, image = self.image_char)
        self.char_lbl.x = self.image_char
        self.char_lbl.place(x=0, y=0)
    
    def kill_to_base(self):
        self.create_base_widgets()
        self.destroy_kill_widgets()
    
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
        self.image_char = PhotoImage(file = "images/deadlol.png")
        self.char_lbl=Label(self, image = self.image_char)
        self.char_lbl.x = self.image_char
        self.char_lbl.place(x=0, y=0)

    def die_battle(self):
        self.destroy_battle_widgets()
        self.image_char = PhotoImage(file = "images/deadlol.png")
        self.char_lbl=Label(self, image = self.image_char)
        self.char_lbl.x = self.image_char
        self.char_lbl.place(x=0, y=0)

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
    
    def destroy_okay_lucky(self):
        self.luck_vspacing.destroy()
        self.luck_vspacing2.destroy()
        self.AM_btn.destroy()
        self.NZ_btn.destroy()
        self.okay.destroy()
        self.luckytext.destroy()
        self.endluck_vspacing.destroy()
        self.endluck_spacing2.destroy()
        self.create_base_widgets()
    
    def destroy_create_luck_widgets(self):
        self.luck_vspacing.destroy()
        self.luck_vspacing2.destroy()
        self.AM_btn.destroy()
        self.NZ_btn.destroy()

    def destroy_base_widgets_for_luck(self):
        self.destroy_base_widgets()
        self.create_luck_widgets()

    def create_luck_widgets(self):
        # self.columnconfigure(0,weight=2)
        self.image_char2 = PhotoImage(file = "images/background_battle.png")
        self.char_lbl2=Label(self, image = self.image_char2)
        self.char_lbl2.x = self.image_char2
        self.char_lbl2.place(x=0, y=0)
        
        self.luck_vspacing=Label(self,text="",height=15)
        self.luck_vspacing.grid(row=0,column=0,sticky=E,columnspan=2)

        self.luckytext = Label(self,text=f"You have come to test your luck!!! Choose!!!", font="Luminari 32", width=67)
        self.luckytext.grid(row=1, column=0, columnspan=2, sticky=N)

        self.luck_vspacing2 = Label(self,text="",height=10)
        self.luck_vspacing2.grid(row=2,column=0,sticky=E,columnspan=2)

        self.AM_btn = Button(self, text = "A-M", font = "Luminari 30", width = 15, command = self.luckam)
        self.AM_btn.grid(row=2,column=0,sticky=E)

        self.NZ_btn = Button(self, text = "N-Z", font = "Luminari 30", width = 15, command = self.lucknz)
        self.NZ_btn.grid(row=2,column=1,sticky=W)

    def luckam(self):
        # self.columnconfigure(0,weight=2)
        self.destroy_create_luck_widgets()
        
        self.luck_vspacing=Label(self,text="",height=15)
        self.luck_vspacing.grid(row=0,column=0,sticky=E,columnspan=2)

        self.luckytext = Label(self,text=f"HMMMM!!! Choose!!!", font="Luminari 32", width=67)
        self.luckytext.grid(row=1, column=0, columnspan=2, sticky=N)

        self.luck_vspacing2 = Label(self,text="",height=10)
        self.luck_vspacing2.grid(row=2,column=0,sticky=E,columnspan=2)

        self.AM_btn = Button(self, text = "1-99", font = "Luminari 30", width = 15, command = self.luck199)
        self.AM_btn.grid(row=2,column=0,sticky=E)

        self.NZ_btn = Button(self, text = "100", font = "Luminari 30", width = 15, command = self.luck100)
        self.NZ_btn.grid(row=2,column=1,sticky=W)

    def luck199(self):
        # self.columnconfigure(0,weight=2)
        self.destroy_create_luck_widgets()
        
        self.luck_vspacing=Label(self,text="",height=15)
        self.luck_vspacing.grid(row=0,column=0,sticky=E,columnspan=2)

        self.luckytext = Label(self,text=f"Interesting!!! Choose!!!", font="Luminari 32", width=67)
        self.luckytext.grid(row=1, column=0, columnspan=2, sticky=N)

        self.luck_vspacing2 = Label(self,text="",height=10)
        self.luck_vspacing2.grid(row=2,column=0,sticky=E,columnspan=2)

        self.AM_btn = Button(self, text = "Rrrrred", font = "Luminari 30", width = 15, command = self.luckred)
        self.AM_btn.grid(row=2,column=0,sticky=E)

        self.NZ_btn = Button(self, text = "Bllllue", font = "Luminari 30", width = 15, command = self.luckblue)
        self.NZ_btn.grid(row=2,column=1,sticky=W)

    def luckred(self):
        self.destroy_create_luck_widgets()
        
        self.endluck_vspacing=Label(self,text="",height=13)
        self.endluck_vspacing.grid(row=0,column=0,columnspan=2, sticky=E)

        self.health = 5
        self.luckytext.config(text = f"You made your choices.\n Your health is now at 5.\n\nGood luck surviving.\nIf you can. MWAHAHAHAHA",font="Luminari 30",width=70)

        self.endluck_spacing2=Label(self, text="", height=5)
        self.endluck_spacing2.grid(row=2, column=0, sticky=E,columnspan=2)

        self.okay=Button(self,text="Okay", font="Luminari 30", command=self.destroy_okay_lucky,width=10,height=2)
        self.okay.grid(row=3,column=0,sticky=N,columnspan=2)     

    def luckblue(self):
        self.destroy_create_luck_widgets()

        self.endluck_vspacing=Label(self,text="",height=13)
        self.endluck_vspacing.grid(row=0,column=0,sticky=E,columnspan=2)

        self.health = 95
        self.luckytext.config(text = f"You made your choices.\n Your health is now at 95.\n\nYou, are very lucky.\nGood luck with survival...sigh",font="Luminari 30",width=70)

        self.endluck_spacing2=Label(self, text="", height=5)
        self.endluck_spacing2.grid(row=2, column=0, sticky=E,columnspan=2)

        self.okay=Button(self,text="Okay", font="Luminari 30", command=self.destroy_okay_lucky,width=10,height=2)
        self.okay.grid(row=3,column=0,columnspan=2)

    def luck100(self):
        # self.columnconfigure(0,weight=2)
        self.destroy_create_luck_widgets()
        
        self.luck_vspacing=Label(self,text="",height=15)
        self.luck_vspacing.grid(row=0,column=0,sticky=E,columnspan=2)

        self.luckytext = Label(self,text=f"Sigh. Choose Human.", font="Luminari 32", width=67)
        self.luckytext.grid(row=1, column=0, columnspan=2, sticky=N)

        self.luck_vspacing2 = Label(self,text="",height=10)
        self.luck_vspacing2.grid(row=2,column=0,sticky=E,columnspan=2)

        self.AM_btn = Button(self, text = "Food", font = "Luminari 30", width = 15, command = self.luckfood)
        self.AM_btn.grid(row=2,column=0,sticky=E)

        self.NZ_btn = Button(self, text = "School", font = "Luminari 30", width = 15, command = self.luckschool)
        self.NZ_btn.grid(row=2,column=1,sticky=W)

    def luckschool(self):
        self.destroy_create_luck_widgets()

        self.endluck_vspacing=Label(self,text="",height=13)
        self.endluck_vspacing.grid(row=0,column=0,sticky=E,columnspan=2)

        self.health = random.randint(1,10)
        self.supplies = random.randint(1,10)
        self.luckytext.config(text = f"Why would you do that?!?\n Your health is now at {str(self.health)}.\n Your supplies are at {str(self.supplies)}\n\nHonestly, you are hopeless.\nSee you around... If you're around",font="Luminari 30",width=70)

        self.endluck_spacing2=Label(self, text="", height=2)
        self.endluck_spacing2.grid(row=2, column=0, sticky=E,columnspan=2)

        self.okay=Button(self,text="Okay", font="Luminari 30", command=self.destroy_okay_lucky,width=10,height=2)
        self.okay.grid(row=3,column=0,columnspan=2)     

    def luckfood(self):
        self.destroy_create_luck_widgets()

        self.endluck_vspacing=Label(self,text="",height=13)
        self.endluck_vspacing.grid(row=0,column=0,sticky=E,columnspan=2)

        self.supplies = random.randint(30,50)
        self.luckytext.config(text = f"I like food too.\n Buuuuut I think you need to keep a healthy diet.\n\nYour food supply is at {str(self.supplies)}.\nWhat you eat is very important",font="Luminari 30",width=70)

        self.endluck_spacing2=Label(self, text="", height=2)
        self.endluck_spacing2.grid(row=2, column=0, sticky=E,columnspan=2)

        self.okay=Button(self,text="Okay", font="Luminari 30", command=self.destroy_okay_lucky,width=10,height=2)
        self.okay.grid(row=3,column=0,columnspan=2)

    def lucknz(self):
        # self.columnconfigure(0,weight=2)
        self.destroy_create_luck_widgets()
        
        self.luck_vspacing=Label(self,text="",height=15)
        self.luck_vspacing.grid(row=0,column=0,sticky=E,columnspan=2)

        self.luckytext = Label(self,text=f"Woah... You're weird aren't you...? Let's see how weird you are.", font="Luminari 32", width=67)
        self.luckytext.grid(row=1, column=0, columnspan=2, sticky=N)

        self.luck_vspacing2 = Label(self,text="",height=10)
        self.luck_vspacing2.grid(row=2,column=0,sticky=E,columnspan=2)

        self.AM_btn = Button(self, text = "Oink", font = "Luminari 30", width = 15, command = self.luckoink)
        self.AM_btn.grid(row=2,column=0,sticky=E)

        self.NZ_btn = Button(self, text = "Mooo", font = "Luminari 30", width = 15, command = self.luckmooo)
        self.NZ_btn.grid(row=2,column=1,sticky=W)

    def luckoink(self):
        # self.columnconfigure(0,weight=2)
        self.destroy_create_luck_widgets()
        
        self.luck_vspacing=Label(self,text="",height=15)
        self.luck_vspacing.grid(row=0,column=0,sticky=E,columnspan=2)

        self.luckytext = Label(self,text=f"Oink, oink, oink. OINK!!!! (= When, is, your. BIRTHDAY!!!!)", font="Luminari 32", width=67)
        self.luckytext.grid(row=1, column=0, columnspan=2, sticky=N)

        self.luck_vspacing2 = Label(self,text="",height=10)
        self.luck_vspacing2.grid(row=2,column=0,sticky=E,columnspan=2)

        self.AM_btn = Button(self, text = "1-6", font = "Luminari 30", width = 15, command = self.luck16)
        self.AM_btn.grid(row=2,column=0,sticky=E)

        self.NZ_btn = Button(self, text = "7-12", font = "Luminari 30", width = 15, command = self.luck712)
        self.NZ_btn.grid(row=2,column=1,sticky=W)

    def luck16(self):
        self.destroy_create_luck_widgets()

        self.endluck_vspacing=Label(self,text="",height=13)
        self.endluck_vspacing.grid(row=0,column=0,sticky=E,columnspan=2)

        self.dice = random.randint(0,1)
        if self.dice == 0:
            self.health = 1
        if self.dice == 1:
            self.health = 100
        self.luckytext.config(text = f"I can't believe you tried to gamble your health.\n Your health is now at {str(self.health)}.\n\nYou know, it was a 1 or 100.\nI really don't know if it was worth it.",font="Luminari 30",width=70)

        self.endluck_spacing2=Label(self, text="", height=2)
        self.endluck_spacing2.grid(row=2, column=0, sticky=E,columnspan=2)

        self.okay=Button(self,text="Okay", font="Luminari 30", command=self.destroy_okay_lucky,width=10,height=2)
        self.okay.grid(row=3,column=0,columnspan=2)     

    def luck712(self):
        self.destroy_create_luck_widgets()

        self.endluck_vspacing=Label(self,text="",height=13)
        self.endluck_vspacing.grid(row=0,column=0,sticky=E,columnspan=2)

        self.dice = random.randint(0,1)
        if self.dice == 0:
            self.supplies = 1
        if self.dice == 1:
            self.supplies = 100
        self.luckytext.config(text = f"You gambled whaaaat?\n Your supplies?!?\n\nYour supply level is at {str(self.supplies)}.\nJust know, if you don't have any supplies, you may just...",font="Luminari 30",width=70)

        self.endluck_spacing2=Label(self, text="", height=2)
        self.endluck_spacing2.grid(row=2, column=0, sticky=E,columnspan=2)

        self.okay=Button(self,text="Okay", font="Luminari 30", command=self.destroy_okay_lucky,width=10,height=2)
        self.okay.grid(row=3,column=0,columnspan=2)

    def luckmooo(self):
        # self.columnconfigure(0,weight=2)
        self.destroy_create_luck_widgets()
        
        self.luck_vspacing=Label(self,text="",height=15)
        self.luck_vspacing.grid(row=0,column=0,sticky=E,columnspan=2)

        self.luckytext = Label(self,text=f"True or False: Cows can be 5ft tall?", font="Luminari 32", width=67)
        self.luckytext.grid(row=1, column=0, columnspan=2, sticky=N)

        self.luck_vspacing2 = Label(self,text="",height=10)
        self.luck_vspacing2.grid(row=2,column=0,sticky=E,columnspan=2)

        self.AM_btn = Button(self, text = "Yees", font = "Luminari 30", width = 15, command = self.lucky)
        self.AM_btn.grid(row=2,column=0,sticky=E)

        self.NZ_btn = Button(self, text = "Noope", font = "Luminari 30", width = 15, command = self.luckn)
        self.NZ_btn.grid(row=2,column=1,sticky=W)

    def lucky(self):
        self.destroy_create_luck_widgets()
        self.endluck_vspacing=Label(self,text="",height=13)
        self.endluck_vspacing.grid(row=0,column=0,sticky=E,columnspan=2)

        self.health = 75
        self.luckytext.config(text = f"Wow...\n You cheated, didn't you\n Your health is now at 75.\n\nJust know I'm not encouraging cheating.\nThere just is that tiny possibility you actually knew...(wink)",font="Luminari 30",width=70)

        self.endluck_spacing2=Label(self, text="", height=2)
        self.endluck_spacing2.grid(row=2, column=0, sticky=E,columnspan=2)

        self.okay=Button(self,text="Okay", font="Luminari 30", command=self.destroy_okay_lucky,width=10,height=2)
        self.okay.grid(row=3,column=0,columnspan=2)     

    def luckn(self):
        self.destroy_create_luck_widgets()
        
        self.endluck_vspacing=Label(self,text="",height=13)
        self.endluck_vspacing.grid(row=0,column=0,sticky=E,columnspan=2)

        self.health = 100
        self.supplies = 100
        self.luckytext.config(text = f"You didn't know...\nWell, cows can grow up to 6ft 4in.\nBut since you were sincere,\n\nYour health is at {str(self.health)}.\nYour supply is at {str(self.supplies)}.",font="Luminari 30",width=70)

        self.endluck_spacing2=Label(self, text="", height=2)
        self.endluck_spacing2.grid(row=2, column=0, sticky=E,columnspan=2)

        self.okay=Button(self,text="Okay", font="Luminari 30", command=self.destroy_okay_lucky,width=10,height=2)
        self.okay.grid(row=3,column=0,columnspan=2)