'''import tkinter as tk
from tkinter import ttk

my_w = tk.Tk()
my_w.geometry("300x150")  # Size of the window 
my_w.title("www.plus2net.com")  # Adding a title
def my_upd1():
    #cb1.set('Jan') # update selection to Apr
    #l1.config(text=cb1.get()+':'+ str(cb1.current())) # value & index
    print(cb1.get())

	
months=['Jan','Feb','Mar','Apr','May','Jun']
cb1 = ttk.Combobox(my_w, values=months,width=7)
cb1.grid(row=1,column=1,padx=10,pady=20)

b1=tk.Button(my_w,text="Get selection", command=lambda: my_upd1())
b1.grid(row=1,column=2)

my_w.mainloop()  # Keep the window open'''


import tkinter as tk
L1 = 0
def Click(e, var):
    print(e)
    #e.widget.focus()
    nclist=[(' Excellent', lambda: print("Excellent")),
            (' Very Good', lambda: print("Very Good")),
            (' Good', lambda: print("Good")),
            (' Poor', lambda: print("Poor")),]

    my_menu = tk.Menu(None, tearoff=0, takefocus=0)
    for (txt, cmd) in nclist:
        my_menu.add_command(label=txt, command=cmd)
    my_menu.tk_popup(e.x_root + 20, e.y_root + 10,entry="0")

root = tk.Tk()
root.geometry('200x200')





root.mainloop()


