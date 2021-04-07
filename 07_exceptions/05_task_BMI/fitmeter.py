import bmi


def get_weight():
    while True:
        try:
            weight = float(input('Podaj wage w kg: '))
        except (ValueError, TypeError):
            print('To nie jest prawidłowa wartość! Spróbuj jeszcze raz')
            continue

        if weight > 30:
            break
        else:
            print('Twoja waga nieprawdopodobnie niska. Podaj wagę jeszcze raz')

    return weight


def get_height():
    while True:
        try:
            height = float(input('Podaj wzrost w metrach: '))
        except (ValueError, TypeError):
            print('To nie jest prawidłowa wartość! Spróbuj jeszcze raz')
            continue

        if 1.5 < height < 2.35:
            break
        else:
            print('Twoj wzorst jest nieprawdopodobmy. Podaj wartość jeszcze raz')

    return height


def open_advice(filename):
    filename = filename + ".txt"
    try:
        with open(filename) as file:
            advice = file.read()
    except FileNotFoundError:
        advice = 'Nie znaleziono pliku'

    return advice


if __name__ == "__main__":
    m = get_weight()
    h = get_height()
    result = bmi.calculate_BMI(m, h)
    print(result)
    print(open_advice(result))
