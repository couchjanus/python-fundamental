# -*- coding: utf-8 -*-
# tk.messagebox.py
# Модуль messagebox – стандартные диалоговые окна
# Окно выбора "да" или "нет" – askyesno():

from tkinter import *
from tkinter import messagebox as mb
 
def check():
    answer = mb.askyesno(title="Вопрос", message="Перенести данные?")
    if answer == True:
        s = entry.get()
        entry.delete(0, END)
        label['text'] = s
 
root = Tk()
entry = Entry()
entry.pack(pady=10)
Button(text='Передать', command=check).pack()
label = Label(height=3)
label.pack()
 
root.mainloop()


