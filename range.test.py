# range.test.py

type(range(3))  # class 'range'
list(range(5))  # [0, 1, 2, 3, 4]
list(range(1, 5))  # [1, 2, 3, 4]
list(range(0, 10, 3))  # [0, 3, 6, 9]
list(range(0, -5, -1))  # [0, -1, -2, -3, -4]
list(range(0))  # []
list(range(1, 0))  # []

print(type(range(3)))

print(list(range(5)))

range(0) == range(2, 1, 3) 

range(0, 3, 2) == range(0, 4, 2)

type(range(3))  # type 'list'
type(xrange(3))  # type 'xrange'
