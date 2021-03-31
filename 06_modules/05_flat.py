# Stwórz moduł obliczający pola różnych figur.
# W nowym pliku utwórz skrypt, który na podstawie podanych składowych kształtów pomieszczeń
# oraz ich wymiarów zwraca powierzchnię budynku.

import shapes


def calculate_room_field(room):
    if room[0] == 'rectangle':
        wall1 = room[1]
        wall2 = room[2]
        return shapes.rectangle(wall1, wall2)

    if room[0] == 'triangle':
        wall = room[1]
        height = room[2]
        return shapes.triangle(wall, height)

    if room[0] == 'trapezoid':
        wall1 = room[1]
        wall2 = room[2]
        height = room[3]
        return shapes.trapezoid(wall1, wall2, height)


if __name__ == '__main__':
    flat = [
        ('rectangle', 4, 3.2),
        ('trapezoid', 4, 3, 3),
        ('rectangle', 3, 3),
        ('triangle', 3, 4)
    ]

    sum_field = 0
    for r in flat:
        sum_field += calculate_room_field(r)

    print(f'Flat field = {sum_field}')
