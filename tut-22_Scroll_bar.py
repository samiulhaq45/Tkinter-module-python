from tkinter import *

window = Tk()
window.geometry("500x350")
window.title('Scroll Bar in tkinter')

# For Connecting ScrollBar to a widget
# 1. Widget (yscrollcommand) = scrollbar.set
# 2. scrollbar.config(command = widget.yview)
frame = Frame(window)
frame.pack()

listbox = Listbox(frame)
listbox.grid(row=0, column=0)

scrollbar = Scrollbar(frame, command=listbox.yview)
scrollbar.grid(row=0, column=1, sticky='ns')

listbox.config(yscrollcommand=scrollbar.set)

for i in range(350):
    listbox.insert(END, f'Item No: {i}')

window.mainloop()