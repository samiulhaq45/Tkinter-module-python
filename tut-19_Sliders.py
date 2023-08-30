from tkinter import *
import tkinter.messagebox as msgb
window = Tk()
window.geometry("500x350")
window.title("Slider in tkinter.")

def Age():
    age = myslider.get()
    if age <=15:
        msgb.showinfo("Age Detector", f"Your age: {age}. You are kid.")
    elif age >15 and age <= 25:
        msgb.showinfo("Age Detector", f"Your age: {age}. You are Young.")
    elif age >25 and age <=40:
        msgb.showinfo("Age Detector", f"Your age: {age}. You are Man.")
    else:
        msgb.showinfo("Age Detector", f'Your age: {age}. You are old.')
Label(window, text="How old are you?").pack()
myslider = Scale(window, from_=0, to=10, orient=HORIZONTAL)
myslider.set(23)
myslider.pack()

Button(window, text="Submit", command=Age).pack()

window.mainloop()