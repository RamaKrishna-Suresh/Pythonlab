# code to draw an arc

# import turtle package
from turtle import *


def arc(t, length, r, angle_user):
    """Function that takes turtle object and other parameters
    as arguments and draws an arc"""

    n = int((2 * 3.14 * r) / length)

    angle = angle_user / n

    for x in range(0, n):
        t.fd(length)
        t.rt(angle)


# input parameters
length_input = 1
radius_input = float(input('enter radius '))
angle_input = float(input('enter angle  '))

# Creating turtle object and setting delay
bob = Turtle()
bob.delay = 0.01

# Invoking arc function
arc(bob, length_input, radius_input, angle_input)

# wait for user
mainloop()
