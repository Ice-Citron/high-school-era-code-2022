from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, END


def relative_to_assets(direc: str, path: str) -> Path:
    two_level_up = Path(__file__).parents[1]
    
    OUTPUT_PATH = f"{two_level_up}/{direc}"
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")

    return ASSETS_PATH / Path(path)


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


window = Tk()

window.geometry("1280x800")
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
image_image_1 = PhotoImage(
    file=relative_to_assets(direc = 'Made an Error', path = "image_1.png"))
image_1 = canvas.create_image(
    640.0,
    400.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets(direc = 'Made an Error', path = "image_2.png"))
image_2 = canvas.create_image(
    639.6435546875,
    426.4892578125,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets(direc = 'Made an Error', path = "image_3.png"))
image_3 = canvas.create_image(
    639.36328125,
    399.27783203125,
    image=image_image_3
)

canvas.create_rectangle(
    315.36328125,
    173.0947265625,
    963.6376953125,
    675.573486328125,
    fill="#171819",
    outline="")

image_image_4 = PhotoImage(
    file=relative_to_assets(direc = 'Made an Error', path = "image_4.png"))
image_4 = canvas.create_image(
    639.3623046875,
    173.0947265625,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets(direc = 'Made an Error', path = "image_5.png"))
image_5 = canvas.create_image(
    639.3623046875,
    675.573486328125,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets(direc = 'Made an Error', path = "image_6.png"))
image_6 = canvas.create_image(
    639.3642578125,
    298.71435546875,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets(direc = 'Made an Error', path = "image_7.png"))
image_7 = canvas.create_image(
    639.3623046875,
    549.953857421875,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets(direc = 'Made an Error', path = "image_8.png"))
image_8 = canvas.create_image(
    639.3642578125,
    424.334228515625,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets(direc = 'Made an Error', path = "image_9.png"))
image_9 = canvas.create_image(
    464.609375,
    212.751708984375,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets(direc = 'Made an Error', path = "image_10.png"))
image_10 = canvas.create_image(
    434.0,
    253.0,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets(direc = 'Made an Error', path = "image_11.png"))
image_11 = canvas.create_image(
    637.333984375,
    253.0,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=relative_to_assets(direc = 'Made an Error', path = "image_12.png"))
image_12 = canvas.create_image(
    841.66015625,
    253.0,
    image=image_image_12
)

image_image_13 = PhotoImage(
    file=relative_to_assets(direc = 'Made an Error', path = "image_13.png"))
image_13 = canvas.create_image(
    465.1044921875,
    337.6552734375,
    image=image_image_13
)

image_image_14 = PhotoImage(
    file=relative_to_assets(direc = 'Made an Error', path = "image_14.png"))
image_14 = canvas.create_image(
    434.4951171875,
    377.90380859375,
    image=image_image_14
)

image_image_15 = PhotoImage(
    file=relative_to_assets(direc = 'Made an Error', path = "image_15.png"))
image_15 = canvas.create_image(
    637.830078125,
    377.90380859375,
    image=image_image_15
)

image_image_16 = PhotoImage(
    file=relative_to_assets(direc = 'Made an Error', path = "image_16.png"))
image_16 = canvas.create_image(
    465.1044921875,
    464.75244140625,
    image=image_image_16
)

image_image_17 = PhotoImage(
    file=relative_to_assets(direc = 'Made an Error', path = "image_17.png"))
image_17 = canvas.create_image(
    434.4951171875,
    505.0009765625,
    image=image_image_17
)

image_image_18 = PhotoImage(
    file=relative_to_assets(direc = 'Made an Error', path = "image_18.png"))
image_18 = canvas.create_image(
    465.1044921875,
    590.335205078125,
    image=image_image_18
)

image_image_19 = PhotoImage(
    file=relative_to_assets(direc = 'Made an Error', path = "image_19.png"))
image_19 = canvas.create_image(
    434.4951171875,
    630.583984375,
    image=image_image_19
)

image_image_20 = PhotoImage(
    file=relative_to_assets(direc = 'Made an Error', path = "image_20.png"))
image_20 = canvas.create_image(
    637.830078125,
    630.583984375,
    image=image_image_20
)

entry_image_1 = PhotoImage(
    file=relative_to_assets(direc = 'Made an Error', path = "entry_1.png"))
entry_bg_1 = canvas.create_image(
    637.5,
    254.0,
    image=entry_image_1
)
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

entry_image_2 = PhotoImage(
    file=relative_to_assets(direc = 'Made an Error', path = "entry_2.png"))
