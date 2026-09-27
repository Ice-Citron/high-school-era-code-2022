
from pathlib import Path
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, END, NORMAL, DISABLED, StringVar, Menu, Label

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from math import pi

##########################################################################################################################################################################################################

from functions import function_input, function_check, data_retrieve, data_save, drive_check, undo_init, connection_check
from forms import function_forms, token
from undo import undo_func

import datetime as dt
import json
import time

#import sys
#sys.path.insert(1, 'GUI/Login page')sys.path.insert(1, 'GUI/dashboard')

initial_glitch = False

def relative_to_assets(direc: str, path: str) -> Path:
    two_level_up = Path(__file__).parents[0]
    
    OUTPUT_PATH = f"{two_level_up}/GUI/{direc}"
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")

    return ASSETS_PATH / Path(path)


##########################################################################################################################################################################################################


window = Tk()

window.resizable(False, False)
window.geometry("1280x785")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 800,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)



##########################################################################################################################################################################################################

'''
form_service, drive_service = token().return_form_service()

folder_id = drive_check(drive_service = drive_service)
data, data_fileId = data_retrieve(drive_service = drive_service, folder_id = folder_id)
note that data_fileId is the fileId for data.json in the drive
'''
with open("data.json", "r") as datafile:
    data = json.load(datafile)
'''
func = function_input(datafile = data)
chec = function_check(datafile = data)
form = function_forms(datafile = data,
                      form_service = form_service,
                      drive_service = drive_service,
                      folder_id = folder_id)

undo = undo_func(datafile = data,
                 undofile = undo_init(),
                 form_service = form_service,
                 drive_service = drive_service,
                 folder_id = folder_id
                 )'''


##########################################################################################################################################################################################################

'''connection error external'''

def create_internet_error():

    def delete_internet_error():
    
        canvas.itemconfig(ie1, state = 'hidden')
        canvas.itemconfig(ie2, state = 'hidden')
        canvas.itemconfig(ie3, state = 'hidden')
        canvas.itemconfig(ie4, state = 'hidden')
        canvas.itemconfig(ie5, state = 'hidden')
        canvas.itemconfig(ie6, state = 'hidden')
        canvas.itemconfig(ie7, state = 'hidden')
        canvas.itemconfig(ie8, state = 'hidden')
        canvas.itemconfig(ie9, state = 'hidden')
        canvas.itemconfig(ie10, state = 'hidden')

        ie_button_1.lower()

        if initial == True:
            initialise()
            

    def check_internet_connection():

        #if connection is available
        
        if connection_check() == True:
            
            delete_internet_error()


    ie_image_1 = PhotoImage(
        file=relative_to_assets(direc = 'Internet Error', path = "image_1.png"))
    ie1 = canvas.create_image(
        640.0,
        400.0,
        image=ie_image_1
    )

    ie_label_1 = Label(canvas, image = ie_image_1)
    ie_label_1.image = ie_image_1

    ie_image_2 = PhotoImage(
        file=relative_to_assets(direc = 'Internet Error', path = "image_2.png"))
    ie2 = canvas.create_image(
        639.7705078125,
        399.0361328125,
        image=ie_image_2
    )

    ie_label_2 = Label(canvas, image = ie_image_2)
    ie_label_2.image = ie_image_2

    ie_image_3 = PhotoImage(
        file=relative_to_assets(direc = 'Internet Error', path = "image_3.png"))
    ie3 = canvas.create_image(
        639.376953125,
        399.58642578125,
        image=ie_image_3
    )

    ie_label_3 = Label(canvas, image = ie_image_3)
    ie_label_3.image = ie_image_3

    ie_image_4 = PhotoImage(
        file=relative_to_assets(direc = 'Internet Error', path = "image_4.png"))
    ie4 = canvas.create_image(
        639.376953125,
        405.4169921875,
        image=ie_image_4
    )

    ie_label_4 = Label(canvas, image = ie_image_4)
    ie_label_4.image = ie_image_4

    ie_image_5 = PhotoImage(
        file=relative_to_assets(direc = 'Internet Error', path = "image_5.png"))
    ie5 = canvas.create_image(
        639.0,
        349.0,
        image=ie_image_5
    )

    ie_label_5 = Label(canvas, image = ie_image_5)
    ie_label_5.image = ie_image_5

    ie_image_6 = PhotoImage(
        file=relative_to_assets(direc = 'Internet Error', path = "image_6.png"))
    ie6 = canvas.create_image(
        639.0,
        461.6171875,
        image=ie_image_6
    )

    ie_label_6 = Label(canvas, image = ie_image_6)
    ie_label_6.image = ie_image_6

    ie_button_image_1 = PhotoImage(
        file=relative_to_assets(direc = 'Internet Error', path = "button_1.png"))
    ie_button_1 = Button(
        image=ie_button_image_1,
        highlightthickness=0,
        command=lambda: check_internet_connection(),
        relief="flat"
    )
    ie_button_1.place(
        x=730.0009765625,
        y=475.0,
        width=61,
        height=17
    )

    ie_button_label_1 = Label(canvas, image = ie_button_image_1)
    ie_button_label_1.image = ie_button_image_1


    ie7 = canvas.create_text(
        481.5009765625,
        317.5,
        anchor="nw",
        text="No connection",
        fill="#D1D3D4",
        font=("Inter", 20 * -1)
    )

    ie8 = canvas.create_text(
        482.0,
        373.0,
        anchor="nw",
        text="Please connect to an internet connection.",
        fill="#D1D3D4",
        font=("Inter", 11 * -1)
    )

    ie9 = canvas.create_text(
        482.0,
        404.0,
        anchor="nw",
        text="The app is unable to function without a connection. As",
        fill="#D1D3D4",
        font=("Inter", 11 * -1)
    )

    ie10 = canvas.create_text(
        482.0,
        420.0,
        anchor="nw",
        text="the data storage method is cloud based.",
        fill="#D1D3D4",
        font=("Inter", 11 * -1)
    )



def check_connection():

    result = connection_check()

    if result == False:

        create_internet_error()
        raise



##########################################################################################################################################################################################################

'''dashboard and login create'''

