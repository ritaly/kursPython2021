def circle(r):
    circle_field = 3.14 * r**2
    return circle_field


def rectangle(a, b):

    rectangle_field = a * b
    return rectangle_field


def triangle(a, h):
    triangle_field = 0.5 * a * h
    return triangle_field

def trapezoid(a, b, h):
    trapezoid_field = 0.5 * (a + b) * h
    return trapezoid_field

if __name__ == '__main__':
    print(circle(5))
    print(triangle(12, 4))

