# -*- coding: utf-8 -*-
# string.encode.test.py

# string.encode(кодировка) – сменить кодировку символов на кодировка (по-умолчанию – ASCII), не работает в Python 2.6 и более ранних версиях (вызывает исключение TypeError: encode() takes no keyword arguments):

string = 'This Is Some string'

print(string.encode(encoding='base64'))

# string.decode(кодировка) – то же, но наоборот:

string = 'VGhpcyBJcyBTb21lIHN0cmluZw=='
print(string.decode(encoding='base64'))
