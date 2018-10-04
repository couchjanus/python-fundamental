# -*- coding: utf-8 -*-
# packs/bar/main.py

from ..foo.echo.main import as_int

# Exported function
def add(a, b):
    return as_int(a) + as_int(b)

# Test function for module  
def _test():
    assert add('1', '1') == 2

if __name__ == '__main__':
    _test()
