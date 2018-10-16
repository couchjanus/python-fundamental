# -*- coding: utf-8 -*-
# fibonacci.generator.test.py

from __future__ import print_function

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Печатает все числа последовательности Фибоначчи, меньше 1000
for i in fibonacci_generator():
    if  i > 1000:
        break
    print(i)
