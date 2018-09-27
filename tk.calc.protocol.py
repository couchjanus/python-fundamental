# -*- coding: utf-8 -*-
# tk.calc.protocol.py

# from tkinter import *

import tkinter as tk
class Calc:
    def __init__(self, master):
        
        self.initUI(master)
        

    def initUI(self, master):
        master.title('Calulator')
        master.geometry()
        # создаём виджет
        self.closeButton = tk.Button(master, command = lambda:master.quit())
        # конфигурируем виджет после создания
        self.closeButton.configure(text="Close", fg="Red")
        self.closeButton.pack(side=tk.RIGHT, padx=5, pady=5)
        
        self.okButton = tk.Button(master)
        # также можно использовать квадратные скобки:
        self.okButton['text'] = "OK"
        self.okButton['fg'] = "Green"
        self.okButton.pack(side=tk.RIGHT)
        master.protocol('WM_DELETE_WINDOW', self.destroyApp(master)) # обработчик закрытия окна
        master.resizable(True, False) # размер окна может быть изменён только по горизонтали
    
    def destroyApp(self, master):
        master.quit() # явное указание на выход из программы

root = tk.Tk()

root.geometry("350x350+300+300")

obj=Calc(root) # object instantiated

root.mainloop()




