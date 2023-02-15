from tkinter import *

class BackgroundInfo(Frame):
    def __init__(self, master, callback_on_bginfo):
        super(BackgroundInfo, self).__init__(master)
        self.grid()
        self.callback_on_bginfo = callback_on_bginfo
        self.create_widgets()
        

    
    def create_widgets(self):
        spacing=Label(self,text=" ",height=2)
        spacing.grid(row=0,column=0)

        heading = Label(self, text="Background Information", font="Ariel 40 bold", fg="black",width=43)
        heading.grid(row=1, column=0, columnspan=2)

        spacing=Label(self,text=" ",height=2)
        spacing.grid(row=2,column=0)

        padding=5

        text1 = Label(self, text="Year 2845, the Gods have abandoned human civilization. No one knows what exactly happened.", font="Ariel 24")
        text1.grid(row=3, column=0, columnspan=2, pady=(0, padding))
        text2 = Label(self, text="Just that one day, half the population vanished, and the animals turned feral. Their eyes", font="Ariel 24")
        text2.grid(row=4, column=0, columnspan=2, pady=(0, padding))
        text3 = Label(self, text="turned horrifying red, and their mouths drizzled with their salvia, their wanting for blood.", font="Ariel 24")
        text3.grid(row=5, column=0, columnspan=2, pady=(0, padding))
        text4 = Label(self, text="Even the pets kept in individuals\' households turned this way, and those who smiled and", font="Ariel 24")
        text4.grid(row=6, column=0, columnspan=2, pady=(0, padding))
        text5 = Label(self, text="hugged their pets were bitten. Those who were bitten, then took the form of more horrifying", font="Ariel 24")
        text5.grid(row=7, column=0, columnspan=2, pady=(0, padding))
        text6 = Label(self, text="creatures that can no longer be called \'human\'.", font="Georgia 24")
        text6.grid(row=8, column=0, columnspan=2, pady=(0, padding))

        spacing=Label(self,text=" ",height=5)
        spacing.grid(row=9,column=0)

        next_button = Button(self, text="Next", font = "Ariel 20", command=self.next, width=12, height=2, bg="#A0A0A0") # add the command later
        next_button.grid(row=10,column=0)
        quit_button = Button(self, text="Quit", font = "Ariel 20", width=12, height=2)
        quit_button.grid(row=10,column=1)
    
    def next(self):
        self.callback_on_bginfo()