# Napisz grę ciepło - zimno tak, aby korzystać z funkcji.

def check_user_value(secret, user, previous_nearest):
    if abs(secret - user) < abs(previous_nearest):
        print('warm!')
        previous_nearest = abs(secret - user)
    else:
        print('cold!')

    return previous_nearest


secret_number = 5
nearest_guess = -100

while True:
    user_number = int(input("Give me your guess: "))
    if user_number == secret_number:
        break

    nearest_guess = check_user_value(secret_number, user_number, nearest_guess)


print('Congratulations - you guessed right!')