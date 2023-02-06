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
        mybutton1.grid(row=1,column=0)
    
    def start(self):
        self.callback_on_start()
    
# root = Tk()
# root.title("Start")
# root.geometry(1250,750)
# app = StartPage(root)
# root.mainloop()