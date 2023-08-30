import tkinter as tk  # importing required libraries

root = tk.Tk() # creating object of the tk class

# setting geometry(width and height) of GUI Window.
root.geometry("733x434") # set width = 800, height = 400
root.minsize(733,434) # setting minsize to not make it smaller than this
root.maxsize(800, 600) # defining maximum size.

# Chaning title of Window
root.title("Pycharm")

# adding label
mylabel = tk.Label(text = "Welcome to Pycharm.", font=("Adobe Hebrew", 20, "bold"), fg="#FCF849", bg="#01C5ED", width=60, pady=25, relief="ridge")
mylabel.pack()

# adding an image
img = tk.PhotoImage(file="pycharm-logo.png")
resized_img = img.subsample(3,3)  # Resize the image by a factor of 2 (halves the size)
label2 = tk.Label(image=resized_img, padx=50, pady=50)
label2.pack()

#adding footer
footer = tk.Label(text="This is official documentation of pycharm IDE.", fg="white", bg="black", padx=5, pady=5, relief="solid", borderwidth=3)
footer.pack(side="bottom", anchor="sw")
# Pack option
# side = top, bottom, left, right
# anchor = se(south-east), nw(north-west), n, ne, e, se, s, sw, w, nw, or center
# Fill = X,Y (when we expand window in x direction it will cover x and same for y as well.)
root.mainloop() # starting mainloop for managing events of user.
