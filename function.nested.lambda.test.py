# -*- coding: utf-8 -*-
# function.nested.lambda.test.py

# Вложенные lambda-выражения и области видимости:
# Соблюдается правило LEGB. 
# Например, lambda-выражение находится внутри инструкции def – типичный случай – и потому получает значение имени x из области видимости объемлющей функции, имевшееся на момент ее вызова:

def action(x):
    return (lambda y: x + y) # Создать и вернуть ф-цию, 
                             # запомнить x
act = action(99)

print(act)
# <function <lambda> at 0x00A16A88>
print(act(2)) # Вызвать функцию, созданную ф-цией action


# Предыдущая инструкция def в виде lambda-выражения:
action = (lambda x: (lambda y: x + y))
act = action(99)
print(act(3))

print(((lambda x: (lambda y: x + y))(99))(4))

# Эта структура lambda-выражений создает функцию, которая при вызове создает другую функцию. В обоих случаях вложенное lambda-выражение имеет доступ к переменной x в объемлющем lambda-выражении.

