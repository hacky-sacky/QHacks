import tkinter as tk
from tkinter import ttk
from tkinter import *

import csv
import os
from tkinter import font

from tkcalendar import Calendar

# global variables

# T/F for if login or not
i = 0

user = 'dsadsa'

LARGEFONT = ("Verdana", 35)
class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp

    # self it like self  (self = tk.Tk())

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
        for F in (FirstPage, AccountPages, SignUpPage, LoginPage, ProfilePage, EventsPage):

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

'''def return_user():

    return user'''

# first window frame startpage
class FirstPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        bg = PhotoImage(file="pictures/signupbg.png")
        bglabel = Label(self, image=bg)
        bglabel.image = bg
        bglabel.place(x=0, y=0)

        thing_to_do_btn = tk.Button(self, text='Things To Do', bg='light grey', font=('Arial 12 bold'),
                                    command=lambda: controller.show_frame(EventsPage))
        thing_to_do_btn.place(x=30, y=300, height=30, width=125)

        chat_wt_ppl_btn = tk.Button(self, text='Chat With People', bg='light grey', font=('Arial 10 bold'))
        chat_wt_ppl_btn.place(x=187.5, y=300, height=30, width=125)

        global i

        canvas = tk.Canvas(self, width=400, height=100, bg= 'lime green', bd=0, highlightthickness=0)
        canvas.create_text(200, 50, text="Active Kingston", font='Helvetica 40 bold', fill='gold')
        canvas.pack()


        account_btn = tk.Button(self, text='Account', bg='light grey', font='Arial 12 bold',
                                command=lambda: controller.show_frame(test(i)))
        account_btn.place(x=337.5, y=300, height=30, width=125)
        print(f'also {i}')

        underlined_font = font.Font(family="Arial", size=12, underline=True)
        # height = 15 pixels

        search_bar = tk.Entry(self, font=('Arial 15 bold'))
        search_bar.place(x=50, y=200, height=50, width=400)
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






