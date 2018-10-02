# -*- coding: utf-8 -*-
# sqlite3.lastrowid.py
 
import sqlite3 as lite
import sys

# Подключаемся к базе данных
con = lite.connect('test.db')
 
with con:
    cur = con.cursor()    
    cur.execute("DROP TABLE IF EXISTS cars");
    cur.execute("CREATE TABLE cars(Id INTEGER PRIMARY KEY, Name TEXT, Price INT)");
    cur.execute("INSERT INTO cars(Name, Price) VALUES('Audi',52642)");
    cur.execute("INSERT INTO cars(Name, Price) VALUES('Mercedes',57127)");
    cur.execute("INSERT INTO cars(Name, Price) VALUES('Skoda',9000)");
    cur.execute("INSERT INTO cars(Name, Price) VALUES('Volvo',29000)");
    cur.execute("INSERT INTO cars(Name, Price) VALUES('Bentley',350000)");
    cur.execute("INSERT INTO cars(Name, Price) VALUES('Citroen',21000)");
    cur.execute("INSERT INTO cars(Name, Price) VALUES('Hummer',41400)");
    cur.execute("INSERT INTO cars(Name, Price) VALUES('Volkswagen',21600)");
       
    lid = cur.lastrowid
    print("The last Id of the inserted row is ", lid)
