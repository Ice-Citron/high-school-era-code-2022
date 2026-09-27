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
    file=relative_to_assets(direc = 'Google Forms', path = "image_1.png"))
image_1 = canvas.create_image(
    639.0009765625,
    400.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets(direc = 'Google Forms', path = "image_2.png"))
image_2 = canvas.create_image(
    639.484375,
    399.1103515625,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets(direc = 'Google Forms', path = "image_3.png"))
image_3 = canvas.create_image(
    639.1328125,
    399.78314208984375,
    image=image_image_3
)

canvas.create_rectangle(
    481.1328125,
    289.72802734375,
    797,
    524.2828979492188,
    fill="#171819",
    outline="")

canvas.create_rectangle(
    481.1328125,
    289.72802734375,
    797,
    289.72802734375,
    fill="#FFFFFF",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets(direc = 'Google Forms', path = "button_1.png"))
button_1 = Button(
    image=button_image_1,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=712.0,
    y=539.7898559570312,
    width=62.0,
    height=17.31134033203125
)

canvas.create_rectangle(
    481.1328125,
    524.2828979492188,
    797,
    524.2828979492188,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    481.1328125,
    404.1632995605469,
    797,
    404.1632995605469,
    fill="#FFFFFF",
    outline="")

image_image_4 = PhotoImage(
    file=relative_to_assets(direc = 'Google Forms', path = "image_4.png"))
image_4 = canvas.create_image(
    640.154296875,
    342.837158203125,
    image=image_image_4
)

button_image_2 = PhotoImage(
    file=relative_to_assets(direc = 'Google Forms', path = "button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=763.412109375,
    y=336.0,
    width=13,
    height=15.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets(direc = 'Google Forms', path = "button_3.png"))
button_3 = Button(
    image=button_image_3,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=499.0,
    y=370.0,
    width=83.30078125,
    height=19.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets(direc = 'Google Forms', path = "button_4.png"))
button_4 = Button(
    image=button_image_4,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=598.80859375,
    y=370.0,
    width=83.19140625,
    height=19.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets(direc = 'Google Forms', path = "button_5.png"))
button_5 = Button(
    image=button_image_5,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=698.0,
    y=370.0,
    width=83.15234375,
    height=19.0
)

image_image_5 = PhotoImage(
    file=relative_to_assets(direc = 'Google Forms', path = "image_5.png"))
image_5 = canvas.create_image(
    640.154296875,
    457.22332763671875,
    image=image_image_5
)

button_image_6 = PhotoImage(
    file=relative_to_assets(direc = 'Google Forms', path = "button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=763.001953125,
    y=450.5,
    width=13,
    height=15.0
)

image_image_6 = PhotoImage(
    file=relative_to_assets(direc = 'Google Forms', path = "image_6.png"))
image_6 = canvas.create_image(
    639.115234375,
    493.5879821777344,
    image=image_image_6
)

canvas.create_text(
    504.5,
    332.5,
    anchor="nw",
    text="Link: https://docs.google.com/forms/d/14NX8cA816CPq",
    fill="#2C2C33",
    font=("Inter", 9 * -1)
)

canvas.create_text(
    504.5,
    343.5,
    anchor="nw",
    text="z2ScefyhTs86kRzw1iU-rkTs_4EsPvg/edit",
    fill="#2C2C33",
    font=("Inter", 9 * -1)
)

canvas.create_text(
    504.5,
    447.0,
    anchor="nw",
    text="Link: https://docs.google.com/forms/d/14NX8cA816CPq",
    fill="#2C2C33",
    font=("Inter", 9 * -1)
)

canvas.create_text(
    504.5,
    458.0,
    anchor="nw",
    text="z2ScefyhTs86kRzw1iU-rkTs_4EsPvg/edit",
    fill="#2C2C33",
    font=("Inter", 9 * -1)
)

canvas.create_text(
    502.0,
    252.0,
    anchor="nw",
    text="Google Forms",
    fill="#D1D3D4",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    499.0,
    306.0,
    anchor="nw",
    text="Google Forms for pupil to enter their orders.",
    fill="#D1D3D4",
    font=("Inter", 11 * -1)
)

canvas.create_text(
    552.0,
    490.0,
    anchor="nw",
    text="Note that this form will be automatically created.",
    fill="#D1D3D4",
    font=("Inter", 7 * -1)
)

canvas.create_text(
    499.0,
    419.0,
    anchor="nw",
    text="Google Forms for workers to input orders.",
    fill="#D1D3D4",
    font=("Inter", 11 * -1)
)
window.resizable(False, False)
window.mainloop()
