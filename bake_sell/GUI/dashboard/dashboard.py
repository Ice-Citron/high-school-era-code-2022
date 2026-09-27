
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

import sys

sys.path.insert(1, '/Users/administrator/Python/bake_sell/GUI/Add products sold')
sys.path.insert(1, '/Users/administrator/Python/bake_sell/GUI/Google Forms')
sys.path.insert(1, '/Users/administrator/Python/bake_sell/GUI/Add type of product')
sys.path.insert(1, '/Users/administrator/Python/bake_sell/GUI/Event Settings')

sys.path.insert(1, '/Users/administrator/Python/bake_sell/GUI/Add time spent')
sys.path.insert(1, '/Users/administrator/Python/bake_sell/GUI/Add new type of product')
sys.path.insert(1, '/Users/administrator/Python/bake_sell/GUI/Add product made')
sys.path.insert(1, '/Users/administrator/Python/bake_sell/GUI/Display charts')
sys.path.insert(1, '/Users/administrator/Python/bake_sell/GUI/Made an Error')
sys.path.insert(1, '/Users/administrator/Python/bake_sell/GUI/Display Tables')

sys.path.insert(1, '/Users/administrator/Python/bake_sell/GUI/Create New Event')
sys.path.insert(1, '/Users/administrator/Python/bake_sell/GUI/Delete an event')
sys.path.insert(1, '/Users/administrator/Python/bake_sell/GUI/Delete product type')
sys.path.insert(1, '/Users/administrator/Python/bake_sell/GUI/Delete google form note')
sys.path.insert(1, '/Users/administrator/Python/bake_sell/GUI/Delete an event note')
sys.path.insert(1, '/Users/administrator/Python/bake_sell/GUI/Retrieve orders')

sys.path.insert(1, '/Users/administrator/Python/bake_sell/GUI/Notifications')

#import notifications

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets_dashboard")


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
canvas.create_rectangle(
    0.0,
    0.0,
    1280.0,
    800.0,
    fill="#010000",
    outline="")

canvas.create_rectangle(
    0.0,
    0.0,
    1280.0,
    99.26806640625,
    fill="#0E1012",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    758.6064453125,
    523.8638610839844,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    383.986328125,
    716.8245239257812,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    383.986328125,
    746.7545166015625,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    383.986328125,
    656.9639892578125,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    383.986328125,
    597.10400390625,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    383.986328125,
    567.1740112304688,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    383.986328125,
    537.2435302734375,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    383.986328125,
    507.3135070800781,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    383.986328125,
    627.0339965820312,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    383.986328125,
    686.8939819335938,
    image=image_image_10
)

canvas.create_text(
    294.0,
    710.50048828125,
    anchor="nw",
    text="Rocky Roads",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    459.5,
    710.5,
    anchor="nw",
    text="33",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    294.0,
    740.5,
    anchor="nw",
    text="Chocolate Chips",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    460.0,
    740.5,
    anchor="nw",
    text="56",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    294.0,
    651.0,
    anchor="nw",
    text="Books",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    468.5,
    651.0,
    anchor="nw",
    text="5",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    294.0,
    592.4139404296875,
    anchor="nw",
    text="Cheese cake",
    fill="#D1D3D4",
    font=("ArchivoRoman Regular", 10 * -1)
)

canvas.create_text(
    468.5,
    591.0,
    anchor="nw",
    text="3",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    294.0,
    561.0,
    anchor="nw",
    text="Sprite",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    469.0,
    561.0,
    anchor="nw",
    text="2",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    294.0,
    531.2254638671875,
    anchor="nw",
    text="Balloon",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    462.0,
    531.0,
    anchor="nw",
    text="12",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    294.0,
    501.0,
    anchor="nw",
    text="Cookies",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    460.0,
    501.0,
    anchor="nw",
    text="32",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    294.0,
    621.0,
    anchor="nw",
    text="Rose",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    470.5,
    621.0,
    anchor="nw",
    text="1",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    294.0,
    680.5,
    anchor="nw",
    text="Gold keys",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    469.0,
    680.5,
    anchor="nw",
    text="2",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    131.7373046875,
    452.85498046875,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    131.7373046875,
    752.8101196289062,
    image=image_image_12
)

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    131.7373046875,
    146.541015625,
    image=image_image_13
)

