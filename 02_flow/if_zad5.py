# Stwórz zmienną password.
# Hasło powinno składać z liter i cyfr, zwierać conajmniej 1 dużą literę i mieć długość conajmniej 8 znaków.
# Poinformuj użytkownika, jeśli wpisane hasło jest nie poprawne.
# Wyświetl różne komunikaty w zależności od rodzaju błędu.
password = input('Podaj hasło:')

length_correct = password >= 8
includes_letters_and_digits = password.isalnum() and not password.isdigit() and not password.isalpha()
at_list_one_capital_letter = not password.islower()

if not length_correct:
    print('Haslo jest za krotki, haslo musi miec min. 8 znaków')

if not includes_letters_and_digits:
    print('Haslo musi składać z liter i cyfr')

if not at_list_one_capital_letter:
    print('Hasło musi zwierać conajmniej 1 dużą literę')

# if len(password) < 8:
#     print('Hasło ma za mało znaków')
#
# if password.islower():
#     print('Hasło musi zawierać co najmniej jedną dużą litertę.')
#
# if password.isalpha():
#     print('Hasło musi zawierać cyfry.')
# elif password.isdigit():
#     print('Hasło musi zawierać litery')
# elif (not password.isalnum()):
#     print('Hasło nie może zawierać spacji ani znaków specjalnych')


