# -*- coding: utf-8 -*-
# continue.test.py
# ---------- CALCULATOR ----------
'''
    To run under Python replace 'input' call
    with 'raw_input'
    Store the user input an operator
'''

print('Super Calc')

running = True

while running:
    # Convert strings into integers
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))

    # Store the user input an operator
    operator = input('Enter Operator: ')

    if operator == 'q':
        print('Programm done.')
        running = False # это останавливает цикл while
        break
    
    elif operator not in ('+','-','*','/','//','%','**'):
        print ("Help: Use either + - * / or % next time")
        continue
    
    elif operator == "+":
        print("{} + {} = {}".format(x, y, x * y))

    # If the 1st condition wasn't true check if this one is
    elif operator == "-":
        print("{} - {} = {}".format(x, y, x - y))
    elif operator == "*":
        print("{} * {} = {}".format(x, y, x * y))
    elif (operator == "/" or operator == "//" or operator == "%" ) and y==0:
        print('integer division or modulo by zero')
    elif operator == "/" and y !=0:
        print("{} / {} = {}".format(x, y, x / y))
    elif operator == "//" and y !=0:
        print("{} // {} = {}".format(x, y, x // y))
    elif operator == "%" and y !=0:
        print("{} % {} = {}".format(x, y, x % y))
    # If none of the above conditions were true then execute this by default
    else:
        print("Use either + - * / or % next time")
