import tkinter as tk
from tkinter import ttk
from tkinter import *
import socket

import csv
import os
from tkinter import font

#global variables

#T/F for if login or not
i = 0


LARGEFONT = ("Verdana", 35)


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp

    #self it like self  (self = tk.Tk())

    def __init__(self, *args, **kwargs):

        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)


        self.geometry("500x500")
        self.resizable(False, False)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        # idk what tf this does
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (FirstPage, AddEventPage, AccountPages, SignUpPage, LoginPage, ProfilePage, EventsPage):
            print(self.frames)

            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(FirstPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()



def test(num):
    if num == 1:
       return ProfilePage
    else:
       return AccountPages

def send_info(information):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("10.216.133.33", 5050))

    print(client.recv(1024).decode())
    client.send(information.encode())


# first window frame startpage
class FirstPage(tk.Frame):


    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        bg = PhotoImage(file="pictures/signupbg.png")
        bglabel = Label(self, image=bg)
        bglabel.image = bg
        bglabel.place(x=0, y=0)



        thing_to_do_btn = tk.Button(self, text='Things To Do', bg='light grey', font=('Arial 12 bold'), command= lambda: controller.show_frame(EventsPage))
        thing_to_do_btn.place(x=30, y=10, height=30, width=125)

        chat_wt_ppl_btn = tk.Button(self, text='Chat With People', bg='light grey', font=('Arial 10 bold'))
        chat_wt_ppl_btn.place(x=187.5, y=10, height=30, width=125)


        global i


        account_btn = tk.Button(self, text='Account', bg='light grey', font='Arial 12 bold', command= lambda: controller.show_frame(test(i)))
        account_btn.place(x=337.5, y=10, height=30, width=125)
        print(f'also {i}')


        underlined_font = font.Font(family="Arial", size=12, underline=True)
        # height = 15 pixels

        search_bar = tk.Entry(self, font=('Arial 15 bold'))
        search_bar.place(x=50, y=100, height=50, width=400)
        search_bar.bind("<Return>", lambda event: show_details_of_event(search_bar.get()))
        search_bar.delete(0, tk.END)

        def show_details_of_event(event_title):
            events_file = "events.txt"

            """
            Displays the details of a specific event when the user clicks the corresponding button.
            """
            events_window = tk.Toplevel()
            events_window.title("Events")
            events_window.geometry("600x600")

            header_label = tk.Label(events_window, text="Events", font=("Montserrat", 18, "bold"))
            header_label.pack(pady=20)

            events_frame = tk.Frame(events_window)
            events_frame.pack(pady=10, padx=20, fill="both", expand=True)

            close_button = tk.Button(events_window, text="Close", command=events_window.destroy)
            close_button.pack(pady=10)

            for widget in events_frame.winfo_children():
                widget.destroy()  # Clear existing content

            if os.path.exists(events_file):
                with open(events_file, "r") as file:
                    for line in file:
                        title, date, time, description, location, event_type = line.strip().split("|")
                        if title == event_title:
                            # Create a frame for event details
                            event_box = tk.Frame(events_frame, borderwidth=1, relief="solid", padx=10, pady=10)
                            event_box.pack(fill="x", pady=5)

                            event_title_label = tk.Label(event_box, text=title, font=("Montserrat", 14, "bold"))
                            event_title_label.pack(anchor="w")

                            event_details = tk.Label(event_box,
                                                     text=f"Type: {event_type} | Time: {time} | Location: {location}",
                                                     font=("Montserrat", 12))
                            event_details.pack(anchor="w")

                            event_description = tk.Label(event_box, text=description, font=("Montserrat", 10),
                                                         fg="gray")
                            event_description.pack(anchor="w")
                            search_bar.delete(0, tk.END)
                            return

        try_smth_new_txt = tk.Label(self, text='try something new ...', bg='grey', fg='blue', font=underlined_font)
        try_smth_new_txt.place(x=150, y=200, height=25, width=150)

        add_button = tk.Button(self, text= '+', font=('Arial 15 bold'), command= lambda: controller.show_frame(AddEventPage))
        add_button.place(x=430, y= 160, height=20, width=20)




