# -*- coding: utf-8 -*-
# elif.test.py

operator = str(input('operatop= '))

if operator == "+":
    print('operator +')
elif operator == "-":
    print('operator -')
elif operator == "*":
    print('operator *')
elif (operator == "/" or operator == "//" or operator == "%" ) and y==0:
    print('integer division or modulo by zero')
elif operator == "/" and y !=0:
    print('operator /')
elif operator == "//" and y !=0:
    print('operator //')
elif operator == "%" and y !=0:
    print('operator %')
else: 
    print('Other')

