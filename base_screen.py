from tkinter import * 
from tkinter import ttk
from tkinter.ttk import Progressbar
  
class BaseScreen(Frame):
    def __init__(self, master):
        super(BaseScreen, self).__init__(master)
        self.grid()
        self.create_widgets()

    
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


    
    def quit_game(self):
        self.destroy()

root = Tk()
root.title("Base")
app = BaseScreen(root)
root.mainloop()