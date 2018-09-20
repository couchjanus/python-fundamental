# -*- coding: utf-8 -*-
# function.pure.test.py

# Детерминированная и чистая:

def Add(val1, val2):
    return val1 + val2

# Детерминированная, но не чистая:

def Add(val1, val2):
	print(val1 + " " + val2)
	return val1 + val2;
