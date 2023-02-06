from tkinter import *
import os

class EventRaid():
    
    def __init__(self, master):
        super(EventRaid, self).__init__(master)
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        mybutton1 = Button(root, text = "Stay", font = "Times 30", width = 15, command = self.start, bg="#ffffff")
        mybutton1.place(x = 312.5, y = 300, anchor=W)

        mybutton2 = Button(root, text = "Raid", font = "Times 30", width = 15, command = self.quit, bg="#ffffff")
        mybutton2.place(x = 660, y = 300, anchor=W)

    def start():
        pass
    def quit():
        root.destroy()

root = Tk()
root.geometry("1250x750")
root.configure(background = "#ffffff")
root.title("Survive the Zombie Apocalypse")
app = EventRaid(root)
root.mainloop()