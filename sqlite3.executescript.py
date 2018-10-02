# -*- coding: utf-8 -*-
# sqlite3.executescript.py
 
import sqlite3 as lite
import sys

try:
    # Подключаемся к базе данных
    con = lite.connect('test.db')
    cur = con.cursor()  
    cur.executescript("""
        DROP TABLE IF EXISTS cars;
        CREATE TABLE cars(Id INT, Name TEXT, Price INT);
        INSERT INTO cars VALUES(1,'Audi',52642);
        INSERT INTO cars VALUES(2,'Mercedes',57127);
        INSERT INTO cars VALUES(3,'Skoda',9000);
        INSERT INTO cars VALUES(4,'Volvo',29000);
        INSERT INTO cars VALUES(5,'Bentley',350000);
        INSERT INTO cars VALUES(6,'Citroen',21000);
        INSERT INTO cars VALUES(7,'Hummer',41400);
        INSERT INTO cars VALUES(8,'Volkswagen',21600);
        """)
 
    con.commit()
    print("8 rows have been inserted into table cars successfully!")
    
except lite.Error as e:
    if con:
        con.rollback()
        
    print("Error %s:" % e.args[0])
    sys.exit(1)
    
finally:
    if con:
        con.close()
