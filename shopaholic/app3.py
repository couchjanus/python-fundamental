# -*- coding: utf-8 -*-
# app3.py

from tkinter import Tk, Button, Label, Frame, LabelFrame, Entry, W, E
from tkinter import ttk
import sqlite3

class Application(Frame):
    db_filename = 'test.db'

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.create_label_frame()
        self.create_bottom_buttons()
        self.create_tree_view()
        self.view_records()

    def execute_db_query(self, query, parameters=()):
        with sqlite3.connect(self.db_filename) as conn:
            cursor = conn.cursor()
            query_result = cursor.execute(query, parameters)
            conn.commit()
        return query_result

    def create_label_frame(self):
        labelframe = LabelFrame(self.master, text='Create New Record')
        labelframe.grid(row=0, column=1, padx=8, pady=8, sticky='ew')
        Label(labelframe, text='Name:').grid(row=1, column=1, sticky=W, pady=2)
        self.namefield = Entry(labelframe)
        self.namefield.grid(row=1, column=2, sticky=W, padx=5, pady=2)
        Label(labelframe, text='Price:').grid(row=2, column=1, sticky=W,  pady=2)
        self.pricefield = Entry(labelframe)
        self.pricefield.grid(row=2, column=2, sticky=W, padx=5, pady=2)
        ttk.Button(labelframe, text='Add Record', command=self.newRecord).grid(row=3, column=2, sticky=E, padx=5, pady=2)

    def create_bottom_buttons(self):
        ttk.Button(text='Delete Selected', command=self.deleteRecord).grid(
            row=5, column=0, sticky=W)
        ttk.Button(text='Modify Selected', command=self.modifyRecord).grid(
            row=5, column=1, sticky=W)

    def create_tree_view(self):
        self.tree = ttk.Treeview(height=15, columns=('Id', 'Name', 'Price'))
        self.tree.grid(row=4, column=0, columnspan=2)
        self.tree.heading('#0', text='#', anchor=W)
        self.tree.heading(0, text='Id', anchor=W)
        self.tree.heading(1, text='Price', anchor=W)
        self.tree.heading(2, text='Price', anchor=W)
        self.i = 0

    def view_records(self):
        items = self.tree.get_children()
        for item in items:
            self.tree.delete(item)
        query = 'SELECT * FROM cars ORDER BY Id desc'
        cars_entries = self.execute_db_query(query)
        for row in cars_entries:
            self.tree.insert('', 0, text="#_"+str(self.i), values=(str(row[0]) +" ", str(row[1]).ljust(35) + str(row[2])))
            # Increment counter
            self.i = self.i + 1       
            
    def newRecord(self):
        print("hi there, newRecord!")

    def deleteRecord(self):
        print("hi there, deleteRecord!")

    def modifyRecord(self):
        print("hi there, modifyRecord!")