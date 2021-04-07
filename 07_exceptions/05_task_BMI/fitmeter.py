import bmi


def get_weight():
    question = 'Podaj wage w kg: '
    weight = ask_user(question, 30, 250)
    return weight


def get_height():
    return ask_user('Podaj wzrost w metrach: ', 1.5, 2.35)


def ask_user(question, minimum, maximum):
    while True:
        try:
            value = float(input(question))
        except (ValueError, TypeError):
            print('To nie jest prawidłowa wartość! Spróbuj jeszcze raz')
            continue

        if minimum < value < maximum:
            break
        else:
            print('Podana wartość jest nieprawdopodobna. Spróbuj jeszcze raz')

    return value

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
