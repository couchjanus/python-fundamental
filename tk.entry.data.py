# -*- coding: utf-8 -*-
# tk.entry.data.py

from tkinter import *
from tkinter import messagebox
 
def clear():
    name_entry.delete(0, END)
    price_entry.delete(0, END)
 
def display():
    messagebox.showinfo("GUI Python", name_entry.get() + " " + price_entry.get())
 
root = Tk()
root.title("GUI на Python")
 
name_label = Label(text="Введите модель:")
price_label = Label(text="Введите цену:")
 
name_label.grid(row=0, column=0, sticky="w")
price_label.grid(row=1, column=0, sticky="w")
 
name_entry = Entry()
price_entry = Entry()
 
name_entry.grid(row=0,column=1, padx=5, pady=5)
price_entry.grid(row=1,column=1, padx=5, pady=5)
 
# вставка начальных данных
name_entry.insert(0, "Toshiba")
price_entry.insert(0, 11111)
 
display_button = Button(text="Display", command=display)
clear_button = Button(text="Clear", command=clear)
 
display_button.grid(row=2, column=0, padx=5, pady=5, sticky="e")
clear_button.grid(row=2, column=1, padx=5, pady=5, sticky="e")
 
root.mainloop()
