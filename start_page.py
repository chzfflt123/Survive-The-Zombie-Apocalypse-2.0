from tkinter import *

class Application(Frame):
    
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        Label(self, text = "Survive the Zombie Apocalypse").grid(row = 0, column = 0, columnspan = 5, sticky = N)

        Button(self, text = "Start", command = self.start).grid(row = 3, column = 3)
        Button(self, text = "Quit", command = self.quit).grid(row = 3, column = 7)
    
    def start():
        pass
    def quit():
        pass

root = Tk()
root.geometry("1250x750")
root.title("Survive the Zombie Apocalypse")
app = Application(root)
root.mainloop()