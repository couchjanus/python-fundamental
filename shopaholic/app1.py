# -*- coding: utf-8 -*-
# app1.py

from tkinter import Tk, Button, Label, Frame, LabelFrame, Entry, W, E
from tkinter import ttk

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.create_label_frame()
        self.create_bottom_buttons()

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

    def newRecord(self):
        print("hi there, newRecord!")

    def deleteRecord(self):
        print("hi there, deleteRecord!")

    def modifyRecord(self):
        print("hi there, modifyRecord!")