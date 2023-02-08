from tkinter import * 
from tkinter import ttk
from tkinter.ttk import Progressbar
  
class BaseScreen(Frame):
    def __init__(self, master, callback_on_base):
        super(BaseScreen, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.callback_on_base = callback_on_base

    def create_widgets(self):
        style = ttk.Style()
        style.theme_use('default')
        style.configure("grey.Horizontal.TProgressbar", background='green')
        bar = Progressbar(self, length=180, style='grey.Horizontal.TProgressbar')
        bar['value'] = 50
        Label(self, text="HEALTH", font="Ariel 22").grid(row=0, column=0, padx = 10)
        bar.grid(column=1, row=0, padx = 10)

        bar2 = Progressbar(self, length=180, style='grey.Horizontal.TProgressbar')
        bar2['value'] = 50
        Label(self, text="Supplies", font="Ariel 22").grid(row=1, column=0, padx = 10)
        bar2.grid(column=1, row=1, padx = 10)

        tempnext_button = Button(self, text="temporary Next", font = "Ariel 20", width=12, height=2, bg="#A0A0A0", command=self.next)
        tempnext_button.grid(row=2, column=0)

    def next(self):
        self.callback_on_base()
    
    def quit_game(self):
        self.destroy()

# root = Tk()
# root.title("Base")
# app = BaseScreen(root)
# root.mainloop()