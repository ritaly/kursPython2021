# Napisz program, który będzie sprawdzał, czy nasz samochód kwalifikuje się do zarejestrowania jako zabytek.
#
# Program zacznie ze stworzonym słownikiem o trzech kluczach:
# - marka (str)
# - model (str)
# - rocznik (int)
#
# Wypisze ten słownik na ekran (bez żadnego formatowania)
#
# Sprawdzi, czy samochód ma minimum 25 lat. Jeśli tak, wypisze komunikat:
# “Gratulacje! Twój samochód (tutaj_marka) może być zarejestrowany jako zabytek.”
#
# Jeśli nie spełnia powyższego warunku, wypisze komunikat:
# “Twój samochód (tutaj_marka) jest jeszcze zbyt młody.”
#
# Gdy program będzie poprawnie działał, pozmieniaj wartości słownika (ale nie klucze!), aby zobaczyć, czy progam również zmienia swoje zachowanie.

def check_is_old(age):
    if age >= 25:
        print('Wiek uprawniający do rejestracji zabytku')
    else:
        print('Samochód za młody na zabytek')

def check_is_orignal(value):
    if value:
        print('Samochód ma 75% oryginalnych czesci')
    else:
        print('Nie spełnia wymogu oryginalnych czesci')

def show_is_vintage(age, original):
    check_is_old(age)
    check_is_orignal(original)

def register_car(age, original):
    show_is_vintage(age, original)
    print('---------------------')
    if age >= 25 and original:
        print(f'Gratulacje! Zarejestrowano!')
    elif age < 25:
        print(f'Nie można zarejestrować. Twój samochód jest jeszcze zbyt młody na rejestracje jako zabytek.')
    elif not original:
        print(f'Nie można zarejestrować. Twój samochód nie ma 75% oryginalnych części')


car = {
    'brand': 'renault',
    'model': 'megan',
    'year': 1993,
    'orignal': True
}

print(car)

car_age = 2021 - car['year']
register_car(car_age, car['orignal'])

