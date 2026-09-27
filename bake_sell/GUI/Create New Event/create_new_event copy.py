from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, END


def relative_to_assets(direc: str, path: str) -> Path:
    two_level_up = Path(__file__).parents[1]
    
    OUTPUT_PATH = f"{two_level_up}/{direc}"
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")

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
    file=relative_to_assets(direc = 'Create New Event', path = "image_1.png"))
image_1 = canvas.create_image(
    640.0,
    400.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets(direc = 'Create New Event', path = "image_2.png"))
image_2 = canvas.create_image(
    639.75,
    399.04833984375,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets(direc = 'Create New Event', path = "image_3.png"))
image_3 = canvas.create_image(
    639.1328125,
    399.37109375,
    image=image_image_3
)

canvas.create_rectangle(
    481.1328125,
    312.31591796875,
    797.8681640625,
    502.44482421875,
    fill="#171819",
    outline="")

image_image_4 = PhotoImage(
    file=relative_to_assets(direc = 'Create New Event', path = "image_4.png"))
image_4 = canvas.create_image(
    639.1318359375,
    311.31591796875,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets(direc = 'Create New Event', path = "image_5.png"))
image_5 = canvas.create_image(
    639.1318359375,
    501.44482421875,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets(direc = 'Create New Event', path = "image_6.png"))
image_6 = canvas.create_image(
    639.1318359375,
    408.58447265625,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets(direc = 'Create New Event', path = "image_7.png"))
image_7 = canvas.create_image(
    640.15234375,
    371.3701171875,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets(direc = 'Create New Event', path = "image_8.png"))
image_8 = canvas.create_image(
    564.724609375,
    465.03173828125,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets(direc = 'Create New Event', path = "image_9.png"))
image_9 = canvas.create_image(
    713.888671875,
    465.02978515625,
    image=image_image_9
)

entry_image_1 = PhotoImage(
    file=relative_to_assets(direc = 'Create New Event', path = "entry_1.png"))
entry_bg_1 = canvas.create_image(
    640.0,
    372.0,
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
    y=363.5,
    width=274.0,
    height=15.0
)

canvas.create_text(
    505.0009765625,
    365.0,
    anchor="nw",
    text="New name for event",
    fill="#000000",
    font=("Inter", 11 * -1)
)

canvas.create_text(
    540.5009765625,
    459.0,
    anchor="nw",
    text="Month",
    fill="#000000",
    font=("Inter", 11 * -1)
)

canvas.create_text(
    698.5009765625,
    459.0,
    anchor="nw",
    text="Day",
    fill="#000000",
    font=("Inter", 11 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets(direc = 'Create New Event', path = "button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=611.0009765625,
    y=462.0,
    width=14,
    height=8.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets(direc = 'Create New Event', path = "button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=760.5009765625,
    y=462.0,
    width=14,
    height=8.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets(direc = 'Create New Event', path = "button_3.png"))
button_3 = Button(
    image=button_image_3,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=719.896484375,
    y=517.5,
    width=62,
    height=17
)

button_image_4 = PhotoImage(
    file=relative_to_assets(direc = 'Create New Event', path = "button_4.png"))
button_4 = Button(
    image=button_image_4,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=654.31640625,
    y=517.5,
    width=62,
    height=17
)

canvas.create_text(
    500.0,
    334.0,
    anchor="nw",
    text="What is the name of this event?",
    fill="#D1D3D4",
    font=("Inter", 11 * -1)
)

canvas.create_text(
    500.0,
    428.0,
    anchor="nw",
    text="When will this even take place?",
    fill="#D1D3D4",
    font=("Inter", 11 * -1)
)

canvas.create_text(
    502.0,
    274.0,
    anchor="nw",
    text="Create New Event",
    fill="#D1D3D4",
    font=("Inter", 21 * -1)
)
window.resizable(False, False)
window.mainloop()
