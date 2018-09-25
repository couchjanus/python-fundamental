# -*- coding: utf-8 -*-
# oop.class.car.test.py

class Car(object):
    cars = 'A'

    def __init__(self, name):
        self._name = name

    def __repr__(self):
        return 'Car({})'.format(self._name)

    def foo(self):
        print('foo car')


print(Car.__bases__)  # 


audi = Car('Audi')

print(audi)

# У audi тоже есть атрибут __dict__:
print(audi.__dict__)   # {'name': 'Audi'}

# У a тоже есть атрибут __class__
print(audi.__class__)  # <class '__main__.Car'>

print(type(audi))  # <class '__main__.Car'>
print(audi.__class__ is type(audi))  # True
