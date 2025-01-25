import tkinter as tk
from tkinter import ttk
from tkinter import font
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
        for F in ( FirstPage, AddEventPage):
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



# first window frame startpage
class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.config(bg='grey')

        thing_to_do_btn = tk.Button(self, text='Things To Do', bg='light grey', font=('Arial 12 bold'))
        thing_to_do_btn.place(x=30, y=10, height=30, width=125)

        chat_wt_ppl_btn = tk.Button(self, text='Chat With People', bg='light grey', font=('Arial 10 bold'))
        chat_wt_ppl_btn.place(x=187.5, y=10, height=30, width=125)

        account_btn = tk.Button(self, text='Account', bg='light grey', font=('Arial 12 bold'))
        account_btn.place(x=337.5, y=10, height=30, width=125)

        underlined_font = font.Font(family="Arial", size=12, underline=True)
        # height = 15 pixels

        search_bar = tk.Entry(self, font=('Arial 15 bold'))
        search_bar.place(x=50, y=100, height=50, width=400)

        try_smth_new_txt = tk.Label(self, text='try something new ...', bg='grey', fg='blue', font=underlined_font)
        try_smth_new_txt.place(x=150, y=200, height=25, width=150)

        add_button = tk.Button(self, text= '+', font=('Arial 15 bold'), command=lambda: controller.show_frame(AddEventPage))
        add_button.place(x=430, y= 160, height=20, width=20)


class AddEventPage(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        # Function that handles form submission
        def submit_event():
            title = title_var.get()
            date = date_var.get()
            start_time = start_time_var.get()
            end_time = end_time_var.get()
            description = description_text.get("1.0", tk.END).strip()
            location = location_var.get()
            event_type = type_var.get()

            if all([title, date, start_time, end_time, description, location, event_type]):
                result_label.config(text=f"Event '{title}' added successfully!", fg="green")
                self.after(2000, lambda: controller.show_frame(FirstPage))
            else:
                result_label.config(text="Please fill out all fields.", fg="red")


        # Creating a header
        header_label = tk.Label(self, text="Add New Event", font=("Montserrat", 18, "bold"))
        header_label.pack(pady=20)

        # Create a frame for the form
        form_frame = tk.Frame(self)
        form_frame.pack(pady=10, padx=20, fill="x")

        # Title of event
        title_label = tk.Label(form_frame, text="Title:", font=("Montserrat", 12))
        title_label.grid(row=0, column=0, sticky="w", pady=5)
        title_var = tk.StringVar()
        title_entry = ttk.Entry(form_frame, textvariable=title_var, font=("Montserrat", 12), width=40)
        title_entry.grid(row=0, column=1, pady=5)

        # Date of event
        date_label = tk.Label(form_frame, text="Date (YYYY-MM-DD):", font=("Montserrat", 12))
        date_label.grid(row=1, column=0, sticky="w", pady=5)
        date_var = tk.StringVar()
        date_entry = ttk.Entry(form_frame, textvariable=date_var, font=("Montserrat", 12), width=40)
        date_entry.grid(row=1, column=1, pady=5)

        # Start time of event
        start_time_label = tk.Label(form_frame, text="Start Time (HH:MM):", font=("Montserrat", 12))
        start_time_label.grid(row=2, column=0, sticky="w", pady=5)
        start_time_var = tk.StringVar()
        start_time_entry = ttk.Entry(form_frame, textvariable=start_time_var, font=("Montserrat", 12), width=40)
        start_time_entry.grid(row=2, column=1, pady=5)

        # End time of event
        end_time_label = tk.Label(form_frame, text="End Time (HH:MM):", font=("Montserrat", 12))
        end_time_label.grid(row=3, column=0, sticky="w", pady=5)
        end_time_var = tk.StringVar()
        end_time_entry = ttk.Entry(form_frame, textvariable=end_time_var, font=("Montserrat", 12), width=40)
        end_time_entry.grid(row=3, column=1, pady=5)

        # Description of event
        description_label = tk.Label(form_frame, text="Description:", font=("Montserrat", 12))
        description_label.grid(row=4, column=0, sticky="nw", pady=5)
        description_text = tk.Text(form_frame, font=("Montserrat", 12), width=40, height=5)
        description_text.grid(row=4, column=1, pady=5)

        # Location of event
        location_label = tk.Label(form_frame, text="Location:", font=("Montserrat", 12))
        location_label.grid(row=5, column=0, sticky="w", pady=5)
        location_var = tk.StringVar()
        location_entry = ttk.Entry(form_frame, textvariable=location_var, font=("Montserrat", 12), width=40)
        location_entry.grid(row=5, column=1, pady=5)

        # Drop-down type of event
        type_label = tk.Label(form_frame, text="Type of Event:", font=("Montserrat", 12))
        type_label.grid(row=6, column=0, sticky="w", pady=5)
        type_var = tk.StringVar()
        type_dropdown = ttk.Combobox(form_frame, textvariable=type_var, font=("Montserrat", 12), width=38,
                                     state="readonly")
        type_dropdown['values'] = ["Sports", "Food", "Entertainment", "Shopping", "Study"]
        type_dropdown.grid(row=6, column=1, pady=5)

        # Submit button at the end of form
        submit_button = ttk.Button(self, text="Submit", command=submit_event)
        submit_button.place(x=170, y=400)

        cancel_button = ttk.Button(self, text="Cancel", command=lambda: controller.show_frame(FirstPage))
        cancel_button.place(x=270, y=400)


        result_label = tk.Label(self, text="", font=("Montserrat", 12))
        result_label.place(y=450, x=150)


# Driver Code
app = tkinterApp()
app.mainloop()
