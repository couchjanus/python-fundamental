# -*- coding: utf-8 -*-
# finder.generator.expression.test.py

from __future__ import print_function

# Шаблон проектирования “Итератор”

import re

# Заменим класс Finder на функцию:

def find(pattern, text):
    return (match.group() for match in re.finditer(pattern, text))

finder = find(r'\w+', 'extract; the! words, from @me')

it = iter(finder)

while True:
    item = next(it, None)
    if item is None:
        break
    print(item)
