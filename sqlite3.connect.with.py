# -*- coding: utf-8 -*-
# sqlite3.connect.with.py
 
import sqlite3 as lite

con = lite.connect('test.db')

with con:
    cur = con.cursor()    
    cur.execute('SELECT SQLITE_VERSION()')
    data = cur.fetchone()
    print("SQLite version: %s" % data)
