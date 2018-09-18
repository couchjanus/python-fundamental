# -*- coding: utf-8 -*-
# string.find.test.py

# string.find(символ, начало, конец) – возвращает индекс первого найденного символа, начало-конец – опциональны, или -1 – если не найдено

string = 'This is some string'
string.find('i')

string.find('i', 3, 7)

string.find('g', 0, 7)

# string.index(символ, начало, конец)  – то же, что и find(), но вызывает ValueError в случае, если символ не найден:

string.index('i')
string.index('g', 0, 7)

# string.rfind(символ, начало, конец) – возвращает последний (самый большой) индекс найденного символа, начало-конец – опциональны, -1 – если не найден:

string = 'ia ia ia'

string.rfind('i')

string.rfind('i', 0, 2)

string.rfind('i', 0, 3)

string.rfind('i', 0, 4)

string.rfind('i', 1, 3)

# string.rindex(символ, начало, конец) – то же, что и rfind(), но вызывает ValueError, если не найдено:

string.rindex ('i')

string.rindex('i')

string.rindex('i', 1, 3)

