from tkinter import *

class How_To_Play(Frame):
    def __init__(self, master, callback_on_htp):
        super().__init__(master)
        self.grid()
        self.create_widgets()
        self.callback_on_htp = callback_on_htp

    def create_widgets(self):
        spacing1=Label(self,text=" ",height=3)
        spacing1.grid(row=0,column=1)

        spacing2=Label(self,text=" ",width=10)
        spacing2.grid(row=0,column=0)

        heading = Label(self, text = "How To Play", font="Luminari 48 bold",width=31)
        heading.grid(row=1, column=1,sticky=N)

        padding = 12

        spacing3=Label(self,text=" ",height=2)
        spacing3.grid(row=2,column=1)

        info1 = Label(self,text="Press the buttons corresponding to whichever location you want to go", font="Ariel 26",width=62)
        info1.grid(row=3, column=1, sticky=W, pady=(0, padding))
        info2 = Label(self,text="You could either go explore or stay at home", font="Ariel 26",width=62)
        info2.grid(row=4, column=1, sticky=W, pady=(0, padding))
        info3 = Label(self,text="If you explore there are many things that will happen and if you survive you will go", font="Ariel 26",width=62)
        info3.grid(row=5, column=1, sticky=W, pady=(0, padding))
        info4 = Label(self,text="Back home and be able to choose again whether to explore or stay home", font="Ariel 26",width=62)
        info4.grid(row=6, column=1, sticky=W, pady=(0, padding))
        info5 = Label(self,text="You also have to manage your health and your food throughout the game to avoid death", font="Ariel 26",width=62)
        info5.grid(row=7, column=1, sticky=W, pady=(0, padding))
        info7 = Label(self,text="If you survive long enough you live!", font="Ariel 26",width=62)
        info7.grid(row=8, column=1, sticky=W, pady=(0, padding))

        spacing4=Label(self,text=" ",height=6)
        spacing4.grid(row=9,column=1)
    
        next_button = Button(self, text="Next", font = "Luminari 20", width=12, height=2, bg="#A0A0A0", command=self.next)
        next_button.grid(row=10, column=1,sticky=N)
    
    def next(self):
        self.callback_on_htp()