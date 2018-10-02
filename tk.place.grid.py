# -*- coding: utf-8 -*-
# tk.place.grid.py
from tkinter import *

# Сетка относительных координат метода place()

 
root = Tk()
root.geometry('150x150')
 
Button(bg='red').place(x=75, y=20)
Button(bg='green').place(relx=0.3, rely=0.5)

Label(bg='white').place(x=10, y=10, width=50, height=30)
Label(bg='green').place(x=10, y=50, relwidth=0.3, relheight=0.15)
 
root.mainloop()
