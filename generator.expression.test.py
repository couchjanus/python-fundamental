# -*- coding: utf-8 -*-
# generator.expression.test.py

from __future__ import print_function

# Пример generator.expression:

generator = (x*x for x in xrange(3))

for i in generator:

   print(i)