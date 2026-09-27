#line 7901 - create new event

#for month
    def list_month(data: dict):

        event_date = data['event'][0]

        if len(event_date) == 4:

            current_month = event_date[0]

        elif len(event_date) == 5:

            current_month = event_date[0:2]

        info_month = ['January', 'February', 'March',
                      'April', 'May', 'June',
                      'July', 'August', 'September',
                      'October', 'November', 'December'
                      ]

        current_month = int(current_month)
        final_list = []

        for i in range(current_month):
            month_name = info_month[i]
            final_list.append((month_name, i+1))

        return final_list

    def Click_month(e, var):

        nclist = list_month(data = data)
        my_menu = Menu(None, tearoff=0, takefocus=0)

        for (txt, cmd) in nclist:
            exec(f"(my_menu.add_command(label = '{txt}', command = lambda: canvas.itemconfig({es12}, text = '{txt}')))")

        my_menu.tk_popup(e.x_root - 85, e.y_root + 16,entry="0")


    m_var = StringVar()

    es_button_image_2 = PhotoImage(
        file=relative_to_assets(direc = 'Event Settings', path = "button_2.png"))
    es_button_2 = Button(
        image=es_button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: None,
        relief="flat"
    )
    es_button_2.bind("<Button-1>", lambda e, var = m_var: Click_month(e, var))
    es_button_2.place(
        x=611.5009765625,
        y=456.0,
        width=14,
        height=8.0
    )


#for day
    def list_day():

        final_list = []

        for i in range(31):
            final_list.append((i+1, i+1))
            
        return final_list

    def Click_day(e, var):

        nclist = list_day()
        my_menu = Menu(None, tearoff=0, takefocus=0)
    
        for (txt, cmd) in nclist:
            exec(f"(my_menu.add_command(label = '{txt}', command = lambda: canvas.itemconfig({es13}, text = '{txt}')))")
            
        my_menu.tk_popup(e.x_root - 80, e.y_root + 16,entry="0")
        

    d_var = StringVar()

    es_button_image_3 = PhotoImage(
        file=relative_to_assets(direc = 'Event Settings', path = "button_3.png"))
    es_button_3 = Button(
        image=es_button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: None,
        relief="flat"
    )
    es_button_3.bind("<Button-1>", lambda e, var = d_var: Click_day(e, var))
    es_button_3.place(
        x=761.0009765625,
        y=455.5,
        width=14,
        height=8.0
    )

#extract name

    def extract_name():

        #if current date is 5 days before pre-assigned event date
        event_date = data['event'][0]
        current_time = dt.datetime.now()
        current_year = dt.date.today().year
        event_date += f"/{current_year}" #4/23/2022
        event_time = dt.datetime.strptime(event_date, '%m/%d/%Y')

        time_differential = event_time - current_time
        days_differential = time_differential.days

        if (days_differential <= 5) == False:
        
            event_name_a = entry_1.get()

            if event_name_a == 'New name for current event':
                delete_event_settings()

            func.change_event_name(name = str(event_name_a))

        else:

            call_error(error_text = 'Unable to change name of current event.')
            call_error(error_text = 'Current event is less than 5 days away.')

        delete_event_settings()


#extract date

    def extract_date():

        #if current date is 5 days before pre-assigned event date
        event_date = data['event'][0]
        current_time = dt.datetime.now()
        current_year = dt.date.today().year
        event_date += f"/{current_year}" #4/23/2022
        event_time = dt.datetime.strptime(event_date, '%m/%d/%Y')

        time_differential = event_time - current_time
        days_differential = time_differential.days

        if (days_differential <= 5) == False:
            
            event_date = data['event'][0]

            month_a = es12
            day_a = es13

            month_info_a = {'January': 1,
                            'February': 2,
                            'March': 3,
                            'April': 4,
                            'May': 5,
                            'June': 6,
                            'July': 7,
                            'August': 8,
                            'September': 9,
                            'October': 10,
                            'November': 11,
                            'December': 12
                            }

            month_num = month_info_a[month_a]

            outputc = func.change_event_date(month = month_num, day_a = day_a)

            if outputc != 'All clear':
                call_error(error_text = 'Unable to change date of current event.')
                call_error(error_text = outputc)

        else:

            call_error(error_text = 'Unable to change date of current event.')
            call_error(error_text = 'Current event is less than 5 days away.')

        delete_event_settings()
