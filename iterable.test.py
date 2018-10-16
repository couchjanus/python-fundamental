# -*- coding: utf-8 -*-
# iterable.test.py

from __future__ import print_function

# Итерируемый объект - любой объект, реализующий метод __iter__ или __getitem__
items = [1, 2, 3]


print(dir(items))


lst = [1, 2, 3]
for i in lst:
   print(i)



Lst = [x*x for x in xrange(3)]

for i in Lst:

   print(i)



# Как работает цикл for
# В большинстве случаев, при обработке итерируемого объекта используется цикл for:

for item in items:
    print(item)


# если бы не было цикла for, то для эмуляции его работы, пришлось бы написать такой код:

it = iter(items)
while True:
    try:
        print(next(it))
    except StopIteration:
        break

