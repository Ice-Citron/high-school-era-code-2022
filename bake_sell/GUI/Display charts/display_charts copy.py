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
    file=relative_to_assets(direc = 'Display charts', path = "image_1.png"))
image_1 = canvas.create_image(
    640.0,
    400.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets(direc = 'Display charts', path = "image_2.png"))
image_2 = canvas.create_image(
    639.0556640625,
    399.523193359375,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets(direc = 'Display charts', path = "image_3.png"))
image_3 = canvas.create_image(
    639.0078125,
    399.428466796875,
    image=image_image_3
)

canvas.create_rectangle(
    246.0078125,
    202.24560546875,
    1033,
    642.5537109375,
    fill="#171819",
    outline="")

image_image_4 = PhotoImage(
    file=relative_to_assets(direc = 'Display charts', path = "image_4.png"))
image_4 = canvas.create_image(
    639.005859375,
    202.24560546875,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets(direc = 'Display charts', path = "image_5.png"))
image_5 = canvas.create_image(
    639.005859375,
    642.5537109375,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets(direc = 'Display charts', path = "image_6.png"))
image_6 = canvas.create_image(
    453.056640625,
    320.20556640625,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets(direc = 'Display charts', path = "image_7.png"))
image_7 = canvas.create_image(
    453.79296875,
    531.7265625,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets(direc = 'Display charts', path = "image_8.png"))
image_8 = canvas.create_image(
    823.28125,
    320.20556640625,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets(direc = 'Display charts', path = "image_9.png"))
image_9 = canvas.create_image(
    824.0185546875,
    531.7265625,
    image=image_image_9
)

button_image_1 = PhotoImage(
    file=relative_to_assets(direc = 'Display charts', path = "button_1.png"))
button_1 = Button(
    image=button_image_1,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=915.5009765625,
    y=663.79931640625,
    width=79,
    height=22
)

button_image_2 = PhotoImage(
    file=relative_to_assets(direc = 'Display charts', path = "button_2.png"))
button_2 = Button(
    image=button_image_2,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=574.0009765625,
    y=402.5,
    width=42,
    height=8
)

button_image_3 = PhotoImage(
    file=relative_to_assets(direc = 'Display charts', path = "button_3.png"))
button_3 = Button(
    image=button_image_3,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=532.0009765625,
    y=402.5,
    width=29,
    height=8
)

button_image_4 = PhotoImage(
    file=relative_to_assets(direc = 'Display charts', path = "button_4.png"))
button_4 = Button(
    image=button_image_4,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=571.0009765625,
    y=613.5,
    width=43.0,
    height=8
)

button_image_5 = PhotoImage(
    file=relative_to_assets(direc = 'Display charts', path = "button_5.png"))
button_5 = Button(
    image=button_image_5,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=529.0009765625,
    y=613.5,
    width=29.0,
    height=9.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets(direc = 'Display charts', path = "button_6.png"))
button_6 = Button(
    image=button_image_6,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=944.5009765625,
    y=402.5,
    width=42,
    height=8
)

button_image_7 = PhotoImage(
    file=relative_to_assets(direc = 'Display charts', path = "button_7.png"))
button_7 = Button(
    image=button_image_7,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=902.0009765625,
    y=402.5,
    width=29.0,
    height=8
)

button_image_8 = PhotoImage(
    file=relative_to_assets(direc = 'Display charts', path = "button_8.png"))
button_8 = Button(
    image=button_image_8,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=941.5009765625,
    y=613.5,
    width=42,
    height=8
)

button_image_9 = PhotoImage(
    file=relative_to_assets(direc = 'Display charts', path = "button_9.png"))
button_9 = Button(
    image=button_image_9,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=899.0009765625,
    y=613.5,
    width=29.0,
    height=8
)

canvas.create_text(
    288.5,
    148.5,
    anchor="nw",
    text="Display charts",
    fill="#D1D3D4",
    font=("Inter", 28 * -1)
)

canvas.create_text(
    287.0,
    219.0,
    anchor="nw",
    text="Revenue",
    fill="#D1D3D4",
    font=("Inter", 18 * -1)
)

canvas.create_text(
    658.0,
    219.0,
    anchor="nw",
    text="Profit\n",
    fill="#D1D3D4",
    font=("Inter", 18 * -1)
)

canvas.create_text(
    287.0,
    430.0,
    anchor="nw",
    text="Cost",
    fill="#D1D3D4",
    font=("Inter", 18 * -1)
)

canvas.create_text(
    658.0,
    430.0,
    anchor="nw",
    text="Time Spent\n\n",
    fill="#D1D3D4",
    font=("Inter", 18 * -1)
)
window.resizable(False, False)
window.mainloop()
