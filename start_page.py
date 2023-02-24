from tkinter import *
class StartPage(Frame):
    
    def __init__(self, master, callback_on_start):
        super().__init__(master)
        self.grid()
        self.create_widgets()
        self.callback_on_start = callback_on_start
    
    def create_widgets(self):
        spacing=Label(self,text=" ",height=19)
        spacing.grid(row=0,column=0)

        title1 = Label(self, text = "Survive the Zombie Apocalypse", font = "Times 40 bold",width=63)
        title1.grid(row=1, column=0, sticky=N)

        spacing=Label(self,text=" ",height=1)
        spacing.grid(row=2,column=0)

        mybutton1 = Button(self, text = "Start", font = "Times 30", width = 15, command = self.start)
        mybutton1.grid(row=3, column=0,sticky=N)
    
    def start(self):
        self.callback_on_start()