import tkinter as tk
from tkinter import ttk
from tkinter import Tk, Toplevel, Text, Scrollbar, Button, END, RIGHT, Y, BOTH

import os

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
        with open(events_file, "a") as file:
            file.write(f"{title}|{date}|{start_time}-{end_time}|{description}|{location}|{event_type}\n")
        result_label.config(text=f"Event '{title}' added successfully!", fg="green")
        clear_form()
    else:
        result_label.config(text="Please fill out all fields.", fg="red")

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
    """
    Shows the event details on a separate page after clicking the
    view button on the events from the 'Events Page'. Uses the same
    GUI as the 'Add Event Form'.
    """
    details_window = tk.Toplevel(root)
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

    description_label = tk.Label(details_window, text=f"Description: {event['description']}", font=("Montserrat", 14), wraplength=500, justify="left")
    description_label.pack(anchor="w", padx=20, pady=5)

    location_label = tk.Label(details_window, text=f"Location: {event['location']}", font=("Montserrat", 14))
    location_label.pack(anchor="w", padx=20, pady=5)

    type_label = tk.Label(details_window, text=f"Type: {event['type']}", font=("Montserrat", 14))
    type_label.pack(anchor="w", padx=20, pady=5)

# IMPORTANT: LINK THIS FUNCTION TO 'THINGS TO DO' BUTTON
def show_events_page():
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
    events_window = tk.Toplevel(root)
    events_window.title("Events")
    events_window.geometry("600x600")

    header_label = tk.Label(events_window, text="Events", font=("Montserrat", 18, "bold"))
    header_label.pack(pady=20)

    scroll_frame = tk.Frame(events_window)
    scroll_frame.pack(fill="both", expand=True)

    canvas = tk.Canvas(scroll_frame)
    scrollbar = ttk.Scrollbar(scroll_frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.pack(side="left", fill="both", expand=True)
    canvas.configure(yscrollcommand=scrollbar.set)

    events_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=events_frame, anchor="nw")

    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    events_frame.bind("<Configure>", on_frame_configure)

    if os.path.exists(events_file):
        with open(events_file, "r") as file:
            for line in file:
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

                event_details = tk.Label(event_box, text=f"Event type: {event_type} | Time: {time} | Location: {location}", font=("Montserrat", 12))
                event_details.pack(anchor="w")

                view_button = ttk.Button(event_box, text="View", command=lambda e=event: show_event_details(e))
                view_button.pack(anchor="e", pady=5)
    else:
        no_events_label = tk.Label(events_frame, text="No events added yet.", font=("Montserrat", 14))
        no_events_label.pack(pady=20)

# main GUI for add new event
root = tk.Tk()
root.title("Add New Event")
root.geometry("600x600")

# Create a header
header_label = tk.Label(root, text="Add New Event", font=("Montserrat", 18, "bold"))
header_label.pack(pady=20)

# Create a frame for the form
form_frame = tk.Frame(root)
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
type_dropdown = ttk.Combobox(form_frame, textvariable=type_var, font=("Montserrat", 12), width=38, state="readonly")
type_dropdown['values'] = ["Sports", "Food", "Entertainment", "Shopping", "Study"]
type_dropdown.grid(row=6, column=1, pady=5)

submit_button = ttk.Button(root, text="Submit", command=submit_event)
submit_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Montserrat", 12))
result_label.pack(pady=10)

root.mainloop()
