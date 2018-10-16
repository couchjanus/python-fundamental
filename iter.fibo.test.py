# -*- coding: utf-8 -*-
# iter.fibo.test.py

from __future__ import print_function

import itertools

# итератор, который будет генерировать последовательность чисел Фибоначчи.

class fib:
    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value

f = fib()

print(list(itertools.islice(f, 0, 10)))

