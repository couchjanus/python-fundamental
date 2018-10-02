# -*- coding: utf-8 -*-
# sqlite3.insert.into.table.py
 
import sqlite3 as lite

# Подключаемся к базе данных
con = lite.connect('test.db')
 
with con:
    cur = con.cursor()    
    # Создаем таблицу
    # cur.execute("CREATE TABLE cars(Id INT, Name TEXT, Price INT)")

    # Вносим данные
    cur.execute("INSERT INTO cars VALUES(1, 'Audi', 52642)")
    cur.execute("INSERT INTO cars VALUES(2, 'Mercedes', 57127)")
    cur.execute("INSERT INTO cars VALUES(3, 'Skoda', 9000)")
    cur.execute("INSERT INTO cars VALUES(4, 'Volvo', 29000)")
    cur.execute("INSERT INTO cars VALUES(5, 'Bentley', 350000)")
    cur.execute("INSERT INTO cars VALUES(6, 'Citroen', 21000)")
    cur.execute("INSERT INTO cars VALUES(7, 'Hummer', 41400)")
    cur.execute("INSERT INTO cars VALUES(8, 'Volkswagen', 21600)")

    print("8 rows have been inserted into table cars successfully!")

