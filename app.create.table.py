# -*- coding: utf-8 -*-
# app.create.table.py
 
import sqlite3 as lite

# Подключаемся к базе данных
con = lite.connect('shopaholic.db')
 
with con:
    # Создаем таблицу
    cur = con.cursor()  
    cur.executescript("""
        DROP TABLE IF EXISTS products;
        CREATE TABLE 'products'('product_id' INTEGER PRIMARY KEY, 'product' TEXT, 'brand_id' INTEGER, 'category_id' INTEGER,'description' TEXT, 'price' REAL, 'stock' INTEGER, 'available' BOOLEAN DEFAULT '1');
        INSERT INTO products VALUES(1,'Soft drinks for cats', 1, 1, 'description', 111, 2, 1);
        DROP TABLE IF EXISTS categories;
        CREATE TABLE 'categories' ('category_id' INTEGER PRIMARY KEY, 'category' TEXT,'description' TEXT,'enable' BOOLEAN DEFAULT '1');
        INSERT INTO "categories" VALUES(1, 'Beverages', 'Soft drinks, coffees, teas, beers, and ales', 1);
        DROP TABLE IF EXISTS brands;
        CREATE TABLE 'brands' ('brand_id' INTEGER PRIMARY KEY, 'company' TEXT, 'enable' BOOLEAN DEFAULT '1');
        INSERT INTO "brands" VALUES(1, 'Exotic Liquids', 1);
        """)
    con.commit()
    print("1 rows have been inserted into tables products, brands and categories successfully!")



