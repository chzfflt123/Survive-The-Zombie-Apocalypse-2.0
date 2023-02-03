from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        heading = Label(root, text = "How to play", font=("Ariel",72))
        heading.place(x=625, y=100, anchor = CENTER)

        Label(root,text="press the buttons corresponding to whichever location you want to go\nyou could either go explore or stay at home\nif you explore there are many things that will happen and if you survive you will go \nback home and be able to choose again whether to explore or stay home\nyou also have to manage your health and your food throughout the game to avoid \ndeath\nif you survive long enough you live!", font=("Ariel",32)).place(x=625,y=300, anchor=CENTER)

root = Tk()
root.title("How To Play")
root.geometry("1250x750")
app = Application(root)
root.mainloop()