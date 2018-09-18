# -*- coding: utf-8 -*-
# re.findall.test.py

import re

# Два метода возвращают все совпадения для шаблона. 

result = re.findall(r'AV', 'AV Analytics Vidhya AV')
print(result)


# findall() возвращает список совпавших подстрок:
p = re.compile(r'\d+')

res = p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')

print(res)
# Метод findall() должен создать полный список, прежде чем он может быть возвращен в качестве результата. 

print(re.findall(r'\d\d\.\d\d\.\d{4}', r'Эта строка написана 19.01.2018, а могла бы и 01.09.2019')) 
