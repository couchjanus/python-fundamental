# -*- coding: utf-8 -*-
# in.str.test.py

#  ключевое слово in. 

stmt = "mary had a little lamb"
for char in stmt[11:18]:
    print(char) # печать каждого символа в срезе

if 'x' in stmt: 
    print('got x') # проверка на вхождение символа

if 'y' in stmt: 
    print('got y') # проверка на вхождение символа
