# -*- coding: utf-8 -*-
# string.constants.test.py

import string

# String constants
# The constants defined in this module are:



# The concatenation of the ascii_lowercase and ascii_uppercase constants described below. This value is not locale-dependent.
print(string.ascii_letters)

# The lowercase letters 'abcdefghijklmnopqrstuvwxyz'. This value is not locale-dependent and will not change.
print(string.ascii_lowercase)

# The uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. This value is not locale-dependent and will not change.
print(string.ascii_uppercase)

# The string '0123456789'.
print(string.digits)


# The string '0123456789abcdefABCDEF'.
print(string.hexdigits)


# The string '01234567'.
print(string.octdigits)


# String of ASCII characters which are considered punctuation characters in the C locale.
print(string.punctuation)

# String of ASCII characters which are considered printable. This is a combination of digits, ascii_letters, punctuation, and whitespace.
print(string.printable)

# A string containing all ASCII characters that are considered whitespace. This includes the characters space, tab, linefeed, return, formfeed, and vertical tab.
print(string.whitespace)
