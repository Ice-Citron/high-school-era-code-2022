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
    file=relative_to_assets(direc = 'Delete product type', path = "image_1.png"))
image_1 = canvas.create_image(
    640.0009765625,
    400.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets(direc = 'Delete product type', path = "image_2.png"))
image_2 = canvas.create_image(
    639.568359375,
    399.908203125,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets(direc = 'Delete product type', path = "image_3.png"))
image_3 = canvas.create_image(
    639.376953125,
    399.68408203125,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets(direc = 'Delete product type', path = "image_4.png"))
image_4 = canvas.create_image(
    639.376953125,
    404.298828125,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets(direc = 'Delete product type', path = "image_5.png"))
image_5 = canvas.create_image(
    639.375,
    348.298828125,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets(direc = 'Delete product type', path = "image_6.png"))
image_6 = canvas.create_image(
    639.4375,
    422.0830078125,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets(direc = 'Delete product type', path = "image_7.png"))
image_7 = canvas.create_image(
    639.376953125,
    461.55029296875,
    image=image_image_7
)

button_image_1 = PhotoImage(
    file=relative_to_assets(direc = 'Delete product type', path = "button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=765.501953125,
    y=419.0,
    width=14,
    height=8.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets(direc = 'Delete product type', path = "button_2.png"))
button_2 = Button(
    image=button_image_2,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=665.0,
    y=477.443359375,
    width=61,
    height=17
)

button_image_3 = PhotoImage(
    file=relative_to_assets(direc = 'Delete product type', path = "button_3.png"))
button_3 = Button(
    image=button_image_3,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=736.001953125,
    y=477.443359375,
    width=61,
    height=17
)

canvas.create_text(
    494.0,
    415.5,
    anchor="nw",
    text="Product name",
    fill="#000000",
    font=("Inter", 11 * -1)
)

canvas.create_text(
    481.0,
    315.0,
    anchor="nw",
    text="Delete Product Type",
    fill="#D1D3D4",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    483.0,
    371.0,
    anchor="nw",
    text="Note: Your are deleeting the product from the application. It’s data will still",
    fill="#D1D3D4",
    font=("Inter", 8 * -1)
)

canvas.create_text(
    483.0,
    381.0,
    anchor="nw",
    text="remain but the product wouldn’t be used for new/current events anymore.",
    fill="#D1D3D4",
    font=("Inter", 8 * -1)
)
window.resizable(False, False)
window.mainloop()
