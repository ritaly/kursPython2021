# Poproś użytkownika o podanie liczby.
# Sprawdź czy liczba podana przez użytkownika jest podzielna przez 3 bez reszty
# i wyświetl komunikat “Twoja liczba jest podzielna przez 3”.

number = int(input('Podaj liczbe całkowitą: '))

if number % 3 == 0:
    print('Twoja liczba jest podzielna przez 3')
else:
    print('Nie jest podzielna')

# print("Twoja liczba jest podzielna przez 3" if number % 3 == 0 else "Nie jest podzielna")
