# -*- coding: utf-8 -*-
# tk.calc.grid.py

# from tkinter import *

import tkinter as tk
class Calc:
    def __init__(self, master):
        self.initUI(master)

    def initUI(self, master):
        master.title('Calulator')
        master.geometry()
        
        self.entry = tk.Entry(master)
        self.entry.grid(row=0, column=0, columnspan=6, pady=3)

        self.frame_bottom = tk.Frame(master)
        # создаём виджет
        self.closeButton = tk.Button(self.frame_bottom, command = lambda:master.quit())
        # конфигурируем виджет после создания
        self.closeButton.configure(text="Close", fg="Red")
        self.closeButton.pack(side=tk.RIGHT, padx=5, pady=5)
        self.okButton = tk.Button(self.frame_bottom)
        # также можно использовать квадратные скобки:
        self.okButton['text'] = "HELP"
        self.okButton['fg'] = "Green"
        self.okButton.pack(side=tk.RIGHT)
        # Фреймы размещают на главном окне, а уже в фреймах – виджеты:
        self.frame_bottom.grid(row=6, column=4, columnspan=2, pady=3)

        # Generating Buttons
        tk.Button(master,text="=",width=10).grid(row=4, column=4,columnspan=2)
        tk.Button(master,text='AC',width=3).grid(row=1, column=4)
        tk.Button(master,text='C',width=3).grid(row=1, column=5)
        tk.Button(master,text="+",width=3).grid(row=4, column=3)
        tk.Button(master,text="x",width=3).grid(row=2, column=3)
        tk.Button(master,text="-",width=3).grid(row=3, column=3)
        tk.Button(master,text="÷",width=3).grid(row=1, column=3)
        tk.Button(master,text="%",width=3).grid(row=4, column=2)
        tk.Button(master,text="7",width=3).grid(row=1, column=0)
        tk.Button(master,text="8",width=3).grid(row=1, column=1)
        tk.Button(master,text="9",width=3).grid(row=1, column=2)
        tk.Button(master,text="4",width=3).grid(row=2, column=0)
        tk.Button(master,text="5",width=3).grid(row=2, column=1)
        tk.Button(master,text="6",width=3).grid(row=2, column=2)
        tk.Button(master,text="1",width=3).grid(row=3, column=0)
        tk.Button(master,text="2",width=3).grid(row=3, column=1)
        tk.Button(master,text="3",width=3).grid(row=3, column=2)
        tk.Button(master,text="0",width=3).grid(row=4, column=0)
        tk.Button(master,text=".",width=3).grid(row=4, column=1)
        tk.Button(master,text="(",width=3).grid(row=2, column=4)
        tk.Button(master,text=")",width=3).grid(row=2, column=5)
        tk.Button(master,text="√",width=3).grid(row=3, column=4)
        tk.Button(master,text="x²",width=3).grid(row=3, column=5)
		
        master.protocol('WM_DELETE_WINDOW', self.destroyApp(master)) # обработчик закрытия окна
        master.resizable(True, False) # размер окна может быть изменён только по горизонтали
    
    def destroyApp(self, master):
        master.quit() # явное указание на выход из программы

root = tk.Tk()

root.geometry("350x350+300+300")

obj=Calc(root) # object instantiated

root.mainloop()
