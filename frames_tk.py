import tkinter as tk

root = tk.Tk()
root.title("FRAME TUTORIALS")
root.geometry("655x333")
root.minsize(500, 150)

f1 = tk.Frame(root, bg="black", borderwidth=6, relief="sunken")
f1.pack(side="left", fill="y")

f2 = tk.Frame(root, bg="black", borderwidth=4, relief="sunken")
f2.pack(side="top", fill="x")


l = tk.Label(f1, text="TKINTER PROJECT", fg="white", bg="black", font=("Adobe Hebrew", 16, "bold"))
l.pack(side="left")

l2 = tk.Label(f2, text="TKINTER PROJECT", fg="white", bg="black", font=("Adobe Hebrew", 16, "bold"))
l2.pack()

root.mainloop()