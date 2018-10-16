# -*- coding: utf-8 -*-
# container.test.py
import math


assert 1 in [1, 2, 3]      # списки
assert 4 not in [1, 2, 3]
assert 1 in {1, 2, 3}      # множества
assert 4 not in {1, 2, 3}
assert 1 in (1, 2, 3)      # кортежи
assert 4 not in (1, 2, 3)

# assert 4 in (1, 2, 3), "number should be in (1, 2, 3)"

d = {1: 'foo', 2: 'bar', 3: 'qux'}
assert 1 in d
assert 4 not in d
assert 'foo' not in d  # 'foo' не является _ключом_ словаря

s = 'foobar'
assert 'b' in s
assert 'x' not in s

assert 'foo' in s


def chkassert(num):
    assert type(num) == int

# chkassert('a')

x = "hello"
#if condition returns False, AssertionError is raised:
# assert x == "goodbye", "x should be 'hello'"

# Python assert example

# defining the function definition
def divide(num1, num2):
   assert num2 > 0 , "Divisor cannot be zero"
   return num1/num2
# calling the divide function
a1 = divide(12,3)
# print the quotient
print(a1)
# this will give the assertion error
a2 = divide(12,0)
print(a2)

def sqrt(a,b,c):
   assert b*b >= 4*a*c, "Cannot find square root of negative number, found %s < %s" % (b*b, 4*a*c)
   return math.sqrt(b*b - 4*a*c)

print(sqrt(10, 12, 3))
# this will cause assertion error
print(sqrt(-4, 5, -3))



# content of test
def f():
    return 3

def test_function():
    assert f() == 4