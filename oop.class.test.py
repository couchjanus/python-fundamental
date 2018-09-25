# -*- coding: utf-8 -*-
# oop.class.test.py

# Минимально возможное определение класса выглядит так:

class A:
    pass

class B:
    def m1(self, x):
        # блок кода метода
        pass

class AA:
    attr1 = 2 * 2

# добавить атрибуты можно и после определения:
def my_method(self, x):
    return x * x

A.m1 = my_method
A.attr1 = 2 * 2

class Y:
    """The vertical motion of a ball."""
    val = "hello"

a = Y()
print(a.val)

class Mat:
    """Mathematical function for the vertical motion of a ball.

    Methods:
        constructor(v0): set initial velocity v0.
        value(t): compute the height as function of t.
        formula(): print out the formula for the height.

    Attributes:
        v0: the initial velocity of the ball (time 0).
        g: acceleration of gravity (fixed).

    Usage:
    >>> y  =  Y(3)
    >>> position1 = y.value(0.1)
    >>> position2 = y.value(0.3)
    >>> print  y.formula()
    v0*t - 0.5*g*t**2; v0=3
    """
    pass