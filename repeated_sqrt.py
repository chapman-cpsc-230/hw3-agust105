"""
File: repeated_sqrt.py

Copyright (c) 2016 Francis Agustin

License: MIT

Exercise 2.18, Investigate and fix square root loop.
"""

from math import sqrt
for n in range(1,60):
    r = 2.0
    for i in range(n):
        r = sqrt(r)
    for i in range(n):
        r = r**2
    print '%d times sqrt and **2: %.16f' % (n, r)

# Takes numbers 1 to 60
# Sets value equal to 2.0
# Takes square root
# Squares the square root
# repeats loop 59 more times

# Round off error occurs as the value becomes 1 instead of 2

from math import sqrt
for n in range(1,25):
    r = 2.0
    for i in range(n):
        r = sqrt(r)
    for i in range(n):
        r = r**2
    print '%d times sqrt and **2: %.16f' % (n, r)

# No round off error if