image_image_14 = PhotoImage(
    file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(
    1066.6640625,
    389.67120361328125,
    image=image_image_14
)

image_image_15 = PhotoImage(
    file=relative_to_assets("image_15.png"))
image_15 = canvas.create_image(
    1066.6640625,
    711.9931030273438,
    image=image_image_15
)

image_image_16 = PhotoImage(
    file=relative_to_assets("image_16.png"))
image_16 = canvas.create_image(
    701.5107421875,
    549.4396057128906,
    image=image_image_16
)

image_image_17 = PhotoImage(
    file=relative_to_assets("image_17.png"))
image_17 = canvas.create_image(
    700.701171875,
    455.1448669433594,
    image=image_image_17
)

image_image_18 = PhotoImage(
    file=relative_to_assets("image_18.png"))
image_18 = canvas.create_image(
    193.7470703125,
    49.44256591796875,
    image=image_image_18
)

image_image_19 = PhotoImage(
    file=relative_to_assets("image_19.png"))
image_19 = canvas.create_image(
    383.9833984375,
    399.67120361328125,
    image=image_image_19
)

image_image_20 = PhotoImage(
    file=relative_to_assets("image_20.png"))
image_20 = canvas.create_image(
    607.474609375,
    302.47021484375,
    image=image_image_20
)

image_image_21 = PhotoImage(
    file=relative_to_assets("image_21.png"))
image_21 = canvas.create_image(
    383.9833984375,
    626.9024658203125,
    image=image_image_21
)

image_image_22 = PhotoImage(
    file=relative_to_assets("image_22.png"))
image_22 = canvas.create_image(
    336.6533203125,
    398.9997253417969,
    image=image_image_22
)

image_image_23 = PhotoImage(
    file=relative_to_assets("image_23.png"))
image_23 = canvas.create_image(
    339.8837890625,
    302.1947021484375,
    image=image_image_23
)

image_image_24 = PhotoImage(
    file=relative_to_assets("image_24.png"))
image_24 = canvas.create_image(
    434.716796875,
    384.1643371582031,
    image=image_image_24
)

image_image_25 = PhotoImage(
    file=relative_to_assets("image_25.png"))
image_25 = canvas.create_image(
    412.068359375,
    417.91845703125,
    image=image_image_25
)

image_image_26 = PhotoImage(
    file=relative_to_assets("image_26.png"))
image_26 = canvas.create_image(
    557.3564453125,
    363.828857421875,
    image=image_image_26
)

image_image_27 = PhotoImage(
    file=relative_to_assets("image_27.png"))
image_27 = canvas.create_image(
    701.4384765625,
    666.6658935546875,
    image=image_image_27
)

image_image_28 = PhotoImage(
    file=relative_to_assets("image_28.png"))
image_28 = canvas.create_image(
    580.4736328125,
    577.2693481445312,
    image=image_image_28
)

image_image_29 = PhotoImage(
    file=relative_to_assets("image_29.png"))
image_29 = canvas.create_image(
    1066.6640625,
    557.3362121582031,
    image=image_image_29
)

image_image_30 = PhotoImage(
    file=relative_to_assets("image_30.png"))
image_30 = canvas.create_image(
    999.564453125,
    302.47021484375,
    image=image_image_30
)

image_image_31 = PhotoImage(
    file=relative_to_assets("image_31.png"))
image_31 = canvas.create_image(
    1011.564453125,
    476.1513671875,
    image=image_image_31
)

image_image_32 = PhotoImage(
    file=relative_to_assets("image_32.png"))
image_32 = canvas.create_image(
    941.7138671875,
    636.498291015625,
    image=image_image_32
)

image_image_33 = PhotoImage(
    file=relative_to_assets("image_33.png"))
image_33 = canvas.create_image(
    1066.5,
    750.0,
    image=image_image_33
)

image_image_34 = PhotoImage(
    file=relative_to_assets("image_34.png"))
image_34 = canvas.create_image(
    932.58203125,
    749.96533203125,
    image=image_image_34
)

image_image_35 = PhotoImage(
    file=relative_to_assets("image_35.png"))
image_35 = canvas.create_image(
    1066.5,
    722.0,
    image=image_image_35
)

image_image_36 = PhotoImage(
    file=relative_to_assets("image_36.png"))
image_36 = canvas.create_image(
    932.58203125,
    721.9653930664062,
    image=image_image_36
)

image_image_37 = PhotoImage(
    file=relative_to_assets("image_37.png"))
image_37 = canvas.create_image(
    1080.9033203125,
    182.54107666015625,
    image=image_image_37
)

image_image_38 = PhotoImage(
    file=relative_to_assets("image_38.png"))
image_38 = canvas.create_image(
    574.0,
    183.5,
    image=image_image_38
)

image_image_39 = PhotoImage(
    file=relative_to_assets("image_39.png"))
image_39 = canvas.create_image(
    990.0,
    146.0,
    image=image_image_39
)

image_image_40 = PhotoImage(
    file=relative_to_assets("image_40.png"))
image_40 = canvas.create_image(
    324.7001953125,
    146.6259765625,
    image=image_image_40
)

image_image_41 = PhotoImage(
    file=relative_to_assets("image_41.png"))
image_41 = canvas.create_image(
    1077.1337890625,
    193.7281494140625,
    image=image_image_41
)

image_image_42 = PhotoImage(
    file=relative_to_assets("image_42.png"))
image_42 = canvas.create_image(
    569.662109375,
    193.8759765625,
    image=image_image_42
)

image_image_43 = PhotoImage(
    file=relative_to_assets("image_43.png"))
image_43 = canvas.create_image(
    130.140625,
    220.26641845703125,
    image=image_image_43
)

canvas.create_rectangle(
    186.828125,
    218.853271484375,
    225.3447265625,
    218.853271484375,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    34.265625,
    218.8780517578125,
    72.7822265625,
    219.1959228515625,
    fill="#FFFFFF",
    outline="")

image_image_44 = PhotoImage(
    file=relative_to_assets("image_44.png"))
image_44 = canvas.create_image(
    131.7138671875,
    498.30712890625,
    image=image_image_44
)

canvas.create_rectangle(
    194.1533203125,
    497.1221008300781,
    228.5224609375,
    497.1221008300781,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    34.7255859375,
    497.1931457519531,
    69.0947265625,
    497.4691467285156,
    fill="#FFFFFF",
    outline="")

image_image_45 = PhotoImage(
    file=relative_to_assets("image_45.png"))
image_45 = canvas.create_image(
    131.8759765625,
    132.44317626953125,
    image=image_image_45
)

image_image_46 = PhotoImage(
    file=relative_to_assets("image_46.png"))
image_46 = canvas.create_image(
    1144.0,
    404.0,
    image=image_image_46
)

image_image_47 = PhotoImage(
    file=relative_to_assets("image_47.png"))
image_47 = canvas.create_image(
    990.28125,
    350.0,
    image=image_image_47
)

image_image_48 = PhotoImage(
    file=relative_to_assets("image_48.png"))
image_48 = canvas.create_image(
    990.0,
    377.0,
    image=image_image_48
)

image_image_49 = PhotoImage(
    file=relative_to_assets("image_49.png"))
image_49 = canvas.create_image(
    990.0,
    404.0,
    image=image_image_49
)

image_image_50 = PhotoImage(
    file=relative_to_assets("image_50.png"))
image_50 = canvas.create_image(
    990.0,
    431.0,
    image=image_image_50
)

image_image_51 = PhotoImage(
    file=relative_to_assets("image_51.png"))
image_51 = canvas.create_image(
    1144.0,
    350.0,
    image=image_image_51
)

image_image_52 = PhotoImage(
    file=relative_to_assets("image_52.png"))
image_52 = canvas.create_image(
    1144.0,
    377.0,
    image=image_image_52
)

image_image_53 = PhotoImage(
    file=relative_to_assets("image_53.png"))
image_53 = canvas.create_image(
    1144.0,
    431.0,
    image=image_image_53
)

canvas.create_text(
    923.0,
    344.0,
    anchor="nw",
    text="Cookies",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    1048.0,
    344.0,
    anchor="nw",
    text="32",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    923.0,
    371.0,
    anchor="nw",
    text="Cookies",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    1048.0,
    371.0,
    anchor="nw",
    text="32",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    923.0,
    398.0,
    anchor="nw",
    text="Cookies",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    1048.0,
    398.0,
    anchor="nw",
    text="32",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    923.0,
    425.0,
    anchor="nw",
    text="Cookies",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    1048.0,
    426.0,
    anchor="nw",
    text="32",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    1076.0,
    344.0,
    anchor="nw",
    text="Cookies",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    1201.0,
    344.0,
    anchor="nw",
    text="32",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    1076.0,
    371.0,
    anchor="nw",
    text="Cookies",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    1201.0,
    371.0,
    anchor="nw",
    text="32",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    1076.0,
    398.0,
    anchor="nw",
    text="Cookies",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    1201.0,
    398.0,
    anchor="nw",
    text="32",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    1076.0,
    425.0,
    anchor="nw",
    text="Cookies",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    1201.0,
    426.0,
    anchor="nw",
    text="32",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

image_image_54 = PhotoImage(
    file=relative_to_assets("image_54.png"))
image_54 = canvas.create_image(
    1144.0,
    572.0,
    image=image_image_54
)

image_image_55 = PhotoImage(
    file=relative_to_assets("image_55.png"))
image_55 = canvas.create_image(
    990.28125,
    518.0,
    image=image_image_55
)

image_image_56 = PhotoImage(
    file=relative_to_assets("image_56.png"))
image_56 = canvas.create_image(
    990.0,
    545.0,
    image=image_image_56
)

image_image_57 = PhotoImage(
    file=relative_to_assets("image_57.png"))
image_57 = canvas.create_image(
    990.0,
    572.0,
    image=image_image_57
)

image_image_58 = PhotoImage(
    file=relative_to_assets("image_58.png"))
image_58 = canvas.create_image(
    990.0,
    599.0,
    image=image_image_58
)

image_image_59 = PhotoImage(
    file=relative_to_assets("image_59.png"))
image_59 = canvas.create_image(
    1144.0,
    518.0,
    image=image_image_59
)

image_image_60 = PhotoImage(
    file=relative_to_assets("image_60.png"))
image_60 = canvas.create_image(
    1144.0,
    545.0,
    image=image_image_60
)

image_image_61 = PhotoImage(
    file=relative_to_assets("image_61.png"))
image_61 = canvas.create_image(
    1144.0,
    599.0,
    image=image_image_61
)

canvas.create_text(
    923.0,
    512.0,
    anchor="nw",
    text="Cookies",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    1048.0,
    512.0,
    anchor="nw",
    text="32",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    923.0,
    539.0,
    anchor="nw",
    text="Cookies",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    1048.0,
    539.0,
    anchor="nw",
    text="32",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    923.0,
    566.0,
    anchor="nw",
    text="Cookies",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    1048.0,
    566.0,
    anchor="nw",
    text="32",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    923.0,
    593.0,
    anchor="nw",
    text="Cookies",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    1048.0,
    594.0,
    anchor="nw",
    text="32",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    1076.0,
    512.0,
    anchor="nw",
    text="Cookies",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    1201.0,
    512.0,
    anchor="nw",
    text="32",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    1076.0,
    539.0,
    anchor="nw",
    text="Cookies",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    1201.0,
    539.0,
    anchor="nw",
    text="32",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    1076.0,
    566.0,
    anchor="nw",
    text="Cookies",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    1201.0,
    566.0,
    anchor="nw",
    text="32",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    1076.0,
    593.0,
    anchor="nw",
    text="Cookies",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    1201.0,
    594.0,
    anchor="nw",
    text="32",
    fill="#D1D3D4",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    948.5,
    745.0,
    anchor="nw",
    text="You are all set!",
    fill="#D1D3D4",
    font=("Inter", 9 * -1)
)

canvas.create_text(
    949.0,
    716.9999389648438,
    anchor="nw",
    text="Error. Input for sell price must be a number.",
    fill="#D1D3D4",
    font=("Inter", 9 * -1)
)

canvas.create_text(
    316.0,
    387.0,
    anchor="nw",
    text="50%",
    fill="#D1D3D4",
    font=("Inter Regular", 21 * -1)
)

canvas.create_text(
    393.5,
    394.0,
    anchor="nw",
    text="50% of the",
    fill="#D1D3D4",
    font=("Inter Regular", 13 * -1)
)

canvas.create_text(
    70.0,
    146.0,
    anchor="nw",
    text="EOY Bakesale",
    fill="#FFFFFF",
    font=("Inter", 18 * -1)
)

canvas.create_text(
    279.5,
    172.5,
    anchor="nw",
    text="Revenue",
    fill="#D1D3D4",
    font=("Inter Regular", 16 * -1)
)

canvas.create_text(
    279.5,
    196.76800537109375,
    anchor="nw",
    text="RM 2 233",
    fill="#D1D3D4",
    font=("Inter Regular", 16 * -1)
)

canvas.create_text(
    431.0224609375,
    172.5,
    anchor="nw",
    text="Profit",
    fill="#D1D3D4",
    font=("Inter Regular", 16 * -1)
)

canvas.create_text(
    431.0224609375,
    196.76800537109375,
    anchor="nw",
    text="RM 221",
    fill="#D1D3D4",
    font=("Inter Regular", 16 * -1)
)

canvas.create_text(
    579.4482421875,
    172.5,
    anchor="nw",
    text="Cost",
    fill="#D1D3D4",
    font=("Inter Regular", 16 * -1)
)

canvas.create_text(
    579.44921875,
    196.76800537109375,
    anchor="nw",
    text="RM 2 012",
    fill="#D1D3D4",
    font=("Inter Regular", 16 * -1)
)

canvas.create_text(
    730.091796875,
    172.5,
    anchor="nw",
    text="Time spent",
    fill="#D1D3D4",
    font=("Inter Regular", 16 * -1)
)

canvas.create_text(
    729.88671875,
    196.76800537109375,
    anchor="nw",
    text="6 Hours 7 Minutes",
    fill="#D1D3D4",
    font=("Inter Regular", 16 * -1)
)

canvas.create_text(
    935.228515625,
    174.0,
    anchor="nw",
    text="Event Name               ",
    fill="#D1D3D4",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    935.0,
    195.7764892578125,
    anchor="nw",
    text="Due Date                     ",
    fill="#D1D3D4",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    1085.5,
    174.0,
    anchor="nw",
    text="Summer Bakesale",
    fill="#D1D3D4",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    1085.5,
    195.7769775390625,
    anchor="nw",
    text="14/05/2022",
    fill="#D1D3D4",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    1188.0,
    226.5,
    anchor="nw",
    text="In 21 days",
    fill="#FFFFFF",
    font=("Inter", 8 * -1)
)

canvas.create_text(
    58.5,
    744.0,
    anchor="nw",
    text="shng2025@gmail.com",
    fill="#FFFFFF",
    font=("Inter", 14 * -1)
)

image_image_62 = PhotoImage(
    file=relative_to_assets("image_62.png"))
image_62 = canvas.create_image(
    336.6494140625,
    399.0,
    image=image_image_62
)

image_image_63 = PhotoImage(
    file=relative_to_assets("image_63.png"))
image_63 = canvas.create_image(
    336.6494140625,
    399.0,
    image=image_image_63
)

image_image_64 = PhotoImage(
    file=relative_to_assets("image_64.png"))
image_64 = canvas.create_image(
    314.6494140625,
    399.0,
    image=image_image_64
)

image_image_65 = PhotoImage(
    file=relative_to_assets("image_65.png"))
image_65 = canvas.create_image(
    315.8494140625,
    421.0,
    image=image_image_65
)

##########################################################################################################################################################################################################


def button_1():
    canvas.destroy()
    import notifications

#notification bell button
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    highlightthickness=0,
    command=button_1,
    relief="flat"
)
button_1.place(
    x=1075.0,
    y=47.0,
    width=42.0,
    height=39.0
)

#save button
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=1133.0,
    y=41.0,
    width=111.0,
    height=47.0
)

