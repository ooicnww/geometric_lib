import math


def area(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("The sides are negative")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The triangle cannot exist")
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


def perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("The sides are negative")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The triangle cannot exist")
    return a + b + c
