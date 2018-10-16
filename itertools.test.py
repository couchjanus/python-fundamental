# -*- coding: utf-8 -*-
# itertools.test.py

from itertools import permutations
from itertools import combinations
from itertools import chain

# permutations позволяет генерировать 
# все возможные способы упорядочения набора

for p in permutations([1,2,3]):
    print(p)	

# combinations создает все возможные способы 
# выбора предметов из коллекции, 
# в отличии от permutations порядок не имеет значения:

for c in combinations([1, 2, 3, 4], 2):
    print(c)

# itertools содержит вспомогательные функции, 
# такие как chain, которая принимает итерируемую 
# и создает новый итератор, 
# который возвращает элементы из данных поочередно, 
# в виде одной последовательности:

for c in chain(range(3), range(12, 15)):
    print(c)
