from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


def relative_to_assets(direc: str, path: str) -> Path:
    two_level_up = Path(__file__).parents[1]
    
    OUTPUT_PATH = f"{two_level_up}/{direc}"
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")

    return ASSETS_PATH / Path(path)


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
    file=relative_to_assets(direc = 'Delete an event note', path = "image_1.png"))
image_1 = canvas.create_image(
    640.0,
    400.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets(direc = 'Delete an event note', path = "image_2.png"))
image_2 = canvas.create_image(
    639.7705078125,
    399.0361328125,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets(direc = 'Delete an event note', path = "image_3.png"))
image_3 = canvas.create_image(
    639.376953125,
    399.58642578125,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets(direc = 'Delete an event note', path = "image_4.png"))
image_4 = canvas.create_image(
    639.376953125,
    405.4169921875,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets(direc = 'Delete an event note', path = "image_5.png"))
image_5 = canvas.create_image(
    639.0,
    349.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets(direc = 'Delete an event note', path = "image_6.png"))
image_6 = canvas.create_image(
    639.0,
    461.6171875,
    image=image_image_6
)

button_image_1 = PhotoImage(
    file=relative_to_assets(direc = 'Delete an event note', path = "button_1.png"))
button_1 = Button(
    image=button_image_1,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=666.5009765625,
    y=475.0,
    width=61,
    height=17
)

button_image_2 = PhotoImage(
    file=relative_to_assets(direc = 'Delete an event note', path = "button_2.png"))
button_2 = Button(
    image=button_image_2,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=736.0009765625,
    y=475.0,
    width=61,
    height=17
)

canvas.create_text(
    481.5009765625,
    317.5,
    anchor="nw",
    text="Deleting an Event",
    fill="#D1D3D4",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    482.0,
    370.0,
    anchor="nw",
    text="Are you sure that you like to delete this event?",
    fill="#D1D3D4",
    font=("Inter", 11 * -1)
)

canvas.create_text(
    482.0,
    401.0,
    anchor="nw",
    text="You canno undo this move. The data will be removed",
    fill="#D1D3D4",
    font=("Inter", 11 * -1)
)

canvas.create_text(
    482.0,
    417.0,
    anchor="nw",
    text="permanently.",
    fill="#D1D3D4",
    font=("Inter", 11 * -1)
)
window.resizable(False, False)
window.mainloop()
