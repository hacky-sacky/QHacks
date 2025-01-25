import tkinter as tk
from tkinter import *
import csv

login_status = False
user_pass = []

def write_csv():
    with open("user_pass.csv", mode="a", newline="") as csvfile:
        fieldnames = ["username", "password"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if csvfile.tell() == 0:
            writer.writeheader()
        writer.writerows([new_user])

def read_csv():
    global user_pass
    user_pass.clear()
    with open("user_pass.csv", mode="r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            user_pass.append(row)
        print(user_pass)

def sign_up():
    global new_user
    read_csv()
    if not new_username or not new_password:
        print("enter stuff")
        return 0
    elif any (user["username"].lower() == new_username.lower() for user in user_pass):
        print("username taken")
        return 1
    else:
        new_user = {"username": new_username, "password": new_password}
        write_csv()
        print("success")
        return 2

def signup_page():
    root = tk.Tk()
    root.title('Signup Page')
    root.resizable(False, False)
    root.geometry("500x500")

    bg = PhotoImage(file = "pictures/signupbg.png")
    bglabel = Label(root, image = bg)
    bglabel.place(x=0, y=0)

    def when_signup_clicked():
        global new_username
        global new_password
        new_username = username.get()
        new_password = password.get()

        result = sign_up()

        if result == 0:
            error = tk.Label(root, text="please fill all fields", fg='red')
            error.place(x=200, y=280)
        elif result == 1:
            error = tk.Label(root, text="username taken nt bro", fg='red')
            error.place(x=200, y=280)
        else:
            print("hello")

    signup_button = tk.Button(root,
                            text='Sign Up',
                            bg='#52bfdc',
                            font= ('Modern', 30),
                            command=when_signup_clicked)
    signup_button.place(x=176, y=335)

    username = tk.Entry(root, bg='white', fg='black')
    username.place(x=150, y=120)

    password = tk.Entry(root, bg='white', fg='black')
    password.place(x=150, y=200)
    
    user = tk.Label(root, text="user:")
    user.place(x=100, y=120)

    passy = tk.Label(root, text="pass:")
    passy.place(x=100, y=200)

    root.mainloop()


def login_page():
    root = tk.Tk()
    root.title('Login Page')
    root.resizable(False, False)
    root.geometry("500x500")

    bg = PhotoImage(file = "pictures/signupbg.png")
    bglabel = Label(root, image = bg)
    bglabel.place(x=0, y=0)

    def when_signup_clicked():
        global input_username
        global input_password
        input_username = username.get()
        input_password = password.get()

        result = login()

        if result == 0:
            error = tk.Label(root, text="wrong password bro", fg='red')
            error.place(x=200, y=280)
        elif result == 1:
            print("hello")

    login_button = tk.Button(root,
                            text='Log in',
                            bg='#52bfdc',
                            font= ('Modern', 30),
                            command=when_signup_clicked)
    login_button.place(x=176, y=335)

    username = tk.Entry(root, bg='white', fg='black')
    username.place(x=150, y=120)

    password = tk.Entry(root, bg='white', fg='black')
    password.place(x=150, y=200)

    user = tk.Label(root, text="user:")
    user.place(x=100, y=120)

    passy = tk.Label(root, text="pass:")
    passy.place(x=100, y=200)
    
    root.mainloop()

def login():
    global login_status
    read_csv()
    for user in user_pass:
        if user["username"] == input_username and user["password"] == input_password:
            login_status = True
            break

def verify_login():
    return login_status


signup_page()
