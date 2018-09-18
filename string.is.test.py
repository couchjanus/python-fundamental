# -*- coding: utf-8 -*-
# string.is.test.py

# string.isalnum() – возвращает True, если строка – буквенно-цифровая, и в ней есть хотя бы один символ:

string = 'Alpha12345'
string.isalnum()

string = '12345'

string.isalnum()

string = ''
string.isalnum()

# string.isalpha() – возвращает True, если строка состоит только из букв:

string = 'Alpha'
string.isalpha()

string = '12345'

string.isalpha()

# string.isdigit() – то же, но наоборот:

string = '12345'
string.isdigit()

string = 'Alpha'

string.isdigit()

# string.islower() – возвращает True, если все символы – строчные:

string = 'Alpha'

string.islower()

string = 'alpha'
string.islower()

# string.isspace() – возвращает True, если все символы – пробелы:

string = '  '

string.isspace()

string = ' a '

string.isspace()

# string.istitle() – возвращает True, если все элементы начинаются с ЗАГЛАВНОЙ буквы:

string = 'This Is Titled String'

string.istitle()

string = 'this is titled string'

string.istitle()

string = 'This is titled string'

string.istitle()

# string.isupper() – возвращает True, если все буквы ЗАГЛАВНЫЕ:
string = 'UPPER STRING'

string.isupper()

string = 'lower string'

string.isupper()
