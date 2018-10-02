# -*- coding: utf-8 -*-
# sqlite3.placeholder.py
 
import sqlite3 as lite

# Подключаемся к базе данных
con = lite.connect('test.db')

uId = 4

with con:
    cur = con.cursor()    
    cur.execute("SELECT Name, Price FROM cars WHERE Id=:Id", 
        {"Id": uId})        
    con.commit()
    
    row = cur.fetchone()
    print(row[0], row[1])