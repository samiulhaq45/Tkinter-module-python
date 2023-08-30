from tkinter import *
from tkinter import PhotoImage

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x350')
        self.title("OOPS Concept in Tkinter")
        icon = PhotoImage(file='1.png')
        self.iconphoto(True, icon)

    def status(self):
        self.var = StringVar()
        self.var.set('Ready...')
        self.statusbar = Label(self, textvariable=self.var, relief=SUNKEN, anchor='w')
        self.statusbar.pack(side=BOTTOM, fill=X)

    def heading(self, txt):
        self.label = Label(self, text=txt, font=('Helvetica', 20, 'bold'))
        self.label.pack()

if __name__ == '__main__':
    window = GUI()
    window.status()
    window.heading("Oops Concept in Tkinter")
    window.mainloop()