"""
File: turtlepoly.py

Copyright (c) 2016 Francis Agustin

License: MIT

Program that asks the user for two natural numbers `n`
and `side_len` and produces a regular `n` sided polygon
with each side of length `side_len`.
"""

import turtle

num_sides_inp = raw_input("Enter a number of sides: ")
num_sides = int(num_sides_inp)
side_len_inp = raw_input("Enter length of sides: ")
side_len = int(side_len_inp)

t = turtle.Pen()

for side in range(num_sides):
    t.forward(side_len)
    t.left(360/num_sides)

stopper = raw_input("Hit <enter> to quit.")

turtle.bye()