#undo button
button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=380.0,
    y=62.0,
    width=35.5,
    height=25.5
)

#redo button
button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=421.5,
    y=61.5,
    width=35.5,
    height=25.5
)

#overall - time spent chart
button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=819.0,
    y=748.0,
    width=43.0,
    height=9.0
)

#y/d - time spent chart
button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=777.0,
    y=749.0,
    width=29.0,
    height=8
)

#overall - profit chart
button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=822.0,
    y=537.0,
    width=43.0,
    height=9.0
)

#y/d - profit chart
button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=780.0,
    y=537.0,
    width=29.0,
    height=9.0
)

#overall - main data
button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=822.744140625,
    y=231.0,
    width=43.255859375,
    height=8
)

#y/d - main data
button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat"
)
button_10.place(
    x=780.0,
    y=231.0,
    width=29.0,
    height=9.0
)

#log out button
button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    highlightthickness=0,
    command=lambda: print("button_11 clicked"),
    relief="flat"
)
button_11.place(
    x=116.0,
    y=765.0,
    width=32.1259765625,
    height=9.43988037109375
)

#made an error
button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    image=button_image_12,
    highlightthickness=0,
    command=lambda: print("button_12 clicked"),
    relief="flat"
)
button_12.place(
    x=32.3984375,
    y=418.9002990722656,
    width=203.8076171875,
    height=21.443695068359375
)

