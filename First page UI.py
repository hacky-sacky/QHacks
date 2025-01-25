import tkinter as tk
from tkinter import font


root = tk.Tk()
root.title('simple app')
root.resizable(False, False)
root.geometry("500x500")

root.config(bg= 'grey')

thing_to_do_btn = tk.Button(root, text='things to do', bg='light grey', font= ('Arial 12 bold'))
thing_to_do_btn.place(x = 37.5, y = 10, height = 30, width = 125)

chat_wt_ppl_btn = tk.Button(root, text='chat with people', bg='light grey',font= ('Arial 10 bold'))
chat_wt_ppl_btn.place(x = 187.5, y = 10, height = 30, width = 125)

account_btn = tk.Button(root, text='Account', bg='light grey',font= ('Arial 12 bold'))
account_btn.place(x = 337.5, y = 10, height = 30, width = 125)

underlined_font = font.Font(family="Arial", size=12, underline=True)
# height = 15 pixels

search_bar = tk.Entry(root, font= ('Arial 15 bold'))
search_bar.place(x = 50, y = 100, height = 50, width = 400)

try_smth_new_txt = tk.Label(root, text= 'try something new ...', bg= 'grey', fg = 'blue', font= underlined_font)
try_smth_new_txt.place(x = 150, y = 200, height = 25, width = 150)



root.mainloop()
#locks the screen


