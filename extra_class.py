bg = PhotoImage(file="pictures/homepage.png")
        bglabel = Label(self, image=bg)
        bglabel.image = bg
        bglabel.place(x=0, y=0)

        thing_to_do_btn = tk.Button(self, text='Things To Do', bg='light grey', font=('Arial 12 bold'),
                                    command=lambda: controller.show_frame(EventsPage))
        thing_to_do_btn.place(x=30, y=360, height=30, width=125)

        chat_wt_ppl_btn = tk.Button(self, text='Chat With People', bg='light grey', font=('Arial 10 bold'))
        chat_wt_ppl_btn.place(x=187.5, y=360, height=30, width=125)

        global i

        canvas = tk.Canvas(self, width=400, height=100, bg= '#3C6E47', bd=0, highlightthickness=0)
        canvas.create_text(200, 50, text="Active Kingston", font='Helvetica 40 bold', fill='#FFB300')
        canvas.place(x=50, y=20)


        account_btn = tk.Button(self, text='Account', bg='light grey', font='Arial 12 bold',
                                command=lambda: controller.show_frame(test(i)))
        account_btn.place(x=337.5, y=360, height=30, width=125)
        print(f'also {i}')

        underlined_font = font.Font(family="Arial", size=12, underline=True)
        # height = 15 pixels

        search_bar = tk.Entry(self, font=('Arial 15 bold'), bg='white', fg='black')
        search_bar.place(x=50, y=235, height=50, width=400)
        search_bar.bind("<Return>", lambda event: show_details_of_event(search_bar.get()))
        search_bar.delete(0, tk.END)
