# -*- coding: utf-8 -*-
# finder.yield.test.py

from __future__ import print_function

# Шаблон проектирования “Итератор”

import re

# класс Finder используем генераторную функцию:

class Finder:

    def __init__(self, pattern, text):
        self.text = text
        self.matches = re.findall(pattern, text)

    def __iter__(self):
        for match in self.matches:
            yield match

finder = Finder(r'\w+', 'extract; the! words, from @me')

it = iter(finder)

while True:
    item = next(it, None)
    if item is None:
        break
    print(item)
