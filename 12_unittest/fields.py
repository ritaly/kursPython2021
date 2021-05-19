def rectangle(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError('Bok musi być wartością liczbową')

    return a * b


def triangle(a, h):
    return 0.5 * a * h


def trapezoid(a, b, h):
    return 0.5 * (a + b) * h

