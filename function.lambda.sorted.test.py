# -*- coding: utf-8 -*-
# function.lambda.sorted.test.py

# sorted()
print(sorted([[3, 4], [3, 5], [1, 2], [7, 3]], key=lambda x: x[1]))

# Почему анонимные функции (lambda), определенные в цикле с разными значениями, возвращают один и тот же результат? 
# Например, вы написали следующий код:

squares = []

for x in range(5):
   squares.append(lambda: x**2)

# Это даёт вам список из 5 функций, считающих x**2. 
# Можно ожидать, что, будучи вызванными, они вернут, соответственно, 0, 1, 4, 9, и 16. Однако, все они возвращают 16:

print(squares[2]())
print(squares[4]())

# Это случается, поскольку x не является локальной для lambda, а определена во внешней области видимости, и получается тогда, когда она вызывается - а не когда определяется.

# В конце цикла, x=4, поэтому все функции возвращают 4**2, то есть 16. Это можно также проверить, изменив значение x и посмотрев на результат:

x = 8
print(squares[2]())

# Чтобы избежать подобного, необходимо сохранять значения переменных локально:

squares = []
for x in range(5):
   squares.append(lambda n=x: n**2)
# Здесь, n=x создаёт локальную для функции переменную n и вычисляется в момент определения функции:

print(squares[2]())
print(squares[4]())

# Это применимо не только к анонимным, а также и к обычным функциям.