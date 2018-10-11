# -*- coding: utf-8 -*-
# widgets03.py

from tkinter import *
from tkinter import ttk  
from tkinter import font

class Widgets(object):

    def __init__(self,*args, **kwargs):

        super(Widgets, self).__init__( *args, **kwargs)

    def get_button(self, container, text, row=None, col=None):

        obj = Button(container, text=text, borderwidth=1,relief='raised',padx=5,pady=5,)

        if row is not None:
            obj.grid(row=row, column=col, sticky=W+E, padx=5, pady=5)
        else:
            obj.pack(fill =X, padx=5, pady=5)
        
        return obj


    def get_radio_buttons(self, container,text, ops, v, callback=None):

        obj = LabelFrame(container, borderwidth=1, text = text)

        for index, text in enumerate(ops):
            Radiobutton(obj,
                            text=text,
                            #fg='blue',
                            bd=0,
                            padx = 5,
                            pady = 5,
                            relief=GROOVE,
                            variable=v,
                            command=callback,
                            value=index).pack(anchor=W)

        obj.pack(fill=X, expand=0)            

        return obj            


    def get_buttons_label_frame(self, container):
        return LabelFrame(container, bd=1 ,padx=5, pady=5, relief=GROOVE)

    def get_tree(self, container, cols,):

        headers = []

        for col in cols:
            headers.append(col[1])
        del headers[0]

        obj = ttk.Treeview(container,)
        
        obj['columns']=headers

        for col in cols:
            obj.heading(col[0], text=col[1], anchor=col[2],)
            obj.column(col[0], anchor=col[2], stretch=col[3],minwidth=col[4], width=col[5])
           
        sb = Scrollbar(container)
        sb.configure(command=obj.yview)
        obj.configure(yscrollcommand=sb.set)

        obj.pack(side=LEFT, fill=BOTH, expand =1)
        sb.pack(fill=Y, expand=1)

        return obj

    def get_panel_frame(self, container):
        return Frame(container, bd=1, padx = 5, pady = 5)

    
    def get_listbox(self, container,):

        sb = Scrollbar(container,orient=VERTICAL)
        obj = Listbox(container,relief=GROOVE,selectmode=BROWSE,yscrollcommand=sb.set,)
        sb.config(command=obj.yview)
     
        obj.pack(side=LEFT,fill=BOTH, expand =1) 
        sb.pack(fill=Y, expand=1)

        return obj

    def get_add_edit_cancel(self, caller, container):
    
        bts = self.get_buttons_label_frame(container)

        caller.btnAdd = self.get_button(bts, "Add")
        caller.btnAdd.bind("<Return>", caller.on_add)
        caller.btnAdd.bind("<Button-1>", caller.on_add)
        caller.btnEdit = self.get_button(bts, "Edit")
        caller.btnEdit.bind("<Button-1>", caller.on_edit)
        caller.btCancel = self.get_button(bts, "Close")
        caller.btCancel.bind("<Button-1>", caller.on_cancel)

        bts.pack(side=RIGHT, fill=Y, expand=0)

        return bts




