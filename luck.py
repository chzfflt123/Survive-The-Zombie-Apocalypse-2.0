import *
from tkinter

def destroy_base_widgets_for_luck(self):
    self.destroy_base_widgets()
    self.create_luck_widgets()

def create_luck_widgets(self):
    # self.columnconfigure(0,weight=2)
    self.image_char2 = PhotoImage(file = "images/background_battle.png")
    self.char_lbl2=Label(self, image = self.image_char2)
    self.char_lbl2.x = self.image_char2
    self.char_lbl2.place(x=0, y=0)
    
    self.battle_vspacing=Label(self,text="",height=15)
    self.battle_vspacing.grid(row=0,column=0,sticky=E,columnspan=2)

    self.fighttext = Label(self,text=f"You have come to test your luck!!! Choose!!!", font="Luminari 32", width=67)
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