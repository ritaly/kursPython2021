def uppercase_decorator(func):
    def nested_function():
        # txt = func()
        # txt = txt.upper()
        # return txt
        return func().upper()
    return nested_function


@uppercase_decorator
def lorem_generator():
    return 'lorem ipsum dolor sit amet'


print(lorem_generator())
