# -*- coding: utf-8 -*-
# function.rec.area.test.py

# На данном этапе мы еще не указываем имена переменных

def rectangle_area_finder():
    """
    >>> rectangle_area_finder(3, 5)
    >>> rectangle_area_finder(17.2, 6)
    """

# Указать типы данных, которые принимает функция и тип данных, который она возвращает

# функция принимает два числа, а возвращает одно

def rectangle_area_finder():
    """
    (num, num) -> num    
 
    >>> rectangle_area_finder(3, 5)
    15
    >>> rectangle_area_finder(17.2, 6)
    103.2
    """
# Подобрать подходящие названия для переменных

# Поскольку это математическая функция нам вполне подойдут имена a и b
def rectangle_area_finder(a, b):
    """
    (num, num) -> num
    >>> rectangle_area_finder(3, 5)
    >>> rectangle_area_finder(17.2, 6)
    """
# Написать краткое, но содержательное описание функции

def rectangle_area_finder(a, b):
    """
    (num, num) -> num
    Returns an area of a rectangle with given sides a and b.    
    >>> rectangle_area_finder(3, 5)
    >>> rectangle_area_finder(17.2, 6)
    """
# Написать собственно тело функции

def rectangle_area_finder(a, b):
    """
    (num, num) -> num
    Returns an area of a rectangle with given sides a and b.    
    >>> rectangle_area_finder(3, 5)
    >>> rectangle_area_finder(17.2, 6)
    """
    return a * b
# Функция готова! Осталось вызвать ее с указанными аргументами


# 
print()
def hello():
    print('Hello!')

def area(width, height):
    return width * height

def print_welcome(name):
    print('Welcome,', name)

name = input('Your Name: ')
hello()
print_welcome(name)
print
print('To find the area of a rectangle,')
print('enter the width and height below.')
print

w = input('Width: ')
while w <= 0:
    print('Must be a positive number')
    w = input('Width: ')

h = input('Height: ')
while h <= 0:
    print('Must be a positive number')
    h = input('Height: ')

print('Width =', w, 'Height =', h, 'so Area =', area(w, h))

# converts temperature to fahrenheit or celsius

def print_options():
    print("Options:")
    print(" 'p' print options")
    print(" 'c' convert from celsius")
    print(" 'f' convert from fahrenheit")
    print(" 'q' quit the program")

def celsius_to_fahrenheit(c_temp):
    return 9.0 / 5.0 * c_temp + 32

def fahrenheit_to_celsius(f_temp):
    return (f_temp - 32.0) * 5.0 / 9.0

choice = "p"
while choice != "q":
    if choice == "c":
        temp = input("Celsius temperature: ")
        print("Fahrenheit:", celsius_to_fahrenheit(temp))
    elif choice == "f":
        temp = input("Fahrenheit temperature: ")
        print("Celsius:", fahrenheit_to_celsius(temp))
    elif choice == "p":
        print_options()
    choice = input("option: ")
