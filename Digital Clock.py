from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()

root.title('Clock')

def Clock():
    tick = strftime('%H:%M:%S %p')

    label.config(text = tick)

    label.after(1000, Clock)

label = Label(root, font = ('sans', 80), background = 'black', foreground = 'white')

label.pack(anchor = 'center')

Clock()
mainloop()

import datetime

x = datetime.datetime.now()
print(x.year)
