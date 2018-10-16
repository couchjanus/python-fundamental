# -*- coding: utf-8 -*-
# list.iterator.test.py

from __future__ import print_function

# итерируемый объект на основе списка и его итератор:

class ListIterator():
    def __init__(self, collection, cursor):
        """
        :param collection: список
        :param cursor: индекс с которого начнется перебор коллекции.
        так же должна быть проверка -1 >= cursor < len(collection)
        """
        self._collection = collection
        self._cursor = cursor

    def __next__(self):
        if self._cursor + 1 >= len(self._collection):
            raise StopIteration()
        self._cursor += 1
        return self._collection[self._cursor]

class ListCollection():
    def __init__(self, collection):
        self._collection = collection

    def __iter__(self):
        return ListIterator(self._collection, -1)


collection = [1, 2, 5, 6, 8]
aggregate = ListCollection(collection)

for item in aggregate:
    print(item)

print("*" * 50)

itr = iter(aggregate)
while True:
    try:
        print(next(itr))
    except StopIteration:
        break
