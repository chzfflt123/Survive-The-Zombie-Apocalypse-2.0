from tkinter import *

class Application(Frame):
    
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        title1 = Label(root, text = "Survive the Zombie Apocalypse", font = "Times 40")
        title1.place(x= 312.5, y=200, anchor=W)

        mybutton1 = Button(root, text = "Start", font = "Times 30", width = 15, command = self.start)
        mybutton1.place(x = 312.5, y = 300, anchor=W)

        mybutton2 = Button(root, text = "Quit", font = "Times 30", width = 15, command = self.quit)
        mybutton2.place(x = 660, y = 300, anchor=W)

    def start():
        pass
    def quit():
        pass

root = Tk()
root.geometry("1250x750")
root.title("Survive the Zombie Apocalypse")
app = Application(root)
root.mainloop()