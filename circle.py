import math


def area(r):
    if r <= 0:
        raise ValueError("The number is negative")
    return math.pi * r * r


def perimeter(r):
    if r <= 0:
        raise ValueError("The number is negative")
    return 2 * math.pi * r

