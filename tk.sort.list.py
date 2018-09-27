# -*- coding: utf-8 -*-
# tk.sort.list.py

from tkinter import *
root = Tk()
e = Entry(root, width=20)
b = Button(root, text="Hello World")
l = Label(root, bg='black', fg='white', width=20)

def strToSortlist(event):
    s = e.get()
    s = s.split()
    s.sort()
    l['text'] = ' '.join(s)

# Теперь необходимо связать вызов функции с событием:

b.bind('<Button-1>', strToSortlist)

# расположим элементы друг за другом 
# с помощью наиболее простого 
# менеджера геометрии tkinter – метода pack():
e.pack()
b.pack()
l.pack()

root.mainloop()