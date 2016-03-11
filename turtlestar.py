"""
File: turtlestar.py

Copyright (c) 2016 Francis Agustin

License: MIT

Program that asks the user for an odd natural number `n`
(needs to be at least 5) and a natural number `side_len`
and produces an `n`-pointed star with `side_len` length
between points.
"""

import turtle

bob = turtle.Pen()

sides = int(input("Enter an odd natural number greater than 5: "))
side_len = int(input("Enter a natural number: "))

for i in range(sides):
        bob.forward(side_len)
        bob.left(180 - 180.0/sides)
        bob.forward(side_len)


inp = raw_input ("Hit <enter> to quit")

turtle.bye()
