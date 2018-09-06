# -*- coding: utf-8 -*-
# set.test.py

# Сгенерировать сет можно с помощью функции:
s = set('abcde')
s2 = set('aghij')

# Над сетами можно выполнять разные операции, например:
# вычитание:
s3 = s - s2

#  сложение:
s3 = s | s2

# пересечение:
s3 = s & s2

# add() — добавление элемента:
s.add(6)
# remove() — удаление элемента:
s.remove('a')
# Итерация:
for item in s:print (item)

L = [1,2,3,4,1,2,6,7]
set(L)
L = list(set(L))

programmers = set(['ivan','petro','simon'])
managers = set(['ivan','mox','igor'])

# Найти тех, кто одновременно и программист, и менеджер:
print(programmers & managers)
# Найти всех программистов и менеджеров:
print(programmers | managers)
# Найти программистов, которые не менеджеры:
print(programmers - managers)

# Пример: определим простые числа в диапазоне до 100:
def f(x):
    for y in range(2, x):
        if x%y==0: return 0
    return 1

print(list(filter(f, range(2, 100))))

# Например, создадим список кубов натуральных чисел от 1 до 10:

def cube(x): return x*x*x
c = map(cube, range(1, 11))
print(list(c))

# zip(sequence) — функция, аналогичная map(), но может работать с последовательностями разной длины, возвращает список кортежей:

a = (1, 2, 3, 4)
b = (5, 6, 7, 8)
print(list(zip(a, b)))
