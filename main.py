from math import *
from random import *
from tkinter import *


def update(event):
    pattern = "#{:02x}{:02x}{:02x}"
    color = pattern.format(scale1.get(),
                           scale2.get(),
                           scale3.get())
    label.config(bg=color)

window = Tk()

scale1 = Scale(window, orient=VERTICAL,        
               label="rot", to=225,
               command=update)
scale1.grid(column=0, row=0)

scale2 = Scale(window, orient=VERTICAL,
               label="grün", to=225,
               command=update)
scale2.grid(column=1, row=0)

scale3 = Scale(window, orient=VERTICAL,
               label="blau", to=225,
               command=update)
scale3.grid(column=2,row=0)

label = Label(window, width=20, height=10, bg="black")
label.grid(column=3,row=0)

window.mainloop()