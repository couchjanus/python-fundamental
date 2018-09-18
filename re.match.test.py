# -*- coding: utf-8 -*-
# re.match.test.py

import re

p = re.compile('Te', re.IGNORECASE)
print(p)
m = p.match('test')
print(m.group())
print(m.group(0))


p = re.compile('[a-z]+')
print(p)

print(p.match(""))

print(p.match("abrahabra"))

print(p.match("abrahabra").group())
print(p.match("abrahabra").group(0))

m = p.match("abrahabra")
print(m.start())
print(m.end())
print(m.span())



