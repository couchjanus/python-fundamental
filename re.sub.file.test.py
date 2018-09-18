# -*- coding: utf-8 -*-
# re.sub.file.test.py

import re

result = re.sub(r'Ukraine', 'the World', 'QALight is largest IT community of Ukraine')
print(result)

s = '100 NORTH MAIN ROAD'
print(s)
print(s.replace('ROAD', 'RD.'))

s = '100 NORTH BROAD ROAD'
print(s)

print(s.replace('ROAD', 'RD.'))

print(s[:-4] + s[-4:].replace('ROAD', 'RD.'))

print(re.sub('ROAD$', 'RD.', s))

print(re.sub(r'\d\d\.\d\d\.\d{4}', r'DD.MM.YYYY', r'Эта строка написана 19.01.2018, а могла бы и 01.09.2019')) 


p = re.compile( '(blue|white|red)')

print(p.sub('colour', 'blue socks and red shoes'))

print(p.sub('colour', 'blue socks and red shoes', count=1))


# Метод subn() делает то же самое, но возвращает кортеж, содержащий новую строку и число произведенных замен:

p = re.compile( '(blue|white|red)')
print(p.subn( 'colour', 'blue socks and red shoes'))

print(p.subn( 'colour', 'no colours at all'))

