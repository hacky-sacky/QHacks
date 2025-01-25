from socket import *
from threading import *
import tkinter as tk
from tkinter import *

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

host_ip = "127.0.0.1"
port_number = 55667

client_socket.bind((host_ip, port_number))

root = tk.Tk()
root.title("Connected to: " + host_ip + ":" + str(port_number))

txt_messages = Text(root, width=50)
txt_messages.grid(row=0, column=0, padx=10, pady=10)

txt_entry = Entry(root, width=50)
txt_entry.insert(0, "Your message")
txt_entry.grid(row=1, column=0, padx=10, pady=10)

def send_message():
    client_message = txt_entry.get()
    txt_messages.insert(END, "\n" + "You: " + client_message)
    client_socket.send(client_message.encode("utf-8"))

send_button = Button(root, text="Send", width=20, command=send_message)
send_button.grid(row=2, column=0, padx=10, pady=10)

def recv_message():
    while True:
        server_message = client_socket.recv(1024).decode("utf-8")
        print(server_message)
        txt_messages.insert(END, "\n" + server_message)

recv_thread = Thread(target=recv_message)
recv_thread.daemon = True
recv_thread.start()

root.mainloop()