class AddEventPage(tk.Frame):
    def __init__(self, parent, controller):


        tk.Frame.__init__(self, parent)

        events_file = "events.txt"

        def submit_event():
            """
            This function gets all the data entries from the 'Add New Event' page
            and checks that if all data entry is 'gotten' (from .get) and appends
            all data to a txt.file. It also displays a text that the event has been
            added or not added in case the user didn't fill all the entry fields.
            """
            title = title_var.get()
            date = date_var.get()
            start_time = start_time_var.get()
            end_time = end_time_var.get()
            description = description_text.get("1.0", tk.END).strip()
            location = location_var.get()
            event_type = type_var.get()

            if all([title, date, start_time, end_time, description, location, event_type]):
                send_info(f"{title}|{date}|{start_time}-{end_time}|{description}|{location}|{event_type}\n")
                with open(events_file, "a") as file:
                    file.write(f"{title}|{date}|{start_time}-{end_time}|{description}|{location}|{event_type}\n")

                result_label.config(text=f"Event '{title}' added successfully!", fg="green")
                clear_form()
                self.after(2000, lambda: controller.show_frame(FirstPage))
                result_label.destroy()
            else:
                result_label.config(text="Please fill out all fields.", fg="red")
                result_label.place(x=170, y=450)


        def clear_form():
            """
            This function clears the form after a user has wrote
            in all fields of entry and has submitted it. This is
            called after the user presses the submit button.
            """
            title_var.set("")
            date_var.set("")
            start_time_var.set("")
            end_time_var.set("")
            description_text.delete("1.0", tk.END)
            location_var.set("")
            type_var.set("")

        def show_event_details(event):
            details_window = tk.Toplevel(self)
            details_window.title("Event Details")
            details_window.geometry("600x600")

            header_label = tk.Label(details_window, text="Event Details", font=("Montserrat", 18, "bold"))
            header_label.pack(pady=20)

            title_label = tk.Label(details_window, text=f"Title: {event['title']}", font=("Montserrat", 14))
            title_label.pack(anchor="w", padx=20, pady=5)

            date_label = tk.Label(details_window, text=f"Date: {event['date']}", font=("Montserrat", 14))
            date_label.pack(anchor="w", padx=20, pady=5)

            time_label = tk.Label(details_window, text=f"Time: {event['time']}", font=("Montserrat", 14))
            time_label.pack(anchor="w", padx=20, pady=5)

            description_label = tk.Label(details_window, text=f"Description: {event['description']}",
                                         font=("Montserrat", 14), wraplength=500, justify="left")
            description_label.pack(anchor="w", padx=20, pady=5)

            location_label = tk.Label(details_window, text=f"Location: {event['location']}", font=("Montserrat", 14))
            location_label.pack(anchor="w", padx=20, pady=5)

            type_label = tk.Label(details_window, text=f"Type: {event['type']}", font=("Montserrat", 14))
            type_label.pack(anchor="w", padx=20, pady=5)



        # Create a header
        header_label = tk.Label(self, text="Add New Event", font=("Montserrat", 18, "bold"))
        header_label.pack(pady=20)

        # Create a frame for the form
        form_frame = tk.Frame(self)
        form_frame.pack(pady=10, padx=20, fill="x")

        # Title
        title_label = tk.Label(form_frame, text="Title:", font=("Montserrat", 12))
        title_label.grid(row=0, column=0, sticky="w", pady=5)
        title_var = tk.StringVar()
        title_entry = ttk.Entry(form_frame, textvariable=title_var, font=("Montserrat", 12), width=40)
        title_entry.grid(row=0, column=1, pady=5)

        # Date
        date_label = tk.Label(form_frame, text="Date (YYYY-MM-DD):", font=("Montserrat", 12))
        date_label.grid(row=1, column=0, sticky="w", pady=5)
        date_var = tk.StringVar()
        date_entry = ttk.Entry(form_frame, textvariable=date_var, font=("Montserrat", 12), width=40)
        date_entry.grid(row=1, column=1, pady=5)

        # Start Time
        start_time_label = tk.Label(form_frame, text="Start Time (HH:MM):", font=("Montserrat", 12))
        start_time_label.grid(row=2, column=0, sticky="w", pady=5)
        start_time_var = tk.StringVar()
        start_time_entry = ttk.Entry(form_frame, textvariable=start_time_var, font=("Montserrat", 12), width=40)
        start_time_entry.grid(row=2, column=1, pady=5)

        # End Time
        end_time_label = tk.Label(form_frame, text="End Time (HH:MM):", font=("Montserrat", 12))
        end_time_label.grid(row=3, column=0, sticky="w", pady=5)
        end_time_var = tk.StringVar()
        end_time_entry = ttk.Entry(form_frame, textvariable=end_time_var, font=("Montserrat", 12), width=40)
        end_time_entry.grid(row=3, column=1, pady=5)

        # Description
        description_label = tk.Label(form_frame, text="Description:", font=("Montserrat", 12))
        description_label.grid(row=4, column=0, sticky="nw", pady=5)
        description_text = tk.Text(form_frame, font=("Montserrat", 12), width=40, height=5)
        description_text.grid(row=4, column=1, pady=5)

        # Location
        location_label = tk.Label(form_frame, text="Location:", font=("Montserrat", 12))
        location_label.grid(row=5, column=0, sticky="w", pady=5)
        location_var = tk.StringVar()
        location_entry = ttk.Entry(form_frame, textvariable=location_var, font=("Montserrat", 12), width=40)
        location_entry.grid(row=5, column=1, pady=5)

        # Type of Event
        type_label = tk.Label(form_frame, text="Type of Event:", font=("Montserrat", 12))
        type_label.grid(row=6, column=0, sticky="w", pady=5)
        type_var = tk.StringVar()
        type_dropdown = ttk.Combobox(form_frame, textvariable=type_var, font=("Montserrat", 12), width=38,
                                     state="readonly")
        type_dropdown['values'] = ["Sports", "Food", "Entertainment", "Shopping", "Study"]
        type_dropdown.grid(row=6, column=1, pady=5)

        submit_button = ttk.Button(self, text="Submit", command=submit_event)
        submit_button.place(x=170, y=400)

        cancel_button = ttk.Button(self, text="Cancel", command=lambda: controller.show_frame(FirstPage))
        cancel_button.place(x=270, y=400)


        result_label = tk.Label(self, text="", font=("Montserrat", 12))
        result_label.pack(pady=10)


