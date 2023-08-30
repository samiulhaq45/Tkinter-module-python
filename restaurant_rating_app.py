from tkinter import *
import tkinter.messagebox as msgb
from tkinter import PhotoImage

window = Tk()
window.geometry("700x600")
window.title("Restaurant Rating App")
icon = PhotoImage(file="food-rating.png")
window.iconphoto(True, icon)

# Define Functions
def getVals():
    with open('customer_feedback.txt', 'r') as f:
        lines = f.readlines()
    
    # Determine the last customer number
    last_customer = 0
    for line in lines:
        if line.startswith('Customer No: '):
            customer_number = int(line.split()[-1])
            last_customer = max(last_customer, customer_number)
    
    n = last_customer + 1
    msgb.showinfo("Message", "Thanks for your feedback, for any queries please contact us.")
    with open('customer_feedback.txt', 'a') as f:
        f.write(f'\nCustomer No: {n}\n')
        f.write(f'Have you enjoy the meal?: {s1.get()}\n')
        f.write(f'How was the Location? : {s2.get()}\n')
        f.write(f'How do you rate our Service? : {s3.get()}\n')
        f.write(f'How about Cleanness? : {s4.get()}\n')
        f.write(f'How was the Waiters behaviour? : {s5.get()}\n')
        f.write(f'Do you Recommend Us? : {s6.get()}\n')


color = '#db860f'
Label(window, text="Welcome to Our Hotel Rating System!", fg=color, font=('Helvetica', 20, 'bold')).pack(pady=10)
Label(window, text="How much do you Satisfied with Our Service!", font=('Helvetica', 12, 'bold')).pack()

frame = Frame(window)
frame.pack()

Label(frame, text='Thanks for your time, please rate between 0 and 10(0=Bad, 10=Perfect)').grid(row=0, column=0, columnspan=2, pady=10)

Label(frame, text='Have you enjoy the meal?', font=('Helvetica', 10, 'bold')).grid(row=1, column=0)
s1 = Scale(frame, from_=0, to=10, tickinterval=1, orient=HORIZONTAL, length=200)
s1.grid(row=1, column=1)

Label(frame, text='How was the Location?', font=('Helvetica', 10, 'bold')).grid(row=2, column=0)
s2 = Scale(frame, from_=0, to=10, tickinterval=1, orient=HORIZONTAL, length=200)
s2.grid(row=2, column=1)

Label(frame, text='How do you rate our Service?', font=('Helvetica', 10, 'bold')).grid(row=3, column=0)
s3 = Scale(frame, from_=0, to=10, tickinterval=1, orient=HORIZONTAL, length=200)
s3.grid(row=3, column=1)

Label(frame, text='How about Cleanness?', font=('Helvetica', 10, 'bold')).grid(row=4, column=0)
s4 = Scale(frame, from_=0, to=10, tickinterval=1, orient=HORIZONTAL, length=200)
s4.grid(row=4, column=1)

Label(frame, text='How was the Waiters behaviour?', font=('Helvetica', 10, 'bold')).grid(row=5, column=0)
s5 = Scale(frame, from_=0, to=10, tickinterval=1, orient=HORIZONTAL, length=200)
s5.grid(row=5, column=1)

Label(frame, text='Do you Recommend Us?', font=('Helvetica', 10, 'bold')).grid(row=6, column=0)
s6 = Scale(frame, from_=0, to=10, tickinterval=1, orient=HORIZONTAL, length=200)
s6.grid(row=6, column=1)

Button(frame, text='Submit Response', bg=color, fg='#fff', relief='groove', font=('Helvetica', 13, 'bold'), command=getVals).grid(row=7, column=0, columnspan=2, pady=10)

window.mainloop()
