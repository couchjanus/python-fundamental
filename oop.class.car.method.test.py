# -*- coding: utf-8 -*-
# oop.class.car.method.test.py

class Car(object):

    price = 1000

    def __init__(self, name):
        self._name = name

    def __repr__(self):
        return 'Car({})'.format(self._name)

    def beep(self):
        ''' Плохой класс Car'''
        print("Hate all.")

    def print_price(self):
        print(self.price)

    def price_up(self):
        self.price += 1

    def price_down(self):
        self.price -= 1


audi = Car('Audi')

# Вызов метода экземпляра
audi.beep()

# Вызов метода класса
Car.beep(audi)


audi.print_price()

audi.price_up()
audi.price_up()
audi.price_up()
audi.price_up()

audi.print_price()
