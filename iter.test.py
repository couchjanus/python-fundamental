# -*- coding: utf-8 -*-
# iter.test.py

from __future__ import print_function

# из функции которая произвольно возвращает 1-6, 
# можно сделать итератор, который будет возвращать значения пока не «выпадет» 6:

from random import randint

def d6():
    return randint(1, 6)

for roll in iter(d6, 6):
    print(roll)