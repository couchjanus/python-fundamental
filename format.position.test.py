# -*- coding: utf-8 -*-
# format.position.test.py

def menu():
    print("Select operation.")
    print("+.Add")
    print("-.Subtract")
    print("*.Multiply")
    print("/.Divide")
    return str(input("Enter choice(+|-|*|/):"))

def calcHelp():
    print( """\
        Usage operation:
            'h'                        Display this usage message
            '+'                        Add
            '-'                        Subtract
            '*'                        Multiply
            '/'                        Divide
            'q'                        Quit
        """)

# define functions
def add(x, y):
    """This function adds two numbers"""
    return x + y

def subtract(x, y):
    """This function subtracts two numbers"""
    return x - y

def multiply(x, y):
    """This function multiplies two numbers"""
    return x * y

def divide(x, y):
    """This function divides two numbers"""
    return float(x / y)

def intdivide(x, y):
    """This function int divides two numbers"""
    return x // y

def modulo(x,y):
    """This function modulos two numbers"""
    return x % y

print('Super Calc')
running = True

while running:
    operator = menu()

    if operator == 'q':
        print('{!r:~^40}'.format('Thankyou for using calculator.py!'))
        print('{!s:#^40}'.format('Thankyou for using calculator.py!'))
        break
    elif operator not in ('+','-','*','/','//','%','**'):
        calcHelp()
        continue
    elif operator == "-":
        print ("{:+08.2f} - {:+08.2f} = {:+08.2f}".format(x, y, subtract(x, y)))
    elif operator == "*":
        print ("{0} * {k} = {1}".format(x, multiply(x, y), k=y))

print("{0}, {1}, {0}".format("hello", "kitty"))

print("{0}, {who}, {0}".format("hello", who="kitty"))



point = 0, 10
print("x = {0[0]}, y = {0[1]}".format(point))

point = {"x": 0, "y": 10}
print("x = {0[x]}, y = {0[y]}".format(point))

print("{{{0}}} {1} ;-}}".format("I'm in braces", "I'm not"))

record ="{0}{1}".format("The amount due is $", 200)
print(record)


х = "three"
s ="{0} {1} {2}"
s = s.format("The", x, "tops")
print(s)