# -*- coding: utf-8 -*-
# comparison.sequence.test.py

print((1, 2, 3) < (1, 2, 4))  # True
print([1, 2, 3] < [1, 2, 4])  # True

print('ABC' < 'C' < 'Pascal' < 'Python')

print((1, 2, 3, 4) < (1, 2, 4))
print((1, 2) < (1, 2, -1))
print((1, 2, 3) == (1.0, 2.0, 3.0))

print((1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4))

# Python 2
print([1, 'two'] < ['two', 1])  # True
# Python 3
print([1, 'two'] < ['two', 1])  # TypeError: '<' not supported between instances of 'int' and 'str'


a = [3, 2, 1]
b = [1, 2, 3]
d = [3, 2, 2]
e = [3, 2]
f = [3, 2, 'a']

a > b  # True
a > d  # False
d > b  # True
a > e  # True
a > f  # False


a = (3, 2, 1)
b = (1, 2, 3)
d = (3, 2, 2)
e = (3, 2)
f = (3, 2, 'a')
a > b  # True
a > d  # False
d > b  # True
a > e  # True

# Python 3
a > f  # TypeError: '>' not supported between instances of 'int' and 'str'
# Python 2
a > f  # False





