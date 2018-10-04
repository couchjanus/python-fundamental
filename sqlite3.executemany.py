# -*- coding: utf-8 -*-
# sqlite3.executemany.py
 
import sqlite3 as lite

# Подключаемся к базе данных
con = lite.connect('test.db')
 
cars = (
    (1, 'Audi', 52642),
    (2, 'Mercedes', 57127),
    (3, 'Skoda', 9000),
    (4, 'Volvo', 29000),
    (5, 'Bentley', 350000),
    (6, 'Hummer', 41400),
    (7, 'Volkswagen', 21600)
)
 
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS cars")
    cur.execute("CREATE TABLE cars(Id INT, Name TEXT, Price INT)")
    cur.executemany("INSERT INTO cars VALUES(?, ?, ?)", cars)

    print("7 rows have been inserted into table cars successfully!")
