from tkinter import *

class How_To_Play(Frame):
    def __init__(self, master, callback_on_htp):
        super(How_To_Play, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.current_screen=None
        self.callback_on_htp = callback_on_htp

    def create_widgets(self):
        heading = Label(self, text = "How to play", font=("Ariel",72))
        heading.place(x=625, y=100, anchor = CENTER)

        Label(self,text="press the buttons corresponding to whichever location you want to go\nyou could either go explore or stay at home\nif you explore there are many things that will happen and if you survive you will go \nback home and be able to choose again whether to explore or stay home\nyou also have to manage your health and your food throughout the game to avoid \ndeath\nif you survive long enough you live!", font=("Ariel",32)).place(x=625,y=300, anchor=CENTER)
    
        next_button = Button(self, text="Next", font = "Ariel 20", width=12, height=2, bg="#A0A0A0")
        next_button.place(x=525, y=600, anchor=CENTER)

        quit_button = Button(self, text="Quit", font = "Ariel 20", width=12, height=2)
        quit_button.place(x=725, y=600, anchor=CENTER)
    
    def next(self):
        self.callback_on_htp()