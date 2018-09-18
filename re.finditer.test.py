# -*- coding: utf-8 -*-
# re.finditer.test.py

import re
# Два метода возвращают все совпадения для шаблона. 
# findall() возвращает список совпавших подстрок:
p = re.compile('\d+')

# Метод finditer() возвращает последовательность экземпляров MatchObject в качестве итератора.

iterator = p.finditer('12 drummers drumming, 10 pipers piping, 10 lords a-leaping')

print(iterator)

for match in iterator:
    print(match.span())


for m in re.finditer(r'\d\d\.\d\d\.\d{4}', r'Эта строка написана 19.01.2018, а могла бы и 01.09.2019'):
    print('Дата', m[0], 'начинается с позиции', m.start()) 
