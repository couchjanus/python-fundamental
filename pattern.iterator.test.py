# -*- coding: utf-8 -*-
# pattern.iterator.test.py

from __future__ import print_function

# Шаблон проектирования “Итератор”

import re

# напишем итерируемый объект, который создает и возвращает итератор 
# при обращении к методу __iter__:

class Finder:

    def __init__(self, pattern, text):
        self.text = text
        self.matches = re.findall(pattern, text)

    def __iter__(self):
        return FinderIterator(self.matches)


class FinderIterator:

    def __init__(self, matches):
        self.matches = matches
        self.index = 0

    def __next__(self):
        try:
            match = self.matches[self.index]
        except IndexError:
            raise StopIteration()
        self.index = self.index + 1
        return match
# Используем Finder через цикл for:

finder = Finder(r'\w+', 'extract; the! words, from @me')

for match in finder:
    print(match)
