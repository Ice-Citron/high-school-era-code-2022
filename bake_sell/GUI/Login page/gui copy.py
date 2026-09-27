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
    file=relative_to_assets(direc = 'Login page', path = "image_1.png"))
image_1 = canvas.create_image(
    640.5,
    400.5,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets(direc = 'Login page', path = "image_2.png"))
image_2 = canvas.create_image(
    639.5,
    389.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets(direc = 'Login page', path = "button_1.png"))
button_1 = Button(
    image=button_image_1,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=540.0,
    y=531.0,
    width=199.0,
    height=59.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets(direc = 'Login page', path = "image_3.png"))
image_3 = canvas.create_image(
    640.0,
    368.0,
    image=image_image_3
)

canvas.create_text(
    511.0,
    211.0,
    anchor="nw",
    text="Welcome Back!",
    fill="#FFFFFF",
    font=("ABeeZee Regular", 37 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets(direc = 'Login page', path = "image_4.png"))
image_4 = canvas.create_image(
    88.0009765625,
    29.419921875,
    image=image_image_4
)

canvas.create_text(
    529.0,
    479.0,
    anchor="nw",
    text="You will be redirected to your web",
    fill="#FFFFFF",
    font=("ABeeZee", 14 * -1)
)

canvas.create_text(
    529.0,
    496.0,
    anchor="nw",
    text="browser to sign into your account.",
    fill="#FFFFFF",
    font=("ABeeZee", 14 * -1)
)
window.resizable(False, False)
window.mainloop()
