# -*- coding: utf-8 -*-
# dbms06.py

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
    
    def get_selected(self, table, field, *args):
        """recive table name, pk and return a dictionary
       
        @param name: table,field,*args
        @return: dictionary
        @rtype: dictionary
        """
        
        d = {}
        sql = "SELECT * FROM %s WHERE %s =?" % (table, field)

        for k,v in enumerate(self.read(False, sql, args)):
            d[k]=v
            
        return d

    def write(self, sql, args=()):
        try:
            con = self.get_connection() 
            cur = con.cursor()
            cur.execute(sql,args)
            con.commit()
            
        except:
            con.rollback()
            print (sys.exc_info()[0])
            print (sys.exc_info()[1])
            print (sys.exc_info()[2])
            
        finally:
            try:
                cur.close()
                con.close()
            except:
                print (sys.exc_info()[0])
                print (sys.exc_info()[1])
                print (sys.exc_info()[2])
    
    def get_insert_sql(self,table, n):
        return "INSERT INTO %s(%s)VALUES(%s)"%(table,",".join(self.get_fields(table)), ",".join("?"*n))

    def get_fields(self, table):
        """Return fields name for the passed table ordered by field position"""

        try:

            columns = []
            ret = []

            sql = 'SELECT * FROM %s ' % table
            con = self.get_connection()
            cur = con.cursor()
            cur.execute(sql)

            for field in cur.description:
                columns.append(field[0])
            cur.close()
            
            for k,v in enumerate(columns):
                if k > 0:
                    ret.append(v)
            return ret
        except:
            print (sys.exc_info()[0])
            print (sys.exc_info()[1])
            print (sys.exc_info()[2])
            
        finally:
            try:
                cur.close()
                con.close()
            except:
                print (sys.exc_info()[0])
                print (sys.exc_info()[1])
                print (sys.exc_info()[2])

    def get_update_sql(self,table,pk):
        return "UPDATE %s SET %s =? WHERE %s =?"%(table," =?, ".join(self.get_fields(table)),pk)

    def get_update_sql_args(self, args, item):
        l = list(args)
        l.append(item)
        return tuple(l)
       


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
