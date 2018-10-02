# -*- coding: utf-8 -*-
# sqlite3.select.py
 
import sqlite3 as lite
import sys

# Подключаемся к базе данных
con = lite.connect('test.db')
 
with con:    
    cur = con.cursor()    
    cur.execute("SELECT * FROM Cars")
    rows = cur.fetchall()
 
    for row in rows:
        print(row)
