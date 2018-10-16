# -*- coding: utf-8 -*-
# yield.test.py

from __future__ import print_function

# Рассмотрим работу yield:

def gen_fun():
    print('block 1')
    yield 1
    print('block 2')
    yield 2
    print('end')

for i in gen_fun():
    print(i)

# block 1
# 1
# block 2
# 2
# end

# Генераторная функция разбивается на части:
# def gen_fun_1():
#     print('block 1')
#     return 1
# def gen_fun_2():
#     print('block 2')
#     return 2
# def gen_fun_3():
#     print('end')
# def gen_fun_end():
#    raise StopIteration
