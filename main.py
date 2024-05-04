from math import *
from random import *
from tkinter import *
from PIL import Image, ImageTk
import ctypes, os, sys

myappid = u'RGB.generator.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

window = Tk()
# Set the taskbar icon
window.geometry("500x300")
window.resizable(True, True)
window.title('RGB Generator')


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

icon = Image.open(resource_path("rgb.ico"))
icon = ImageTk.PhotoImage(icon)
window.iconphoto(True, icon)

def update(event):
    pattern = "#{:02x}{:02x}{:02x}"
    color = pattern.format(scale1.get(),
                           scale2.get(),
                           scale3.get())
    label.config(bg=color)




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