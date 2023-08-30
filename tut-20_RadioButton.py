from tkinter import *
import tkinter.messagebox as msgb

window = Tk()
window.geometry('250x250')
window.title("Radio Button in Tkinter")

def order():
    msgb.showinfo("Order", f"Thanks for ordering {var.get()}, Your order will be served in 20 minutes.")

var = StringVar()
var.set(None)

Label(window, text="What would you like to eat!", justify=LEFT, padx=14, font=("Helvetica", 12, 'bold')).pack(pady=20)

radio = Radiobutton(window, text="Pizza", value=
'Pizza', variable=var).pack(anchor='w', padx=20)
radio = Radiobutton(window, text="Burger", value='Burger', variable=var).pack(anchor='w', padx=20)
radio = Radiobutton(window, text="Shwarma", value='Shwarma', variable=var).pack(anchor='w', padx=20)
radio = Radiobutton(window, text="Paratha Roll", value='Paratha Roll', variable=var).pack(anchor='w', padx=20)

Button(window, text='Order Now', bg="#000", fg='#fff', font=("Helvetica", 10, 'bold'), command=order).pack(pady=15)

window.mainloop()