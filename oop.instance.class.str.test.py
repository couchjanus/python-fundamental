# -*- coding: utf-8 -*-
# oop.instance.class.str.test.py

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector2D({}, {})'.format(self.x, self.y)

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)


x = Vector2D(3, 4)
print(x)
print(repr(x))

y = Vector2D(5, 6)
print(y)
print(repr(y))