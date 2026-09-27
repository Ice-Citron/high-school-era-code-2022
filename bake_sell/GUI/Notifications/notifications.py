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
    file=relative_to_assets(direc = 'Notifications', path = "image_1.png"))
image_1 = canvas.create_image(
    639.001953125,
    400.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets(direc = 'Notifications', path = "image_2.png"))
image_2 = canvas.create_image(
    921.5625,
    286.37353515625,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets(direc = 'Notifications', path = "image_3.png"))
image_3 = canvas.create_image(
    921.33984375,
    286.16064453125,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets(direc = 'Notifications', path = "image_4.png"))
image_4 = canvas.create_image(
    921.33984375,
    289.99072265625,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets(direc = 'Notifications', path = "image_5.png"))
image_5 = canvas.create_image(
    921.33984375,
    137.99072265625,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets(direc = 'Notifications', path = "image_6.png"))
image_6 = canvas.create_image(
    921.33984375,
    443.63134765625,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets(direc = 'Notifications', path = "image_7.png"))
image_7 = canvas.create_image(
    921.58984375,
    424.28125,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets(direc = 'Notifications', path = "image_8.png"))
image_8 = canvas.create_image(
    771.716796875,
    424.21875,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets(direc = 'Notifications', path = "image_9.png"))
image_9 = canvas.create_image(
    921.5,
    393.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets(direc = 'Notifications', path = "image_10.png"))
image_10 = canvas.create_image(
    772.0,
    393.0,
    image=image_image_10
)

button_image_1 = PhotoImage(
    file=relative_to_assets(direc = 'Notifications', path = "button_1.png"))
button_1 = Button(
    image=button_image_1,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=1009.0,
    y=456.0,
    width=61,
    height=17
)

canvas.create_text(
    792.0,
    419.0,
    anchor="nw",
    text="You are all set!",
    fill="#D1D3D4",
    font=("Inter", 9 * -1)
)

canvas.create_text(
    792.0,
    388.0,
    anchor="nw",
    text="Error. Input for sell price must be a number.",
    fill="#D1D3D4",
    font=("Inter", 9 * -1)
)

canvas.create_text(
    763.0,
    107.0,
    anchor="nw",
    text="Alerts",
    fill="#D1D3D4",
    font=("Inter", 20 * -1)
)
window.resizable(False, False)
window.mainloop()
