# -*- coding: utf-8 -*-
# string.strip.test.py

# string.lstrip(символы) – возвращает строку, с обрезанными с левой стороны символами (по-умолчанию – пробелы):


# S.lstrip([chars])	Удаление пробельных символов в начале строки
# S.rstrip([chars])	Удаление пробельных символов в конце строки
# S.strip([chars])	Удаление пробельных символов в начале и в конце строки

string = 'This Is Some string'
print(string.lstrip('T'))

# string.rstrip(символы) – то же, но с правой стороны:

print(string.rstrip('g'))

# string.strip(символы) – выполняет lstrip() и rstrip() для символов, по-умолчанию – пробелы:

string = '     This Is Some string     '
print(string.strip())

string = '-----This Is Some string-----'

print(string.strip('-'))
