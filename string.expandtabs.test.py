# -*- coding: utf-8 -*-
# string.expandtabs.test.py

# string.expandtabs(количество) – меняет количество символов в табуляции, если не указано количество – используется по-умолчанию 8:

string = 'tThis Is Some stringt'

print(string)
 
print(string.expandtabs(2))

print(string.expandtabs())
