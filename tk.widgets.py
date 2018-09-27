# -*- coding: utf-8 -*-
# tk.element.pack.py

from tkinter import *
root = Tk()
e = Entry(root, width=20)
b = Button(root, text="Преобразовать") # надпись на кнопке


l = Label(root, bg='black', fg='white', width=20, font="Arial 32") # ширина, цвет фона и надписи

l1 = Label(text="Машинное обучение", font="Arial 32")
l2 = Label(text="Распознавание образов", font=("Comic Sans MS", 24, "bold"))

l1.config(bd=20, bg='#ffaaaa')
l2.config(bd=20, bg='#aaffff')

# расположим элементы друг за другом 
# с помощью наиболее простого 
# менеджера геометрии tkinter – метода pack():
e.pack()
b.pack()
l.pack()

root.mainloop()