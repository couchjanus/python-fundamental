# -*- coding: utf-8 -*-
# yield.generator.test.py

from __future__ import print_function

def cool_range(start, stop, inc):
    x = start
    while x < stop:
        yield x
        x += inc

for n in cool_range(1, 5, 0.5):
    print(n)

print(list(cool_range(0, 2, 0.5)))



