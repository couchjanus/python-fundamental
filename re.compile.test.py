# -*- coding: utf-8 -*-
# re.compile.test.py

import re

pattern = re.compile('QALight')
result = pattern.findall('QALight IT community')
print(result)
result2 = pattern.findall('QALight is largest QALight community of Ukraine')
print(result2)


p = re.compile('Te')
print(p)

p = re.compile('Te', re.IGNORECASE)
print(p)

p = re.compile('[a-z]+')
print(p)
