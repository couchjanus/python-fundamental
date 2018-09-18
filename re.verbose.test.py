# -*- coding: utf-8 -*-
# re.verbose.test.py

import re
# Без verbose:

charref = re.compile("&#(0[0-7]+"
                     "|[0-9]+"
                     "|x[0-9a-fA-F]+);")


# Пример того, как РВ становится существенно проще читать:

charref = re.compile(r"""
  &[#]           # Start of a numeric entity reference
 (
     0[0-7]+         # Octal form
   | [0-9]+          # Decimal form
   | x[0-9a-fA-F]+   # Hexadecimal form
 )
 ;                   # Trailing semicolon
""", re.VERBOSE)

ref = '12345'

matches = re.match(charref, ref) 

print(matches)


# Форматирование будет более аккуратным при использовании тройных кавычек:

pat = re.compile(r"""
 \s*                 # Skip leading whitespace
 (?P<header>[^:]+)   # Header name
 \s* :               # Whitespace, and a colon
 (?P<value>.*?)      # The header's value -- *? used to
                     # lose the following trailing whitespace
 \s*$                # Trailing whitespace to end-of-line
""", re.VERBOSE)


# Это гораздо проще читается, чем:

pat = re.compile(r"\s*(?P<header>[^:]+)\s*:(?P<value>.*?)\s*$")


s = "textl, text2, textЗ text4"
p = re.compile(r'\w+(?=[,])', re.S | re.I) # все слова, после которых есть запятая
print(p.findall(s))

р = re.compile(r"[a-z]+[0-9] (?![,])", re.S | re.I) # все слова, после которых нет запятой
print(p.findall(s))

р = re.compile(r"(?<=[,][ ])[a-z]+[0-9]", re.S | re.I) # все слова, перед которыми есть запятая с пробелм
print(p.findall(s))
