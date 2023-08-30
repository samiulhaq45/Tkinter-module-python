# importing required Libraries
from tkinter import *

# Creating function for command
def getvals():
    print("Form Submitted Sucessfully.")
    print("Name: ", nameValue.get())
    print("Phone Number: ", phoneValue.get())
    print("Gender: ", genderValue.get())
    print("Emergency Number: ", emergencyValue.get())
    print("Payment Mode: ", paymentmodeValue.get())

# setting basics layout
root = Tk()
root.geometry("550x450")
root.minsize(500, 350)
root.title("Checkbox and Entry Widgets - tkinter")

# Heading of the window
Label(root, text="Welcome to Travel Agency", font="comicsansms 15 bold").grid(row=0, column=1, pady=15)

#Labels for input boxes
name = Label(root, text="Name", font="comicsansms 12 bold", pady=5)
phone = Label(root, text="Phone", font="comicsansms 12 bold", pady=5)
gender = Label(root, text="Gender", font="comicsansms 12 bold", pady=5)
emergency = Label(root, text="Emergency Contact", font="comicsansms 12 bold", pady=5)
paymentMode = Label(root, text="Payment Mode", font="comicsansms 12 bold", pady=5)

# Displaying Label on the window 
name.grid(row=1, column=0)
phone.grid(row=2, column=0)
gender.grid(row=3, column=0)
emergency.grid(row=4, column=0)
paymentMode.grid(row=5, column=0)

# creating variable for storing values of input boxes
nameValue = StringVar()
phoneValue = IntVar()
genderValue = StringVar()
emergencyValue = StringVar()
paymentmodeValue = StringVar()
foodServiceValue = IntVar()

# Creating boxes for input
Name = Entry(root, textvariable=nameValue).grid(row=1, column=1)
Entry(root, textvariable=phoneValue).grid(row=2, column=1)
Entry(root, textvariable=genderValue).grid(row=3, column=1)
Entry(root, textvariable=emergencyValue).grid(row=4, column=1)
Entry(root, textvariable=paymentmodeValue).grid(row=5, column=1)

# Check Button
foodservice = Checkbutton(text="Want to pre-book your meal.", variable=foodServiceValue, pady=15)
foodservice.grid(row=6, column=1)

# Submit button
Button(text="Submit Now", command=getvals).grid(row=7, column=1)

root.mainloop()