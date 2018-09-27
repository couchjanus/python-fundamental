# -*- coding: utf-8 -*-
# tk.calc.geometry.py

from tkinter import *

class Calc:
    def __init__(self, master):
        self.initUI(master)

    def initUI(self, master):
        master.title('Calulator')
        master.geometry() 

root = Tk()

root.geometry("350x350+300+300")

obj=Calc(root) # object instantiated

root.mainloop()