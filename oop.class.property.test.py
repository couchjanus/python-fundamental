# -*- coding: utf-8 -*-
# oop.class.property.test.py

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

print(Car.__class__) # <type 'type'>

# Правда __dict__ у классов не совсем словарь
print(Car.__dict__) # 

print('_'*70) #
# __dict__ ответственен за доступ к внутреннему пространству имен, в котором хранятся методы, дескрипторы, переменные, свойства и прочее:

print(dict(Car.__dict__)) # 
print('_'*70) #
print(Car.__dict__.keys()) #

# В классах помимо class и dict, имеется еще несколько специальных атрибутов: bases — список прямых родителей, name — имя класса.
print('_'*70) #
print(Car.__bases__)

print('_'*70) #
print(Car.__name__)

# Класс является объектом.
class A(object):
    pass

print(isinstance(A, object)) # True

# Число — это тоже объект.
print(isinstance(42, object)) # True

# Класс — это класс (т.е. тип).
print(isinstance(A, type)) # True

# А вот число классом (типом) не является.
print(isinstance(42, type)) # False

# Ну и a — тоже обычный объект.
a = A()
print(isinstance(a, A)) # True
print(isinstance(a, object)) # True
print(isinstance(a, type)) # False

# И у A всего один прямой родительский класс — object.
print(A.__bases__) # (<type 'object'>,)

# Часть специальных параметров можно даже менять:
print(A.__name__) # 'A'
A.__name__ = 'B'
print(A) # <class '__main__.B'>

# С помощью getattr получаем доступ к атрибутам класса:
# print A.qux # 'A'
# print A.foo # <unbound method A.foo>

