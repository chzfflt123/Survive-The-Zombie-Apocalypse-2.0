from tkinter import *
class StartPage(Frame):
    
    def __init__(self, master, callback_on_start):
        super().__init__(master)
        self.grid()
        self.create_widgets()
        self.callback_on_start = callback_on_start
    
    def create_widgets(self):

        mybutton1 = Button(self, text = "Start", font = "Times 30", width = 15, command = self.start)
        mybutton1.place(x=10, y=10)
        title1 = Label(self, text = "Survive the Zombie Apocalypse", font = "Times 40")
        title1.place(x=150, y=150)


        
    
    def start(self):
        self.callback_on_start()