import tkinter as tk

def btn1():
    print("Button 1 has been clicked.")

def btn2():
    print("Button 2 has been clicked.")

def btn3():
    print("Button 3 has been clicked.")

def btn4():
    print("Button 4 has been clicked.")\
    
root = tk.Tk()
root.title("BUTTONS TUTORIALS")
root.geometry("655x333")
root.minsize(500, 150)

f1 = tk.Frame(root, borderwidth=3, bg="gray", relief="sunken")
f1.pack(side="left", anchor="nw")

b1 = tk.Button(f1, bg="black",fg="white", text="1:Click Here", command= btn1)
b1.pack(side="left", padx=15, pady=15)

b2 = tk.Button(f1, bg="black",fg="white", text="2:Click Here", command=btn2)
b2.pack(side="left", padx=15, pady=15)

b3 = tk.Button(f1, bg="black",fg="white", text="3:Click Here", command=btn3)
b3.pack(side="left", padx=15, pady=15)

b4 = tk.Button(f1, bg="black",fg="white", text="4:Click Here", command=btn4)
b4.pack(side="left", padx=15, pady=15)

root.mainloop()