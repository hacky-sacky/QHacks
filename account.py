import tkinter as tk
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
    with open("user_pass.csv", mode="r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            user_pass.append(row)
        print(user_pass)

def sign_up():
    global new_user
    read_csv()
    new_username = input("enter new user: ")
    if any (user["username"].lower() == new_username.lower() for user in user_pass):
        print("username taken")
    else:
        new_password = input("enter new pass: ")
        new_user = {"username": new_username, "password": new_password}
        write_csv()
        print("success")



#input_username = input("enter user: ")
#input_password = input("enter pass: ")

def login():
    global login_status
    for user in user_pass:
        if user["username"] == input_username and user["password"] == input_password:
            login_status = True
            break

def verify_login():
    return login_status



#ACTUAL CODE
sign_up()
