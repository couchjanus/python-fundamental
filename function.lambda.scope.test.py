# -*- coding: utf-8 -*-
# function.lambda.scope.test.py

# Выражение lambda
# lambda-выражения создают локальную область видимости, как и вложенные инструкции def, и ав томатически получают доступ к именам в объемлющих функциях, в модуле и во встроенной области видимости (в соответствии с правилом LEGB).

def knights():
    title = 'Sir'
    action = (lambda x: title + ' ' + x) # Заголовок в объемлющей def
    return action                        # Возвращает функцию

act = knights()

act('robin')

token = 'global'

def access_local():
    token = 'local'
    if 'token' in locals() and 'token' in globals():
        print('Yes, token is in local and global scope')
    print('Valie of token used is = ('+token+')\n')

def access_global():
    if 'token' in globals():
        print('Yes, token is in global scope')
    print('Valie of token used is = ('+token+')\n')

def access_enclosed():
    token = 1
    for test in range(5):
        token = 'enclosed'
        pass
    if 'token' in globals():
        print('Though token is in global scope')
    print('Valie of token used is = ('+token+')\n')

def id(token):
    return 1

access_local()
access_enclosed()
access_global()

print("%s = %d\n" % ("token length", id(token)))
print(token)
