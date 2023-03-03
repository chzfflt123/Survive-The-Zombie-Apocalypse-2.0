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

def destroy_create_luck_widgets(self):
    self.luck_vspacing.destroy()
    self.luckytext.destroy()
    self.luck_vspacing2.destroy()
    self.AM_btn.destroy()
    self.NZ_btn.destroy()

def luckam(self):
    # self.columnconfigure(0,weight=2)
    destroy_create_luck_widgets()
    
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
    destroy_create_luck_widgets()
    
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
    self.okay_vspacing=Label(self,text="",height=13)
    self.okay_vspacing.grid(row=0,column=0,sticky=E)

    self.health = 5
    self.fought.config(text = f"You made your choices.\n Your health is now at 5.\n\nGood luck surviving.\nIf you can. MWAHAHAHAHA",font="Luminari 30",width=70)

    self.okay_spacing2=Label(self, text="", height=2)
    self.okay_spacing2.grid(row=2, column=0, sticky=E)

    self.okay=Button(self,text="Okay", font="Luminari 30", command=self.destroy_okay,width=20,height=2)
    self.okay.grid(row=3,column=0)     

def luckblue(self):
    self.okay_vspacing=Label(self,text="",height=13)
    self.okay_vspacing.grid(row=0,column=0,sticky=E)

    self.supplies = 95
    self.fought.config(text = f"You made your choices.\n Your health is now at 95.\n\nYou, are very lucky.\nGood luck with survival...sigh",font="Luminari 30",width=70)

    self.okay_spacing2=Label(self, text="", height=2)
    self.okay_spacing2.grid(row=2, column=0, sticky=E)

    self.okay=Button(self,text="Okay", font="Luminari 30", command=self.destroy_okay,width=20,height=2)
    self.okay.grid(row=3,column=0)

def luck100(self):
    # self.columnconfigure(0,weight=2)
    destroy_create_luck_widgets()
    
    self.luck_vspacing=Label(self,text="",height=15)
    self.luck_vspacing.grid(row=0,column=0,sticky=E,columnspan=2)

    self.luckytext = Label(self,text=f"Sigh. Choose Human.", font="Luminari 32", width=67)
    self.luckytext.grid(row=1, column=0, columnspan=2, sticky=N)

    self.luck_vspacing2 = Label(self,text="",height=10)
    self.luck_vspacing2.grid(row=2,column=0,sticky=E,columnspan=2)

    self.AM_btn = Button(self, text = "Food", font = "Luminari 30", width = 15, command = self.luckred)
    self.AM_btn.grid(row=2,column=0,sticky=E)

    self.NZ_btn = Button(self, text = "School", font = "Luminari 30", width = 15, command = self.luckblue)
    self.NZ_btn.grid(row=2,column=1,sticky=W)

def luckschool(self):
    self.okay_vspacing=Label(self,text="",height=13)
    self.okay_vspacing.grid(row=0,column=0,sticky=E)

    self.health = random.randint(1,10)
    self.supplies = random.randint(1,10)
    self.fought.config(text = f"Why would you do that?!?\n Your health is now at {str(self.health)}.\n Your supplies are at {str(self.supplies)}\n\nHonestly, you are hopeless.\nSee you around... If you're around",font="Luminari 30",width=70)

    self.okay_spacing2=Label(self, text="", height=2)
    self.okay_spacing2.grid(row=2, column=0, sticky=E)

    self.okay=Button(self,text="Okay", font="Luminari 30", command=self.destroy_okay,width=20,height=2)
    self.okay.grid(row=3,column=0)     

def luckfood(self):
    self.okay_vspacing=Label(self,text="",height=13)
    self.okay_vspacing.grid(row=0,column=0,sticky=E)

    self.supplies = random.randint(30,50)
    self.fought.config(text = f"I like food too.\n Buuuuut I think you need to keep a healthy diet.\n\nYou're (food) supply is at {str(self.supplies)}.\nWhat you eat is very important",font="Luminari 30",width=70)

    self.okay_spacing2=Label(self, text="", height=2)
    self.okay_spacing2.grid(row=2, column=0, sticky=E)

    self.okay=Button(self,text="Okay", font="Luminari 30", command=self.destroy_okay,width=20,height=2)
    self.okay.grid(row=3,column=0)

