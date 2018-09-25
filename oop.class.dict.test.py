# -*- coding: utf-8 -*-
# oop.class.dict.test.py

class Car(object):
    wheels = 4

    def __init__(self, brand, model):
        self._brand = brand
        self._model = model
    
    def __repr__(self):
        return 'Car({} {})'.format(self._brand, self._model)

    def foo(self):
        print('foo car')

print(Car.__dict__)

mustang = Car('Ford', 'Mustang')

print(mustang)

# Чтобы найти атрибут объекта mustang, python отыскивает:

# Сам объект (mustang.__dict__ и его системные атрибуты):
print(mustang.__dict__)   # 

# Класс объекта (mustang.__class__.__dict__). 
# Только __dict__ класса, не системные атрибуты.
print(mustang.__class__.__dict__) 

mustang = Car('Ford', 'Mustang')
print(mustang.wheels)
print(Car.wheels)

rodeo = Car('Ford', 'Rodeo')
accord = Car('Honda', 'Accord')

print(rodeo.wheels)
print(accord.wheels)

# Добавление объекту accord атрибута miles, никак не отражается на rodeo.
accord.miles = 10000

print(rodeo.__dict__)
print(accord.__dict__)

# В случае присваивания значения атрибуту экземпляра, 
# изменяется только __dict__ экземпляра, 
# то есть значение в __dict__ класса остаётся неизменным
