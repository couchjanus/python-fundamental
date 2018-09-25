# -*- coding: utf-8 -*-
# oop.class.attr.test.py

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

# Работа с атрибутам объекта: установка, удаление и поиск, равносильна
# вызову встроенных функций settattr, delattr, getattr:

accord.x = 1
print(accord.x)
setattr(rodeo, 'x', 1)
print(rodeo.x)

del rodeo.x

print(rodeo.x)

delattr(accord, 'x')
print(accord.x)
getattr(accord, 'x')

# При этом стоит стоит понимать, что setattr и delattr
# влияют и изменяют только
# сам объект (точнее .__dict__), и не изменяют класс объекта.

# wheels — является классовой переменной, т.е. она «принадлежит»
# классу Car, а не объекту:

print(accord.wheels)   #
print(accord.__dict__)  # 

# Если мы попытаемся удалить этот атрибут, 
# то получим ошибку, т.к. delattr будет пытаться удалить 
# атрибут из accord.__dict__

delattr(accord, 'wheels')
del accord.wheels

# если мы попытаемся изменить (установить) атрибут,
# setattr поместит его в __dict__, 
# специфичный для данного, конкретного объекта.

accord.wheels = 10
print(accord.wheels)   #
print(accord.__dict__)  # 

# Ну и раз есть 'wheels' в __dict__ объекта, 
# его можно удалить с помощью delattr:
del accord.wheels
# После удаления, accord.wheels будет возвращать 
# значение классовой переменной:
print(accord.wheels)   #
print(accord.__dict__)  # 

