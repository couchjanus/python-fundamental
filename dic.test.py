# -*- coding: utf-8 -*-
# dic.test.py

d = {1:'one', 2:'two', 4:'four'}
d0 = {0 : 'zero'}
d[1] # 'one'
d[0] = 0
del d[0]
print(d) # печать всего хеша


h1 = {1:"one", 2:"two", 3:"three"}
h2 = {0:"zero", 5:"five"}
h3 = {"z":1, "y":2, "x":3}

# Цикл по паре ключ-значение

for k,v in h1.items():
    print(k, ' ', v)

for key, val in h3.items():
    print(key, val)
# Цикл по ключам
for key in h3.keys():
    print(key, h3[key])

# Цикл по значениям
for val in h3.values():
    print(val)

# Добавление элементов из другого хеша
h3.update(h1) # пополняем словарь из другого словаря

# Количество пар в хеше
print(len(h3)) # количество пар ключ-значение
