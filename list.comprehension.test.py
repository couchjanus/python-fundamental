# -*- coding: utf-8 -*-
# list.comprehension.test.py

a = [ i*i for i in range(1,10)]

print(a)

# Конструктор может быть условным
# найдем квадраты четных натуральных чисел:

a = [ i*i for i in range(1,10) if i % 2 == 0]

print(a)

# отсортируем слова в предложении в порядке их длительности:

words = ' to perform the task of sorting the words in a string by their length'.split()

wordlens = [(len(word), word) for word in words]
wordlens.sort()

print(' '.join(w for (_, w) in wordlens))
