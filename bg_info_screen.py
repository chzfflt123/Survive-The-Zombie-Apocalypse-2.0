from tkinter import *

class BackgroundInfo(Frame):
    def __init__(self, master, callback_on_bginfo):
        super(BackgroundInfo, self).__init__(master)
        self.grid()
        self.callback_on_bginfo = callback_on_bginfo
        self.create_widgets()
    
    def create_widgets(self):

        image123 = PhotoImage(file = "images/start_background.png")
        background=Label(self, image = image123)
        background.x = image123
        background.place(x=0, y=0)

        spacing0=Label(self,text="",width=140)
        spacing0.grid(row=0,column=0)

        spacing1=Label(self,text="",height=5)
        spacing1.grid(row=1,column=0,sticky=E)

        heading = Label(self, text="Background Information", font="Luminari 42 bold", fg="black",width=35)
        heading.grid(row=2, column=0)

        spacing3=Label(self,text=" ",height=3)
        spacing3.grid(row=3,column=0,sticky=E)

        padding=12

        text1 = Label(self, text="Year 2845, the Gods have abandoned human civilization. No one knows what exactly", font="Ariel 24")
        text1.grid(row=4, column=0, columnspan=4, pady=(0, padding))
        text2 = Label(self, text="happened. Just that one day, half the population vanished, and the animals turned", font="Ariel 24")
        text2.grid(row=5, column=0, columnspan=4, pady=(0, padding))
        text3 = Label(self, text="feral. Their eyes turned horrifying red, and their mouths drizzled with their", font="Ariel 24")
        text3.grid(row=6, column=0, columnspan=4, pady=(0, padding))
        text4 = Label(self, text="salvia, their wanting for blood. Even the pets kept in individuals\' households", font="Ariel 24")
        text4.grid(row=7, column=0, columnspan=4, pady=(0, padding))
        text5 = Label(self, text="turned this way, and those who smiled and hugged their pets were bitten. Those", font="Ariel 24")
        text5.grid(row=8, column=0, columnspan=4, pady=(0, padding))
        text6 = Label(self, text="who were bitten, then took the form of more horrifying creatures that can no", font="Georgia 24")
        text6.grid(row=9, column=0, columnspan=4, pady=(0, padding))
        text7 = Label(self, text="longer be called \'human\'.", font="Ariel 24")
        text7.grid(row=10, column=0, columnspan=4, pady=(0, padding))

        spacing=Label(self,text="",height=3)
        spacing.grid(row=11,column=0,sticky=E)

        next_button = Button(self, text="Next", font = "Luminari 20", command=self.next, width=12, height=2, bg="#A0A0A0") # add the command later
        next_button.grid(row=12,column=0,sticky=N)

        spacing4=Label(self,text="",height=100)
        spacing4.grid(row=13,column=0,sticky=E)
    
    def next(self):
        self.callback_on_bginfo()