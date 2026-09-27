from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1254x784")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 784,
    width = 1254,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    627.0,
    392.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    626.1220703125,
    391.82763671875,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    626.9638671875,
    391.5947265625,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    626.9638671875,
    397.42822265625,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    626.9638671875,
    342.42822265625,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    626.9638671875,
    452.79345703125,
    image=image_image_6
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
    x=651.4931640625,
    y=465.5,
    width=60,
    height=17
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=719.5810546875,
    y=465.5,
    width=60,
    height=17
)

canvas.create_text(
    472.0,
    311.0,
    anchor="nw",
    text="Deleting Google Form",
    fill="#D1D3D4",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    472.0,
    357.0,
    anchor="nw",
    text="Are you sure that you would like to delete this",
    fill="#D1D3D4",
    font=("Inter", 11 * -1)
)

canvas.create_text(
    472.0,
    372.0,
    anchor="nw",
    text="google form?",
    fill="#D1D3D4",
    font=("Inter", 11 * -1)
)

canvas.create_text(
    472.0,
    403.0,
    anchor="nw",
    text="You cannot undo this move. The data will be",
    fill="#D1D3D4",
    font=("Inter", 11 * -1)
)

canvas.create_text(
    472.0,
    418.0,
    anchor="nw",
    text="deleted permanently.",
    fill="#D1D3D4",
    font=("Inter", 11 * -1)
)
window.resizable(False, False)
window.mainloop()
