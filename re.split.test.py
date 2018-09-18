# -*- coding: utf-8 -*-
# re.split.test.py

import re

p = re.compile(r'\W+')

print(p.split('This is a test, short and sweet, of split().'))

print(p.split('This is a test, short and sweet, of split().', 3))


print(re.split(r'\W+', 'Где, скажите мне, мои gluki??!')) 


# Если в РВ есть захватывающие скобки, то и эти значения также возвращаются, как часть списка:

p = re.compile(r'\W+')
p2 = re.compile(r'(\W+)')

print(p.split('This... is a test.'))

print(p2.split('This... is a test.'))

# Функция модуля re.split() в качестве первого аргумента берет РВ, а в остальном ведет себя также:

print(re.split('[\W]+', 'Words, words, words.'))

print(re.split('([\W]+)', 'Words, words, words.'))

print(re.split('[\W]+', 'Words, words, words.', 1))

