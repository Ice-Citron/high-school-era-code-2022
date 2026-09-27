from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, END

def relative_to_assets(path: str) -> Path:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")
    print(OUTPUT_PATH)
    print(ASSETS_PATH)
    return ASSETS_PATH / Path(path)

def temp_text_1(e):
    entry_1.delete(0, END)

def temp_text_2(e):
    entry_2.delete(0, END)


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
    640.0029296875,
    400.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    639.7666015625,
    399.780029296875,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    639.3779296875,
    399.310302734375,
    image=image_image_3
)

canvas.create_rectangle(
    463.3779296875,
    320.744873046875,
    816,
    493.26611328125,
    fill="#171819",
    outline="")

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    639.376953125,
    320.744873046875,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    639.4404296875,
    359.87109375,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    639.4404296875,
    453.75732421875,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    639.4404296875,
    406.814208984375,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    639.376953125,
    493.26611328125,
    image=image_image_8
)

canvas.create_text(
    494.0009765625,
    353.0,
    anchor="nw",
    text="Product Name",
    fill="#000000",
    font=("Inter", 11 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    640.5,
    407.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D1D3D4",
    fg="#000000",
    font=("Inter", 11 * -1),
    highlightthickness=0
)
entry_1.insert(0,"Amount of products made")
entry_1.pack()
entry_1.bind("<FocusIn>", temp_text_1) 
entry_1.place(
    x=494.0,
    y=399.0,
    width=293.0,
    height=16.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    640.5,
    454.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D1D3D4",
    fg="#000000",
    font=("Inter", 11 * -1),
    highlightthickness=0
)
entry_2.insert(0,"Cost to make products")
entry_2.pack()
entry_2.bind("<FocusIn>", temp_text_2) 
entry_2.place(
    x=494.0,
    y=446.0,
    width=293.0,
    height=16.0
)

canvas.create_text(
    494.5009765625,
    400.0,
    anchor="nw",
    text="Amount of products made",
    fill="#000000",
    font=("Inter", 11 * -1)
)

canvas.create_text(
    494.5009765625,
    447.0,
    anchor="nw",
    text="Cost to make products",
    fill="#000000",
    font=("Inter", 11 * -1)
)

canvas.create_text(
    481.5009765625,
    286.5,
    anchor="nw",
    text="Add Products made",
    fill="#D1D3D4",
    font=("Inter", 20 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=765.5009765625,
    y=356.0,
    width=14,
    height=8.0
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
    x=670.0009765625,
    y=506.5,
    width=61,
    height=17
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
    x=736.5009765625,
    y=506.5,
    width=61,
    height=17
)
window.resizable(False, False)
window.mainloop()