def create_main_frame(odd_initial: bool):

    
    def lower_dashboard_buttons():

        #button_1['state'] = DISABLED
        button_1.lower()
        button_2.lower()
        button_3.lower()
        button_4.lower()
        button_5.lower()
        button_6.lower()
        button_7.lower()
        button_8.lower()
        button_9.lower()
        button_10.lower()
        button_11.lower()
        button_12.lower()
        button_13.lower()
        button_14.lower()
        button_15.lower()
        button_16.lower()
        button_17.lower()
        button_18.lower()
        button_19.lower()
        button_20.lower()
        button_21.lower()
        button_22.lower()
        button_23.lower()
        button_24.lower()
        button_25.lower()

        destroy_progress_bar()
        destroy_dashboard_charts()
        


    def raise_dashboard_buttons():

        button_1.lift()
        button_2.lift()
        button_3.lift()
        button_4.lift()
        button_5.lift()
        button_6.lift()
        button_7.lift()
        button_8.lift()
        button_9.lift()
        button_10.lift()
        button_11.lift()
        button_12.lift()
        button_13.lift()
        button_14.lift()
        button_15.lift()
        button_16.lift()
        button_17.lift()
        button_18.lift()
        button_19.lift()
        button_20.lift()
        button_21.lift()
        button_22.lift()
        button_23.lift()
        button_24.lift()
        button_25.lift()

        create_chart(chart_type = 'timespent', year_over = 'year', data = data, x_cord = 540, y_cord = 597)
        create_chart(chart_type = 'profit', year_over = 'year', data = data, x_cord = 540, y_cord = 385)

        refresh_data()
        


    def create_internet_error():
        
        def delete_internet_error():
        
            canvas.itemconfig(ie1, state = 'hidden')
            canvas.itemconfig(ie2, state = 'hidden')
            canvas.itemconfig(ie3, state = 'hidden')
            canvas.itemconfig(ie4, state = 'hidden')
            canvas.itemconfig(ie5, state = 'hidden')
            canvas.itemconfig(ie6, state = 'hidden')
            canvas.itemconfig(ie7, state = 'hidden')
            canvas.itemconfig(ie8, state = 'hidden')
            canvas.itemconfig(ie9, state = 'hidden')
            canvas.itemconfig(ie10, state = 'hidden')

            ie_button_1.lower()

            raise_dashboard_buttons()
                

        def check_internet_connection():

            #if connection is available
            
            if connection_check() == True:
                
                delete_internet_error()


        ie_image_1 = PhotoImage(
            file=relative_to_assets(direc = 'Internet Error', path = "image_1.png"))
        ie1 = canvas.create_image(
            640.0,
            400.0,
            image=ie_image_1
        )

        ie_label_1 = Label(canvas, image = ie_image_1)
        ie_label_1.image = ie_image_1

        ie_image_2 = PhotoImage(
            file=relative_to_assets(direc = 'Internet Error', path = "image_2.png"))
        ie2 = canvas.create_image(
            639.7705078125,
            399.0361328125,
            image=ie_image_2
        )

        ie_label_2 = Label(canvas, image = ie_image_2)
        ie_label_2.image = ie_image_2

        ie_image_3 = PhotoImage(
            file=relative_to_assets(direc = 'Internet Error', path = "image_3.png"))
        ie3 = canvas.create_image(
            639.376953125,
            399.58642578125,
            image=ie_image_3
        )

        ie_label_3 = Label(canvas, image = ie_image_3)
        ie_label_3.image = ie_image_3

        ie_image_4 = PhotoImage(
            file=relative_to_assets(direc = 'Internet Error', path = "image_4.png"))
        ie4 = canvas.create_image(
            639.376953125,
            405.4169921875,
            image=ie_image_4
        )

        ie_label_4 = Label(canvas, image = ie_image_4)
        ie_label_4.image = ie_image_4

        ie_image_5 = PhotoImage(
            file=relative_to_assets(direc = 'Internet Error', path = "image_5.png"))
        ie5 = canvas.create_image(
            639.0,
            349.0,
            image=ie_image_5
        )

        ie_label_5 = Label(canvas, image = ie_image_5)
        ie_label_5.image = ie_image_5

        ie_image_6 = PhotoImage(
            file=relative_to_assets(direc = 'Internet Error', path = "image_6.png"))
        ie6 = canvas.create_image(
            639.0,
            461.6171875,
            image=ie_image_6
        )

        ie_label_6 = Label(canvas, image = ie_image_6)
        ie_label_6.image = ie_image_6

        ie_button_image_1 = PhotoImage(
            file=relative_to_assets(direc = 'Internet Error', path = "button_1.png"))
        ie_button_1 = Button(
            image=ie_button_image_1,
            highlightthickness=0,
            command=lambda: check_internet_connection(),
            relief="flat"
        )
        ie_button_1.place(
            x=730.0009765625,
            y=475.0,
            width=61,
            height=17
        )

        ie_button_label_1 = Label(canvas, image = ie_button_image_1)
        ie_button_label_1.image = ie_button_image_1


        ie7 = canvas.create_text(
            481.5009765625,
            317.5,
            anchor="nw",
            text="No connection",
            fill="#D1D3D4",
            font=("Inter", 20 * -1)
        )

        ie8 = canvas.create_text(
            482.0,
            373.0,
            anchor="nw",
            text="Please connect to an internet connection.",
            fill="#D1D3D4",
            font=("Inter", 11 * -1)
        )

        ie9 = canvas.create_text(
            482.0,
            404.0,
            anchor="nw",
            text="The app is unable to function without a connection. As",
            fill="#D1D3D4",
            font=("Inter", 11 * -1)
        )

        ie10 = canvas.create_text(
            482.0,
            420.0,
            anchor="nw",
            text="the data storage method is cloud based.",
            fill="#D1D3D4",
            font=("Inter", 11 * -1)
        )



    def check_connection():

        result = connection_check()

        if result == False:

            create_internet_error()
            raise



    ##########################################################################################################################################################################################################


      

    canvas.create_rectangle(
        0.0,
        0.0,
        1280.0,
        800.0,
        fill="#010000",
        outline="")

    canvas.create_rectangle(
        0.0,
        0.0,
        1280.0,
        99.26806640625,
        fill="#0E1012",
        outline="")


    image_image_1 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_1.png"))
    image_1 = canvas.create_image(
        758.6064453125,
        523.8638610839844,
        image=image_image_1
    )

    image_label_1 = Label(canvas, image = image_image_1)
    image_label_1.image = image_image_1

    image_image_2 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_2.png"))
    image_2 = canvas.create_image(
        383.986328125,
        716.8245239257812,
        image=image_image_2
    )

    image_label_2 = Label(canvas, image = image_image_2)
    image_label_2.image = image_image_2

    image_image_3 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_3.png"))
    image_3 = canvas.create_image(
        383.986328125,
        746.7545166015625,
        image=image_image_3
    )

    image_label_3 = Label(canvas, image = image_image_3)
    image_label_3.image = image_image_3

    image_image_4 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_4.png"))
    image_4 = canvas.create_image(
        383.986328125,
        656.9639892578125,
        image=image_image_4
    )

    image_label_4 = Label(canvas, image = image_image_4)
    image_label_4.image = image_image_4

    image_image_5 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_5.png"))
    image_5 = canvas.create_image(
        383.986328125,
        597.10400390625,
        image=image_image_5
    )

    image_label_5 = Label(canvas, image = image_image_5)
    image_label_5.image = image_image_5

    image_image_6 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_6.png"))
    image_6 = canvas.create_image(
        383.986328125,
        567.1740112304688,
        image=image_image_6
    )

    image_label_6 = Label(canvas, image = image_image_6)
    image_label_6.image = image_image_6

    image_image_7 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_7.png"))
    image_7 = canvas.create_image(
        383.986328125,
        537.2435302734375,
        image=image_image_7
    )

    image_label_7 = Label(canvas, image = image_image_7)
    image_label_7.image = image_image_7

    image_image_8 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_8.png"))
    image_8 = canvas.create_image(
        383.986328125,
        507.3135070800781,
        image=image_image_8
    )

    image_label_8 = Label(canvas, image = image_image_8)
    image_label_8.image = image_image_8

    image_image_9 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_9.png"))
    image_9 = canvas.create_image(
        383.986328125,
        627.0339965820312,
        image=image_image_9
    )

    image_label_9 = Label(canvas, image = image_image_9)
    image_label_9.image = image_image_9

    image_image_10 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_10.png"))
    image_10 = canvas.create_image(
        383.986328125,
        686.8939819335938,
        image=image_image_10
    )

    image_label_10 = Label(canvas, image = image_image_10)
    image_label_10.image = image_image_10

    image_image_11 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_11.png"))
    image_11 = canvas.create_image(
        131.7373046875,
        452.85498046875,
        image=image_image_11
    )

    image_label_11 = Label(canvas, image = image_image_11)
    image_label_11.image = image_image_11

    image_image_12 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_12.png"))
    image_12 = canvas.create_image(
        131.7373046875,
        752.8101196289062,
        image=image_image_12
    )

    image_label_12 = Label(canvas, image = image_image_12)
    image_label_12.image = image_image_12

    image_image_13 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_13.png"))
    image_13 = canvas.create_image(
        131.7373046875,
        146.541015625,
        image=image_image_13
    )

    image_label_13 = Label(canvas, image = image_image_13)
    image_label_13.image = image_image_13

    image_image_14 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_14.png"))
    image_14 = canvas.create_image(
        1066.6640625,
        389.67120361328125,
        image=image_image_14
    )

    image_label_14 = Label(canvas, image = image_image_14)
    image_label_14.image = image_image_14

    image_image_15 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_15.png"))
    image_15 = canvas.create_image(
        1066.6640625,
        711.9931030273438,
        image=image_image_15
    )

    image_label_15 = Label(canvas, image = image_image_15)
    image_label_15.image = image_image_15

    image_image_16 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_16.png"))
    image_16 = canvas.create_image(
        701.5107421875,
        549.4396057128906,
        image=image_image_16
    )

    image_label_16 = Label(canvas, image = image_image_16)
    image_label_16.image = image_image_16

    image_image_17 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_17.png"))
    image_17 = canvas.create_image(
        700.701171875,
        455.1448669433594,
        image=image_image_17
    )

    image_label_17 = Label(canvas, image = image_image_17)
    image_label_17.image = image_image_17

    image_image_18 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_18.png"))
    image_18 = canvas.create_image(
        193.7470703125,
        49.44256591796875,
        image=image_image_18
    )

    image_label_18 = Label(canvas, image = image_image_18)
    image_label_18.image = image_image_18

    image_image_19 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_19.png"))
    image_19 = canvas.create_image(
        383.9833984375,
        399.67120361328125,
        image=image_image_19
    )

    image_label_19 = Label(canvas, image = image_image_19)
    image_label_19.image = image_image_19

    image_image_20 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_20.png"))
    image_20 = canvas.create_image(
        607.474609375,
        302.47021484375,
        image=image_image_20
    )

    image_label_20 = Label(canvas, image = image_image_20)
    image_label_20.image = image_image_20

    image_image_21 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_21.png"))
    image_21 = canvas.create_image(
        383.9833984375,
        626.9024658203125,
        image=image_image_21
    )

    image_label_21 = Label(canvas, image = image_image_21)
    image_label_21.image = image_image_21

    image_image_22 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_22.png"))
    image_22 = canvas.create_image(
        337.6533203125,
        398.9997253417969,
        image=image_image_22
    )

    image_label_22 = Label(canvas, image = image_image_22)
    image_label_22.image = image_image_22

    image_image_23 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_23.png"))
    image_23 = canvas.create_image(
        339.8837890625,
        302.1947021484375,
        image=image_image_23
    )

    image_label_23 = Label(canvas, image = image_image_23)
    image_label_23.image = image_image_23

    image_image_26 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_26.png"))
    image_26 = canvas.create_image(
        557.3564453125,
        363.828857421875,
        image=image_image_26
    )

    image_label_26 = Label(canvas, image = image_image_26)
    image_label_26.image = image_image_26

    image_image_27 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_27.png"))
    image_27 = canvas.create_image(
        701.4384765625,
        666.6658935546875,
        image=image_image_27
    )

    image_label_27 = Label(canvas, image = image_image_27)
    image_label_27.image = image_image_27

    image_image_28 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_28.png"))
    image_28 = canvas.create_image(
        580.4736328125,
        577.2693481445312,
        image=image_image_28
    )

    image_label_28 = Label(canvas, image = image_image_28)
    image_label_28.image = image_image_28

    image_image_29 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_29.png"))
    image_29 = canvas.create_image(
        1066.6640625,
        557.3362121582031,
        image=image_image_29
    )

    image_label_29 = Label(canvas, image = image_image_29)
    image_label_29.image = image_image_29

    image_image_30 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_30.png"))
    image_30 = canvas.create_image(
        999.564453125,
        302.47021484375,
        image=image_image_30
    )

    image_label_30 = Label(canvas, image = image_image_30)
    image_label_30.image = image_image_30

    image_image_31 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_31.png"))
    image_31 = canvas.create_image(
        1011.564453125,
        476.1513671875,
        image=image_image_31
    )

    image_label_31 = Label(canvas, image = image_image_31)
    image_label_31.image = image_image_31

    image_image_32 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_32.png"))
    image_32 = canvas.create_image(
        941.7138671875,
        636.498291015625,
        image=image_image_32
    )

    image_label_32 = Label(canvas, image = image_image_32)
    image_label_32.image = image_image_32

    image_image_37 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_37.png"))
    image_37 = canvas.create_image(
        1080.9033203125,
        182.54107666015625,
        image=image_image_37
    )

    image_label_37 = Label(canvas, image = image_image_37)
    image_label_37.image = image_image_37

    image_image_38 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_38.png"))
    image_38 = canvas.create_image(
        574.0,
        183.5,
        image=image_image_38
    )

    image_label_38 = Label(canvas, image = image_image_38)
    image_label_38.image = image_image_38

    image_image_39 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_39.png"))
    image_39 = canvas.create_image(
        990.0,
        146.0,
        image=image_image_39
    )

    image_label_39 = Label(canvas, image = image_image_39)
    image_label_39.image = image_image_39

    image_image_40 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_40.png"))
    image_40 = canvas.create_image(
        324.7001953125,
        146.6259765625,
        image=image_image_40
    )

    image_label_40 = Label(canvas, image = image_image_40)
    image_label_40.image = image_image_40

    image_image_41 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_41.png"))
    image_41 = canvas.create_image(
        1077.1337890625,
        193.7281494140625,
        image=image_image_41
    )

    image_label_41 = Label(canvas, image = image_image_41)
    image_label_41.image = image_image_41

    image_image_42 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_42.png"))
    image_42 = canvas.create_image(
        569.662109375,
        193.8759765625,
        image=image_image_42
    )

    image_label_42 = Label(canvas, image = image_image_42)
    image_label_42.image = image_image_42

    image_image_43 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_43.png"))
    image_43 = canvas.create_image(
        130.140625,
        220.26641845703125,
        image=image_image_43
    )

    image_label_43 = Label(canvas, image = image_image_43)
    image_label_43.image = image_image_43

    canvas.create_rectangle(
        186.828125,
        218.853271484375,
        225.3447265625,
        218.853271484375,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        34.265625,
        218.8780517578125,
        72.7822265625,
        219.1959228515625,
        fill="#FFFFFF",
        outline="")

    image_image_44 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_44.png"))
    image_44 = canvas.create_image(
        131.7138671875,
        498.30712890625,
        image=image_image_44
    )

    image_label_44 = Label(canvas, image = image_image_44)
    image_label_44.image = image_image_44

    canvas.create_rectangle(
        194.1533203125,
        497.1221008300781,
        228.5224609375,
        497.1221008300781,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        34.7255859375,
        497.1931457519531,
        69.0947265625,
        497.4691467285156,
        fill="#FFFFFF",
        outline="")

    image_image_45 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_45.png"))
    image_45 = canvas.create_image(
        131.8759765625,
        132.44317626953125,
        image=image_image_45
    )

    image_label_45 = Label(canvas, image = image_image_45)
    image_label_45.image = image_image_45

    image_image_46 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_46.png"))
    image_46 = canvas.create_image(
        1144.0,
        404.0,
        image=image_image_46
    )

    image_label_46 = Label(canvas, image = image_image_46)
    image_label_46.image = image_image_46

    image_image_47 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_47.png"))
    image_47 = canvas.create_image(
        990.28125,
        350.0,
        image=image_image_47
    )

    image_label_47 = Label(canvas, image = image_image_47)
    image_label_47.image = image_image_47

    image_image_48 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_48.png"))
    image_48 = canvas.create_image(
        990.0,
        377.0,
        image=image_image_48
    )

    image_label_48 = Label(canvas, image = image_image_48)
    image_label_48.image = image_image_48

    image_image_49 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_49.png"))
    image_49 = canvas.create_image(
        990.0,
        404.0,
        image=image_image_49
    )

    image_label_49 = Label(canvas, image = image_image_49)
    image_label_49.image = image_image_49

    image_image_50 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_50.png"))
    image_50 = canvas.create_image(
        990.0,
        431.0,
        image=image_image_50
    )

    image_label_50 = Label(canvas, image = image_image_50)
    image_label_50.image = image_image_50

    image_image_51 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_51.png"))
    image_51 = canvas.create_image(
        1144.0,
        350.0,
        image=image_image_51
    )

    image_label_51 = Label(canvas, image = image_image_51)
    image_label_51.image = image_image_51

    image_image_52 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_52.png"))
    image_52 = canvas.create_image(
        1144.0,
        377.0,
        image=image_image_52
    )

    image_label_52 = Label(canvas, image = image_image_52)
    image_label_52.image = image_image_52

    image_image_53 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_53.png"))
    image_53 = canvas.create_image(
        1144.0,
        431.0,
        image=image_image_53
    )

    image_label_53 = Label(canvas, image = image_image_53)
    image_label_53.image = image_image_53

    image_image_54 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_54.png"))
    image_54 = canvas.create_image(
        1144.0,
        572.0,
        image=image_image_54
    )

    image_label_54 = Label(canvas, image = image_image_54)
    image_label_54.image = image_image_54

    image_image_55 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_55.png"))
    image_55 = canvas.create_image(
        990.28125,
        518.0,
        image=image_image_55
    )

    image_label_55 = Label(canvas, image = image_image_55)
    image_label_55.image = image_image_55

    image_image_56 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_56.png"))
    image_56 = canvas.create_image(
        990.0,
        545.0,
        image=image_image_56
    )

    image_label_56 = Label(canvas, image = image_image_56)
    image_label_56.image = image_image_56

    image_image_57 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_57.png"))
    image_57 = canvas.create_image(
        990.0,
        572.0,
        image=image_image_57
    )

    image_label_57 = Label(canvas, image = image_image_57)
    image_label_57.image = image_image_57

    image_image_58 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_58.png"))
    image_58 = canvas.create_image(
        990.0,
        599.0,
        image=image_image_58
    )

    image_label_58 = Label(canvas, image = image_image_58)
    image_label_58.image = image_image_58

    image_image_59 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_59.png"))
    image_59 = canvas.create_image(
        1144.0,
        518.0,
        image=image_image_59
    )

    image_label_59 = Label(canvas, image = image_image_59)
    image_label_59.image = image_image_59

    image_image_60 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_60.png"))
    image_60 = canvas.create_image(
        1144.0,
        545.0,
        image=image_image_60
    )

    image_label_60 = Label(canvas, image = image_image_60)
    image_label_60.image = image_image_60

    image_image_61 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "image_61.png"))
    image_61 = canvas.create_image(
        1144.0,
        599.0,
        image=image_image_61
    )

    image_label_61 = Label(canvas, image = image_image_61)
    image_label_61.image = image_image_61

    canvas.create_text(
        398,
        376.0,
        anchor="nw",
        text="You have filled",
        fill="#D1D3D4",
        font=("Inter Regular", 12 * -1)
    )


    ##########################################################################################################################################################################################################

    #red:yellow:green
    #color gradient dictionary

    cg_dict = [

        '#ff0101','#ff0502','#ff0900','#fe1401','#ff1d04',
        '#fe2a04','#ff3702','#ff4806','#ff5807','#fe6905',
        '#ff7d09','#ff8a07','#fea30b','#ffb00a','#ffbf10',
        '#ffcd10','#fdda0e','#fee60f','#fef00e','#fef810',
        '#fffb13','#fffe12','#ffff13','#ffff13','#ffff13',
        '#ffff13','#ffff13','#fefe12','#fcfd11','#f7f910',
        '#f0f511','#e5ef10','#dae810','#cddf10','#c0d50a',
        '#b0ca0b','#9fbf0c','#8ab107','#7aa609','#6a9c05',
        '#589105','#458304','#397b03','#297002','#1f6800',
        '#156201','#0b5d02','#045800','#015500','#005502',
        
        ]


    def progress_bar(percent: int, x_cord: int, y_cord: int):

        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={'projection':'polar'})
        data = percent

        startangle = 90
        x = (-data * pi *2)/ 100
        left = (startangle * pi *2)/ 360 #this is to control where the bar starts
        ys = 2.2


        #finding colour for circular bad
        col_index = round((percent / 2) + 0.1)
        colors = cg_dict[col_index - 1]

        if odd_initial == True:
            fig.set_size_inches(1.2, 1.2)
        elif odd_initial == False:
            fig.set_size_inches(0.6, 0.6)
        plt.xticks([])
        plt.yticks([])
        fig.patch.set_facecolor('#0E1012')
        
        ax.spines.clear()
        
        if percent != 0:
            if percent > 60:
                ax.scatter(x+left, ys+0.02, s=0.9, color=colors, zorder=2)
            elif 40 < percent < 60:
                ax.scatter(x+left, ys-0.085, s=0.9, color=colors, zorder=2)
            elif percent < 40:
                ax.scatter(x+left, ys-0.085, s=0.9, color=colors, zorder=2)
                
            ax.scatter(left, ys+0.02744, s=0.9, color=colors, zorder=2)
        
        ax.patch.set_facecolor('#0E1012')
        
        ax.barh(ys, (-100 * pi *2)/ 100, left=left, height=0.9, color='#58595b')
        ax.barh(ys, x, left=left, height=0.9, color=colors)

        plt.ylim(-4, 3)

        if odd_initial == True:
            plt.text(0, -3, f"{data}%  ", ha='center', va='center', fontsize=12, color='white')
        elif odd_initial == False:
            plt.text(0, -3, f"{data}%  ", ha='center', va='center', fontsize=6, color='white')

        canva = FigureCanvasTkAgg(fig, master = window)
        canva.draw()

        global chart7, of_the
        try:
            chart7
        except NameError:
            pass
        else:
            chart7.destroy()
            canvas.itemconfig(of_the, state = 'hidden')
            
        #change_text
        of_the = canvas.create_text(
            398,
            394.0,
            anchor="nw",
            text=f"{percent}% of the",
            fill="#D1D3D4",
            font=("Inter Regular", 12 * -1)
        )
        
        chart7 = canva.get_tk_widget()
        chart7.place(x=x_cord, y=y_cord)
        

    def destroy_progress_bar():
        try:
            chart7
        except NameError:
            pass
        else:
            chart7.destroy()


    canvas.create_text(
        398,
        412.0,
        anchor="nw",
        text="orders.",
        fill="#D1D3D4",
        font=("Inter Regular", 12 * -1)
    )

    ##########################################################################################################################################################################################################

    ##########################################################################################################################################################################################################

    #Products Ordered list

    def sort_product_ordered_list(data: dict):

        if data['orders_req_cancellation'] != {}:
            
            dicta = []
                
            dictb = data['orders_req_cancellation'][data['event'][0]].copy()

            for i in dictb['special_occasion']:
                value = dictb['special_occasion'][i]
                dictb[i] = value
            
            del dictb['special_occasion']
            
            dicta = [[k, v] for k, v in sorted(dictb.items(), key=lambda item: item[1], reverse = True)]
            if len(dicta) > 8:
                for i in range(len(dicta) - 8):
                    del dicta[-1]

            if len(dicta) < 8:
                for i in range(8 - len(dicta)):
                    dicta.append(('', ''))

        else:

            dicta = []
            for i in range(8):
                dicta.append(('', ''))

        return dicta



    def sort_product_in_reserve_list(data: dict):

        if data['product_pending'] != {}:

            dicta = []
                
            dictb = data['product_pending'].copy()

            for i in dictb['special_occasion']:
                value = dictb['special_occasion'][i]
                dictb[i] = value
            
            del dictb['special_occasion']
            
            dicta = [[k, v] for k, v in sorted(dictb.items(), key=lambda item: item[1], reverse = True)]
            if len(dicta) > 8:
                for i in range(len(dicta) - 8):
                    del dicta[-1]

            if len(dicta) < 8:
                for i in range(8 - len(dicta)):
                    dicta.append(('', ''))

        else:

            dicta = []
            for i in range(8):
                dicta.append(('', ''))
                
        return dicta


    def sort_orders_to_fill(data: dict):

        if data['orders_tofill'] != {}:

            dicta = []

            dictb = data['orders_tofill'][data['event'][0]].copy()

            for i in dictb['special_occasion']:
                value = dictb['special_occasion'][i]
                dictb[i] = value

            del dictb['special_occasion']

            dicta = [[k, v] for k, v in sorted(dictb.items(), key=lambda item: item[1], reverse = True)]
            if len(dicta) > 9:
                for i in range(len(dicta) - 9):
                    del dicta[-1]

            if len(dicta) < 9:
                for i in range(9 - len(dicta)):
                    dicta.append(('', ''))

        else:

            dicta = []
            for i in range(9):
                dicta.append(('', ''))
                
        return dicta


    def calculate_bar_percentage(data: dict):

        #amount of product ordered
        sum_ordered = 0

        if data['orders_req_cancellation'] != {}:
            
            ordered_b = data['orders_req_cancellation'][data['event'][0]].copy()

            for i in ordered_b['special_occasion']:
                value = ordered_b['special_occasion'][i]
                ordered_b[i] = value

            del ordered_b['special_occasion']

            ordered = [[k, v] for k, v in sorted(ordered_b.items(), key=lambda item: item[1], reverse = True)]

            name_list = []
            for i in range(len(ordered)):
                name_list.append(ordered[i][0])

            temp_list = ordered.copy()
            for i in range(len(ordered)):
                sum_ordered += ordered[i][1]
            
                
            #amount of product required to be filled
            sum_filled = 0
            
            to_fill_b = data['orders_tofill'][data['event'][0]].copy()

            for i in to_fill_b['special_occasion']:
                value = to_fill_b['special_occasion'][i]
                to_fill_b[i] = value
            
            del to_fill_b['special_occasion']
            
            to_fill = [[k, v] for k, v in sorted(to_fill_b.items(), key=lambda item: item[1], reverse = True)]
            
            for i in range(len(to_fill)):
                if to_fill[i][0] not in name_list or to_fill[i][0] == 0:
                    del to_fill[i]

            for i in range(len(to_fill)):
                temp_list[i][1] = temp_list[i][1] - to_fill[i][1]

            for i in range(len(temp_list)):
                sum_filled += temp_list[i][1]
                
            #temp_list is list for products filled
            #ordered is usual

            #calculate percentage
            percentage = 0
            if sum_ordered != 0:
                percentage = int(round((sum_filled/sum_ordered)*100, 0))

        else:

            percentage = 0

        return percentage

    calculate_bar_percentage(data = data)
    refresh_reset = False

    def delete_orders_list():

        canvas.delete(por1)
        canvas.delete(por2)
        canvas.delete(por3)
        canvas.delete(por4)
        canvas.delete(por5)
        canvas.delete(por6)
        canvas.delete(por7)
        canvas.delete(por8)
        canvas.delete(por9)
        canvas.delete(por10)

        canvas.delete(por11)
        canvas.delete(por12)
        canvas.delete(por13)
        canvas.delete(por14)
        canvas.delete(por15)
        canvas.delete(por16)


        canvas.delete(pir1)
        canvas.delete(pir2)
        canvas.delete(pir3)
        canvas.delete(pir4)
        canvas.delete(pir5)
        canvas.delete(pir6)
        canvas.delete(pir7)
        canvas.delete(pir8)
        canvas.delete(pir9)
        canvas.delete(pir10)

        canvas.delete(pir11)
        canvas.delete(pir12)
        canvas.delete(pir13)
        canvas.delete(pir14)
        canvas.delete(pir15)
        canvas.delete(pir16)


        canvas.delete(otf1)
        canvas.delete(otf2)
        canvas.delete(otf3)
        canvas.delete(otf4)
        canvas.delete(otf5)
        canvas.delete(otf6)
        canvas.delete(otf7)
        canvas.delete(otf8)
        canvas.delete(otf9)
        canvas.delete(otf10)

        canvas.delete(otf11)
        canvas.delete(otf12)
        canvas.delete(otf13)
        canvas.delete(otf14)
        canvas.delete(otf15)
        canvas.delete(otf16)
        canvas.delete(otf17)
        canvas.delete(otf18)

        


    def refresh_orders():


        if refresh_reset == True:
            delete_orders_list()

        refresh_rest = True
        ro_cord_left = [1051, 1046, 1041]
        ro_cord_right = [1204, 1199, 1194]


        po_list = sort_product_ordered_list(data = data)

        #products ordered list

        global por1
        global por2
        global por3
        global por4
        global por5
        global por6
        global por7
        global por8
        global por9
        global por10

        global por11
        global por12
        global por13
        global por14
        global por15
        global por16

        try:
            por1
        except NameError:
            por_exists = False
        else:
            por_exists = True


        if por_exists == False:
            por1 = canvas.create_text(
                923.0,
                344.0,
                anchor="nw",
                text=po_list[0][0],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            por2 = canvas.create_text(
                ro_cord_left[len(str(po_list[0][1]))-1],
                344.0,
                anchor="nw",
                text=po_list[0][1],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            por3 = canvas.create_text(
                1076.0,
                344.0,
                anchor="nw",
                text=po_list[1][0],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            por4 = canvas.create_text(
                ro_cord_right[len(str(po_list[1][1]))-1],
                344.0,
                anchor="nw",
                text=po_list[1][1],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            por5 = canvas.create_text(
                923.0,
                371.0,
                anchor="nw",
                text=po_list[2][0],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            por6 = canvas.create_text(
                ro_cord_left[len(str(po_list[2][1]))-1],
                371.0,
                anchor="nw",
                text=po_list[2][1],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            por7 = canvas.create_text(
                1076.0,
                371.0,
                anchor="nw",
                text=po_list[3][0],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            por8 = canvas.create_text(
                ro_cord_right[len(str(po_list[3][1]))-1],
                371.0,
                anchor="nw",
                text=po_list[3][1],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            por9 = canvas.create_text(
                923.0,
                398.0,
                anchor="nw",
                text=po_list[4][0],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            por10 = canvas.create_text(
                ro_cord_left[len(str(po_list[4][1]))-1],
                398.0,
                anchor="nw",
                text=po_list[4][1],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            por11 = canvas.create_text(
                1076.0,
                398.0,
                anchor="nw",
                text=po_list[5][0],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            por12 = canvas.create_text(
                ro_cord_right[len(str(po_list[5][1]))-1],
                398.0,
                anchor="nw",
                text=po_list[5][1],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            por13 = canvas.create_text(
                923.0,
                425.0,
                anchor="nw",
                text=po_list[6][0],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            por14 = canvas.create_text(
                ro_cord_left[len(str(po_list[6][1]))-1],
                426.0,
                anchor="nw",
                text=po_list[6][1],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            por15 = canvas.create_text(
                1076.0,
                425.0,
                anchor="nw",
                text=po_list[7][0],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            por16 = canvas.create_text(
                ro_cord_right[len(str(po_list[7][1]))-1],
                426.0,
                anchor="nw",
                text=po_list[7][1],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

        elif por_exists == True:

            canvas.itemconfig(por1,  text = po_list[0][0])
            canvas.itemconfig(por2,  text = po_list[0][1])
            canvas.itemconfig(por3,  text = po_list[1][0])
            canvas.itemconfig(por4,  text = po_list[1][1])
            canvas.itemconfig(por5,  text = po_list[2][0])
            canvas.itemconfig(por6,  text = po_list[2][1])
            canvas.itemconfig(por7,  text = po_list[3][0])
            canvas.itemconfig(por8,  text = po_list[3][1])
            canvas.itemconfig(por9,  text = po_list[4][0])
            canvas.itemconfig(por10, text = po_list[4][1])
            canvas.itemconfig(por11, text = po_list[5][0])
            canvas.itemconfig(por12, text = po_list[5][1])
            canvas.itemconfig(por13, text = po_list[6][0])
            canvas.itemconfig(por14, text = po_list[6][1])
            canvas.itemconfig(por15, text = po_list[7][0])
            canvas.itemconfig(por16, text = po_list[7][1])
            

        pir_list = sort_product_in_reserve_list(data = data)

        #products in reserve list

        global pir1
        global pir2
        global pir3
        global pir4
        global pir5
        global pir6
        global pir7
        global pir8
        global pir9
        global pir10
        
        global pir11
        global pir12
        global pir13
        global pir14
        global pir15
        global pir16

        try:
            pir1
        except NameError:
            pir_exists = False
        else:
            pir_exists = True

        if pir_exists == False:
            
            pir1 = canvas.create_text(
                923.0,
                512.0,
                anchor="nw",
                text=pir_list[0][0],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            pir2 = canvas.create_text(
                ro_cord_left[len(str(pir_list[0][1]))-1],
                512.0,
                anchor="nw",
                text=pir_list[0][1],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            pir3 = canvas.create_text(
                1076.0,
                512.0,
                anchor="nw",
                text=pir_list[1][0],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            pir4 = canvas.create_text(
                ro_cord_right[len(str(pir_list[1][1]))-1],
                512.0,
                anchor="nw",
                text=pir_list[1][1],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            pir5 = canvas.create_text(
                923.0,
                539.0,
                anchor="nw",
                text=pir_list[2][0],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            pir6 = canvas.create_text(
                ro_cord_left[len(str(pir_list[2][1]))-1],
                539.0,
                anchor="nw",
                text=pir_list[2][1],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            pir7 = canvas.create_text(
                1076.0,
                539.0,
                anchor="nw",
                text=pir_list[3][0],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            pir8 = canvas.create_text(
                ro_cord_right[len(str(pir_list[3][1]))-1],
                539.0,
                anchor="nw",
                text=pir_list[3][1],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            pir9 = canvas.create_text(
                923.0,
                566.0,
                anchor="nw",
                text=pir_list[4][0],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            pir10 = canvas.create_text(
                ro_cord_left[len(str(pir_list[4][1]))-1],
                566.0,
                anchor="nw",
                text=pir_list[4][1],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            pir11 = canvas.create_text(
                1076.0,
                566.0,
                anchor="nw",
                text=pir_list[5][0],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            pir12 = canvas.create_text(
                ro_cord_right[len(str(pir_list[5][1]))-1],
                566.0,
                anchor="nw",
                text=pir_list[5][1],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            pir13 = canvas.create_text(
                923.0,
                593.0,
                anchor="nw",
                text=pir_list[6][0],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            pir14 = canvas.create_text(
                ro_cord_left[len(str(pir_list[6][1]))-1],
                594.0,
                anchor="nw",
                text=pir_list[6][1],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            pir15 = canvas.create_text(
                1076.0,
                593.0,
                anchor="nw",
                text=pir_list[7][0],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            pir16 = canvas.create_text(
                ro_cord_right[len(str(pir_list[7][1]))-1],
                594.0,
                anchor="nw",
                text=pir_list[7][1],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

        elif pir_exists == True:

            canvas.itemconfig(pir1,  text = pir_list[0][0])
            canvas.itemconfig(pir2,  text = pir_list[0][1])
            canvas.itemconfig(pir3,  text = pir_list[1][0])
            canvas.itemconfig(pir4,  text = pir_list[1][1])
            canvas.itemconfig(pir5,  text = pir_list[2][0])
            canvas.itemconfig(pir6,  text = pir_list[2][1])
            canvas.itemconfig(pir7,  text = pir_list[3][0])
            canvas.itemconfig(pir8,  text = pir_list[3][1])
            canvas.itemconfig(pir9,  text = pir_list[4][0])
            canvas.itemconfig(pir10, text = pir_list[4][1])
            canvas.itemconfig(pir11, text = pir_list[5][0])
            canvas.itemconfig(pir12, text = pir_list[5][1])
            canvas.itemconfig(pir13, text = pir_list[6][0])
            canvas.itemconfig(pir14, text = pir_list[6][1])
            canvas.itemconfig(pir15, text = pir_list[7][0])
            canvas.itemconfig(pir16, text = pir_list[7][1])
                
        otf_list = sort_orders_to_fill(data = data)

        #orders to fill list

        global otf1
        global otf2
        global otf3
        global otf4
        global otf5
        global otf6
        global otf7
        global otf8
        global otf9
        global otf10

        global otf11
        global otf12
        global otf13
        global otf14
        global otf15
        global otf16
        global otf17
        global otf18

        otf_cord_list = [469, 464, 459]

        try:
            otf1
        except NameError:
            otf_exists = False
        else:
            otf_exists = True


        if otf_exists == False:
            
            otf1 = canvas.create_text(
                294.0,
                501.0,
                anchor="nw",
                text=otf_list[0][0],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            otf2 = canvas.create_text(
                otf_cord_list[len(str(otf_list[0][1]))-1],
                501.0,
                anchor="nw",
                text=otf_list[0][1],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            otf3 = canvas.create_text(
                294.0,
                531.0,
                anchor="nw",
                text=otf_list[1][0],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            otf4 = canvas.create_text(
                otf_cord_list[len(str(otf_list[1][1]))-1],
                531.0,
                anchor="nw",
                text=otf_list[1][1],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            otf5 = canvas.create_text(
                294.0,
                561.0,
                anchor="nw",
                text=otf_list[2][0],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            otf6 = canvas.create_text(
                otf_cord_list[len(str(otf_list[2][1]))-1],
                561.0,
                anchor="nw",
                text=otf_list[2][1],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            otf7 = canvas.create_text(
                294.0,
                592.4139404296875,
                anchor="nw",
                text=otf_list[3][0],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            otf8 = canvas.create_text(
                otf_cord_list[len(str(otf_list[3][1]))-1],
                591.0,
                anchor="nw",
                text=otf_list[3][1],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            otf9 = canvas.create_text(
                294.0,
                621.0,
                anchor="nw",
                text=otf_list[4][0],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            otf10 = canvas.create_text(
                otf_cord_list[len(str(otf_list[4][1]))-1],
                621.0,
                anchor="nw",
                text=otf_list[4][1],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            otf11 = canvas.create_text(
                294.0,
                651.0,
                anchor="nw",
                text=otf_list[5][0],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            otf12 = canvas.create_text(
                otf_cord_list[len(str(otf_list[5][1]))-1],
                651.0,
                anchor="nw",
                text=otf_list[5][1],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            otf13 = canvas.create_text(
                294.0,
                680.5,
                anchor="nw",
                text=otf_list[6][0],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            otf14 = canvas.create_text(
                otf_cord_list[len(str(otf_list[6][1]))-1],
                680.5,
                anchor="nw",
                text=otf_list[6][1],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            otf15 = canvas.create_text(
                294.0,
                710.50048828125,
                anchor="nw",
                text=otf_list[7][0],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            otf16 = canvas.create_text(
                otf_cord_list[len(str(otf_list[7][1]))-1],
                710.5,
                anchor="nw",
                text=otf_list[7][1],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            otf17 = canvas.create_text(
                294.0,
                740.5,
                anchor="nw",
                text=otf_list[8][0],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

            otf18 = canvas.create_text(
                otf_cord_list[len(str(otf_list[8][1]))-1],
                740.5,
                anchor="nw",
                text=otf_list[8][1],
                fill="#D1D3D4",
                font=("Inter", 10 * -1)
            )

        elif otf_exists == True:

            canvas.itemconfig(otf1,  text = otf_list[0][0])
            canvas.itemconfig(otf2,  text = otf_list[0][1])
            canvas.itemconfig(otf3,  text = otf_list[1][0])
            canvas.itemconfig(otf4,  text = otf_list[1][1])
            canvas.itemconfig(otf5,  text = otf_list[2][0])
            canvas.itemconfig(otf6,  text = otf_list[2][1])
            canvas.itemconfig(otf7,  text = otf_list[3][0])
            canvas.itemconfig(otf8,  text = otf_list[3][1])
            canvas.itemconfig(otf9,  text = otf_list[4][0])
            canvas.itemconfig(otf10, text = otf_list[4][1])
            canvas.itemconfig(otf11, text = otf_list[5][0])
            canvas.itemconfig(otf12, text = otf_list[5][1])
            canvas.itemconfig(otf13, text = otf_list[6][0])
            canvas.itemconfig(otf14, text = otf_list[6][1])
            canvas.itemconfig(otf15, text = otf_list[7][0])
            canvas.itemconfig(otf16, text = otf_list[7][1])
            canvas.itemconfig(otf17, text = otf_list[8][0])
            canvas.itemconfig(otf18, text = otf_list[8][1])
            

        #setting orders to fill circular progress bar
        bar_percent = calculate_bar_percentage(data = data)
        progress_bar(percent = bar_percent, x_cord = 278, y_cord = 339)
        


    ##########################################################################################################################################################################################################

    main_data_yo = 'year'

    def refresh_main_data(data: dict, year_over: str):

        if year_over == 'year':
            
            revenue_value = "RM " + str(int(data['main_data']['revenue_YD']))
            profit_value = "RM " + str(int(data['main_data']['profit_YD']))
            cost_value = "RM "+ str(int(data['main_data']['cost_YD']))
            time_spent_value = "{} Hours {} Minutes".format(data['main_data']['time_spent_YD']['hour'], data['main_data']['time_spent_YD']['minute'])

        elif year_over == 'over':

            revenue_value = "RM " + str(int(data['main_data']['revenue']))
            profit_value = "RM " + str(int(data['main_data']['profit']))
            cost_value = "RM " + str(int(data['main_data']['cost']))
            time_spent_value = "{} Hours {} Minutes".format(data['main_data']['time_spent']['hour'], data['main_data']['time_spent']['minute'])

        if len(time_spent_value) > 18:
            time_spent_value = time_spent_value[0:16] + '...'

        canvas.itemconfig(rev1, text=revenue_value)
        canvas.itemconfig(pro1, text=profit_value)
        canvas.itemconfig(cos1, text=cost_value)
        canvas.itemconfig(ts1, text=time_spent_value)

        global main_data_yo
        main_data_yo = year_over

        
    upcoming_event = canvas.create_text(
        110.0, #110 for None
        146.0,
        anchor="nw",
        text="None",
        fill="#FFFFFF",
        font=("Inter", 18 * -1)
    )

    canvas.create_text(
        279.5,
        172.5,
        anchor="nw",
        text="Revenue",
        fill="#D1D3D4",
        font=("Inter Regular", 16 * -1)
    )

    rev1 = canvas.create_text(
        279.5,
        196.76800537109375,
        anchor="nw",
        text="RM 2 233",
        fill="#D1D3D4",
        font=("Inter Regular", 16 * -1)
    )

    canvas.create_text(
        431.0224609375,
        172.5,
        anchor="nw",
        text="Profit",
        fill="#D1D3D4",
        font=("Inter Regular", 16 * -1)
    )

    pro1 = canvas.create_text(
        431.0224609375,
        196.76800537109375,
        anchor="nw",
        text="RM 221",
        fill="#D1D3D4",
        font=("Inter Regular", 16 * -1)
    )

    canvas.create_text(
        579.4482421875,
        172.5,
        anchor="nw",
        text="Cost",
        fill="#D1D3D4",
        font=("Inter Regular", 16 * -1)
    )

    cos1 = canvas.create_text(
        579.44921875,
        196.76800537109375,
        anchor="nw",
        text="RM 2 012",
        fill="#D1D3D4",
        font=("Inter Regular", 16 * -1)
    )

    canvas.create_text(
        730.091796875,
        172.5,
        anchor="nw",
        text="Time spent",
        fill="#D1D3D4",
        font=("Inter Regular", 16 * -1)
    )

    ts1 = canvas.create_text(
        729.88671875,
        196.76800537109375,
        anchor="nw",
        text="6 Hours 7 Minutes",
        fill="#D1D3D4",
        font=("Inter Regular", 16 * -1)
    )


    def refresh_events(data: dict):

        if data['event'] != []:
            due_date_val = data['event'][0]
            event_name_val = data['event_name'][due_date_val]

            #check length of event name
            if len(event_name_val) > 19:
                event_name_val = event_name_val[0:14] + "..."

            today = dt.date.today()
            date_string = due_date_val + "/{}".format(today.year)
            future = dt.datetime.strptime(date_string, "%m/%d/%Y").date()
            diff = future - today

            days_pending_val = f"In {diff.days} days"

            date_event = future.strftime("%d/%m/%Y")

            #to find the x_cord for "In {diff.days} days"
            coords_d_pending = [1192 ,1187, 1182, 1177]
            x_coordinate = coords_d_pending[len(str(diff.days)) - 1]


        else:
            event_name_val = "None"
            date_event = "None"
            days_pending_val = "In -- days"
            x_coordinate = 1187

        canvas.itemconfig(event_name, text=event_name_val)
        canvas.itemconfig(due_date, text=date_event)
        canvas.itemconfig(days_pending, text=days_pending_val)
        canvas.coords(days_pending, x_coordinate, 226.5)

        if len(data['event']) == 1 or len(data['event']) == 0:        
            canvas.itemconfig(upcoming_event, text = 'None')
        else:
            upcoming_name = data['event_name'][data['event'][1]]
            if len(upcoming_name) > 16:
                upcoming_name = upcoming_name[0:16] + "..."
            canvas.itemconfig(upcoming_event, text=upcoming_name)
            x_cords = 110 - (len(upcoming_name) - 5) * 4.5              
            canvas.coords(upcoming_event, x_cords, 146.0)



    def account_status(data: dict):

        account_name = token['id_token']['email']
        if len(account_name) == 0:
            account_name = "None"
        elif len(account_name) > 24:
            account_name = account_name[0:22]
            account_name += "..."
        canvas.itemconfig(email, text=account_name)    
        x_cords = 126 - (len(account_name) - 1) * 3.75
        canvas.coords(email, x_cords, 744.0)


    def refresh_event_order():

        #does base checking from data['event']
        sorted_list = data['event'].copy()
        sorted_list.sort()

        copied_otf  = data['orders_tofill'].copy()
        copied_orc  = data['orders_req_cancellation'].copy()
        copied_morc = data['manual_orders_req_cancellation'].copy()
        copied_ena  = data['event_name'].copy()
        copied_fid  = data['form_id'].copy()

        data['event'] = sorted_list
        data['orders_tofill'] = {}
        data['orders_req_cancellation'] = {}
        data['manual_orders_req_cancellation'] = {}
        data['event_name'] = {}
        data['form_id'] = {}

        for i in sorted_list:
            data['orders_tofill'][i] = copied_otf[i]
            data['orders_req_cancellation'][i] = copied_orc[i]
            data['manual_orders_req_cancellation'][i] = copied_morc[i]
            data['event_name'][i] = copied_ena[i]
            data['form_id'][i] = copied_fid[i]

            

        

    canvas.create_text(
        935.228515625,
        174.0,
        anchor="nw",
        text="Event Name               ",
        fill="#D1D3D4",
        font=("Inter", 16 * -1)
    )

    canvas.create_text(
        935.0,
        195.7764892578125,
        anchor="nw",
        text="Due Date                     ",
        fill="#D1D3D4",
        font=("Inter", 16 * -1)
    )

    event_name = canvas.create_text(
        1085.5,
        174.0,
        anchor="nw",
        text="Summer Bakesale",
        fill="#D1D3D4",
        font=("Inter", 16 * -1)
    )

    due_date = canvas.create_text(
        1085.5,
        195.7769775390625,
        anchor="nw",
        text="14/05/2022",
        fill="#D1D3D4",
        font=("Inter", 16 * -1)
    )

    days_pending = canvas.create_text(
        1182.0,
        226.5,
        anchor="nw",
        text="In 21 days",
        fill="#FFFFFF",
        font=("Inter", 8 * -1)
    )

    email = canvas.create_text(
        58.5,
        744.0,
        anchor="nw",
        text="shng2025@gmail.com",
        fill="#FFFFFF",
        font=("Inter", 14 * -1)
    )

    with open("token.json", "r") as datafile:
        token = json.load(datafile)
        

    #by default the "Main Data" table is set to 'Y/D'
    def refresh_data():
        refresh_main_data(data = data, year_over = main_data_yo)
        account_status(data = token)
        refresh_orders()
        refresh_events(data = data)

    refresh_data()


    ##########################################################################################################################################################################################################


    def create_chart(chart_type: str, year_over: str , data: dict, x_cord: int, y_cord: int, dashboard = True):

        datea = []
        revenuea = []
        costa = []
        profita = []
        timespenta = []

        current_date = dt.datetime.now().strftime('%Y/%m/%d')
        index_checker = 0

        for i in range(len(data['YD_calendar'])):

            datee = list(data['YD_calendar'])[i]

            if datee == current_date:
                index_checker = i

            
        for i in data['YD_calendar']:
            
            current_index = list(data['YD_calendar']).index(i)
            datea.append(dt.datetime.strptime(i, '%Y/%m/%d'))

            if current_index <= index_checker:
                revenue_num = data['YD_calendar'][i]['revenue']
                cost_num = data['YD_calendar'][i]['cost']
                profit_num = data['YD_calendar'][i]['profit']

                timespent_min = data['YD_calendar'][i]['time_spent']['minute']
                timespent_hour = data['YD_calendar'][i]['time_spent']['hour']
                timespent_comp = timespent_hour + (timespent_min / 60)
                
                revenuea.append(revenue_num)
                costa.append(cost_num)
                profita.append(profit_num)
                timespenta.append(timespent_comp)
                
            else:
                
                revenuea.append(None)
                costa.append(None)
                profita.append(None)
                timespenta.append(None)
                

        if year_over == 'over':

            revenueo = data['main_data']['revenue']
            costo = data['main_data']['cost']
            profito = data['main_data']['profit']

            timespento_min = data['main_data']['time_spent']['minute']
            timespento_hour = data['main_data']['time_spent']['hour']
            timespento = timespento_hour + (timespento_min / 60)
            
            tester = []
            final_value = 0

            for i in range(len(revenuea)):
                if revenuea[i] != None:
                    tester.append(revenuea[i])

            final_value = len(tester) - 1

            revenue_diff = revenueo - revenuea[final_value]
            cost_diff = costo - costa[final_value]
            profit_diff = profito - profita[final_value]
            timespent_diff = timespento - timespenta[final_value]

            for i in range(len(revenuea)):
                
                if revenuea[i] != None:
                    revenuea[i] = revenuea[i] + revenue_diff
                    costa[i] = costa[i] + cost_diff
                    profita[i] = profita[i] + profit_diff
                    timespenta[i] = timespenta[i] + timespent_diff

        if odd_initial == True:           
            plt.rcParams.update({'font.size': 4})
        elif odd_initial == False:
            plt.rcParams.update({'font.size': 2})

        if chart_type == 'revenue':

            fig, ax1 = plt.subplots()
            if odd_initial == True:           
                fig.set_size_inches(3.2, 1.4)
                ax1.plot(datea, revenuea, color = '#d0d3d4', linewidth=1.2)
            elif odd_initial == False:
                fig.set_size_inches(1.6, 0.7)
                ax1.plot(datea, revenuea, color = '#d0d3d4', linewidth=0.6)
            ax1.axes.xaxis.set_visible(False)
            #fig.autofmt_xdate()

        elif chart_type == 'cost':

            fig, ax1 = plt.subplots()
            if odd_initial == True:           
                fig.set_size_inches(3.2, 1.4)
                ax1.plot(datea, revenuea, color = '#d0d3d4', linewidth=1.2)
            elif odd_initial == False:
                fig.set_size_inches(1.6, 0.7)
            ax1.plot(datea, costa, color = '#d0d3d4', linewidth=0.6)
            ax1.axes.xaxis.set_visible(False)
            #fig.autofmt_xdate()

        elif chart_type == 'profit':

            fig, ax1 = plt.subplots()
            if odd_initial == True:           
                fig.set_size_inches(3.2, 1.4)
                ax1.plot(datea, revenuea, color = '#d0d3d4', linewidth=1.2)
            elif odd_initial == False:
                fig.set_size_inches(1.6, 0.7)
            ax1.plot(datea, profita, color = '#d0d3d4', linewidth=0.6)
            ax1.axes.xaxis.set_visible(False)
            #fig.autofmt_xdate()

        elif chart_type == 'timespent':

            fig, ax1 = plt.subplots()
            if odd_initial == True:           
                fig.set_size_inches(3.2, 1.4)
                ax1.plot(datea, revenuea, color = '#d0d3d4', linewidth=1.2)
            elif odd_initial == False:
                fig.set_size_inches(1.6, 0.7)
            ax1.plot(datea, timespenta, color = '#d0d3d4', linewidth=0.6)
            ax1.axes.xaxis.set_visible(False)
            #fig.autofmt_xdate()

        if dashboard == True:
            fig.patch.set_facecolor('#0E1012')
            ax1.patch.set_facecolor('#0E1012')
        elif dashboard == False:
            fig.patch.set_facecolor('#171819')
            ax1.patch.set_facecolor('#171819')

        ax1.spines.right.set_visible(False)
        ax1.spines.top.set_visible(False)
        #ax1.xaxis.set_visible(False)
        #ax1.yaxis.set_visible(False)
        
        ax1.spines['bottom'].set_color('#d0d3d4')
        ax1.spines['left'].set_color('#d0d3d4')
        if odd_initial == True:
            ax1.spines['bottom'].set_linewidth(0.8)
            ax1.spines['left'].set_linewidth(0.8)
            ax1.tick_params(axis='x', colors='#d0d3d4', width=0.8)
            ax1.tick_params(axis='y', colors='#d0d3d4', width=0.8)
        elif odd_initial == False:
            ax1.spines['bottom'].set_linewidth(0.4)
            ax1.spines['left'].set_linewidth(0.4)
            ax1.tick_params(axis='x', colors='#d0d3d4', width=0.4)
            ax1.tick_params(axis='y', colors='#d0d3d4', width=0.4)
        

        canvas = FigureCanvasTkAgg(fig, master = window)
        canvas.draw()

        if chart_type == 'revenue':

            global chart_revenue
            try:
                chart_revenue
            except NameError:
                pass
            else:
                chart_revenue.destroy()
            
            chart_revenue = canvas.get_tk_widget()
            chart_revenue.place(x=x_cord, y=y_cord)

        elif chart_type == 'cost':

            global chart_cost
            try:
                chart_cost
            except NameError:
                pass
            else:
                chart_cost.destroy()
            
            chart_cost = canvas.get_tk_widget()
            chart_cost.place(x=x_cord, y=y_cord)

        elif chart_type == 'profit':

            global chart_profit
            try:
                chart_profit
            except NameError:
                pass
            else:
                chart_profit.destroy()
            
            chart_profit = canvas.get_tk_widget()
            chart_profit.place(x=x_cord, y=y_cord)

        elif chart_type == 'timespent':

            global chart_timespent
            try:
                chart_timespent
            except NameError:
                pass
            else:
                chart_timespent.destroy()
            
            chart_timespent = canvas.get_tk_widget()
            chart_timespent.place(x=x_cord, y=y_cord)
            

    def destroy_dashboard_charts():

        global chart_timespent
        try:
            chart_timespent
        except NameError:
            pass
        else:
            chart_timespent.destroy()

        global chart_profit
        try:
            chart_profit
        except NameError:
            pass
        else:
            chart_profit.destroy()

        plt.close('all')

            
    def destroy_display_charts():

        global chart_timespent
        try:
            chart_timespent
        except NameError:
            pass
        else:
            chart_timespent.destroy()

        global chart_profit
        try:
            chart_profit
        except NameError:
            pass
        else:
            chart_profit.destroy()

        global chart_cost
        try:
            chart_cost
        except NameError:
            pass
        else:
            chart_cost.destroy()

        global chart_revenue
        try:
            chart_revenue
        except NameError:
            pass
        else:
            chart_revenue.destroy()

        plt.close('all')

        
    create_chart(chart_type = 'timespent', year_over = 'year', data = data, x_cord = 540, y_cord = 597)
    create_chart(chart_type = 'profit', year_over = 'year', data = data, x_cord = 540, y_cord = 385)


    call_error_list = []


    def create_status_nodes():

        #hide green node if exist
        try:
            image_33
        except NameError:
            pass
        else:
            canvas.itemconfig(image_33, state = 'hidden')
            canvas.itemconfig(image_34, state = 'hidden')
            canvas.itemconfig(status_text_1, state = 'hidden')
            

        #create red nodes
        if len(call_error_list) <= 4:
            lena = len(call_error_list)
        else:
            lena = 4

        if lena > 0:
        
            for i in range(lena):
                
                text_y_cord = 746 - (27 * i)
                node_y_cord = 751 - (27 * i)

                status_text_x_cord = 949.9
                status_node_x_cord = 932.5
                status_gray_x_cord = 1066.5

                #gray box
                sn_image = PhotoImage(
                    file=relative_to_assets(direc = 'dashboard', path = 'image_33.png'))
                exec(f"sn_image_gray_{i} = canvas.create_image({status_gray_x_cord}, {node_y_cord}, image = sn_image)")
                exec(f"sn_label_gray_{i} = Label(canvas, image = sn_image)")
                exec(f"sn_label_gray_{i}.image = sn_image")

                #red node
                sn_red_node = PhotoImage(
                    file=relative_to_assets(direc = 'dashboard', path = "image_36.png"))
                exec(f"sn_image_node_{i} = canvas.create_image({status_node_x_cord}, {node_y_cord}, image = sn_red_node)")
                exec(f"sn_label_node_{i} = Label(canvas, image = sn_red_node)")
                exec(f"sn_label_node_{i}.image = sn_red_node")

                #text
                texta = call_error_list[-i-1]
                exec(f'status_text_{i} = canvas.create_text({status_text_x_cord}, {text_y_cord}, anchor = "nw", text = "{texta}", fill = "#D1D3D4", font = ("Inter", 9 * -1))')


        elif lena == 0:

            image_image_33 = PhotoImage(
                file=relative_to_assets(direc = 'dashboard', path = "image_33.png"))
            image_33 = canvas.create_image(
                1066.5,
                751.0,
                image=image_image_33
            )
            
            label_33 = Label(canvas, image=image_image_33)
            label_33.image = image_image_33 # keep a reference!

            image_image_34 = PhotoImage(
                file=relative_to_assets(direc = 'dashboard', path = "image_34.png"))
            image_34 = canvas.create_image(
                932.5,
                751.0,
                image=image_image_34
            )

            label_34 = Label(canvas, image=image_image_33)
            label_34.image = image_image_34 # keep a reference!

            status_text_1 = canvas.create_text(
                949.0,
                746.0,
                anchor="nw",
                text="You are all set!",
                fill="#D1D3D4",
                font=("Inter", 9 * -1)
            )



    create_status_nodes()


    def call_error(error_text: str):

        #beep notification indicating mistake
        import AppKit
        AppKit.NSBeep()

        if len(call_error_list) > 10:
            call_error_list.pop(0)

        #adding error into list
        call_error_list.append(error_text)
        create_status_nodes()




    ##########################################################################################################################################################################################################


    def create_add_products_made():

        lower_dashboard_buttons()
        check_connection()

        apm_image_1 = PhotoImage(
            file=relative_to_assets(direc = 'Add products made', path = "image_1.png"))
        apm1 = canvas.create_image(
            640.0029296875,
            400.0,
            image=apm_image_1
        )

        apm_label_1 = Label(canvas, image = apm_image_1)
        apm_label_1.image = apm_image_1
        
        apm_image_2 = PhotoImage(
            file=relative_to_assets(direc = 'Add products made', path = "image_2.png"))
        apm2 = canvas.create_image(
            639.7666015625,
            399.780029296875,
            image=apm_image_2
        )

        apm_label_2 = Label(canvas, image = apm_image_2)
        apm_label_2.image = apm_image_2

        apm_image_3 = PhotoImage(
            file=relative_to_assets(direc = 'Add products made', path = "image_3.png"))
        apm3 = canvas.create_image(
            639.3779296875,
            399.310302734375,
            image=apm_image_3
        )

        apm_label_3 = Label(canvas, image = apm_image_3)
        apm_label_3.image = apm_image_3

        apm4 = canvas.create_rectangle(
                463.3779296875,
                320.744873046875,
                816,
                493.26611328125,
                fill="#171819",
                outline="")


        apm_image_4 = PhotoImage(
            file=relative_to_assets(direc = 'Add products made', path = "image_4.png"))
        apm5 = canvas.create_image(
            639.376953125,
            320.744873046875,
            image=apm_image_4
        )

        apm_label_4 = Label(canvas, image = apm_image_4)
        apm_label_4.image = apm_image_4

        apm_image_5 = PhotoImage(
            file=relative_to_assets(direc = 'Add products made', path = "image_5.png"))
        apm6 = canvas.create_image(
            639.4404296875,
            359.87109375,
            image=apm_image_5
        )

        apm_label_5 = Label(canvas, image = apm_image_5)
        apm_label_5.image = apm_image_5

        apm_image_6 = PhotoImage(
            file=relative_to_assets(direc = 'Add products made', path = "image_6.png"))
        apm7 = canvas.create_image(
            639.4404296875,
            453.75732421875,
            image=apm_image_6
        )

        apm_label_6 = Label(canvas, image = apm_image_6)
        apm_label_6.image = apm_image_6

        apm_image_7 = PhotoImage(
            file=relative_to_assets(direc = 'Add products made', path = "image_7.png"))
        apm8 = canvas.create_image(
            639.4404296875,
            406.814208984375,
            image=apm_image_7
        )

        apm_label_7 = Label(canvas, image = apm_image_7)
        apm_label_7.image = apm_image_7

        apm_image_8 = PhotoImage(
            file=relative_to_assets(direc = 'Add products made', path = "image_8.png"))
        apm9 = canvas.create_image(
            639.376953125,
            493.26611328125,
            image=apm_image_8
        )

        apm_label_8 = Label(canvas, image = apm_image_8)
        apm_label_8.image = apm_image_8

        apm10 = canvas.create_text(
            494.0009765625,
            353.0,
            anchor="nw",
            text="Product Name",
            fill="#000000",
            font=("Inter", 11 * -1)
        )

        apm_entry_image_1 = PhotoImage(
            file=relative_to_assets(direc = 'Add products made', path = "entry_1.png"))
        apm11 = canvas.create_image(
            640.5,
            407.0,
            image=apm_entry_image_1
        )

        apm_entry_label_1 = Label(canvas, image = apm_entry_image_1)
        apm_entry_label_1.image = apm_entry_image_1

        def temp_text_1(e):
            entry_1.delete(0, END)

        def temp_text_2(e):
            entry_2.delete(0, END)
            
            
        entry_1 = Entry(
            bd=0,
            bg="#D1D3D4",
            fg="#000000",
            font=("Inter", 11 * -1),
            highlightthickness=0
        )
        entry_1.insert(0,"Amount of products made")
        entry_1.pack()
        entry_1.bind("<FocusIn>", temp_text_1) 
        apm12 = entry_1.place(
            x=494.0,
            y=399.0,
            width=293.0,
            height=16.0
        )

        apm_entry_image_2 = PhotoImage(
            file=relative_to_assets(direc = 'Add products made', path = "entry_2.png"))
        apm13 = canvas.create_image(
            640.5,
            454.0,
            image=apm_entry_image_2
        )

        apm_entry_label_2 = Label(canvas, image = apm_entry_image_2)
        apm_entry_label_2.image = apm_entry_image_2
        
        entry_2 = Entry(
            bd=0,
            bg="#D1D3D4",
            fg="#000000",
            font=("Inter", 11 * -1),
            highlightthickness=0
        )
        entry_2.insert(0,"Cost to make products")
        entry_2.pack()
        entry_2.bind("<FocusIn>", temp_text_2) 
        apm14 = entry_2.place(
            x=494.0,
            y=446.0,
            width=293.0,
            height=16.0
        )

        apm15 = canvas.create_text(
            494.5009765625,
            400.0,
            anchor="nw",
            text="Amount of products made",
            fill="#000000",
            font=("Inter", 11 * -1)
        )

        apm16 = canvas.create_text(
            494.5009765625,
            447.0,
            anchor="nw",
            text="Cost to make products",
            fill="#000000",
            font=("Inter", 11 * -1)
        )

        apm17 = canvas.create_text(
            481.5009765625,
            286.5,
            anchor="nw",
            text="Add Products made",
            fill="#D1D3D4",
            font=("Inter", 20 * -1)
        )

        
        def list_product_name(data: dict):

            def change_name(name: str):

                canvas.itemconfig(apm10, text = i)
                Choice = i

            list_product = []
            final_list = []

            if data['orders_tofill'] != {}:

                for i in data['orders_tofill'][list(data['orders_tofill'])[0]]:
                    list_product.append(i)

                list_product.remove("special_occasion")

                for i in data['orders_tofill'][list(data['orders_tofill'])[0]]['special_occasion']:
                    list_product.append(i)

                for i in list_product:
                    temp_array = (i.capitalize(), i)
                    final_list.append(temp_array)
                
            return final_list

        def Click(e, var):

            nclist = list_product_name(data = data)
            my_menu = Menu(None, tearoff=0, takefocus=0)
        
            for (txt, cmd) in nclist:
                exec(f"(my_menu.add_command(label = '{txt}', command = lambda: canvas.itemconfig({apm10}, text = '{txt}')))")
                
            my_menu.tk_popup(e.x_root - 285, e.y_root + 16,entry="0")
            

        l_var = StringVar()

        button_image_1 = PhotoImage(
            file=relative_to_assets(direc = 'Add products made', path = "button_1.png"))
        apm_button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: None,
            relief="flat"
        )
        apm_button_1.bind("<Button-1>", lambda e, var = l_var: Click(e, var))
        apm_button_1.place(
            x=765.5009765625,
            y=356.0,
            width=14,
            height=8.0
        )

        button_label_1 = Label(canvas, image = button_image_1)
        button_label_1.image = button_image_1

        def delete_add_products_made():
            
            raise_dashboard_buttons()
        
            canvas.itemconfig(apm1, state = 'hidden')
            canvas.itemconfig(apm2, state = 'hidden')
            canvas.itemconfig(apm3, state = 'hidden')
            canvas.itemconfig(apm4, state = 'hidden')
            canvas.itemconfig(apm5, state = 'hidden')
            canvas.itemconfig(apm6, state = 'hidden')
            canvas.itemconfig(apm7, state = 'hidden')
            canvas.itemconfig(apm8, state = 'hidden')
            canvas.itemconfig(apm9, state = 'hidden')
            canvas.itemconfig(apm10, state = 'hidden')
            canvas.itemconfig(apm11, state = 'hidden')
            canvas.itemconfig(apm12, state = 'hidden')
            canvas.itemconfig(apm13, state = 'hidden')
            canvas.itemconfig(apm14, state = 'hidden')
            canvas.itemconfig(apm15, state = 'hidden')
            canvas.itemconfig(apm16, state = 'hidden')
            canvas.itemconfig(apm17, state = 'hidden')
            canvas.itemconfig(apm19, state = 'hidden')
            canvas.itemconfig(apm20, state = 'hidden')

            entry_1.lower()
            entry_2.lower()

            apm_button_1.lower()
            apm_button_2.lower()
            apm_button_3.lower()



        apm_button_image_2 = PhotoImage(
            file=relative_to_assets(direc = 'Add products made', path = "button_2.png"))
        apm_button_2 = Button(
            image=apm_button_image_2,
            highlightthickness=0,
            command=lambda: delete_add_products_made(),
            relief="flat"
        )
            
        apm19 = apm_button_2.place(
            x=670.0009765625,
            y=506.5,
            width=61,
            height=17
        )
        
        apm_button_label_2 = Label(canvas, image = apm_button_image_2)
        apm_button_label_2.image = apm_button_image_2
        

        def extract_info():
            
            product_name_a = canvas.itemcget(apm10, 'text')
            amount_pm = entry_1.get()
            cost_pm = entry_2.get()

            def cost_pm_check_float():
                try:
                    float(cost_pm)
                    return True
                except ValueError:
                    return False

            #checking

            if product_name_a == 'Product Name':
                call_error(error_text = "Please choose a type of product.")
                delete_add_products_made()

            if amount_pm.isdigit() == False:
                call_error(error_text = "Please only input an integer for 'Amount of Products Made'.")
                delete_add_products_made()            

            if cost_pm_check_float == False:
                call_error(error_text = "Please only input an integer or decimal for 'Cost to Make Products'.")
                delete_add_products_made()

            
            func.input_product_made(product = product_name_a, amount = int(amount_pm))
            func.input_cost(cost = float(cost_pm))

            chec.refresh_orders_tofill()

            delete_add_products_made()



        apm_button_image_3 = PhotoImage(
            file=relative_to_assets(direc = 'Add products made', path = "button_3.png"))
        apm_button_3 = Button(
            image=apm_button_image_3,
            highlightthickness=0,
            command=lambda: extract_info(),
            relief="flat"
        )
        apm20 = apm_button_3.place(
            x=736.5009765625,
            y=506.5,
            width=61,
            height=17
        )

        apm_button_label_3 = Label(canvas, image = apm_button_image_3)
        apm_button_label_3.image = apm_button_image_3



    def create_add_products_sold():

        lower_dashboard_buttons()
        check_connection()

        def delete_add_products_sold(variable: bool):
                
            canvas.itemconfig(aps1, state = 'hidden')
            canvas.itemconfig(aps2, state = 'hidden')
            canvas.itemconfig(aps3, state = 'hidden')
            canvas.itemconfig(aps4, state = 'hidden')
            canvas.itemconfig(aps5, state = 'hidden')
            canvas.itemconfig(aps6, state = 'hidden')
            canvas.itemconfig(aps7, state = 'hidden')
            canvas.itemconfig(aps8, state = 'hidden')
            canvas.itemconfig(aps9, state = 'hidden')
            canvas.itemconfig(aps10, state = 'hidden')
            canvas.itemconfig(aps11, state = 'hidden')
            canvas.itemconfig(aps12, state = 'hidden')
            
            entry_1.lower()

            aps_button_1.lower()
            aps_button_2.lower()
            aps_button_3.lower()
            
            if variable == True:

                global product_name_a
                global amount_pm
                
                product_name_a = ""
                amount_pm = ""
                raise_dashboard_buttons()


        def temp_text(e):
            entry_1.delete(0, END)


        aps_image_1 = PhotoImage(
            file=relative_to_assets(direc = 'Add products sold', path = "image_1.png"))
        aps1 = canvas.create_image(
            640.0087890625,
            400.0,
            image=aps_image_1
        )

        aps_label_1 = Label(canvas, image = aps_image_1)
        aps_label_1.image = aps_image_1

        aps_image_2 = PhotoImage(
            file=relative_to_assets(direc = 'Add products sold', path = "image_2.png"))
        aps2 = canvas.create_image(
            639.8017578125,
            399.6600341796875,
            image=aps_image_2
        )

        aps_label_2 = Label(canvas, image = aps_image_2)
        aps_label_2.image = aps_image_2

        aps_image_3 = PhotoImage(
            file=relative_to_assets(direc = 'Add products sold', path = "image_3.png"))
        aps3 = canvas.create_image(
            639.3779296875,
            399.2175598144531,
            image=aps_image_3
        )

        aps_label_3 = Label(canvas, image = aps_image_3)
        aps_label_3.image = aps_image_3

        aps_image_4 = PhotoImage(
            file=relative_to_assets(direc = 'Add products sold', path = "image_4.png"))
        aps4 = canvas.create_image(
            639.3779296875,
            406.652099609375,
            image=aps_image_4
        )

        aps_label_4 = Label(canvas, image = aps_image_4)
        aps_label_4.image = aps_image_4

        aps_image_5 = PhotoImage(
            file=relative_to_assets(direc = 'Add products sold', path = "image_5.png"))
        aps5 = canvas.create_image(
            639.376953125,
            338.652099609375,
            image=aps_image_5
        )

        aps_label_5 = Label(canvas, image = aps_image_5)
        aps_label_5.image = aps_image_5

        aps_button_image_1 = PhotoImage(
            file=relative_to_assets(direc = 'Add products sold', path = "button_1.png"))
        aps_button_1 = Button(
            image=aps_button_image_1,
            highlightthickness=0,
            command=lambda: delete_add_products_sold(variable = True),
            relief="flat"
        )
        aps_button_1.place(
            x=665.0,
            y=487.0,
            width=61.75,
            height=19.0
        )

        aps_button_label_1 = Label(canvas, image = aps_button_image_1)
        aps_button_label_1.image = aps_button_image_1
        
        aps_image_6 = PhotoImage(
            file=relative_to_assets(direc = 'Add products sold', path = "image_6.png"))
        aps6 = canvas.create_image(
            639.4404296875,
            383.2812194824219,
            image=aps_image_6
        )

        aps_label_6 = Label(canvas, image = aps_image_6)
        aps_label_6.image = aps_image_6

        def list_product_name(data: dict):

            def change_name(name: str):

                canvas.itemconfig(apm10, text = i)
                Choice = i

            list_product = []
            final_list = []

            if data['orders_tofill'] != {}:

                for i in data['orders_tofill'][list(data['orders_tofill'])[0]]:
                    list_product.append(i)

                list_product.remove("special_occasion")

                for i in data['orders_tofill'][list(data['orders_tofill'])[0]]['special_occasion']:
                    list_product.append(i)

                for i in list_product:
                    temp_array = (i.capitalize(), i)
                    final_list.append(temp_array)
                
            return final_list
        

        def Click(e, var):

            nclist = list_product_name(data = data)
            my_menu = Menu(None, tearoff=0, takefocus=0)
        
            for (txt, cmd) in nclist:
                exec(f"(my_menu.add_command(label = '{txt}', command = lambda: canvas.itemconfig({aps11}, text = '{txt}')))")
                
            my_menu.tk_popup(e.x_root - 285, e.y_root + 16,entry="0")
            

        l_var = StringVar()

        aps_button_image_2 = PhotoImage(
            file=relative_to_assets(direc = 'Add products sold', path = "button_2.png"))
        aps_button_2 = Button(
            image=aps_button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: None,
            relief="flat"
        )
        aps_button_2.bind("<Button-1>", lambda e, var = l_var: Click(e, var))
        
        aps_button_2.place(
            x=765.5009765625,
            y=379.5,
            width=14,
            height=7.5
        )

        aps_button_label_2 = Label(canvas, image = aps_button_image_2)
        aps_button_label_2.image = aps_button_image_2
        
        aps_image_7 = PhotoImage(
            file=relative_to_assets(direc = 'Add products sold', path = "image_7.png"))
        aps7 = canvas.create_image(
            639.4404296875,
            430.22418212890625,
            image=aps_image_7
        )

        aps_label_7 = Label(canvas, image = aps_image_7)
        aps_label_7.image = aps_image_7
        
        entry_1 = Entry(
            bd=0,
            bg="#D1D3D4",
            fg="#000000",
            font=("Inter", 11 * -1),
            highlightthickness=0
        )
        entry_1.insert(0,"Amount of products sold")
        entry_1.pack()
        entry_1.bind("<FocusIn>", temp_text) 
        aps8 = entry_1.place(
            x=494.0,
            y=422.0,
            width=297.0,
            height=15.0
        )

        aps_image_8 = PhotoImage(
            file=relative_to_assets(direc = 'Add products sold', path = "image_8.png"))
        aps9 = canvas.create_image(
            639.376953125,
            475.2358093261719,
            image=aps_image_8
        )

        aps_label_8 = Label(canvas, image = aps_image_8)
        aps_label_8.image = aps_image_8


        def delete_add_products_sold_note():

            delete_add_products_sold(variable = False)

            def delete_delete_add_products_sold_note():

                raise_dashboard_buttons()

                canvas.itemconfig(ddaen1, state = 'hidden')
                canvas.itemconfig(ddaen2, state = 'hidden')
                canvas.itemconfig(ddaen3, state = 'hidden')
                canvas.itemconfig(ddaen4, state = 'hidden')
                canvas.itemconfig(ddaen5, state = 'hidden')
                canvas.itemconfig(ddaen6, state = 'hidden')
                canvas.itemconfig(ddaen7, state = 'hidden')
                canvas.itemconfig(ddaen8, state = 'hidden')
                canvas.itemconfig(ddaen9, state = 'hidden')
                canvas.itemconfig(ddaen10, state = 'hidden')
                canvas.itemconfig(ddaen11, state = 'hidden')
                
                ddaen_button_1.lower()
                ddaen_button_2.lower()


            def product_sold():

                global amount_pm
                global product_name_a

                func.input_product_sold(amount = int(amount_pm), product = product_name_a)

                chec.refresh_orders_tofill()
                
                product_name_a = ''
                amount_pm = ''

                delete_delete_add_products_sold_note()


            ddaen_image_1 = PhotoImage(
                file=relative_to_assets(direc = 'Delete an event note', path = "image_1.png"))
            ddaen1 = canvas.create_image(
                640.0,
                400.0,
                image=ddaen_image_1
            )

            ddaen_label_1 = Label(canvas, image = ddaen_image_1)
            ddaen_label_1.image = ddaen_image_1

            ddaen_image_2 = PhotoImage(
                file=relative_to_assets(direc = 'Delete an event note', path = "image_2.png"))
            ddaen2 = canvas.create_image(
                639.7705078125,
                399.0361328125,
                image=image_image_2
            )

            ddaen_label_2 = Label(canvas, image = ddaen_image_2)
            ddaen_label_2.image = ddaen_image_2

            ddaen_image_3 = PhotoImage(
                file=relative_to_assets(direc = 'Delete an event note', path = "image_3.png"))
            ddaen3 = canvas.create_image(
                639.376953125,
                399.58642578125,
                image=ddaen_image_3
            )

            ddaen_label_3 = Label(canvas, image = ddaen_image_3)
            ddaen_label_3.image = ddaen_image_3

            ddaen_image_4 = PhotoImage(
                file=relative_to_assets(direc = 'Delete an event note', path = "image_4.png"))
            ddaen4 = canvas.create_image(
                639.376953125,
                405.4169921875,
                image=ddaen_image_4
            )

            ddaen_label_4 = Label(canvas, image = ddaen_image_4)
            ddaen_label_4.image = ddaen_image_4

            ddaen_image_5 = PhotoImage(
                file=relative_to_assets(direc = 'Delete an event note', path = "image_5.png"))
            ddaen5 = canvas.create_image(
                639.0,
                349.0,
                image=ddaen_image_5
            )

            ddaen_label_5 = Label(canvas, image = ddaen_image_5)
            ddaen_label_5.image = ddaen_image_5

            ddaen_image_6 = PhotoImage(
                file=relative_to_assets(direc = 'Delete an event note', path = "image_6.png"))
            ddaen6 = canvas.create_image(
                639.0,
                461.6171875,
                image=ddaen_image_6
            )

            ddaen_label_6 = Label(canvas, image = ddaen_image_6)
            ddaen_label_6.image = ddaen_image_6

            ddaen_button_image_1 = PhotoImage(
                file=relative_to_assets(direc = 'Delete an event note', path = "button_1.png"))
            ddaen_button_1 = Button(
                image=ddaen_button_image_1,
                highlightthickness=0,
                command=lambda: delete_delete_add_products_sold_note(),
                relief="flat"
            )
            ddaen_button_1.place(
                x=666.5009765625,
                y=475.0,
                width=61,
                height=17
            )

            ddaen_button_label_1 = Label(canvas, image = ddaen_button_image_1)
            ddaen_button_label_1.image = ddaen_button_image_1

            ddaen_button_image_2 = PhotoImage(
                file=relative_to_assets(direc = 'Delete an event note', path = "button_2.png"))
            ddaen_button_2 = Button(
                image=ddaen_button_image_2,
                highlightthickness=0,
                command=lambda: product_sold(),
                relief="flat"
            )
            ddaen_button_2.place(
                x=736.0009765625,
                y=475.0,
                width=61,
                height=17
            )

            ddaen_button_label_2 = Label(canvas, image = ddaen_button_image_2)
            ddaen_button_label_2.image = ddaen_button_image_2

            ddaen7 = canvas.create_text(
                481.5009765625,
                317.5,
                anchor="nw",
                text="Sold a product",
                fill="#D1D3D4",
                font=("Inter", 20 * -1)
            )

            ddaen8 = canvas.create_text(
                482.0,
                365.0,
                anchor="nw",
                text="Are you sure that you like to add this data to the",
                fill="#D1D3D4",
                font=("Inter", 11 * -1)
            )

            ddaen9 = canvas.create_text(
                482.0,
                381.0,
                anchor="nw",
                text="database for this event?",
                fill="#D1D3D4",
                font=("Inter", 11 * -1)
            )

            ddaen10 = canvas.create_text(
                482.0,
                411.0,
                anchor="nw",
                text="You cannot undo this move. The data will be added",
                fill="#D1D3D4",
                font=("Inter", 11 * -1)
            )

            ddaen11 = canvas.create_text(
                482.0,
                427.0,
                anchor="nw",
                text="permanently.",
                fill="#D1D3D4",
                font=("Inter", 11 * -1)
            )

        

        def extract_info():
            
            global product_name_a
            global amount_pm
            
            product_name_a = canvas.itemcget(aps11, 'text')
            amount_pm = entry_1.get()

            #checking
            
            def clear_global_var():
                product_name_a = ''
                amount_pm = ''
            
            if product_name_a == 'Product Name' and amount_pm == 'Amount of products sold':
                clear_global_var()
                delete_add_products_sold(variable = True)            

            if product_name_a == 'Product Name':
                clear_global_var()
                call_error(error_text = "Please choose a type of product.")
                delete_add_products_sold(variable = True)

            if amount_pm.isdigit() == False:
                clear_global_var()
                call_error(error_text = "Please only input an integer for 'Amount of Products Sold'.")
                delete_add_products_sold(variable = True)

            delete_add_products_sold_note()
            

        aps_button_image_3 = PhotoImage(
            file=relative_to_assets(direc = 'Add products sold', path = "button_3.png"))
        aps_button_3 = Button(
            image=aps_button_image_3,
            highlightthickness=0,
            command=lambda: extract_info(),
            relief="flat"
        )
        aps_button_3.place(
            x=735.0,
            y=487.0,
            width=63.0,
            height=19.0
        )

        aps_button_label_3 = Label(canvas, image = aps_button_image_3)
        aps_button_label_3.image = aps_button_image_3

        aps10 = canvas.create_text(
            481.5009765625,
            304.5,
            anchor="nw",
            text="Add Products Sold",
            fill="#D1D3D4",
            font=("Inter", 20 * -1)
        )

        aps11 = canvas.create_text(
            494.0009765625,
            377.0,
            anchor="nw",
            text="Product Name",
            fill="#000000",
            font=("Inter", 11 * -1)
        )

        aps12 = canvas.create_text(
            494.0009765625,
            422.5,
            anchor="nw",
            text="Amount of products sold",
            fill="#000000",
            font=("Inter", 11 * -1)
        )



    def create_retrieve_orders():

        lower_dashboard_buttons()
        check_connection()

        def delete_retrieve_orders():
            
            raise_dashboard_buttons()
        
            canvas.itemconfig(ro1, state = 'hidden')
            canvas.itemconfig(ro2, state = 'hidden')
            canvas.itemconfig(ro3, state = 'hidden')
            canvas.itemconfig(ro4, state = 'hidden')
            canvas.itemconfig(ro5, state = 'hidden')
            canvas.itemconfig(ro6, state = 'hidden')
            canvas.itemconfig(ro7, state = 'hidden')
            canvas.itemconfig(ro8, state = 'hidden')
            canvas.itemconfig(ro9, state = 'hidden')
            canvas.itemconfig(ro10, state = 'hidden')
            canvas.itemconfig(ro11, state = 'hidden')
            
            ro_button_1.lower()
            ro_button_2.lower()


        ro_image_1 = PhotoImage(
            file=relative_to_assets(direc = 'Retrieve orders', path = "image_1.png"))
        ro1 = canvas.create_image(
            640.0,
            400.0,
            image=ro_image_1
        )

        ro_label_1 = Label(canvas, image = ro_image_1)
        ro_label_1.image = ro_image_1

        ro_image_2 = PhotoImage(
            file=relative_to_assets(direc = 'Retrieve orders', path = "image_2.png"))
        ro2 = canvas.create_image(
            639.7890625,
            405.74658203125,
            image=ro_image_2
        )

        ro_label_2 = Label(canvas, image = ro_image_2)
        ro_label_2.image = ro_image_2

        ro_image_3 = PhotoImage(
            file=relative_to_assets(direc = 'Retrieve orders', path = "image_3.png"))
        ro3 = canvas.create_image(
            639.376953125,
            405.31201171875,
            image=ro_image_3
        )

        ro_label_3 = Label(canvas, image = ro_image_3)
        ro_label_3.image = ro_image_3

        ro_image_4 = PhotoImage(
            file=relative_to_assets(direc = 'Retrieve orders', path = "image_4.png"))
        ro4 = canvas.create_image(
            639.376953125,
            411.14208984375,
            image=ro_image_4
        )

        ro_label_4 = Label(canvas, image = ro_image_4)
        ro_label_4.image = ro_image_4

        ro_image_5 = PhotoImage(
            file=relative_to_assets(direc = 'Retrieve orders', path = "image_5.png"))
        ro5 = canvas.create_image(
            639.3759765625,
            355.14208984375,
            image=ro_image_5
        )

        ro_label_5 = Label(canvas, image = ro_image_5)
        ro_label_5.image = ro_image_5

        ro_image_6 = PhotoImage(
            file=relative_to_assets(direc = 'Retrieve orders', path = "image_6.png"))
        ro6 = canvas.create_image(
            639.3759765625,
            467.759765625,
            image=ro_image_6
        )

        ro_label_6 = Label(canvas, image = ro_image_6)
        ro_label_6.image = ro_image_6

        ro_button_image_1 = PhotoImage(
            file=relative_to_assets(direc = 'Retrieve orders', path = "button_1.png"))
        ro_button_1 = Button(
            image=ro_button_image_1,
            highlightthickness=0,
            command=lambda: delete_retrieve_orders(),
            relief="flat"
        )
        ro_button_1.place(
            x=665.0009765625,
            y=480.5,
            width=61,
            height=17
        )

        ro_button_label_1 = Label(canvas, image = ro_button_image_1)
        ro_button_label_1.image = ro_button_image_1

        def extract_info():
            
            if form.check_input_form_created() == False:
                call_error(error_text = "Unable to retreive order from forms. Form isnt created yet.")
            elif form.check_input_form_created() == True:
                form.retrieve_responses_input()

            chec.refresh_orders_tofill()        
            delete_retrieve_orders()

        ro_button_image_2 = PhotoImage(
            file=relative_to_assets(direc = 'Retrieve orders', path = "button_2.png"))
        ro_button_2 = Button(
            image=ro_button_image_2,
            highlightthickness=0,
            command=lambda: extract_info(),
            relief="flat"
        )
        ro_button_2.place(
            x=736.0009765625,
            y=480.5,
            width=61,
            height=17
        )

        ro_button_label_2 = Label(canvas, image = ro_button_image_2)
        ro_button_label_2.image = ro_button_image_2

        ro7 = canvas.create_text(
            481.0,
            324.0,
            anchor="nw",
            text="Retrieve Orders",
            fill="#D1D3D4",
            font=("Inter", 20 * -1)
        )

        ro8 = canvas.create_text(
            482.0,
            371.0,
            anchor="nw",
            text="Are you sure that you would like to retrieve the orders",
            fill="#D1D3D4",
            font=("Inter", 11 * -1)
        )

        ro9 = canvas.create_text(
            482.0,
            387.0,
            anchor="nw",
            text="from the google form?",
            fill="#D1D3D4",
            font=("Inter", 11 * -1)
        )

        ro10 = canvas.create_text(
            482.0,
            418.0,
            anchor="nw",
            text="You cannot undo this move. The data will be recorded",
            fill="#D1D3D4",
            font=("Inter", 11 * -1)
        )

        ro11 = canvas.create_text(
            482.0,
            434.0,
            anchor="nw",
            text="permanently.",
            fill="#D1D3D4",
            font=("Inter", 11 * -1)
        )

        

    def create_add_type_of_product():

        lower_dashboard_buttons()
        check_connection()

        def delete_add_type_of_product():
            
            raise_dashboard_buttons()
        
            canvas.itemconfig(atop1, state = 'hidden')
            canvas.itemconfig(atop2, state = 'hidden')
            canvas.itemconfig(atop3, state = 'hidden')
            canvas.itemconfig(atop4, state = 'hidden')
            canvas.itemconfig(atop5, state = 'hidden')
            canvas.itemconfig(atop6, state = 'hidden')
            canvas.itemconfig(atop7, state = 'hidden')
            canvas.itemconfig(atop8, state = 'hidden')
            canvas.itemconfig(atop9, state = 'hidden')
            canvas.itemconfig(atop10, state = 'hidden')
            canvas.itemconfig(atop11, state = 'hidden')

            atop_button_1.lower()
            atop_button_2.lower()
            atop_button_3.lower()


        atop_image_1 = PhotoImage(
            file=relative_to_assets(direc = 'Add type of product', path = "image_1.png"))
        atop1 = canvas.create_image(
            640.0,
            400.0,
            image=atop_image_1
        )

        atop_label_1 = Label(canvas, image = atop_image_1)
        atop_label_1.image = atop_image_1

        atop_image_2 = PhotoImage(
            file=relative_to_assets(direc = 'Add type of product', path = "image_2.png"))
        atop2 = canvas.create_image(
            639.544921875,
            382.080078125,
            image=atop_image_2
        )

        atop_label_2 = Label(canvas, image = atop_image_2)
        atop_label_2.image = atop_image_2

        atop_image_3 = PhotoImage(
            file=relative_to_assets(direc = 'Add type of product', path = "image_3.png"))
        atop3 = canvas.create_image(
            639.3779296875,
            381.818359375,
            image=atop_image_3
        )

        atop_label_3 = Label(canvas, image = atop_image_3)
        atop_label_3.image = atop_image_3

        atop4 = canvas.create_rectangle(
            463.3779296875,
            330.43310546875,
            816.6259765625,
            443.684326171875,
            fill="#171819",
            outline="")

        atop_image_4 = PhotoImage(
            file=relative_to_assets(direc = 'Add type of product', path = "image_4.png"))
        atop5 = canvas.create_image(
            639.376953125,
            330.43310546875,
            image=atop_image_4
        )

        atop_label_4 = Label(canvas, image = atop_image_4)
        atop_label_4.image = atop_image_4

        atop_button_image_1 = PhotoImage(
            file=relative_to_assets(direc = 'Add type of product', path = "button_1.png"))
        atop_button_1 = Button(
            image=atop_button_image_1,
            highlightthickness=0,
            command=lambda: delete_add_type_of_product(),
            relief="flat"
        )
        atop_button_1.place(
            x=665.0,
            y=459.0,
            width=62.0,
            height=18.0
        )

        atop_button_label_1 = Label(canvas, image = atop_button_image_1)
        atop_button_label_1.image = atop_button_image_1

        atop_image_5 = PhotoImage(
            file=relative_to_assets(direc = 'Add type of product', path = "image_5.png"))
        atop6 = canvas.create_image(
            639.439453125,
            404.217041015625,
            image=atop_image_5
        )

        atop_label_5 = Label(canvas, image = atop_image_5)
        atop_label_5.image = atop_image_5

        def list_product_name(data: dict):

            def change_name(name: str):

                canvas.itemconfig(apm10, text = i)
                Choice = i

            list_product = []
            final_list = []

            for i in data['type_of_products']:
                list_product.append(i)

            list_product.remove("special_occasion")

            for i in data['type_of_products']['special_occasion']:
                list_product.append(i)

            if data['orders_tofill'] != {}:
                
                #sort out
                for i in data['orders_tofill'][list(data['orders_tofill'])[0]]:
                    if i in list_product:
                        list_product.remove(i)

                for i in data['orders_tofill'][list(data['orders_tofill'])[0]]['special_occasion']:
                    if i in list_product:
                        list_product.remove(i)
                
                for i in list_product:
                    temp_array = (i.capitalize(), i)
                    final_list.append(temp_array)
                    
            return final_list
        
              

        def Click(e, var):

            nclist = list_product_name(data = data)
            my_menu = Menu(None, tearoff=0, takefocus=0)
        
            for (txt, cmd) in nclist:
                exec(f"(my_menu.add_command(label = '{txt}', command = lambda: canvas.itemconfig({atop8}, text = '{txt}')))")
                
            my_menu.tk_popup(e.x_root - 285, e.y_root + 16,entry="0")
            

        l_var = StringVar()
        

        atop_button_image_2 = PhotoImage(
            file=relative_to_assets(direc = 'Add type of product', path = "button_2.png"))
        atop_button_2 = Button(
            image=atop_button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: None,
            relief="flat"
        )
        atop_button_2.bind("<Button-1>", lambda e, var = l_var: Click(e, var))
        atop_button_2.place(
            x=765.5009765625,
            y=401.0,
            width=14,
            height=8.0
        )

        atop_button_label_2 = Label(canvas, image = atop_button_image_2)
        atop_button_label_2.image = atop_button_image_2

        atop_image_6 = PhotoImage(
            file=relative_to_assets(direc = 'Add type of product', path = "image_6.png"))
        atop7 = canvas.create_image(
            639.3779296875,
            443.684326171875,
            image=atop_image_6
        )

        atop_label_6 = Label(canvas, image = atop_image_6)
        atop_label_6.image = atop_image_6

        def extract_info():
            
            product_name_a = canvas.itemcget(atop8, 'text')

            if product_name_a == 'Product Name':
                delete_add_type_of_product()

            func.input_event_product(product = product_name_a)

            delete_add_type_of_product()

        atop_button_image_3 = PhotoImage(
            file=relative_to_assets(direc = 'Add type of product', path = "button_3.png"))
        atop_button_3 = Button(
            image=atop_button_image_3,
            highlightthickness=0,
            command=lambda: extract_info(),
            relief="flat"
        )
        atop_button_3.place(
            x=736.0,
            y=459.0,
            width=62.0,
            height=18.0
        )

        atop_button_label_3 = Label(canvas, image = atop_button_image_3)
        atop_button_label_3.image = atop_button_image_3

        atop8 = canvas.create_text(
            494.0009765625,
            397.5,
            anchor="nw",
            text="Product Name",
            fill="#000000",
            font=("Inter", 11 * -1)
        )

        atop9 = canvas.create_text(
            481.0,
            297.0,
            anchor="nw",
            text="Add Type of Product",
            fill="#D1D3D4",
            font=("Inter", 18 * -1)
        )

        atop10 = canvas.create_text(
            486.7001953125,
            348.300048828125,
            anchor="nw",
            text="Note: You are now adding a new type of product for the current event.",
            fill="#D1D3D4",
            font=("Inter", 8 * -1)
        )

        atop11 = canvas.create_text(
            487.0,
            360.0,
            anchor="nw",
            text="You are not adding a brand new type of product to the application.",
            fill="#D1D3D4",
            font=("Inter", 8 * -1)
        )




    def create_add_new_product():

        lower_dashboard_buttons()
        check_connection()

        def delete_add_new_product():
            
            raise_dashboard_buttons()
        
            canvas.itemconfig(anp1, state = 'hidden')
            canvas.itemconfig(anp2, state = 'hidden')
            canvas.itemconfig(anp3, state = 'hidden')
            canvas.itemconfig(anp4, state = 'hidden')
            canvas.itemconfig(anp5, state = 'hidden')
            canvas.itemconfig(anp6, state = 'hidden')
            canvas.itemconfig(anp7, state = 'hidden')
            canvas.itemconfig(anp8, state = 'hidden')
            canvas.itemconfig(anp10, state = 'hidden')
            canvas.itemconfig(anp11, state = 'hidden')
            canvas.itemconfig(anp12, state = 'hidden')

            entry_1.lower()
            entry_2.lower()

            anp_button_1.lower()
            anp_button_2.lower()
            anp_button_3.lower()
            anp_button_4.lower()

            global special_occasion_anp

            special_occasion_anp = ""

        def temp_text_1(e):
            entry_1.delete(0, END)

        def temp_text_2(e):
            entry_2.delete(0, END)
            

        global special_occasion_anp
        special_occasion_anp = ""

        anp_image_1 = PhotoImage(
            file=relative_to_assets(direc = 'Add new type of product', path = "image_1.png"))
        anp1 = canvas.create_image(
            640.0,
            400.0,
            image=anp_image_1
        )

        anp_label_1 = Label(canvas, image = anp_image_1)
        anp_label_1.image = anp_image_1

        anp_image_2 = PhotoImage(
            file=relative_to_assets(direc = 'Add new type of product', path = "image_2.png"))
        anp2 = canvas.create_image(
            639.80078125,
            399.7003173828125,
            image=anp_image_2
        )

        anp_label_2 = Label(canvas, image = anp_image_2)
        anp_label_2.image = anp_image_2

        anp_image_3 = PhotoImage(
            file=relative_to_assets(direc = 'Add new type of product', path = "image_3.png"))
        anp3 = canvas.create_image(
            639.376953125,
            399.310302734375,
            image=anp_image_3
        )

        anp_label_3 = Label(canvas, image = anp_image_3)
        anp_label_3.image = anp_image_3

        anp4 = canvas.create_rectangle(
            463.376953125,
            320.744873046875,
            815.625,
            493.2659912109375,
            fill="#171819",
            outline="")

        anp_image_4 = PhotoImage(
            file=relative_to_assets(direc = 'Add new type of product', path = "image_4.png"))
        anp5 = canvas.create_image(
            639.375,
            320.744873046875,
            image=anp_image_4
        )

        anp_label_4 = Label(canvas, image = anp_image_4)
        anp_label_4.image = anp_image_4

        anp_button_image_1 = PhotoImage(
            file=relative_to_assets(direc = 'Add new type of product', path = "button_1.png"))
        anp_button_1 = Button(
            image=anp_button_image_1,
            highlightthickness=0,
            command=lambda: delete_add_new_product(),
            relief="flat"
        )
        anp_button_1.place(
            x=665.0,
            y=506.5,
            width=61,
            height=17
        )

        anp_button_label_1 = Label(canvas, image = anp_button_image_1)
        anp_button_label_1.image = anp_button_image_1

        anp_image_5 = PhotoImage(
            file=relative_to_assets(direc = 'Add new type of product', path = "image_5.png"))
        anp6 = canvas.create_image(
            639.439453125,
            359.8712158203125,
            image=anp_image_5
        )

        anp_label_5 = Label(canvas, image = anp_image_5)
        anp_label_5.image = anp_image_5

        anp_image_6 = PhotoImage(
            file=relative_to_assets(direc = 'Add new type of product', path = "image_6.png"))
        anp7 = canvas.create_image(
            639.439453125,
            406.814208984375,
            image=anp_image_6
        )

        anp_label_6 = Label(canvas, image = anp_image_6)
        anp_label_6.image = anp_image_6

        anp_image_7 = PhotoImage(
            file=relative_to_assets(direc = 'Add new type of product', path = "image_7.png"))
        anp8 = canvas.create_image(
            639.375,
            493.2659912109375,
            image=anp_image_7
        )

        anp_label_7 = Label(canvas, image = anp_image_7)
        anp_label_7.image = anp_image_7

        def special_occa_no():

            global special_occasion_anp

            special_occasion_anp = False

        anp_button_image_3 = PhotoImage(
            file=relative_to_assets(direc = 'Add new type of product', path = "button_3.png"))
        anp_button_3 = Button(
            image=anp_button_image_3,
            highlightthickness=0,
            command=lambda: special_occa_no(),
            relief="flat"
        )
        anp_button_3.place(
            x=651.0,
            y=463.0,
            width=36.0,
            height=13.0
        )

        anp_button_label_3 = Label(canvas, image = anp_button_image_3)
        anp_button_label_3.image = anp_button_image_3

        def special_occa_yes():

            global special_occasion_anp

            special_occasion_anp = True

        anp_button_image_4 = PhotoImage(
            file=relative_to_assets(direc = 'Add new type of product', path = "button_4.png"))
        anp_button_4 = Button(
            image=anp_button_image_4,
            highlightthickness=0,
            command=lambda: special_occa_yes(),
            relief="flat"
        )
        anp_button_4.place(
            x=591.0,
            y=463.0,
            width=39.0,
            height=13.0
        )

        anp_button_label_4 = Label(canvas, image = anp_button_image_4)
        anp_button_label_4.image = anp_button_image_4

        anp10 = canvas.create_text(
            481.5,
            286.0,
            anchor="nw",
            text="Add New Type of Product",
            fill="#D1D3D4",
            font=("Inter", 20 * -1)
        )

        entry_1 = Entry(
            bd=0,
            bg="#D1D3D4",
            fg="#000000",
            font=("Inter", 11 * -1),
            highlightthickness=0
        )
        entry_1.insert(0,"Name of new product")
        entry_1.pack()
        entry_1.bind("<FocusIn>", temp_text_1) 
        entry_1.place(
            x=494.0,
            y=352,
            width=292.0,
            height=15.0
        )

        entry_2 = Entry(
            bd=0,
            bg="#D1D3D4",
            fg="#000000",
            font=("Inter", 11 * -1),
            highlightthickness=0
        )
        entry_2.insert(0,"Sell price")
        entry_2.pack()
        entry_2.bind("<FocusIn>", temp_text_2) 
        entry_2.place(
            x=494.0,
            y=399,
            width=292.0,
            height=15.0
        )

        canvas.update()

        anp11 = canvas.create_text(
            494.0,
            400.0,
            anchor="nw",
            text="Sell price",
            fill="#000000",
            font=("Inter", 11 * -1)
        )

        anp12 = canvas.create_text(
            493.0,
            438.0,
            anchor="nw",
            text="Is this product only available during special occasions?",
            fill="#FFFFFF",
            font=("Inter", 11 * -1)
        )

        def extract_info():

            global special_occasion_anp

            product_name_a = entry_1.get()
            price = entry_2.get()

            def cost_pm_check_float():
                try:
                    float(price)
                    return True
                except ValueError:
                    return False

            if (product_name_a == 'Name of new product' or product_name_a == '') and (price == 'Sell price' or price == ''):
                call_error(error_text = "You didn't add anything to 'Add New Product'.")
                delete_add_new_product()

            elif product_name_a == 'Name of new product' or product_name_a == '':
                call_error(error_text = "Please write down a new product name.")
                delete_add_new_product()

            elif cost_pm_check_float == False or price == 'Sell price' or price == '':
                call_error(error_text = "Only input integer or decimal for 'Add New Product'.")
                delete_add_new_product()

            elif special_occasion_anp == '':
                call_error(error_text = "Unable to add new product.")
                call_error(error_text = "You didn't click the 'Special Occasions' button.")

            else:
                func.input_new_product(new_product = product_name_a, special_occasion = special_occasion_anp, price = price)
                special_occasion_anp = ''

            delete_add_new_product()



        anp_button_image_2 = PhotoImage(
            file=relative_to_assets(direc = 'Add new type of product', path = "button_2.png"))
        anp_button_2 = Button(
            image=anp_button_image_2,
            highlightthickness=0,
            command=lambda: extract_info(),
            relief="flat"
        )
        anp_button_2.place(
            x=731.501953125,
            y=506.5,
            width=62,
            height=17
        )

        anp_button_label_2 = Label(canvas, image = anp_button_image_2)
        anp_button_label_2.image = anp_button_image_2




    def create_add_time_spent():

        lower_dashboard_buttons()
        check_connection()

        def delete_add_time_spent():
            
            raise_dashboard_buttons()
        
            canvas.itemconfig(ats1, state = 'hidden')
            canvas.itemconfig(ats2, state = 'hidden')
            canvas.itemconfig(ats3, state = 'hidden')
            canvas.itemconfig(ats4, state = 'hidden')
            canvas.itemconfig(ats5, state = 'hidden')
            canvas.itemconfig(ats6, state = 'hidden')
            canvas.itemconfig(ats7, state = 'hidden')
            canvas.itemconfig(ats8, state = 'hidden')
            canvas.itemconfig(ats9, state = 'hidden')
            canvas.itemconfig(ats10, state = 'hidden')
            canvas.itemconfig(ats11, state = 'hidden')
            
            entry_1.lower()
            entry_2.lower()

            ats_button_1.lower()
            ats_button_2.lower()
            

        def temp_text_1(e):
            entry_1.delete(0, END)

        def temp_text_2(e):
            entry_2.delete(0, END)


        ats_image_1 = PhotoImage(
            file=relative_to_assets(direc = 'Add time spent', path = "image_1.png"))
        ats1 = canvas.create_image(
            640.0087890625,
            400.3363037109375,
            image=ats_image_1
        )

        ats_label_1 = Label(canvas, image = ats_image_1)
        ats_label_1.image = ats_image_1

        ats_image_2 = PhotoImage(
            file=relative_to_assets(direc = 'Add time spent', path = "image_2.png"))
        ats2 = canvas.create_image(
            639.8017578125,
            399.6611328125,
            image=ats_image_2
        )

        ats_label_2 = Label(canvas, image = ats_image_2)
        ats_label_2.image = ats_image_2

        ats_image_3 = PhotoImage(
            file=relative_to_assets(direc = 'Add time spent', path = "image_3.png"))
        ats3 = canvas.create_image(
            639.3779296875,
            399.217529296875,
            image=ats_image_3
        )

        ats_label_3 = Label(canvas, image = ats_image_3)
        ats_label_3.image = ats_image_3

        ats4 = canvas.create_rectangle(
            463.3779296875,
            338.652099609375,
            816,
            475.23583984375,
            fill="#171819",
            outline="")

        ats_image_4 = PhotoImage(
            file=relative_to_assets(direc = 'Add time spent', path = "image_4.png"))
        ats5 = canvas.create_image(
            639.376953125,
            338.652099609375,
            image=ats_image_4
        )

        ats_label_4 = Label(canvas, image = ats_image_4)
        ats_label_4.image = ats_image_4

        ats_button_image_1 = PhotoImage(
            file=relative_to_assets(direc = 'Add time spent', path = "button_1.png"))
        ats_button_1 = Button(
            image=ats_button_image_1,
            highlightthickness=0,
            command=lambda: delete_add_time_spent(),
            relief="flat"
        )
        ats_button_1.place(
            x=668,
            y=487.5,
            width=61,
            height=17.548095703125
        )

        ats_button_label_1 = Label(canvas, image = ats_button_image_1)
        ats_button_label_1.image = ats_button_image_1

        ats_image_5 = PhotoImage(
            file=relative_to_assets(direc = 'Add time spent', path = "image_5.png"))
        ats6 = canvas.create_image(
            639.4404296875,
            383.28125,
            image=ats_image_5
        )

        ats_label_5 = Label(canvas, image = ats_image_5)
        ats_label_5.image = ats_image_5

        ats_image_6 = PhotoImage(
            file=relative_to_assets(direc = 'Add time spent', path = "image_6.png"))
        ats7 = canvas.create_image(
            639.4404296875,
            430.22412109375,
            image=ats_image_6
        )

        ats_label_6 = Label(canvas, image = ats_image_6)
        ats_label_6.image = ats_image_6

        ats_image_7 = PhotoImage(
            file=relative_to_assets(direc = 'Add time spent', path = "image_7.png"))
        ats8 = canvas.create_image(
            639.376953125,
            475.23583984375,
            image=ats_image_7
        )

        ats_label_7 = Label(canvas, image = ats_image_7)
        ats_label_7.image = ats_image_7
        

        def extract_info():

            hour = entry_1.get()
            minute = entry_2.get()

            #checking

            if hour == "" and minute == "":
                delete_add_time_spent()

            elif hour == "Hours (enter 0 if none)" and minute == "Minutes (enter 0 if none)":
                delete_add_time_spent()
                
            else:

                if hour == "" or hour == "Hours (enter 0 if none)":
                    hour = 0
                elif hour != "":
                    if hour.isdigit() == False:
                        call_error(error_text = "Please only input an integer for 'Add Time Spent'.")
                        delete_add_time_spent()
                        
                if minute == "" or minute == "Minutes (enter 0 if none)":
                    minute = 0
                elif minute != "":
                    if minute.isdigit() == False:
                        call_error(error_text = "Please only input an integer for 'Add Time Spent'.")
                        delete_add_time_spent()


            func.input_time_spent(hour = int(hour), minute = int(minute))

            delete_add_time_spent()
            

        ats_button_image_2 = PhotoImage(
            file=relative_to_assets(direc = 'Add time spent', path = "button_2.png"))
        ats_button_2 = Button(
            image=ats_button_image_2,
            highlightthickness=0,
            command=lambda: extract_info(),
            relief="flat"
        )
        ats_button_2.place(
            x=736.0009765625,
            y=487.5,
            width=61.53515625,
            height=17.548095703125
        )

        ats_button_label_2 = Label(canvas, image = ats_button_image_2)
        ats_button_label_2.image = ats_button_image_2

        ats_entry_image_1 = PhotoImage(
            file=relative_to_assets(direc = 'Add time spent', path = "entry_1.png"))
        ats9 = canvas.create_image(
            641.5,
            383.0,
            image=ats_entry_image_1
        )

        ats_entry_label_1 = Label(canvas, image = ats_entry_image_1)
        ats_entry_label_1.image = ats_entry_image_1
        
        entry_1 = Entry(
            bd=0,
            bg="#D1D3D4",
            fg="#000000",
            font=("Inter", 11 * -1),
            highlightthickness=0
        )

        entry_1.insert(0,"Hours (enter 0 if none)")
        entry_1.pack()
        entry_1.bind("<FocusIn>", temp_text_1)

        entry_1.place(
            x=493.0,
            y=375.0,
            width=297.0,
            height=15.0
        )

        ats_entry_image_2 = PhotoImage(
            file=relative_to_assets(direc = 'Add time spent', path = "entry_2.png"))
        ats10 = canvas.create_image(
            641.5,
            430.0,
            image=ats_entry_image_2
        )

        ats_entry_label_2 = Label(canvas, image = ats_entry_image_2)
        ats_entry_label_2.image = ats_entry_image_2

        entry_2 = Entry(
            bd=0,
            bg="#D1D3D4",
            fg="#000000",
            font=("Inter", 11 * -1),
            highlightthickness=0
        )

        entry_2.insert(0,"Minutes (enter 0 if none)")
        entry_2.pack()
        entry_2.bind("<FocusIn>", temp_text_2)

        entry_2.place(
            x=493.0,
            y=422.0,
            width=297.0,
            height=15.0
        )

        canvas.update()

        ats11 = canvas.create_text(
            481.5009765625,
            304.5,
            anchor="nw",
            text="Add Time Spent",
            fill="#D1D3D4",
            font=("Inter", 20 * -1)
        )



    def create_google_form():

        lower_dashboard_buttons()

        def delete_google_form(variable: bool):
        
            canvas.itemconfig(go1, state = 'hidden')
            canvas.itemconfig(go2, state = 'hidden')
            canvas.itemconfig(go3, state = 'hidden')
            canvas.itemconfig(go4, state = 'hidden')
            canvas.itemconfig(go5, state = 'hidden')
            canvas.itemconfig(go6, state = 'hidden')
            canvas.itemconfig(go7, state = 'hidden')
            canvas.itemconfig(go8, state = 'hidden')
            canvas.itemconfig(go9, state = 'hidden')
            canvas.itemconfig(go10, state = 'hidden')
            canvas.itemconfig(go11, state = 'hidden')
            canvas.itemconfig(go12, state = 'hidden')
            canvas.itemconfig(go13, state = 'hidden')
            canvas.itemconfig(go14, state = 'hidden')
            canvas.itemconfig(go15, state = 'hidden')
            canvas.itemconfig(go16, state = 'hidden')
            canvas.itemconfig(go17, state = 'hidden')
            canvas.itemconfig(go18, state = 'hidden')

            go_button_1.lower()
            go_button_2.lower()
            go_button_3.lower()
            go_button_4.lower()
            go_button_5.lower()
            go_button_6.lower()

            if variable == True:
                raise_dashboard_buttons()


        def delete_google_form_note():

            delete_google_form(variable = False)

            def delete_delete_google_form_note():

                canvas.itemconfig(dgfn1, state = 'hidden')
                canvas.itemconfig(dgfn2, state = 'hidden')
                canvas.itemconfig(dgfn3, state = 'hidden')
                canvas.itemconfig(dgfn4, state = 'hidden')
                canvas.itemconfig(dgfn5, state = 'hidden')
                canvas.itemconfig(dgfn6, state = 'hidden')
                canvas.itemconfig(dgfn7, state = 'hidden')
                canvas.itemconfig(dgfn8, state = 'hidden')
                canvas.itemconfig(dgfn9, state = 'hidden')
                canvas.itemconfig(dgfn10, state = 'hidden')
                canvas.itemconfig(dgfn11, state = 'hidden')


                dgfn_button_1.lower()
                dgfn_button_2.lower()

                raise_dashboard_buttons()

            def delete_google_form_actual():
                
                form.delete_form_input_order()
                delete_delete_google_form_note()
                

            dgfn_image_1 = PhotoImage(
                file=relative_to_assets(direc = 'Delete google form note', path = "image_1.png"))
            dgfn1 = canvas.create_image(
                627.0,
                392.0,
                image=dgfn_image_1
            )

            dgfn_label_1 = Label(canvas, image = dgfn_image_1)
            dgfn_label_1.image = dgfn_image_1

            dgfn_image_2 = PhotoImage(
                file=relative_to_assets(direc = 'Delete google form note', path = "image_2.png"))
            dgfn2 = canvas.create_image(
                626.1220703125,
                391.82763671875,
                image=dgfn_image_2
            )

            dgfn_label_2 = Label(canvas, image = dgfn_image_2)
            dgfn_label_2.image = dgfn_image_2

            dgfn_image_3 = PhotoImage(
                file=relative_to_assets(direc = 'Delete google form note', path = "image_3.png"))
            dgfn3 = canvas.create_image(
                626.9638671875,
                391.5947265625,
                image=dgfn_image_3
            )

            dgfn_label_3 = Label(canvas, image = dgfn_image_3)
            dgfn_label_3.image = dgfn_image_3

            dgfn_image_4 = PhotoImage(
                file=relative_to_assets(direc = 'Delete google form note', path = "image_4.png"))
            dgfn4 = canvas.create_image(
                626.9638671875,
                397.42822265625,
                image=dgfn_image_4
            )

            dgfn_label_4 = Label(canvas, image = dgfn_image_4)
            dgfn_label_4.image = dgfn_image_4

            dgfn_image_5 = PhotoImage(
                file=relative_to_assets(direc = 'Delete google form note', path = "image_5.png"))
            dgfn5 = canvas.create_image(
                626.9638671875,
                342.42822265625,
                image=dgfn_image_5
            )

            dgfn_label_5 = Label(canvas, image = dgfn_image_5)
            dgfn_label_5.image = dgfn_image_5

            dgfn_image_6 = PhotoImage(
                file=relative_to_assets(direc = 'Delete google form note', path = "image_6.png"))
            dgfn6 = canvas.create_image(
                626.9638671875,
                452.79345703125,
                image=dgfn_image_6
            )

            dgfn_label_6 = Label(canvas, image = dgfn_image_6)
            dgfn_label_6.image = dgfn_image_6

            dgfn_button_image_1 = PhotoImage(
                file=relative_to_assets(direc = 'Delete google form note', path = "button_1.png"))
            dgfn_button_1 = Button(
                image=dgfn_button_image_1,
                highlightthickness=0,
                command=lambda: delete_delete_google_form_note(),
                relief="flat"
            )
            dgfn_button_1.place(
                x=651.4931640625,
                y=465.5,
                width=60,
                height=17
            )

            dgfn_button_label_1 = Label(canvas, image = dgfn_button_image_1)
            dgfn_button_label_1.image = dgfn_button_image_1

            dgfn_button_image_2 = PhotoImage(
                file=relative_to_assets(direc = 'Delete google form note', path = "button_2.png"))
            dgfn_button_2 = Button(
                image=dgfn_button_image_2,
                highlightthickness=0,
                command=lambda: delete_google_form_actual(),
                relief="flat"
            )
            dgfn_button_2.place(
                x=719.5810546875,
                y=465.5,
                width=60,
                height=17
            )

            dgfn_button_label_2 = Label(canvas, image = dgfn_button_image_2)
            dgfn_button_label_2.image = dgfn_button_image_2

            dgfn7 = canvas.create_text(
                472.0,
                311.0,
                anchor="nw",
                text="Deleting Google Form",
                fill="#D1D3D4",
                font=("Inter", 20 * -1)
            )

            dgfn8 = canvas.create_text(
                472.0,
                357.0,
                anchor="nw",
                text="Are you sure that you would like to delete this",
                fill="#D1D3D4",
                font=("Inter", 11 * -1)
            )

            dgfn9 = canvas.create_text(
                472.0,
                372.0,
                anchor="nw",
                text="google form?",
                fill="#D1D3D4",
                font=("Inter", 11 * -1)
            )

            dgfn10 = canvas.create_text(
                472.0,
                403.0,
                anchor="nw",
                text="You cannot undo this move. The data will be",
                fill="#D1D3D4",
                font=("Inter", 11 * -1)
            )

            dgfn11 = canvas.create_text(
                472.0,
                418.0,
                anchor="nw",
                text="deleted permanently.",
                fill="#D1D3D4",
                font=("Inter", 11 * -1)
            )



        go_image_1 = PhotoImage(
            file=relative_to_assets(direc = 'Google Forms', path = "image_1.png"))
        go1 = canvas.create_image(
            639.0009765625,
            400.0,
            image=go_image_1
        )

        go_label_1 = Label(canvas, image = go_image_1)
        go_label_1.image = go_image_1

        go_image_2 = PhotoImage(
            file=relative_to_assets(direc = 'Google Forms', path = "image_2.png"))
        go2 = canvas.create_image(
            639.484375,
            399.1103515625,
            image=go_image_2
        )

        go_label_2 = Label(canvas, image = go_image_2)
        go_label_2.image = go_image_2

        go_image_3 = PhotoImage(
            file=relative_to_assets(direc = 'Google Forms', path = "image_3.png"))
        go3 = canvas.create_image(
            639.1328125,
            399.78314208984375,
            image=go_image_3
        )

        go_label_3 = Label(canvas, image = go_image_3)
        go_label_3.image = go_image_3

        go4 = canvas.create_rectangle(
            481.1328125,
            289.72802734375,
            797,
            524.2828979492188,
            fill="#171819",
            outline="")

        go5 = canvas.create_rectangle(
            481.1328125,
            289.72802734375,
            797,
            289.72802734375,
            fill="#FFFFFF",
            outline="")

        go_button_image_1 = PhotoImage(
            file=relative_to_assets(direc = 'Google Forms', path = "button_1.png"))
        go_button_1 = Button(
            image=go_button_image_1,
            highlightthickness=0,
            command=lambda: delete_google_form(variable = True),
            relief="flat"
        )
        go_button_1.place(
            x=712.0,
            y=539.7898559570312,
            width=62.0,
            height=17.31134033203125
        )

        go_button_label_1 = Label(canvas, image = go_button_image_1)
        go_button_label_1.image = go_button_image_1

        go6 = canvas.create_rectangle(
            481.1328125,
            524.2828979492188,
            797,
            524.2828979492188,
            fill="#FFFFFF",
            outline="")

        go7 = canvas.create_rectangle(
            481.1328125,
            404.1632995605469,
            797,
            404.1632995605469,
            fill="#FFFFFF",
            outline="")

        go_image_4 = PhotoImage(
            file=relative_to_assets(direc = 'Google Forms', path = "image_4.png"))
        go8 = canvas.create_image(
            640.154296875,
            342.837158203125,
            image=go_image_4
        )

        go_label_4 = Label(canvas, image = go_image_4)
        go_label_4.image = go_image_4


        def copy_to_clipboard_order():
            import subprocess

            event = data['event'][0]
            form_id = data['form_id'][event]['input']

            if form_id == 0:
                output = ""
            elif form_id != 0:
                output = "https://docs.google.com/forms/d/"
                output += form_id
                output += "/edit"
            
            subprocess.run("pbcopy", universal_newlines=True, input=output)
            

        go_button_image_2 = PhotoImage(
            file=relative_to_assets(direc = 'Google Forms', path = "button_2.png"))
        go_button_2 = Button(
            image=go_button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: copy_to_clipboard_order(),
            relief="flat"
        )
        go_button_2.place(
            x=763.412109375,
            y=336.0,
            width=13,
            height=15.0
        )

        go_button_label_2 = Label(canvas, image = go_button_image_2)
        go_button_label_2.image = go_button_image_2

        go_button_image_3 = PhotoImage(
            file=relative_to_assets(direc = 'Google Forms', path = "button_3.png"))
        go_button_3 = Button(
            image=go_button_image_3,
            highlightthickness=0,
            command=lambda: copy_to_clipboard_order(),
            relief="flat"
        )
        go_button_3.place(
            x=499.0,
            y=370.0,
            width=83.30078125,
            height=19.0
        )

        go_button_label_3 = Label(canvas, image = go_button_image_3)
        go_button_label_3.image = go_button_image_3

        go_button_image_4 = PhotoImage(
            file=relative_to_assets(direc = 'Google Forms', path = "button_4.png"))
        go_button_4 = Button(
            image=go_button_image_4,
            highlightthickness=0,
            command=lambda: form.create_form_input_order(),
            relief="flat"
        )
        go_button_4.place(
            x=598.80859375,
            y=370.0,
            width=83.19140625,
            height=19.0
        )

        go_button_label_4 = Label(canvas, image = go_button_image_4)
        go_button_label_4.image = go_button_image_4

        go_button_image_5 = PhotoImage(
            file=relative_to_assets(direc = 'Google Forms', path = "button_5.png"))
        go_button_5 = Button(
            image=go_button_image_5,
            highlightthickness=0,
            command=lambda: delete_google_form_note(),
            relief="flat"
        )
        go_button_5.place(
            x=698.0,
            y=370.0,
            width=83.15234375,
            height=19.0
        )

        go_button_label_5 = Label(canvas, image = go_button_image_5)
        go_button_label_5.image = go_button_image_5

        go_image_5 = PhotoImage(
            file=relative_to_assets(direc = 'Google Forms', path = "image_5.png"))
        go9 = canvas.create_image(
            640.154296875,
            457.22332763671875,
            image=go_image_5
        )

        go_label_5 = Label(canvas, image = go_image_5)
        go_label_5.image = go_image_5


        def copy_to_clipboard_worker():
            import subprocess

            event = data['event'][0]
            form_id = data['form_id'][event]['sell']

            if form_id == 0:
                output = ""
            elif form_id != 0:
                output = "https://docs.google.com/forms/d/"
                output += form_id
                output += "/edit"
            
            subprocess.run("pbcopy", universal_newlines=True, input=output)

            
        go_button_image_6 = PhotoImage(
            file=relative_to_assets(direc = 'Google Forms', path = "button_6.png"))
        go_button_6 = Button(
            image=go_button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: copy_to_clipboard_worker(),
            relief="flat"
        )
        go_button_6.place(
            x=763.001953125,
            y=450.5,
            width=13,
            height=15.0
        )

        go_button_label_6 = Label(canvas, image = go_button_image_6)
        go_button_label_6.image = go_button_image_6

        go_image_6 = PhotoImage(
            file=relative_to_assets(direc = 'Google Forms', path = "image_6.png"))
        go10 = canvas.create_image(
            639.115234375,
            493.5879821777344,
            image=go_image_6
        )

        go_label_6 = Label(canvas, image = go_image_6)
        go_label_6.image = go_image_6

        go11 = canvas.create_text(
            504.5,
            332.5,
            anchor="nw",
            text="Link: https://docs.google.com/forms/d/14NX8cA816CPq",
            fill="#2C2C33",
            font=("Inter", 9 * -1)
        )

        go12 = canvas.create_text(
            504.5,
            343.5,
            anchor="nw",
            text="z2ScefyhTs86kRzw1iU-rkTs_4EsPvg/edit",
            fill="#2C2C33",
            font=("Inter", 9 * -1)
        )

        go13 = canvas.create_text(
            504.5,
            447.0,
            anchor="nw",
            text="Link: https://docs.google.com/forms/d/14NX8cA816CPq",
            fill="#2C2C33",
            font=("Inter", 9 * -1)
        )

        go14 = canvas.create_text(
            504.5,
            458.0,
            anchor="nw",
            text="z2ScefyhTs86kRzw1iU-rkTs_4EsPvg/edit",
            fill="#2C2C33",
            font=("Inter", 9 * -1)
        )

        def refresh_form_links():

            if data['event'] != []:
                
                event = data['event'][0]
                pupil_form = data['form_id'][event]['input']
                worker_form = data['form_id'][event]['sell']

            elif data['event'] == []:

                pupil_form = 0
                worker_form = 0

            pupil_link = ''
            worker_link = ''

            p_first_line = ''
            p_second_line = ''

            w_first_line = ''
            w_second_line = ''

            if pupil_form == 0:
                p_first_line = "Link: Google forms for students to fill has not been"
                p_second_line = "         created yet."
            else:
                p_first_line = "Link: https://docs.google.com/forms/d/"
                p_first_line += pupil_form[0:13]
                p_second_line = pupil_form[13:44]
                p_second_line += "/edit"

            if worker_form == 0:
                w_first_line = "Link: Google forms for workers to input data will be"
                w_second_line = "         created at the day of the event."
            else:
                w_first_line = "Link: https://docs.google.com/forms/d/"
                w_first_line += worker_form[0:13]
                w_second_line += worker_form[13:44]
                w_second_line += "/edit"
                
            canvas.itemconfig(go11, text = p_first_line)
            canvas.itemconfig(go12, text = p_second_line)
            canvas.itemconfig(go13, text = w_first_line)
            canvas.itemconfig(go14, text = w_second_line)
                

        refresh_form_links()

        go15 = canvas.create_text(
            502.0,
            252.0,
            anchor="nw",
            text="Google Forms",
            fill="#D1D3D4",
            font=("Inter", 20 * -1)
        )

        go16 = canvas.create_text(
            499.0,
            306.0,
            anchor="nw",
            text="Google Forms for pupil to enter their orders.",
            fill="#D1D3D4",
            font=("Inter", 11 * -1)
        )

        go17 = canvas.create_text(
            552.0,
            490.0,
            anchor="nw",
            text="Note that this form will be automatically created.",
            fill="#D1D3D4",
            font=("Inter", 7 * -1)
        )

        go18 = canvas.create_text(
            499.0,
            419.0,
            anchor="nw",
            text="Google Forms for workers to input orders.",
            fill="#D1D3D4",
            font=("Inter", 11 * -1)
        )



    def create_event_settings():

        lower_dashboard_buttons()
        check_connection()

        def delete_event_settings():
            
            raise_dashboard_buttons()
        
            canvas.itemconfig(es1, state = 'hidden')
            canvas.itemconfig(es2, state = 'hidden')
            canvas.itemconfig(es3, state = 'hidden')
            canvas.itemconfig(es4, state = 'hidden')
            canvas.itemconfig(es5, state = 'hidden')
            canvas.itemconfig(es6, state = 'hidden')
            canvas.itemconfig(es7, state = 'hidden')
            canvas.itemconfig(es8, state = 'hidden')
            canvas.itemconfig(es9, state = 'hidden')
            canvas.itemconfig(es10, state = 'hidden')
            canvas.itemconfig(es11, state = 'hidden')
            canvas.itemconfig(es12, state = 'hidden')
            canvas.itemconfig(es13, state = 'hidden')
            canvas.itemconfig(es14, state = 'hidden')
            canvas.itemconfig(es15, state = 'hidden')
            canvas.itemconfig(es16, state = 'hidden')
            
            entry_1.lower()

            es_button_1.lower()
            es_button_2.lower()
            es_button_3.lower()
            es_button_4.lower()
            es_button_5.lower()
            
           
        def temp_text(e):
            entry_1.delete(0, END)


        es_image_1 = PhotoImage(
            file=relative_to_assets(direc = 'Event Settings', path = "image_1.png"))
        es1 = canvas.create_image(
            640.0009765625,
            399.03326416015625,
            image=es_image_1
        )

        es_label_1 = Label(canvas, image = es_image_1)
        es_label_1.image = es_image_1

        es_image_2 = PhotoImage(
            file=relative_to_assets(direc = 'Event Settings', path = "image_2.png"))
        es2 = canvas.create_image(
            639.4609375,
            399.2303466796875,
            image=es_image_2
        )

        es_label_2 = Label(canvas, image = es_image_2)
        es_label_2.image = es_image_2

        es_image_3 = PhotoImage(
            file=relative_to_assets(direc = 'Event Settings', path = "image_3.png"))
        es3 = canvas.create_image(
            639.1337890625,
            399.81640625,
            image=es_image_3
        )

        es_label_3 = Label(canvas, image = es_image_3)
        es_label_3.image = es_image_3

        es_image_4 = PhotoImage(
            file=relative_to_assets(direc = 'Event Settings', path = "image_4.png"))
        es4 = canvas.create_image(
            639.1337890625,
            406.76123046875,
            image=es_image_4
        )
        
        es_label_4 = Label(canvas, image = es_image_4)
        es_label_4.image = es_image_4

        es_image_5 = PhotoImage(
            file=relative_to_assets(direc = 'Event Settings', path = "image_5.png"))
        es5 = canvas.create_image(
            639.1328125,
            289.76123046875,
            image=es_image_5
        )

        es_label_5 = Label(canvas, image = es_image_5)
        es_label_5.image = es_image_5

        es_button_image_1 = PhotoImage(
            file=relative_to_assets(direc = 'Event Settings', path = "button_1.png"))
        es_button_1 = Button(
            image=es_button_image_1,
            highlightthickness=0,
            command=lambda: delete_event_settings(),
            relief="flat"
        )
        es_button_1.place(
            x=712.400390625,
            y=539.822998046875,
            width=62,
            height=17
        )

        es_button_label_1 = Label(canvas, image = es_button_image_1)
        es_button_label_1.image = es_button_image_1

        def list_month(data: dict):

            info_month = ['January', 'February', 'March',
                          'April', 'May', 'June',
                          'July', 'August', 'September',
                          'October', 'November', 'December'
                          ]

            current_month = 12 - dt.date.today().month + 1
            final_list = []

            for i in range(current_month):
                month_name = info_month[+i-current_month]
                final_list.append((month_name, i+1))

            return final_list

        def Click_month(e, var):

            nclist = list_month(data = data)
            my_menu = Menu(None, tearoff=0, takefocus=0)

            for (txt, cmd) in nclist:
                exec(f"(my_menu.add_command(label = '{txt}', command = lambda: canvas.itemconfig({es12}, text = '{txt}')))")

            my_menu.tk_popup(e.x_root - 104, e.y_root + 16,entry="0")


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

        es_button_label_2 = Label(canvas, image = es_button_image_2)
        es_button_label_2.image = es_button_image_2

        es_image_6 = PhotoImage(
            file=relative_to_assets(direc = 'Event Settings', path = "image_6.png"))
        es6 = canvas.create_image(
            639.1328125,
            524.316162109375,
            image=es_image_6
        )

        es_label_6 = Label(canvas, image = es_image_6)
        es_label_6.image = es_image_6

        es_image_7 = PhotoImage(
            file=relative_to_assets(direc = 'Event Settings', path = "image_7.png"))
        es7 = canvas.create_image(
            639.1328125,
            407.0386962890625,
            image=es_image_7
        )

        es_label_7 = Label(canvas, image = es_image_7)
        es_label_7.image = es_image_7

        es_image_8 = PhotoImage(
            file=relative_to_assets(direc = 'Event Settings', path = "image_8.png"))
        es8 = canvas.create_image(
            640.1533203125,
            342.870361328125,
            image=es_image_8
        )

        es_label_8 = Label(canvas, image = es_image_8)
        es_label_8.image = es_image_8

        es_image_9 = PhotoImage(
            file=relative_to_assets(direc = 'Event Settings', path = "image_9.png"))
        es9 = canvas.create_image(
            564.1533203125,
            458.7791748046875,
            image=es_image_9
        )

        es_label_9 = Label(canvas, image = es_image_9)
        es_label_9.image = es_image_9

        es_image_10 = PhotoImage(
            file=relative_to_assets(direc = 'Event Settings', path = "image_10.png"))
        es10 = canvas.create_image(
            713.3173828125,
            457.92529296875,
            image=es_image_10
        )

        es_label_10 = Label(canvas, image = es_image_10)
        es_label_10.image = es_image_10

        entry_1 = Entry(
            bd=0,
            bg="#D1D3D4",
            fg="#000000",
            font=("Inter", 11 * -1),
            highlightthickness=0
        )
        entry_1.insert(0,"New name for current event")
        entry_1.pack()
        entry_1.bind("<FocusIn>", temp_text) 
        entry_1.place(
            x=503.0,
            y=335.5,
            width=273.0,
            height=15.0
        )

        es11 = canvas.create_text(
            505.0009765625,
            336.5,
            anchor="nw",
            text="New name for current event",
            fill="#000000",
            font=("Inter", 11 * -1)
        )

        es12 = canvas.create_text(
            540.5009765625,
            452.5,
            anchor="nw",
            text="Month",
            fill="#000000",
            font=("Inter", 11 * -1)
        )

        es13 = canvas.create_text(
            698.5009765625,
            451.5,
            anchor="nw",
            text="Day",
            fill="#000000",
            font=("Inter", 11 * -1)
        )
         

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

        es_button_label_3 = Label(canvas, image = es_button_image_3)
        es_button_label_3.image = es_button_image_3

        def extract_name():

            if data['event'] != []:
                
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

                    outputc = func.change_event_name(name = str(event_name_a))

                else:

                    call_error(error_text = "Unable to change name of current event.")
                    call_error(error_text = "Current event is less than 5 days away.")

            else:

                call_error(error_text = "Unable to change name of current event.")
                call_error(error_text = "There is no existing event to change.")

            delete_event_settings()


        es_button_image_4 = PhotoImage(
            file=relative_to_assets(direc = 'Event Settings', path = "button_4.png"))
        es_button_4 = Button(
            image=es_button_image_4,
            highlightthickness=0,
            command=lambda: extract_name(),
            relief="flat"
        )
        es_button_4.place(
            x=609.5009765625,
            y=370.5,
            width=62,
            height=17
        )

        es_button_label_4 = Label(canvas, image = es_button_image_4)
        es_button_label_4.image = es_button_image_4

        def extract_date():

            if data['event'] != []:

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

                    month_a = canvas.itemcget(es12, 'text')
                    day_a = canvas.itemcget(es13, 'text')

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

                else:

                    call_error(error_text = "Unable to change date of current event.")
                    call_error(error_text = "Current event is less than 5 days away.")

            else:

                call_error(error_text = "Unable to change name of current event.")
                call_error(error_text = "There is no existing event to change.")

            delete_event_settings()


                    

        es_button_image_5 = PhotoImage(
            file=relative_to_assets(direc = 'Event Settings', path = "button_5.png"))
        es_button_5 = Button(
            image=es_button_image_5,
            highlightthickness=0,
            command=lambda: extract_date(),
            relief="flat"
        )
        es_button_5.place(
            x=609.5009765625,
            y=487.0,
            width=62,
            height=17
        )

        es_button_label_5 = Label(canvas, image = es_button_image_5)
        es_button_label_5.image = es_button_image_5

        es14 = canvas.create_text(
            502.5,
            253.5,
            anchor="nw",
            text="Event Settings",
            fill="#D1D3D4",
            font=("Inter", 20 * -1)
        )

        es15 = canvas.create_text(
            499.0,
            304.0,
            anchor="nw",
            text="Change name of Bake Sale event",
            fill="#D1D3D4",
            font=("Inter", 12 * -1)
        )

        es16 = canvas.create_text(
            499.0,
            421.0,
            anchor="nw",
            text="Change date for event",
            fill="#D1D3D4",
            font=("Inter", 12 * -1)
        )




    def create_made_an_error():

        lower_dashboard_buttons()
        check_connection()
        
        def delete_made_an_error(variable: bool):
        
            canvas.itemconfig(mae1, state = 'hidden')
            canvas.itemconfig(mae2, state = 'hidden')
            canvas.itemconfig(mae3, state = 'hidden')
            canvas.itemconfig(mae4, state = 'hidden')
            canvas.itemconfig(mae5, state = 'hidden')
            canvas.itemconfig(mae6, state = 'hidden')
            canvas.itemconfig(mae7, state = 'hidden')
            canvas.itemconfig(mae8, state = 'hidden')
            canvas.itemconfig(mae9, state = 'hidden')
            canvas.itemconfig(mae10, state = 'hidden')
            canvas.itemconfig(mae11, state = 'hidden')
            canvas.itemconfig(mae12, state = 'hidden')
            canvas.itemconfig(mae13, state = 'hidden')
            canvas.itemconfig(mae14, state = 'hidden')
            canvas.itemconfig(mae15, state = 'hidden')
            canvas.itemconfig(mae16, state = 'hidden')
            canvas.itemconfig(mae17, state = 'hidden')
            canvas.itemconfig(mae18, state = 'hidden')
            canvas.itemconfig(mae19, state = 'hidden')
            canvas.itemconfig(mae20, state = 'hidden')
            canvas.itemconfig(mae21, state = 'hidden')
            canvas.itemconfig(mae22, state = 'hidden')
            canvas.itemconfig(mae23, state = 'hidden')
            canvas.itemconfig(mae24, state = 'hidden')
            canvas.itemconfig(mae25, state = 'hidden')
            canvas.itemconfig(mae26, state = 'hidden')
            canvas.itemconfig(mae27, state = 'hidden')
            canvas.itemconfig(mae28, state = 'hidden')
            canvas.itemconfig(mae29, state = 'hidden')
            canvas.itemconfig(mae30, state = 'hidden')
            canvas.itemconfig(mae31, state = 'hidden')
            canvas.itemconfig(mae32, state = 'hidden')
            canvas.itemconfig(mae33, state = 'hidden')
            canvas.itemconfig(mae34, state = 'hidden')

            entry_1.lower()
            entry_2.lower()
            entry_3.lower()
            entry_4.lower()
            entry_5.lower()

            mae_button_1.lower()
            mae_button_2.lower()
            mae_button_3.lower()
            mae_button_4.lower()
            mae_button_5.lower()
            mae_button_6.lower()
            mae_button_7.lower()
            mae_button_8.lower()
            mae_button_9.lower()
            mae_button_10.lower()
            mae_button_11.lower()
            mae_button_12.lower()

            if variable == True:

                global product_name_a
                product_name_a = ''
                raise_dashboard_buttons()


        def temp_text_1(e):
            entry_1.delete(0, END)

        def temp_text_2(e):
            entry_2.delete(0, END)

        def temp_text_3(e):
            entry_3.delete(0, END)

        def temp_text_4(e):
            entry_4.delete(0, END)

        def temp_text_5(e):
            entry_5.delete(0, END)

        def delete_made_an_error_note():

            delete_made_an_error(variable = False)

            def delete_delete_made_an_error_note():

                raise_dashboard_buttons()

                canvas.itemconfig(ddaen1, state = 'hidden')
                canvas.itemconfig(ddaen2, state = 'hidden')
                canvas.itemconfig(ddaen3, state = 'hidden')
                canvas.itemconfig(ddaen4, state = 'hidden')
                canvas.itemconfig(ddaen5, state = 'hidden')
                canvas.itemconfig(ddaen6, state = 'hidden')
                canvas.itemconfig(ddaen7, state = 'hidden')
                canvas.itemconfig(ddaen8, state = 'hidden')
                canvas.itemconfig(ddaen9, state = 'hidden')
                canvas.itemconfig(ddaen10, state = 'hidden')
                canvas.itemconfig(ddaen11, state = 'hidden')
                
                ddaen_button_1.lower()
                ddaen_button_2.lower()


            def delete_the_event_execute():

                global product_name_a
                func.delete_event_product(product = product_name_a)
                product_name_a = ''
                delete_delete_made_an_error_note()    
            

            ddaen_image_1 = PhotoImage(
                file=relative_to_assets(direc = 'Delete an event note', path = "image_1.png"))
            ddaen1 = canvas.create_image(
                640.0,
                400.0,
                image=ddaen_image_1
            )

            ddaen_label_1 = Label(canvas, image = ddaen_image_1)
            ddaen_label_1.image = ddaen_image_1

            ddaen_image_2 = PhotoImage(
                file=relative_to_assets(direc = 'Delete an event note', path = "image_2.png"))
            ddaen2 = canvas.create_image(
                639.7705078125,
                399.0361328125,
                image=image_image_2
            )

            ddaen_label_2 = Label(canvas, image = ddaen_image_2)
            ddaen_label_2.image = ddaen_image_2

            ddaen_image_3 = PhotoImage(
                file=relative_to_assets(direc = 'Delete an event note', path = "image_3.png"))
            ddaen3 = canvas.create_image(
                639.376953125,
                399.58642578125,
                image=ddaen_image_3
            )

            ddaen_label_3 = Label(canvas, image = ddaen_image_3)
            ddaen_label_3.image = ddaen_image_3

            ddaen_image_4 = PhotoImage(
                file=relative_to_assets(direc = 'Delete an event note', path = "image_4.png"))
            ddaen4 = canvas.create_image(
                639.376953125,
                405.4169921875,
                image=ddaen_image_4
            )

            ddaen_label_4 = Label(canvas, image = ddaen_image_4)
            ddaen_label_4.image = ddaen_image_4

            ddaen_image_5 = PhotoImage(
                file=relative_to_assets(direc = 'Delete an event note', path = "image_5.png"))
            ddaen5 = canvas.create_image(
                639.0,
                349.0,
                image=ddaen_image_5
            )

            ddaen_label_5 = Label(canvas, image = ddaen_image_5)
            ddaen_label_5.image = ddaen_image_5

            ddaen_image_6 = PhotoImage(
                file=relative_to_assets(direc = 'Delete an event note', path = "image_6.png"))
            ddaen6 = canvas.create_image(
                639.0,
                461.6171875,
                image=ddaen_image_6
            )

            ddaen_label_6 = Label(canvas, image = ddaen_image_6)
            ddaen_label_6.image = ddaen_image_6

            ddaen_button_image_1 = PhotoImage(
                file=relative_to_assets(direc = 'Delete an event note', path = "button_1.png"))
            ddaen_button_1 = Button(
                image=ddaen_button_image_1,
                highlightthickness=0,
                command=lambda: delete_delete_an_event_note(),
                relief="flat"
            )
            ddaen_button_1.place(
                x=666.5009765625,
                y=475.0,
                width=61,
                height=17
            )

            ddaen_button_label_1 = Label(canvas, image = ddaen_button_image_1)
            ddaen_button_label_1.image = ddaen_button_image_1

            ddaen_button_image_2 = PhotoImage(
                file=relative_to_assets(direc = 'Delete an event note', path = "button_2.png"))
            ddaen_button_2 = Button(
                image=ddaen_button_image_2,
                highlightthickness=0,
                command=lambda: delete_the_event_execute(),
                relief="flat"
            )
            ddaen_button_2.place(
                x=736.0009765625,
                y=475.0,
                width=61,
                height=17
            )

            ddaen_button_label_2 = Label(canvas, image = ddaen_button_image_2)
            ddaen_button_label_2.image = ddaen_button_image_2

            ddaen7 = canvas.create_text(
                481.5009765625,
                317.5,
                anchor="nw",
                text="Removing a product",
                fill="#D1D3D4",
                font=("Inter", 20 * -1)
            )

            ddaen8 = canvas.create_text(
                482.0,
                365.0,
                anchor="nw",
                text="Are you sure that you like to remove this product from",
                fill="#D1D3D4",
                font=("Inter", 11 * -1)
            )

            ddaen9 = canvas.create_text(
                482.0,
                381.0,
                anchor="nw",
                text="this event?",
                fill="#D1D3D4",
                font=("Inter", 11 * -1)
            )

            ddaen10 = canvas.create_text(
                482.0,
                411.0,
                anchor="nw",
                text="You cannot undo this move. The data will be removed",
                fill="#D1D3D4",
                font=("Inter", 11 * -1)
            )

            ddaen11 = canvas.create_text(
                482.0,
                427.0,
                anchor="nw",
                text="permanently.",
                fill="#D1D3D4",
                font=("Inter", 11 * -1)
            )



        mae_image_1 = PhotoImage(
            file=relative_to_assets(direc = 'Made an Error', path = "image_1.png"))
        mae1 = canvas.create_image(
            640.0,
            400.0,
            image=mae_image_1
        )

        mae_label_1 = Label(canvas, image = mae_image_1)
        mae_label_1.image = mae_image_1

        mae_image_2 = PhotoImage(
            file=relative_to_assets(direc = 'Made an Error', path = "image_2.png"))
        mae2 = canvas.create_image(
            639.6435546875,
            426.4892578125,
            image=mae_image_2
        )

        mae_label_2 = Label(canvas, image = mae_image_2)
        mae_label_2.image = mae_image_2

        mae_image_3 = PhotoImage(
            file=relative_to_assets(direc = 'Made an Error', path = "image_3.png"))
        mae3 = canvas.create_image(
            639.36328125,
            399.27783203125,
            image=mae_image_3
        )

        mae_label_3 = Label(canvas, image = mae_image_3)
        mae_label_3.image = mae_image_3

        mae4 = canvas.create_rectangle(
            315.36328125,
            173.0947265625,
            963.6376953125,
            675.573486328125,
            fill="#171819",
            outline="")

        mae_image_4 = PhotoImage(
            file=relative_to_assets(direc = 'Made an Error', path = "image_4.png"))
        mae5 = canvas.create_image(
            639.3623046875,
            173.0947265625,
            image=mae_image_4
        )

        mae_label_4 = Label(canvas, image = mae_image_4)
        mae_label_4.image = mae_image_4

        mae_image_5 = PhotoImage(
            file=relative_to_assets(direc = 'Made an Error', path = "image_5.png"))
        mae6 = canvas.create_image(
            639.3623046875,
            675.573486328125,
            image=mae_image_5
        )

        mae_label_5 = Label(canvas, image = mae_image_5)
        mae_label_5.image = mae_image_5

        mae_image_6 = PhotoImage(
            file=relative_to_assets(direc = 'Made an Error', path = "image_6.png"))
        mae7 = canvas.create_image(
            639.3642578125,
            298.71435546875,
            image=mae_image_6
        )

        mae_label_6 = Label(canvas, image = mae_image_6)
        mae_label_6.image = mae_image_6

        mae_image_7 = PhotoImage(
            file=relative_to_assets(direc = 'Made an Error', path = "image_7.png"))
        mae8 = canvas.create_image(
            639.3623046875,
            549.953857421875,
            image=mae_image_7
        )

        mae_label_7 = Label(canvas, image = mae_image_7)
        mae_label_7.image = mae_image_7

        mae_image_8 = PhotoImage(
            file=relative_to_assets(direc = 'Made an Error', path = "image_8.png"))
        mae9 = canvas.create_image(
            639.3642578125,
            424.334228515625,
            image=mae_image_8
        )

        mae_label_8 = Label(canvas, image = mae_image_8)
        mae_label_8.image = mae_image_8

        mae_image_9 = PhotoImage(
            file=relative_to_assets(direc = 'Made an Error', path = "image_9.png"))
        mae10 = canvas.create_image(
            464.609375,
            212.751708984375,
            image=mae_image_9
        )

        mae_label_9 = Label(canvas, image = mae_image_9)
        mae_label_9.image = mae_image_9

        mae_image_10 = PhotoImage(
            file=relative_to_assets(direc = 'Made an Error', path = "image_10.png"))
        mae11 = canvas.create_image(
            434.0,
            253.0,
            image=mae_image_10
        )

        mae_label_10 = Label(canvas, image = mae_image_10)
        mae_label_10.image = mae_image_10

        mae_image_11 = PhotoImage(
            file=relative_to_assets(direc = 'Made an Error', path = "image_11.png"))
        mae12 = canvas.create_image(
            637.333984375,
            253.0,
            image=mae_image_11
        )

        mae_label_11 = Label(canvas, image = mae_image_11)
        mae_label_11.image = mae_image_11

        mae_image_12 = PhotoImage(
            file=relative_to_assets(direc = 'Made an Error', path = "image_12.png"))
        mae13 = canvas.create_image(
            841.66015625,
            253.0,
            image=mae_image_12
        )

        mae_label_12 = Label(canvas, image = mae_image_12)
        mae_label_12.image = mae_image_12

        mae_image_13 = PhotoImage(
            file=relative_to_assets(direc = 'Made an Error', path = "image_13.png"))
        mae14 = canvas.create_image(
            465.1044921875,
            337.6552734375,
            image=mae_image_13
        )

        mae_label_13 = Label(canvas, image = mae_image_13)
        mae_label_13.image = mae_image_13

        mae_image_14 = PhotoImage(
            file=relative_to_assets(direc = 'Made an Error', path = "image_14.png"))
        mae15 = canvas.create_image(
            434.4951171875,
            377.90380859375,
            image=mae_image_14
        )

        mae_label_14 = Label(canvas, image = mae_image_14)
        mae_label_14.image = mae_image_14

        mae_image_15 = PhotoImage(
            file=relative_to_assets(direc = 'Made an Error', path = "image_15.png"))
        mae16 = canvas.create_image(
            637.830078125,
            377.90380859375,
            image=mae_image_15
        )

        mae_label_15 = Label(canvas, image = mae_image_15)
        mae_label_15.image = mae_image_15

        mae_image_16 = PhotoImage(
            file=relative_to_assets(direc = 'Made an Error', path = "image_16.png"))
        mae17 = canvas.create_image(
            465.1044921875,
            464.75244140625,
            image=mae_image_16
        )

        mae_label_16 = Label(canvas, image = mae_image_16)
        mae_label_16.image = mae_image_16

        mae_image_17 = PhotoImage(
            file=relative_to_assets(direc = 'Made an Error', path = "image_17.png"))
        mae18 = canvas.create_image(
            434.4951171875,
            505.0009765625,
            image=mae_image_17
        )

        mae_label_17 = Label(canvas, image = mae_image_17)
        mae_label_17.image = mae_image_17

        mae_image_18 = PhotoImage(
            file=relative_to_assets(direc = 'Made an Error', path = "image_18.png"))
        mae19 = canvas.create_image(
            465.1044921875,
            590.335205078125,
            image=mae_image_18
        )

        mae_label_18 = Label(canvas, image = mae_image_18)
        mae_label_18.image = mae_image_18

        mae_image_19 = PhotoImage(
            file=relative_to_assets(direc = 'Made an Error', path = "image_19.png"))
        mae20 = canvas.create_image(
            434.4951171875,
            630.583984375,
            image=mae_image_19
        )

        mae_label_19 = Label(canvas, image = mae_image_19)
        mae_label_19.image = mae_image_19

        mae_image_20 = PhotoImage(
            file=relative_to_assets(direc = 'Made an Error', path = "image_20.png"))
        mae21 = canvas.create_image(
            637.830078125,
            630.583984375,
            image=mae_image_20
        )

        mae_label_20 = Label(canvas, image = mae_image_20)
        mae_label_20.image = mae_image_20

        entry_1 = Entry(
            bd=0,
            bg="#D1D3D4",
            fg="#000000",
            font=("Inter", 8 * -1),
            highlightthickness=0
        )
        entry_1.insert(0,"Amount of products made")
        entry_1.pack()
        entry_1.bind("<FocusIn>", temp_text_1) 
        entry_1.place(
            x=547.0,
            y=248.0,
            width=181.0,
            height=12.0
        )

        entry_2 = Entry(
            bd=0,
            bg="#D1D3D4",
            fg="#000000",
            font=("Inter", 8 * -1),
            highlightthickness=0
        )
        entry_2.insert(0,"Cost to make product")
        entry_2.pack()
        entry_2.bind("<FocusIn>", temp_text_2) 
        entry_2.place(
            x=752.0,
            y=248.0,
            width=181.0,
            height=12.0
        )

        entry_3 = Entry(
            bd=0,
            bg="#D1D3D4",
            fg="#000000",
            font=("Inter", 8 * -1),
            highlightthickness=0
        )
        entry_3.insert(0,"Price of product")
        entry_3.pack()
        entry_3.bind("<FocusIn>", temp_text_3) 
        entry_3.place(
            x=547.0,
            y=373.0,
            width=181.0,
            height=12.0
        )

        entry_4 = Entry(
            bd=0,
            bg="#D1D3D4",
            fg="#000000",
            font=("Inter", 8 * -1),
            highlightthickness=0
        )
        entry_4.insert(0,"Minutes (enter 0 if none)")
        entry_4.pack()
        entry_4.bind("<FocusIn>", temp_text_4) 
        entry_4.place(
            x=547.0,
            y=625.0,
            width=181.0,
            height=12.0
        )

        entry_5 = Entry(
            bd=0,
            bg="#D1D3D4",
            fg="#000000",
            font=("Inter", 8 * -1),
            highlightthickness=0
        )
        entry_5.insert(0,"Hours (enter 0 if none)")
        entry_5.pack()
        entry_5.bind("<FocusIn>", temp_text_5) 
        entry_5.place(
            x=345.0,
            y=625.0,
            width=181.0,
            height=12.0
        )

        mae22 = canvas.create_text(
            344.390625,
            248.626953125,
            anchor="nw",
            text="Product Name",
            fill="#000000",
            font=("Inter", 8 * -1)
        )

        mae23 = canvas.create_text(
            550.3916015625,
            248.626953125,
            anchor="nw",
            text="Amount of products made",
            fill="#000000",
            font=("Inter", 8 * -1)
        )

        mae24 = canvas.create_text(
            344.390625,
            373.626953125,
            anchor="nw",
            text="Product Name",
            fill="#000000",
            font=("Inter", 8 * -1)
        )

        mae25 = canvas.create_text(
            344.390625,
            500.626953125,
            anchor="nw",
            text="Product Name",
            fill="#000000",
            font=("Inter", 8 * -1)
        )

        mae26 = canvas.create_text(
            344.890625,
            626.126953125,
            anchor="nw",
            text="Hours (enter 0 if none)",
            fill="#000000",
            font=("Inter", 8 * -1)
        )

        mae27 = canvas.create_text(
            550.3916015625,
            626.126953125,
            anchor="nw",
            text="Minutes (enter 0 if none)",
            fill="#000000",
            font=("Inter", 8 * -1)
        )

        mae28 = canvas.create_text(
            550.3916015625,
            373.626953125,
            anchor="nw",
            text="Price of product",
            fill="#000000",
            font=("Inter", 8 * -1)
        )

        mae29 = canvas.create_text(
            753.8916015625,
            248.626953125,
            anchor="nw",
            text="Cost to make product (enter 0 if none)",
            fill="#000000",
            font=("Inter", 8 * -1)
        )

        mae30 = canvas.create_text(
            347.5,
            119.0,
            anchor="nw",
            text="Made an Error",
            fill="#D1D3D4",
            font=("Inter", 29 * -1)
        )

        def list_rpe(data: dict):

            final_list = []

            if data['event'] != []:
                
                event = data['event'][0]

                for i in data['orders_tofill'][event]:
                    final_list.append(i)

                final_list.remove('special_occasion')

                for i in data['orders_tofill'][event]['special_occasion']:
                    final_list.append(i)

            return final_list

        def Click_remove_product_event(e, var):

            nclist = list_rpe(data = data)
            my_menu = Menu(None, tearoff=0, takefocus=0)

            for txt in nclist:
                exec(f"(my_menu.add_command(label = '{txt}', command = lambda: canvas.itemconfig({mae25}, text = '{txt}')))")

            my_menu.tk_popup(e.x_root - 176, e.y_root + 15,entry="0")


        c_var = StringVar()

        mae_button_image_1 = PhotoImage(
            file=relative_to_assets(direc = 'Made an Error', path = "button_1.png"))
        mae_button_1 = Button(
            image=mae_button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: None,
            relief="flat"
        )
        mae_button_1.bind("<Button-1>", lambda e, var = c_var: Click_remove_product_event(e, var))
        mae_button_1.place(
            x=509.3916015625,
            y=503.126953125,
            width=10,
            height=5
        )

        mae_button_label_1 = Label(canvas, image = mae_button_image_1)
        mae_button_label_1.image = mae_button_image_1

        def list_cpp(data: dict):

            final_list = []

            if data['event'] != []:

                event = data['event'][0]

                for i in data['orders_tofill'][event]:
                    final_list.append(i)

                final_list.remove('special_occasion')

                for i in data['orders_tofill'][event]['special_occasion']:
                    final_list.append(i)

            return final_list

        def Click_change_product_price(e, var):

            nclist = list_cpp(data = data)
            my_menu = Menu(None, tearoff=0, takefocus=0)

            for txt in nclist:
                exec(f"(my_menu.add_command(label = '{txt}', command = lambda: canvas.itemconfig({mae22}, text = '{txt}')))")

            my_menu.tk_popup(e.x_root - 176, e.y_root + 15,entry="0")


        b_var = StringVar()

        mae_button_image_2 = PhotoImage(
            file=relative_to_assets(direc = 'Made an Error', path = "button_2.png"))
        mae_button_2 = Button(
            image=mae_button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: None,
            relief="flat"
        )
        mae_button_2.bind("<Button-1>", lambda e, var = b_var: Click_change_product_price(e, var))
        mae_button_2.place(
            x=509.3916015625,
            y=375.626953125,
            width=10,
            height=5
        )

        mae_button_label_2 = Label(canvas, image = mae_button_image_2)
        mae_button_label_2.image = mae_button_image_2

        mae_button_image_3 = PhotoImage(
            file=relative_to_assets(direc = 'Made an Error', path = "button_3.png"))
        mae_button_3 = Button(
            image=mae_button_image_3,
            highlightthickness=0,
            command=lambda: delete_made_an_error(variable = True),
            relief="flat"
        )
        mae_button_3.place(
            x=805.0,
            y=271.79931640625,
            width=64,
            height=18
        )

        mae_button_label_3 = Label(canvas, image = mae_button_image_3)
        mae_button_label_3.image = mae_button_image_3
        

        def extract_delete_product_made():

            product_name_a = canvas.itemcget(mae22, 'text') #mae24 for removing event product #required to create function and change graphics for error product cost  
            amount_a = entry_1.get()
            cost_a = entry_2.get()

            def cost_pm_check_float():
                try:
                    float(cost_a)
                    return True
                except ValueError:
                    return False

            #checking

            if product_name_a == 'Product Name':
                call_error(error_text = "Please choose a type of product.")
                delete_made_an_error(variable = True)

            if amount_pm.isdigit() == False:
                call_error(error_text = "Please only input integer for 'Error with Numbers of Product Made'.")
                delete_made_an_error(variable = True)

            if cost_pm_check_float == False:
                call_error(error_text = "Please only input integer or decimal for 'Error with Numbers of Product Made'.")
                delete_made_an_error(variable = True)

            func.delete_product_made(product = product_name_a, amount = int(amount_pm))
            func.delete_cost(cost = float(cost_pm))

            delete_add_products_made()
            

        mae_button_image_4 = PhotoImage(
            file=relative_to_assets(direc = 'Made an Error', path = "button_4.png"))
        mae_button_4 = Button(
            image=mae_button_image_4,
            highlightthickness=0,
            command=lambda: extract_delete_product_made(),
            relief="flat"
        )
        mae_button_4.place(
            x=874.0693359375,
            y=271.79931640625,
            width=64,
            height=18
        )

        mae_button_label_4 = Label(canvas, image = mae_button_image_4)
        mae_button_label_4.image = mae_button_image_4

        mae_button_image_5 = PhotoImage(
            file=relative_to_assets(direc = 'Made an Error', path = "button_5.png"))
        mae_button_5 = Button(
            image=mae_button_image_5,
            highlightthickness=0,
            command=lambda: delete_made_an_error(variable = True),
            relief="flat"
        )
        mae_button_5.place(
            x=805.0,
            y=397.29931640625,
            width=64,
            height=18
        )

        mae_button_label_5 = Label(canvas, image = mae_button_image_5)
        mae_button_label_5.image = mae_button_image_5

        def extract_cost_error():
            
            product_name_a = canvas.itemcget(mae24, 'text')
            cost_a = ''

            delete_made_an_error(variable = True)

        mae_button_image_6 = PhotoImage(
            file=relative_to_assets(direc = 'Made an Error', path = "button_6.png"))
        mae_button_6 = Button(
            image=mae_button_image_6,
            highlightthickness=0,
            command=lambda: extract_cost_error(),
            relief="flat"
        )
        mae_button_6.place(
            x=874.0693359375,
            y=397.29931640625,
            width=64,
            height=18
        )

        mae_button_label_6 = Label(canvas, image = mae_button_image_6)
        mae_button_label_6.image = mae_button_image_6

        mae_button_image_7 = PhotoImage(
            file=relative_to_assets(direc = 'Made an Error', path = "button_7.png"))
        mae_button_7 = Button(
            image=mae_button_image_7,
            highlightthickness=0,
            command=lambda: delete_made_an_error(variable = True),
            relief="flat"
        )
        mae_button_7.place(
            x=805.0,
            y=523.29931640625,
            width=64,
            height=18
        )

        mae_button_label_7 = Label(canvas, image = mae_button_image_7)
        mae_button_label_7.image = mae_button_image_7
        

        def extract_remove_product():

            global product_name_a

            product_name_a = canvas.itemcget(mae25, 'text')
            cost = entry_3.get()

            def cost_pm_check_float():
                try:
                    float(cost)
                    return True
                except ValueError:
                    return False

            #checking
            if product_name_a == 'Product Name':
                product_name_a == ''
                call_error(error_text = "Unable to remove product from event. Please select a type of product.")
                delete_made_an_error(variable = True)

            if cost_pm_check_float == False:
                call_error(error_text = "Please only input an integer or decimal for 'Cost to Make Products'.")
                delete_made_an_error(variable = True)


            func.change_product_price(product = product_name_a, price = cost)

            delete_made_an_error_note()
        

        mae_button_image_8 = PhotoImage(
            file=relative_to_assets(direc = 'Made an Error', path = "button_8.png"))
        mae_button_8 = Button(
            image=mae_button_image_8,
            highlightthickness=0,
            command=lambda: extract_remove_product(),
            relief="flat"
        )
        mae_button_8.place(
            x=874.0693359375,
            y=523.29931640625,
            width=64,
            height=18
        )

        mae_button_label_8 = Label(canvas, image = mae_button_image_8)
        mae_button_label_8.image = mae_button_image_8

        mae_button_image_9 = PhotoImage(
            file=relative_to_assets(direc = 'Made an Error', path = "button_9.png"))
        mae_button_9 = Button(
            image=mae_button_image_9,
            highlightthickness=0,
            command=lambda: delete_made_an_error(variable = True),
            relief="flat"
        )
        mae_button_9.place(
            x=805.0,
            y=647.79931640625,
            width=64,
            height=18
        )

        mae_button_label_9 = Label(canvas, image = mae_button_image_9)
        mae_button_label_9.image = mae_button_image_9

        def extract_time_spent_error():

            hour_a = entry_5.get()
            minute_a = entry_4.get()

            if hour_a.isdigit() == False:
                call_error(error_text = "Unable to delete time spent in 'Made an Error.'")
                call_error(error_text = "Please only input an integer for 'Error with Time Spent'.")
                delete_made_an_error(variable = True)

            if minute_a.isdigit() == False:
                call_error(error_text = "Unable to delete time spent in 'Made an Error.'")
                call_error(error_text = "Please only input an integer for 'Error with Time Spent'.")
                delete_made_an_error(variable = True)

            func.delete_time_spent(hour = hour_a, minute = minute_a)

            delete_made_an_error(variable = True)

        mae_button_image_10 = PhotoImage(
            file=relative_to_assets(direc = 'Made an Error', path = "button_10.png"))
        mae_button_10 = Button(
            image=mae_button_image_10,
            highlightthickness=0,
            command=lambda: extract_time_spent_error(),
            relief="flat"
        )
        mae_button_10.place(
            x=874.0693359375,
            y=647.79931640625,
            width=64,
            height=18
        )

        mae_button_label_10 = Label(canvas, image = mae_button_image_10)
        mae_button_label_10.image = mae_button_image_10

        def list_rpm(data: dict):

            final_list = []

            if data['event'] != []:

                event = data['event'][0]

                for i in data['orders_tofill'][event]:
                    final_list.append(i)

                final_list.remove('special_occasion')

                for i in data['orders_tofill'][event]['special_occasion']:
                    final_list.append(i)

            return final_list

        def Click_remove_product_made(e, var):

            nclist = list_rpm(data = data)
            my_menu = Menu(None, tearoff=0, takefocus=0)

            for txt in nclist:
                exec(f"(my_menu.add_command(label = '{txt}', command = lambda: canvas.itemconfig({mae22}, text = '{txt}')))")

            my_menu.tk_popup(e.x_root - 176, e.y_root + 15,entry="0")


        a_var = StringVar()

        mae_button_image_11 = PhotoImage(
            file=relative_to_assets(direc = 'Made an Error', path = "button_11.png"))
        mae_button_11 = Button(
            image=mae_button_image_11,
            highlightthickness=0,
            command=lambda: None,
            relief="flat"
        )
        mae_button_11.bind("<Button-1>", lambda e, var = c_var: Click_remove_product_made(e, var))
        mae_button_11.place(
            x=509.3916015625,
            y=250.626953125,
            width=10,
            height=5
        )

        mae_button_label_11 = Label(canvas, image = mae_button_image_11)
        mae_button_label_11.image = mae_button_image_11

        mae_button_image_12 = PhotoImage(
            file=relative_to_assets(direc = 'Made an Error', path = "button_12.png"))
        mae_button_12 = Button(
            image=mae_button_image_12,
            highlightthickness=0,
            command=lambda: delete_made_an_error(variable = True),
            relief="flat"
        )
        mae_button_12.place(
            x=848.7509765625,
            y=694.5,
            width=79,
            height=22
        )

        mae_button_label_12 = Label(canvas, image = mae_button_image_12)
        mae_button_label_12.image = mae_button_image_12

        mae31 = canvas.create_text(
            350.0,
            205.0,
            anchor="nw",
            text="Error with number of products made",
            fill="#FFFFFF",
            font=("Inter", 13 * -1)
        )

        mae32 = canvas.create_text(
            350.0,
            330.0,
            anchor="nw",
            text="Error with price of product",
            fill="#FFFFFF",
            font=("Inter", 13 * -1)
        )

        mae33 = canvas.create_text(
            350.0,
            457.0,
            anchor="nw",
            text="Removing specific product from event\n",
            fill="#FFFFFF",
            font=("Inter", 13 * -1)
        )

        mae34 = canvas.create_text(
            350.0,
            583.0,
            anchor="nw",
            text="Error with amount of time spent\n\n",
            fill="#FFFFFF",
            font=("Inter", 13 * -1)
        )
            



    def create_display_charts():

        lower_dashboard_buttons()
        check_connection()

        def delete_display_charts():
                
            canvas.itemconfig(dc1, state = 'hidden')
            canvas.itemconfig(dc2, state = 'hidden')
            canvas.itemconfig(dc3, state = 'hidden')
            canvas.itemconfig(dc4, state = 'hidden')
            canvas.itemconfig(dc5, state = 'hidden')
            canvas.itemconfig(dc6, state = 'hidden')
            canvas.itemconfig(dc7, state = 'hidden')
            canvas.itemconfig(dc8, state = 'hidden')
            canvas.itemconfig(dc9, state = 'hidden')
            canvas.itemconfig(dc10, state = 'hidden')
            canvas.itemconfig(dc11, state = 'hidden')
            canvas.itemconfig(dc12, state = 'hidden')
            canvas.itemconfig(dc13, state = 'hidden')
            canvas.itemconfig(dc14, state = 'hidden')
            canvas.itemconfig(dc15, state = 'hidden')


            dc_button_1.lower()
            dc_button_2.lower()
            dc_button_3.lower()
            dc_button_4.lower()
            dc_button_5.lower()
            dc_button_6.lower()
            dc_button_7.lower()
            dc_button_8.lower()
            dc_button_9.lower()

            destroy_display_charts()
            raise_dashboard_buttons()



        dc_image_1 = PhotoImage(
            file=relative_to_assets(direc = 'Display charts', path = "image_1.png"))
        dc1 = canvas.create_image(
            640.0,
            400.0,
            image=dc_image_1
        )

        dc_label_1 = Label(canvas, image = dc_image_1)
        dc_label_1.image = dc_image_1

        dc_image_2 = PhotoImage(
            file=relative_to_assets(direc = 'Display charts', path = "image_2.png"))
        dc2 = canvas.create_image(
            639.0556640625,
            399.523193359375,
            image=dc_image_2
        )

        dc_label_2 = Label(canvas, image = dc_image_2)
        dc_label_2.image = dc_image_2

        dc_image_3 = PhotoImage(
            file=relative_to_assets(direc = 'Display charts', path = "image_3.png"))
        dc3 = canvas.create_image(
            639.0078125,
            399.428466796875,
            image=dc_image_3
        )

        dc_label_3 = Label(canvas, image = dc_image_3)
        dc_label_3.image = dc_image_3

        dc4 = canvas.create_rectangle(
            246.0078125,
            202.24560546875,
            1033,
            642.5537109375,
            fill="#171819",
            outline="")

        dc_image_4 = PhotoImage(
            file=relative_to_assets(direc = 'Display charts', path = "image_4.png"))
        dc5 = canvas.create_image(
            639.005859375,
            202.24560546875,
            image=dc_image_4
        )

        dc_label_4 = Label(canvas, image = dc_image_4)
        dc_label_4.image = dc_image_4

        dc_image_5 = PhotoImage(
            file=relative_to_assets(direc = 'Display charts', path = "image_5.png"))
        dc6 = canvas.create_image(
            639.005859375,
            642.5537109375,
            image=dc_image_5
        )

        dc_label_5 = Label(canvas, image = dc_image_5)
        dc_label_5.image = dc_image_5

        dc_image_6 = PhotoImage(
            file=relative_to_assets(direc = 'Display charts', path = "image_6.png"))
        dc7 = canvas.create_image(
            453.056640625,
            320.20556640625,
            image=dc_image_6
        )

        dc_label_6 = Label(canvas, image = dc_image_6)
        dc_label_6.image = dc_image_6

        dc_image_7 = PhotoImage(
            file=relative_to_assets(direc = 'Display charts', path = "image_7.png"))
        dc8 = canvas.create_image(
            453.79296875,
            531.7265625,
            image=dc_image_7
        )

        dc_label_7 = Label(canvas, image = dc_image_7)
        dc_label_7.image = dc_image_7

        dc_image_8 = PhotoImage(
            file=relative_to_assets(direc = 'Display charts', path = "image_8.png"))
        dc9 = canvas.create_image(
            823.28125,
            320.20556640625,
            image=dc_image_8
        )

        dc_label_8 = Label(canvas, image = dc_image_8)
        dc_label_8.image = dc_image_8

        dc_image_9 = PhotoImage(
            file=relative_to_assets(direc = 'Display charts', path = "image_9.png"))
        dc10 = canvas.create_image(
            824.0185546875,
            531.7265625,
            image=dc_image_9
        )

        dc_label_9 = Label(canvas, image = dc_image_9)
        dc_label_9.image = dc_image_9

        dc_button_image_1 = PhotoImage(
            file=relative_to_assets(direc = 'Display charts', path = "button_1.png"))
        dc_button_1 = Button(
            image=dc_button_image_1,
            highlightthickness=0,
            command=lambda: delete_display_charts(),
            relief="flat"
        )
        dc_button_1.place(
            x=915.5009765625,
            y=663.79931640625,
            width=79,
            height=22
        )

        dc_button_label_1 = Label(canvas, image = dc_button_image_1)
        dc_button_label_1.image = dc_button_image_1

        dc_button_image_2 = PhotoImage(
            file=relative_to_assets(direc = 'Display charts', path = "button_2.png"))
        dc_button_2 = Button(
            image=dc_button_image_2,
            highlightthickness=0,
            command=lambda: create_chart(chart_type = 'revenue', year_over = 'over', data = data, x_cord = 297, y_cord = 250, dashboard = False),
            relief="flat"
        )
        dc_button_2.place(
            x=574.0009765625,
            y=402.5,
            width=44,
            height=8
        )

        dc_button_label_2 = Label(canvas, image = dc_button_image_2)
        dc_button_label_2.image = dc_button_image_2

        dc_button_image_3 = PhotoImage(
            file=relative_to_assets(direc = 'Display charts', path = "button_3.png"))
        dc_button_3 = Button(
            image=dc_button_image_3,
            highlightthickness=0,
            command=lambda: create_chart(chart_type = 'revenue', year_over = 'year', data = data, x_cord = 297, y_cord = 250, dashboard = False),
            relief="flat"
        )
        dc_button_3.place(
            x=532.0009765625,
            y=402.5,
            width=29,
            height=8
        )

        dc_button_label_3 = Label(canvas, image = dc_button_image_3)
        dc_button_label_3.image = dc_button_image_3

        dc_button_image_4 = PhotoImage(
            file=relative_to_assets(direc = 'Display charts', path = "button_4.png"))
        dc_button_4 = Button(
            image=dc_button_image_4,
            highlightthickness=0,
            command=lambda: create_chart(chart_type = 'cost', year_over = 'over', data = data, x_cord = 297, y_cord = 462, dashboard = False),
            relief="flat"
        )
        dc_button_4.place(
            x=571.0009765625,
            y=613.5,
            width=44.0,
            height=8
        )

        dc_button_label_4 = Label(canvas, image = dc_button_image_4)
        dc_button_label_4.image = dc_button_image_4

        dc_button_image_5 = PhotoImage(
            file=relative_to_assets(direc = 'Display charts', path = "button_5.png"))
        dc_button_5 = Button(
            image=dc_button_image_5,
            highlightthickness=0,
            command=lambda: create_chart(chart_type = 'cost', year_over = 'year', data = data, x_cord = 297, y_cord = 462, dashboard = False),
            relief="flat"
        )
        dc_button_5.place(
            x=529.0009765625,
            y=613.5,
            width=29.0,
            height=9.0
        )

        dc_button_label_5 = Label(canvas, image = dc_button_image_5)
        dc_button_label_5.image = dc_button_image_5

        dc_button_image_6 = PhotoImage(
            file=relative_to_assets(direc = 'Display charts', path = "button_6.png"))
        dc_button_6 = Button(
            image=dc_button_image_6,
            highlightthickness=0,
            command=lambda: create_chart(chart_type = 'profit', year_over = 'over', data = data, x_cord = 666, y_cord = 250, dashboard = False),
            relief="flat"
        )
        dc_button_6.place(
            x=944.5009765625,
            y=402.5,
            width=44,
            height=8
        )

        dc_button_label_6 = Label(canvas, image = dc_button_image_6)
        dc_button_label_6.image = dc_button_image_6

        dc_button_image_7 = PhotoImage(
            file=relative_to_assets(direc = 'Display charts', path = "button_7.png"))
        dc_button_7 = Button(
            image=dc_button_image_7,
            highlightthickness=0,
            command=lambda: create_chart(chart_type = 'profit', year_over = 'year', data = data, x_cord = 666, y_cord = 250, dashboard = False),
            relief="flat"
        )
        dc_button_7.place(
            x=902.0009765625,
            y=402.5,
            width=29.0,
            height=8
        )

        dc_button_label_7 = Label(canvas, image = dc_button_image_7)
        dc_button_label_7.image = dc_button_image_7

        dc_button_image_8 = PhotoImage(
            file=relative_to_assets(direc = 'Display charts', path = "button_8.png"))
        dc_button_8 = Button(
            image=dc_button_image_8,
            highlightthickness=0,
            command=lambda: create_chart(chart_type = 'timespent', year_over = 'over', data = data, x_cord = 666, y_cord = 462, dashboard = False),
            relief="flat"
        )
        dc_button_8.place(
            x=941.5009765625,
            y=613.5,
            width=44,
            height=8
        )

        dc_button_label_8 = Label(canvas, image = dc_button_image_8)
        dc_button_label_8.image = dc_button_image_8

        dc_button_image_9 = PhotoImage(
            file=relative_to_assets(direc = 'Display charts', path = "button_9.png"))
        dc_button_9 = Button(
            image=dc_button_image_9,
            highlightthickness=0,
            command=lambda: create_chart(chart_type = 'timespent', year_over = 'year', data = data, x_cord = 666, y_cord = 462, dashboard = False),
            relief="flat"
        )
        dc_button_9.place(
            x=899.0009765625,
            y=613.5,
            width=29.0,
            height=8
        )

        dc_button_label_9 = Label(canvas, image = dc_button_image_9)
        dc_button_label_9.image = dc_button_image_9

        dc11 = canvas.create_text(
            288.5,
            148.5,
            anchor="nw",
            text="Display charts",
            fill="#D1D3D4",
            font=("Inter", 28 * -1)
        )

        dc12 = canvas.create_text(
            287.0,
            219.0,
            anchor="nw",
            text="Revenue",
            fill="#D1D3D4",
            font=("Inter", 18 * -1)
        )

        dc13 = canvas.create_text(
            658.0,
            219.0,
            anchor="nw",
            text="Profit\n",
            fill="#D1D3D4",
            font=("Inter", 18 * -1)
        )

        dc14 = canvas.create_text(
            287.0,
            430.0,
            anchor="nw",
            text="Cost",
            fill="#D1D3D4",
            font=("Inter", 18 * -1)
        )

        dc15 = canvas.create_text(
            658.0,
            430.0,
            anchor="nw",
            text="Time Spent\n\n",
            fill="#D1D3D4",
            font=("Inter", 18 * -1)
        )

        create_chart(chart_type = 'revenue', year_over = 'year', data = data, x_cord = 297, y_cord = 250, dashboard = False)
        create_chart(chart_type = 'cost', year_over = 'year', data = data, x_cord = 297, y_cord = 464, dashboard = False)
        create_chart(chart_type = 'profit', year_over = 'year', data = data, x_cord = 666, y_cord = 250, dashboard = False)
        create_chart(chart_type = 'timespent', year_over = 'year', data = data, x_cord = 666, y_cord = 464, dashboard = False)
        


    ##########################################################################################################################################################################################################

    def product_sold(data: dict, year_over: str):

        dicta = []
        dictb = {}

        if year_over == 'year':
            
            dictb = data['product_sold_YD'].copy()
            del dictb['special_occasion']
            dicta = [(k, v) for k, v in sorted(dictb.items(), key=lambda item: item[1], reverse = True)]
            if len(dicta) > 10:
                for i in range(len(dicta) - 10):
                    del dicta[-1]

        elif year_over == 'over':
            
            dictb = data['product_sold'].copy()
            del dictb['special_occasion']
            dicta = [(k, v) for k, v in sorted(dictb.items(), key=lambda item: item[1], reverse = True)]
            if len(dicta) > 10:
                for i in range(len(dicta) - 10):
                    del dicta[-1]

        return dicta


    def product_sold_so(data: dict, year_over: str):

        dicta = []
        dictb = {}

        if year_over == 'year':
            
            dictb = data['product_sold_YD']['special_occasion'].copy()
            dicta = [(k, v) for k, v in sorted(dictb.items(), key=lambda item: item[1], reverse = True)]
            if len(dicta) > 10:
                for i in range(len(dicta) - 10):
                    del dicta[-1]

        elif year_over == 'over':

            dictb = data['product_sold']['special_occasion'].copy()
            dicta = [(k, v) for k, v in sorted(dictb.items(), key=lambda item: item[1], reverse = True)]
            if len(dicta) > 10:
                for i in range(len(dicta) - 10):
                    del dicta[-1]
            
        return dicta


    def net_loss(data: dict, year_over: str):

        dicta = []

        if year_over == 'year':
            
            dictb = data['net_loss_YD'].copy()
            del dictb['special_occasion']
            dicta = [(k, v) for k, v in sorted(dictb.items(), key=lambda item: item[1], reverse = True)]
            if len(dicta) > 10:
                for i in range(len(dicta) - 10):
                    del dicta[-1]

        elif year_over == 'over':
            
            dictb = data['net_loss'].copy()
            del dictb['special_occasion']
            dicta = [(k, v) for k, v in sorted(dictb.items(), key=lambda item: item[1], reverse = True)]
            if len(dicta) > 10:
                for i in range(len(dicta) - 10):
                    del dicta[-1]

        return dicta


    def net_loss_so(data: dict, year_over: str):

        dicta = []

        if year_over == 'year':

            dictb = data['net_loss_YD']['special_occasion'].copy()
            dicta = [(k, v) for k, v in sorted(dictb.items(), key=lambda item: item[1], reverse = True)]
            if len(dicta) > 10:
                for i in range(len(dicta) - 10):
                    del dicta[-1]

        elif year_over == 'over':

            dictb = data['net_loss']['special_occasion'].copy()
            dicta = [(k, v) for k, v in sorted(dictb.items(), key=lambda item: item[1], reverse = True)]
            if len(dicta) > 10:
                for i in range(len(dicta) - 10):
                    del dicta[-1]

        return dicta



    ##########################################################################################################################################################################################################


    def create_display_tables():

        lower_dashboard_buttons()
        check_connection()

        def delete_display_tables():
            
            raise_dashboard_buttons()
        
            canvas.itemconfig(dc1, state = 'hidden')
            canvas.itemconfig(dc2, state = 'hidden')
            canvas.itemconfig(dc3, state = 'hidden')
            canvas.itemconfig(dc4, state = 'hidden')
            canvas.itemconfig(dc5, state = 'hidden')
            canvas.itemconfig(dc6, state = 'hidden')
            canvas.itemconfig(dc7, state = 'hidden')
            canvas.itemconfig(dc8, state = 'hidden')
            canvas.itemconfig(dc9, state = 'hidden')
            canvas.itemconfig(dc10, state = 'hidden')
            canvas.itemconfig(dc11, state = 'hidden')
            canvas.itemconfig(dc12, state = 'hidden')
            canvas.itemconfig(dc13, state = 'hidden')
            canvas.itemconfig(dc14, state = 'hidden')
            canvas.itemconfig(dc15, state = 'hidden')
            canvas.itemconfig(dc16, state = 'hidden')
            canvas.itemconfig(dc17, state = 'hidden')
            canvas.itemconfig(dc18, state = 'hidden')
            canvas.itemconfig(dc19, state = 'hidden')
            canvas.itemconfig(dc20, state = 'hidden')
            
            canvas.itemconfig(dc21, state = 'hidden')
            canvas.itemconfig(dc22, state = 'hidden')
            canvas.itemconfig(dc23, state = 'hidden')
            canvas.itemconfig(dc24, state = 'hidden')
            canvas.itemconfig(dc25, state = 'hidden')
            canvas.itemconfig(dc26, state = 'hidden')
            canvas.itemconfig(dc27, state = 'hidden')
            canvas.itemconfig(dc28, state = 'hidden')
            canvas.itemconfig(dc29, state = 'hidden')
            canvas.itemconfig(dc30, state = 'hidden')
            canvas.itemconfig(dc31, state = 'hidden')
            canvas.itemconfig(dc32, state = 'hidden')
            canvas.itemconfig(dc33, state = 'hidden')
            canvas.itemconfig(dc34, state = 'hidden')
            canvas.itemconfig(dc35, state = 'hidden')
            canvas.itemconfig(dc36, state = 'hidden')
            canvas.itemconfig(dc37, state = 'hidden')
            canvas.itemconfig(dc38, state = 'hidden')
            canvas.itemconfig(dc39, state = 'hidden')
            canvas.itemconfig(dc40, state = 'hidden')
            
            canvas.itemconfig(dc41, state = 'hidden')
            canvas.itemconfig(dc42, state = 'hidden')
            canvas.itemconfig(dc43, state = 'hidden')
            canvas.itemconfig(dc44, state = 'hidden')
            canvas.itemconfig(dc45, state = 'hidden')
            canvas.itemconfig(dc46, state = 'hidden')
            canvas.itemconfig(dc47, state = 'hidden')
            canvas.itemconfig(dc48, state = 'hidden')
            canvas.itemconfig(dc49, state = 'hidden')
            canvas.itemconfig(dc50, state = 'hidden')
            canvas.itemconfig(dc51, state = 'hidden')
            canvas.itemconfig(dc52, state = 'hidden')
            canvas.itemconfig(dc53, state = 'hidden')
            canvas.itemconfig(dc54, state = 'hidden')
            canvas.itemconfig(dc55, state = 'hidden')
            canvas.itemconfig(dc56, state = 'hidden')
            canvas.itemconfig(dc57, state = 'hidden')
            canvas.itemconfig(dc58, state = 'hidden')
            canvas.itemconfig(dc59, state = 'hidden')
            canvas.itemconfig(dc60, state = 'hidden')
            
            canvas.itemconfig(dc61, state = 'hidden')
            canvas.itemconfig(dc62, state = 'hidden')
            canvas.itemconfig(dc63, state = 'hidden')
            canvas.itemconfig(dc64, state = 'hidden')
            canvas.itemconfig(dc65, state = 'hidden')
            canvas.itemconfig(dc66, state = 'hidden')
            canvas.itemconfig(dc67, state = 'hidden')
            canvas.itemconfig(dc68, state = 'hidden')
            canvas.itemconfig(dc69, state = 'hidden')
            canvas.itemconfig(dc70, state = 'hidden')
            canvas.itemconfig(dc71, state = 'hidden')
            canvas.itemconfig(dc72, state = 'hidden')
            #canvas.itemconfig(dc73, state = 'hidden')
            canvas.itemconfig(dc74, state = 'hidden')
            canvas.itemconfig(dc75, state = 'hidden')
            canvas.itemconfig(dc76, state = 'hidden')
            canvas.itemconfig(dc77, state = 'hidden')
            canvas.itemconfig(dc78, state = 'hidden')
            canvas.itemconfig(dc79, state = 'hidden')
            canvas.itemconfig(dc80, state = 'hidden')
            
            canvas.itemconfig(dc81, state = 'hidden')
            canvas.itemconfig(dc82, state = 'hidden')
            canvas.itemconfig(dc83, state = 'hidden')
            canvas.itemconfig(dc84, state = 'hidden')
            canvas.itemconfig(dc85, state = 'hidden')
            canvas.itemconfig(dc86, state = 'hidden')
            canvas.itemconfig(dc87, state = 'hidden')
            canvas.itemconfig(dc88, state = 'hidden')
            canvas.itemconfig(dc89, state = 'hidden')
            canvas.itemconfig(dc90, state = 'hidden')
            canvas.itemconfig(dc91, state = 'hidden')
            canvas.itemconfig(dc92, state = 'hidden')
            canvas.itemconfig(dc93, state = 'hidden')
            canvas.itemconfig(dc94, state = 'hidden')
            canvas.itemconfig(dc95, state = 'hidden')
            canvas.itemconfig(dc96, state = 'hidden')
            canvas.itemconfig(dc97, state = 'hidden')
            canvas.itemconfig(dc98, state = 'hidden')
            canvas.itemconfig(dc99, state = 'hidden')
            canvas.itemconfig(dc100, state = 'hidden')

            canvas.itemconfig(dc101, state = 'hidden')
            canvas.itemconfig(dc102, state = 'hidden')
            canvas.itemconfig(dc103, state = 'hidden')
            canvas.itemconfig(dc104, state = 'hidden')
            canvas.itemconfig(dc105, state = 'hidden')
            canvas.itemconfig(dc106, state = 'hidden')
            canvas.itemconfig(dc107, state = 'hidden')
            canvas.itemconfig(dc108, state = 'hidden')
            canvas.itemconfig(dc109, state = 'hidden')
            canvas.itemconfig(dc110, state = 'hidden')
            canvas.itemconfig(dc111, state = 'hidden')
            canvas.itemconfig(dc112, state = 'hidden')
            canvas.itemconfig(dc113, state = 'hidden')
            canvas.itemconfig(dc114, state = 'hidden')
            canvas.itemconfig(dc115, state = 'hidden')
            canvas.itemconfig(dc116, state = 'hidden')
            canvas.itemconfig(dc117, state = 'hidden')
            canvas.itemconfig(dc118, state = 'hidden')
            canvas.itemconfig(dc119, state = 'hidden')
            canvas.itemconfig(dc120, state = 'hidden')
            
            canvas.itemconfig(dc121, state = 'hidden')
            canvas.itemconfig(dc122, state = 'hidden')
            canvas.itemconfig(dc123, state = 'hidden')
            canvas.itemconfig(dc124, state = 'hidden')
            canvas.itemconfig(dc125, state = 'hidden')
            canvas.itemconfig(dc126, state = 'hidden')
            canvas.itemconfig(dc127, state = 'hidden')
            canvas.itemconfig(dc128, state = 'hidden')
            canvas.itemconfig(dc129, state = 'hidden')
            canvas.itemconfig(dc130, state = 'hidden')
            canvas.itemconfig(dc131, state = 'hidden')
            canvas.itemconfig(dc132, state = 'hidden')
            canvas.itemconfig(dc133, state = 'hidden')
            canvas.itemconfig(dc134, state = 'hidden')
            canvas.itemconfig(dc135, state = 'hidden')
            canvas.itemconfig(dc136, state = 'hidden')
            canvas.itemconfig(dc137, state = 'hidden')
            canvas.itemconfig(dc138, state = 'hidden')

            dc_button_1.lower()
            dc_button_2.lower()
            dc_button_3.lower()
            dc_button_4.lower()
            dc_button_5.lower()
            dc_button_6.lower()
            dc_button_7.lower()
            dc_button_8.lower()
            dc_button_9.lower()


        list_product_sold_so_year = product_sold_so(data = data, year_over = 'year')
        list_product_sold_so_over = product_sold_so(data = data, year_over = 'over')

        list_net_loss_year = net_loss(data = data, year_over = 'year')
        list_net_loss_so_year = net_loss_so(data = data, year_over = 'year')
        list_net_loss_over = net_loss(data = data, year_over = 'over')
        list_net_loss_so_over = net_loss_so(data = data, year_over = 'over')


        dc_image_1 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_1.png"))
        dc1 = canvas.create_image(
            640.0,
            400.0,
            image=dc_image_1
        )

        dc_label_1 = Label(canvas, image = dc_image_1)
        dc_label_1.image = dc_image_1

        dc_image_2 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_2.png"))
        dc2 = canvas.create_image(
            640.0,
            400.0,
            image=dc_image_2
        )

        dc_label_2 = Label(canvas, image = dc_image_2)
        dc_label_2.image = dc_image_2

        dc_image_3 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_3.png"))
        dc3 = canvas.create_image(
            640.0,
            400.0,
            image=dc_image_3
        )

        dc_label_3 = Label(canvas, image = dc_image_3)
        dc_label_3.image = dc_image_3

        dc4 = canvas.create_rectangle(
            246.0,
            202.0,
            1034.001953125,
            643.0,
            fill="#171819",
            outline="")

        dc_image_4 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_4.png"))
        dc5 = canvas.create_image(
            640.0,
            202.0,
            image=dc_image_4
        )

        dc_label_4 = Label(canvas, image = dc_image_4)
        dc_label_4.image = dc_image_4

        dc_image_5 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_5.png"))
        dc6 = canvas.create_image(
            640.0,
            643.0,
            image=dc_image_5
        )

        dc_label_5 = Label(canvas, image = dc_image_5)
        dc_label_5.image = dc_image_5

        dc_image_6 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_6.png"))
        dc7 = canvas.create_image(
            453.0,
            321.0,
            image=dc_image_6
        )

        dc_label_6 = Label(canvas, image = dc_image_6)
        dc_label_6.image = dc_image_6

        dc_image_7 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_7.png"))
        dc8 = canvas.create_image(
            454.0,
            532.0,
            image=dc_image_7
        )

        dc_label_7 = Label(canvas, image = dc_image_7)
        dc_label_7.image = dc_image_7

        dc_image_8 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_8.png"))
        dc9 = canvas.create_image(
            823.0,
            321.0,
            image=dc_image_8
        )

        dc_label_8 = Label(canvas, image = dc_image_8)
        dc_label_8.image = dc_image_8

        dc_image_9 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_9.png"))
        dc10 = canvas.create_image(
            824.0,
            532.0,
            image=dc_image_9
        )

        dc_label_9 = Label(canvas, image = dc_image_9)
        dc_label_9.image = dc_image_9

        dc_image_10 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_10.png"))
        dc11 = canvas.create_image(
            376.0,
            266.0,
            image=dc_image_10
        )

        dc_label_10 = Label(canvas, image = dc_image_10)
        dc_label_10.image = dc_image_10

        dc_image_11 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_11.png"))
        dc12 = canvas.create_image(
            376.0,
            293.0,
            image=dc_image_11
        )

        dc_label_11 = Label(canvas, image = dc_image_11)
        dc_label_11.image = dc_image_11

        dc_image_12 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_12.png"))
        dc13 = canvas.create_image(
            376.0,
            321.0,
            image=dc_image_12
        )

        dc_label_12 = Label(canvas, image = dc_image_12)
        dc_label_12.image = dc_image_12

        dc_image_13 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_13.png"))
        dc14 = canvas.create_image(
            376.0,
            348.0,
            image=dc_image_13
        )

        dc_label_13 = Label(canvas, image = dc_image_13)
        dc_label_13.image = dc_image_13

        dc_image_14 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_14.png"))
        dc15 = canvas.create_image(
            530.0,
            266.0,
            image=dc_image_14
        )

        dc_label_14 = Label(canvas, image = dc_image_14)
        dc_label_14.image = dc_image_14

        dc_image_15 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_15.png"))
        dc16 = canvas.create_image(
            530.0,
            293.0,
            image=dc_image_15
        )

        dc_label_15 = Label(canvas, image = dc_image_15)
        dc_label_15.image = dc_image_15

        dc_image_16 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_16.png"))
        dc17 = canvas.create_image(
            530.0,
            321.0,
            image=dc_image_16
        )

        dc_label_16 = Label(canvas, image = dc_image_16)
        dc_label_16.image = dc_image_16

        dc_image_17 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_17.png"))
        dc18 = canvas.create_image(
            530.0,
            348.0,
            image=dc_image_17
        )

        dc_label_17 = Label(canvas, image = dc_image_17)
        dc_label_17.image = dc_image_17

        dc_image_18 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_18.png"))
        dc19 = canvas.create_image(
            376.0,
            375.0,
            image=dc_image_18
        )

        dc_label_18 = Label(canvas, image = dc_image_18)
        dc_label_18.image = dc_image_18

        dc_image_19 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_19.png"))
        dc20 = canvas.create_image(
            530.0,
            375.0,
            image=dc_image_19
        )

        dc_label_19 = Label(canvas, image = dc_image_19)
        dc_label_19.image = dc_image_19

        dc_image_20 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_20.png"))
        dc21 = canvas.create_image(
            376.0,
            478.0,
            image=dc_image_20
        )

        dc_label_20 = Label(canvas, image = dc_image_20)
        dc_label_20.image = dc_image_20
        
        dc_image_21 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_21.png"))
        dc22 = canvas.create_image(
            376.0,
            505.0,
            image=dc_image_21
        )

        dc_label_21 = Label(canvas, image = dc_image_21)
        dc_label_21.image = dc_image_21

        dc_image_22 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_22.png"))
        dc23 = canvas.create_image(
            376.0,
            532.0,
            image=dc_image_22
        )

        dc_label_22 = Label(canvas, image = dc_image_22)
        dc_label_22.image = dc_image_22

        dc_image_23 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_23.png"))
        dc24 = canvas.create_image(
            376.0,
            560.0,
            image=dc_image_23
        )

        dc_label_23 = Label(canvas, image = dc_image_23)
        dc_label_23.image = dc_image_23

        dc_image_24 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_24.png"))
        dc25 = canvas.create_image(
            530.0,
            478.0,
            image=dc_image_24
        )

        dc_label_24 = Label(canvas, image = dc_image_24)
        dc_label_24.image = dc_image_24

        dc_image_25 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_25.png"))
        dc26 = canvas.create_image(
            530.0,
            505.0,
            image=dc_image_25
        )

        dc_label_25 = Label(canvas, image = dc_image_25)
        dc_label_25.image = dc_image_25

        dc_image_26 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_26.png"))
        dc27 = canvas.create_image(
            530.0,
            532.0,
            image=dc_image_26
        )

        dc_label_26 = Label(canvas, image = dc_image_26)
        dc_label_26.image = dc_image_26

        dc_image_27 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_27.png"))
        dc28 = canvas.create_image(
            530.0,
            560.0,
            image=dc_image_27
        )

        dc_label_27 = Label(canvas, image = dc_image_27)
        dc_label_27.image = dc_image_27

        dc_image_28 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_28.png"))
        dc29 = canvas.create_image(
            748.0,
            266.0,
            image=dc_image_28
        )

        dc_label_28 = Label(canvas, image = dc_image_28)
        dc_label_28.image = dc_image_28

        dc_image_29 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_29.png"))
        dc30 = canvas.create_image(
            748.0,
            293.0,
            image=dc_image_29
        )

        dc_label_29 = Label(canvas, image = dc_image_29)
        dc_label_29.image = dc_image_29

        dc_image_30 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_30.png"))
        dc31 = canvas.create_image(
            748.0,
            321.0,
            image=dc_image_30
        )

        dc_label_30 = Label(canvas, image = dc_image_30)
        dc_label_30.image = dc_image_30

        dc_image_31 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_31.png"))
        dc32 = canvas.create_image(
            748.0,
            348.0,
            image=dc_image_31
        )

        dc_label_31 = Label(canvas, image = dc_image_31)
        dc_label_31.image = dc_image_31

        dc_image_32 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_32.png"))
        dc33 = canvas.create_image(
            902.001953125,
            266.0,
            image=dc_image_32
        )

        dc_label_32 = Label(canvas, image = dc_image_32)
        dc_label_32.image = dc_image_32

        dc_image_33 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_33.png"))
        dc34 = canvas.create_image(
            902.001953125,
            293.0,
            image=dc_image_33
        )

        dc_label_33 = Label(canvas, image = dc_image_33)
        dc_label_33.image = dc_image_33

        dc_image_34 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_34.png"))
        dc35 = canvas.create_image(
            902.001953125,
            321.0,
            image=dc_image_34
        )

        dc_label_34 = Label(canvas, image = dc_image_34)
        dc_label_34.image = dc_image_34

        dc_image_35 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_35.png"))
        dc36 = canvas.create_image(
            902.001953125,
            348.0,
            image=dc_image_35
        )

        dc_label_35 = Label(canvas, image = dc_image_35)
        dc_label_35.image = dc_image_35

        dc_image_36 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_36.png"))
        dc37 = canvas.create_image(
            748.0,
            375.0,
            image=dc_image_36
        )

        dc_label_36 = Label(canvas, image = dc_image_36)
        dc_label_36.image = dc_image_36

        dc_image_37 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_37.png"))
        dc38 = canvas.create_image(
            902.001953125,
            375.0,
            image=dc_image_37
        )

        dc_label_37 = Label(canvas, image = dc_image_37)
        dc_label_37.image = dc_image_37

        dc_image_38 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_38.png"))
        dc39 = canvas.create_image(
            748.0,
            478.0,
            image=dc_image_38
        )

        dc_label_38 = Label(canvas, image = dc_image_38)
        dc_label_38.image = dc_image_38

        dc_image_39 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_39.png"))
        dc40 = canvas.create_image(
            748.0,
            505.0,
            image=dc_image_39
        )

        dc_label_39 = Label(canvas, image = dc_image_39)
        dc_label_39.image = dc_image_39

        dc_image_40 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_40.png"))
        dc41 = canvas.create_image(
            748.0,
            532.0,
            image=dc_image_40
        )

        dc_label_40 = Label(canvas, image = dc_image_40)
        dc_label_40.image = dc_image_40

        dc_image_41 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_41.png"))
        dc42 = canvas.create_image(
            748.0,
            560.0,
            image=dc_image_41
        )

        dc_label_41 = Label(canvas, image = dc_image_41)
        dc_label_41.image = dc_image_41

        dc_image_42 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_42.png"))
        dc43 = canvas.create_image(
            902.001953125,
            478.0,
            image=dc_image_42
        )

        dc_label_42 = Label(canvas, image = dc_image_42)
        dc_label_42.image = dc_image_42

        dc_image_43 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_43.png"))
        dc44 = canvas.create_image(
            902.001953125,
            505.0,
            image=dc_image_43
        )

        dc_label_43 = Label(canvas, image = dc_image_43)
        dc_label_43.image = dc_image_43

        dc_image_44 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_44.png"))
        dc45 = canvas.create_image(
            902.001953125,
            532.0,
            image=dc_image_44
        )

        dc_label_44 = Label(canvas, image = dc_image_44)
        dc_label_44.image = dc_image_44

        dc_image_45 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_45.png"))
        dc46 = canvas.create_image(
            902.001953125,
            560.0,
            image=dc_image_45
        )

        dc_label_45 = Label(canvas, image = dc_image_45)
        dc_label_45.image = dc_image_45

        dc_image_46 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_46.png"))
        dc47 = canvas.create_image(
            748.0,
            587.0,
            image=dc_image_46
        )

        dc_label_46 = Label(canvas, image = dc_image_46)
        dc_label_46.image = dc_image_46

        dc_image_47 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_47.png"))
        dc48 = canvas.create_image(
            902.001953125,
            587.0,
            image=dc_image_47
        )

        dc_label_47 = Label(canvas, image = dc_image_47)
        dc_label_47.image = dc_image_47

        dc_image_48 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_48.png"))
        dc49 = canvas.create_image(
            376.0,
            587.0,
            image=dc_image_48
        )

        dc_label_48 = Label(canvas, image = dc_image_48)
        dc_label_48.image = dc_image_48

        dc_image_49 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_49.png"))
        dc50 = canvas.create_image(
            530.0,
            587.0,
            image=dc_image_49
        )

        dc_label_49 = Label(canvas, image = dc_image_49)
        dc_label_49.image = dc_image_49

        dc_image_50 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_50.png"))
        dc51 = canvas.create_image(
            748.0,
            587.0,
            image=dc_image_50
        )

        dc_label_50 = Label(canvas, image = dc_image_50)
        dc_label_50.image = dc_image_50

        dc_image_51 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "image_51.png"))
        dc52 = canvas.create_image(
            902.001953125,
            587.0,
            image=dc_image_51
        )

        dc_label_51 = Label(canvas, image = dc_image_51)
        dc_label_51.image = dc_image_51

    ##########################################################################################################################################################################################################

        list_product_sold_year = product_sold(data = data, year_over = 'year')
        list_product_sold_over = product_sold(data = data, year_over = 'over')
        

        def create_product_sold_table(year_over: str):

            cords_info = [260, 287, 315, 342, 369] #for y-coordinates
            
            num_cord_left = [437, 432, 427, 422]
            num_cord_right = [590, 585, 580, 575]
            
            nonlocal dc53
            nonlocal dc54
            nonlocal dc55
            nonlocal dc56
            nonlocal dc57
            nonlocal dc58
            nonlocal dc59
            nonlocal dc60
            nonlocal dc61
            nonlocal dc62
            nonlocal dc63
            nonlocal dc64
            nonlocal dc65
            nonlocal dc66
            nonlocal dc67
            nonlocal dc68
            nonlocal dc69
            nonlocal dc70
            nonlocal dc71
            nonlocal dc72

            for i in range(20):
                
                dc_value = 'dc{}'.format(i + 53)
                exec(f"canvas.itemconfig({dc_value}, text='')")

                
            if year_over == 'year':
                
                for i in range(len(list_product_sold_year)):
                    
                    num1 = 53+i*2
                    num2 = 54+i*2
                    name = list_product_sold_year[i][0]
                    value = list_product_sold_year[i][1]
                    level = round(i/2 - 0.1)
                    y_cord = cords_info[level]

                    #to find if block is left or tight                
                    if (i+1) % 2 == 0:
                        direction = 'right'
                        x_cord_2 = num_cord_right[len(str(value))-1]
                    else:
                        direction = 'left'
                        x_cord_2 = num_cord_left[len(str(value))-1]
                        
                    if len(name) > 20:
                        name = name[0:19] + '...'

                    dc_1_val = f"'{name}'"
                    dc_2_val = f"'{value}'"
                    dc_1_name = f"dc{num1}"
                    dc_2_name = f"dc{num2}"

                    exec(f"canvas.itemconfig({dc_1_name}, text={dc_1_val})")
                    exec(f"canvas.itemconfig({dc_2_name}, text={dc_2_val})")
                    exec(f"canvas.coords({dc_2_name}, {x_cord_2}, {y_cord})")
                    

            elif year_over == 'over':


                for i in range(len(list_product_sold_over)):
                    
                    num1 = 53+i*2
                    num2 = 54+i*2
                    name = list_product_sold_over[i][0]
                    value = list_product_sold_over[i][1]
                    level = round(i/2 - 0.1)
                    y_cord = cords_info[level]

                    #to find if block is left or tight                
                    if (i+1) % 2 == 0:
                        direction = 'right'
                        x_cord_2 = num_cord_right[len(str(value))-1]
                    else:
                        direction = 'left'
                        x_cord_2 = num_cord_left[len(str(value))-1]
                        
                    if len(name) > 20:
                        name = name[0:19] + '...'

                    dc_1_val = f"'{name}'"
                    dc_2_val = f"'{value}'"
                    dc_1_name = f"dc{num1}"
                    dc_2_name = f"dc{num2}"

                    exec(f"canvas.itemconfig({dc_1_name}, text={dc_1_val})")
                    exec(f"canvas.itemconfig({dc_2_name}, text={dc_2_val})")
                    exec(f"canvas.coords({dc_2_name}, {x_cord_2}, {y_cord})")


        dc53 = canvas.create_text(
            308.0,
            260.0,
            anchor="nw",
            text="",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc54 = canvas.create_text(
            433.0,
            260.0,
            anchor="nw",
            text="",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc55 = canvas.create_text(
            462.0,
            260.0,
            anchor="nw",
            text="",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc56 = canvas.create_text(
            587.0,
            260.0,
            anchor="nw",
            text="",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc57 = canvas.create_text(
            308.0,
            287.0,
            anchor="nw",
            text="",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc58 = canvas.create_text(
            436.0,
            287.0,
            anchor="nw",
            text="",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc59 = canvas.create_text(
            462.0,
            287.0,
            anchor="nw",
            text="",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc60 = canvas.create_text(
            593.0,
            287.0,
            anchor="nw",
            text="",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc61 = canvas.create_text(
            308.0,
            315.0,
            anchor="nw",
            text="",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc62 = canvas.create_text(
            440.0,
            315.0,
            anchor="nw",
            text="",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc63 = canvas.create_text(
            462.0,
            315.0,
            anchor="nw",
            text="",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc64 = canvas.create_text(
            593.0,
            315.0,
            anchor="nw",
            text="",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc65 = canvas.create_text(
            308.0,
            342.0,
            anchor="nw",
            text="",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc66 = canvas.create_text(
            436.0,
            342.0,
            anchor="nw",
            text="",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc67 = canvas.create_text(
            462.0,
            342.0,
            anchor="nw",
            text="",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc68 = canvas.create_text(
            593.0,
            342.0,
            anchor="nw",
            text="",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc69 = canvas.create_text(
            308.0,
            369.0,
            anchor="nw",
            text="",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc70 = canvas.create_text(
            440.0,
            369.0,
            anchor="nw",
            text="",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc71 = canvas.create_text(
            462.0,
            369.0,
            anchor="nw",
            text="",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc72 = canvas.create_text(
            593.0,
            369.0,
            anchor="nw",
            text="",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        create_product_sold_table(year_over = 'year')
        
    ##########################################################################################################################################################################################################


        list_net_loss_year = net_loss(data = data, year_over = 'year')
        list_net_loss_over = net_loss(data = data, year_over = 'over')
        

        def create_net_loss_table(year_over: str):

            cords_info = [472, 499, 527, 554, 581] #for y-coordinates
            
            num_cord_left = [437, 432, 427, 422]
            num_cord_right = [590, 585, 580, 575]
            
            nonlocal dc74
            nonlocal dc75
            nonlocal dc76
            nonlocal dc77
            nonlocal dc78
            nonlocal dc79
            nonlocal dc80
            nonlocal dc81
            nonlocal dc82
            nonlocal dc83
            nonlocal dc84
            nonlocal dc85
            nonlocal dc86
            nonlocal dc87
            nonlocal dc88
            nonlocal dc89
            nonlocal dc90
            nonlocal dc91
            nonlocal dc92
            nonlocal dc93

            for i in range(20):
                
                dc_value = 'dc{}'.format(i + 74)
                exec(f"canvas.itemconfig({dc_value}, text='')")

                
            if year_over == 'year':
                
                for i in range(len(list_net_loss_year)):
                    
                    num1 = 74+i*2
                    num2 = 75+i*2
                    name = list_net_loss_year[i][0]
                    value = list_net_loss_year[i][1]
                    level = round(i/2 - 0.1)
                    y_cord = cords_info[level]

                    #to find if block is left or tight                
                    if (i+1) % 2 == 0:
                        direction = 'right'
                        x_cord_2 = num_cord_right[len(str(value))-1]
                    else:
                        direction = 'left'
                        x_cord_2 = num_cord_left[len(str(value))-1]
                        
                    if len(name) > 20:
                        name = name[0:19] + '...'

                    dc_1_val = f"'{name}'"
                    dc_2_val = f"'{value}'"
                    dc_1_name = f"dc{num1}"
                    dc_2_name = f"dc{num2}"

                    exec(f"canvas.itemconfig({dc_1_name}, text={dc_1_val})")
                    exec(f"canvas.itemconfig({dc_2_name}, text={dc_2_val})")
                    exec(f"canvas.coords({dc_2_name}, {x_cord_2}, {y_cord})")
                    

            elif year_over == 'over':


                for i in range(len(list_net_loss_over)):
                    
                    num1 = 74+i*2
                    num2 = 75+i*2
                    name = list_net_loss_over[i][0]
                    value = list_net_loss_over[i][1]
                    level = round(i/2 - 0.1)
                    y_cord = cords_info[level]

                    #to find if block is left or tight                
                    if (i+1) % 2 == 0:
                        direction = 'right'
                        x_cord_2 = num_cord_right[len(str(value))-1]
                    else:
                        direction = 'left'
                        x_cord_2 = num_cord_left[len(str(value))-1]
                        
                    if len(name) > 20:
                        name = name[0:19] + '...'

                    dc_1_val = f"'{name}'"
                    dc_2_val = f"'{value}'"
                    dc_1_name = f"dc{num1}"
                    dc_2_name = f"dc{num2}"

                    exec(f"canvas.itemconfig({dc_1_name}, text={dc_1_val})")
                    exec(f"canvas.itemconfig({dc_2_name}, text={dc_2_val})")
                    exec(f"canvas.coords({dc_2_name}, {x_cord_2}, {y_cord})")



        dc74 = canvas.create_text(
            308.0,
            472.0,
            anchor="nw",
            text="Cookies",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc75 = canvas.create_text(
            434.0,
            472.0,
            anchor="nw",
            text="32",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc76 = canvas.create_text(
            462.0,
            472.0,
            anchor="nw",
            text="Balloon",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc77 = canvas.create_text(
            587.0,
            472.0,
            anchor="nw",
            text="22",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )
        
        dc78 = canvas.create_text(
            308.0,
            499.0,
            anchor="nw",
            text="Amogus",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc79 = canvas.create_text(
            437.0,
            499.0,
            anchor="nw",
            text="11",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc80 = canvas.create_text(
            462.0,
            499.0,
            anchor="nw",
            text="Chocolate Chips Cookie",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc81 = canvas.create_text(
            593.0,
            499.0,
            anchor="nw",
            text="7",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )
        

        dc82 = canvas.create_text(
            308.0,
            527.0,
            anchor="nw",
            text="McDonalds",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc83 = canvas.create_text(
            440.0,
            527.0,
            anchor="nw",
            text="9",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc84 = canvas.create_text(
            462.0,
            527.0,
            anchor="nw",
            text="Rose",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc85 = canvas.create_text(
            593.0,
            527.0,
            anchor="nw",
            text="2",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc86 = canvas.create_text(
            308.0,
            554.0,
            anchor="nw",
            text="Coke",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc87 = canvas.create_text(
            436.0,
            554.0,
            anchor="nw",
            text="12",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc88 = canvas.create_text(
            462.0,
            554.0,
            anchor="nw",
            text="Sprite",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc89 = canvas.create_text(
            593.0,
            554.0,
            anchor="nw",
            text="3",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )    

        dc90 = canvas.create_text(
            308.0,
            581.0,
            anchor="nw",
            text="Sus",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc91 = canvas.create_text(
            440.0,
            581.0,
            anchor="nw",
            text="2",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc92 = canvas.create_text(
            462.0,
            581.0,
            anchor="nw",
            text="Reee",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc93 = canvas.create_text(
            593.0,
            581.0,
            anchor="nw",
            text="3",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        create_net_loss_table(year_over = 'year')

    ##########################################################################################################################################################################################################


        list_product_sold_so_year = product_sold_so(data = data, year_over = 'year')
        list_product_sold_so_over = product_sold_so(data = data, year_over = 'over')
        

        def create_product_sold_so_table(year_over: str):

            cords_info = [260, 287, 315, 342, 369] #for y-coordinates
            
            num_cord_left = [812, 807, 802, 797] 
            num_cord_right = [965, 960, 955, 950] 
            
            nonlocal dc94
            nonlocal dc95
            nonlocal dc96
            nonlocal dc97
            nonlocal dc98
            nonlocal dc99
            nonlocal dc100
            nonlocal dc101
            nonlocal dc102
            nonlocal dc103
            nonlocal dc104
            nonlocal dc105
            nonlocal dc106
            nonlocal dc107
            nonlocal dc108
            nonlocal dc109
            nonlocal dc110
            nonlocal dc111
            nonlocal dc112
            nonlocal dc113

            for i in range(20):
                
                dc_value = 'dc{}'.format(i + 94)
                exec(f"canvas.itemconfig({dc_value}, text='')")

                
            if year_over == 'year':
                
                for i in range(len(list_product_sold_so_year)):
                    
                    num1 = 94+i*2
                    num2 = 95+i*2
                    name = list_product_sold_so_year[i][0]
                    value = list_product_sold_so_year[i][1]
                    level = round(i/2 - 0.1)
                    y_cord = cords_info[level]

                    #to find if block is left or tight                
                    if (i+1) % 2 == 0:
                        direction = 'right'
                        x_cord_2 = num_cord_right[len(str(value))-1]
                    else:
                        direction = 'left'
                        x_cord_2 = num_cord_left[len(str(value))-1]
                        
                    if len(name) > 20:
                        name = name[0:19] + '...'

                    dc_1_val = f"'{name}'"
                    dc_2_val = f"'{value}'"
                    dc_1_name = f"dc{num1}"
                    dc_2_name = f"dc{num2}"

                    exec(f"canvas.itemconfig({dc_1_name}, text={dc_1_val})")
                    exec(f"canvas.itemconfig({dc_2_name}, text={dc_2_val})")
                    exec(f"canvas.coords({dc_2_name}, {x_cord_2}, {y_cord})")
                    

            elif year_over == 'over':


                for i in range(len(list_product_sold_so_over)):
                    
                    num1 = 94+i*2
                    num2 = 95+i*2
                    name = list_product_sold_so_over[i][0]
                    value = list_product_sold_so_over[i][1]
                    level = round(i/2 - 0.1)
                    y_cord = cords_info[level]

                    #to find if block is left or tight                
                    if (i+1) % 2 == 0:
                        direction = 'right'
                        x_cord_2 = num_cord_right[len(str(value))-1]
                    else:
                        direction = 'left'
                        x_cord_2 = num_cord_left[len(str(value))-1]
                        
                    if len(name) > 20:
                        name = name[0:19] + '...'

                    dc_1_val = f"'{name}'"
                    dc_2_val = f"'{value}'"
                    dc_1_name = f"dc{num1}"
                    dc_2_name = f"dc{num2}"

                    exec(f"canvas.itemconfig({dc_1_name}, text={dc_1_val})")
                    exec(f"canvas.itemconfig({dc_2_name}, text={dc_2_val})")
                    exec(f"canvas.coords({dc_2_name}, {x_cord_2}, {y_cord})")


        dc94 = canvas.create_text(
            680.0,
            260.0,
            anchor="nw",
            text="Cookies",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc95 = canvas.create_text(
            805.001953125,
            260.0,
            anchor="nw",
            text="32",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc96 = canvas.create_text(
            834.001953125,
            260.0,
            anchor="nw",
            text="Balloon",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc97 = canvas.create_text(
            959.001953125,
            260.0,
            anchor="nw",
            text="22",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc98 = canvas.create_text(
            680.0,
            287.0,
            anchor="nw",
            text="Amogus",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc99 = canvas.create_text(
            808.001953125,
            287.0,
            anchor="nw",
            text="11",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc100 = canvas.create_text(
            834.001953125,
            287.0,
            anchor="nw",
            text="Chocolate Chips Cookie",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc101 = canvas.create_text(
            965.001953125,
            287.0,
            anchor="nw",
            text="7",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc102 = canvas.create_text(
            680.0,
            315.0,
            anchor="nw",
            text="McDonalds",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc103 = canvas.create_text(
            812.001953125,
            315.0,
            anchor="nw",
            text="9",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc104 = canvas.create_text(
            834.001953125,
            315.0,
            anchor="nw",
            text="Rose",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc105 = canvas.create_text(
            965.001953125,
            315.0,
            anchor="nw",
            text="2",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc106 = canvas.create_text(
            680.0,
            342.0,
            anchor="nw",
            text="Coke",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc107 = canvas.create_text(
            808.001953125,
            342.0,
            anchor="nw",
            text="12",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc108 = canvas.create_text(
            834.001953125,
            342.0,
            anchor="nw",
            text="Sprite",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc109 = canvas.create_text(
            965.001953125,
            342.0,
            anchor="nw",
            text="3",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc110 = canvas.create_text(
            680.0,
            369.0,
            anchor="nw",
            text="Sus",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc111 = canvas.create_text(
            812.001953125,
            369.0,
            anchor="nw",
            text="2",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc112 = canvas.create_text(
            834.001953125,
            369.0,
            anchor="nw",
            text="Reee",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc113 = canvas.create_text(
            965.001953125,
            369.0,
            anchor="nw",
            text="3",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        create_product_sold_so_table(year_over = 'year')

    ##########################################################################################################################################################################################################


        list_net_loss_so_year = net_loss_so(data = data, year_over = 'year')
        list_net_loss_so_over = net_loss_so(data = data, year_over = 'over')
        

        def create_net_loss_so_table(year_over: str):

            cords_info = [472, 499, 527, 554, 581] #for y-coordinates
            
            num_cord_left = [812, 807, 802, 797] 
            num_cord_right = [965, 960, 955, 950] 
            
            nonlocal dc114
            nonlocal dc115
            nonlocal dc116
            nonlocal dc117
            nonlocal dc118
            nonlocal dc119
            nonlocal dc120
            nonlocal dc121
            nonlocal dc122
            nonlocal dc123
            nonlocal dc124
            nonlocal dc125
            nonlocal dc126
            nonlocal dc127
            nonlocal dc128
            nonlocal dc129
            nonlocal dc130
            nonlocal dc131
            nonlocal dc132
            nonlocal dc133

            for i in range(20):
                
                dc_value = 'dc{}'.format(i + 114)
                exec(f"canvas.itemconfig({dc_value}, text='')")

                
            if year_over == 'year':
                
                for i in range(len(list_net_loss_so_year)):
                    
                    num1 = 114+i*2
                    num2 = 115+i*2
                    name = list_net_loss_so_year[i][0]
                    value = list_net_loss_so_year[i][1]
                    level = round(i/2 - 0.1)
                    y_cord = cords_info[level]

                    #to find if block is left or tight                
                    if (i+1) % 2 == 0:
                        direction = 'right'
                        x_cord_2 = num_cord_right[len(str(value))-1]
                    else:
                        direction = 'left'
                        x_cord_2 = num_cord_left[len(str(value))-1]
                        
                    if len(name) > 20:
                        name = name[0:19] + '...'

                    dc_1_val = f"'{name}'"
                    dc_2_val = f"'{value}'"
                    dc_1_name = f"dc{num1}"
                    dc_2_name = f"dc{num2}"

                    exec(f"canvas.itemconfig({dc_1_name}, text={dc_1_val})")
                    exec(f"canvas.itemconfig({dc_2_name}, text={dc_2_val})")
                    exec(f"canvas.coords({dc_2_name}, {x_cord_2}, {y_cord})")
                    

            elif year_over == 'over':


                for i in range(len(list_net_loss_so_over)):
                    
                    num1 = 114+i*2
                    num2 = 115+i*2
                    name = list_net_loss_so_over[i][0]
                    value = list_net_loss_so_over[i][1]
                    level = round(i/2 - 0.1)
                    y_cord = cords_info[level]

                    #to find if block is left or tight                
                    if (i+1) % 2 == 0:
                        direction = 'right'
                        x_cord_2 = num_cord_right[len(str(value))-1]
                    else:
                        direction = 'left'
                        x_cord_2 = num_cord_left[len(str(value))-1]
                        
                    if len(name) > 20:
                        name = name[0:19] + '...'

                    dc_1_val = f"'{name}'"
                    dc_2_val = f"'{value}'"
                    dc_1_name = f"dc{num1}"
                    dc_2_name = f"dc{num2}"

                    exec(f"canvas.itemconfig({dc_1_name}, text={dc_1_val})")
                    exec(f"canvas.itemconfig({dc_2_name}, text={dc_2_val})")
                    exec(f"canvas.coords({dc_2_name}, {x_cord_2}, {y_cord})")



        dc114 = canvas.create_text(
            680.0,
            472.0,
            anchor="nw",
            text="Cookies",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc115 = canvas.create_text(
            806.001953125,
            472.0,
            anchor="nw",
            text="32",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc116 = canvas.create_text(
            834.001953125,
            472.0,
            anchor="nw",
            text="Balloon",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc117 = canvas.create_text(
            959.001953125,
            472.0,
            anchor="nw",
            text="22",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc118 = canvas.create_text(
            680.0,
            499.0,
            anchor="nw",
            text="Amogus",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc119 = canvas.create_text(
            809.001953125,
            499.0,
            anchor="nw",
            text="11",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc120 = canvas.create_text(
            834.001953125,
            499.0,
            anchor="nw",
            text="Chocolate Chips Cookie",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc121 = canvas.create_text(
            965.001953125,
            499.0,
            anchor="nw",
            text="7",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc122 = canvas.create_text(
            680.0,
            527.0,
            anchor="nw",
            text="McDonalds",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc123 = canvas.create_text(
            812.001953125,
            527.0,
            anchor="nw",
            text="9",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc124 = canvas.create_text(
            834.001953125,
            527.0,
            anchor="nw",
            text="Rose",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc125 = canvas.create_text(
            965.001953125,
            527.0,
            anchor="nw",
            text="2",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc126 = canvas.create_text(
            680.0,
            554.0,
            anchor="nw",
            text="Coke",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc127 = canvas.create_text(
            808.001953125,
            554.0,
            anchor="nw",
            text="12",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc128 = canvas.create_text(
            834.001953125,
            554.0,
            anchor="nw",
            text="Sprite",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc129 = canvas.create_text(
            965.001953125,
            554.0,
            anchor="nw",
            text="3",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )


        dc130 = canvas.create_text(
            680.0,
            581.0,
            anchor="nw",
            text="Sus",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc131 = canvas.create_text(
            812.001953125,
            581.0,
            anchor="nw",
            text="2",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc132 = canvas.create_text(
            834.001953125,
            581.0,
            anchor="nw",
            text="Reee",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        dc133 = canvas.create_text(
            965.001953125,
            581.0,
            anchor="nw",
            text="3",
            fill="#D1D3D4",
            font=("Inter", 10 * -1)
        )

        create_net_loss_so_table(year_over = 'year')


    ##########################################################################################################################################################################################################


        dc_button_image_1 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "button_1.png"))
        dc_button_1 = Button(
            image=dc_button_image_1,
            highlightthickness=0,
            command=lambda: delete_display_tables(),
            relief="flat"
        )
        dc_button_1.place(
            x=915.501953125,
            y=663.79931640625,
            width=79,
            height=22
        )

        dc_button_label_1 = Label(canvas, image = dc_button_image_1)
        dc_button_label_1.image = dc_button_image_1

        dc_button_image_2 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "button_2.png"))
        dc_button_2 = Button(
            image=dc_button_image_2,
            highlightthickness=0,
            command=lambda: create_net_loss_so_table(year_over = 'over'),
            relief="flat"
        )
        dc_button_2.place(
            x=941.501953125,
            y=613.5,
            width=43,
            height=8
        )

        dc_button_label_2 = Label(canvas, image = dc_button_image_2)
        dc_button_label_2.image = dc_button_image_2

        dc_button_image_3 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "button_3.png"))
        dc_button_3 = Button(
            image=dc_button_image_3,
            highlightthickness=0,
            command=lambda: create_net_loss_so_table(year_over = 'year'),
            relief="flat"
        )
        dc_button_3.place(
            x=899.001953125,
            y=613.5,
            width=29,
            height=8
        )

        dc_button_label_3 = Label(canvas, image = dc_button_image_3)
        dc_button_label_3.image = dc_button_image_3

        dc_button_image_4 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "button_4.png"))
        dc_button_4 = Button(
            image=dc_button_image_4,
            highlightthickness=0,
            command=lambda: create_product_sold_so_table(year_over = 'over'),
            relief="flat"
        )
        dc_button_4.place(
            x=945.001953125,
            y=402.5,
            width=43,
            height=8
        )

        dc_button_label_4 = Label(canvas, image = dc_button_image_4)
        dc_button_label_4.image = dc_button_image_4

        dc_button_image_5 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "button_5.png"))
        dc_button_5 = Button(
            image=dc_button_image_5,
            highlightthickness=0,
            command=lambda: create_product_sold_so_table(year_over = 'year'),
            relief="flat"
        )
        dc_button_5.place(
            x=902.501953125,
            y=402.5,
            width=29,
            height=8
        )

        dc_button_label_5 = Label(canvas, image = dc_button_image_5)
        dc_button_label_5.image = dc_button_image_5

        dc_button_image_6 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "button_6.png"))
        dc_button_6 = Button(
            image=dc_button_image_6,
            highlightthickness=0,
            command=lambda: create_product_sold_table(year_over = 'over'),
            relief="flat"
        )
        dc_button_6.place(
            x=574.5,
            y=402.5,
            width=43,
            height=8
        )

        dc_button_label_6 = Label(canvas, image = dc_button_image_6)
        dc_button_label_6.image = dc_button_image_6

        dc_button_image_7 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "button_7.png"))
        dc_button_7 = Button(
            image=dc_button_image_7,
            highlightthickness=0,
            command=lambda: create_product_sold_table(year_over = 'year'),
            relief="flat"
        )
        dc_button_7.place(
            x=532.0,
            y=402.5,
            width=29,
            height=8
        )

        dc_button_label_7 = Label(canvas, image = dc_button_image_7)
        dc_button_label_7.image = dc_button_image_7

        dc_button_image_8 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "button_8.png"))
        dc_button_8 = Button(
            image=dc_button_image_8,
            highlightthickness=0,
            command=lambda: create_net_loss_table(year_over = 'over'),
            relief="flat"
        )
        dc_button_8.place(
            x=571.5,
            y=613.5,
            width=43,
            height=8
        )

        dc_button_label_8 = Label(canvas, image = dc_button_image_8)
        dc_button_label_8.image = dc_button_image_8

        dc_button_image_9 = PhotoImage(
            file=relative_to_assets(direc = 'Display Tables', path = "button_9.png"))
        dc_button_9 = Button(
            image=dc_button_image_9,
            highlightthickness=0,
            command=lambda: create_net_loss_table(year_over = 'year'),
            relief="flat"
        )
        dc_button_9.place(
            x=529.0,
            y=613.5,
            width=29,
            height=8
        )

        dc_button_label_9 = Label(canvas, image = dc_button_image_9)
        dc_button_label_9.image = dc_button_image_9

        dc134 = canvas.create_text(
            288.0,
            221.0,
            anchor="nw",
            text="Product sold - Common",
            fill="#FFFFFF",
            font=("Inter", 16 * -1)
        )

        dc135 = canvas.create_text(
            658.0,
            221.0,
            anchor="nw",
            text="Product sold - Special Occasion",
            fill="#FFFFFF",
            font=("Inter", 16 * -1)
        )

        dc136 = canvas.create_text(
            287.0,
            431.0,
            anchor="nw",
            text="Net loss - Common",
            fill="#FFFFFF",
            font=("Inter", 16 * -1)
        )

        dc137 = canvas.create_text(
            657.0,
            431.0,
            anchor="nw",
            text="Net loss - Special Occasion",
            fill="#FFFFFF",
            font=("Inter", 16 * -1)
        )

        dc138 = canvas.create_text(
            287.0,
            148.0,
            anchor="nw",
            text="Display tables",
            fill="#D1D3D4",
            font=("Inter", 29 * -1)
        )



    def create_delete_product_type():

        lower_dashboard_buttons()
        check_connection()

        def delete_delete_product_type(variable: bool):
        
            canvas.itemconfig(dpt1, state = 'hidden')
            canvas.itemconfig(dpt2, state = 'hidden')
            canvas.itemconfig(dpt3, state = 'hidden')
            canvas.itemconfig(dpt4, state = 'hidden')
            canvas.itemconfig(dpt5, state = 'hidden')
            canvas.itemconfig(dpt6, state = 'hidden')
            canvas.itemconfig(dpt7, state = 'hidden')
            canvas.itemconfig(dpt8, state = 'hidden')
            canvas.itemconfig(dpt9, state = 'hidden')
            canvas.itemconfig(dpt10, state = 'hidden')
            canvas.itemconfig(dpt11, state = 'hidden')

            dpt_button_1.lower()
            dpt_button_2.lower()
            dpt_button_3.lower()


            if variable == True:
                global product_name_a
                product_name_a = ""
                raise_dashboard_buttons()


        def delete_product_type_note():

            delete_delete_product_type(variable = False)

            def delete_delete_product_type_note():

                raise_dashboard_buttons()

                canvas.itemconfig(ddaen1, state = 'hidden')
                canvas.itemconfig(ddaen2, state = 'hidden')
                canvas.itemconfig(ddaen3, state = 'hidden')
                canvas.itemconfig(ddaen4, state = 'hidden')
                canvas.itemconfig(ddaen5, state = 'hidden')
                canvas.itemconfig(ddaen6, state = 'hidden')
                canvas.itemconfig(ddaen7, state = 'hidden')
                canvas.itemconfig(ddaen8, state = 'hidden')
                canvas.itemconfig(ddaen9, state = 'hidden')
                canvas.itemconfig(ddaen10, state = 'hidden')
                canvas.itemconfig(ddaen11, state = 'hidden')
                

                ddaen_button_1.lower()
                ddaen_button_2.lower()


            def delete_product_type():

                global product_name_a
                func.delete_new_product(del_product = product_name_a)
                delete_delete_product_type_note()


            ddaen_image_1 = PhotoImage(
                file=relative_to_assets(direc = 'Delete an event note', path = "image_1.png"))
            ddaen1 = canvas.create_image(
                640.0,
                400.0,
                image=ddaen_image_1
            )

            ddaen_label_1 = Label(canvas, image = ddaen_image_1)
            ddaen_label_1.image = ddaen_image_1

            ddaen_image_2 = PhotoImage(
                file=relative_to_assets(direc = 'Delete an event note', path = "image_2.png"))
            ddaen2 = canvas.create_image(
                639.7705078125,
                399.0361328125,
                image=image_image_2
            )

            ddaen_label_2 = Label(canvas, image = ddaen_image_2)
            ddaen_label_2.image = ddaen_image_2

            ddaen_image_3 = PhotoImage(
                file=relative_to_assets(direc = 'Delete an event note', path = "image_3.png"))
            ddaen3 = canvas.create_image(
                639.376953125,
                399.58642578125,
                image=ddaen_image_3
            )

            ddaen_label_3 = Label(canvas, image = ddaen_image_3)
            ddaen_label_3.image = ddaen_image_3

            ddaen_image_4 = PhotoImage(
                file=relative_to_assets(direc = 'Delete an event note', path = "image_4.png"))
            ddaen4 = canvas.create_image(
                639.376953125,
                405.4169921875,
                image=ddaen_image_4
            )

            ddaen_label_4 = Label(canvas, image = ddaen_image_4)
            ddaen_label_4.image = ddaen_image_4

            ddaen_image_5 = PhotoImage(
                file=relative_to_assets(direc = 'Delete an event note', path = "image_5.png"))
            ddaen5 = canvas.create_image(
                639.0,
                349.0,
                image=ddaen_image_5
            )

            ddaen_label_5 = Label(canvas, image = ddaen_image_5)
            ddaen_label_5.image = ddaen_image_5

            ddaen_image_6 = PhotoImage(
                file=relative_to_assets(direc = 'Delete an event note', path = "image_6.png"))
            ddaen6 = canvas.create_image(
                639.0,
                461.6171875,
                image=ddaen_image_6
            )

            ddaen_label_6 = Label(canvas, image = ddaen_image_6)
            ddaen_label_6.image = ddaen_image_6

            ddaen_button_image_1 = PhotoImage(
                file=relative_to_assets(direc = 'Delete an event note', path = "button_1.png"))
            ddaen_button_1 = Button(
                image=ddaen_button_image_1,
                highlightthickness=0,
                command=lambda: delete_delete_product_type_note(),
                relief="flat"
            )
            ddaen_button_1.place(
                x=666.5009765625,
                y=475.0,
                width=61,
                height=17
            )

            ddaen_button_label_1 = Label(canvas, image = ddaen_button_image_1)
            ddaen_button_label_1.image = ddaen_button_image_1

            ddaen_button_image_2 = PhotoImage(
                file=relative_to_assets(direc = 'Delete an event note', path = "button_2.png"))
            ddaen_button_2 = Button(
                image=ddaen_button_image_2,
                highlightthickness=0,
                command=lambda: delete_product_type(),
                relief="flat"
            )
            ddaen_button_2.place(
                x=736.0009765625,
                y=475.0,
                width=61,
                height=17
            )

            ddaen_button_label_2 = Label(canvas, image = ddaen_button_image_2)
            ddaen_button_label_2.image = ddaen_button_image_2

            ddaen7 = canvas.create_text(
                481.5009765625,
                317.5,
                anchor="nw",
                text="Removing a product from use",
                fill="#D1D3D4",
                font=("Inter", 20 * -1)
            )

            ddaen8 = canvas.create_text(
                482.0,
                365.0,
                anchor="nw",
                text="Are you sure that you are not going to use",
                fill="#D1D3D4",
                font=("Inter", 11 * -1)
            )

            ddaen9 = canvas.create_text(
                482.0,
                381.0,
                anchor="nw",
                text="this product anymore?",
                fill="#D1D3D4",
                font=("Inter", 11 * -1)
            )

            ddaen10 = canvas.create_text(
                482.0,
                411.0,
                anchor="nw",
                text="You cannot undo this move. This product will be removed",
                fill="#D1D3D4",
                font=("Inter", 11 * -1)
            )

            ddaen11 = canvas.create_text(
                482.0,
                427.0,
                anchor="nw",
                text="and not be usable in future events.",
                fill="#D1D3D4",
                font=("Inter", 11 * -1)
            )



        dpt_image_1 = PhotoImage(
            file=relative_to_assets(direc = 'Delete product type', path = "image_1.png"))
        dpt1 = canvas.create_image(
            640.0009765625,
            400.0,
            image=dpt_image_1
        )

        dpt_label_1 = Label(canvas, image = dpt_image_1)
        dpt_label_1.image = dpt_image_1

        dpt_image_2 = PhotoImage(
            file=relative_to_assets(direc = 'Delete product type', path = "image_2.png"))
        dpt2 = canvas.create_image(
            639.568359375,
            399.908203125,
            image=dpt_image_2
        )

        dpt_label_2 = Label(canvas, image = dpt_image_2)
        dpt_label_2.image = dpt_image_2

        dpt_image_3 = PhotoImage(
            file=relative_to_assets(direc = 'Delete product type', path = "image_3.png"))
        dpt3 = canvas.create_image(
            639.376953125,
            399.68408203125,
            image=dpt_image_3
        )

        dpt_label_3 = Label(canvas, image = dpt_image_3)
        dpt_label_3.image = dpt_image_3

        dpt_image_4 = PhotoImage(
            file=relative_to_assets(direc = 'Delete product type', path = "image_4.png"))
        dpt4 = canvas.create_image(
            639.376953125,
            404.298828125,
            image=dpt_image_4
        )

        dpt_label_4 = Label(canvas, image = dpt_image_4)
        dpt_label_4.image = dpt_image_4

        dpt_image_5 = PhotoImage(
            file=relative_to_assets(direc = 'Delete product type', path = "image_5.png"))
        dpt5 = canvas.create_image(
            639.375,
            348.298828125,
            image=dpt_image_5
        )

        dpt_label_5 = Label(canvas, image = dpt_image_5)
        dpt_label_5.image = dpt_image_5

        dpt_image_6 = PhotoImage(
            file=relative_to_assets(direc = 'Delete product type', path = "image_6.png"))
        dpt6 = canvas.create_image(
            639.4375,
            422.0830078125,
            image=dpt_image_6
        )

        dpt_label_6 = Label(canvas, image = dpt_image_6)
        dpt_label_6.image = dpt_image_6

        dpt_image_7 = PhotoImage(
            file=relative_to_assets(direc = 'Delete product type', path = "image_7.png"))
        dpt7 = canvas.create_image(
            639.376953125,
            461.55029296875,
            image=dpt_image_7
        )

        dpt_label_7 = Label(canvas, image = dpt_image_7)
        dpt_label_7.image = dpt_image_7
        
        dpt_button_image_2 = PhotoImage(
            file=relative_to_assets(direc = 'Delete product type', path = "button_2.png"))
        dpt_button_2 = Button(
            image=dpt_button_image_2,
            highlightthickness=0,
            command=lambda: delete_delete_product_type(variable = True),
            relief="flat"
        )
        dpt_button_2.place(
            x=665.0,
            y=477.443359375,
            width=61,
            height=17
        )

        dpt_button_label_2 = Label(canvas, image = dpt_button_image_2)
        dpt_button_label_2.image = dpt_button_image_2


        def extract_info():

            global product_name_a

            product_name_a = canvas.itemcget(dpt8, 'text')

            if product_name_a == "Product name":
                call_error(error_text = "Please select a type of product to delete.")
                product_name_a = ""
                delete_delete_product_type(variable = True)
            else: 
                delete_delete_product_type(variable = True)
                delete_product_type_note()
            

        dpt_button_image_3 = PhotoImage(
            file=relative_to_assets(direc = 'Delete product type', path = "button_3.png"))
        dpt_button_3 = Button(
            image=dpt_button_image_3,
            highlightthickness=0,
            command=lambda: extract_info(),
            relief="flat"
        )
        dpt_button_3.place(
            x=736.001953125,
            y=477.443359375,
            width=61,
            height=17
        )

        dpt_button_label_3 = Label(canvas, image = dpt_button_image_3)
        dpt_button_label_3.image = dpt_button_image_3

        dpt8 = canvas.create_text(
            494.0,
            415.5,
            anchor="nw",
            text="Product name",
            fill="#000000",
            font=("Inter", 11 * -1)
        )

        dpt9 = canvas.create_text(
            481.0,
            315.0,
            anchor="nw",
            text="Delete Product Type",
            fill="#D1D3D4",
            font=("Inter", 20 * -1)
        )

        dpt10 = canvas.create_text(
            483.0,
            371.0,
            anchor="nw",
            text="Note: Your are deleting the product from the application. It’s data will still",
            fill="#D1D3D4",
            font=("Inter", 8 * -1)
        )

        dpt11 = canvas.create_text(
            483.0,
            381.0,
            anchor="nw",
            text="remain but the product wouldn’t be used for events in the future.",
            fill="#D1D3D4",
            font=("Inter", 8 * -1)
        )

        def list_products(data: dict):

            final_list = []

            for i in data['type_of_products']:
                final_list.append(i)

            final_list.remove('special_occasion')

            for i in data['type_of_products']['special_occasion']:
                final_list.append(i)

            return final_list

        def Click_product_type(e, var):

            nclist = list_products(data = data)
            my_menu = Menu(None, tearoff=0, takefocus=0)

            for txt in nclist:
                exec(f"(my_menu.add_command(label = '{txt}', command = lambda: canvas.itemconfig({dpt8}, text = '{txt}')))")

            my_menu.tk_popup(e.x_root - 285, e.y_root + 16,entry="0")


        m_var = StringVar()

        dpt_button_image_1 = PhotoImage(
            file=relative_to_assets(direc = 'Delete product type', path = "button_1.png"))
        dpt_button_1 = Button(
            image=dpt_button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: None,
            relief="flat"
        )
        dpt_button_1.bind("<Button-1>", lambda e, var = m_var: Click_product_type(e, var))
        dpt_button_1.place(
            x=765.501953125,
            y=419.0,
            width=14,
            height=8.0
        )

        dpt_button_label_1 = Label(canvas, image = dpt_button_image_1)
        dpt_button_label_1.image = dpt_button_image_1




    def create_create_new_event():

        lower_dashboard_buttons()
        check_connection()

        def delete_create_new_event():
            
            raise_dashboard_buttons()
        
            canvas.itemconfig(cne1, state = 'hidden')
            canvas.itemconfig(cne2, state = 'hidden')
            canvas.itemconfig(cne3, state = 'hidden')
            canvas.itemconfig(cne4, state = 'hidden')
            canvas.itemconfig(cne5, state = 'hidden')
            canvas.itemconfig(cne6, state = 'hidden')
            canvas.itemconfig(cne7, state = 'hidden')
            canvas.itemconfig(cne8, state = 'hidden')
            canvas.itemconfig(cne9, state = 'hidden')
            canvas.itemconfig(cne10, state = 'hidden')
            canvas.itemconfig(cne11, state = 'hidden')
            canvas.itemconfig(cne12, state = 'hidden')
            canvas.itemconfig(cne13, state = 'hidden')
            canvas.itemconfig(cne14, state = 'hidden')
            canvas.itemconfig(cne15, state = 'hidden')
            canvas.itemconfig(cne16, state = 'hidden')

            entry_1.lower()
        

            cne_button_1.lower()
            cne_button_2.lower()
            cne_button_3.lower()
            cne_button_4.lower()


        def temp_text(e):
            entry_1.delete(0, END)


        cne_image_1 = PhotoImage(
            file=relative_to_assets(direc = 'Create New Event', path = "image_1.png"))
        cne1 = canvas.create_image(
            640.0,
            400.0,
            image=cne_image_1
        )

        cne_label_1 = Label(canvas, image = cne_image_1)
        cne_label_1.image = cne_image_1

        cne_image_2 = PhotoImage(
            file=relative_to_assets(direc = 'Create New Event', path = "image_2.png"))
        cne2 = canvas.create_image(
            639.75,
            399.04833984375,
            image=cne_image_2
        )

        cne_label_2 = Label(canvas, image = cne_image_2)
        cne_label_2.image = cne_image_2

        cne_image_3 = PhotoImage(
            file=relative_to_assets(direc = 'Create New Event', path = "image_3.png"))
        cne3 = canvas.create_image(
            639.1328125,
            399.37109375,
            image=cne_image_3
        )

        cne_label_3 = Label(canvas, image = cne_image_3)
        cne_label_3.image = cne_image_3

        cne4 = canvas.create_rectangle(
            481.1328125,
            312.31591796875,
            797.8681640625,
            502.44482421875,
            fill="#171819",
            outline="")

        cne_image_4 = PhotoImage(
            file=relative_to_assets(direc = 'Create New Event', path = "image_4.png"))
        cne5 = canvas.create_image(
            639.1318359375,
            311.31591796875,
            image=cne_image_4
        )

        cne_label_4 = Label(canvas, image = cne_image_4)
        cne_label_4.image = cne_image_4

        cne_image_5 = PhotoImage(
            file=relative_to_assets(direc = 'Create New Event', path = "image_5.png"))
        cne6 = canvas.create_image(
            639.1318359375,
            501.44482421875,
            image=cne_image_5
        )

        cne_label_5 = Label(canvas, image = cne_image_5)
        cne_label_5.image = cne_image_5

        cne_image_6 = PhotoImage(
            file=relative_to_assets(direc = 'Create New Event', path = "image_6.png"))
        cne7 = canvas.create_image(
            639.1318359375,
            408.58447265625,
            image=cne_image_6
        )

        cne_label_6 = Label(canvas, image = cne_image_6)
        cne_label_6.image = cne_image_6

        cne_image_7 = PhotoImage(
            file=relative_to_assets(direc = 'Create New Event', path = "image_7.png"))
        cne8 = canvas.create_image(
            640.15234375,
            371.3701171875,
            image=cne_image_7
        )

        cne_label_7 = Label(canvas, image = cne_image_7)
        cne_label_7.image = cne_image_7

        cne_image_8 = PhotoImage(
            file=relative_to_assets(direc = 'Create New Event', path = "image_8.png"))
        cne9 = canvas.create_image(
            564.724609375,
            465.03173828125,
            image=cne_image_8
        )

        cne_label_8 = Label(canvas, image = cne_image_8)
        cne_label_8.image = cne_image_8

        cne_image_9 = PhotoImage(
            file=relative_to_assets(direc = 'Create New Event', path = "image_9.png"))
        cne10 = canvas.create_image(
            713.888671875,
            465.02978515625,
            image=cne_image_9
        )

        cne_label_9 = Label(canvas, image = cne_image_9)
        cne_label_9.image = cne_image_9


        entry_1 = Entry(
            bd=0,
            bg="#D1D3D4",
            fg="#000000",
            font=("Inter", 11 * -1),
            highlightthickness=0
        )
        entry_1.insert(0,"New name for event")
        entry_1.pack()
        entry_1.bind("<FocusIn>", temp_text) 
        entry_1.place(
            x=503.0,
            y=363.5,
            width=274.0,
            height=15.0
        )

        cne11 = canvas.create_text(
            505.0009765625,
            365.0,
            anchor="nw",
            text="New name for event",
            fill="#000000",
            font=("Inter", 11 * -1)
        )

        cne12 = canvas.create_text(
            540.5009765625,
            459.0,
            anchor="nw",
            text="Month",
            fill="#000000",
            font=("Inter", 11 * -1)
        )

        cne13 = canvas.create_text(
            698.5009765625,
            459.0,
            anchor="nw",
            text="Day",
            fill="#000000",
            font=("Inter", 11 * -1)
        )

        def list_month(data: dict):

            current_month = dt.date.today().month

            info_month = ['January', 'February', 'March',
                          'April', 'May', 'June',
                          'July', 'August', 'September',
                          'October', 'November', 'December'
                          ]

            final_list = []

            for i in range(13 - current_month):
                month_name = info_month[i + current_month - 1]
                final_list.append(month_name)

            return final_list

        def Click_month(e, var):

            nclist = list_month(data = data)
            my_menu = Menu(None, tearoff=0, takefocus=0)

            for txt in nclist:
                exec(f"(my_menu.add_command(label = '{txt}', command = lambda: canvas.itemconfig({cne12}, text = '{txt}')))")

            my_menu.tk_popup(e.x_root - 85, e.y_root + 16,entry="0")


        m_var = StringVar()

        cne_button_image_1 = PhotoImage(
            file=relative_to_assets(direc = 'Create New Event', path = "button_1.png"))
        cne_button_1 = Button(
            image=cne_button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: None,
            relief="flat"
        )
        cne_button_1.bind("<Button-1>", lambda e, var = m_var: Click_month(e, var))
        cne_button_1.place(
            x=611.0009765625,
            y=462.0,
            width=14,
            height=8.0
        )

        cne_button_label_1 = Label(canvas, image = cne_button_image_1)
        cne_button_label_1.image = cne_button_image_1

        def list_day():

            final_list = []

            for i in range(31):
                final_list.append(i+1)
                
            return final_list

        def Click_day(e, var):

            nclist = list_day()
            my_menu = Menu(None, tearoff=0, takefocus=0)
        
            for txt in nclist:
                exec(f"(my_menu.add_command(label = '{txt}', command = lambda: canvas.itemconfig({cne13}, text = '{txt}')))")
                
            my_menu.tk_popup(e.x_root - 80, e.y_root + 16,entry="0")
            

        d_var = StringVar()

        cne_button_image_2 = PhotoImage(
            file=relative_to_assets(direc = 'Create New Event', path = "button_2.png"))
        cne_button_2 = Button(
            image=cne_button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: None,
            relief="flat"
        )
        cne_button_2.bind("<Button-1>", lambda e, var = d_var: Click_day(e, var))
        cne_button_2.place(
            x=760.5009765625,
            y=462.0,
            width=14,
            height=8.0
        )

        cne_button_label_2 = Label(canvas, image = cne_button_image_2)
        cne_button_label_2.image = cne_button_image_2

        def extract_info():

            #if current date is 5 days before pre-assigned event date
            
            event_name_a = entry_1.get()

            if event_name_a == 'New name for current event':
                delete_event_settings()

            month_a = canvas.itemcget(cne12, 'text')
            day_a = canvas.itemcget(cne13, 'text')
            day_a = int(day_a)

            current_year = dt.datetime.today().year
            current_month = dt.datetime.today().month
            current_day = dt.datetime.today().day

            month_info = {
                'January': 1,
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

            month_name = month_a
            month_a = month_info[month_a]

            #check if leap year for february
            if current_year % 400 == 0 or current_year % 100 != 0 and current_year % 4 == 0:
                #if leap year true
                if month_a == 2:
                    if day_a > 29:
                        call_error(error_text = "Unable to create new event")
                        call_error(error_text = "There is only 29 days in February. Please check your input.")

            else:
                #if leap year false
                if month_a == 2:
                    if day_a > 28:
                        call_error(error_text = "Unable to create new event")
                        call_error(error_text = "There is only 28 days in February. Please check your input.")

            short_month = [4, 6, 9, 11]
            long_month = [1, 3, 5, 7, 8, 10, 12]


            if month_a in short_month:
                #if more than 30 days in specific months
                if day_a > 30:
                    call_error(error_text = "Unable to create new event")
                    call_error(error_text = f"There is only 30 days in {month_name}. Please check your input.")

            elif month_a in long_month:
                #if more than 31 days in specific months
                if day_a > 31:
                    call_error(error_text = "Unable to create new event")
                    call_error(error_text = f"There is only 31 days in {month_name}. Please check your input.")

            if month_a == current_month:
                if day_a > (current_day - 5):
                    call_error(error_text = "Unable to create new event")
                    call_error(error_text = "Event is within 5 days of taking place, select a further date.")


            #construct date
            date = f"{str(month_a)}/"
            if len(str(day_a)) == 1:
                date += '0'
                date += str(day_a)
            elif len(str(day_a)) == 2:
                date += str(day_a)


            func.input_new_event(event = date, name = event_name_a)

            delete_create_new_event()



        cne_button_image_3 = PhotoImage(
            file=relative_to_assets(direc = 'Create New Event', path = "button_3.png"))
        cne_button_3 = Button(
            image=cne_button_image_3,
            highlightthickness=0,
            command=lambda: extract_info(),
            relief="flat"
        )
        cne_button_3.place(
            x=719.896484375,
            y=517.5,
            width=62,
            height=17
        )

        cne_button_label_3 = Label(canvas, image = cne_button_image_3)
        cne_button_label_3.image = cne_button_image_3

        cne_button_image_4 = PhotoImage(
            file=relative_to_assets(direc = 'Create New Event', path = "button_4.png"))
        cne_button_4 = Button(
            image=cne_button_image_4,
            highlightthickness=0,
            command=lambda: delete_create_new_event(),
            relief="flat"
        )
        cne_button_4.place(
            x=654.31640625,
            y=517.5,
            width=62,
            height=17
        )

        cne_button_label_4 = Label(canvas, image = cne_button_image_4)
        cne_button_label_4.image = cne_button_image_4

        cne14 = canvas.create_text(
            500.0,
            334.0,
            anchor="nw",
            text="What is the name of this event?",
            fill="#D1D3D4",
            font=("Inter", 11 * -1)
        )

        cne15 = canvas.create_text(
            500.0,
            428.0,
            anchor="nw",
            text="When will this even take place?",
            fill="#D1D3D4",
            font=("Inter", 11 * -1)
        )

        cne16 = canvas.create_text(
            502.0,
            274.0,
            anchor="nw",
            text="Create New Event",
            fill="#D1D3D4",
            font=("Inter", 21 * -1)
        )



    def create_delete_an_event():

        lower_dashboard_buttons()
        check_connection()

        def delete_delete_an_event(variable: bool):
        
        
            canvas.itemconfig(dae1, state = 'hidden')
            canvas.itemconfig(dae2, state = 'hidden')
            canvas.itemconfig(dae3, state = 'hidden')
            canvas.itemconfig(dae4, state = 'hidden')
            canvas.itemconfig(dae5, state = 'hidden')
            canvas.itemconfig(dae6, state = 'hidden')
            canvas.itemconfig(dae7, state = 'hidden')
            canvas.itemconfig(dae8, state = 'hidden')
            canvas.itemconfig(dae9, state = 'hidden')
            canvas.itemconfig(dae10, state = 'hidden')
            canvas.itemconfig(dae11, state = 'hidden')

            dae_button_1.lower()
            dae_button_2.lower()
            dae_button_3.lower()

            if variable == True:

                global event_name_a
                event_name_a = ''
                raise_dashboard_buttons()    
            

        def delete_an_event_note():

            delete_delete_an_event(variable = False)

            def delete_delete_an_event_note():

                raise_dashboard_buttons()

                canvas.itemconfig(ddaen1, state = 'hidden')
                canvas.itemconfig(ddaen2, state = 'hidden')
                canvas.itemconfig(ddaen3, state = 'hidden')
                canvas.itemconfig(ddaen4, state = 'hidden')
                canvas.itemconfig(ddaen5, state = 'hidden')
                canvas.itemconfig(ddaen6, state = 'hidden')
                canvas.itemconfig(ddaen7, state = 'hidden')
                canvas.itemconfig(ddaen8, state = 'hidden')
                canvas.itemconfig(ddaen9, state = 'hidden')
                canvas.itemconfig(ddaen10, state = 'hidden')
                

                ddaen_button_1.lower()
                ddaen_button_2.lower()

            def delete_the_event():

                global event_name_a
                func.delete_event(event = event_name_a)
                event_name_a = ''            
                delete_delete_an_event_note()


                
            ddaen_image_1 = PhotoImage(
                file=relative_to_assets(direc = 'Delete an event note', path = "image_1.png"))
            ddaen1 = canvas.create_image(
                640.0,
                400.0,
                image=ddaen_image_1
            )

            ddaen_label_1 = Label(canvas, image = ddaen_image_1)
            ddaen_label_1.image = ddaen_image_1

            ddaen_image_2 = PhotoImage(
                file=relative_to_assets(direc = 'Delete an event note', path = "image_2.png"))
            ddaen2 = canvas.create_image(
                639.7705078125,
                399.0361328125,
                image=image_image_2
            )

            ddaen_label_2 = Label(canvas, image = ddaen_image_2)
            ddaen_label_2.image = ddaen_image_2

            ddaen_image_3 = PhotoImage(
                file=relative_to_assets(direc = 'Delete an event note', path = "image_3.png"))
            ddaen3 = canvas.create_image(
                639.376953125,
                399.58642578125,
                image=ddaen_image_3
            )

            ddaen_label_3 = Label(canvas, image = ddaen_image_3)
            ddaen_label_3.image = ddaen_image_3

            ddaen_image_4 = PhotoImage(
                file=relative_to_assets(direc = 'Delete an event note', path = "image_4.png"))
            ddaen4 = canvas.create_image(
                639.376953125,
                405.4169921875,
                image=ddaen_image_4
            )

            ddaen_label_4 = Label(canvas, image = ddaen_image_4)
            ddaen_label_4.image = ddaen_image_4

            ddaen_image_5 = PhotoImage(
                file=relative_to_assets(direc = 'Delete an event note', path = "image_5.png"))
            ddaen5 = canvas.create_image(
                639.0,
                349.0,
                image=ddaen_image_5
            )

            ddaen_label_5 = Label(canvas, image = ddaen_image_5)
            ddaen_label_5.image = ddaen_image_5

            ddaen_image_6 = PhotoImage(
                file=relative_to_assets(direc = 'Delete an event note', path = "image_6.png"))
            ddaen6 = canvas.create_image(
                639.0,
                461.6171875,
                image=ddaen_image_6
            )

            ddaen_label_6 = Label(canvas, image = ddaen_image_6)
            ddaen_label_6.image = ddaen_image_6

            ddaen_button_image_1 = PhotoImage(
                file=relative_to_assets(direc = 'Delete an event note', path = "button_1.png"))
            ddaen_button_1 = Button(
                image=ddaen_button_image_1,
                highlightthickness=0,
                command=lambda: delete_delete_an_event_note(),
                relief="flat"
            )
            ddaen_button_1.place(
                x=666.5009765625,
                y=475.0,
                width=61,
                height=17
            )

            ddaen_button_label_1 = Label(canvas, image = ddaen_button_image_1)
            ddaen_button_label_1.image = ddaen_button_image_1

            ddaen_button_image_2 = PhotoImage(
                file=relative_to_assets(direc = 'Delete an event note', path = "button_2.png"))
            ddaen_button_2 = Button(
                image=ddaen_button_image_2,
                highlightthickness=0,
                command=lambda: delete_the_event(),
                relief="flat"
            )
            ddaen_button_2.place(
                x=736.0009765625,
                y=475.0,
                width=61,
                height=17
            )

            ddaen_button_label_2 = Label(canvas, image = ddaen_button_image_2)
            ddaen_button_label_2.image = ddaen_button_image_2

            ddaen7 = canvas.create_text(
                481.5009765625,
                317.5,
                anchor="nw",
                text="Deleting an Event",
                fill="#D1D3D4",
                font=("Inter", 20 * -1)
            )

            ddaen8 = canvas.create_text(
                482.0,
                370.0,
                anchor="nw",
                text="Are you sure that you like to delete this event?",
                fill="#D1D3D4",
                font=("Inter", 11 * -1)
            )

            ddaen9 = canvas.create_text(
                482.0,
                401.0,
                anchor="nw",
                text="You cannot undo this move. The data will be removed",
                fill="#D1D3D4",
                font=("Inter", 11 * -1)
            )

            ddaen10 = canvas.create_text(
                482.0,
                417.0,
                anchor="nw",
                text="permanently.",
                fill="#D1D3D4",
                font=("Inter", 11 * -1)
            )


        global event_name_a
        event_name_a = ''

        dae_image_1 = PhotoImage(
            file=relative_to_assets(direc = 'Delete an event', path = "image_1.png"))
        dae1 = canvas.create_image(
            640.0,
            400.0,
            image=dae_image_1
        )

        dae_label_1 = Label(canvas, image = dae_image_1)
        dae_label_1.image = dae_image_1

        dae_image_2 = PhotoImage(
            file=relative_to_assets(direc = 'Delete an event', path = "image_2.png"))
        dae2 = canvas.create_image(
            639.5810546875,
            399.908203125,
            image=dae_image_2
        )

        dae_label_2 = Label(canvas, image = dae_image_2)
        dae_label_2.image = dae_image_2

        dae_image_3 = PhotoImage(
            file=relative_to_assets(direc = 'Delete an event', path = "image_3.png"))
        dae3 = canvas.create_image(
            639.376953125,
            399.68408203125,
            image=dae_image_3
        )

        dae_label_3 = Label(canvas, image = dae_image_3)
        dae_label_3.image = dae_image_3

        dae4 = canvas.create_rectangle(
            463.376953125,
            348.298828125,
            815.625,
            461.55029296875,
            fill="#171819",
            outline="")

        dae_image_4 = PhotoImage(
            file=relative_to_assets(direc = 'Delete an event', path = "image_4.png"))
        dae5 = canvas.create_image(
            639.3759765625,
            348.298828125,
            image=dae_image_4
        )

        dae_label_4 = Label(canvas, image = dae_image_4)
        dae_label_4.image = dae_image_4

        dae_image_5 = PhotoImage(
            file=relative_to_assets(direc = 'Delete an event', path = "image_5.png"))
        dae6 = canvas.create_image(
            639.4384765625,
            422.0830078125,
            image=dae_image_5
        )

        dae_label_5 = Label(canvas, image = dae_image_5)
        dae_label_5.image = dae_image_5

        dae_image_6 = PhotoImage(
            file=relative_to_assets(direc = 'Delete an event', path = "image_6.png"))
        dae7 = canvas.create_image(
            639.376953125,
            461.55029296875,
            image=dae_image_6
        )

        dae_label_6 = Label(canvas, image = dae_image_6)
        dae_label_6.image = dae_image_6
        

        dae_button_image_1 = PhotoImage(
            file=relative_to_assets(direc = 'Delete an event', path = "button_1.png"))
        dae_button_1 = Button(
            image=dae_button_image_1,
            highlightthickness=0,
            command=lambda: delete_delete_an_event(variable = True),
            relief="flat"
        )
        dae_button_1.place(
            x=670.5009765625,
            y=477.443359375,
            width=61,
            height=18
        )

        dae_button_label_1 = Label(canvas, image = dae_button_image_1)
        dae_button_label_1.image = dae_button_image_1


        def extract_info():

            global event_name_a

            event_name_a = canvas.itemcget(dae8, 'text')

            if event_name_a == 'Event name':
                event_name_a = ''
                call_error(error_text = "Please choose an event to delete the event.")

                delete_delete_an_event(variable = True)

            else:

                converter = {}
                
                for i in data['event_name']:
                    temp_event_name = data['event_name'][i]
                    converter[temp_event_name] = i

                event_name_a = converter[event_name_a]
                delete_an_event_note()

        dae_button_image_2 = PhotoImage(
            file=relative_to_assets(direc = 'Delete an event', path = "button_2.png"))
        dae_button_2 = Button(
            image=dae_button_image_2,
            highlightthickness=0,
            command=lambda: extract_info(),
            relief="flat"
        )
        dae_button_2.place(
            x=736.0009765625,
            y=477.443359375,
            width=62,
            height=18
        )

        dae_button_label_2 = Label(canvas, image = dae_button_image_2)
        dae_button_label_2.image = dae_button_image_2
        

        def list_event(data: dict):

            final_list = []

            if data['event'] != []:

                for i in data['event_name']:
                    final_list.append(data['event_name'][i])

                #check if nearest event is deletable
                nearest_event = data['event'][0]
                nearest_event += f"/{str(dt.datetime.today().year)}"
                nearest_event_time = dt.datetime.strptime(nearest_event, "%m/%d/%Y")
                time_now = dt.datetime.now()

                time_diff = (time_now - nearest_event_time).days

                if time_diff > -6:
                    closest_event = data['event'][0]
                    final_list.remove(data['event_name'][closest_event])

            return final_list
        

        def Click_event(e, var):

            nclist = list_event(data = data)
            my_menu = Menu(None, tearoff=0, takefocus=0)

            for txt in nclist:
                exec(f"(my_menu.add_command(label = '{txt}', command = lambda: canvas.itemconfig({dae8}, text = '{txt}')))")

            my_menu.tk_popup(e.x_root - 285, e.y_root + 16,entry="0")


        m_var = StringVar()

        dae_button_image_3 = PhotoImage(
            file=relative_to_assets(direc = 'Delete an event', path = "button_3.png"))
        dae_button_3 = Button(
            image=dae_button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: None,
            relief="flat"
        )
        dae_button_3.bind("<Button-1>", lambda e, var = m_var: Click_event(e, var))
        dae_button_3.place(
            x=765.0009765625,
            y=418.0,
            width=14,
            height=8.0
        )

        dae_button_label_3 = Label(canvas, image = dae_button_image_3)
        dae_button_label_3.image = dae_button_image_3

        dae8 = canvas.create_text(
            494.5009765625,
            415.0,
            anchor="nw",
            text="Event name",
            fill="#000000",
            font=("Inter", 11 * -1)
        )

        dae9 = canvas.create_text(
            484.0,
            370.0,
            anchor="nw",
            text="Note: You are deleting an entire event! The deletion of an event is",
            fill="#D1D3D4",
            font=("Inter", 9 * -1)
        )

        dae10 = canvas.create_text(
            484.0,
            381.0,
            anchor="nw",
            text="unrecoverable and you won’t be able to undo this move!",
            fill="#D1D3D4",
            font=("Inter", 9 * -1)
        )

        dae11 = canvas.create_text(
            484.0,
            313.0,
            anchor="nw",
            text="Delete an Event",
            fill="#D1D3D4",
            font=("Inter", 20 * -1)
        )



    def initialisation():

        lower_dashboard_buttons()
        check_connection()
        canvas.delete("all")
        remove_userid()
        initialise()

        '''lower_dashboard_buttons()

        def delete_login_page():
            
            raise_dashboard_buttons()
        
            canvas.itemconfig(lp1, state = 'hidden')
            canvas.itemconfig(lp2, state = 'hidden')
            canvas.itemconfig(lp3, state = 'hidden')
            canvas.itemconfig(lp4, state = 'hidden')
            canvas.itemconfig(lp5, state = 'hidden')
            canvas.itemconfig(lp6, state = 'hidden')
            canvas.itemconfig(lp7, state = 'hidden')

            lp_button_1.lower()


        lp_image_1 = PhotoImage(
            file=relative_to_assets(direc = 'Login page', path = "image_1.png"))
        lp1 = canvas.create_image(
            640.5,
            400.5,
            image=lp_image_1
        )

        lp_label_1 = Label(canvas, image = lp_image_1)
        lp_label_1.image = lp_image_1

        lp_image_2 = PhotoImage(
            file=relative_to_assets(direc = 'Login page', path = "image_2.png"))
        lp2 = canvas.create_image(
            639.5,
            389.0,
            image=lp_image_2
        )

        lp_label_2 = Label(canvas, image = lp_image_2)
        lp_label_2.image = lp_image_2

        lp_button_image_1 = PhotoImage(
            file=relative_to_assets(direc = 'Login page', path = "button_1.png"))
        lp_button_1 = Button(
            image=lp_button_image_1,
            highlightthickness=0,
            command=lambda: delete_login_page(),
            relief="flat"
        )
        lp_button_1.place(
            x=540.0,
            y=531.0,
            width=199.0,
            height=59.0
        )

        lp_button_label_1 = Label(canvas, image = lp_button_image_1)
        lp_button_label_1.image = lp_button_image_1

        lp_image_3 = PhotoImage(
            file=relative_to_assets(direc = 'Login page', path = "image_3.png"))
        lp3 = canvas.create_image(
            640.0,
            368.0,
            image=lp_image_3
        )

        lp_label_3 = Label(canvas, image = lp_image_3)
        lp_label_3.image = lp_image_3

        lp4 = canvas.create_text(
            511.0,
            211.0,
            anchor="nw",
            text="Welcome Back!",
            fill="#FFFFFF",
            font=("ABeeZee Regular", 37 * -1)
        )

        lp_image_4 = PhotoImage(
            file=relative_to_assets(direc = 'Login page', path = "image_4.png"))
        lp5 = canvas.create_image(
            88.0009765625,
            29.419921875,
            image=lp_image_4
        )

        lp_label_4 = Label(canvas, image = lp_image_4)
        lp_label_4.image = lp_image_4

        lp6 = canvas.create_text(
            529.0,
            479.0,
            anchor="nw",
            text="You will be redirected to your web",
            fill="#FFFFFF",
            font=("ABeeZee", 14 * -1)
        )

        lp7 = canvas.create_text(
            529.0,
            496.0,
            anchor="nw",
            text="browser to sign into your account.",
            fill="#FFFFFF",
            font=("ABeeZee", 14 * -1)
        )'''


    def create_notifications():

        lower_dashboard_buttons()
        check_connection()

        def delete_notifications():
            
            raise_dashboard_buttons()
        
            canvas.itemconfig(n1, state = 'hidden')
            canvas.itemconfig(n2, state = 'hidden')
            canvas.itemconfig(n3, state = 'hidden')
            canvas.itemconfig(n4, state = 'hidden')
            canvas.itemconfig(n5, state = 'hidden')
            canvas.itemconfig(n6, state = 'hidden')
            canvas.itemconfig(n7, state = 'hidden')

            canvas.itemconfig(notif_image_gray_1, state = 'hidden')
            canvas.itemconfig(notif_image_node_1, state = 'hidden')
            canvas.itemconfig(notif_text_1, state = 'hidden')

            canvas.itemconfig(notif_image_gray_2, state = 'hidden')
            canvas.itemconfig(notif_image_node_2, state = 'hidden')
            canvas.itemconfig(notif_text_2, state = 'hidden')

            canvas.itemconfig(notif_image_gray_3, state = 'hidden')
            canvas.itemconfig(notif_image_node_3, state = 'hidden')
            canvas.itemconfig(notif_text_3, state = 'hidden')

            canvas.itemconfig(notif_image_gray_4, state = 'hidden')
            canvas.itemconfig(notif_image_node_4, state = 'hidden')
            canvas.itemconfig(notif_text_4, state = 'hidden')

            canvas.itemconfig(notif_image_gray_5, state = 'hidden')
            canvas.itemconfig(notif_image_node_5, state = 'hidden')
            canvas.itemconfig(notif_text_5, state = 'hidden')

            canvas.itemconfig(notif_image_gray_6, state = 'hidden')
            canvas.itemconfig(notif_image_node_6, state = 'hidden')
            canvas.itemconfig(notif_text_6, state = 'hidden')

            canvas.itemconfig(notif_image_gray_7, state = 'hidden')
            canvas.itemconfig(notif_image_node_7, state = 'hidden')
            canvas.itemconfig(notif_text_7, state = 'hidden')

            canvas.itemconfig(notif_image_gray_8, state = 'hidden')
            canvas.itemconfig(notif_image_node_8, state = 'hidden')
            canvas.itemconfig(notif_text_8, state = 'hidden')

            canvas.itemconfig(notif_image_gray_9, state = 'hidden')
            canvas.itemconfig(notif_image_node_9, state = 'hidden')
            canvas.itemconfig(notif_text_9, state = 'hidden')

            canvas.itemconfig(notif_image_gray_10, state = 'hidden')
            canvas.itemconfig(notif_image_node_10, state = 'hidden')
            canvas.itemconfig(notif_text_10, state = 'hidden')
                
            n_button_1.lower()



        n_image_1 = PhotoImage(
            file=relative_to_assets(direc = 'Notifications', path = "image_1.png"))
        n1 = canvas.create_image(
            639.001953125,
            400.0,
            image=n_image_1
        )

        n1_label = Label(canvas, image = n_image_1)
        n1_label.image = n_image_1

        n_image_2 = PhotoImage(
            file=relative_to_assets(direc = 'Notifications', path = "image_2.png"))
        n2 = canvas.create_image(
            921.5625,
            286.37353515625,
            image=n_image_2
        )

        n2_label = Label(canvas, image = n_image_2)
        n2_label.image = n_image_2
        
        n_image_3 = PhotoImage(
            file=relative_to_assets(direc = 'Notifications', path = "image_3.png"))
        n3 = canvas.create_image(
            921.33984375,
            286.16064453125,
            image=n_image_3
        )

        n3_label = Label(canvas, image = n_image_3)
        n3_label.image = n_image_3

        n_image_4 = PhotoImage(
            file=relative_to_assets(direc = 'Notifications', path = "image_4.png"))
        n4 = canvas.create_image(
            921.33984375,
            289.99072265625,
            image=n_image_4
        )

        n4_label = Label(canvas, image = n_image_4)
        n4_label.image = n_image_4

        n_image_5 = PhotoImage(
            file=relative_to_assets(direc = 'Notifications', path = "image_5.png"))
        n5 = canvas.create_image(
            921.33984375,
            137.99072265625,
            image=n_image_5
        )

        n5_label = Label(canvas, image = n_image_5)
        n5_label.image = n_image_5
        
        n_image_6 = PhotoImage(
            file=relative_to_assets(direc = 'Notifications', path = "image_6.png"))
        n6 = canvas.create_image(
            921.33984375,
            443.63134765625,
            image=n_image_6
        )

        n6_label = Label(canvas, image = n_image_6)
        n6_label.image = n_image_6

        n_button_image_1 = PhotoImage(
            file=relative_to_assets(direc = 'Notifications', path = "button_1.png"))
        n_button_1 = Button(
            image=n_button_image_1,
            highlightthickness=0,
            command=lambda: delete_notifications(),
            relief="flat"
        )
        n_button_1.place(
            x=1009.0,
            y=456.0,
            width=61,
            height=17
        )

        n_button_label_1 = Label(canvas, image = n_button_image_1)
        n_button_label_1.image = n_button_image_1

        n2_label = Label(canvas, image = n_image_2)
        n2_label.image = n_image_2

        n7 = canvas.create_text(
            763.0,
            107.0,
            anchor="nw",
            text="Alerts",
            fill="#D1D3D4",
            font=("Inter", 20 * -1)
        )

        def refresh_notif():

            nonlocal notif_image_gray_1
            nonlocal notif_image_node_1
            nonlocal notif_text_1
            nonlocal notif_image_gray_2
            nonlocal notif_image_node_2
            nonlocal notif_text_2
            nonlocal notif_image_gray_3
            nonlocal notif_image_node_3
            nonlocal notif_text_3
            nonlocal notif_image_gray_4
            nonlocal notif_image_node_4
            nonlocal notif_text_4
            nonlocal notif_image_gray_5
            nonlocal notif_image_node_5
            nonlocal notif_text_5
            nonlocal notif_image_gray_6
            nonlocal notif_image_node_6
            nonlocal notif_text_6
            nonlocal notif_image_gray_7
            nonlocal notif_image_node_7
            nonlocal notif_text_7
            nonlocal notif_image_gray_8
            nonlocal notif_image_node_8
            nonlocal notif_text_8
            nonlocal notif_image_gray_9
            nonlocal notif_image_node_9
            nonlocal notif_text_9
            nonlocal notif_image_gray_10
            nonlocal notif_image_node_10
            nonlocal notif_text_10
        
            for i in range(1):

                if len(call_error_list) <= 10:
                    lena = len(call_error_list)
                else:
                    lena = 10

                for i in range(lena):
                    
                    #gray box
                    notif_image = PhotoImage(
                        file=relative_to_assets(direc = 'Notifications', path = "image_7.png"))
                    exec(f"canvas.itemconfig(notif_image_gray_{i+1}, image = notif_image)")
                    notif_label_gray = Label(canvas, image = notif_image)
                    notif_label_gray.image = notif_image

                    #red node
                    notif_red_node = PhotoImage(
                        file=relative_to_assets(direc = 'Notifications', path = "image_10.png"))
                    exec(f"canvas.itemconfig(notif_image_node_{i+1}, image = notif_red_node)")
                    notif_label_node = Label(canvas, image = notif_red_node)
                    notif_label_node.image = notif_red_node

                    #text
                    texta = call_error_list[-i-1]
                    print(texta)
                    exec(f"canvas.itemconfig(notif_text_{i+1}, text = texta)")


                if lena == 0:

                    #gray box
                    notif_image = PhotoImage(
                        file=relative_to_assets(direc = 'Notifications', path = "image_7.png"))
                    canvas.itemconfig(notif_image_gray_1, image = notif_image)
                    
                    notif_label_gray_1 = Label(canvas, image = notif_image)
                    notif_label_gray_1.image = notif_image

                    #green node
                    notif_green_node = PhotoImage(
                        file=relative_to_assets(direc = 'Notifications', path = "image_8.png"))
                    canvas.itemconfig(notif_image_node_1, image = notif_green_node)

                    notif_label_node_1 = Label(canvas, image = notif_green_node)
                    notif_label_node_1.image = notif_green_node

                    canvas.itemconfig(notif_text_1, text = "You are all set!")
                    
                    

        nig_image_1 = PhotoImage(
            file=relative_to_assets(direc = 'Notifications', path = "blank_image.png"))
        notif_image_gray_1 = canvas.create_image(
            921.5,
            422.0,
            image=nig_image_1
        )

        notif_label_gray_1 = Label(canvas, image = nig_image_1)
        notif_label_gray_1.image = nig_image_1

        nin_image_1 = PhotoImage(
            file=relative_to_assets(direc = 'Notifications', path = "blank_image.png"))
        notif_image_node_1 = canvas.create_image(
            772.0,
            422.0,
            image=nin_image_1
        )
        
        notif_label_node_1 = Label(canvas, image = nin_image_1)
        notif_label_node_1.image = nin_image_1

        notif_text_1 = canvas.create_text(
            792.0,
            417.0,
            anchor="nw",
            text="",
            fill="#D1D3D4",
            font=("Inter", 9 * -1)
        )

        nig_image_2 = PhotoImage(
            file=relative_to_assets(direc = 'Notifications', path = "blank_image.png"))
        notif_image_gray_2 = canvas.create_image(
            921.5,
            393.0,
            image=nig_image_2
        )

        notif_label_gray_2 = Label(canvas, image = nig_image_2)
        notif_label_gray_2.image = nig_image_2

        nin_image_2 = PhotoImage(
            file=relative_to_assets(direc = 'Notifications', path = "blank_image.png"))
        notif_image_node_2 = canvas.create_image(
            772.0,
            393.0,
            image=nin_image_2
        )

        notif_label_node_2 = Label(canvas, image = nin_image_2)
        notif_label_node_2.image = nin_image_2

        notif_text_2 = canvas.create_text(
            792.0,
            388.0,
            anchor="nw",
            text="",
            fill="#D1D3D4",
            font=("Inter", 9 * -1)
        )

        nig_image_3 = PhotoImage(
            file=relative_to_assets(direc = 'Notifications', path = "blank_image.png"))
        notif_image_gray_3 = canvas.create_image(
            921.5,
            364.0,
            image=nig_image_3
        )

        notif_label_gray_3 = Label(canvas, image = nig_image_3)
        notif_label_gray_3.image = nig_image_3

        nin_image_3 = PhotoImage(
            file=relative_to_assets(direc = 'Notifications', path = "blank_image.png"))
        notif_image_node_3 = canvas.create_image(
            772.0,
            364.0,
            image=nin_image_3
        )

        notif_label_node_3 = Label(canvas, image = nin_image_3)
        notif_label_node_3.image = nin_image_3

        notif_text_3 = canvas.create_text(
            792.0,
            359.0,
            anchor="nw",
            text="",
            fill="#D1D3D4",
            font=("Inter", 9 * -1)
        )

        nig_image_4 = PhotoImage(
            file=relative_to_assets(direc = 'Notifications', path = "blank_image.png"))
        notif_image_gray_4 = canvas.create_image(
            921.5,
            335.0,
            image=nig_image_4
        )

        notif_label_gray_4 = Label(canvas, image = nig_image_4)
        notif_label_gray_4.image = nig_image_4

        nin_image_4 = PhotoImage(
            file=relative_to_assets(direc = 'Notifications', path = "blank_image.png"))
        notif_image_node_4 = canvas.create_image(
            772.0,
            335.0,
            image=nin_image_4
        )

        notif_label_node_4 = Label(canvas, image = nin_image_4)
        notif_label_node_4.image = nin_image_4

        notif_text_4 = canvas.create_text(
            792.0,
            330.0,
            anchor="nw",
            text="",
            fill="#D1D3D4",
            font=("Inter", 9 * -1)
        )

        nig_image_5 = PhotoImage(
            file=relative_to_assets(direc = 'Notifications', path = "blank_image.png"))
        notif_image_gray_5 = canvas.create_image(
            921.5,
            306.0,
            image=nig_image_5
        )

        notif_label_gray_5 = Label(canvas, image = nig_image_5)
        notif_label_gray_5.image = nig_image_5

        nin_image_5 = PhotoImage(
            file=relative_to_assets(direc = 'Notifications', path = "blank_image.png"))
        notif_image_node_5 = canvas.create_image(
            772.0,
            306.0,
            image=nin_image_5
        )

        notif_label_node_5 = Label(canvas, image = nin_image_5)
        notif_label_node_5.image = nin_image_5

        notif_text_5 = canvas.create_text(
            792.0,
            301.0,
            anchor="nw",
            text="",
            fill="#D1D3D4",
            font=("Inter", 9 * -1)
        )

        nig_image_6 = PhotoImage(
            file=relative_to_assets(direc = 'Notifications', path = "blank_image.png"))
        notif_image_gray_6 = canvas.create_image(
            921.5,
            277.0,
            image=nig_image_6
        )

        notif_label_gray_6 = Label(canvas, image = nig_image_6)
        notif_label_gray_6.image = nig_image_6

        nin_image_6 = PhotoImage(
            file=relative_to_assets(direc = 'Notifications', path = "blank_image.png"))
        notif_image_node_6 = canvas.create_image(
            772.0,
            277.0,
            image=nin_image_6
        )

        notif_label_node_6 = Label(canvas, image = nin_image_6)
        notif_label_node_6.image = nin_image_6

        notif_text_6 = canvas.create_text(
            792.0,
            272.0,
            anchor="nw",
            text="",
            fill="#D1D3D4",
            font=("Inter", 9 * -1)
        )

        nig_image_7 = PhotoImage(
            file=relative_to_assets(direc = 'Notifications', path = "blank_image.png"))
        notif_image_gray_7 = canvas.create_image(
            921.5,
            248.0,
            image=nig_image_7
        )

        notif_label_gray_7 = Label(canvas, image = nig_image_7)
        notif_label_gray_7.image = nig_image_7

        nin_image_7 = PhotoImage(
            file=relative_to_assets(direc = 'Notifications', path = "blank_image.png"))
        notif_image_node_7 = canvas.create_image(
            772.0,
            248.0,
            image=nin_image_7
        )

        notif_label_node_7 = Label(canvas, image = nin_image_7)
        notif_label_node_7.image = nin_image_7

        notif_text_7 = canvas.create_text(
            792.0,
            243.0,
            anchor="nw",
            text="",
            fill="#D1D3D4",
            font=("Inter", 9 * -1)
        )

        nig_image_8 = PhotoImage(
            file=relative_to_assets(direc = 'Notifications', path = "blank_image.png"))
        notif_image_gray_8 = canvas.create_image(
            921.5,
            219.0,
            image=nig_image_8
        )

        notif_label_gray_8 = Label(canvas, image = nig_image_8)
        notif_label_gray_8.image = nig_image_8

        nin_image_8 = PhotoImage(
            file=relative_to_assets(direc = 'Notifications', path = "blank_image.png"))
        notif_image_node_8 = canvas.create_image(
            772.0,
            219.0,
            image=nin_image_8
        )

        notif_label_node_8 = Label(canvas, image = nin_image_8)
        notif_label_node_8.image = nin_image_8

        notif_text_8 = canvas.create_text(
            792.0,
            214.0,
            anchor="nw",
            text="",
            fill="#D1D3D4",
            font=("Inter", 9 * -1)
        )

        nig_image_9 = PhotoImage(
            file=relative_to_assets(direc = 'Notifications', path = "blank_image.png"))
        notif_image_gray_9 = canvas.create_image(
            921.5,
            190.0,
            image=nig_image_9
        )

        notif_label_gray_9 = Label(canvas, image = nig_image_9)
        notif_label_gray_9.image = nig_image_9

        nin_image_9 = PhotoImage(
            file=relative_to_assets(direc = 'Notifications', path = "blank_image.png"))
        notif_image_node_9 = canvas.create_image(
            772.0,
            190.0,
            image=nin_image_9
        )

        notif_label_node_9 = Label(canvas, image = nin_image_9)
        notif_label_node_9.image = nin_image_9

        notif_text_9 = canvas.create_text(
            792.0,
            185.0,
            anchor="nw",
            text="",
            fill="#D1D3D4",
            font=("Inter", 9 * -1)
        )

        nig_image_10 = PhotoImage(
            file=relative_to_assets(direc = 'Notifications', path = "blank_image.png"))
        notif_image_gray_10 = canvas.create_image(
            921.5,
            161.0,
            image=nig_image_10
        )

        notif_label_gray_10 = Label(canvas, image = nig_image_10)
        notif_label_gray_10.image = nig_image_10

        nin_image_10 = PhotoImage(
            file=relative_to_assets(direc = 'Notifications', path = "blank_image.png"))
        notif_image_node_10 = canvas.create_image(
            772.0,
            161.0,
            image=nin_image_10
        )

        notif_label_node_10 = Label(canvas, image = nin_image_10)
        notif_label_node_10.image = nin_image_10
        
        notif_text_10 = canvas.create_text(
            792.0,
            156.0,
            anchor="nw",
            text="",
            fill="#D1D3D4",
            font=("Inter", 9 * -1)
        )
        

        refresh_notif()


    def button_redo():

        resultc = connection_check()
        if resultc == False:
            lower_dashboard_buttons()
            check_connection()

        result = undo.redo()
        if result == "There is nothing to redo.":
            call_error(error_text = "There is nothing to redo.")


    def button_undo():

        resultc = connection_check()
        if resultc == False:
            lower_dashboard_buttons()
            check_connection()

        result = undo.undo()
        if result == "There is nothing to undo":
            call_error(error_text = "There is nothing to undo.")


    def data_save_check():

        resultc = connection_check()
        if resultc == False:
            lower_dashboard_buttons()
            check_connection()
            
        data_save(drive_service = drive_service, data_fileId = data_fileId, folder_id = folder_id)


    ##########################################################################################################################################################################################################

    #notification bell button
    button_image_1 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "button_1.png"))
    button_1 = Button(
        image=button_image_1,
        highlightthickness=0,
        command=lambda: create_notifications(),
        relief="flat"
    )

    button_label_1 = Label(canvas, image = button_image_1)
    button_label_1.image = button_image_1
    
    button_1.place(
        x=1075.0,
        y=47.0,
        width=42.0,
        height=39.0
    )

    image_button_1 = canvas.create_image(
        1096,
        65.5,
        image=button_image_1
    )
    

    #save button
    button_image_2 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "button_2.png"))
    button_2 = Button(
        image=button_image_2,
        highlightthickness=0,
        command=lambda: data_save_check(),
        relief="flat"
    )

    button_label_2 = Label(canvas, image = button_image_2)
    button_label_2.image = button_image_2
    
    button_2.place(
        x=1133.0,
        y=41.0,
        width=111.0,
        height=47.0
    )

    image_button_2 = canvas.create_image(
        1188,
        64,
        image=button_image_2
    )


    #undo button
    button_image_3 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "button_3.png"))
    button_3 = Button(
        image=button_image_3,
        highlightthickness=0,
        command=lambda: button_undo(),
        relief="flat"
    )

    button_label_3 = Label(canvas, image = button_image_3)
    button_label_3.image = button_image_3
    
    button_3.place(
        x=380.0,
        y=62.0,
        width=35.5,
        height=25.5
    )

    image_button_3 = canvas.create_image(
        397.75,
        74.75,
        image=button_image_3
    )


    #redo button
    button_image_4 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "button_4.png"))
    button_4 = Button(
        image=button_image_4,
        highlightthickness=0,
        command=lambda: button_redo(),
        relief="flat"
    )

    button_label_4 = Label(canvas, image = button_image_4)
    button_label_4.image = button_image_4
    
    button_4.place(
        x=421,
        y=62,
        width=35.5,
        height=25.5
    )

    image_button_4 = canvas.create_image(
        438.75,
        74.75,
        image=button_image_4
    )


    #overall - time spent chart
    button_image_5 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "button_5.png"))
    button_5 = Button(
        image=button_image_5,
        highlightthickness=0,
        command=lambda: create_chart(chart_type = 'timespent', year_over = 'over', data = data, x_cord = 540, y_cord = 597),
        relief="flat"
    )

    button_label_5 = Label(canvas, image = button_image_5)
    button_label_5.image = button_image_5
    
    button_5.place(
        x=819.0,
        y=748.0,
        width=43.5,
        height=9.0
    )

    image_button_5 = canvas.create_image(
        840.5,
        752.5,
        image=button_image_5
    )


    #y/d - time spent chart
    button_image_6 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "button_6.png"))
    button_6 = Button(
        image=button_image_6,
        highlightthickness=0,
        command=lambda: create_chart(chart_type = 'timespent', year_over = 'year', data = data, x_cord = 540, y_cord = 597),
        relief="flat"
    )

    button_label_6 = Label(canvas, image = button_image_6)
    button_label_6.image = button_image_6
    
    button_6.place(
        x=777.0,
        y=749.0,
        width=30.0,
        height=8
    )

    image_button_6 = canvas.create_image(
        791.5,
        753,
        image=button_image_6
    )


    #overall - profit chart
    button_image_7 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "button_7.png"))
    button_7 = Button(
        image=button_image_7,
        highlightthickness=0,
        command=lambda: create_chart(chart_type = 'profit', year_over = 'over', data = data, x_cord = 540, y_cord = 385),
        relief="flat"
    )

    button_label_7 = Label(canvas, image = button_image_7)
    button_label_7.image = button_image_7
    
    button_7.place(
        x=822.0,
        y=537.0,
        width=43.5,
        height=9.0
    )

    image_button_7 = canvas.create_image(
        843.5,
        541.5,
        image=button_image_7
    )


    #y/d - profit chart
    button_image_8 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "button_8.png"))
    button_8 = Button(
        image=button_image_8,
        highlightthickness=0,
        command=lambda: create_chart(chart_type = 'profit', year_over = 'year', data = data, x_cord = 540, y_cord = 385),
        relief="flat"
    )

    button_label_8 = Label(canvas, image = button_image_8)
    button_label_8.image = button_image_8
    
    button_8.place(
        x=780.0,
        y=537.0,
        width=30.0,
        height=9.0
    )

    image_button_8 = canvas.create_image(
        794.5,
        541.5,
        image=button_image_8
    )


    #overall - main data
    button_image_9 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "button_9.png"))
    button_9 = Button(
        image=button_image_9,
        highlightthickness=0,
        command=lambda: refresh_main_data(data = data, year_over = 'over'),
        relief="flat"
    )

    button_label_9 = Label(canvas, image = button_image_9)
    button_label_9.image = button_image_9
    
    button_9.place(
        x=822.744140625,
        y=231.0,
        width=43.5,
        height=8
    )

    image_button_9 = canvas.create_image(
        844.3720703,
        235,
        image=button_image_9
    )


    #y/d - main data
    button_image_10 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "button_10.png"))
    button_10 = Button(
        image=button_image_10,
        highlightthickness=0,
        command=lambda: refresh_main_data(data = data, year_over = 'year'),
        relief="flat"
    )

    button_label_10 = Label(canvas, image = button_image_10)
    button_label_10.image = button_image_10
    
    button_10.place(
        x=780.0,
        y=231.0,
        width=30.0,
        height=9.0
    )

    image_button_10 = canvas.create_image(
        794.5,
        235.5,
        image=button_image_10
    )


    #log out button
    button_image_11 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "button_11.png"))
    button_11 = Button(
        image=button_image_11,
        highlightthickness=0,
        command=lambda: initialisation(),
        relief="flat"
    )

    button_label_11 = Label(canvas, image = button_image_11)
    button_label_11.image = button_image_11
    
    button_11.place(
        x=116.0,
        y=765.0,
        width=32.1259765625,
        height=9.43988037109375
    )

    image_button_11 = canvas.create_image(
        132.0629883,
        769.7199402,
        image=button_image_11
    )


    #made an error
    button_image_12 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "button_12.png"))
    button_12 = Button(
        image=button_image_12,
        highlightthickness=0,
        command=lambda: create_made_an_error(),
        relief="flat"
    )

    button_label_12 = Label(canvas, image = button_image_12)
    button_label_12.image = button_image_12
    
    button_12.place(
        x=32.3984375,
        y=418.9002990722656,
        width=203.8076171875,
        height=21.443695068359375
    )

    image_button_12 = canvas.create_image(
        134.3022461,
        429.6221466,
        image=button_image_12
    )


    #google forms
    button_image_13 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "button_13.png"))
    button_13 = Button(
        image=button_image_13,
        highlightthickness=0,
        command=lambda: create_google_form(),
        relief="flat"
    )

    button_label_13 = Label(canvas, image = button_image_13)
    button_label_13.image = button_image_13
    
    button_13.place(
        x=32.3984375,
        y=370.6551513671875,
        width=203.8076171875,
        height=21.4437255859375
    )

    image_button_13 = canvas.create_image(
        134.3022461,
        381.3770142,
        image=button_image_13
    )


    #add type of product
    button_image_14 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "button_14.png"))
    button_14 = Button(
        image=button_image_14,
        highlightthickness=0,
        command=lambda: create_add_type_of_product(),
        relief="flat"
    )

    button_label_14 = Label(canvas, image = button_image_14)
    button_label_14.image = button_image_14
    
    button_14.place(
        x=32.3984375,
        y=321.7023010253906,
        width=203.8076171875,
        height=21.443756103515625
    )

    image_button_14 = canvas.create_image(
        134.3022461,
        332.4241791,
        image=button_image_14
    )


    #event settings
    button_image_15 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "button_15.png"))
    button_15 = Button(
        image=button_image_15,
        highlightthickness=0,
        command=lambda: create_event_settings(),
        relief="flat"
    )

    button_label_15 = Label(canvas, image = button_image_15)
    button_label_15.image = button_image_15
    
    button_15.place(
        x=32.3984375,
        y=394.7588806152344,
        width=203.8076171875,
        height=21.443756103515625
    )

    image_button_15 = canvas.create_image(
        134.3022461,
        405.4806848,
        image=button_image_15
    )


    #retrieve orders
    button_image_16 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "button_16.png"))
    button_16 = Button(
        image=button_image_16,
        highlightthickness=0,
        command=lambda: create_retrieve_orders(),
        relief="flat"
    )

    button_label_16 = Label(canvas, image = button_image_16)
    button_label_16.image = button_image_16
    
    button_16.place(
        x=32.3984375,
        y=297.4139404296875,
        width=203.8076171875,
        height=21.443756103515625
    )

    image_button_16 = canvas.create_image(
        134.3022464,
        307.7632721,
        image=button_image_16
    )


    #add products made
    button_image_17 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "button_17.png"))
    button_17 = Button(
        image=button_image_17,
        highlightthickness=0,
        command=lambda: create_add_products_made(),
        relief="flat"
    )

    button_label_17 = Label(canvas, image = button_image_17)
    button_label_17.image = button_image_17
    
    button_17.place(
        x=32.3984375,
        y=248.83721923828125,
        width=203.8076171875,
        height=21.44378662109375
    )

    image_button_17 = canvas.create_image(
        134.3022461,
        259.5591125,
        image=button_image_17
    )


    #display tables
    button_image_18 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "button_18.png"))
    button_18 = Button(
        image=button_image_18,
        highlightthickness=0,
        command=lambda: create_display_tables(),
        relief="flat"
    )

    button_label_18 = Label(canvas, image = button_image_18)
    button_label_18.image = button_image_18
    
    button_18.place(
        x=32.3984375,
        y=552.5751342773438,
        width=203.8076171875,
        height=21.4437255859375
    )

    image_button_18 = canvas.create_image(
        134.3022461,
        563.2969971,
        image=button_image_18
    )


    #display charts
    button_image_19 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "button_19.png"))
    button_19 = Button(
        image=button_image_19,
        highlightthickness=0,
        command=lambda: create_display_charts(),
        relief="flat"
    )

    button_label_19 = Label(canvas, image = button_image_19)
    button_label_19.image = button_image_19
    
    button_19.place(
        x=32.3984375,
        y=528.2867431640625,
        width=203.8076171875,
        height=21.44378662109375
    )

    image_button_19 = canvas.create_image(
        134.3022461,
        539.0086365,
        image=button_image_19
    )


    #delete product type
    button_image_20 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "button_20.png"))
    button_20 = Button(
        image=button_image_20,
        highlightthickness=0,
        command=lambda: create_delete_product_type(),
        relief="flat"
    )

    button_label_20 = Label(canvas, image = button_image_20)
    button_label_20.image = button_image_20
    
    button_20.place(
        x=32.3984375,
        y=601.15185546875,
        width=203.8076171875,
        height=21.44378662109375
    )

    image_button_20 = canvas.create_image(
        134.3022461,
        611.8737488,
        image=button_image_20
    )


    #add new product
    button_image_21 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "button_21.png"))
    button_21 = Button(
        image=button_image_21,
        highlightthickness=0,
        command=lambda: create_add_new_product(),
        relief="flat"
    )

    button_label_21 = Label(canvas, image = button_image_21)
    button_label_21.image = button_image_21
    
    button_21.place(
        x=32.3984375,
        y=576.863525390625,
        width=203.8076171875,
        height=21.4437255859375
    )

    image_button_21 = canvas.create_image(
        134.3022461,
        587.5853882,
        image=button_image_21
    )


    #delete an event
    button_image_22 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "button_22.png"))
    button_22 = Button(
        image=button_image_22,
        highlightthickness=0,
        command=lambda: create_delete_an_event(),
        relief="flat"
    )

    button_label_22 = Label(canvas, image = button_image_22)
    button_label_22.image = button_image_22
    
    button_22.place(
        x=32.3984375,
        y=650.2776489257812,
        width=203.8076171875,
        height=21.44378662109375
    )

    image_button_22 = canvas.create_image(
        134.3022461,
        660.9995422,
        image=button_image_22
    )


    #create new event
    button_image_23 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "button_23.png"))
    button_23 = Button(
        image=button_image_23,
        highlightthickness=0,
        command=lambda: create_create_new_event(),
        relief="flat"
    )

    button_label_23 = Label(canvas, image = button_image_23)
    button_label_23.image = button_image_23
    
    button_23.place(
        x=32.3984375,
        y=625.9893188476562,
        width=203.8076171875,
        height=21.4437255859375
    )

    image_button_23 = canvas.create_image(
        134.3022461,
        636.7111816,
        image=button_image_23
    )
    

    #add products sold
    button_image_24 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "button_24.png"))
    button_24 = Button(
        image=button_image_24,
        highlightthickness=0,
        command=lambda: create_add_products_sold(),
        relief="flat"
    )

    button_label_24 = Label(canvas, image = button_image_24)
    button_label_24.image = button_image_24
    
    button_24.place(
        x=32.3984375,
        y=273.1255798339844,
        width=203.8076171875,
        height=21.443756103515625
    )

    image_button_24 = canvas.create_image(
        134.3022461,
        283.8474579,
        image=button_image_24
    )


    #add time spent
    button_image_25 = PhotoImage(
        file=relative_to_assets(direc = 'dashboard', path = "button_25.png"))
    button_25 = Button(
        image=button_image_25,
        highlightthickness=0,
        command=lambda: create_add_time_spent(),
        relief="flat"
    )

    button_label_25 = Label(canvas, image = button_image_25)
    button_label_25.image = button_image_25
    
    button_25.place(
        x=32.3984375,
        y=346.1821594238281,
        width=203.8076171875,
        height=21.44378662109375
    )

    image_button_25 = canvas.create_image(
        134.3022461,
        356.9040527,
        image=button_image_25
    )




##########################################################################################################################################################################################################

def initial_login_page():

    def delete_login_page():
            
        canvas.itemconfig(lp1, state = 'hidden')
        canvas.itemconfig(lp2, state = 'hidden')
        canvas.itemconfig(lp3, state = 'hidden')
        canvas.itemconfig(lp4, state = 'hidden')
        canvas.itemconfig(lp5, state = 'hidden')
        canvas.itemconfig(lp6, state = 'hidden')
        canvas.itemconfig(lp7, state = 'hidden')

        lp_button_1.lower()
        
        if initial_glitch == True:
            create_main_frame(odd_initial = False)
        elif initial_glitch == False:
            create_main_frame(odd_initial = True)

    def connect():

        global form_service
        global drive_service
        global folder_id
        global data
        global data_fileId
        global func
        global chec
        global form
        global undo

        form_service, drive_service = token().return_form_service()
        
        folder_id = drive_check(drive_service = drive_service)
        data, data_fileId = data_retrieve(drive_service = drive_service, folder_id = folder_id)
        #note that data_fileId is the fileId for data.json in the drive

        func = function_input(datafile = data)
        chec = function_check(datafile = data)
        form = function_forms(datafile = data,
                              form_service = form_service,
                              drive_service = drive_service,
                              folder_id = folder_id)

        undo = undo_func(datafile = data,
                         undofile = undo_init(),
                         form_service = form_service,
                         drive_service = drive_service,
                         folder_id = folder_id
                         )

        chec.refresh_YD_product()

        delete_login_page()



    lp_image_1 = PhotoImage(
        file=relative_to_assets(direc = 'Login page', path = "image_1.png"))
    lp1 = canvas.create_image(
        640.5,
        400.5,
        image=lp_image_1
    )

    lp_label_1 = Label(canvas, image = lp_image_1)
    lp_label_1.image = lp_image_1

    lp_image_2 = PhotoImage(
        file=relative_to_assets(direc = 'Login page', path = "image_2.png"))
    lp2 = canvas.create_image(
        639.5,
        389.0,
        image=lp_image_2
    )

    lp_label_2 = Label(canvas, image = lp_image_2)
    lp_label_2.image = lp_image_2

    lp_button_image_1 = PhotoImage(
        file=relative_to_assets(direc = 'Login page', path = "button_1.png"))
    lp_button_1 = Button(
        image=lp_button_image_1,
        highlightthickness=0,
        command=lambda: connect(),
        #command = lambda: delete_login_page(),
        relief="flat"
    )
    lp_button_1.place(
        x=540.0,
        y=531.0,
        width=199.0,
        height=59.0
    )

    lp_button_label_1 = Label(canvas, image = lp_button_image_1)
    lp_button_label_1.image = lp_button_image_1

    lp_image_3 = PhotoImage(
        file=relative_to_assets(direc = 'Login page', path = "image_3.png"))
    lp3 = canvas.create_image(
        640.0,
        368.0,
        image=lp_image_3
    )

    lp_label_3 = Label(canvas, image = lp_image_3)
    lp_label_3.image = lp_image_3

    lp4 = canvas.create_text(
        511.0,
        211.0,
        anchor="nw",
        text="Welcome Back!",
        fill="#FFFFFF",
        font=("ABeeZee Regular", 37 * -1)
    )

    lp_image_4 = PhotoImage(
        file=relative_to_assets(direc = 'Login page', path = "image_4.png"))
    lp5 = canvas.create_image(
        88.0009765625,
        29.419921875,
        image=lp_image_4
    )

    lp_label_4 = Label(canvas, image = lp_image_4)
    lp_label_4.image = lp_image_4

    lp6 = canvas.create_text(
        529.0,
        479.0,
        anchor="nw",
        text="You will be redirected to your web",
        fill="#FFFFFF",
        font=("ABeeZee", 14 * -1)
    )

    lp7 = canvas.create_text(
        529.0,
        496.0,
        anchor="nw",
        text="browser to sign into your account.",
        fill="#FFFFFF",
        font=("ABeeZee", 14 * -1)
    )
    

##########################################################################################################################################################################################################

'''delete token id'''

def remove_userid():
    import os
    os.remove('token.json')
    global initial_glitch
    initial_glitch = True

'''initialiser'''

def initialise():
    
    #check if user is already log in
    login_ed = token().check_id_existence()

    if login_ed == False:

        initial_login_page()

    else:

        global form_service
        global drive_service
        global folder_id
        global data
        global data_fileId
        global func
        global chec
        global form
        global undo

        form_service, drive_service = token().return_form_service()

        folder_id = drive_check(drive_service = drive_service)
        data, data_fileId = data_retrieve(drive_service = drive_service, folder_id = folder_id)
        #note that data_fileId is the fileId for data.json in the drive

        func = function_input(datafile = data)
        chec = function_check(datafile = data)
        form = function_forms(datafile = data,
                              form_service = form_service,
                              drive_service = drive_service,
                              folder_id = folder_id)

        undo = undo_func(datafile = data,
                         undofile = undo_init(),
                         form_service = form_service,
                         drive_service = drive_service,
                         folder_id = folder_id
                         )

        chec.refresh_YD_product()

        create_main_frame(odd_initial = False)

#run initialisation
check_connection()
initialise()


window.mainloop()
