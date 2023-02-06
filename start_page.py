from tkinter import *
class StartPage(Frame):
    
    def __init__(self, master, callback_on_start):
        super().__init__(master)
        self.grid()
        self.create_widgets()
        self.callback_on_start = callback_on_start
    
    def create_widgets(self):
        title1 = Label(self, text = "Survive the Zombie Apocalypse", font = "Times 40", bg="#ffffff")
        title1.grid(row=0, column=0)

        mybutton1 = Button(self, text = "Start", font = "Times 30", width = 15, command = self.start, bg="#ffffff")
        mybutton1.place(x = 312.5, y = 300, anchor=W)
    
    def start(self):
        self.callback_on_start()