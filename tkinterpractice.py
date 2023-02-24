from tkinter import *
class StartPage(Frame):
    
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        image_char = PhotoImage(file = "images/girl.png")
        char_lbl=Label(self, image = image_char)
        char_lbl.x = image_char
        char_lbl.grid(row = 0, column =0, sticky = W)

def main():
    root = Tk()
    root.title("Pizza Mad Libs")
    app = StartPage(root)
    root.geometry("200x500")
    root.mainloop()

main()
