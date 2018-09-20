# -*- coding: utf-8 -*-
# function.lambda.test.py

# Выражение lambda

# Без выражения lambda:
def func(x, y, z): return x + y + z
func(2, 3, 4)

# С выражением lambda:
f = lambda x, y, z: x + y + z
f(2, 3, 4)

# Использование значений по умолчанию в lambda-выражениях:

x = (lambda a='fee', b='fie', c='foe': a + b + c)

print(x('wee'))

# Анонимные функции могут содержать лишь одно выражение, но и выполняются они быстрее.

funca = lambda x, y: x + y
print(funca(1, 2))

print(funca('a', 'b'))

print((lambda x, y: x + y)(1, 2))

print((lambda x, y: x + y)('a', 'b'))

# lambda функции, в отличие от обычной, не требуется инструкция return, а в остальном, ведет себя точно так же:

funcr = lambda *args: args
print(funcr(1, 2, 3, 4))
