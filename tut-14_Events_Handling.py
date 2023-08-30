from tkinter import *

def sami(event):
    print("button has been clicked.")

window = Tk()
window.title('Events Handling in tkinter')
window.geometry("500x300")

widget = Button(window, text="Click here!")
widget.pack()

widget.bind('<Button-1>', sami)
widget.bind('<Double-1>', quit)

window.mainloop()