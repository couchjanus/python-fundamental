# -*- coding: utf-8 -*-
# sqlite3.fetchone.py
 
import sqlite3 as lite
import sys

# Подключаемся к базе данных
con = lite.connect('test.db')
 
with con:
    cur = con.cursor()    
    cur.execute("SELECT * FROM Cars")
 
    while True:
        row = cur.fetchone()
        
        if row == None:
            break
            
        print(row[0], row[1], row[2])
