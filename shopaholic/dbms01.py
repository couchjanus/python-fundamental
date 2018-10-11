# -*- coding: utf-8 -*-
# dbms01.py

import sqlite3 as lite
import os
import sys

class DBMS(object):
    
    db_filename = 'shopaholic.db'
    
    def __init__(self,):
        super(DBMS, self).__init__()
    
    def get_connection(self,):

        con = lite.connect(self.db_filename, isolation_level = 'IMMEDIATE')
        con.text_factory = lambda x: str(x, 'utf-8')
        return con
    
    def read(self, fetch, query, parameters=()):

        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            cursor.execute(query, parameters)
            conn.commit()
            
            if fetch == True:
                rs =  cursor.fetchall()
            else:
                rs =  cursor.fetchone()
            
            return rs

def main():

    foo = DBMS()
    print (foo)

    sql = "SELECT * FROM products"
    rs = foo.read(True, sql)
    if rs:
        for i in enumerate(rs):
            print (i)
   
    input('end')
    
    
if __name__ == "__main__":
    main()
