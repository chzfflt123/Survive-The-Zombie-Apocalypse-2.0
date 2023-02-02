from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init(master)
        self.grid()
        self.create_widgets()