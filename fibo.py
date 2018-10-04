# -*- coding: utf-8 -*-
# fibo.py

"""Модуль вычисления чисел Фибоначчи"""
 
def fib(n):    # вывести числа Фибоначчи вплоть до n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()
 
def fib2(n): # вернуть числа Фибоначчи вплоть до n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