def lucknz(self):
    # self.columnconfigure(0,weight=2)
    destroy_create_luck_widgets()
    
    self.luck_vspacing=Label(self,text="",height=15)
    self.luck_vspacing.grid(row=0,column=0,sticky=E,columnspan=2)

    self.luckytext = Label(self,text=f"Woah... You're wierd aren't you...? Let's see how wierd you are.", font="Luminari 32", width=67)
    self.luckytext.grid(row=1, column=0, columnspan=2, sticky=N)

    self.luck_vspacing2 = Label(self,text="",height=10)
    self.luck_vspacing2.grid(row=2,column=0,sticky=E,columnspan=2)

    self.AM_btn = Button(self, text = "Oink", font = "Luminari 30", width = 15, command = self.luckoink)
    self.AM_btn.grid(row=2,column=0,sticky=E)

    self.NZ_btn = Button(self, text = "Mooo", font = "Luminari 30", width = 15, command = self.luckmooo)
    self.NZ_btn.grid(row=2,column=1,sticky=W)

def luckoink(self):
    # self.columnconfigure(0,weight=2)
    destroy_create_luck_widgets()
    
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
    self.okay_vspacing=Label(self,text="",height=13)
    self.okay_vspacing.grid(row=0,column=0,sticky=E)

    self.dice = random.randint(0,1)
    if self.dice == 0:
        self.health = 1
    if self.dice == 1:
        self.health = 100
    self.fought.config(text = f"I can't believe you tried to gamble your health.\n Your health is now at {str(self.health)}.\n\nYou know, it was a 1 or 100.\nI really don't know if it was worth it.",font="Luminari 30",width=70)

    self.okay_spacing2=Label(self, text="", height=2)
    self.okay_spacing2.grid(row=2, column=0, sticky=E)

    self.okay=Button(self,text="Okay", font="Luminari 30", command=self.destroy_okay,width=20,height=2)
    self.okay.grid(row=3,column=0)     

def luck719(self):
    self.okay_vspacing=Label(self,text="",height=13)
    self.okay_vspacing.grid(row=0,column=0,sticky=E)

    self.dice = random.randint(0,1)
    if self.dice == 0:
        self.supplies = 1
    if self.dice == 1:
        self.supplies = 100
    self.fought.config(text = f"You gambled whaaaat?\n Your supplies?!?\n\nYou're supply is at {str(self.supplies)}.\nJust know, if you don't have any supplies, you may just...",font="Luminari 30",width=70)

    self.okay_spacing2=Label(self, text="", height=2)
    self.okay_spacing2.grid(row=2, column=0, sticky=E)

    self.okay=Button(self,text="Okay", font="Luminari 30", command=self.destroy_okay,width=20,height=2)
    self.okay.grid(row=3,column=0)

def luckmooo(self):
    # self.columnconfigure(0,weight=2)
    destroy_create_luck_widgets()
    
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
    self.okay_vspacing=Label(self,text="",height=13)
    self.okay_vspacing.grid(row=0,column=0,sticky=E)

    self.fought.config(text = f"Wow...\n You cheated, didn't you\n Your health is now at 75.\n\nJust know I'm not encouraging cheating.\nThere just is that tiny possibility you actually knew...(wink)",font="Luminari 30",width=70)

    self.okay_spacing2=Label(self, text="", height=2)
    self.okay_spacing2.grid(row=2, column=0, sticky=E)

    self.okay=Button(self,text="Okay", font="Luminari 30", command=self.destroy_okay,width=20,height=2)
    self.okay.grid(row=3,column=0)     

def luckn(self):
    self.okay_vspacing=Label(self,text="",height=13)
    self.okay_vspacing.grid(row=0,column=0,sticky=E)

    self.health = 100
    self.supplies = 100
    self.fought.config(text = f"You didn't know...\nWell, cows can grow up to 6ft 4in.\nBut since you were sincere,\n\nYour health is at {str(self.health)}.\nYour supply is at {str(self.supplies)}.",font="Luminari 30",width=70)

    self.okay_spacing2=Label(self, text="", height=2)
    self.okay_spacing2.grid(row=2, column=0, sticky=E)

    self.okay=Button(self,text="Okay", font="Luminari 30", command=self.destroy_okay,width=20,height=2)
    self.okay.grid(row=3,column=0)