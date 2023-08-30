from tkinter import *


window = Tk()
window.geometry("800x400")
window.title('Menus and SubMenus in tkinter')

def myFunc():
    print("Hello World!")

# # for single line Menu not drop-drown menu
# mymenu = Menu(window)
# mymenu.add_command(label="File", command=myFunc)
# mymenu.add_command(label="Quit", command=quit)

# window.config(menu=mymenu)

# Menu item - 1
myMenu = Menu(window)
d1 = Menu(myMenu, tearoff=0)
d1.add_command(label="Open File", command=myFunc)
d1.add_command(label="New File", command=myFunc)
d1.add_separator()
d1.add_command(label="Save", command=myFunc)
d1.add_command(label="Save As", command=myFunc)
d1.add_separator()
d1.add_command(label="Quit", command=quit)

myMenu.add_cascade(label="File", menu=d1)

# Menu item - 2
d2 = Menu(myMenu, tearoff=0)
d2.add_command(label="Undo", command=myFunc)
d2.add_command(label="Redo", command=myFunc)
d2.add_separator()
d2.add_command(label="Cut", command=myFunc)
d2.add_command(label="Copy", command=myFunc)
d2.add_command(label="Paste", command=myFunc)
d2.add_separator()
d2.add_command(label="Find", command=quit)
d2.add_command(label="Replace", command=quit)

window.config(menu=myMenu)

myMenu.add_cascade(label="Edit", menu=d2)
window.mainloop()