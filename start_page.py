from tkinter import *
from tkinter import font
class StartPage(Frame):
    def __init__(self, master, callback_on_start):
        super().__init__(master)
        self.grid()
        self.create_widgets()
        self.callback_on_start = callback_on_start
    
    def create_widgets(self):
        image = PhotoImage(file = "images/start_background.png")
        background=Label(self, image = image)
        background.x = image
        background.place(x=0, y=0)
    
        print(list(font.families()))

        spacing1=Label(self,text=" ",height=19)
        spacing1.grid(row=0,column=0,sticky=E)

        title1 = Label(self, text = "Survive the Zombie Apocalypse", font = ("Luminari 40"),width=52)
        title1.grid(row=1, column=0, sticky=N)
        

        spacing2=Label(self,text=" ",height=1)
        spacing2.grid(row=2,column=0,sticky=E)

        mybutton1 = Button(self, text = "Start", font = "Times 30", width = 15, command = self.start)
        mybutton1.grid(row=3, column=0,sticky=N)

        spacing3=Label(self,text="",height=100)
        spacing3.grid(row=4,column=0,sticky=E)
    
    def start(self):
        self.callback_on_start()