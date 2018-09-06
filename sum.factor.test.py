# -*- coding: utf-8 -*-
# sun.factor.test.py

n = int(input())
f = 1
sum = 0
for i in range(1, n + 1):
    f = f * i
    sum += f
print (sum)