import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time

from math import pi

window = tk.Tk()
window.geometry("1280x785")
window.configure(bg = "#000000")

cg_dict = [

    '#ff0101','#ff0502','#ff0900','#fe1401','#ff1d04',
    '#fe2a04','#ff3702','#ff4806','#ff5807','#fe6905',
    '#ff7d09','#ff8a07','#fea30b','#ffb00a','#ffbf10',
    '#ffcd10','#fdda0e','#fee60f','#fef00e','#fef810',
    '#fffb13','#fffe12','#ffff13','#ffff13','#ffff13',
    '#ffff13','#ffff13','#fefe12','#fcfd11','#f7f910',
    '#f0f511','#e5ef10','#dae810','#cddf10','#c0d50a',
    '#b0ca0b','#9fbf0c','#8ab107','#7aa609','#6a9c05',
    '#589105','#458304','#397b03','#297002','#1f6800',
    '#156201','#0b5d02','#045800','#015500','#005502',
    
    ]


def progress_bar(percent: int, x_cord: int, y_cord: int):

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={'projection':'polar'})
    data = percent

    startangle = 90
    x = (-data * pi *2)/ 100
    left = (startangle * pi *2)/ 360 #this is to control where the bar starts
    ys = 2.2


    #finding colour for circular bad
    col_index = round((percent / 2) + 0.1)
    colors = cg_dict[col_index - 1]

    fig.set_size_inches(0.6, 0.6)
    plt.xticks([])
    plt.yticks([])
    fig.patch.set_facecolor('#0E1012')

    ax.spines.clear()
    if percent > 60:
        ax.scatter(x+left, ys+0.02, s=0.9, color=colors, zorder=2)
    elif 40 < percent < 60:
        ax.scatter(x+left, ys-0.085, s=0.9, color=colors, zorder=2)
    elif percent < 40:
        ax.scatter(x+left, ys-0.085, s=0.9, color=colors, zorder=2)
        
    ax.scatter(left, ys+0.02744, s=0.9, color=colors, zorder=2)
    
    ax.patch.set_facecolor('#0E1012')
    
    ax.barh(ys, (-100 * pi *2)/ 100, left=left, height=0.9, color='#58595b')
    ax.barh(ys, x, left=left, height=0.9, color=colors)

    
    plt.ylim(-4, 3)

    plt.text(0, -3, f"{data}%  ", ha='center', va='center', fontsize=6, color='white')

    
    canvas = FigureCanvasTkAgg(fig, master = window)
    canvas.draw()

    global chart7
    try:
        chart7
    except NameError:
        pass
    else:
        chart7.destroy()
    
    chart7 = canvas.get_tk_widget()
    chart7.place(x=x_cord, y=y_cord)


for i in range(100):
    progress_bar(percent = 1+i, x_cord = 300, y_cord = 300)
    window.update_idletasks()
    time.sleep(0.01)


def export_progress_bar(percent: int, x_cord: int, y_cord: int):

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={'projection':'polar'})
    data = percent

    startangle = 90
    x = (-data * pi *2)/ 100
    left = (startangle * pi *2)/ 360 #this is to control where the bar starts
    ys = 2.2


    #finding colour for circular bad
    col_index = round((percent / 2) + 0.1)
    colors = cg_dict[col_index - 1]

    fig.set_size_inches(0.6, 0.6)
    plt.xticks([])
    plt.yticks([])
    fig.patch.set_facecolor('#0E1012')

    ax.spines.clear()

        
    
    ax.patch.set_facecolor('#0E1012')
    
    ax.barh(ys, (-100 * pi *2)/ 100, left=left, height=0.9, color='#58595b')

    
    plt.ylim(-4, 3)

    
    canvas = FigureCanvasTkAgg(fig, master = window)
    canvas.draw()

    global chart7
    try:
        chart7
    except NameError:
        pass
    else:
        chart7.destroy()
    
    chart7 = canvas.get_tk_widget()
    chart7.place(x=x_cord, y=y_cord)

    plt.savefig('image_22')



#export_progress_bar(percent = 65, x_cord = 300, y_cord = 300)

window.mainloop()
