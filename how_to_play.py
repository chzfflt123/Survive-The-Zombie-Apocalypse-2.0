from tkinter import *

class How_To_Play(Frame):
    def __init__(self, master, callback_on_htp):
        super(How_To_Play, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.callback_on_htp = callback_on_htp

    def create_widgets(self):
        spacing=Label(self,text=" ",height=8)
        spacing.grid(row=0,column=0)

        heading = Label(self, text = "How to play", font=("Ariel",64),width=31)
        heading.grid(row=1, column=0,sticky=N)

        info = Label(self,text="press the buttons corresponding to whichever location you want to go\nyou could either go explore or stay at home\nif you explore there are many things that will happen and if you survive you will go \nback home and be able to choose again whether to explore or stay home\nyou also have to manage your health and your food throughout the game to avoid \ndeath\nif you survive long enough you live!", font=("Ariel",32),width=62)
        info.grid(row=2, column=0, sticky=W)
    
        next_button = Button(self, text="Next", font = "Ariel 20", width=12, height=2, bg="#A0A0A0", command=self.next)
        next_button.grid(row=3, column=0,sticky=N)
    
    def next(self):
        self.callback_on_htp()