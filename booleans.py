"""
File: booleans.py

Copyright (c) 2016 Francis Agustin

License: MIT

Exercise 2.17, evaluate Boolean expressions.
"""

C = 41

C == 40 # False     c equals 40
C != 40 and C < 41 # False      c does not equal 40. C is less than 41
C != 40 or C < 41 #True     c does not equal 40
not C == 40 # True       c does not equal 40, but 'not' makes it true
not C > 40 # False      c is greater than 40, but 'not' makes it false
C <= 41 # c is less than or equal to 41
not False # True        'not' makes false true
True and False  # False     cannot be both true and false
False or True # True        can be false and not true, and vice versa
False or False or False # False     false is false, it can't be or
True and True and False # False     something true and true cannot also be false
False == 0  # True      numerical value of false is 0
True == 0 # False       numerical value of false is 0
True == 1 # True        numerical value of false is 0
