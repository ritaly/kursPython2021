def divide_by(number):
    number = float(number)
    return 10/number

if __name__ == '__main__':
    user_input = input('Give me a number -->')

    try:
        result = divide_by(user_input)
        print(result)
    except ValueError as e:
        print('This is not a number')
        print(e)
    except ZeroDivisionError as e:
        print("You can't divide by 0")
        print('Temp result:', 0)
        print(e)
    finally:
        print('Finally here!')