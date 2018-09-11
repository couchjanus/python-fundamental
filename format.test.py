# -*- coding: utf-8 -*-
# format.test.py

'{0}, {1}, {2}'.format('a', 'b', 'c') # 'a, b, c'
'{}, {}, {}'.format('a', 'b', 'c') # 'a, b, c'
'{2}, {1}, {0}'.format('a', 'b', 'c') # 'c, b, a'
'{2}, {1}, {0}'.format(*'abc') # 'c, b, a'
'{0}{1}{0}'.format('abra', 'cad') # 'abracadabra'
'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W') # 'Coordinates: 37.24N, -115.81W' 
coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
'Coordinates: {latitude}, {longitude}'.format(**coord) # 'Coordinates: 37.24N, -115.81W'


print("{}, {}, how are you?".format("Hello", "Sally"))

print("{!s}".format("я строка"))  # str

print("{!r}".format("я строка"))  # repr

print("{!a}".format("я строка")) # ascii

print("'\\u044f \\u0441\\u0442\\u0440\\u043e\\u043a\\u0430'")


# выровнять строку в “блоке” фиксированной длины,
print('{!r:~^40}'.format('Thankyou for using calculator.py!'))
# привести число к другой системе исчисления,
print("int: {0:d} hex: {0:x}".format(42))
print("oct: {0:o} bin: {0:b}".format(42))
# потребовать наличие знака в строковом представлении числа и зафиксировать количество знаков до или после запятой.
print("{:+08.2f}".format(-42.42))
