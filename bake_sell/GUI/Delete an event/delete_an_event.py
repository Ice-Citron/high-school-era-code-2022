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
    639.5810546875,
    399.908203125,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    639.376953125,
    399.68408203125,
    image=image_image_3
)

canvas.create_rectangle(
    463.376953125,
    348.298828125,
    815.625,
    461.55029296875,
    fill="#171819",
    outline="")

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    639.3759765625,
    348.298828125,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    639.4384765625,
    422.0830078125,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    639.376953125,
    461.55029296875,
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
    x=670.5009765625,
    y=477.443359375,
    width=61,
    height=18
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
    x=736.0009765625,
    y=477.443359375,
    width=62,
    height=18
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
    x=765.0009765625,
    y=418.0,
    width=14,
    height=8.0
)

canvas.create_text(
    494.5009765625,
    415.0,
    anchor="nw",
    text="Event name",
    fill="#000000",
    font=("Inter", 11 * -1)
)

canvas.create_text(
    484.0,
    370.0,
    anchor="nw",
    text="Note: You are deleting an entire event! The deletion of an event is",
    fill="#D1D3D4",
    font=("Inter", 9 * -1)
)

canvas.create_text(
    484.0,
    381.0,
    anchor="nw",
    text="unrecoverable and you won’t be able to undo this move!",
    fill="#D1D3D4",
    font=("Inter", 9 * -1)
)

canvas.create_text(
    484.0,
    313.0,
    anchor="nw",
    text="Delete an Event",
    fill="#D1D3D4",
    font=("Inter", 20 * -1)
)
window.resizable(False, False)
window.mainloop()
