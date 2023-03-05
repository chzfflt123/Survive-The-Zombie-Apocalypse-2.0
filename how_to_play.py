from tkinter import *

class How_To_Play(Frame):
    def __init__(self, master, callback_on_htp):
        super().__init__(master)
        self.grid()
        self.create_widgets()
        self.callback_on_htp = callback_on_htp

    def create_widgets(self):
        image = PhotoImage(file = "images/start_background.png")
        background=Label(self, image = image)
        background.x = image
        background.place(x=0, y=0)

        spacing1=Label(self,text="",width=140)
        spacing1.grid(row=0,column=1,sticky=E)

        spacing=Label(self,text="",height=5)
        spacing.grid(row=1,column=1,sticky=E)

        heading = Label(self, text = "How To Play", font="Luminari 48 bold",width=31)
        heading.grid(row=2, column=1,sticky=N)

        padding = 12

        spacing3=Label(self,text=" ",height=2)
        spacing3.grid(row=3,column=1,sticky=E)

        info1 = Label(self,text="Press the buttons corresponding to whichever action you want to make", font="Luminari 26",width=62)
        info1.grid(row=4, column=1, sticky=N, pady=(0, padding))
        info2 = Label(self,text="You could either go raid, adjust your party, or stay at home", font="Luminari 26",width=62)
        info2.grid(row=5, column=1, sticky=N, pady=(0, padding))
        info3 = Label(self,text="If you choose to explore many things may happen, based on the decisions you make", font="Luminari 26",width=62)
        info3.grid(row=6, column=1, sticky=N, pady=(0, padding))
        info4 = Label(self,text="Survive and return to base with supplies!", font="Luminari 26",width=62)
        info4.grid(row=7, column=1, sticky=N, pady=(0, padding))
        info5 = Label(self,text="Manage your supplies and health.", font="Luminari 26",width=62)
        info5.grid(row=8, column=1, sticky=N, pady=(0, padding))
        info6 = Label(self,text="New party members can bring supplies but also have mysterious effects.", font="Luminari 26",width=62)
        info6.grid(row=9, column=1, sticky=N, pady=(0, padding))
        info7 = Label(self,text="Stay Alive. MWAHAHAHAHAHA", font="Luminari 26",width=62)
        info7.grid(row=10, column=1, sticky=N, pady=(0, padding))

        spacing4=Label(self,text=" ",height=3)
        spacing4.grid(row=11,column=1,sticky=E)
    
        next_button = Button(self, text="Next", font = "Luminari 20", width=12, height=2, bg="#A0A0A0", command=self.next)
        next_button.grid(row=12, column=1,sticky=N)

        spacing5=Label(self,text="",height=100)
        spacing5.grid(row=13,column=1,sticky=E)
    
    def next(self):
        self.callback_on_htp()