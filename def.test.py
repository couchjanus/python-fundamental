# -*- coding: utf-8 -*-
# def.test.py

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

print('Super Calc')
running = True

while running:
    operator = menu()

    if operator == 'q':
        print('Thankyou for using calculator.py!')
        break
    elif operator not in ('+','-','*','/','//','%','**'):
        calcHelp()
        continue
