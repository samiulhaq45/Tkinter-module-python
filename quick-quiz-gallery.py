from tkinter import *
from PIL import Image, ImageTk
import os

root = Tk()
root.geometry('800x500')

file_path = "C:/Users/SAMI UL HAQ/Desktop/Desktop Application/images/"
files = os.listdir(file_path)

# For all types of images
x_cord = 0
y_cord = 0

for file in files:
    if file.lower().endswith((".jpeg", ".png", ".jpg")):
        # Create the complete file path for the image
        image_path = os.path.join(file_path, file)

        # Open the image using the complete file path
        image = Image.open(image_path)

        # Resize the image and create a PhotoImage
        resize = image.resize((100, 100))
        photo = ImageTk.PhotoImage(resize)

        # Create a label with the image and place it on the window
        lab = Label(image=photo)
        lab.place(x=x_cord, y=y_cord)

        # Keep a reference to the PhotoImage to prevent garbage collection
        lab.image = photo

        x_cord += 100  # Increment x-coordinate

root.mainloop()
