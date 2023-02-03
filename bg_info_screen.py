from tkinter import *

class BackgroundInfo(Frame):
    def __init__(self, master):
        super(BackgroundInfo, self).__init__(master)
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        Label(root, text="Background Information", font="Georgia 40 bold", fg="black", bg="#F0F0F0").place(x=625, y=60, anchor=CENTER)

        i = 50
        bg_color = "#F0F0F0"

        text1 = Label(root, text="Year 2845, the Gods have abandoned human civilization. No one knows what exactly happened.", font="Georgia 24", bg=bg_color)
        text1.place(x=625, y=150, anchor=CENTER)
        text2 = Label(root, text="Just that one day, half the population vanished, and the animals turned feral. Their eyes", font="Georgia 24", bg=bg_color)
        text2.place(x=625, y=150+i, anchor=CENTER)
        text3 = Label(root, text="turned horrifying red, and their mouths drizzled with their salvia, their wanting for blood.", font="Georgia 24", bg=bg_color)
        text3.place(x=625, y=150+i*2, anchor=CENTER)
        text4 = Label(root, text="Even the pets kept in individuals\' households turned this way, and those who smiled and", font="Georgia 24", bg=bg_color)
        text4.place(x=625, y=150+i*3, anchor=CENTER)
        text5 = Label(root, text="hugged their pets were bitten. Those who were bitten, then took the form of more horrifying", font="Georgia 24", bg=bg_color)
        text5.place(x=625, y=150+i*4, anchor=CENTER)
        text6 = Label(root, text="creatures that can no longer be called \'human\'.", font="Georgia 24", bg=bg_color)
        text6.place(x=625, y=150+i*5, anchor=CENTER)

        next_button = Button(root, text="Next", font = "Ariel 20", width=12, height=2, bg="#A0A0A0") # add the command later
        next_button.place(x=525, y=600, anchor=CENTER)
        quit_button = Button(root, text="Quit", font = "Ariel 20", command=self.quit_game, width=12, height=2)
        quit_button.place(x=725, y=600, anchor=CENTER)
    
    def quit_game(self):
        root.destroy()
        

root = Tk()
root.title("Background Information")
root.geometry("1250x750")
app = BackgroundInfo(root)
bg_color = "#F0F0F0"
root.config(bg=bg_color)
root.resizable(width=False,height=False)
root.mainloop()