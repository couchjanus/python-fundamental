# -*- coding: utf-8 -*-
# oop.get.set.class.test.py

# Принято присваивать полям, а также получать их значения, 
# путем вызова методов:

class User:
    def setName(self, n):
        self.name = n
    def getName(self):
        try:
            return self.name
        except:
            print("No name")

first = User()
second = User()

first.setName("Bob")

first.getName()

second.getName()

# Подобные методы называют сеттерами (set – установить) 
# и геттерами (get – получить).
