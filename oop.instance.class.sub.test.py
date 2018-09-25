# -*- coding: utf-8 -*-
# oop.instance.class.sub.test.py

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector2D({}, {})'.format(self.x, self.y)

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __format__(self, format_spec):
        return '<Vector2D: x={0} y={1}>'.format(self.x, self.y)

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)


x = Vector2D(3, 4)
print(x)
y = Vector2D(5, 6)
print(y)

print(x - y)
