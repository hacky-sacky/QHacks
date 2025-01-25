import tkinter as tk
from tkinter import *
import account

def login_or_signup():
    root = tk.Tk()
    root.title('Login or Signup Page')
    root.resizable(False, False)
    root.geometry("500x500")

    bg = PhotoImage(file = "pictures/signupbg.png")
    bglabel = Label(root, image = bg)
    bglabel.place(x=0, y=0)

    signup_button = tk.Button(root,
                            text='Sign Up',
                            bg='#52bfdc',
                            font= ('Modern', 100))
    signup_button.place(x=60, y=70)
    signup_button.config(command=account.signup_page)

    login_button = tk.Button(root,
                            text='Log In',
                            bg='#52bfdc',
                            font= ('Modern', 100))
    login_button.place(x=93, y=270)

    root.mainloop()

#REAL CODE
login_or_signup()