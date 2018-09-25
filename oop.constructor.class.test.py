# -*- coding: utf-8 -*-
# oop.constructor.class.test.py

# Принято присваивать полям, а также получать их значения, 
# путем вызова методов:

class User:
    def __init__(self, n, s):
        self.name = n
        self.surname = s

    def setName(self, n):
        self.name = n

    def getName(self):
        try:
            return self.name
        except:
            print("No name")

# конструктор класса не позволит создать объект без обязательных полей:
#  
p1 = User("Sam", "Baker")
print(p1.name, p1.surname)


class Rectangle:
    def __init__(self, w = 0.5, h = 1):
        self.width = w
        self.height = h
    def square(self):
        return self.width * self.height


rec1 = Rectangle(5, 2)
rec2 = Rectangle()
rec3 = Rectangle(3)
rec4 = Rectangle(h = 4)

print(rec1.square())
print(rec2.square())
print(rec3.square())
print(rec4.square())
