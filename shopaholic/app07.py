# -*- coding: utf-8 -*-
# app07.py

from __future__ import print_function

import os
import _thread
import datetime

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image 

from .engine06 import Engine

class Application(Frame):

    def __init__(self, engine):
        super().__init__()

        self.status_bar_text = StringVar()
        self.engine = engine
       
        self.master.title(self.engine.title)
        self.master.protocol("WM_DELETE_WINDOW",self.on_exit)

        self.cols = (["#0",'id','w',False,0,0],
                      ["#1",'Product','w',True,200,200],
                      ["#2",'Description','w',True,200,200],
                      ["#3",'Stock','w',True,50,50],
                      ["#4",'Price','w',True,50,50],)

        self.filter_id = IntVar()
        self.ops = ('Cateogries','Brands')

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

        #products
        left_widgets = Frame(self,)

        self.tree_products = LabelFrame(left_widgets,text='Products',)
        self.lstProducts = self.engine.get_tree(self.tree_products, self.cols,)
        self.lstProducts.bind("<<TreeviewSelect>>", self.get_selected_product)
        self.tree_products.pack(fill=BOTH, expand=1)

        # categories
        self.combo_label_frame = LabelFrame(left_widgets,)
        self.cbFilters =  ttk.Combobox(self.combo_label_frame)
        self.cbFilters.bind("<<ComboboxSelected>>", self.get_selected_combo_item)
        self.cbFilters.pack(side=TOP, anchor=W, fill=X, expand=YES)
        
        self.combo_label_frame.pack(side=TOP, anchor=W, fill=X, expand=0)
        
        left_widgets.pack(side=LEFT, fill=BOTH, anchor=W, expand=1)

        # buttons

        buttons_label_frame = self.engine.get_buttons_label_frame(self)

        self.btnSearch = self.engine.get_button(buttons_label_frame, "Refresh")
        self.btnSearch.bind("<Button-1>", self.on_open)

        self.btnAdd = self.engine.get_button(buttons_label_frame, "New")
        self.btnAdd.bind("<Button-1>", self.on_add)
        
        self.btnSamples = self.engine.get_button(buttons_label_frame, "Edit")
        self.btnSamples.bind("<Button-1>", self.on_edit)
        
        self.btClose = self.engine.get_button(buttons_label_frame, "Close")
        self.btClose.bind("<Button-1>", self.on_exit)
        
        self.coiche = self.engine.get_radio_buttons(buttons_label_frame,'Combo data',self.ops,self.filter_id,self.set_combo_values)

        buttons_label_frame.pack(side=RIGHT, fill=Y, expand=0)


    def on_open(self, evt=None):
    
        _thread.start_new_thread(self.update_status_bar,())

        self.selected_product = None
        self.cbFilters.set('')
        self.combo_label_frame['text'] = 'Categories'
        self.set_combo_values()

    def on_add(self):
        pass
                   
    def on_about(self,):
        messagebox.showinfo(self.engine.title, self.engine.about)   
        
    def on_exit(self, evt=None):
        if messagebox.askokcancel(self.engine.title, "Do you want to quit?"):
            self.master.destroy()

    def on_edit(self):
        pass

    def on_double_click(self):
        pass

    def get_selected_product(self, evt):
        pass

    def set_combo_values(self):

        self.dict_combo_values={}

        if self.filter_id.get() !=1:
            self.combo_label_frame['text'] = 'Categories'
        else:
            self.combo_label_frame['text'] = 'Brands'

    def get_selected_combo_item(self, evt):
        pass

    def update_status_bar(self):
        
        while True:
            s = "Astral date: "
            t = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            msg = s+t
            self.status_bar_text.set(msg)        
        

def main():
    engine = Engine()
    root = Tk()
    root.style = ttk.Style()
    
    root.style.theme_use("clam")
    app = Application(engine)
    app.on_open()
    root.mainloop()
  
if __name__ == '__main__':
    main()