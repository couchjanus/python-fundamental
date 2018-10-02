# -*- coding: utf-8 -*-
# sqlite3.delete.py
 
import sqlite3 as lite

# Подключаемся к базе данных
conn = lite.connect('test.db')

cursor = conn.cursor()

sql = "DELETE FROM cars WHERE Name = 'BMW'"

cursor.execute(sql)
conn.commit()
