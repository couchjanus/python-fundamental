# -*- coding: utf-8 -*-
# re.group.test.py

import re

string = u"Eli: Josh go move your laundry" # Our string

# Здесь одна или более букв, следующих за «:», 0 или более символов, „Josh“ и снова 0 или более символов.
#  /.*word.*/ — простой способ задать строку, содержащую „word“, причем другие символы в ней могут присутствовать, а могут и нет.

p = re.compile(r'(\w+): .*Josh.*') # Our regex

matches = re.match(p, string) # Test the string

who = matches.group()

print(who) # "Eli"

p = re.compile(r'(\w+): .*Josh.*') # Our regex

matches = re.match(p, string) # Test the string

who = matches.group(1) # Get who said the message

print(who) # "Eli"
