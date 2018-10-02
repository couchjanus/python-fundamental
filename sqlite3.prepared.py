# -*- coding: utf-8 -*-
# sqlite3.prepared.py
 
import sqlite3 as lite

# Подключаемся к базе данных
con = lite.connect('test.db')

uId = 1
uPrice = 62300 

with con:
    cur = con.cursor()    
    cur.execute("UPDATE cars SET Price=? WHERE Id=?", (uPrice, uId))        
    con.commit()
    print("Number of rows updated: %d" % cur.rowcount)