class EventsPage(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        events_file = "events_by_date.txt"

        if not os.path.exists(events_file):
            with open(events_file, "w") as file:
                pass

        def show_events_for_date(selected_date):
            """
            This function shows the particular event for a selected
            date after selecting a date on the calendar then pressing
            "View Events". Same GUI as main show events page.
            """
            formatted_date = selected_date.lstrip("0").replace("/0", "/")
            events_window = Toplevel(self)
            events_window.title(f"Events on {formatted_date}")
            events_window.geometry("600x600")

            header_label = Label(events_window, text=f"Events on {formatted_date}", font=("Arial", 16, "bold"))
            header_label.pack(pady=10)

            events_frame = Frame(events_window)
            events_frame.pack(fill="both", expand=True, padx=10, pady=10)

            canvas = Canvas(events_frame)
            scrollbar = ttk.Scrollbar(events_frame, orient="vertical", command=canvas.yview)
            scrollable_frame = Frame(canvas)

            scrollable_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
            )

            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)

            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")

            events_found = False

            if os.path.exists(events_file):
                with open(events_file, "r") as file:
                    for line in file:
                        date, title, time, description, location, event_type = line.strip().split("|")
                        if date == formatted_date:
                            events_found = True
                            event_box = Frame(scrollable_frame, borderwidth=1, relief="solid", padx=10, pady=10)
                            event_box.pack(fill="x", pady=5)

                            Label(event_box, text=title, font=("Arial", 14, "bold")).pack(anchor="w")
                            Label(event_box, text=f"Type: {event_type} | Time: {time} | Location: {location}",
                                  font=("Arial", 12)).pack(anchor="w")
                            Label(event_box, text=description, font=("Arial", 12, "italic")).pack(anchor="w", pady=5)

            if not events_found:
                Label(scrollable_frame, text="No events found on this date.", font=("Arial", 14)).pack(pady=20)

        def calendar_page():
            """
            Main calendar event page which has all the stored
            events on the particular dates.
            """
            calendar_window = Toplevel(self)
            calendar_window.title("Event Calendar")
            calendar_window.geometry("500x500")

            Label(calendar_window, text="Select a Date", font=("Arial", 16, "bold")).pack(pady=10)

            cal = Calendar(calendar_window, selectmode='day', year=2025, month=1, day=25, showweeknumbers=False)
            cal.pack(pady=20, expand=True, fill=BOTH)

            def get_events():
                """
                Direct users to the events page for the particular
                date after they select a date from the calendar and
                then press the "View Events" button.
                """
                selected_date = cal.get_date()
                show_events_for_date(selected_date)

            Button(calendar_window, text="View Events", command=get_events).pack(pady=20)

        def show_events_page():
            """
            This function displays the 'Events' page with all the events added
            by users.
            Reads the `events_by_date.txt` file and shows all events.
            """
            events_window = Toplevel(self)
            events_window.title("All Events")
            events_window.geometry("600x600")

            header_label = Label(events_window, text="All Events", font=("Arial", 18, "bold"))
            header_label.pack(pady=10)

            # Scrollable Frame
            events_frame = Frame(events_window)
            events_frame.pack(fill="both", expand=True, padx=10, pady=10)

            canvas = Canvas(events_frame)
            scrollbar = ttk.Scrollbar(events_frame, orient="vertical", command=canvas.yview)
            scrollable_frame = Frame(canvas)

            scrollable_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
            )

            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)

            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")

            # Read and display events
            events_found = False

            if os.path.exists(events_file):
                with open(events_file, "r") as file:
                    for line in file:
                        # Ensure the line is valid
                        if "|" in line:
                            date, title, time, description, location, event_type = line.strip().split("|")
                            events_found = True

                            # Event Display
                            event_box = Frame(scrollable_frame, borderwidth=1, relief="solid", padx=10, pady=10)
                            event_box.pack(fill="x", pady=5)

                            Label(event_box, text=title, font=("Arial", 14, "bold")).pack(anchor="w")
                            Label(event_box, text=f"Date: {date} | Type: {event_type}", font=("Arial", 12)).pack(
                                anchor="w")
                            Label(event_box, text=f"Time: {time} | Location: {location}", font=("Arial", 12)).pack(
                                anchor="w")
                            Label(event_box, text=description, font=("Arial", 12, "italic")).pack(anchor="w", pady=5)

            if not events_found:
                Label(scrollable_frame, text="No events found.", font=("Arial", 14)).pack(pady=20)

        def add_event_page():
            def save_event():
                title = title_entry.get()
                date = cal.get_date()
                start_time = start_time_entry.get()
                end_time = end_time_entry.get()
                description = description_text.get("1.0", END).strip()
                location = location_entry.get()
                event_type = event_type_var.get()

                if not title or not date or not start_time or not end_time or not location or not event_type:
                    error_label.config(text="All fields are required!", fg="red")
                    return

                formatted_date = date.lstrip("0").replace("/0", "/")

                with open(events_file, "a") as file:
                    file.write(
                        f"{formatted_date}|{title}|{start_time}-{end_time}|{description}|{location}|{event_type}\n")

                error_label.config(text="Event added successfully!", fg="green")

                title_entry.delete(0, END)
                start_time_entry.delete(0, END)
                end_time_entry.delete(0, END)
                description_text.delete("1.0", END)
                location_entry.delete(0, END)
                event_type_var.set("")

            add_window = Toplevel(self)
            add_window.title("Add New Event")
            add_window.geometry("600x830")

            Label(add_window, text="Add New Event", font=("Arial", 18, "bold")).pack(pady=10)

            # Event Title
            Label(add_window, text="Title:").pack(anchor="w", padx=20, pady=5)
            title_entry = Entry(add_window, width=40)
            title_entry.pack(padx=20, pady=5)

            # Date Picker
            Label(add_window, text="Date:").pack(anchor="w", padx=20, pady=5)
            cal = Calendar(add_window, selectmode='day', showweeknumbers=False, font=("Arial", 12), borderwidth=2)
            cal.pack(pady=5)

            # Start and End Time
            Label(add_window, text="Start Time:").pack(anchor="w", padx=20, pady=5)
            start_time_entry = Entry(add_window, width=20)
            start_time_entry.pack(padx=20, pady=5)

            Label(add_window, text="End Time:").pack(anchor="w", padx=20, pady=5)
            end_time_entry = Entry(add_window, width=20)
            end_time_entry.pack(padx=20, pady=5)

            # Description
            Label(add_window, text="Description:").pack(anchor="w", padx=20, pady=5)
            description_text = Text(add_window, height=5, width=50)
            description_text.pack(padx=20, pady=5)

            # Location
            Label(add_window, text="Location:").pack(anchor="w", padx=20, pady=5)
            location_entry = Entry(add_window, width=40)
            location_entry.pack(padx=20, pady=5)

            Label(add_window, text="Type:").pack(anchor="w", padx=20, pady=5)
            event_type_var = StringVar()
            event_type_dropdown = ttk.Combobox(add_window, textvariable=event_type_var,
                                               values=["Sports", "Food", "Entertainment", "Shopping", "Study"])
            event_type_dropdown.pack(padx=20, pady=5)

            error_label = Label(add_window, text="", font=("Arial", 12))
            error_label.pack(pady=10)
            Button(add_window, text="Save Event", command=save_event).pack(pady=10)

            Button(add_window, text="View Calendar", command=calendar_page).pack(pady=20)

        Button(self, text="Add New Event", command=add_event_page, width=20).pack(pady=20)
        Button(self, text="View Calendar", command=calendar_page, width=20).pack(pady=20)
        Button(self, text="View Events", command=show_events_page, width=20).pack(pady=20)

        back_button = tk.Button(self, text="Back", font=("Montserrat 7 bold"),
                                command=lambda: controller.show_frame(FirstPage))
        back_button.place(x=20, y=20, height=20, width=34)