class AccountPages(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        bg = PhotoImage(file="pictures/signupbg.png")
        bglabel = Label(self, image=bg)
        bglabel.image = bg
        bglabel.place(x=0, y=0)

        signup_button = tk.Button(self, command= lambda: controller.show_frame(SignUpPage),
                                  text='Sign Up',
                                  bg='light blue',
                                  font=('Arial 30 bold'))
        signup_button.place(x=160, y=70, height= 100, width= 200)

        login_button = tk.Button(self,
                                 text='Log In',
                                 bg='light blue',
                                 font=('Arial 30 bold'),
                                 command= lambda: controller.show_frame(LoginPage))
        login_button.place(x=160, y=270, height= 100, width = 200)

        back_button = tk.Button(self, text="Back", font=("Montserrat 7 bold"), command=lambda: controller.show_frame(FirstPage))
        back_button.place(x=20, y=20, height=20, width = 34)


class SignUpPage(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)


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
            elif any(user["username"].lower() == new_username.lower() for user in user_pass):
                print("username taken")
                return 1
            else:
                new_user = {"username": new_username, "password": new_password}
                write_csv()
                print("success")
                return 2


        bg = PhotoImage(file="pictures/signupbg.png")

        bglabel = Label(self, image=bg)
        bglabel.image = bg
        bglabel.place(x=0, y=0)

        def when_signup_clicked():
            global new_username
            global new_password
            new_username = username.get()
            new_password = password.get()

            result = sign_up()

            if result == 0:
                error = tk.Label(self, text="please fill all fields", fg='red')
                error.place(x=200, y=280)
            elif result == 1:
                error = tk.Label(self, text="username taken nt bro", fg='red')
                error.place(x=200, y=280)
            else:
                global i
                i = 1
                self.after(1, lambda: controller.show_frame(FirstPage))

        signup_button = tk.Button(self,
                                  text='Sign Up',
                                  bg='#52bfdc',
                                  font=('Modern', 30),
                                  command=when_signup_clicked)
        signup_button.place(x=176, y=335)
        username = tk.Entry(self, bg='white', fg='black')
        username.place(x=150, y=120)

        password = tk.Entry(self, bg='white', fg='black')
        password.place(x=150, y=200)

        back_button = tk.Button(self, text="Back", font=("Montserrat 7 bold"), command=lambda: controller.show_frame(FirstPage))
        back_button.place(x=20, y=20, height=20, width = 34)

        user = tk.Label(self, text="user:")
        user.place(x=100, y=120)

        passy = tk.Label(self, text="pass:")
        passy.place(x=100, y=200)


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        login_status = False
        user_pass = []

        def read_csv():
            user_pass.clear()
            with open("user_pass.csv", mode="r") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    user_pass.append(row)
                print(user_pass)

        bg = PhotoImage(file="pictures/signupbg.png")
        bglabel = Label(self, image=bg)
        bglabel.image = bg
        bglabel.place(x=0, y=0)

        def login():
            global login_status
            read_csv()
            for user in user_pass:
                if user["username"] == input_username and user["password"] == input_password:
                    login_status = True
                    return 1
            return 0
        
        def when_signup_clicked():
            global input_username
            global input_password
            input_username = username.get()
            input_password = password.get()

            result = login()

            if result == 0:
                error = tk.Label(self, text="wrong password bro", fg='red')
                error.place(x=200, y=280)
            else:
                global i

                i = 1
                self.after(1, lambda: controller.show_frame(FirstPage))




        def verify_login():
            return login_status

        login_button = tk.Button(self,
                                 text='Log in',
                                 bg='#52bfdc',
                                 font=('Modern', 30),
                                 command=when_signup_clicked)
        login_button.place(x=176, y=335)

        username = tk.Entry(self, bg='white', fg='black')
        username.place(x=150, y=120)

        password = tk.Entry(self, bg='white', fg='black')
        password.place(x=150, y=200)

        user = tk.Label(self, text="user:")
        user.place(x=100, y=120)

        passy = tk.Label(self, text="pass:")
        passy.place(x=100, y=200)

        back_button = tk.Button(self, text="Back", font=("Montserrat 7 bold"), command=lambda: controller.show_frame(FirstPage))
        back_button.place(x=20, y=20, height=20, width = 34)


class ProfilePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)



        bg = PhotoImage(file="pictures/signupbg.png")
        bglabel = Label(self, image=bg)
        bglabel.image = bg
        bglabel.place(x=0, y=0)

        pfp = PhotoImage(file="pictures/NEWAMONGUS.png")
        pfplabel = Label(self, image=pfp)
        pfplabel.image = pfp
        pfplabel.place(x=100, y=100)

        back_button = tk.Button(self, text="Back", font=("Montserrat 7 bold"), command=lambda: controller.show_frame(FirstPage))
        back_button.place(x=20, y=20, height=20, width = 34)



class EventsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        events_file = "events.txt"

        def show_event_details(event):
            details_window = tk.Toplevel(self)
            details_window.title("Event Details")
            details_window.geometry("600x600")

            header_label = tk.Label(details_window, text="Event Details", font=("Montserrat", 18, "bold"))
            header_label.pack(pady=20)

            title_label = tk.Label(details_window, text=f"Title: {event['title']}", font=("Montserrat", 14))
            title_label.pack(anchor="w", padx=20, pady=5)

            date_label = tk.Label(details_window, text=f"Date: {event['date']}", font=("Montserrat", 14))
            date_label.pack(anchor="w", padx=20, pady=5)

            time_label = tk.Label(details_window, text=f"Time: {event['time']}", font=("Montserrat", 14))
            time_label.pack(anchor="w", padx=20, pady=5)

            description_label = tk.Label(details_window, text=f"Description: {event['description']}",
                                         font=("Montserrat", 14), wraplength=500, justify="left")
            description_label.pack(anchor="w", padx=20, pady=5)

            location_label = tk.Label(details_window, text=f"Location: {event['location']}", font=("Montserrat", 14))
            location_label.pack(anchor="w", padx=20, pady=5)

            type_label = tk.Label(details_window, text=f"Type: {event['type']}", font=("Montserrat", 14))
            type_label.pack(anchor="w", padx=20, pady=5)

        """
        This function displays the 'Events' page with all the events added
        by users.
        This function reads the txt file that was created and creates a list
        of all data entries and puts them in a label which is ultimately
        displayed on the 'Events' page.
        Each event has a view button that takes the user to a separate page
        with all the proper details listed for the public to see.
        If there are no events added and a user goes on this page, it says
        'No events added'.
        """

        header_label = tk.Label(self, text="Events", font=("Montserrat", 18, "bold"))
        header_label.pack(pady=20)

        events_frame = tk.Frame(self)
        events_frame.pack(pady=10, padx=20, fill="both", expand=True)

        back_button = tk.Button(self, text="Back", font=("Montserrat 7 bold"), command=lambda: controller.show_frame(FirstPage))
        back_button.place(x=20, y=20, height=20, width = 34)

        #bounds for displaying the events
        lower = 0
        upper = 2

        if os.path.exists(events_file):
            with open(events_file, "r") as file:
                for i,line in enumerate(file):
                    if lower<=i<=upper:

                        title, date, time, description, location, event_type = line.strip().split("|")
                        event = {
                            "title": title,
                            "date": date,
                            "time": time,
                            "description": description,
                            "location": location,
                            "type": event_type
                        }

                        event_box = tk.Frame(events_frame, borderwidth=1, relief="solid", padx=10, pady=10)
                        event_box.pack(fill="x", pady=5)

                        event_title = tk.Label(event_box, text=title, font=("Montserrat", 14, "bold"))
                        event_title.pack(anchor="w")

                        event_details = tk.Label(event_box,
                                                 text=f"Event type: {event_type} | Time: {time} | Location: {location}",
                                                 font=("Montserrat", 12))
                        event_details.pack(anchor="w")

                        view_button = ttk.Button(event_box, text="View", command=lambda e=event: show_event_details(e))
                        view_button.pack(anchor="e", pady=5)

                        view_button = tk.Button(self, text="next page")
                        view_button.pack(anchor="e", pady=5)



        else:
            no_events_label = tk.Label(events_frame, text="No events added yet.", font=("Montserrat", 14))
            no_events_label.pack(pady=20)




# Driver Code
app = tkinterApp()

app.mainloop()
