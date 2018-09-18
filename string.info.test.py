# -*- coding: utf-8 -*-
# string.info.test.py


# Строковые методы, для получения информации об объекте
# string.count(символ, начало, конец) – возвращает количество вхождений символа, начало-конец – опциональны, отсчёт с 0:

string = 'This is some string'

print(string.count('T'))

print(string.count('T', 0, 2))

print(string.count('T', 2, 6))

type(string.count('T', 2, 6))


# string.startswith(символ, начало, конец) – возвращает True, если строка начинается с символа, начало-конец – опциональны:

string = 'ia ia ia'

string.startswith('i', 1, 3)

string.startswith('i')

# string.endswith(символ, начало, конец) – возвращает True, если строка заканчивается на символ, начало-конец – опциональны, отсчёт с нуля:

string = 'This is some string'

string.endswith('g')

string.endswith('g', 0, 2)
