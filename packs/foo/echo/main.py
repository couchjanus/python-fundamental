# -*- coding: utf-8 -*-
# packs/foo/echo/main.py

# Exported function
def as_int(a):
    return int(a)

# Test function for module  
def _test():
    assert as_int('1') == 1

if __name__ == '__main__':
    _test()
