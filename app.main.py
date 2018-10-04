# -*- coding: utf-8 -*-
# app.main.py

from tkinter import Tk
# import shopaholic
# from shopaholic.app import Application
from shopaholic import *

if __name__ == '__main__':
    root = Tk()
    root.title("Cars Store")
    # application = shopaholic.app.Application(master=root)
    application = Application(master=root)
    root.mainloop()
