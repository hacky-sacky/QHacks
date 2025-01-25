import tkinter as tk
from tkinter import ttk

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
    else:
        result_label.config(text="Please fill out all fields.", fg="red")

# Main application
root = tk.Tk()
root.title("Add New Event")
root.geometry("500x500")

# Creating a header
header_label = tk.Label(root, text="Add New Event", font=("Montserrat", 18, "bold"))
header_label.pack(pady=20)

# Create a frame for the form
form_frame = tk.Frame(root)
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
type_dropdown = ttk.Combobox(form_frame, textvariable=type_var, font=("Montserrat", 12), width=38, state="readonly")
type_dropdown['values'] = ["Sports", "Food", "Entertainment", "Shopping", "Study"]
type_dropdown.grid(row=6, column=1, pady=5)

# Submit button at the end of form
submit_button = ttk.Button(root, text="Submit", command=submit_event)
submit_button.pack(pady=20)

result_label = tk.Label(root, text="", font=("Montserrat", 12))
result_label.pack(pady=10)

root.mainloop()