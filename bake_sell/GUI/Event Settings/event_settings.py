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
    640.0009765625,
    399.03326416015625,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    639.4609375,
    399.2303466796875,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    639.1337890625,
    399.81640625,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    639.1337890625,
    406.76123046875,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    639.1328125,
    289.76123046875,
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
    x=712.400390625,
    y=539.822998046875,
    width=62,
    height=17
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    639.1328125,
    524.316162109375,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    639.1328125,
    407.0386962890625,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    640.1533203125,
    342.870361328125,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    564.1533203125,
    458.7791748046875,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    713.3173828125,
    457.92529296875,
    image=image_image_10
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    639.5,
    343.0,
    image=entry_image_1
)
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
    y=335.5,
    width=273.0,
    height=15.0
)

canvas.create_text(
    505.0009765625,
    336.5,
    anchor="nw",
    text="New name for event",
    fill="#000000",
    font=("Inter", 11 * -1)
)

canvas.create_text(
    540.5009765625,
    452.5,
    anchor="nw",
    text="Month",
    fill="#000000",
    font=("Inter", 11 * -1)
)

canvas.create_text(
    698.5009765625,
    451.5,
    anchor="nw",
    text="Day",
    fill="#000000",
    font=("Inter", 11 * -1)
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
    x=611.5009765625,
    y=456.0,
    width=14,
    height=8.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=761.0009765625,
    y=455.5,
    width=14,
    height=8.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=609.5009765625,
    y=370.5,
    width=62,
    height=17
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=609.5009765625,
    y=487.0,
    width=62,
    height=17
)

canvas.create_text(
    502.5,
    253.5,
    anchor="nw",
    text="Event Settings",
    fill="#D1D3D4",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    499.0,
    304.0,
    anchor="nw",
    text="Change name of Bake Sale event",
    fill="#D1D3D4",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    499.0,
    421.0,
    anchor="nw",
    text="Change date for event",
    fill="#D1D3D4",
    font=("Inter", 12 * -1)
)
window.resizable(False, False)
window.mainloop()
