# -*- coding: utf-8 -*-
# finder.generator.expression.test.py

from __future__ import print_function

# Шаблон проектирования “Итератор”

import re

# класс Finder используем генераторную функцию:

class Finder:
    
    def __init__(self, pattern, text):
        self.pattern = pattern
        self.text = text

    def __iter__(self):
        return (match.group()
                for match in re.finditer(self.pattern, self.text))

finder = Finder(r'\w+', 'extract; the! words, from @me')

it = iter(finder)

while True:
    item = next(it, None)
    if item is None:
        break
    print(item)
