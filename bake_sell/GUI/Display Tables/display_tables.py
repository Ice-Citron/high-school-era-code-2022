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
    640.0,
    400.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    640.0,
    400.0,
    image=image_image_3
)

canvas.create_rectangle(
    246.0,
    202.0,
    1034.001953125,
    643.0,
    fill="#171819",
    outline="")

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    640.0,
    202.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    640.0,
    643.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    453.0,
    321.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    454.0,
    532.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    823.0,
    321.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    824.0,
    532.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    376.0,
    266.0,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    376.0,
    293.0,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    376.0,
    321.0,
    image=image_image_12
)

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    376.0,
    348.0,
    image=image_image_13
)

image_image_14 = PhotoImage(
    file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(
    530.0,
    266.0,
    image=image_image_14
)

image_image_15 = PhotoImage(
    file=relative_to_assets("image_15.png"))
image_15 = canvas.create_image(
    530.0,
    293.0,
    image=image_image_15
)

image_image_16 = PhotoImage(
    file=relative_to_assets("image_16.png"))
image_16 = canvas.create_image(
    530.0,
    321.0,
    image=image_image_16
)

image_image_17 = PhotoImage(
    file=relative_to_assets("image_17.png"))
image_17 = canvas.create_image(
    530.0,
    348.0,
    image=image_image_17
)

image_image_18 = PhotoImage(
    file=relative_to_assets("image_18.png"))
image_18 = canvas.create_image(
    376.0,
    375.0,
    image=image_image_18
)

image_image_19 = PhotoImage(
    file=relative_to_assets("image_19.png"))
image_19 = canvas.create_image(
    530.0,
    375.0,
    image=image_image_19
)

image_image_20 = PhotoImage(
    file=relative_to_assets("image_20.png"))
image_20 = canvas.create_image(
    376.0,
    478.0,
    image=image_image_20
)

image_image_21 = PhotoImage(
    file=relative_to_assets("image_21.png"))
image_21 = canvas.create_image(
    376.0,
    505.0,
    image=image_image_21
)

image_image_22 = PhotoImage(
    file=relative_to_assets("image_22.png"))
image_22 = canvas.create_image(
    376.0,
    532.0,
    image=image_image_22
)

image_image_23 = PhotoImage(
    file=relative_to_assets("image_23.png"))
image_23 = canvas.create_image(
    376.0,
    560.0,
    image=image_image_23
)

image_image_24 = PhotoImage(
    file=relative_to_assets("image_24.png"))
image_24 = canvas.create_image(
    530.0,
    478.0,
    image=image_image_24
)

image_image_25 = PhotoImage(
    file=relative_to_assets("image_25.png"))
image_25 = canvas.create_image(
    530.0,
    505.0,
    image=image_image_25
)

image_image_26 = PhotoImage(
    file=relative_to_assets("image_26.png"))
image_26 = canvas.create_image(
    530.0,
    532.0,
    image=image_image_26
)

image_image_27 = PhotoImage(
    file=relative_to_assets("image_27.png"))
image_27 = canvas.create_image(
    530.0,
    560.0,
    image=image_image_27
)

image_image_28 = PhotoImage(
    file=relative_to_assets("image_28.png"))
image_28 = canvas.create_image(
    748.0,
    266.0,
    image=image_image_28
)

image_image_29 = PhotoImage(
    file=relative_to_assets("image_29.png"))
image_29 = canvas.create_image(
    748.0,
    293.0,
    image=image_image_29
)

image_image_30 = PhotoImage(
    file=relative_to_assets("image_30.png"))
image_30 = canvas.create_image(
    748.0,
    321.0,
    image=image_image_30
)

image_image_31 = PhotoImage(
    file=relative_to_assets("image_31.png"))
image_31 = canvas.create_image(
    748.0,
    348.0,
    image=image_image_31
)

image_image_32 = PhotoImage(
    file=relative_to_assets("image_32.png"))
image_32 = canvas.create_image(
    902.001953125,
    266.0,
    image=image_image_32
)

image_image_33 = PhotoImage(
    file=relative_to_assets("image_33.png"))
image_33 = canvas.create_image(
    902.001953125,
    293.0,
    image=image_image_33
)

image_image_34 = PhotoImage(
    file=relative_to_assets("image_34.png"))
image_34 = canvas.create_image(
    902.001953125,
    321.0,
    image=image_image_34
)

image_image_35 = PhotoImage(
    file=relative_to_assets("image_35.png"))
image_35 = canvas.create_image(
    902.001953125,
    348.0,
    image=image_image_35
)

image_image_36 = PhotoImage(
    file=relative_to_assets("image_36.png"))
image_36 = canvas.create_image(
    748.0,
    375.0,
    image=image_image_36
)

image_image_37 = PhotoImage(
    file=relative_to_assets("image_37.png"))
image_37 = canvas.create_image(
    902.001953125,
    375.0,
    image=image_image_37
)

image_image_38 = PhotoImage(
    file=relative_to_assets("image_38.png"))
image_38 = canvas.create_image(
    748.0,
    478.0,
    image=image_image_38
)

image_image_39 = PhotoImage(
    file=relative_to_assets("image_39.png"))
image_39 = canvas.create_image(
    748.0,
    505.0,
    image=image_image_39
)

image_image_40 = PhotoImage(
    file=relative_to_assets("image_40.png"))
image_40 = canvas.create_image(
    748.0,
    532.0,
    image=image_image_40
)

image_image_41 = PhotoImage(
    file=relative_to_assets("image_41.png"))
image_41 = canvas.create_image(
    748.0,
    560.0,
    image=image_image_41
)

image_image_42 = PhotoImage(
    file=relative_to_assets("image_42.png"))
image_42 = canvas.create_image(
    902.001953125,
    478.0,
    image=image_image_42
)

image_image_43 = PhotoImage(
    file=relative_to_assets("image_43.png"))
image_43 = canvas.create_image(
    902.001953125,
    505.0,
    image=image_image_43
)

image_image_44 = PhotoImage(
    file=relative_to_assets("image_44.png"))
image_44 = canvas.create_image(
    902.001953125,
    532.0,
    image=image_image_44
)

image_image_45 = PhotoImage(
    file=relative_to_assets("image_45.png"))
image_45 = canvas.create_image(
    902.001953125,
    560.0,
    image=image_image_45
)

image_image_46 = PhotoImage(
    file=relative_to_assets("image_46.png"))
image_46 = canvas.create_image(
    748.0,
    587.0,
    image=image_image_46
)

image_image_47 = PhotoImage(
    file=relative_to_assets("image_47.png"))
image_47 = canvas.create_image(
    902.001953125,
    587.0,
    image=image_image_47
)

image_image_48 = PhotoImage(
    file=relative_to_assets("image_48.png"))
image_48 = canvas.create_image(
    376.0,
    587.0,
    image=image_image_48
)

image_image_49 = PhotoImage(
    file=relative_to_assets("image_49.png"))
image_49 = canvas.create_image(
    530.0,
    587.0,
    image=image_image_49
)

image_image_50 = PhotoImage(
    file=relative_to_assets("image_50.png"))
image_50 = canvas.create_image(
    748.0,
    587.0,
    image=image_image_50
)

image_image_51 = PhotoImage(
    file=relative_to_assets("image_51.png"))
image_51 = canvas.create_image(
    902.001953125,
    587.0,
    image=image_image_51
)

canvas.create_text(
    308.0,
    342.0,
    anchor="nw",
    text="Coke",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    436.0,
    342.0,
    anchor="nw",
    text="12",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    462.0,
    343.0,
    anchor="nw",
    text="Sprite",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    593.0,
    343.0,
    anchor="nw",
    text="3",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    308.0,
    315.0,
    anchor="nw",
    text="McDonalds",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    440.0,
    315.0,
    anchor="nw",
    text="9",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    462.0,
    315.0,
    anchor="nw",
    text="Rose",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    593.0,
    315.0,
    anchor="nw",
    text="2",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    308.0,
    287.0,
    anchor="nw",
    text="Amogus",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    436.0,
    287.0,
    anchor="nw",
    text="11",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    462.0,
    288.0,
    anchor="nw",
    text="Chocolate Chips Cookie",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    593.0,
    288.0,
    anchor="nw",
    text="7",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    308.0,
    260.0,
    anchor="nw",
    text="Cookies",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    433.0,
    260.0,
    anchor="nw",
    text="32",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    462.0,
    260.0,
    anchor="nw",
    text="Balloon",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    587.0,
    260.0,
    anchor="nw",
    text="22",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    308.0,
    369.0,
    anchor="nw",
    text="Sus",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    440.0,
    369.0,
    anchor="nw",
    text="2",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    462.0,
    369.0,
    anchor="nw",
    text="Reee",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    593.0,
    369.0,
    anchor="nw",
    text="3",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    308.0,
    554.0,
    anchor="nw",
    text="Coke",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    436.0,
    554.0,
    anchor="nw",
    text="12",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    462.0,
    554.0,
    anchor="nw",
    text="Sprite",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    593.0,
    554.0,
    anchor="nw",
    text="3",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    308.0,
    527.0,
    anchor="nw",
    text="McDonalds",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    440.0,
    527.0,
    anchor="nw",
    text="9",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    462.0,
    527.0,
    anchor="nw",
    text="Rose",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    593.0,
    527.0,
    anchor="nw",
    text="2",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    308.0,
    499.0,
    anchor="nw",
    text="Amogus",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    437.0,
    499.0,
    anchor="nw",
    text="11",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    462.0,
    499.0,
    anchor="nw",
    text="Chocolate Chips Cookie",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    593.0,
    499.0,
    anchor="nw",
    text="7",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    308.0,
    472.0,
    anchor="nw",
    text="Cookies",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    434.0,
    472.0,
    anchor="nw",
    text="32",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    462.0,
    472.0,
    anchor="nw",
    text="Balloon",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    587.0,
    472.0,
    anchor="nw",
    text="22",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    308.0,
    581.0,
    anchor="nw",
    text="Sus",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    440.0,
    581.0,
    anchor="nw",
    text="2",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    462.0,
    581.0,
    anchor="nw",
    text="Reee",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    593.0,
    581.0,
    anchor="nw",
    text="3",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    680.0,
    342.0,
    anchor="nw",
    text="Coke",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    808.001953125,
    342.0,
    anchor="nw",
    text="12",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    834.001953125,
    343.0,
    anchor="nw",
    text="Sprite",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    965.001953125,
    343.0,
    anchor="nw",
    text="3",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    680.0,
    315.0,
    anchor="nw",
    text="McDonalds",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    812.001953125,
    315.0,
    anchor="nw",
    text="9",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    834.001953125,
    315.0,
    anchor="nw",
    text="Rose",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    965.001953125,
    315.0,
    anchor="nw",
    text="2",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    680.0,
    287.0,
    anchor="nw",
    text="Amogus",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    808.001953125,
    287.0,
    anchor="nw",
    text="11",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    834.001953125,
    288.0,
    anchor="nw",
    text="Chocolate Chips Cookie",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    965.001953125,
    288.0,
    anchor="nw",
    text="7",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    680.0,
    260.0,
    anchor="nw",
    text="Cookies",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    805.001953125,
    260.0,
    anchor="nw",
    text="32",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    834.001953125,
    260.0,
    anchor="nw",
    text="Balloon",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    959.001953125,
    260.0,
    anchor="nw",
    text="22",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    680.0,
    369.0,
    anchor="nw",
    text="Sus",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    812.001953125,
    369.0,
    anchor="nw",
    text="2",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    834.001953125,
    369.0,
    anchor="nw",
    text="Reee",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    965.001953125,
    369.0,
    anchor="nw",
    text="3",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    680.0,
    554.0,
    anchor="nw",
    text="Coke",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    808.001953125,
    554.0,
    anchor="nw",
    text="12",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    834.001953125,
    554.0,
    anchor="nw",
    text="Sprite",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    965.001953125,
    554.0,
    anchor="nw",
    text="3",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    680.0,
    527.0,
    anchor="nw",
    text="McDonalds",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    812.001953125,
    527.0,
    anchor="nw",
    text="9",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    834.001953125,
    527.0,
    anchor="nw",
    text="Rose",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    965.001953125,
    527.0,
    anchor="nw",
    text="2",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    680.0,
    499.0,
    anchor="nw",
    text="Amogus",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    809.001953125,
    499.0,
    anchor="nw",
    text="11",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    834.001953125,
    499.0,
    anchor="nw",
    text="Chocolate Chips Cookie",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    965.001953125,
    499.0,
    anchor="nw",
    text="7",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    680.0,
    472.0,
    anchor="nw",
    text="Cookies",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    806.001953125,
    472.0,
    anchor="nw",
    text="32",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    834.001953125,
    472.0,
    anchor="nw",
    text="Balloon",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    959.001953125,
    472.0,
    anchor="nw",
    text="22",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    680.0,
    581.0,
    anchor="nw",
    text="Sus",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    812.001953125,
    581.0,
    anchor="nw",
    text="2",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    834.001953125,
    581.0,
    anchor="nw",
    text="Reee",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    965.001953125,
    581.0,
    anchor="nw",
    text="3",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
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
    x=915.501953125,
    y=663.79931640625,
    width=79,
    height=22
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
    x=941.501953125,
    y=613.5,
    width=43,
    height=8
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
    x=899.001953125,
    y=613.5,
    width=29,
    height=8
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=945.001953125,
    y=402.5,
    width=43,
    height=8
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=902.501953125,
    y=402.5,
    width=29,
    height=8
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=574.5,
    y=402.5,
    width=43,
    height=8
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=532.0,
    y=402.5,
    width=29,
    height=8
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=571.5,
    y=613.5,
    width=43,
    height=8
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=529.0,
    y=613.5,
    width=29,
    height=8
)

canvas.create_text(
    288.0,
    221.0,
    anchor="nw",
    text="Product sold - Common",
    fill="#FFFFFF",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    658.0,
    221.0,
    anchor="nw",
    text="Product sold - Special Occasion",
    fill="#FFFFFF",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    287.0,
    431.0,
    anchor="nw",
    text="Net loss - Common",
    fill="#FFFFFF",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    657.0,
    431.0,
    anchor="nw",
    text="Net loss - Special Occasion",
    fill="#FFFFFF",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    287.0,
    148.0,
    anchor="nw",
    text="Display tables",
    fill="#D1D3D4",
    font=("Inter", 29 * -1)
)
window.resizable(False, False)
window.mainloop()
