# -*- coding: utf-8 -*-
# iteration.list.test.py

# Создать список L
L=[3,1,5,2.5,5.5,7.5] 
L2=[31,32,35,'a','b','cd',2.5,5.5,7.5] 
print(L)

# простая итерация списка:

for x in L:
    print(x)

# сортированная итерация:

for x in sorted(L):
    print(x)

# уникальная итерация:

for x in set(L):
    print(x)


# итерация в обратном порядке:

for x in reversed(L):
    print(x)

# исключающая итерация — например, вывести элементы 1-го списка, которых нет во 2-м списке:

for item in set(L).difference(L2):
    print(item)
