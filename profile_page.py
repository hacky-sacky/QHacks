import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title('Profile Page')
root.resizable(False, False)
root.geometry("500x500")

bg = PhotoImage(file = "pictures/signupbg.png")
bglabel = Label(root, image = bg)
bglabel.place(x=0, y=0)

pfp = PhotoImage(file = "pictures/NEWAMONGUS.png")
pfplabel = Label(root, image = pfp)
pfplabel.place(x=100, y=100)

root.mainloop()