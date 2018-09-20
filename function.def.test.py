# -*- coding: utf-8 -*-
# function.def.test.py

def func(x, y):
    return x**2 + y**2

lfunc = lambda x, y: x**2 + y**2

# При вызове функции задаются фактические аргументы. Например:

func(2, y=7)

lfunc(2, y=7)


def bigger(a,b):
    if a > b:
        return a # Если a больше чем b, то возвращаем b и прекращаем выполнение функции
    return b # Незачем использовать else. Если мы дошли до этой строки, то b, точно не меньше чем a
 
# присваиваем результат функции bigger переменной num

num = bigger(23,42)

def pfunc():
    pass
