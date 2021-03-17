# Napisz grę ciepło - zimno tak, aby korzystać z funkcji.

def check_user_value(secret, user, previous):
    if abs(secret - user) < abs(previous):
        print('warm!')
        previous = abs(secret - user)
    else:
        print('cold!')

    return previous


secret_number = 5
previous_guess = -100

while True:
    user_number = int(input("Give me your guess: "))
    if user_number == secret_number:
        break

    previous_guess = check_user_value(secret_number, user_number, previous_guess)


print('Congratulations - you guessed right!')