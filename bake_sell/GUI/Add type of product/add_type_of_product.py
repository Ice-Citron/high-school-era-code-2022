from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
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
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    640.0,
    400.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    639.544921875,
    382.080078125,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    639.3779296875,
    381.818359375,
    image=image_image_3
)

canvas.create_rectangle(
    463.3779296875,
    330.43310546875,
    816.6259765625,
    443.684326171875,
    fill="#171819",
    outline="")

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    639.376953125,
    330.43310546875,
    image=image_image_4
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
    y=459.0,
    width=62.0,
    height=18.0
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    639.439453125,
    404.217041015625,
    image=image_image_5
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
    y=401.0,
    width=14,
    height=8.0
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    639.3779296875,
    443.684326171875,
    image=image_image_6
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
    x=736.0,
    y=459.0,
    width=62.0,
    height=18.0
)

canvas.create_text(
    494.0009765625,
    397.5,
    anchor="nw",
    text="Product Name",
    fill="#000000",
    font=("Inter", 11 * -1)
)

canvas.create_text(
    481.0,
    297.0,
    anchor="nw",
    text="Add Type of Product",
    fill="#D1D3D4",
    font=("Inter", 18 * -1)
)

canvas.create_text(
    486.7001953125,
    348.300048828125,
    anchor="nw",
    text="Note: You are now adding a new type of product for the current event.",
    fill="#D1D3D4",
    font=("Inter", 8 * -1)
)

canvas.create_text(
    487.0,
    360.0,
    anchor="nw",
    text="You are not adding a brand new type of product to the application.",
    fill="#D1D3D4",
    font=("Inter", 8 * -1)
)
window.resizable(False, False)
window.mainloop()
