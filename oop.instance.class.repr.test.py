# -*- coding: utf-8 -*-
# oop.instance.class.repr.test.py

class Point:
    def __init__(self, x, y, z):
        self.coord = (x, y, z)

    def __repr__(self):
        return "Point(%s, %s, %s)" % self.coord

p = Point(0.0, 1.0, 0.0)

print(p) 



