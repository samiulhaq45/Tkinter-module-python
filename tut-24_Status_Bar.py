from tkinter import *

def upload():
    statusVar.set("Busy...")
    sbar.update()
    import time
    time.sleep(2)
    statusVar.set("Ready...")

window = Tk()
window.geometry('500x400')
window.title('Status Bar in tkinter')

statusVar = StringVar()
statusVar.set('Ready')

sbar = Label(window, textvariable=statusVar, relief=SUNKEN, anchor='w')
sbar.pack(side=BOTTOM, fill=X)

Button(window, text="Upload", command=upload).pack()

window.mainloop()