# -*- coding: utf-8 -*-
# tk.bind.py

from tkinter import *
root = Tk()
e = Entry(root, width=20)
b = Button(root, text="Hello World") # надпись на кнопке
l = Label(root, bg='black', fg='white', width=20)

def Hello(event):
    print("Yet another hello world")

# связать вызов функции с событием:
b.bind('<Button-1>', Hello)

# менеджер геометрии pack():
e.pack()
b.pack()
l.pack()

root.mainloop()