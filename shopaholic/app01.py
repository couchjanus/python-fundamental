# -*- coding: utf-8 -*-
# app01.py

from __future__ import print_function

import os

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image 

class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)

        self.status_bar_text = StringVar()
        self.title = "Shopaholic"
        self.about = "Shopaholic Release Candidate version 0.1 alpha"

        self.master = master
        self.init_widgets()

    def init_widgets(self):
        self.init_menu()
        self.init_toolbar()
        self.init_status_bar()
        self.init_window()

    def init_menu(self):
    
        menuMain = Menu(self)
        mFile = Menu(menuMain, tearoff=0, bd = 1)
        mTools = Menu(menuMain, tearoff=0, bd = 1)
        mAbout = Menu(menuMain, tearoff=0, bd = 1)
        
        menuMain.add_cascade(label="File", menu=mFile)
        menuMain.add_cascade(label="Tools", menu=mTools)
        menuMain.add_cascade(label="?", menu=mAbout)
        
        mFile.add_command(label="Exit", command=self.on_exit)
        mAbout.add_command(label="About", command=self.on_about)

        self.master.config(menu=menuMain)

    
    def init_toolbar(self):

        toolbar = Frame(self, bd=1, relief=RAISED)

        img_exit = PhotoImage(file=os.path.join('icons', 'exit.png'))
        img_info = PhotoImage(file=os.path.join('icons', 'info.png'))

        exitButton = Button(toolbar,width=20, image=img_exit, relief=FLAT, command=self.on_exit)
        infoButton = Button(toolbar,width=20, image=img_info, relief=FLAT, command=self.on_about)
        
        exitButton.image = img_exit
        infoButton.image = img_info

        exitButton.pack(side=LEFT, padx=2, pady=2)
        infoButton.pack(side=LEFT, padx=2, pady=2)

        toolbar.pack(side=TOP, fill=X)
        

    def init_status_bar(self):

        self.status = Label(self.master, textvariable=self.status_bar_text, bd=1, relief=SUNKEN, anchor=W)
        self.status.pack(side=BOTTOM, fill=X)
    
    
    def init_window(self):
        """create widgets"""
        self.pack(fill=BOTH, expand=1)
        left_widgets = Frame(self,)
        self.tree_products = LabelFrame(left_widgets,text='Products',)
        self.tree_products.pack(fill=BOTH, expand=1)
        self.combo_label_frame = LabelFrame(left_widgets,) # родительсикй виджет
        self.cbFilters =  ttk.Combobox(self.combo_label_frame)
        self.cbFilters.pack(side=TOP, anchor=W, fill=X, expand=YES)
        self.combo_label_frame.pack(side=TOP, anchor=W, fill=X, expand=0)
        left_widgets.pack(side=LEFT, fill=BOTH, anchor=W, expand=1)

    def on_open(self):
        pass

    def on_add(self):
        pass
                   
    def on_about(self):
        messagebox.showinfo(self.title, self.about) 
      
    def on_exit(self, evt=None):
        if messagebox.askokcancel(self.title, "Do you want to quit?"):
            self.master.destroy()

    def on_edit(self):
        pass

    def on_double_click(self):
        pass


def main():
    root = Tk()
    root.style = ttk.Style()
    root.style.theme_use("clam")
    app = Application(master=root)
    root.mainloop()
  
if __name__ == '__main__':
    main()