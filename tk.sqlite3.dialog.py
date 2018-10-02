# -*- coding: utf-8 -*-
# tk.sqlite3.dialog.py

from tkinter import *
from tkinter import messagebox
import sqlite3 as lite

def create_record(conn, record):
    """
    Create a new record
    :param conn:
    :param record:
    :return:
    """
    sql = ''' INSERT INTO cars(Name, Price)
              VALUES(?,?) '''
    cursor = conn.cursor()
    cursor.execute(sql, record)
    return cursor.lastrowid

def clear():
    name_entry.delete(0, END)
    price_entry.delete(0, END)

def display(record_id):
    name_entry.delete(0, END)
    price_entry.delete(0, END)
    messagebox.showinfo("Success", "One row have been inserted into table cars successfully with id = " + str(record_id))

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = lite.connect(db_file)
        return conn
    except lite.Error as e:
        print(e)
 
    return None

def newRecord():
    # create a database connection
    conn = create_connection('test.db')
    with conn:
        # create a new record
        record = (name_entry.get(), price_entry.get());
        record_id = create_record(conn, record)
        display(record_id)

root = Tk()
root.title("Add New Record")
 
name_label = Label(text="Введите модель:")
price_label = Label(text="Введите цену:")
 
name_label.grid(row=0, column=0, sticky="w")
price_label.grid(row=1, column=0, sticky="w")
 
name_entry = Entry()
price_entry = Entry()
 
name_entry.grid(row=0,column=1, padx=5, pady=5)
price_entry.grid(row=1,column=1, padx=5, pady=5)
 
# вставка начальных данных
name_entry.insert(0, "Toshiba")
price_entry.insert(0, 11111)
 
display_button = Button(text="Add New", command=newRecord)

clear_button = Button(text="Clear", command=clear)
 
display_button.grid(row=2, column=0, padx=5, pady=5, sticky="e")
clear_button.grid(row=2, column=1, padx=5, pady=5, sticky="e")
 
root.mainloop()