entry_bg_2 = canvas.create_image(
    842.5,
    254.0,
    image=entry_image_2
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

entry_image_3 = PhotoImage(
    file=relative_to_assets(direc = 'Made an Error', path = "entry_3.png"))
entry_bg_3 = canvas.create_image(
    637.5,
    379.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D1D3D4",
    fg="#000000",
    font=("Inter", 8 * -1),
    highlightthickness=0
)
entry_3.insert(0,"Amount of products made")
entry_3.pack()
entry_3.bind("<FocusIn>", temp_text_3) 
entry_3.place(
    x=547.0,
    y=373.0,
    width=181.0,
    height=12.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets(direc = 'Made an Error', path = "entry_4.png"))
entry_bg_4 = canvas.create_image(
    637.5,
    631.0,
    image=entry_image_4
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

entry_image_5 = PhotoImage(
    file=relative_to_assets(direc = 'Made an Error', path = "entry_4.png"))
entry_bg_5 = canvas.create_image(
    430,
    631.0,
    image=entry_image_5
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

canvas.create_text(
    344.390625,
    248.626953125,
    anchor="nw",
    text="Product Name",
    fill="#000000",
    font=("Inter", 8 * -1)
)

canvas.create_text(
    550.3916015625,
    248.626953125,
    anchor="nw",
    text="Amount of products made",
    fill="#000000",
    font=("Inter", 8 * -1)
)

canvas.create_text(
    344.390625,
    373.626953125,
    anchor="nw",
    text="Product Name",
    fill="#000000",
    font=("Inter", 8 * -1)
)

canvas.create_text(
    344.390625,
    500.626953125,
    anchor="nw",
    text="Product Name",
    fill="#000000",
    font=("Inter", 8 * -1)
)

canvas.create_text(
    344.890625,
    626.126953125,
    anchor="nw",
    text="Hours (enter 0 if none)",
    fill="#000000",
    font=("Inter", 8 * -1)
)

canvas.create_text(
    550.3916015625,
    626.126953125,
    anchor="nw",
    text="Minutes (enter 0 if none)",
    fill="#000000",
    font=("Inter", 8 * -1)
)

canvas.create_text(
    550.3916015625,
    373.626953125,
    anchor="nw",
    text="Amount of products made",
    fill="#000000",
    font=("Inter", 8 * -1)
)

canvas.create_text(
    753.8916015625,
    248.626953125,
    anchor="nw",
    text="Cost to make product",
    fill="#000000",
    font=("Inter", 8 * -1)
)

canvas.create_text(
    347.5,
    119.0,
    anchor="nw",
    text="Made an Error",
    fill="#D1D3D4",
    font=("Inter", 29 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets(direc = 'Made an Error', path = "button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=509.3916015625,
    y=503.126953125,
    width=10,
    height=5
)

button_image_2 = PhotoImage(
    file=relative_to_assets(direc = 'Made an Error', path = "button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=509.3916015625,
    y=375.626953125,
    width=10,
    height=5
)

button_image_3 = PhotoImage(
    file=relative_to_assets(direc = 'Made an Error', path = "button_3.png"))
button_3 = Button(
    image=button_image_3,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=805.0,
    y=271.79931640625,
    width=64,
    height=18
)

button_image_4 = PhotoImage(
    file=relative_to_assets(direc = 'Made an Error', path = "button_4.png"))
button_4 = Button(
    image=button_image_4,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=874.0693359375,
    y=271.79931640625,
    width=64,
    height=18
)

button_image_5 = PhotoImage(
    file=relative_to_assets(direc = 'Made an Error', path = "button_5.png"))
button_5 = Button(
    image=button_image_5,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=805.0,
    y=397.29931640625,
    width=64,
    height=18
)

button_image_6 = PhotoImage(
    file=relative_to_assets(direc = 'Made an Error', path = "button_6.png"))
button_6 = Button(
    image=button_image_6,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=874.0693359375,
    y=397.29931640625,
    width=64,
    height=18
)

button_image_7 = PhotoImage(
    file=relative_to_assets(direc = 'Made an Error', path = "button_7.png"))
button_7 = Button(
    image=button_image_7,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=805.0,
    y=523.29931640625,
    width=64,
    height=18
)

button_image_8 = PhotoImage(
    file=relative_to_assets(direc = 'Made an Error', path = "button_8.png"))
button_8 = Button(
    image=button_image_8,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=874.0693359375,
    y=523.29931640625,
    width=64,
    height=18
)

button_image_9 = PhotoImage(
    file=relative_to_assets(direc = 'Made an Error', path = "button_9.png"))
button_9 = Button(
    image=button_image_9,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=805.0,
    y=647.79931640625,
    width=64,
    height=18
)

button_image_10 = PhotoImage(
    file=relative_to_assets(direc = 'Made an Error', path = "button_10.png"))
button_10 = Button(
    image=button_image_10,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat"
)
button_10.place(
    x=874.0693359375,
    y=647.79931640625,
    width=64,
    height=18
)

button_image_11 = PhotoImage(
    file=relative_to_assets(direc = 'Made an Error', path = "button_11.png"))
button_11 = Button(
    image=button_image_11,
    highlightthickness=0,
    command=lambda: print("button_11 clicked"),
    relief="flat"
)
button_11.place(
    x=509.3916015625,
    y=250.626953125,
    width=10,
    height=5
)

button_image_12 = PhotoImage(
    file=relative_to_assets(direc = 'Made an Error', path = "button_12.png"))
button_12 = Button(
    image=button_image_12,
    highlightthickness=0,
    command=lambda: print("button_12 clicked"),
    relief="flat"
)
button_12.place(
    x=848.7509765625,
    y=694.5,
    width=79,
    height=22
)

canvas.create_text(
    359.0,
    205.0,
    anchor="nw",
    text="Delete products made",
    fill="#FFFFFF",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    359.0,
    330.0,
    anchor="nw",
    text="Delete products sold\n",
    fill="#FFFFFF",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    359.0,
    457.0,
    anchor="nw",
    text="Delete type of products in event\n",
    fill="#FFFFFF",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    359.0,
    583.0,
    anchor="nw",
    text="Delete time spent\n\n",
    fill="#FFFFFF",
    font=("Inter", 13 * -1)
)
window.resizable(False, False)
window.mainloop()