#google forms
button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
button_13 = Button(
    image=button_image_13,
    highlightthickness=0,
    command=lambda: print("button_13 clicked"),
    relief="flat"
)
button_13.place(
    x=32.3984375,
    y=370.6551513671875,
    width=203.8076171875,
    height=21.4437255859375
)

#add type of product
button_image_14 = PhotoImage(
    file=relative_to_assets("button_14.png"))
button_14 = Button(
    image=button_image_14,
    highlightthickness=0,
    command=lambda: print("button_14 clicked"),
    relief="flat"
)
button_14.place(
    x=32.3984375,
    y=321.7023010253906,
    width=203.8076171875,
    height=21.443756103515625
)

#event settings
button_image_15 = PhotoImage(
    file=relative_to_assets("button_15.png"))
button_15 = Button(
    image=button_image_15,
    highlightthickness=0,
    command=lambda: print("button_15 clicked"),
    relief="flat"
)
button_15.place(
    x=32.3984375,
    y=394.7588806152344,
    width=203.8076171875,
    height=21.443756103515625
)

#retrieve orders
button_image_16 = PhotoImage(
    file=relative_to_assets("button_16.png"))
button_16 = Button(
    image=button_image_16,
    highlightthickness=0,
    command=lambda: print("button_16 clicked"),
    relief="flat"
)
button_16.place(
    x=32.3984375,
    y=297.4139404296875,
    width=203.8076171875,
    height=21.443756103515625
)

