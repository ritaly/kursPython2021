def say_hello_decorator(func_param):

    def good_morning(): # funkcja lokalną
        print('Good morning')
        func_param()

    return good_morning


@say_hello_decorator
def small_talk():
    print('How are you today?')


# meeting = say_hello_decorator(small_talk) # good_morning
# meeting()

small_talk()