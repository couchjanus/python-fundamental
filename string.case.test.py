# -*- coding: utf-8 -*-
# string.case.test.py

# S.upper()	Преобразование строки к верхнему регистру
# S.lower()	Преобразование строки к нижнему регистру

# S.swapcase()	Переводит символы нижнего регистра в верхний, а верхнего – в нижний
# S.title()	Первую букву каждого слова переводит в верхний регистр, а все остальные в нижний

# string.swapcase() – инвертирует ЗАГЛАВНЫЕ в строчные, и наоборот:

string = 'This Is Some String'

print(string.swapcase())

# string.lower() – возвращает строку, в которой все символы переведены в строчные:

string = 'This Is Some string'
print(string.lower())

# string.upper() – возвращает строку, в которой все символы переведены в ЗАГЛАВНЫЕ:

string = 'This Is Some String'

print(string.upper())

# string.title() – возвращает стркоу, в которой все первые символы элементов переведены в Заглавные (“titlestyle“):

string = 'This is some string'

print(string.title())