#add products made
button_image_17 = PhotoImage(
    file=relative_to_assets("button_17.png"))
button_17 = Button(
    image=button_image_17,
    highlightthickness=0,
    command=lambda: print("button_17 clicked"),
    relief="flat"
)
button_17.place(
    x=32.3984375,
    y=248.83721923828125,
    width=203.8076171875,
    height=21.44378662109375
)

#display tables
button_image_18 = PhotoImage(
    file=relative_to_assets("button_18.png"))
button_18 = Button(
    image=button_image_18,
    highlightthickness=0,
    command=lambda: print("button_18 clicked"),
    relief="flat"
)
button_18.place(
    x=32.3984375,
    y=552.5751342773438,
    width=203.8076171875,
    height=21.4437255859375
)

#display charts
button_image_19 = PhotoImage(
    file=relative_to_assets("button_19.png"))
button_19 = Button(
    image=button_image_19,
    highlightthickness=0,
    command=lambda: print("button_19 clicked"),
    relief="flat"
)
button_19.place(
    x=32.3984375,
    y=528.2867431640625,
    width=203.8076171875,
    height=21.44378662109375
)

#delete product type
button_image_20 = PhotoImage(
    file=relative_to_assets("button_20.png"))
button_20 = Button(
    image=button_image_20,
    highlightthickness=0,
    command=lambda: print("button_20 clicked"),
    relief="flat"
)
button_20.place(
    x=32.3984375,
    y=601.15185546875,
    width=203.8076171875,
    height=21.44378662109375
)

