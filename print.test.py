# -*- coding: utf-8 -*-
# print.test.py

print(5 + 10)
print(3 * 7, (17 - 2) * 8)
print(2 ** 16)  # две звёздочки означают возведение в степень
print(37 / 3)   # один слэш — это деление с ответом-дробью
print(37 // 3)  # два слэша считают частное от деления нацело
                # это как операция div в других языках
print(37 % 3)   # процент считает остаток от деления нацело
                # это как операция mod в других языках


# Оператор print был заменён функцией print(),
# с именованными аргументами для замены 
# большей части синтаксиса старого оператора print.


# Python2: 
print "The answer is", 2*2
# Python3: 
print("The answer is", 2*2)
# Python2: 
print x,    # Запятая в конце подавляет перевод строки
# Python3: 
print(x, end=" ")  # Добавляет пробел вместо перевода строки
# Python2: 
print              # Печатает перевод строки
# Python3: 
print()            # Нужно вызвать функцию!
# Python2: 
print >>sys.stderr, "fatal error"
# Python3: 
print("fatal error", file=sys.stderr)
# Python2: 
print (x, y)       # Печатает repr((x, y))
# Python3: 
print((x, y))      # Не путать с print(x, y)!
# Также вы можете настроить разделитель между элементами, например:
print("There are <", 2**32, "> possibilities!", sep="")
