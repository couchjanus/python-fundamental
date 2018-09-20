# -*- coding: utf-8 -*-
# function.local.scope.test.py

a = 4
 
def print_func():
    a = 17
    print("in print_func a = ", a)

print_func()

print("a = ", a, "which is global variable assigned prior to the function print_func")

# Если попробовать вывести значения переменных, то обнаружится, что некоторые из них почему-то не существуют:

def mathem(a,b):
    a = a/2
    b = b+10
    print(a+b)
 
num1 = 100
num2 = 12

mathem(num1,num2)

# Переменные num1 и num2 не изменили своих первоначальных значений. 
# в функцию передаются копии значений. 
# Прежние значения из основной ветки программы остались по прежнему связанны с их переменными.

print(num1)
print(num2)

# переменных a и b нет (ошибка "name 'b' is not defined" переводится как "переменная b не определена"). 
# Эти переменные существуют лишь в момент выполнения функции и называются локальными. 

print(a)
# print(b)

# переменные num1 и num2 видны не только во внешней ветке, но и внутри функции:

def mathem2():
   print(num1+num2)
 
mathem2()