#add new product
button_image_21 = PhotoImage(
    file=relative_to_assets("button_21.png"))
button_21 = Button(
    image=button_image_21,
    highlightthickness=0,
    command=lambda: print("button_21 clicked"),
    relief="flat"
)
button_21.place(
    x=32.3984375,
    y=576.863525390625,
    width=203.8076171875,
    height=21.4437255859375
)

#delete an event
button_image_22 = PhotoImage(
    file=relative_to_assets("button_22.png"))
button_22 = Button(
    image=button_image_22,
    highlightthickness=0,
    command=lambda: print("button_22 clicked"),
    relief="flat"
)
button_22.place(
    x=32.3984375,
    y=650.2776489257812,
    width=203.8076171875,
    height=21.44378662109375
)

#create new event
button_image_23 = PhotoImage(
    file=relative_to_assets("button_23.png"))
button_23 = Button(
    image=button_image_23,
    highlightthickness=0,
    command=lambda: print("button_23 clicked"),
    relief="flat"
)
button_23.place(
    x=32.3984375,
    y=625.9893188476562,
    width=203.8076171875,
    height=21.4437255859375
)

#add products sold
button_image_24 = PhotoImage(
    file=relative_to_assets("button_24.png"))
button_24 = Button(
    image=button_image_24,
    highlightthickness=0,
    command=lambda: print("button_24 clicked"),
    relief="flat"
)
button_24.place(
    x=32.3984375,
    y=273.1255798339844,
    width=203.8076171875,
    height=21.443756103515625
)

#add time spent
button_image_25 = PhotoImage(
    file=relative_to_assets("button_25.png"))
button_25 = Button(
    image=button_image_25,
    highlightthickness=0,
    command=lambda: print("button_25 clicked"),
    relief="flat"
)
button_25.place(
    x=32.3984375,
    y=346.1821594238281,
    width=203.8076171875,
    height=21.44378662109375
)
##########################################################################################################################################################################################################

window.resizable(False, False)
window.mainloop()
