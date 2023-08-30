from tkinter import *
import tkinter.messagebox as msgb


def add():
    item = entry.get()

    if lbx.curselection():
        selected_index = lbx.curselection()[0]
        lbx.insert(selected_index + 1, item)
    else:
        lbx.insert(END, item)
    msgb.showinfo("Item Added", f"\"{item}\" has been added to the Box.")
    entry.delete(0, END)  # Clear the entry widget after adding

def remove():
    
    if lbx.get(ACTIVE) != "":
        value = msgb.askquestion("Warning!", f"Do you want to remove \"{lbx.get(ACTIVE)}\" from the list.")

        if value == 'yes':
            lbx.delete(ACTIVE)
    else:
        msgb.showinfo("Empty List", "Sorry! list is Empty")


window = Tk()
window.geometry('420x400')
window.title("List Box Button in Tkinter")
window.configure(bg='#4285F4')

# Frame-0 for top Heading
frame0 = Frame(window)
frame0.pack()
frame0.config(bg='#4285F4')

Label(frame0, text="ToDo List", font=("Helvetica", 25, 'bold'), bg='#4285F4', fg='#fff').grid(row=0, column=0,columnspan=2, pady=15)

# Creating Frame for listbox
frame1 = Frame(window)
frame1.pack()
frame1.config(bg='#4285F4')

# Creating List Box
lbx = Listbox(frame1, width=60)
lbx.grid(row=0, column=0, pady=12)

#Creating Scroll bar
scrollbar = Scrollbar(frame1, command=lbx.yview, troughcolor='#000')
scrollbar.grid(row=0, column=1, sticky='ns')

# Attaching scroll to ListBox
lbx.config(yscrollcommand=scrollbar.set)

# frame 2 for entry widget
frame2 = Frame(window)
frame2.pack()
frame2.config(bg='#4285F4')

entry = Entry(frame2, width=60)
entry.grid(row=0, column=0, pady=15, padx=12, ipady=5)

# Frame 3 for Buttons
frame3 = Frame(window)
frame3.pack()
frame3.config(bg='#4285F4')

Button(frame3, text='Add item', command=add, bg='#e65c07', fg='#fff', font=('Helvetica', 12, 'bold'), relief='sunken').grid(row=3, column=0, padx=5)

Button(frame3, text='Remove item', command=remove, bg='#e65c07', fg='#fff', font=('Helvetica', 12, 'bold'), relief='sunken').grid(row=3, column=1, padx=5)

window.mainloop()
