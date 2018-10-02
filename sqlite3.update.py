# -*- coding: utf-8 -*-
# sqlite3.update.py
 
import sqlite3 as lite

# Подключаемся к базе данных
conn = lite.connect('test.db')

cursor = conn.cursor()

sql = """
UPDATE cars 
SET Name = 'BMW' 
WHERE Price = 44000
"""

cursor.execute(sql)
conn.commit()
