from tkinter import *

class BackgroundInfo(Frame):
    def __init__(self, master, callback_on_bginfo):
        super(BackgroundInfo, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.callback_on_bginfo = callback_on_bginfo

    
    def create_widgets(self):
        heading = Label(self, text="Background Information", font="Georgia 40 bold", fg="black", bg="#F0F0F0")
        heading.grid(row=0, column=0)

        i = 50
        bg_color = "#F0F0F0"

        text1 = Label(self, text="Year 2845, the Gods have abandoned human civilization. No one knows what exactly happened.", font="Georgia 24", bg=bg_color)
        text1.grid(row=1, column=0)
        text2 = Label(self, text="Just that one day, half the population vanished, and the animals turned feral. Their eyes", font="Georgia 24", bg=bg_color)
        text2.place(row=2, column=0)
        text3 = Label(self, text="turned horrifying red, and their mouths drizzled with their salvia, their wanting for blood.", font="Georgia 24", bg=bg_color)
        text3.place(row=3, column=0)
        text4 = Label(self, text="Even the pets kept in individuals\' households turned this way, and those who smiled and", font="Georgia 24", bg=bg_color)
        text4.place(row=4, column=0)
        text5 = Label(self, text="hugged their pets were bitten. Those who were bitten, then took the form of more horrifying", font="Georgia 24", bg=bg_color)
        text5.place(row=5, column=0)
        text6 = Label(self, text="creatures that can no longer be called \'human\'.", font="Georgia 24", bg=bg_color)
        text6.place(row=6, column=0)

        next_button = Button(self, text="Next", font = "Ariel 20", width=12, height=2, bg="#A0A0A0") # add the command later
        next_button.grid(row=7,column=0)
        quit_button = Button(self, text="Quit", font = "Ariel 20", command=self.quit_game, width=12, height=2)
        quit_button.grid(row=7,column=1)
    
    def quit_game(self):
        self.destroy()