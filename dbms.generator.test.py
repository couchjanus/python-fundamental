# -*- coding: utf-8 -*-
# dbms.generator.test.py
from __future__ import generators    # needs to be at the top of your module

import sqlite3 as lite

db_filename = 'shopaholic.db'

con = lite.connect(db_filename, isolation_level = 'IMMEDIATE')
con.text_factory = lambda x: str(x, 'utf-8')

# Метод cursor.fetchmany() возвращает следующие «n» строк запроса
def ResultIter(cursor, arraysize=1000):
    'An iterator that uses fetchmany to keep memory usage down'
    while True:
        results = cursor.fetchmany(arraysize)
        if not results:
            break
        for result in results:
            yield result

# where con is a DB API 2.0 database connection object

cursor = con.cursor()

# for result in cursor.fetchall():
#     print(result)

# resLen = list(ResultIter(cursor))
# print(len(resLen))

cursor.execute("SELECT COUNT(*) FROM products")
print(cursor.fetchone()[0])

cursor.execute('select * from products')

for result in ResultIter(cursor):
    print(result)
