# -*- coding: utf-8 -*-
# tk.calc.pack.py

# from tkinter import *

import tkinter as tk
class Calc:
    def __init__(self, master):
        
        self.initUI(master)

    def initUI(self, master):
        master.title('Calulator')
        master.geometry()
        self.closeButton = tk.Button(master, text="Close")
        self.closeButton.pack(side=tk.RIGHT, padx=5, pady=5)
        self.okButton = tk.Button(master, text="OK")
        self.okButton.pack(side=tk.RIGHT)

root = tk.Tk()

root.geometry("350x350+300+300")

obj=Calc(root) # object instantiated

root.mainloop()