class AccountPages(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        bg = PhotoImage(file="pictures/signupbg.png")
        bglabel = Label(self, image=bg)
        bglabel.image = bg
        bglabel.place(x=0, y=0)

        signup_button = tk.Button(self, command=lambda: controller.show_frame(SignUpPage),
                                  text='Sign Up',
                                  bg='light blue',
                                  font=('Arial 30 bold'))
        signup_button.place(x=160, y=70, height=100, width=200)

        login_button = tk.Button(self,
                                 text='Log In',
                                 bg='light blue',
                                 font=('Arial 30 bold'),
                                 command=lambda: controller.show_frame(LoginPage))
        login_button.place(x=160, y=270, height=100, width=200)

        back_button = tk.Button(self, text="Back", font=("Montserrat 7 bold"),
                                command=lambda: controller.show_frame(FirstPage))
        back_button.place(x=20, y=20, height=20, width=34)


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

                global user
                user = "Andy"

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

        back_button = tk.Button(self, text="Back", font=("Montserrat 7 bold"),
                                command=lambda: controller.show_frame(FirstPage))
        back_button.place(x=20, y=20, height=20, width=34)

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

                global user
                user = "Andy"


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

        back_button = tk.Button(self, text="Back", font=("Montserrat 7 bold"),
                                command=lambda: controller.show_frame(FirstPage))
        back_button.place(x=20, y=20, height=20, width=34)


class ProfilePage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        bg = PhotoImage(file="pictures/profilepage.png")
        bglabel = Label(self, image=bg)
        bglabel.image = bg
        bglabel.place(x=0, y=0)

        pfp = PhotoImage(file="pictures/NEWAMONGUS.png")
        pfplabel = Label(self, image=pfp)
        pfplabel.image = pfp
        pfplabel.place(x=60, y=100)

        username = Label(self, text=(f"hello"), fg='white', bg="#006994", font=("Montserrat 20 bold"))
        username.place(x=200, y=120)

        event_button = Button(self, text="New Event")
        event_button.place(x=80, y=300)

        review_button = Button(self, text="Leave Review")
        review_button.place(x=260, y=300)

        back_button = tk.Button(self, text="Back", font=("Montserrat 7 bold"),
                                command=lambda: controller.show_frame(FirstPage))
        back_button.place(x=20, y=20, height=20, width=34)

# Driver Code
app = tkinterApp()

app.mainloop()
