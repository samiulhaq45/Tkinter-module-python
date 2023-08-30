from tkinter import *

def getvals():
    print(username.get())
    print(password.get())

root = Tk()
root.geometry("650x344")
root.title("Entry Widget")

Label(root, text="Username", pady=15).grid()
Label(root, text="Password", pady=15).grid()


# Variable Classes in tkinter:
# BooleanVar, DoubleVar, IntVar, StringVar

username = StringVar()
password = StringVar()

Entry(root, textvariable=username).grid(row=0, column=1)

Entry(root, textvariable=password, show="*").grid(row=1, column=1)


#creating button
clickbtn = Button(root, text="Login", bg="black", fg="white", font=("Helvatica", 12, "bold"), command=getvals)
clickbtn.grid(row=2, column=1)


root.mainloop()