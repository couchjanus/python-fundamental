# -*- coding: utf-8 -*-
# packs.test.py

# import packs
# import packs.foo

# import packs.foo.echo
# import packs.foo.surround
# from packs.foo import *

# импортирует три именованных подмодуля из пакета packs.

# print(dir(packs)) # 

# from packs.foo import *

# print(dir(packs.foo))


from packs.bar.main import add

def main():
    print(add('1', '1'))

if __name__ == '__main__':
    main()