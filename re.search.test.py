# -*- coding: utf-8 -*-
# re.search.test.py

import re

p = re.compile('[a-z]+')

print(p.match('::: message'))

m = p.search('::: message')
print(m)

print(m.group())
print(m.span())

m = p.match('string goes here')

if m:
    print('Match found: ')
    print(m.group())
else:
    print('No match')


result = re.search(r'Analytics', 'AV Analytics Vidhya AV')
print(result.group(0))


match = re.search(r'\d\d\D\d\d', r'Телефон 123-12-12') 

if match:
    print(match.group())
else:
    print('Not found')

match = re.search(r'\d\d\D\d\d', r'Телефон 1231212') 

print(match[0] if match else 'Not found') 


email_address = 'Please contact us at: support@datacamp.com'
match = re.search(r'([\w\.-]+)@([\w\.-]+)', email_address)
if match:
  print(match.group()) # The whole matched text
  print(match.group(1)) # The username (group 1)
  print(match.group(2)) # The host (group 2)

