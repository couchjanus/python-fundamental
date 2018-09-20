# -*- coding: utf-8 -*-
# function.global.scope.test.py

# глобальная переменная age
age = 44
 
def info():
    print(age) # Печатаем глобальную переменную age
 
def local_info():
    age = 22 # создаем локальную переменную age 
    print(age)
 
info() # напечатает 44
local_info() # напечатает 22

# слово global
# Глобальные переменные доступны отовсюду:

def simple():
    global b
    b='Дафтер'

# глобальная переменная age
age = 13
 
# функция изменяющая глобальную переменную
def get_older():
    global age
    age += 1
 
print(age) # напечатает 13
get_older() # увеличиваем age на 1
print(age) # напечатает 14


# Этот код:

x = 10
def bar():
   print(x)
bar()

# работает

# foo() исключение UnboundLocalError
# но следующий код:

x = 10
def foo():
    print(x)
    x += 1
# приводит к UnboundLocalError:
# foo()
# Traceback (most recent call last):
#   ...
# UnboundLocalError: local variable 'x' referenced before assignment
# Это происходит потому, что, когда вы делаете присваивание переменной в области видимости, она становится локальной в этой области и скрывает другие переменные с таким же именем во внешних областях.

x = 10
def foobar():
    global x
    print(x)
    x += 1
foobar()

# Это явное объявление требуется для того, чтобы напомнить вам, что (в отличие от внешне аналогичной ситуации с переменными класса и экземпляра), вы на самом деле, изменяете значение переменной во внешней области видимости:

print(x)

# nonlocal - python3
# Вы можете сделать подобную вещь во вложенной области видимости использованием ключевого слова nonlocal:

def fool():
   x = 10
   def bar():
       nonlocal x
       print(x)
       x += 1
   bar()
   print(x)
fool()

# Complex example
a_var = 10
b_var = 15
c_var = 25

def a_func(a_var):
    print("in a_func a_var = ", a_var)
    b_var = 100 + a_var
    d_var = 2 * a_var
    print("in a_func b_var = ", b_var)
    print("in a_func d_var = ", d_var)
    print("in a_func c_var = ", c_var)
    return b_var + 10

c_var = a_func(b_var)

print("a_var = ", a_var)
print("b_var = ", b_var)
print("c_var = ", c_var)
# print("d_var = ", d_var)
