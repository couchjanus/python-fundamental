# -*- coding: utf-8 -*-
# widgets03.py

from tkinter import *
from tkinter import ttk  

class Widgets(object):

    def __init__(self,*args, **kwargs):
        super(Widgets, self).__init__( *args, **kwargs)

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
