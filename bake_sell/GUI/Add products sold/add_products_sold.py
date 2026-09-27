from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, END


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def temp_text(e):
    entry_1.delete(0, END)

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
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    640.0087890625,
    400.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    639.8017578125,
    399.6600341796875,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    639.3779296875,
    399.2175598144531,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    639.3779296875,
    406.652099609375,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    639.376953125,
    338.652099609375,
    image=image_image_5
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=665.0,
    y=487.0,
    width=61.75,
    height=19.0
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    639.4404296875,
    383.2812194824219,
    image=image_image_6
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=765.5009765625,
    y=379.5,
    width=14,
    height=7
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    639.4404296875,
    430.22418212890625,
    image=image_image_7
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    642.5,
    430.0,
    image=entry_image_1
)
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
entry_1.place(
    x=494.0,
    y=422.0,
    width=297.0,
    height=15.0
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    639.376953125,
    475.2358093261719,
    image=image_image_8
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=735.0,
    y=487.0,
    width=63.0,
    height=19.0
)

canvas.create_text(
    481.5009765625,
    304.5,
    anchor="nw",
    text="Add Products Sold",
    fill="#D1D3D4",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    494.0009765625,
    377.0,
    anchor="nw",
    text="Product Name",
    fill="#000000",
    font=("Inter", 11 * -1)
)

canvas.create_text(
    494.0009765625,
    422.5,
    anchor="nw",
    text="Amount of products sold",
    fill="#000000",
    font=("Inter", 11 * -1)
)
window.resizable(False, False)
window.mainloop()
