# -*- coding: utf-8 -*-
# stopiteration.test.py

from __future__ import print_function

# Итерируемый объект - любой объект, реализующий метод __iter__ или __getitem__
items = [1, 2, 3]

for item in items:
    print(item)

print(items[2])

# если бы не было цикла for, то для эмуляции его работы, пришлось бы написать такой код:

it = iter(items)
while True:
    try:
        print(next(it))
    except StopIteration:
        break

# по итератору можно пройтись только один раз

print(next(it))

# Traceback (most recent call last):
#   File "stopiteration.test.py", line 25, in <module>
    # print(next(it))
# StopIteration
