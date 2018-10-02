# -*- coding: utf-8 -*-
# sqlite3.create.table.py
 
import sqlite3 as lite

# Подключаемся к базе данных
con = lite.connect('test.db')
 
with con:
    cur = con.cursor()    
    # Создаем таблицу
    cur.execute("CREATE TABLE cars(Id INT, Name TEXT, Price INT)")
    print("Table cars created successfully!")

