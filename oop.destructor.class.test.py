# -*- coding: utf-8 -*-
# oop.destructor.class.test.py

class Line:
    def __new__(cls):
        return super(Line, cls).__new__(cls)
        
    def __init__(self, p1, p2):
        self.line = (p1, p2)

    def __del__(self):
        print("Удаляется линия %s - %s" % self.line)

l = Line((0.0, 1.0), (0.0, 2.0))

del l # Удаляется линия (0.0, 1.0) - (0.0, 2.0)

