def validate_values(*values):
    for arg in values:
        if not isinstance(arg, (int, float)):
            raise ValueError(f'Bok musi być wartością liczbową, a jest {arg} ')


def rectangle(a, b):
    validate_values(a, b)

    return a * b


def triangle(a, h):
    validate_values(a, h)
    return 0.5 * a * h


def trapezoid(a, b, h):
    validate_values(a, b, h)

    return 0.5 * (a + b) * h

