from tkinter import *
import tkinter.messagebox as msgb

window = Tk()
window.geometry("800x400")
window.title('Menus and SubMenus in tkinter')

def myFunc():
    print("Hello World!")

def help():
    print("I will help you.")
    msgb.showinfo("Help", "Our Customer support team will contact you shortly. Thanks for your patience")

def rate():
    val = msgb.askquestion("Rate Us", "Do you like our app.")
    if val == 'yes':
        msgb.showinfo("Rate Us", "Thanks! Please rate us on app store.")
    else:
        msgb.showinfo("Rate Us", "Sad to hear! Contact our customer care for your complaint.")
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
myMenu.add_cascade(label="Edit", menu=d2)

# Menu item - 3
d3 = Menu(myMenu, tearoff=0)
d3.add_command(label="Help", command=help)
d3.add_command(label="Rate Us", command=rate)
myMenu.add_cascade(label="Help", menu=d3)


window.config(menu=myMenu)

window.mainloop()