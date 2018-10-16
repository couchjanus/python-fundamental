# -*- coding: utf-8 -*-
# generator.test.py

from __future__ import print_function

# Пример простой генераторной функции:

def generator():
    for i in range(3):
        yield i

# Через цикл for
for i in generator():
    print(i)

# Вручную
gen = generator()

next(gen)
next(gen)
next(gen)
next(gen)
