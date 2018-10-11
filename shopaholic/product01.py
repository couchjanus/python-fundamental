# -*- coding: utf-8 -*-
# product01.py

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Product(Toplevel):     
    def __init__(self,parent,engine,):
        super().__init__(name='product')
        
        self.resizable(0,0)
        self.parent = parent
        self.engine = engine
        self.vcmd = (self.register(self.validate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        self.stock = DoubleVar()
        self.price = DoubleVar() 
        self.available = BooleanVar()
        
        self.center_me()
        self.init_ui()

    def center_me(self):
        #center window
        x = (self.master.winfo_screenwidth() - self.master.winfo_reqwidth()) / 2
        y = (self.master.winfo_screenheight() - self.master.winfo_reqheight()) / 2
        self.master.geometry("+%d+%d" % (x, y))
        
    def init_ui(self):

        self.panel = self.engine.get_panel_frame(self)
        self.panel.grid(row = 0, column = 0, sticky=N+W+S+E)

        Label(self.panel, text="Product:",anchor='w').grid(row=0, sticky='w')
        self.txtProduct = Entry(self.panel,)
        self.txtProduct.grid(row=0, column=1, sticky='w')

        Label(self.panel, text="Brands:",anchor='w').grid(row=1, sticky='w')
        self.cbBrands = ttk.Combobox(self.panel,)
        self.cbBrands.grid(row=1, column=1, sticky='w')

        Label(self.panel, text="Categories:",anchor='w').grid(row=2, sticky='w')
        self.cbCategories = ttk.Combobox(self.panel,)
        self.cbCategories.grid(row=2, column=1, sticky='w')

        Label(self.panel, text="Description:",anchor='w').grid(row=3, sticky='w')
        self.txtPackage = Entry(self.panel,)
        self.txtPackage.grid(row=3, column=1, sticky='w')

        Label(self.panel, text="Price:",anchor='w').grid(row=4, sticky='w')
        self.txtPrice = Entry(self.panel,
                              validate = 'key',
                              validatecommand = self.vcmd,
                              textvariable = self.price,
                              width=5)
        self.txtPrice.grid(row=4, column=1, sticky='w')

        Label(self.panel, text="Stock:",anchor='w').grid(row=5, sticky='w')
        self.txtStock = Entry(self.panel,
                              validate = 'key',
                              validatecommand = self.vcmd,
                              textvariable = self.stock,
                              width=5)
        self.txtStock.grid(row=5, column=1, sticky='w')

        Label(self.panel, text="Available:").grid(row=6, sticky='w')
        self.ckAvailable = Checkbutton(self.panel, onvalue=1, offvalue=0, variable = self.available,)
        self.ckAvailable.grid(row=6, column=1, sticky='w')

        self.engine.get_save_cancel(self, self)

    def on_open(self, selected_product = None):

        self.selected_product = selected_product
        self.set_categories()
        self.set_brands()
        msg = "Insert new product"
        self.title(msg)
        self.txtProduct.focus()

    def set_values(self,):
        pass

    def get_values(self,):
        pass
        
    def on_save(self, evt):
        pass
           

    def on_cancel(self,evt=None):
        self.destroy()

    def set_categories(self):
        pass
        
    def set_brands(self,):
        pass


    def validate(self, action, index, value_if_allowed,
                 prior_value, text, validation_type,
                 trigger_type, widget_name):
        pass

    def on_fields_control(self):
        pass
