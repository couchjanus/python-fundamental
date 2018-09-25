# -*- coding: utf-8 -*-
# oop.class.object.test.py

class MyClass:
    pass

print(object.__dict__['__init__'])
# <slot wrapper '__init__' of 'object' objects>

print(object.__dict__['__new__'])
# <built-in method __new__ of type object at 0x8f8740>

# Раз есть такие методы, значит, получается, 
# что my_obj = MyClass() аналогичен последовательности вызовов:
# my_obj = object.__new__(MyClass)
# object.__init__(my_obj)

my_obj = MyClass()

print(my_obj)
print(my_obj.__class__)
print(my_obj.__class__ is MyClass)
