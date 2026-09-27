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
    file=relative_to_assets(direc = 'Add new type of product', path = "image_1.png"))
image_1 = canvas.create_image(
    640.0,
    400.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets(direc = 'Add new type of product', path = "image_2.png"))
image_2 = canvas.create_image(
    639.80078125,
    399.7003173828125,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets(direc = 'Add new type of product', path = "image_3.png"))
image_3 = canvas.create_image(
    639.376953125,
    399.310302734375,
    image=image_image_3
)

canvas.create_rectangle(
    463.376953125,
    320.744873046875,
    815.625,
    493.2659912109375,
    fill="#171819",
    outline="")

image_image_4 = PhotoImage(
    file=relative_to_assets(direc = 'Add new type of product', path = "image_4.png"))
image_4 = canvas.create_image(
    639.375,
    320.744873046875,
    image=image_image_4
)

button_image_1 = PhotoImage(
    file=relative_to_assets(direc = 'Add new type of product', path = "button_1.png"))
button_1 = Button(
    image=button_image_1,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=665.0,
    y=506.5,
    width=61,
    height=17
)

image_image_5 = PhotoImage(
    file=relative_to_assets(direc = 'Add new type of product', path = "image_5.png"))
image_5 = canvas.create_image(
    639.439453125,
    359.8712158203125,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets(direc = 'Add new type of product', path = "image_6.png"))
image_6 = canvas.create_image(
    639.439453125,
    406.814208984375,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets(direc = 'Add new type of product', path = "image_7.png"))
image_7 = canvas.create_image(
    639.375,
    493.2659912109375,
    image=image_image_7
)

button_image_2 = PhotoImage(
    file=relative_to_assets(direc = 'Add new type of product', path = "button_2.png"))
button_2 = Button(
    image=button_image_2,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=731.501953125,
    y=506.5,
    width=62,
    height=17
)

button_image_3 = PhotoImage(
    file=relative_to_assets(direc = 'Add new type of product', path = "button_3.png"))
button_3 = Button(
    image=button_image_3,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=651.0,
    y=463.0,
    width=36.0,
    height=13.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets(direc = 'Add new type of product', path = "button_4.png"))
button_4 = Button(
    image=button_image_4,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=591.0,
    y=463.0,
    width=39.0,
    height=13.0
)


canvas.create_text(
    481.5,
    286.0,
    anchor="nw",
    text="Add New Type of Product",
    fill="#D1D3D4",
    font=("Inter", 20 * -1)
)

#####

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

#####

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

canvas.create_text(
    494.0,
    400.0,
    anchor="nw",
    text="Sell price",
    fill="#000000",
    font=("Inter", 11 * -1)
)

canvas.create_text(
    493.0,
    438.0,
    anchor="nw",
    text="Is this product only available during special ocasions?",
    fill="#FFFFFF",
    font=("Inter", 11 * -1)
)
window.resizable(False, False)
window.mainloop()
