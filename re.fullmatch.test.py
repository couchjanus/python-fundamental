# -*- coding: utf-8 -*-
# re.fullmatch.test.py

import re

# Проверить, подходит ли строка string под шаблон pattern;

match = re.fullmatch(r'\d\d\D\d\d', r'12-12')
print('YES' if match else 'NO')

match = re.fullmatch(r'\d\d\D\d\d', r'Т. 12-12')
print('YES' if match else 'NO')
