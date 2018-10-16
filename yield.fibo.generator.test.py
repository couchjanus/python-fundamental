# -*- coding: utf-8 -*-
# yield.fibo.generator.test.py

from __future__ import print_function

# используя ключевое слово yield можно упростить реализацию:

def fibonacci():
    prev, cur = 0, 1
    while True:
        yield prev
        prev, cur = cur, prev + cur

for i in fibonacci():
    print(i)
    if i > 100:
        break

fib = fibonacci()
print(next(fib))
print(next(fib))

for num, fib in enumerate(fibonacci()):
    print('{0}: {1}'.format(num, fib))
    if num > 9:
        break
