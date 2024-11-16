
def area(a):
    if a <= 0:
        raise ValueError("The side is negative")
    return a * a


def perimeter(a):
    if a <= 0:
        raise ValueError("The side is negative")
    return 4 * a
