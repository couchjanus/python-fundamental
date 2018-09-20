# -*- coding: utf-8 -*-
# function.closure.test.py

# Функция может быть любой сложности и возвращать любые объекты (списки, кортежи, и даже функции!):

def newfunc(n):
    def myfunc(x):
        return x + n
    return myfunc

new = newfunc(100)  # new - это функция
print(new(200))


# closure example:

def attribution(name):
   return lambda x: x + ' -- ' + name

pp = attribution('John')
print(pp('Dinner is in the fridge'))
