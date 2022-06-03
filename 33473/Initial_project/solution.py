from math import pi


def square(a):
    return a * a


def circle(r):
    return pi * r * r


def rectangle(a, b):
    return a * b


def triangle(a, b):
    return (1 / 2) * a * b


def get_func(ls):
    return [globals()[l] for l in ls]
