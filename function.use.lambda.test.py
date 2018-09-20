# -*- coding: utf-8 -*-
# function.use.lambda.test.py

# Выражение lambda
# Когда можно использовать lambda-выражения:
# Для создания таблиц переходов, которые представляют собой списки или словари действий, выполняемых по требованию:

L = [lambda x: x**2,   # Встроенные определения функций
     lambda x: x**3, 
     lambda x: x**4]   # Список из трех функций

for f in L:
    print(f(2))        # Выведет 4, 8, 16

print(L[0](3))         # Выведет 9

# Тот же пример без использования lambda:

def f1(x): return x ** 2
def f2(x): return x ** 3   # Определения именованных функций
def f3(x): return x ** 4

L = [f1, f2, f3]           # Ссылка по имени

for f in L:
    print(f(2))            # Выведет 4, 8, 16

print(L[0](3))             # Выведет 9

# Подобные таблицы действий в языке Python можно создавать с помощью словарей и других структур данных:
D = {
    'already': (lambda: 2 + 2),
    'got':     (lambda: 2 * 4),
    'one':     (lambda: 2 ** 6)
    }

print('D= ', D['got']())        # Выведет 8 
print('D= ', D['one']())        # Выведет 64 

# Тот же пример без использования lambda:
def d1(): return 2 + 2
def d2(): return 2 * 4
def d3(): return 2 ** 6

key = 'one'

print({'already': d1, 'got': d2, 'one': d3}[key]())

# Так же возможна реализация логики выбора внутри lambda-функций:

lower = (lambda x, y: x if x < y else y)

print(lower('bb', 'aa'))
print(lower('aa', 'bb'))
