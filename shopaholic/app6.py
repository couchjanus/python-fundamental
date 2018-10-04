# -*- coding: utf-8 -*-
# app6.py

from tkinter import Tk, Button, Label, Frame, LabelFrame, Entry, W, E, END, Toplevel, StringVar
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
        self.create_message_area()
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

    def create_message_area(self):
        self.message = Label(text='', fg='red')
        self.message.grid(row=3, column=1, sticky=W)

    def view_records(self):
        items = self.tree.get_children()
        for item in items:
            self.tree.delete(item)
        query = 'SELECT * FROM cars ORDER BY Id desc'
        cars_entries = self.execute_db_query(query)
        for row in cars_entries:
            self.tree.insert('', 0, text=str(row[0]), values=(str(row[0]) +" ", str(row[1]).ljust(35), str(row[2])))
            # Increment counter
            # self.i = self.i + 1

    def add_new_record(self):
        if self.new_records_validated():
            query = 'INSERT INTO cars VALUES(NULL, ?, ?)'
            parameters = (self.namefield.get(), self.pricefield.get())
            self.execute_db_query(query, parameters)
            self.message['text'] = 'Cars record of {} added'.format(
                self.namefield.get())
            self.namefield.delete(0, END)
            self.pricefield.delete(0, END)
        else:
            self.message['text'] = 'name and price cannot be blank'
        self.view_records()

    def new_records_validated(self):
        return len(self.namefield.get()) != 0 and len(self.pricefield.get()) != 0

    def newRecord(self):
        self.add_new_record()

    def deleteRecord(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'No item selected to delete'
            return
        self.delete_record()


    def modifyRecord(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][1]
        except IndexError as e:
            self.message['text'] = 'No item selected to modify'
            return
        self.open_modify_window()

    def delete_record(self):
        self.message['text'] = ''
        Id = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM cars WHERE Id = ?'
        self.execute_db_query(query, (Id,))
        self.message['text'] = 'Cars record for {} deleted'.format(Id)
        self.view_records()

    def open_modify_window(self):
        name = self.tree.item(self.tree.selection())['values'][1]
        old_price = self.tree.item(self.tree.selection())['values'][2]
        
        self.transient = Toplevel()
        Label(self.transient, text='Name:').grid(row=0, column=1)
        Entry(self.transient, textvariable=StringVar(
            self.transient, value=name), state='readonly').grid(row=0, column=2)
        Label(self.transient, text='Old Price:').grid(row=1, column=1)
        Entry(self.transient, textvariable=StringVar(
            self.transient, value=old_price), state='readonly').grid(row=1, column=2)
        Label(self.transient, text='New Price:').grid(
            row=2, column=1)
        new_price = Entry(self.transient)
        new_price.grid(row=2, column=2)
        Button(self.transient, text='Update Record', command=lambda: self.update_record(
            new_price.get(), old_price, name)).grid(row=3, column=2, sticky=E)
        self.transient.mainloop()

    def update_record(self, newprice, old_price, name):
        query = 'UPDATE cars SET Price=? WHERE Price=? AND Name=?'
        parameters = (newprice, old_price, name)
        self.execute_db_query(query, parameters)
        self.transient.destroy()
        self.message['text'] = 'Price of {} modified'.format(name)
        self.view_records()
