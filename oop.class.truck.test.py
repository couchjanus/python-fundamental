# -*- coding: utf-8 -*-
# oop.class.truck.test.py

class Car(object):
    wheels = 4

    def __init__(self, brand, model):
        self._brand = brand
        self._model = model
    
    def __repr__(self):
        return 'Car({} {})'.format(self._brand, self._model)

    def foo(self):
        print('Class Far')

mustang = Car('Ford', 'Mustang')
rodeo = Car('Ford', 'Rodeo')
accord = Car('Honda', 'Accord')

class Truck(object):
    wheels = 8

    def __init__(self, brand, model):
        self._brand = brand
        self._model = model
    
    def __repr__(self):
        return 'Car({} {})'.format(self._brand, self._model)

    def bar(self):
        print('class Truck')

print(accord.__dict__)
print(accord.__class__) # <class '__main__.Car'>

# Переопределим класс объекта accord:
accord.__class__ = Truck
print(accord.__class__) # <class '__main__.Truck'>

# Смотрим, что поменялось.
print(accord.__dict__)

# Значения {'_model': 'Accord', '_brand': 'Honda'} остались прежними,
# т.е. __init__ не вызывался при смене класса.

# Доступ к классовым переменным и методам «прошлого» класса Car пропал:
# А вот классовые переменные и методы класса Truck доступы:
print(accord.wheels)
print(accord.bar())
