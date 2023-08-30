from tkinter import *

window = Tk()
window.title("Canvas Widget in Python.")

window.geometry("800x400")

canvas_widget = Canvas(window, width=800, height=400)
canvas_widget.pack()

# creating line in canvas it takes two arg (x1,y1) and (x2, y2)
canvas_widget.create_line(0, 0, 800, 400, fill="red")
canvas_widget.create_line(0, 400, 800, 0, fill="red")

# creating rectangle in canvas, it takes top-left and bottom-right coordinates
canvas_widget.create_rectangle(0, 0, 150, 150, fill="green")

canvas_widget.create_line(0, 75, 150, 75, fill="blue")
canvas_widget.create_line(75, 0, 75, 150, fill="blue")
canvas_widget.create_text(37, 37, text="C-1")
canvas_widget.create_text(110, 37, text="C-2")
canvas_widget.create_text(37, 110, text="C-3")
canvas_widget.create_text(110, 110, text="C-4")

canvas_widget.create_oval(200, 50, 300, 150, fill="red")
canvas_widget.create_text(250, 100, text="OVAL")

canvas_widget.create_arc(10, 50, 240, 210, start=0, extent=180, fill='green')
window.mainloop()